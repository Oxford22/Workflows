"""Memory hooks — the seam where Zep + Graphiti will plug in.

This module ships with a no-op default implementation that exposes the
exact protocol the memory module will fulfill. Every Crew kickoff and
every LangGraph node passes through `pre_*` and `post_*` hooks. The
no-op records correlation IDs to structlog so we can verify hook
placement under integration tests today, before the memory module exists.

Contract for the future Zep+Graphiti implementation:

    Read path (pre-hook):
        async def pre_crew(state) -> MemoryContext: ...
        async def pre_node(node_name, state) -> MemoryContext: ...
    The MemoryContext object will carry retrieved facts/entities the
    agent reasoning step is expected to fold into its prompt. Today
    MemoryContext is empty.

    Write path (post-hook):
        async def post_crew(state_before, state_after, result) -> None
        async def post_node(node_name, state_before, state_after) -> None
    Writes derive facts (kreditor entity, posting decisions, exception
    reasons) and append them to Graphiti's temporal graph. Today this
    is a no-op log line.

Two reasons to define the no-op interface now instead of waiting:
    1. Every call site that needs hooks gets them on first commit. The
       memory module ships by swapping `MemoryHooks` implementation;
       no call sites move.
    2. The shape of MemoryContext is part of the orchestration contract
       — the memory module fulfills *our* API, not the other way around.

Trust-boundary contract for implementers (ADR-002):

    The memory write path is one of the most dangerous sinks in the
    system. Anything written to Graphiti facts or Zep session memory
    is later re-ingested by agent reasoning steps — an injection
    persisted here becomes an injection that fires on every later
    invoice from the same vendor. Sanitize-on-write is therefore
    mandatory in `post_crew` and `post_node` implementations: every
    tainted string passing into the memory backend MUST go through
    `putsch_orchestration.sanitize.strip_instruction_patterns()`
    first. The no-op implementation below performs no writes, but the
    contract is the same: the real implementation must not violate it.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Mapping
from dataclasses import dataclass, field
from typing import Any

from putsch_orchestration.logging_setup import get_logger
from putsch_orchestration.state import InvoiceState

_log = get_logger(__name__)


@dataclass(frozen=True)
class MemoryContext:
    """Facts and entities retrieved from memory ahead of agent reasoning.

    Today this is empty. The memory module will populate:
        facts          tuple[Fact, ...]      — temporally-scoped Graphiti facts
        entities       Mapping[str, dict]    — Kreditor / Sachkonto entities
        prior_decisions tuple[dict, ...]     — earlier postings against same PO
    """

    facts: tuple[Any, ...] = field(default_factory=tuple)
    entities: Mapping[str, Any] = field(default_factory=dict)
    prior_decisions: tuple[Mapping[str, Any], ...] = field(default_factory=tuple)


class MemoryHooks(ABC):
    """The protocol the memory module fulfills.

    Async because every implementation will eventually do network I/O
    (Zep API call, Graphiti graph query). Returning fast paths is
    fine when memory is empty or disabled.
    """

    @abstractmethod
    async def pre_crew(self, crew_name: str, state: InvoiceState) -> MemoryContext: ...

    @abstractmethod
    async def post_crew(
        self,
        crew_name: str,
        state_before: InvoiceState,
        state_after: InvoiceState,
        result: Mapping[str, Any],
    ) -> None: ...

    @abstractmethod
    async def pre_node(self, node_name: str, state: InvoiceState) -> MemoryContext: ...

    @abstractmethod
    async def post_node(
        self, node_name: str, state_before: InvoiceState, state_after: InvoiceState
    ) -> None: ...


class NoopMemoryHooks(MemoryHooks):
    """Default implementation. Records the hook fired and returns empty context.

    Acceptable for local dev and CI. NOT acceptable in production once the
    memory module is integrated — the call sites here must surface
    `MemoryContext` into the agent prompts."""

    async def pre_crew(self, crew_name: str, state: InvoiceState) -> MemoryContext:
        _log.debug("memory.pre_crew", crew=crew_name, correlation_id=state.correlation_id)
        return MemoryContext()

    async def post_crew(
        self,
        crew_name: str,
        state_before: InvoiceState,
        state_after: InvoiceState,
        result: Mapping[str, Any],  # noqa: ARG002
    ) -> None:
        _log.debug(
            "memory.post_crew",
            crew=crew_name,
            correlation_id=state_after.correlation_id,
            status_before=state_before.status.value,
            status_after=state_after.status.value,
        )

    async def pre_node(self, node_name: str, state: InvoiceState) -> MemoryContext:
        _log.debug("memory.pre_node", node=node_name, correlation_id=state.correlation_id)
        return MemoryContext()

    async def post_node(
        self, node_name: str, state_before: InvoiceState, state_after: InvoiceState
    ) -> None:
        _log.debug(
            "memory.post_node",
            node=node_name,
            correlation_id=state_after.correlation_id,
            status_before=state_before.status.value,
            status_after=state_after.status.value,
        )


_hooks: MemoryHooks = NoopMemoryHooks()


def get_memory_hooks() -> MemoryHooks:
    return _hooks


def set_memory_hooks(hooks: MemoryHooks) -> None:
    """Swap the active hooks. Called by the memory module on import."""
    global _hooks
    _hooks = hooks


__all__ = [
    "MemoryContext",
    "MemoryHooks",
    "NoopMemoryHooks",
    "get_memory_hooks",
    "set_memory_hooks",
]
