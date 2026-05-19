"""AP Crew assembly + the async kickoff that satisfies CrewAsNode.

This is where the deliberate constraints land:

    1. The Crew kickoff is the unit of work that gets a checkpoint
       boundary in the LangGraph supervisor. The Crew itself does not
       checkpoint mid-flight. If the process dies inside `kickoff()`,
       recovery re-runs from the last node boundary.

    2. The orchestration *inside* the Crew uses DSPy modules under the
       hood for the actual LLM work. CrewAI's hierarchical process
       manages role coordination; DSPy manages prompts. We do not use
       CrewAI's prompt templating layer.

    3. Decision authority is split:
            APCrew.kickoff returns a CrewKickoffResult with a
            recommendation (next_status, recommend_human_review).
       The LangGraph supervisor turns recommendations into transitions
       and decides escalation. The Crew never calls interrupt().

    4. CrewAI is synchronous internally. We wrap each blocking module
       call in `asyncio.to_thread`. That keeps the event loop responsive
       and lets the supervisor cancel a stuck kickoff via the standard
       cancellation pathway.
"""

from __future__ import annotations

import asyncio
import json
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Any

import dspy

from putsch_orchestration.config import Settings, get_settings
from putsch_orchestration.crews.ap.agents import APAgents, build_ap_agents
from putsch_orchestration.crews.ap.signatures import (
    ClassifyIntake,
    ComposePostingCommentary,
    ExtractInvoiceFields,
    ReasonOverMatch,
    all_signature_hashes,
)
from putsch_orchestration.crews.ap.tasks import (
    IntakeOutput,
    MatchInput,
    MatchOutput,
    OCRInput,
    OCRLineItem,
    OCROutput,
    PostingInput,
    PostingOutput,
)
from putsch_orchestration.crews.ap.tools import (
    APToolset,
    DATEVPosting,
    build_ap_toolset,
)
from putsch_orchestration.crews.node import CrewKickoffResult
from putsch_orchestration.logging_setup import get_logger
from putsch_orchestration.models import AgentRole, resolve_model
from putsch_orchestration.sanitize import wrap_external_content
from putsch_orchestration.state import (
    CrewError,
    InvoiceState,
    InvoiceStatus,
    MatchOutcome,
    Money,
    PostingDecision,
    ThreeWayMatch,
    VendorRef,
)

_log = get_logger(__name__)


def _configure_dspy_lm(settings: Settings) -> None:
    """Configure DSPy's default LM to use our LiteLLM proxy.

    DSPy modules created later in this module pick up the configured LM
    on first call. We configure once per APCrew instance; nothing here
    is shared cross-process.
    """
    handle = resolve_model(AgentRole.MANAGER_AGENT, settings)
    dspy.settings.configure(
        lm=dspy.LM(
            model=handle.model,
            api_base=handle.api_base,
            api_key=handle.api_key,
        )
    )


