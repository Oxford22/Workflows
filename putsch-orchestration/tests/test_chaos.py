"""Chaos tests: kill the process mid-workflow, restart, verify resume.

Two flavors:
    1. In-memory simulation: drive the graph to a checkpoint, drop the
       compiled app object (simulating SIGKILL), rebuild from the same
       checkpointer, resume. Catches state-shape regressions cheaply.
    2. Postgres-backed (marked `slow`): same flow but with
       AsyncPostgresSaver. Requires docker-compose Postgres at the URL
       in PUTSCH_DATABASE_URL.

Pre-condition for flavor 2: PostgresSaver.setup() succeeded against a
clean schema. The fixture rolls back at exit.
"""

from __future__ import annotations

import os
from typing import Any

import pytest
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command

from putsch_orchestration.crews.ap.crew import APCrew
from putsch_orchestration.graph import build_graph
from putsch_orchestration.sanitize import TaintedText
from putsch_orchestration.state import IntakeChannel, InvoiceState, InvoiceStatus, MatchOutcome


pytestmark = pytest.mark.chaos


@pytest.fixture
def initial_state() -> InvoiceState:
    return InvoiceState(
        thread_id="01HRCHAOS0000000000000000",
        intake_channel=IntakeChannel.EMAIL,
        source_uri="s3://test/chaos.pdf",
        raw_text=TaintedText(
            value=(
                "Rechnung Nr. 2026-9999\n"
                "Datum: 18.05.2026\n"
                "Mustermann GmbH\n"
                "Position 1: Item — 1 Stk x 100,00 EUR = 100,00 EUR\n"
                "Gesamt: 119,00 EUR inkl. 19% USt"
            ),
            source="ocr",
        ),
    )


def _resume_payload() -> dict[str, Any]:
    return {
        "decision": "approve",
        "approver_id": "M-77",
        "approver_role": "sachbearbeiter",
        "rationale": "freigegeben nach Pruefung",
    }


async def test_resume_after_process_loss_with_memory_saver(
    ap_crew: APCrew,
    initial_state: InvoiceState,
    patched_dspy: dict[str, Any],
    _block_real_network: None,  # noqa: ARG001
) -> None:
    """Drive to the interrupt, drop the app, rebuild, resume."""
    patched_dspy["match"] = patched_dspy["match"].model_copy(
        update={"outcome": MatchOutcome.PARTIAL, "unmatched_line_numbers": (1,)}
    )

    saver = MemorySaver()
    graph_1 = build_graph(ap_crew=ap_crew, checkpointer=saver)  # type: ignore[arg-type]
    app_1 = graph_1.compile(checkpointer=saver)
    cfg = {"configurable": {"thread_id": initial_state.thread_id}}

    intermediate = await app_1.ainvoke(initial_state, config=cfg)
    # Either we hit __interrupt__, or we landed at PARTIAL_MATCH with
    # interrupt_payload set — both indicate the human-approval pause.
    assert intermediate.get("status") in {InvoiceStatus.PARTIAL_MATCH, None} or "__interrupt__" in intermediate

    # Simulate process loss: rebuild app from scratch against the SAME saver.
    del app_1, graph_1
    graph_2 = build_graph(ap_crew=ap_crew, checkpointer=saver)  # type: ignore[arg-type]
    app_2 = graph_2.compile(checkpointer=saver)

    # Resume.
    final = await app_2.ainvoke(Command(resume=_resume_payload()), config=cfg)
    assert final["status"] is InvoiceStatus.COMPLETED
    assert final["posting_decision"].decided_by == "sachbearbeiter"


@pytest.mark.slow
async def test_resume_with_postgres_saver(
    ap_crew: APCrew,
    initial_state: InvoiceState,
    patched_dspy: dict[str, Any],
    _block_real_network: None,  # noqa: ARG001
) -> None:
    """Same flow against AsyncPostgresSaver. Requires running docker-compose."""
    pytest.importorskip("langgraph.checkpoint.postgres.aio")
    from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver

    dsn = os.environ.get("PUTSCH_DATABASE_URL")
    if not dsn or "localhost" not in dsn:
        pytest.skip("PUTSCH_DATABASE_URL not pointing at a local DB; skipping")

    patched_dspy["match"] = patched_dspy["match"].model_copy(
        update={"outcome": MatchOutcome.PARTIAL, "unmatched_line_numbers": (1,)}
    )

    cfg = {"configurable": {"thread_id": initial_state.thread_id}}
    async with AsyncPostgresSaver.from_conn_string(dsn) as saver:
        await saver.setup()

        graph_1 = build_graph(ap_crew=ap_crew, checkpointer=saver)  # type: ignore[arg-type]
        app_1 = graph_1.compile(checkpointer=saver)
        await app_1.ainvoke(initial_state, config=cfg)
        del app_1, graph_1

        graph_2 = build_graph(ap_crew=ap_crew, checkpointer=saver)  # type: ignore[arg-type]
        app_2 = graph_2.compile(checkpointer=saver)
        final = await app_2.ainvoke(Command(resume=_resume_payload()), config=cfg)
        assert final["status"] is InvoiceStatus.COMPLETED
