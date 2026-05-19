"""Core domain types for the AP (Eingangsrechnung) orchestration spine.

Glossary (canonical — every other module must use these terms):
    Eingangsrechnung   Incoming supplier invoice; the document that triggers
                      Accounts Payable processing.
    Belege online      DATEV's document-exchange portal; Putsch's external
                      invoice intake channel alongside email.
    Wareneingang       Goods receipt; the SAP MM document confirming physical
                      receipt of ordered material against a purchase order.
    Bestellung / PO    Purchase order; the SAP MM document committing Putsch
                      to a supplier for a specified quantity and price.
    Drei-Wege-Abgleich Three-way match: invoice <-> PO <-> Wareneingang. The
                      core control for AP automation.
    Kreditor           Vendor / supplier; the master-data record an invoice
                      posts against in SAP FI and DATEV.
    Sachkonto          G/L account; where the invoice line items book to.
    Kostenstelle       Cost center; the controlling assignment that scopes
                      who pays.
    Buchung            Posting; the act of writing a debit/credit pair into
                      the books.
    Sachbearbeiter     AP clerk; the human approver for HITL exceptions.
    Freigabe           Approval; the act of authorizing a posting.
    DATEV              Putsch's accounting backend; receives postings via
                      the DATEV-MCP server.

Invariants enforced by Pydantic validators on InvoiceState:
    1. status transitions are append-only: history grows monotonically.
    2. PostingDecision can only be set when status is APPROVED or
       AUTONOMOUS_OK (not from RECEIVED, EXCEPTION, etc.).
    3. requires_human flag implies a non-empty exception_reasons list.
    4. total_amount_cents matches sum of line items when both populated.
    5. correlation_id is set at construction and never mutated.
"""

from __future__ import annotations

import enum
from collections.abc import Mapping
from datetime import UTC, datetime
from decimal import Decimal
from typing import Annotated, Any, Literal, Self
from uuid import UUID

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    StringConstraints,
    field_validator,
    model_validator,
)
from ulid import ULID

from putsch_orchestration.sanitize import TaintedText

# --------------------------------------------------------------------------- #
# Identifiers
# --------------------------------------------------------------------------- #

CorrelationId = Annotated[
    str,
    StringConstraints(min_length=26, max_length=26, pattern=r"^[0-9A-HJKMNP-TV-Z]{26}$"),
]
"""ULID — sortable by creation time, safe in logs, fits in a Postgres uuid column."""


def new_correlation_id() -> CorrelationId:
    """Mint a fresh correlation ID. Deterministic only via test seeding."""
    return str(ULID())


# --------------------------------------------------------------------------- #
# Exceptions
# --------------------------------------------------------------------------- #