@dataclass
class APCrew:
    """The AP Crew packaged as a CrewAsNode.

    Construct once per process; reuse across invoices. The CrewAI Agent
    instances are stateful in their internal scratchpads but
    `kickoff` resets them per call.
    """

    name: str = "ap"
    toolset: APToolset | None = None
    agents: APAgents | None = None
    _settings: Settings | None = None
    _dspy_configured: bool = False

    @classmethod
    def assemble(cls, settings: Settings | None = None) -> "APCrew":
        s = settings or get_settings()
        toolset = build_ap_toolset(s)
        agents = build_ap_agents(toolset=toolset, settings=s)
        crew = cls(toolset=toolset, agents=agents, _settings=s)
        crew._ensure_dspy()
        _log.info(
            "ap_crew.assembled",
            signature_hashes=all_signature_hashes(),
        )
        return crew

    def _ensure_dspy(self) -> None:
        if not self._dspy_configured:
            _configure_dspy_lm(self._settings or get_settings())
            self._dspy_configured = True

    async def aclose(self) -> None:
        if self.toolset is not None:
            await self.toolset.aclose()

    # --------------------------------------------------------------------- #
    # The CrewAsNode contract entrypoint
    # --------------------------------------------------------------------- #

    async def kickoff(self, state: InvoiceState) -> CrewKickoffResult:
        if self.toolset is None or self.agents is None:
            raise CrewError(
                "APCrew not assembled; call APCrew.assemble() first",
                correlation_id=state.correlation_id,
            )

        log = _log.bind(correlation_id=state.correlation_id, crew=self.name)
        try:
            # Dispatch on current status. This is intentional — the Crew can
            # be re-entered from EXTRACTING, MATCHING, or AUTONOMOUS_OK
            # without the supervisor needing to know which phase.
            if state.status in {InvoiceStatus.RECEIVED, InvoiceStatus.EXTRACTING}:
                return await self._phase_extract(state)
            if state.status in {InvoiceStatus.EXTRACTED, InvoiceStatus.MATCHING}:
                return await self._phase_match(state)
            if state.status in {InvoiceStatus.AUTONOMOUS_OK, InvoiceStatus.APPROVED}:
                return await self._phase_post(state)

            raise CrewError(
                f"APCrew received state with non-actionable status {state.status.value}",
                correlation_id=state.correlation_id,
            )
        except CrewError:
            raise
        except Exception as exc:
            log.exception("ap_crew.kickoff.error")
            raise CrewError(
                f"APCrew kickoff raised {type(exc).__name__}",
                correlation_id=state.correlation_id,
            ) from exc

    # --------------------------------------------------------------------- #
    # Phases
    # --------------------------------------------------------------------- #

    async def _phase_extract(self, state: InvoiceState) -> CrewKickoffResult:
        """Eingangs- + OCR-Agent. Produces OCROutput and folds into state."""
        if state.raw_text is None:
            raise CrewError(
                "no raw_text on state; intake pipeline must run first",
                correlation_id=state.correlation_id,
            )

        # Intake classification. `raw_text` is TaintedText; we pass the
        # underlying value and let the runner wrap it in <external_content>
        # before it reaches the LM.
        intake = await asyncio.to_thread(
            _run_classify_intake,
            document_text=state.raw_text.value[:4000],
            sender_hint=state.source_uri,
        )
        if intake.document_kind != "eingangsrechnung":
            return CrewKickoffResult(
                state_update={},
                next_status=InvoiceStatus.EXCEPTION,
                recommend_human_review=True,
                recommend_human_reason=(
                    f"intake classified as {intake.document_kind} "
                    f"(confidence={intake.confidence:.2f}): {intake.reasoning}"
                ),
            )

        # OCR extraction. raw_text.value is the tainted string; runner wraps.
        ocr_out = await asyncio.to_thread(
            _run_extract_fields,
            invoice_text=state.raw_text.value,
            intake_hint=intake.vendor_name_guess,
        )
        if ocr_out.confidence < 0.7:
            return CrewKickoffResult(
                state_update={},
                next_status=InvoiceStatus.EXCEPTION,
                recommend_human_review=True,
                recommend_human_reason=(
                    f"ocr confidence {ocr_out.confidence:.2f} below 0.70: "
                    f"{ocr_out.extraction_notes}"
                ),
            )

        # Kreditor lookup — wire the parsed name to a real Kreditor number.
        kreditor = await self._lookup_kreditor(state.correlation_id, ocr_out)
        if not kreditor.found:
            return CrewKickoffResult(
                state_update={},
                next_status=InvoiceStatus.EXCEPTION,
                recommend_human_review=True,
                recommend_human_reason=(
                    f"unknown kreditor: name='{ocr_out.vendor_name}' "
                    f"ust_id='{ocr_out.vendor_ust_id or '-'}'"
                ),
            )

        update = ocr_out.to_state_fragment()
        # Replace placeholder VendorRef with the looked-up Kreditor.
        existing_vendor = update["vendor"]
        assert isinstance(existing_vendor, VendorRef)
        update["vendor"] = VendorRef(
            kreditor_number=kreditor.kreditor_number or "UNKNOWN",
            name=kreditor.name or existing_vendor.name,
            ust_id=kreditor.ust_id or existing_vendor.ust_id,
            iban=kreditor.iban,
        )
        update["invoice_date"] = _parse_iso_date(ocr_out.invoice_date_iso)

        return CrewKickoffResult(
            state_update=update,
            next_status=InvoiceStatus.EXTRACTED,
        )

    async def _phase_match(self, state: InvoiceState) -> CrewKickoffResult:
        """Match-Agent. Produces ThreeWayMatch and recommends transition."""
        if state.vendor is None or state.total_amount is None or not state.line_items:
            raise CrewError(
                "phase_match called before extraction populated vendor/lines",
                correlation_id=state.correlation_id,
            )
        assert self.toolset is not None

        po = await self.toolset.lookup_po_by_vendor_and_invoice(
            kreditor_number=state.vendor.kreditor_number,
            invoice_number=state.invoice_number or "",
            correlation_id=state.correlation_id,
        )
        if not po.found:
            return CrewKickoffResult(
                state_update={
                    "three_way_match": ThreeWayMatch(
                        outcome=MatchOutcome.NONE,
                        rationale="no PO found for invoice number / Kreditor pair",
                    )
                },
                next_status=InvoiceStatus.NO_MATCH,
                recommend_human_review=True,
                recommend_human_reason="three_way_match: no PO found",
            )

        wareneingang = await self.toolset.lookup_wareneingang(
            po_number=po.po_number or "",
            correlation_id=state.correlation_id,
        )

        # Stage inputs for DSPy reasoning.
        match_input = MatchInput(
            invoice_number=state.invoice_number or "",
            kreditor_number=state.vendor.kreditor_number,
            line_items=tuple(
                OCRLineItem(
                    line_number=li.line_number,
                    description=li.description,
                    quantity=li.quantity,
                    unit_price_eur=li.unit_price.to_decimal(),
                    line_total_eur=li.line_total.to_decimal(),
                    tax_rate_pct=li.tax_rate_pct,
                )
                for li in state.line_items
            ),
            total_amount_eur=state.total_amount.to_decimal(),
            currency=state.total_amount.currency,
        )

        match_out: MatchOutput = await asyncio.to_thread(
            _run_match_reasoning,
            match_input=match_input,
            po_lines_json=json.dumps([p.model_dump(mode="json") for p in po.lines]),
            wareneingang_json=json.dumps(
                [w.model_dump(mode="json") for w in wareneingang.entries]
            ),
        )

        twm = ThreeWayMatch(
            outcome=match_out.outcome,
            po_number=po.po_number,
            wareneingang_numbers=tuple(e.wareneingang_number for e in wareneingang.entries),
            matched_lines=match_out.matched_line_numbers,
            unmatched_lines=match_out.unmatched_line_numbers,
            price_variance_cents=match_out.price_variance_cents,
            notes=match_out.rationale,
        )

        if match_out.outcome is MatchOutcome.FULL:
            # Decide whether autonomy is appropriate purely on threshold.
            settings = self._settings or get_settings()
            requires_human = (
                state.total_amount.amount_cents > settings.autonomous_post_threshold_cents
            )
            return CrewKickoffResult(
                state_update={"three_way_match": twm},
                next_status=(
                    InvoiceStatus.MATCHED if requires_human else InvoiceStatus.AUTONOMOUS_OK
                ),
                recommend_human_review=requires_human,
                recommend_human_reason=(
                    f"threshold: amount {state.total_amount.amount_cents}c "
                    f"> threshold {settings.autonomous_post_threshold_cents}c"
                )
                if requires_human
                else None,
            )

        if match_out.outcome is MatchOutcome.PARTIAL:
            return CrewKickoffResult(
                state_update={"three_way_match": twm},
                next_status=InvoiceStatus.PARTIAL_MATCH,
                recommend_human_review=True,
                recommend_human_reason="three_way_match partial",
            )

        return CrewKickoffResult(
            state_update={"three_way_match": twm},
            next_status=InvoiceStatus.NO_MATCH,
            recommend_human_review=True,
            recommend_human_reason="three_way_match: no lines matched",
        )

    async def _phase_post(self, state: InvoiceState) -> CrewKickoffResult:
        """Buchungs-Agent. Submits to DATEV. Idempotent on correlation_id."""
        if (
            state.vendor is None
            or state.total_amount is None
            or state.invoice_number is None
            or state.invoice_date is None
        ):
            raise CrewError(
                "phase_post called before extraction populated invoice fields",
                correlation_id=state.correlation_id,
            )
        assert self.toolset is not None

        ocr_lines = tuple(
            OCRLineItem(
                line_number=li.line_number,
                description=li.description,
                quantity=li.quantity,
                unit_price_eur=li.unit_price.to_decimal(),
                line_total_eur=li.line_total.to_decimal(),
                tax_rate_pct=li.tax_rate_pct,
            )
            for li in state.line_items
        )

        # Compose Buchungstext via DSPy.
        primary_ks = next(
            (li.kostenstelle for li in state.line_items if li.kostenstelle is not None),
            "",
        )
        buchungstext = await asyncio.to_thread(
            _run_compose_commentary,
            vendor_name=state.vendor.name,
            invoice_number=state.invoice_number,
            primary_kostenstelle=primary_ks,
            line_descriptions=", ".join(li.description for li in state.line_items[:3]),
        )

        posting_input = PostingInput(
            invoice_number=state.invoice_number,
            kreditor_number=state.vendor.kreditor_number,
            vendor_name=state.vendor.name,
            invoice_date_iso=state.invoice_date.isoformat(),
            total_amount_cents=state.total_amount.amount_cents,
            currency=state.total_amount.currency,
            line_items=ocr_lines,
            primary_kostenstelle=primary_ks,
            idempotency_key=state.correlation_id,
        )

        datev_posting = DATEVPosting(
            kreditor_number=posting_input.kreditor_number,
            invoice_number=posting_input.invoice_number,
            invoice_date_iso=posting_input.invoice_date_iso,
            total_amount_cents=posting_input.total_amount_cents,
            currency=posting_input.currency,
            buchungstext=buchungstext[:60],
            line_postings_json=json.dumps(
                [li.model_dump(mode="json") for li in posting_input.line_items]
            ),
            idempotency_key=posting_input.idempotency_key,
        )

        result = await self.toolset.submit_posting(
            posting=datev_posting, correlation_id=state.correlation_id
        )

        if not result.success:
            return CrewKickoffResult(
                state_update={},
                next_status=InvoiceStatus.EXCEPTION,
                recommend_human_review=True,
                recommend_human_reason=(
                    f"datev posting failed: {result.error_code} {result.error_message}"
                ),
            )

        if state.status is InvoiceStatus.AUTONOMOUS_OK:
            decided_by: str = "autonomous"
            approver_id: str | None = None
        else:
            approver_role, approver_id = _approver_from_history(state)
            decided_by = approver_role or "sachbearbeiter"

        posting_decision = PostingDecision(
            decision="post",
            datev_belegnummer=result.datev_belegnummer,
            posted_at=datetime.now(state.received_at.tzinfo),
            decided_by=decided_by,  # type: ignore[arg-type]
            approver_id=approver_id,
            rationale=buchungstext,
        )

        return CrewKickoffResult(
            state_update={"posting_decision": posting_decision},
            next_status=InvoiceStatus.POSTED,
        )

    # --------------------------------------------------------------------- #
    # Helpers
    # --------------------------------------------------------------------- #

    async def _lookup_kreditor(
        self, correlation_id: str, ocr: OCROutput
    ) -> Any:
        assert self.toolset is not None
        return await self.toolset.lookup_kreditor(
            name_hint=ocr.vendor_name,
            ust_id=ocr.vendor_ust_id or None,
            correlation_id=correlation_id,
        )


