"""LangGraph supervisor — the durable spine.

Topology:

    START -> ingest -> extract -> route_after_extract
        route_after_extract --(extracted)--> match
        route_after_extract --(exception)--> finalize
    match -> route_after_match
        route_after_match --(autonomous_ok)--> post
        route_after_match --(matched | partial | no_match)--> human_approval
        route_after_match --(exception)----> finalize
    human_approval (interrupt) -> route_after_approval
        route_after_approval --(approved)--> post
        route_after_approval --(rejected)--> finalize
    post -> finalize
    finalize -> END

Every node is async. Every edge condition is a typed function — no lambdas.
Every transition is checkpointed by PostgresSaver, so a process crash
between any two nodes resumes from the last persisted state.

The supervisor owns:
    - durable state (PostgresSaver)
    - retry policy at the node level (CrewError -> EXCEPTION; NodeError -> retry)
    - interrupt() for HITL
    - all decisions about who handles what (Sachbearbeiter vs auto-post)

The supervisor does NOT own:
    - LLM prompt mechanics (DSPy)
    - role-based team coordination (CrewAI)
    - external system retries (those are tool-level, in tools.py)
"""

from __future__ import annotations

import asyncio
import json
from collections.abc import Awaitable, Callable, Mapping
from contextlib import asynccontextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Literal

from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

from putsch_orchestration.config import Settings, get_settings
from putsch_orchestration.crews.ap.crew import APCrew
from putsch_orchestration.crews.node import build_crew_node
from putsch_orchestration.logging_setup import get_logger, set_correlation_id
from putsch_orchestration.memory_hooks import get_memory_hooks
from putsch_orchestration.obs_hooks import node_span
from putsch_orchestration.state import (
    CrewError,
    InvoiceState,
    InvoiceStatus,
    NodeError,
    PostingDecision,
    StatusEvent,
)

_log = get_logger(__name__)

# Route labels — used by conditional-edge functions; declared once so a
# typo trips the type checker, not a runtime KeyError.
RouteAfterExtract = Literal["match", "finalize"]
RouteAfterMatch = Literal["post", "human_approval", "finalize"]
RouteAfterApproval = Literal["post", "finalize"]


# --------------------------------------------------------------------------- #
# Nodes
# --------------------------------------------------------------------------- #


async def ingest_node(state: InvoiceState) -> dict[str, Any]:
    """Mark the invoice EXTRACTING and surface the source URI.

    This node exists for two reasons even though it does no LLM work:
    1. It is a checkpoint boundary — every workflow starts with one.
    2. It establishes correlation_id context for everything downstream.
    """
    set_correlation_id(state.correlation_id)
    hooks = get_memory_hooks()
    log = _log.bind(node="ingest", correlation_id=state.correlation_id)

    async with node_span("ingest", state):
        await hooks.pre_node("ingest", state)
        log.info("ingest.start", source_uri=state.source_uri)
        update = state.transition(InvoiceStatus.EXTRACTING, actor="ingest")
        projected = state.model_copy(update=update)
        await hooks.post_node("ingest", state, projected)
        return update


def make_extract_node(crew: APCrew) -> Callable[[InvoiceState], Awaitable[Mapping[str, Any]]]:
    """Build the extract node from an assembled AP Crew."""
    return build_crew_node(crew)


def make_match_node(crew: APCrew) -> Callable[[InvoiceState], Awaitable[Mapping[str, Any]]]:
    """Match node also wraps the AP Crew — the Crew dispatches on status.

    Wrapping the same Crew twice is intentional: the Crew is a *thing*
    that owns AP knowledge; the graph is a *process* that decides when to
    apply it. Two nodes can route through the same Crew at different
    phases without duplicating the Crew object.
    """
    return build_crew_node(crew)


def make_post_node(crew: APCrew) -> Callable[[InvoiceState], Awaitable[Mapping[str, Any]]]:
    return build_crew_node(crew)


