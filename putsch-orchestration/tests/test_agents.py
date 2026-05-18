"""Unit tests for the AP Crew agents and the Crew-as-Node adapter.

Strategy:
    - LLM calls are mocked at the DSPy boundary (patched_dspy fixture).
    - MCP tools are mocked at the APToolset boundary (mock_toolset fixture).
    - Real network and real LiteLLM calls are forbidden by the
      _block_real_network fixture activated per test.
"""

from __future__ import annotations

from typing import Any

import pytest

from putsch_orchestration.crews.ap.crew import APCrew
from putsch_orchestration.crews.ap.tools import (
    DATEVPostResult,
    KreditorLookupResult,
    POLookupResult,
)
from putsch_orchestration.crews.node import CrewKickoffResult, build_crew_node
from putsch_orchestration.state import (
    CrewError,
    InvoiceState,
    InvoiceStatus,
    MatchOutcome,
)


class TestExtractPhase:
    async def test_clean_extract(
        self,
        ap_crew: APCrew,
        fresh_state: InvoiceState,
        _block_real_network: None,  # noqa: ARG002
    ) -> None:
        result = await ap_crew.kickoff(fresh_state)
        assert isinstance(result, CrewKickoffResult)
        assert result.next_status is InvoiceStatus.EXTRACTED
        assert result.recommend_human_review is False
        assert result.state_update["invoice_number"] == "2026-1001"
        assert result.state_update["vendor"].kreditor_number == "K-100001"

    async def test_intake_not_an_invoice_routes_to_exception(
        self,
        ap_crew: APCrew,
        fresh_state: InvoiceState,
        patched_dspy: dict[str, Any],
        _block_real_network: None,  # noqa: ARG002
    ) -> None:
        patched_dspy["intake"] = patched_dspy["intake"].model_copy(
            update={"document_kind": "mahnung", "confidence": 0.92}
        )
        # Need to re-patch the runner — patched_dspy fixture overrode it via
        # closure-bound lambda; updating the dict is enough because lambdas
        # read at call time.
        result = await ap_crew.kickoff(fresh_state)
        assert result.next_status is InvoiceStatus.EXCEPTION
        assert result.recommend_human_review is True
        assert "mahnung" in (result.recommend_human_reason or "")

    async def test_low_ocr_confidence_routes_to_exception(
        self,
        ap_crew: APCrew,
        fresh_state: InvoiceState,
        patched_dspy: dict[str, Any],
        _block_real_network: None,  # noqa: ARG002
    ) -> None:
        patched_dspy["ocr"] = patched_dspy["ocr"].model_copy(update={"confidence": 0.4})
        result = await ap_crew.kickoff(fresh_state)
        assert result.next_status is InvoiceStatus.EXCEPTION
        assert result.recommend_human_review is True
        assert "confidence" in (result.recommend_human_reason or "").lower()

    async def test_unknown_vendor_routes_to_exception(
        self,
        ap_crew: APCrew,
        fresh_state: InvoiceState,
        mock_toolset: Any,
        _block_real_network: None,  # noqa: ARG002
    ) -> None:
        mock_toolset.lookup_kreditor.return_value = KreditorLookupResult(found=False)
        result = await ap_crew.kickoff(fresh_state)
        assert result.next_status is InvoiceStatus.EXCEPTION
        assert "unknown kreditor" in (result.recommend_human_reason or "")

    async def test_missing_raw_text_raises_crew_error(
        self,
        ap_crew: APCrew,
        fresh_state: InvoiceState,
        _block_real_network: None,  # noqa: ARG002
    ) -> None:
        bare = fresh_state.model_copy(update={"raw_text": None})
        with pytest.raises(CrewError, match="no raw_text"):
            await ap_crew.kickoff(bare)


