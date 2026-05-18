"""Unit tests for state.py — invariants, transitions, exception types."""

from __future__ import annotations

from datetime import UTC, datetime
from decimal import Decimal

import pytest
from pydantic import ValidationError

from putsch_orchestration.state import (
    AgentMessage,
    CheckpointError,
    CrewError,
    IntakeChannel,
    InvoiceState,
    InvoiceStatus,
    LineItem,
    MatchOutcome,
    Money,
    NodeError,
    OrchestrationError,
    PostingDecision,
    StatusEvent,
    ThreeWayMatch,
    VendorRef,
)


class TestException:
    def test_hierarchy(self) -> None:
        assert issubclass(CrewError, OrchestrationError)
        assert issubclass(NodeError, OrchestrationError)
        assert issubclass(CheckpointError, OrchestrationError)

    def test_carries_correlation_id(self) -> None:
        err = CrewError("boom", correlation_id="01HNYZ8GZJKB6MGAZQQHEKQQ00")
        assert err.correlation_id == "01HNYZ8GZJKB6MGAZQQHEKQQ00"


class TestMoney:
    def test_from_decimal_rounds_to_minor_units(self) -> None:
        m = Money.from_decimal(Decimal("100.50"), "EUR")
        assert m.amount_cents == 10050
        assert m.currency == "EUR"

    def test_add_same_currency(self) -> None:
        a = Money(amount_cents=100, currency="EUR")
        b = Money(amount_cents=50, currency="EUR")
        assert (a + b).amount_cents == 150

    def test_add_different_currency_raises(self) -> None:
        a = Money(amount_cents=100, currency="EUR")
        b = Money(amount_cents=50, currency="USD")
        with pytest.raises(ValueError, match="Cannot add"):
            _ = a + b


class TestInvoiceStateInvariants:
    def test_requires_human_needs_reason(self) -> None:
        with pytest.raises(ValidationError):
            InvoiceState(
                thread_id="t1",
                intake_channel=IntakeChannel.EMAIL,
                source_uri="s3://x",
                requires_human=True,
                exception_reasons=(),
            )

    def test_posting_decision_requires_match(self) -> None:
        decision = PostingDecision(
            decision="post",
            datev_belegnummer="D-1",
            decided_by="autonomous",
            posted_at=datetime.now(UTC),
        )
        with pytest.raises(ValidationError):
            InvoiceState(
                thread_id="t1",
                intake_channel=IntakeChannel.EMAIL,
                source_uri="s3://x",
                status=InvoiceStatus.POSTED,
                posting_decision=decision,
                # three_way_match intentionally missing
            )

    def test_posting_decision_in_wrong_status(self) -> None:
        decision = PostingDecision(
            decision="post",
            datev_belegnummer="D-1",
            decided_by="autonomous",
            posted_at=datetime.now(UTC),
        )
        with pytest.raises(ValidationError):
            InvoiceState(
                thread_id="t1",
                intake_channel=IntakeChannel.EMAIL,
                source_uri="s3://x",
                status=InvoiceStatus.RECEIVED,
                posting_decision=decision,
                three_way_match=ThreeWayMatch(outcome=MatchOutcome.FULL),
            )

    def test_total_amount_matches_line_items(self) -> None:
        with pytest.raises(ValidationError, match="!= sum"):
            InvoiceState(
                thread_id="t1",
                intake_channel=IntakeChannel.EMAIL,
                source_uri="s3://x",
                line_items=(
                    LineItem(
                        line_number=1,
                        description="x",
                        quantity=Decimal("1"),
                        unit_price=Money(amount_cents=100, currency="EUR"),
                        line_total=Money(amount_cents=100, currency="EUR"),
                    ),
                ),
                total_amount=Money(amount_cents=999, currency="EUR"),
            )

    def test_currency_consistency(self) -> None:
        with pytest.raises(ValidationError, match="single currency"):
            InvoiceState(
                thread_id="t1",
                intake_channel=IntakeChannel.EMAIL,
                source_uri="s3://x",
                line_items=(
                    LineItem(
                        line_number=1,
                        description="a",
                        quantity=Decimal("1"),
                        unit_price=Money(amount_cents=100, currency="EUR"),
                        line_total=Money(amount_cents=100, currency="EUR"),
                    ),
                    LineItem(
                        line_number=2,
                        description="b",
                        quantity=Decimal("1"),
                        unit_price=Money(amount_cents=100, currency="USD"),
                        line_total=Money(amount_cents=100, currency="USD"),
                    ),
                ),
            )

    def test_interrupt_payload_only_when_awaiting(self) -> None:
        with pytest.raises(ValidationError, match="interrupt_payload"):
            InvoiceState(
                thread_id="t1",
                intake_channel=IntakeChannel.EMAIL,
                source_uri="s3://x",
                status=InvoiceStatus.EXTRACTED,
                interrupt_payload={"foo": "bar"},
            )

    def test_history_monotonic(self) -> None:
        early = StatusEvent(
            status=InvoiceStatus.RECEIVED,
            occurred_at=datetime(2026, 5, 1, tzinfo=UTC),
            actor="ingest",
        )
        late = StatusEvent(
            status=InvoiceStatus.EXTRACTED,
            occurred_at=datetime(2026, 4, 1, tzinfo=UTC),  # before `early`
            actor="ap",
        )
        with pytest.raises(ValidationError, match="ordered"):
            InvoiceState(
                thread_id="t1",
                intake_channel=IntakeChannel.EMAIL,
                source_uri="s3://x",
                history=(early, late),
            )


class TestPostingDecision:
    def test_human_decision_requires_approver(self) -> None:
        with pytest.raises(ValidationError, match="approver_id"):
            PostingDecision(
                decision="post",
                datev_belegnummer="D-1",
                decided_by="sachbearbeiter",
                posted_at=datetime.now(UTC),
            )

    def test_post_requires_belegnummer(self) -> None:
        with pytest.raises(ValidationError, match="datev_belegnummer"):
            PostingDecision(
                decision="post",
                decided_by="autonomous",
                posted_at=datetime.now(UTC),
            )


class TestTransitionHelper:
    def test_transition_appends_history(self) -> None:
        s = InvoiceState(
            thread_id="t1",
            intake_channel=IntakeChannel.EMAIL,
            source_uri="s3://x",
        )
        update = s.transition(InvoiceStatus.EXTRACTING, actor="ingest")
        assert update["status"] is InvoiceStatus.EXTRACTING
        assert len(update["history"]) == 1
        assert update["history"][0].actor == "ingest"

    def test_record_exception_sets_flags(self) -> None:
        s = InvoiceState(
            thread_id="t1",
            intake_channel=IntakeChannel.EMAIL,
            source_uri="s3://x",
        )
        update = s.record_exception("unknown vendor", actor="ap")
        assert update["requires_human"] is True
        assert "unknown vendor" in update["exception_reasons"]


class TestAgentMessage:
    def test_typed_envelope(self) -> None:
        msg = AgentMessage(
            correlation_id="01HNYZ8GZJKB6MGAZQQHEKQQ00",
            sender="ocr_agent",
            recipient="match_agent",
            payload={"po_number": "PO-1"},
        )
        assert msg.kind == "task"
        # Frozen
        with pytest.raises(ValidationError):
            msg.sender = "other"  # type: ignore[misc]


class TestVendorRef:
    def test_construction(self) -> None:
        v = VendorRef(kreditor_number="K-1", name="Foo GmbH")
        assert v.kreditor_number == "K-1"
        assert v.iban is None