async def human_approval_node(state: InvoiceState) -> Command[Any]:
    """HITL interrupt point.

    Publishes a structured payload to the Sachbearbeiter UI via
    interrupt(). When the human resumes (Command(resume={...})), we
    record their decision and route accordingly.

    Resume payload shape (validated below):
        {
            "decision": "approve" | "reject" | "escalate",
            "approver_id": str,
            "approver_role": "sachbearbeiter" | "abteilungsleiter" | "geschaeftsfuehrer",
            "rationale": str | None,
        }

    Days can pass between the interrupt and the resume — that's the
    point of LangGraph durability. The state carrying us out of this
    node must therefore be derived only from `state` and `decision`,
    not from process memory.
    """
    set_correlation_id(state.correlation_id)
    hooks = get_memory_hooks()
    log = _log.bind(node="human_approval", correlation_id=state.correlation_id)

    async with node_span("human_approval", state):
        await hooks.pre_node("human_approval", state)

        payload: dict[str, Any] = {
            "kind": "approval_request",
            "correlation_id": state.correlation_id,
            "invoice_number": state.invoice_number,
            "vendor": (
                {"kreditor_number": state.vendor.kreditor_number, "name": state.vendor.name}
                if state.vendor
                else None
            ),
            "total_amount_cents": (
                state.total_amount.amount_cents if state.total_amount else None
            ),
            "currency": state.total_amount.currency if state.total_amount else None,
            "match_outcome": (
                state.three_way_match.outcome.value if state.three_way_match else None
            ),
            "exception_reasons": list(state.exception_reasons),
        }

        # Record the interrupt payload onto state before the actual
        # interrupt() so a checkpoint exists with payload set — the UI
        # can read it without re-running the node.
        log.info("human_approval.interrupt", reason=state.exception_reasons)

        decision_payload = interrupt(payload)
        decision = _parse_approval_decision(decision_payload)

        approver_role = decision["approver_role"]
        approver_id = decision["approver_id"]
        outcome = decision["decision"]

        # Note is JSON so the downstream post-phase parses unambiguously
        # even when rationale contains spaces.
        event = StatusEvent(
            status=(
                InvoiceStatus.APPROVED if outcome == "approve" else InvoiceStatus.REJECTED
            ),
            actor="human_approval",
            note=json.dumps(
                {
                    "approver_id": approver_id,
                    "approver_role": approver_role,
                    "rationale": decision.get("rationale"),
                    "outcome": outcome,
                }
            ),
        )

        update: dict[str, Any] = {
            "interrupt_payload": None,
            "status": event.status,
            "history": (*state.history, event),
        }
        if outcome == "reject":
            update["posting_decision"] = PostingDecision(
                decision="reject",
                decided_by=approver_role,
                approver_id=approver_id,
                rationale=decision.get("rationale"),
                posted_at=datetime.now(timezone.utc),
            )
            update["requires_human"] = False

        projected = state.model_copy(update=update)
        await hooks.post_node("human_approval", state, projected)
        return Command(update=update)


async def finalize_node(state: InvoiceState) -> dict[str, Any]:
    """Terminal node: mark COMPLETED, FAILED, or leave at EXCEPTION."""
    set_correlation_id(state.correlation_id)
    hooks = get_memory_hooks()
    log = _log.bind(node="finalize", correlation_id=state.correlation_id)

    async with node_span("finalize", state):
        await hooks.pre_node("finalize", state)

        if state.status is InvoiceStatus.POSTED:
            update = state.transition(InvoiceStatus.COMPLETED, actor="finalize")
        elif state.status in {InvoiceStatus.REJECTED, InvoiceStatus.NO_MATCH}:
            update = state.transition(InvoiceStatus.FAILED, actor="finalize")
        elif state.status is InvoiceStatus.EXCEPTION:
            update = {}  # leave at EXCEPTION; ops process picks it up
        else:
            update = state.transition(
                InvoiceStatus.EXCEPTION,
                actor="finalize",
                note=f"unexpected terminal status: {state.status.value}",
            )

        projected = state.model_copy(update=update)
        await hooks.post_node("finalize", state, projected)
        log.info("finalize.done", status=projected.status.value)
        return update


# --------------------------------------------------------------------------- #
# Edge condition functions — typed, named, testable
# --------------------------------------------------------------------------- #


def route_after_extract(state: InvoiceState) -> RouteAfterExtract:
    if state.status is InvoiceStatus.EXTRACTED:
        return "match"
    return "finalize"


def route_after_match(state: InvoiceState) -> RouteAfterMatch:
    if state.status is InvoiceStatus.AUTONOMOUS_OK and not state.requires_human:
        return "post"
    if state.status in {
        InvoiceStatus.MATCHED,
        InvoiceStatus.PARTIAL_MATCH,
        InvoiceStatus.NO_MATCH,
    } and state.requires_human:
        return "human_approval"
    return "finalize"


