"""Crew-as-Node — the most strategic abstraction in this module.

Treat this file like a public API. It is the contract that lets every
Crew in the system slot into the LangGraph supervisor without bespoke
glue. If you change the shape here, every Crew breaks; bump the package
major and write an ADR.

The contract:
    1. A Crew is a thing (noun). It takes an InvoiceState in, returns
       a CrewKickoffResult out. It does not reach across business
       processes; it does not own checkpoints.
    2. A Crew node is the LangGraph adapter around a Crew. The node
       opens an OTel span, fires memory hooks, runs the Crew (sync
       internals wrapped via asyncio.to_thread), records a status
       transition, and returns the partial state update.
    3. Every Crew kickoff is a checkpoint boundary. State before kickoff,
       state after kickoff, no in-flight Crew survives a process restart.
       This is the deliberate constraint that makes recovery simple.
    4. Crews never call interrupt() directly. Crews recommend; the
       LangGraph supervisor decides between autonomous and human paths.
       Mixing decision authority is the most common architecture mistake.
"""

from __future__ import annotations

from collections.abc import Awaitable, Callable, Mapping
from dataclasses import dataclass
from typing import Any, Protocol, runtime_checkable

from pydantic import BaseModel, ConfigDict, Field

from putsch_orchestration.logging_setup import get_logger, set_correlation_id
from putsch_orchestration.memory_hooks import get_memory_hooks
from putsch_orchestration.obs_hooks import crew_span
from putsch_orchestration.state import (
    CrewError,
    InvoiceState,
    InvoiceStatus,
    OrchestrationError,
)

_log = get_logger(__name__)


class CrewKickoffResult(BaseModel):
    """The typed return of a Crew kickoff.

    `state_update` is the partial dict LangGraph merges into state. It is
    a *partial* — fields not present are not touched. This is what
    keeps the state object additive across nodes.

    `next_status` is the InvoiceStatus the Crew recommends. The supervisor
    can override (e.g. force EXCEPTION on a downstream failure), but in
    the absence of override, this is the transition the Crew records.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid")

    state_update: dict[str, Any] = Field(default_factory=dict)
    next_status: InvoiceStatus
    recommend_human_review: bool = False
    recommend_human_reason: str | None = None


@runtime_checkable
class CrewAsNode(Protocol):
    """Any Crew that wants to be a LangGraph node implements this."""

    name: str
    """Stable identifier — appears in spans, logs, ADRs."""

    async def kickoff(self, state: InvoiceState) -> CrewKickoffResult: ...


@dataclass(frozen=True)
class _NodeAdapter:
    """Internal adapter — turns a CrewAsNode into the async callable
    that LangGraph expects as a node function."""

    crew: CrewAsNode

    async def __call__(self, state: InvoiceState) -> dict[str, Any]:
        set_correlation_id(state.correlation_id)
        hooks = get_memory_hooks()
        log = _log.bind(crew=self.crew.name, correlation_id=state.correlation_id)
        log.info("crew.kickoff.start", status=state.status.value)

        async with crew_span(self.crew.name, state):
            await hooks.pre_crew(self.crew.name, state)
            try:
                result = await self.crew.kickoff(state)
            except CrewError as crew_err:
                # CrewError is a domain-level failure: the Crew said "I cannot
                # process this". Route to EXCEPTION instead of crashing the
                # graph — the workflow drains to finalize and ops follow up.
                log.warning(
                    "crew.kickoff.crew_error",
                    error=crew_err.message,
                )
                update = state.record_exception(
                    crew_err.message, actor=self.crew.name
                )
                projected = state.model_copy(update=update)
                await hooks.post_crew(self.crew.name, state, projected, update)
                return update
            except OrchestrationError:
                # NodeError / CheckpointError / etc. propagate — these are
                # infrastructure failures the graph-level retry policy should
                # handle, not domain exceptions.
                raise
            except Exception as exc:
                # Anything else gets wrapped as CrewError so we land in the
                # EXCEPTION path on the next invocation. We re-raise so the
                # current checkpoint preserves the pre-node state; LangGraph
                # surfaces the error to the caller without corrupting state.
                log.exception("crew.kickoff.unexpected")
                raise CrewError(
                    f"crew '{self.crew.name}' raised {type(exc).__name__}: {exc}",
                    correlation_id=state.correlation_id,
                ) from exc

            # Compose the partial update: the Crew's own update, plus the
            # transition the Crew recommends, plus any human-review signal.
            update = dict(result.state_update)
            transition = state.transition(
                result.next_status,
                actor=self.crew.name,
                note=result.recommend_human_reason,
            )
            update.update(transition)

            if result.recommend_human_review:
                update["requires_human"] = True
                update["exception_reasons"] = (
                    *state.exception_reasons,
                    result.recommend_human_reason or "crew_recommended_review",
                )

            # Reconstruct projected next state to fire post-hook with the
            # actual mutation (memory module will diff before/after).
            projected = state.model_copy(update=update)
            await hooks.post_crew(self.crew.name, state, projected, update)

            log.info(
                "crew.kickoff.done",
                next_status=result.next_status.value,
                recommend_human=result.recommend_human_review,
            )
            return update


def build_crew_node(
    crew: CrewAsNode,
) -> Callable[[InvoiceState], Awaitable[Mapping[str, Any]]]:
    """Wrap a Crew into the async callable LangGraph expects.

    Usage:
        ap_node = build_crew_node(APCrew())
        graph.add_node("extract", ap_node)
    """
    return _NodeAdapter(crew=crew)


__all__ = [
    "CrewAsNode",
    "CrewKickoffResult",
    "build_crew_node",
]
