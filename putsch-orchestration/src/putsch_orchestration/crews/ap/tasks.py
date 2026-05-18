"""Typed Task definitions for the AP Crew.

Every CrewAI Task in this Crew has a Pydantic input schema and a Pydantic
output schema. Code never passes raw strings between agents. The LLM
still sees a rendered string prompt, but the wire format between Python
code is structured.

The pattern:
    1. A Task subclass declares its `Input` and `Output` Pydantic models.
    2. The Crew assembly builds `crewai.Task` instances by serializing
       the input model into the description and parsing the output model
       from the agent's structured response (CrewAI supports
       `output_pydantic` natively as of v1.9).
    3. Agents read `task.context.input_model` to type-check, never
       `task.context.raw_string`.

This is what keeps the Crew composable with the rest of the stack:
LangGraph state -> Pydantic Input -> Task -> Pydantic Output -> state update.
"""

from __future__ import annotations

from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from putsch_orchestration.state import (
    LineItem,
    MatchOutcome,
    Money,
    VendorRef,
)


# --------------------------------------------------------------------------- #
# Eingangs-Agent
# --------------------------------------------------------------------------- #


class IntakeInput(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    source_uri: str
    intake_channel: Literal["email", "belege_online", "upload"]
    raw_text_excerpt: str = Field(..., max_length=4000)
    sender_hint: str = ""


class IntakeOutput(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    document_kind: Literal[
        "eingangsrechnung", "bestellbestaetigung", "mahnung", "gutschrift", "sonstiges"
    ]
    vendor_name_guess: str
    confidence: float = Field(..., ge=0.0, le=1.0)
    reasoning: str


# --------------------------------------------------------------------------- #
# OCR-Agent
# --------------------------------------------------------------------------- #


class OCRInput(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    invoice_text: str
    intake_hint: str = ""


class OCRLineItem(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    line_number: int
    description: str
    quantity: Decimal
    unit_price_eur: Decimal
    line_total_eur: Decimal
    tax_rate_pct: Decimal = Decimal("19")


class OCROutput(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    invoice_number: str
    invoice_date_iso: str
    vendor_name: str
    vendor_ust_id: str = ""
    total_amount_eur: Decimal
    currency: str = "EUR"
    line_items: tuple[OCRLineItem, ...]
    confidence: float = Field(..., ge=0.0, le=1.0)
    extraction_notes: str = ""

    def to_state_fragment(self) -> dict[str, object]:
        """Convert into partial-state fields ready for the graph update."""
        return {
            "invoice_number": self.invoice_number,
            "vendor": VendorRef(
                kreditor_number="UNKNOWN",  # filled after kreditor lookup
                name=self.vendor_name,
                ust_id=self.vendor_ust_id or None,
            ),
            "total_amount": Money.from_decimal(self.total_amount_eur, self.currency),
            "line_items": tuple(
                LineItem(
                    line_number=li.line_number,
                    description=li.description,
                    quantity=li.quantity,
                    unit_price=Money.from_decimal(li.unit_price_eur, self.currency),
                    line_total=Money.from_decimal(li.line_total_eur, self.currency),
                    tax_rate_pct=li.tax_rate_pct,
                )
                for li in self.line_items
            ),
        }


# --------------------------------------------------------------------------- #
# Match-Agent
# --------------------------------------------------------------------------- #


class MatchInput(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    invoice_number: str
    kreditor_number: str
    line_items: tuple[OCRLineItem, ...]
    total_amount_eur: Decimal
    currency: str
    tolerance_cents: int = 100  # 1 EUR per line


class MatchOutput(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    outcome: MatchOutcome
    po_number: str | None = None
    wareneingang_numbers: tuple[str, ...] = ()
    matched_line_numbers: tuple[int, ...] = ()
    unmatched_line_numbers: tuple[int, ...] = ()
    price_variance_cents: int = 0
    rationale: str = ""


# --------------------------------------------------------------------------- #
# Buchungs-Agent
# --------------------------------------------------------------------------- #


class PostingInput(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    invoice_number: str
    kreditor_number: str
    vendor_name: str
    invoice_date_iso: str
    total_amount_cents: int
    currency: str
    line_items: tuple[OCRLineItem, ...]
    primary_kostenstelle: str = ""
    idempotency_key: str
    """Same as the invoice correlation_id — DATEV uses this to dedupe."""


class PostingOutput(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    success: bool
    datev_belegnummer: str | None = None
    buchungstext: str = ""
    error_code: str | None = None
    error_message: str | None = None


__all__ = [
    "IntakeInput",
    "IntakeOutput",
    "MatchInput",
    "MatchOutput",
    "OCRInput",
    "OCRLineItem",
    "OCROutput",
    "PostingInput",
    "PostingOutput",
]
