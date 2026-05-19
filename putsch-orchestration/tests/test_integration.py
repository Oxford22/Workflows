"""End-to-end integration tests on the compiled graph.

These tests use `MemorySaver` instead of `PostgresSaver` so they run in
CI without a database. The chaos suite (test_chaos.py) exercises the
real PostgresSaver against the docker-compose Postgres.

Three scenarios:
    1. Clean match -> autonomous post -> COMPLETED.
    2. Partial match -> human approval -> approved -> POSTED -> COMPLETED.
    3. Unknown vendor -> EXCEPTION (terminal).
"""

from __future__ import annotations

from typing import Any

import pytest
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command

from putsch_orchestration.crews.ap.crew import APCrew
from putsch_orchestration.crews.ap.tools import KreditorLookupResult
from putsch_orchestration.graph import build_graph
from putsch_orchestration.sanitize import TaintedText
from putsch_orchestration.state import (
    IntakeChannel,
    InvoiceState,
    InvoiceStatus,
    MatchOutcome,
)


pytestmark = pytest.mark.integration


@pytest.fixture
def memory_app(ap_crew: APCrew) -> Any:
    saver = MemorySaver()
    graph = build_graph(ap_crew=ap_crew, checkpointer=saver)  # type: ignore[arg-type]
    return graph.compile(checkpointer=saver)


@pytest.fixture
def initial_state() -> InvoiceState:
    return InvoiceState(
        thread_id="01HRZ8GZJKB6MGAZQQHEKQQ001",
        intake_channel=IntakeChannel.EMAIL,
        source_uri="s3://test/clean.pdf",
        raw_text=TaintedText(
            value=(
                "Rechnung Nr. 2026-1001\n"
                "Datum: 18.05.2026\n"
                "Mustermann GmbH, Hagen\nUSt-ID: DE123456789\n"
                "Position 1: Stahlträger HEB-200 — 5 Stk x 100,00 EUR = 500,00 EUR\n"
                "Gesamt: 595,00 EUR inkl. 19% USt"
            ),
            source="ocr",
        ),
    )


async def test_clean_match_runs_to_completion(
    memory_app: Any,
    initial_state: InvoiceState,
    _block_real_network: None,  # noqa: ARG001
) -> None:
    final = await memory_app.ainvoke(
        initial_state,
        config={"configurable": {"thread_id": initial_state.thread_id}},
    )
    assert final["status"] is InvoiceStatus.COMPLETED
    assert final["posting_decision"].decision == "post"
    assert final["posting_decision"].decided_by == "autonomous"


async def test_partial_match_requires_human_approval(
    memory_app: Any,
    initial_state: InvoiceState,
    patched_dspy: dict[str, Any],
    _block_real_network: None,  # noqa: ARG001
) -> None:
    patched_dspy["match"] = patched_dspy["match"].model_copy(
        update={
            "outcome": MatchOutcome.PARTIAL,
            "matched_line_numbers": (1,),
            "unmatched_line_numbers": (2,),
            "price_variance_cents": 250,
        }
    )

    cfg = {"configurable": {"thread_id": initial_state.thread_id}}
    intermediate = await memory_app.ainvoke(initial_state, config=cfg)
    # The graph paused at human_approval — interrupt() surfaces as a
    # special return whose shape includes __interrupt__ entries.
    assert "__interrupt__" in intermediate or intermediate.get("status") is InvoiceStatus.PARTIAL_MATCH

    # Resume with an approval.
    final = await memory_app.ainvoke(
        Command(
            resume={
                "decision": "approve",
                "approver_id": "M-42",
                "approver_role": "sachbearbeiter",
                "rationale": "manuelle Pruefung der Position 2 ok",
            }
        ),
        config=cfg,
    )
    assert final["status"] is InvoiceStatus.COMPLETED
    assert final["posting_decision"].decided_by == "sachbearbeiter"
    assert final["posting_decision"].approver_id == "M-42"


async def test_rejection_path(
    memory_app: Any,
    initial_state: InvoiceState,
    patched_dspy: dict[str, Any],
    _block_real_network: None,  # noqa: ARG001
) -> None:
    patched_dspy["match"] = patched_dspy["match"].model_copy(
        update={
            "outcome": MatchOutcome.PARTIAL,
            "matched_line_numbers": (1,),
            "unmatched_line_numbers": (2,),
            "price_variance_cents": 5000,
        }
    )
    cfg = {"configurable": {"thread_id": initial_state.thread_id}}
    await memory_app.ainvoke(initial_state, config=cfg)
    final = await memory_app.ainvoke(
        Command(
            resume={
                "decision": "reject",
                "approver_id": "M-99",
                "approver_role": "abteilungsleiter",
                "rationale": "Preisabweichung zu hoch",
            }
        ),
        config=cfg,
    )
    assert final["status"] is InvoiceStatus.FAILED
    assert final["posting_decision"].decision == "reject"


async def test_unknown_vendor_routes_to_exception(
    memory_app: Any,
    initial_state: InvoiceState,
    mock_toolset: Any,
    _block_real_network: None,  # noqa: ARG001
) -> None:
    mock_toolset.lookup_kreditor.return_value = KreditorLookupResult(found=False)
    cfg = {"configurable": {"thread_id": initial_state.thread_id}}
    final = await memory_app.ainvoke(initial_state, config=cfg)
    assert final["status"] is InvoiceStatus.EXCEPTION
    assert final["requires_human"] is True
    assert any("kreditor" in r for r in final["exception_reasons"])