class TestMatchPhase:
    async def test_full_match_under_threshold_auto_posts(
        self,
        ap_crew: APCrew,
        fresh_state: InvoiceState,
        _block_real_network: None,  # noqa: ARG002
    ) -> None:
        extracted = await ap_crew.kickoff(fresh_state)
        next_state = fresh_state.model_copy(update=extracted.state_update).model_copy(
            update={"status": InvoiceStatus.EXTRACTED}
        )
        result = await ap_crew.kickoff(next_state)
        assert result.next_status is InvoiceStatus.AUTONOMOUS_OK
        assert result.recommend_human_review is False
        tw = result.state_update["three_way_match"]
        assert tw.outcome is MatchOutcome.FULL

    async def test_full_match_over_threshold_requires_human(
        self,
        ap_crew: APCrew,
        fresh_state: InvoiceState,
        patched_dspy: dict[str, Any],  # noqa: ARG002
        monkeypatch: pytest.MonkeyPatch,
        _block_real_network: None,  # noqa: ARG002
    ) -> None:
        monkeypatch.setattr(ap_crew._settings, "autonomous_post_threshold_cents", 100)
        extracted = await ap_crew.kickoff(fresh_state)
        next_state = fresh_state.model_copy(update=extracted.state_update).model_copy(
            update={"status": InvoiceStatus.EXTRACTED}
        )
        result = await ap_crew.kickoff(next_state)
        assert result.next_status is InvoiceStatus.MATCHED
        assert result.recommend_human_review is True
        assert "threshold" in (result.recommend_human_reason or "")

    async def test_no_po_routes_to_no_match(
        self,
        ap_crew: APCrew,
        fresh_state: InvoiceState,
        mock_toolset: Any,
        _block_real_network: None,  # noqa: ARG002
    ) -> None:
        extracted = await ap_crew.kickoff(fresh_state)
        next_state = fresh_state.model_copy(update=extracted.state_update).model_copy(
            update={"status": InvoiceStatus.EXTRACTED}
        )
        mock_toolset.lookup_po_by_vendor_and_invoice.return_value = POLookupResult(found=False)
        result = await ap_crew.kickoff(next_state)
        assert result.next_status is InvoiceStatus.NO_MATCH
        assert result.recommend_human_review is True

    async def test_partial_match_routes_to_human(
        self,
        ap_crew: APCrew,
        fresh_state: InvoiceState,
        patched_dspy: dict[str, Any],
        _block_real_network: None,  # noqa: ARG002
    ) -> None:
        extracted = await ap_crew.kickoff(fresh_state)
        next_state = fresh_state.model_copy(update=extracted.state_update).model_copy(
            update={"status": InvoiceStatus.EXTRACTED}
        )
        patched_dspy["match"] = patched_dspy["match"].model_copy(
            update={
                "outcome": MatchOutcome.PARTIAL,
                "matched_line_numbers": (1,),
                "unmatched_line_numbers": (2,),
                "price_variance_cents": 250,
            }
        )
        result = await ap_crew.kickoff(next_state)
        assert result.next_status is InvoiceStatus.PARTIAL_MATCH
        assert result.recommend_human_review is True


class TestPostPhase:
    async def test_post_writes_posting_decision(
        self,
        ap_crew: APCrew,
        fresh_state: InvoiceState,
        _block_real_network: None,  # noqa: ARG002
    ) -> None:
        # Drive state through extract + match first.
        extracted = await ap_crew.kickoff(fresh_state)
        s1 = fresh_state.model_copy(update=extracted.state_update).model_copy(
            update={"status": InvoiceStatus.EXTRACTED}
        )
        matched = await ap_crew.kickoff(s1)
        s2 = s1.model_copy(update=matched.state_update).model_copy(
            update={"status": InvoiceStatus.AUTONOMOUS_OK}
        )
        result = await ap_crew.kickoff(s2)
        assert result.next_status is InvoiceStatus.POSTED
        decision = result.state_update["posting_decision"]
        assert decision.decision == "post"
        assert decision.datev_belegnummer == "DATEV-9001"
        assert decision.decided_by == "autonomous"

    async def test_post_failure_routes_to_exception(
        self,
        ap_crew: APCrew,
        fresh_state: InvoiceState,
        mock_toolset: Any,
        _block_real_network: None,  # noqa: ARG002
    ) -> None:
        extracted = await ap_crew.kickoff(fresh_state)
        s1 = fresh_state.model_copy(update=extracted.state_update).model_copy(
            update={"status": InvoiceStatus.EXTRACTED}
        )
        matched = await ap_crew.kickoff(s1)
        s2 = s1.model_copy(update=matched.state_update).model_copy(
            update={"status": InvoiceStatus.AUTONOMOUS_OK}
        )
        mock_toolset.submit_posting.return_value = DATEVPostResult(
            success=False, error_code="DATEV-409", error_message="duplicate idempotency key"
        )
        result = await ap_crew.kickoff(s2)
        assert result.next_status is InvoiceStatus.EXCEPTION
        assert "datev posting failed" in (result.recommend_human_reason or "")


class TestCrewAsNode:
    async def test_node_adapter_records_transition_and_invokes_hooks(
        self,
        ap_crew: APCrew,
        fresh_state: InvoiceState,
        _block_real_network: None,  # noqa: ARG002
    ) -> None:
        node = build_crew_node(ap_crew)
        update = await node(fresh_state)
        assert update["status"] is InvoiceStatus.EXTRACTED
        assert isinstance(update["history"], tuple)
        assert update["history"][-1].actor == "ap"

    async def test_node_adapter_wraps_unexpected_exception(
        self,
        ap_crew: APCrew,
        fresh_state: InvoiceState,
        monkeypatch: pytest.MonkeyPatch,
        _block_real_network: None,  # noqa: ARG002
    ) -> None:
        async def boom(_self: APCrew, _state: InvoiceState) -> CrewKickoffResult:
            raise RuntimeError("unexpected")

        monkeypatch.setattr(APCrew, "kickoff", boom)
        node = build_crew_node(ap_crew)
        with pytest.raises(CrewError, match="RuntimeError"):
            await node(fresh_state)
