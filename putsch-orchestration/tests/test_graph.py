"""Unit tests for the graph: edge conditions, node compositions, interrupt
machinery. Integration tests (real Postgres, end-to-end) live in
test_integration.py."""

from __future__ import annotations

import pytest

from putsch_orchestration.graph import (
    _parse_approval_decision,
    finalize_node,
    ingest_node,
    route_after_approval,
    route_after_extract,
    route_after_match,
)
from putsch_orchestration.state import (
    IntakeChannel,
    InvoiceState,
    InvoiceStatus,
    NodeError,
)


def _state(
    status: InvoiceStatus = InvoiceStatus.RECEIVED,
    *,
    requires_human: bool = False,
    exception_reasons: tuple[str, ...] = (),
) -> InvoiceState:
    return InvoiceState(
        thread_id="t",
        intake_channel=IntakeChannel.EMAIL,
        source_uri="s3://x",
        status=status,
        requires_human=requires_human,
        exception_reasons=exception_reasons,
    )


class TestRouting:
    def test_after_extract_extracted_to_match(self) -> None:
        assert route_after_extract(_state(InvoiceStatus.EXTRACTED)) == "match"

    def test_after_extract_exception_to_finalize(self) -> None:
        assert (
            route_after_extract(
                _state(
                    InvoiceStatus.EXCEPTION,
                    requires_human=True,
                    exception_reasons=("x",),
                )
            )
            == "finalize"
        )

    def test_after_match_autonomous(self) -> None:
        assert route_after_match(_state(InvoiceStatus.AUTONOMOUS_OK)) == "post"

    def test_after_match_partial_to_human(self) -> None:
        s = _state(
            InvoiceStatus.PARTIAL_MATCH,
            requires_human=True,
            exception_reasons=("partial",),
        )
        assert route_after_match(s) == "human_approval"

    def test_after_match_matched_threshold_to_human(self) -> None:
        s = _state(
            InvoiceStatus.MATCHED,
            requires_human=True,
            exception_reasons=("threshold",),
        )
        assert route_after_match(s) == "human_approval"

    def test_after_match_exception_to_finalize(self) -> None:
        s = _state(
            InvoiceStatus.EXCEPTION,
            requires_human=True,
            exception_reasons=("x",),
        )
        assert route_after_match(s) == "finalize"

    def test_after_approval_approved(self) -> None:
        assert route_after_approval(_state(InvoiceStatus.APPROVED)) == "post"

    def test_after_approval_rejected(self) -> None:
        assert route_after_approval(_state(InvoiceStatus.REJECTED)) == "finalize"


class TestNodes:
    async def test_ingest_transitions_to_extracting(self) -> None:
        s = _state()
        update = await ingest_node(s)
        assert update["status"] is InvoiceStatus.EXTRACTING
        assert update["history"][-1].actor == "ingest"

    async def test_finalize_from_posted_to_completed(self) -> None:
        s = _state(InvoiceStatus.POSTED)
        update = await finalize_node(s)
        assert update["status"] is InvoiceStatus.COMPLETED

    async def test_finalize_from_rejected_to_failed(self) -> None:
        s = _state(InvoiceStatus.REJECTED)
        update = await finalize_node(s)
        assert update["status"] is InvoiceStatus.FAILED

    async def test_finalize_from_exception_keeps_status(self) -> None:
        s = _state(
            InvoiceStatus.EXCEPTION,
            requires_human=True,
            exception_reasons=("x",),
        )
        update = await finalize_node(s)
        assert update == {}


class TestApprovalPayloadValidation:
    def test_valid_payload(self) -> None:
        parsed = _parse_approval_decision(
            {
                "decision": "approve",
                "approver_id": "M-123",
                "approver_role": "sachbearbeiter",
                "rationale": "looks good",
            }
        )
        assert parsed["decision"] == "approve"

    def test_invalid_decision(self) -> None:
        with pytest.raises(NodeError, match="invalid approval decision"):
            _parse_approval_decision(
                {"decision": "maybe", "approver_id": "M-1", "approver_role": "sachbearbeiter"}
            )

    def test_missing_approver(self) -> None:
        with pytest.raises(NodeError, match="approver_id"):
            _parse_approval_decision(
                {"decision": "approve", "approver_id": "", "approver_role": "sachbearbeiter"}
            )

    def test_invalid_role(self) -> None:
        with pytest.raises(NodeError, match="approver_role"):
            _parse_approval_decision(
                {"decision": "approve", "approver_id": "M-1", "approver_role": "ceo"}
            )

    def test_non_mapping(self) -> None:
        with pytest.raises(NodeError, match="must be a dict"):
            _parse_approval_decision("ok")
