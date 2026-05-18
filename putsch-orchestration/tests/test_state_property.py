"""Property-based tests on InvoiceState.

Goal: no combination of valid field assignments produces an invalid
state, and no invalid combination passes validation. Hypothesis runs
several hundred randomly-generated cases per property.
"""

from __future__ import annotations

from datetime import UTC, datetime
from decimal import Decimal
from typing import Any

import pytest
from hypothesis import given, settings
from hypothesis import strategies as st
from pydantic import ValidationError

from putsch_orchestration.state import (
    IntakeChannel,
    InvoiceState,
    InvoiceStatus,
    LineItem,
    Money,
    PostingDecision,
    ThreeWayMatch,
    VendorRef,
    new_correlation_id,
)
from putsch_orchestration.state import MatchOutcome


def _line_items_strategy(currency: str = "EUR") -> st.SearchStrategy[tuple[LineItem, ...]]:
    return st.lists(
        st.builds(
            lambda i, desc, qty, price_cents: LineItem(
                line_number=i + 1,
                description=desc,
                quantity=Decimal(qty),
                unit_price=Money(amount_cents=price_cents, currency=currency),
                line_total=Money(amount_cents=price_cents * qty, currency=currency),
            ),
            i=st.integers(min_value=0, max_value=10),
            desc=st.text(min_size=1, max_size=20),
            qty=st.integers(min_value=1, max_value=100),
            price_cents=st.integers(min_value=1, max_value=100_000),
        ),
        min_size=0,
        max_size=5,
    ).map(tuple)


@settings(max_examples=200, deadline=None)
@given(intake=st.sampled_from(list(IntakeChannel)), uri=st.text(min_size=1, max_size=64))
def test_blank_state_always_valid(intake: IntakeChannel, uri: str) -> None:
    s = InvoiceState(thread_id=new_correlation_id(), intake_channel=intake, source_uri=uri)
    assert s.status is InvoiceStatus.RECEIVED
    assert s.requires_human is False


@settings(max_examples=100, deadline=None)
@given(items=_line_items_strategy())
def test_line_items_sum_property(items: tuple[LineItem, ...]) -> None:
    if not items:
        InvoiceState(
            thread_id=new_correlation_id(),
            intake_channel=IntakeChannel.EMAIL,
            source_uri="s3://x",
        )
        return
    summed = sum(li.line_total.amount_cents for li in items)
    # Correct total -> valid.
    InvoiceState(
        thread_id=new_correlation_id(),
        intake_channel=IntakeChannel.EMAIL,
        source_uri="s3://x",
        line_items=items,
        total_amount=Money(amount_cents=summed, currency="EUR"),
    )
    # Wrong total (off by more than 1 cent) -> invalid.
    with pytest.raises(ValidationError):
        InvoiceState(
            thread_id=new_correlation_id(),
            intake_channel=IntakeChannel.EMAIL,
            source_uri="s3://x",
            line_items=items,
            total_amount=Money(amount_cents=summed + 5, currency="EUR"),
        )


@settings(max_examples=80, deadline=None)
@given(
    status=st.sampled_from(
        [
            InvoiceStatus.RECEIVED,
            InvoiceStatus.EXTRACTING,
            InvoiceStatus.EXTRACTED,
            InvoiceStatus.MATCHING,
            InvoiceStatus.PARTIAL_MATCH,
            InvoiceStatus.NO_MATCH,
            InvoiceStatus.AWAITING_APPROVAL,
            InvoiceStatus.EXCEPTION,
        ]
    )
)
def test_posting_decision_forbidden_in_non_decision_states(status: InvoiceStatus) -> None:
    decision = PostingDecision(
        decision="post",
        datev_belegnummer="D-1",
        decided_by="autonomous",
        posted_at=datetime.now(UTC),
    )
    extra: dict[str, Any] = {"three_way_match": ThreeWayMatch(outcome=MatchOutcome.FULL)}
    if status is InvoiceStatus.AWAITING_APPROVAL:
        extra["interrupt_payload"] = {"x": "y"}
        extra["requires_human"] = True
        extra["exception_reasons"] = ("threshold",)
    with pytest.raises(ValidationError):
        InvoiceState(
            thread_id=new_correlation_id(),
            intake_channel=IntakeChannel.EMAIL,
            source_uri="s3://x",
            status=status,
            posting_decision=decision,
            **extra,
        )


@settings(max_examples=50, deadline=None)
@given(
    reasons=st.lists(st.text(min_size=1, max_size=40), min_size=0, max_size=4).map(tuple),
)
def test_requires_human_iff_reasons(reasons: tuple[str, ...]) -> None:
    if reasons:
        # requires_human can be either; no constraint when reasons exist.
        for rh in (True, False):
            InvoiceState(
                thread_id=new_correlation_id(),
                intake_channel=IntakeChannel.EMAIL,
                source_uri="s3://x",
                requires_human=rh,
                exception_reasons=reasons,
            )
    else:
        # No reasons + requires_human=True must fail.
        with pytest.raises(ValidationError):
            InvoiceState(
                thread_id=new_correlation_id(),
                intake_channel=IntakeChannel.EMAIL,
                source_uri="s3://x",
                requires_human=True,
                exception_reasons=(),
            )


def test_roundtrip_through_json() -> None:
    s = InvoiceState(
        thread_id="01HNYZ8GZJKB6MGAZQQHEKQQ00",
        intake_channel=IntakeChannel.BELEGE_ONLINE,
        source_uri="s3://x/y.pdf",
        invoice_number="R-1",
        vendor=VendorRef(kreditor_number="K-1", name="Foo GmbH"),
    )
    blob = s.model_dump_json()
    reconstructed = InvoiceState.model_validate_json(blob)
    assert reconstructed == s