def route_after_approval(state: InvoiceState) -> RouteAfterApproval:
    if state.status is InvoiceStatus.APPROVED:
        return "post"
    return "finalize"


# --------------------------------------------------------------------------- #
# Graph assembly
# --------------------------------------------------------------------------- #


@dataclass
class CompiledAPGraph:
    """The compiled graph + the checkpointer backing it.

    Kept together so callers can run a workflow and inspect the
    checkpointer for audit without re-deriving connection strings.
    """

    app: Any
    """langgraph.graph.state.CompiledStateGraph"""
    checkpointer: AsyncPostgresSaver
    ap_crew: APCrew

    async def aclose(self) -> None:
        await self.ap_crew.aclose()


def build_graph(
    *,
    ap_crew: APCrew,
    checkpointer: AsyncPostgresSaver,
    settings: Settings | None = None,  # noqa: ARG001
) -> Any:
    """Build the StateGraph without compiling. Compilation pulls in the
    checkpointer; tests sometimes want an uncompiled graph to introspect."""
    g = StateGraph(InvoiceState)
    g.add_node("ingest", ingest_node)
    g.add_node("extract", make_extract_node(ap_crew))
    g.add_node("match", make_match_node(ap_crew))
    g.add_node("post", make_post_node(ap_crew))
    g.add_node("human_approval", human_approval_node)
    g.add_node("finalize", finalize_node)

    g.add_edge(START, "ingest")
    g.add_edge("ingest", "extract")
    g.add_conditional_edges(
        "extract",
        route_after_extract,
        {"match": "match", "finalize": "finalize"},
    )
    g.add_conditional_edges(
        "match",
        route_after_match,
        {"post": "post", "human_approval": "human_approval", "finalize": "finalize"},
    )
    g.add_conditional_edges(
        "human_approval",
        route_after_approval,
        {"post": "post", "finalize": "finalize"},
    )
    g.add_edge("post", "finalize")
    g.add_edge("finalize", END)
    return g


@asynccontextmanager
async def compiled_graph(
    settings: Settings | None = None,
):
    """Async context manager that yields a ready-to-run CompiledAPGraph.

    Acquires:
        - the AP Crew (HTTP clients to MCP servers)
        - the AsyncPostgresSaver (DB connection pool)
    Releases:
        - both, in reverse order, on exit.

    Use this in `__main__`, in tests, and in the FastAPI startup hook
    that the workflow API module will eventually own.
    """
    s = settings or get_settings()
    async with AsyncPostgresSaver.from_conn_string(str(s.database_url)) as checkpointer:
        await checkpointer.setup()
        ap_crew = APCrew.assemble(s)
        try:
            graph = build_graph(ap_crew=ap_crew, checkpointer=checkpointer, settings=s)
            app = graph.compile(checkpointer=checkpointer)
            compiled = CompiledAPGraph(app=app, checkpointer=checkpointer, ap_crew=ap_crew)
            yield compiled
        finally:
            await ap_crew.aclose()


# --------------------------------------------------------------------------- #
# Resume payload validation
# --------------------------------------------------------------------------- #


def _parse_approval_decision(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, Mapping):
        raise NodeError("approval resume payload must be a dict")
    decision = payload.get("decision")
    approver_id = payload.get("approver_id")
    approver_role = payload.get("approver_role")
    if decision not in {"approve", "reject", "escalate"}:
        raise NodeError(f"invalid approval decision: {decision!r}")
    if not isinstance(approver_id, str) or not approver_id:
        raise NodeError("approver_id required")
    if approver_role not in {"sachbearbeiter", "abteilungsleiter", "geschaeftsfuehrer"}:
        raise NodeError(f"invalid approver_role: {approver_role!r}")
    rationale = payload.get("rationale")
    if rationale is not None and not isinstance(rationale, str):
        raise NodeError("rationale must be str or None")
    return {
        "decision": decision,
        "approver_id": approver_id,
        "approver_role": approver_role,
        "rationale": rationale,
    }


# Avoid unused-import false positives for symbols referenced only through types.
_ = (CrewError, asyncio, datetime)


__all__ = [
    "CompiledAPGraph",
    "build_graph",
    "compiled_graph",
    "finalize_node",
    "human_approval_node",
    "ingest_node",
    "make_extract_node",
    "make_match_node",
    "make_post_node",
    "route_after_approval",
    "route_after_extract",
    "route_after_match",
]