class OrchestrationError(Exception):
    """Base for every error raised from this package.

    Catch this at process boundaries; never at API boundaries. A bare
    `except Exception` in user code is a code-review smell — string-matching
    on error messages is grounds for rejection in this codebase.
    """

    def __init__(self, message: str, *, correlation_id: str | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.correlation_id = correlation_id


class CrewError(OrchestrationError):
    """Raised when a CrewAI Crew kickoff fails in a way that cannot be
    recovered inside the Crew (manager-agent could not route, all specialists
    failed, etc.). The LangGraph node converts this into a state transition
    to EXCEPTION; it is not retried at the node level."""


class NodeError(OrchestrationError):
    """Raised when a LangGraph node fails for infrastructure reasons
    (checkpointer unavailable, tool circuit open, model provider returned
    a non-retryable error). Distinct from CrewError so the supervisor can
    decide between 'route to human' (CrewError) and 'retry the node'
    (NodeError)."""


class CheckpointError(OrchestrationError):
    """Raised when state could not be persisted or resumed. Almost always
    fatal to the current run — the durability guarantee is broken."""


class InterruptError(OrchestrationError):
    """Raised when an interrupt() resume payload is malformed or arrives
    against a thread whose state has been garbage-collected. Tracked
    separately because the failure mode is "human gave the wrong answer
    days later," not "code is broken right now"."""


class ToolError(OrchestrationError):
    """Raised by MCP-backed tools when an external system rejects a call
    in a way the agent could plausibly recover from (retryable: SAP busy,
    DATEV rate-limited, email server timeout). Distinct from NodeError
    because retry policy lives in the tool wrapper, not the graph."""


class ConfigurationError(OrchestrationError):
    """Raised at startup when configuration is invalid. Prefer crashing
    early over running with bad config — the cost of a crashed pod is
    cheaper than a wrong DATEV posting."""


# --------------------------------------------------------------------------- #
# Domain enums
# --------------------------------------------------------------------------- #


class InvoiceStatus(str, enum.Enum):
    """Lifecycle states for an Eingangsrechnung.

    The transition diagram (graph.py enforces these — Pydantic only
    prevents impossible *combinations*, not impossible *transitions*):

        RECEIVED -> EXTRACTING -> EXTRACTED -> MATCHING -> ...
            -> MATCHED -> AUTONOMOUS_OK -> POSTED -> COMPLETED
            -> PARTIAL_MATCH -> AWAITING_APPROVAL -> APPROVED -> POSTED
            -> NO_MATCH       -> AWAITING_APPROVAL -> REJECTED -> FAILED
            -> any state      -> EXCEPTION (terminal, ops follow-up)
    """

    RECEIVED = "received"
    EXTRACTING = "extracting"
    EXTRACTED = "extracted"
    MATCHING = "matching"
    MATCHED = "matched"
    PARTIAL_MATCH = "partial_match"
    NO_MATCH = "no_match"
    AUTONOMOUS_OK = "autonomous_ok"
    AWAITING_APPROVAL = "awaiting_approval"
    APPROVED = "approved"
    REJECTED = "rejected"
    POSTED = "posted"
    COMPLETED = "completed"
    FAILED = "failed"
    EXCEPTION = "exception"


class MatchOutcome(str, enum.Enum):
    """Result of Drei-Wege-Abgleich."""

    FULL = "full"
    """Invoice, PO, and Wareneingang agree within tolerance on all line items."""
    PARTIAL = "partial"
    """At least one line item matches; at least one disagrees."""
    NONE = "none"
    """No PO found, or PO found but every line disagrees."""
    UNKNOWN_VENDOR = "unknown_vendor"
    """Kreditor lookup failed — cannot even start matching."""


class IntakeChannel(str, enum.Enum):
    EMAIL = "email"
    BELEGE_ONLINE = "belege_online"
    UPLOAD = "upload"


# --------------------------------------------------------------------------- #
# Value objects
# --------------------------------------------------------------------------- #


class Money(BaseModel):
    """Money as integer minor units + ISO 4217 code.

    We never use float for money. Decimal is acceptable at API boundaries
    (DATEV serializes that way) but the in-graph representation is always
    integer minor units to make additions associative and equality decidable.
    """

    model_config = ConfigDict(frozen=True, extra="forbid")

    amount_cents: int = Field(..., description="Amount in minor currency units (e.g. cents).")
    currency: Annotated[str, StringConstraints(min_length=3, max_length=3, pattern=r"^[A-Z]{3}$")]

    @classmethod
    def from_decimal(cls, value: Decimal, currency: str = "EUR") -> Self:
        return cls(amount_cents=int((value * 100).to_integral_value()), currency=currency)

    def to_decimal(self) -> Decimal:
        return Decimal(self.amount_cents) / Decimal(100)

    def __add__(self, other: Money) -> Money:
        if self.currency != other.currency:
            raise ValueError(f"Cannot add {self.currency} and {other.currency}")
        return Money(amount_cents=self.amount_cents + other.amount_cents, currency=self.currency)


class LineItem(BaseModel):
    """A single line on the Eingangsrechnung.

    `po_line_ref` is None when the Match-Agent could not assign this line
    to a PO line — the most common cause of PARTIAL_MATCH.
    """

    model_config = ConfigDict(frozen=True, extra="forbid")

    line_number: int = Field(..., ge=1)
    description: str
    quantity: Decimal
    unit_price: Money
    line_total: Money
    sachkonto: str | None = Field(
        default=None,
        description="G/L account this line books to. Filled by Match-Agent.",
    )
    kostenstelle: str | None = Field(
        default=None,
        description="Cost center. Inherited from PO line; nullable for free-form invoices.",
    )
    po_line_ref: str | None = Field(
        default=None,
        description="SAP MM PO line key in the form '{po_number}/{line_number}'.",
    )
    tax_rate_pct: Decimal = Field(default=Decimal("19"), ge=0, le=100)


class VendorRef(BaseModel):
    """Reference to a Kreditor record. Populated after Stammdaten lookup."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    kreditor_number: str = Field(..., description="SAP Kreditor master-data number.")
    name: str
    ust_id: str | None = Field(default=None, description="VAT ID — required for EU cross-border.")
    iban: str | None = Field(default=None, description="Used only at posting time; never logged.")


class ThreeWayMatch(BaseModel):
    """Outcome of Drei-Wege-Abgleich. Produced by Match-Agent, consumed by
    the supervisor's routing function."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    outcome: MatchOutcome
    po_number: str | None = None
    wareneingang_numbers: tuple[str, ...] = Field(default_factory=tuple)
    matched_lines: tuple[int, ...] = Field(default_factory=tuple)
    unmatched_lines: tuple[int, ...] = Field(default_factory=tuple)
    price_variance_cents: int = Field(
        default=0,
        description="Absolute difference between invoice total and PO total in minor units.",
    )
    notes: str | None = None


class PostingDecision(BaseModel):
    """A Buchung committed to (or rejected from) DATEV.

    Once written, this field is the durable record of what the system did.
    Audit replay re-derives it from earlier state; equality is the
    determinism check."""

    model_config = ConfigDict(frozen=True, extra="forbid")

    decision: Literal["post", "reject", "hold"]
    datev_belegnummer: str | None = Field(
        default=None,
        description="DATEV document number assigned on successful posting.",
    )
    posted_at: datetime | None = None
    decided_by: Literal["autonomous", "sachbearbeiter", "abteilungsleiter", "geschaeftsfuehrer"]
    approver_id: str | None = Field(
        default=None,
        description="Mitarbeiter-ID of the approving human; required when decided_by != autonomous.",
    )
    rationale: str | None = None

    @model_validator(mode="after")
    def _approver_required_for_human_decisions(self) -> Self:
        if self.decided_by != "autonomous" and not self.approver_id:
            raise ValueError("approver_id required when a human made the decision")
        if self.decision == "post" and not self.datev_belegnummer:
            raise ValueError("datev_belegnummer required when decision is 'post'")
        return self


# --------------------------------------------------------------------------- #
# Agent message envelope
# --------------------------------------------------------------------------- #


class AgentMessage(BaseModel):
    """Typed envelope for inter-agent communication.

    Code paths that pass dicts between agents are not allowed in this
    codebase. Every message a Crew specialist receives or emits is an
    AgentMessage with a Pydantic payload — the LLM sees a structured
    prompt rendered from `payload`; the orchestrator sees a typed object.
    """

    model_config = ConfigDict(frozen=True, extra="forbid")

    message_id: UUID = Field(default_factory=lambda: ULID().to_uuid(), repr=False)
    correlation_id: CorrelationId
    sender: str = Field(..., description="Agent role identifier, e.g. 'ocr_agent'.")
    recipient: str = Field(..., description="Agent role identifier or 'broadcast'.")
    kind: Literal["task", "result", "exception", "interrupt"] = "task"
    payload: Mapping[str, Any]
    """Pydantic-serializable payload. The concrete schema is defined per
    sender/recipient pair in `crews/ap/tasks.py`."""
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(UTC))