# --------------------------------------------------------------------------- #
# DSPy module runners — synchronous; called via asyncio.to_thread.
# --------------------------------------------------------------------------- #


def _run_classify_intake(*, document_text: str, sender_hint: str) -> IntakeOutput:
    predictor = dspy.Predict(ClassifyIntake)
    # Both inputs are externally-controlled (OCR'd text, email sender).
    # They reach the LM only via the <external_content> envelope.
    pred = predictor(
        document_text=wrap_external_content(document_text, source="ocr"),
        sender_hint=wrap_external_content(sender_hint, source="email"),
    )
    return IntakeOutput(
        document_kind=pred.document_kind,
        vendor_name_guess=pred.vendor_name_guess or "",
        confidence=float(pred.confidence),
        reasoning=pred.reasoning or "",
    )


def _run_extract_fields(*, invoice_text: str, intake_hint: str) -> OCROutput:
    predictor = dspy.Predict(ExtractInvoiceFields)
    # invoice_text is OCR'd. intake_hint was derived from OCR by the prior
    # step — also tainted. Both wrapped before reaching the model.
    pred = predictor(
        invoice_text=wrap_external_content(invoice_text, source="ocr"),
        intake_hint=wrap_external_content(intake_hint, source="ocr"),
    )
    line_items_raw = json.loads(pred.line_items_json or "[]")
    line_items = tuple(
        OCRLineItem(
            line_number=int(li["line_number"]),
            description=li["description"],
            quantity=Decimal(str(li["quantity"])),
            unit_price_eur=Decimal(str(li["unit_price_eur"])),
            line_total_eur=Decimal(str(li["line_total_eur"])),
            tax_rate_pct=Decimal(str(li.get("tax_rate_pct", "19"))),
        )
        for li in line_items_raw
    )
    return OCROutput(
        invoice_number=pred.invoice_number,
        invoice_date_iso=pred.invoice_date_iso,
        vendor_name=pred.vendor_name,
        vendor_ust_id=pred.vendor_ust_id or "",
        total_amount_eur=Decimal(str(pred.total_amount_eur)),
        currency=pred.currency or "EUR",
        line_items=line_items,
        confidence=float(pred.confidence),
        extraction_notes=pred.extraction_notes or "",
    )