# --------------------------------------------------------------------------- #
# Status history entry — immutable audit trail
# --------------------------------------------------------------------------- #


class StatusEvent(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")

    status: InvoiceStatus
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    actor: str = Field(..., description="Which node or agent wrote this transition.")
    note: str | None = None


# --------------------------------------------------------------------------- #
# The state object (this is the LangGraph TypedState)
# --------------------------------------------------------------------------- #


class InvoiceState(BaseModel):
    """The state object threaded through every LangGraph node.

    Mutability model: LangGraph nodes return *partial updates* (a dict of
    fields to overwrite). We expose update helpers below to keep call sites
    typed instead of dict-shaped. The state object itself is immutable per
    convention — never mutate in place; always return a new dict.

    Persistence: PostgresSaver serializes this to JSON on every node exit.
    Anything inside it must round-trip through model_dump_json / model_validate_json.
    """

    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        ser_json_timedelta="iso8601",
    )

    # --- Identity ---
    correlation_id: CorrelationId = Field(default_factory=new_correlation_id)
    thread_id: str = Field(
        ...,
        description=(
            "LangGraph thread id; equal to correlation_id for new invoices, "
            "different when one invoice spawns sub-workflows."
        ),
    )

    # --- Intake ---
    intake_channel: IntakeChannel
    received_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    source_uri: str = Field(..., description="S3 URI or email message-id of the original document.")

    # --- OCR / extraction ---
    raw_text: TaintedText | None = None
    """Full OCR text. Carries `source="ocr"` provenance — must be unwrapped
    via `.wrap_for_prompt()` or `wrap_external_content()` before reaching any
    LLM prompt. Not logged when config.log_invoice_content=False (default).
    See ADR-002 for the trust-boundary policy."""
    invoice_number: str | None = None
    invoice_date: datetime | None = None
    vendor: VendorRef | None = None
    line_items: tuple[LineItem, ...] = Field(default_factory=tuple)
    total_amount: Money | None = None

    # --- Matching ---
    three_way_match: ThreeWayMatch | None = None

    # --- Decision / posting ---
    posting_decision: PostingDecision | None = None

    # --- Control flow ---
    status: InvoiceStatus = InvoiceStatus.RECEIVED
    history: tuple[StatusEvent, ...] = Field(default_factory=tuple)
    requires_human: bool = False
    exception_reasons: tuple[str, ...] = Field(default_factory=tuple)
    interrupt_payload: Mapping[str, Any] | None = Field(
        default=None,
        description=(
            "Payload published to interrupt() — the Sachbearbeiter UI reads this. "
            "Cleared on resume."
        ),
    )

    # --- Retry bookkeeping ---
    retry_count: int = Field(default=0, ge=0, le=10)

    # --- Validators ---

    @field_validator("history")
    @classmethod
    def _history_is_monotonic(cls, value: tuple[StatusEvent, ...]) -> tuple[StatusEvent, ...]:
        for prev, curr in zip(value, value[1:], strict=False):
            if curr.occurred_at < prev.occurred_at:
                raise ValueError("history must be ordered by occurred_at")
        return value

    @model_validator(mode="after")
    def _invariants(self) -> Self:
        # Invariant 3: requires_human implies non-empty exception_reasons.
        if self.requires_human and not self.exception_reasons:
            raise ValueError("requires_human=True requires at least one exception_reason")

        # Line items must always share a single currency, independent of
        # whether total_amount is populated yet (matching only makes sense
        # against a single currency).
        if self.line_items:
            currencies = {li.line_total.currency for li in self.line_items}
            if len(currencies) > 1:
                raise ValueError("line_items must share a single currency")

            # Invariant 4: total_amount agrees with line items if total set.
            if self.total_amount is not None:
                if currencies.pop() != self.total_amount.currency:
                    raise ValueError(
                        "total_amount.currency must match line_items currency"
                    )
                summed = sum(li.line_total.amount_cents for li in self.line_items)
                # Allow 1 cent rounding tolerance (Steuerrundung).
                if abs(summed - self.total_amount.amount_cents) > 1:
                    raise ValueError(
                        f"total_amount {self.total_amount.amount_cents}c "
                        f"!= sum(line_items) {summed}c"
                    )

        # Invariant 2: PostingDecision only in approved terminal-ish states.
        if self.posting_decision is not None and self.status not in {
            InvoiceStatus.AUTONOMOUS_OK,
            InvoiceStatus.APPROVED,
            InvoiceStatus.POSTED,
            InvoiceStatus.COMPLETED,
            InvoiceStatus.REJECTED,
            InvoiceStatus.FAILED,
        }:
            raise ValueError(
                f"posting_decision incompatible with status {self.status.value}; "
                "decisions are recorded only after a routing outcome is reached"
            )

        # Three-way match is required before any posting decision.
        if self.posting_decision is not None and self.three_way_match is None:
            raise ValueError("posting_decision requires a recorded three_way_match")

        # interrupt_payload only valid while AWAITING_APPROVAL.
        if (
            self.interrupt_payload is not None
            and self.status is not InvoiceStatus.AWAITING_APPROVAL
        ):
            raise ValueError("interrupt_payload only valid while AWAITING_APPROVAL")

        return self

    # --- Convenience updates (used by nodes; always return a partial dict) ---

    def transition(
        self,
        status: InvoiceStatus,
        *,
        actor: str,
        note: str | None = None,
    ) -> dict[str, Any]:
        """Return the partial update dict that records a status transition.

        Usage in a node:
            return state.transition(InvoiceStatus.EXTRACTED, actor="ap_crew")
        """
        event = StatusEvent(status=status, actor=actor, note=note)
        return {"status": status, "history": (*self.history, event)}

    def record_exception(self, reason: str, *, actor: str) -> dict[str, Any]:
        return {
            **self.transition(InvoiceStatus.EXCEPTION, actor=actor, note=reason),
            "requires_human": True,
            "exception_reasons": (*self.exception_reasons, reason),
        }


__all__ = [
    "AgentMessage",
    "CheckpointError",
    "ConfigurationError",
    "CorrelationId",
    "CrewError",
    "IntakeChannel",
    "InterruptError",
    "InvoiceState",
    "InvoiceStatus",
    "LineItem",
    "MatchOutcome",
    "Money",
    "NodeError",
    "OrchestrationError",
    "PostingDecision",
    "StatusEvent",
    "TaintedText",
    "ThreeWayMatch",
    "ToolError",
    "VendorRef",
    "new_correlation_id",
]