def _run_match_reasoning(
    *, match_input: MatchInput, po_lines_json: str, wareneingang_json: str
) -> MatchOutput:
    predictor = dspy.Predict(ReasonOverMatch)
    # Invoice JSON came from OCR; PO + Wareneingang JSON came from SAP.
    # All three carry free-text fields (descriptions, notes) that external
    # actors can influence — all wrapped before reaching the model.
    invoice_lines_json = json.dumps(
        [li.model_dump(mode="json") for li in match_input.line_items]
    )
    pred = predictor(
        invoice_lines_json=wrap_external_content(invoice_lines_json, source="ocr"),
        po_lines_json=wrap_external_content(po_lines_json, source="sap_po"),
        wareneingang_json=wrap_external_content(
            wareneingang_json, source="sap_wareneingang"
        ),
        tolerance_cents=match_input.tolerance_cents,
    )
    outcome = MatchOutcome(pred.outcome)
    return MatchOutput(
        outcome=outcome,
        matched_line_numbers=tuple(json.loads(pred.matched_line_numbers or "[]")),
        unmatched_line_numbers=tuple(json.loads(pred.unmatched_line_numbers or "[]")),
        price_variance_cents=int(pred.price_variance_cents),
        rationale=pred.rationale or "",
    )


def _run_compose_commentary(
    *,
    vendor_name: str,
    invoice_number: str,
    primary_kostenstelle: str,
    line_descriptions: str,
) -> str:
    predictor = dspy.Predict(ComposePostingCommentary)
    # vendor_name and line_descriptions originate from OCR.
    # invoice_number and kostenstelle are also OCR-derived but appear
    # in payment system fields downstream — same trust posture.
    pred = predictor(
        vendor_name=wrap_external_content(vendor_name, source="ocr"),
        invoice_number=wrap_external_content(invoice_number, source="ocr"),
        primary_kostenstelle=wrap_external_content(
            primary_kostenstelle, source="sap_po"
        ),
        line_descriptions=wrap_external_content(line_descriptions, source="ocr"),
    )
    return str(pred.buchungstext)


def _parse_iso_date(value: str) -> datetime:
    """Parse an ISO date string. Raise CrewError on malformed input."""
    try:
        return datetime.fromisoformat(value)
    except ValueError as exc:
        raise CrewError(f"invalid ISO date '{value}'") from exc


def _approver_from_history(state: InvoiceState) -> tuple[str | None, str | None]:
    """Recover (role, id) from the most recent human_approval StatusEvent.

    The note is a JSON object written by `graph.human_approval_node` —
    parsing is unambiguous regardless of free-form rationale content.
    """
    for event in reversed(state.history):
        if event.actor != "human_approval" or not event.note:
            continue
        try:
            payload = json.loads(event.note)
        except json.JSONDecodeError:
            continue
        if isinstance(payload, dict):
            role = payload.get("approver_role")
            approver = payload.get("approver_id")
            return (
                role if isinstance(role, str) else None,
                approver if isinstance(approver, str) else None,
            )
    return None, None


_ = Money  # keep Money import used for type completeness
__all__ = ["APCrew"]
