"""DSPy signatures — the typed prompt artifacts for AP agents.

Every agent prompt is a compiled DSPy module, never an f-string. Reasons:
    1. Type safety: input/output types are enforced at the signature level.
    2. Optimizability: DSPy compilers (BootstrapFewShot, MIPRO) can tune
       these signatures against held-out invoices without code edits.
    3. Versioning: each signature is hashable; we log the hash on every
       call so we know exactly which compiled artifact produced a result.
    4. Reproducibility: prompts evolve as artifacts under version control,
       not buried in agent definitions.

These signatures are the *only* place prompt text lives in this codebase.
Agent role/goal/backstory in agents.py are short German role descriptions
for the CrewAI team metaphor; the actual prompt work happens in DSPy
modules built from these signatures.
"""

from __future__ import annotations

import hashlib
import json
from typing import Any, Literal

import dspy


def signature_hash(sig: type[dspy.Signature]) -> str:
    """Stable hash over signature instructions and field schema.

    Logged on every signature use so a run can be reproduced exactly.
    """
    payload = {
        "instructions": sig.__doc__ or "",
        "fields": {
            name: {
                "kind": field.json_schema_extra.get("__dspy_field_type", "")
                if hasattr(field, "json_schema_extra")
                else "",
                "desc": getattr(field, "description", "") or "",
            }
            for name, field in sig.model_fields.items()
        },
    }
    blob = json.dumps(payload, sort_keys=True).encode("utf-8")
    return hashlib.sha256(blob).hexdigest()[:16]


# --------------------------------------------------------------------------- #
# Eingangs-Agent — intake classification
# --------------------------------------------------------------------------- #


class ClassifyIntake(dspy.Signature):
    """Klassifiziere eingehende Dokumente. Entscheide, ob das Dokument eine
    Eingangsrechnung, eine Bestellbestaetigung, eine Mahnung oder etwas
    anderes ist. Bei Eingangsrechnungen extrahiere die Kreditor-Identitaet
    soweit aus Header/Absender erkennbar. Antworte in deutschen Geschaeftsterms."""

    document_text: str = dspy.InputField(desc="Erste 4000 Zeichen des OCR-Ergebnisses oder E-Mail-Body.")
    sender_hint: str = dspy.InputField(desc="E-Mail-Absender oder Belege-online-Quelle, falls vorhanden.")

    document_kind: Literal[
        "eingangsrechnung", "bestellbestaetigung", "mahnung", "gutschrift", "sonstiges"
    ] = dspy.OutputField()
    vendor_name_guess: str = dspy.OutputField(
        desc="Vermuteter Kreditor-Name. Leerer String, wenn nicht erkennbar."
    )
    confidence: float = dspy.OutputField(desc="0.0 bis 1.0.")
    reasoning: str = dspy.OutputField(desc="Kurzbegruendung in einem Satz.")


# --------------------------------------------------------------------------- #
# OCR-Agent — structured extraction from raw text
# --------------------------------------------------------------------------- #


class ExtractInvoiceFields(dspy.Signature):
    """Extrahiere strukturierte Felder aus einer deutschen Eingangsrechnung.
    Behandle Datumsformate (DD.MM.YYYY), Betraege im Format 1.234,56 sowie
    Umsatzsteuer (19%, 7%, 0%). Bei Unsicherheit nicht raten — Feld leer
    lassen und confidence senken."""

    invoice_text: str = dspy.InputField(desc="Vollstaendiger OCR-Text der Rechnung.")
    intake_hint: str = dspy.InputField(
        desc="Hinweise aus dem Intake-Schritt (z.B. vermuteter Kreditor-Name).",
    )

    invoice_number: str = dspy.OutputField(desc="Rechnungsnummer des Kreditors.")
    invoice_date_iso: str = dspy.OutputField(desc="Rechnungsdatum als ISO-8601-Datum.")
    vendor_name: str = dspy.OutputField()
    vendor_ust_id: str = dspy.OutputField(desc="USt-IdNr; leer, wenn nicht erkennbar.")
    total_amount_eur: str = dspy.OutputField(desc="Bruttoendbetrag in Euro als Zahl mit Punkt-Dezimal.")
    currency: str = dspy.OutputField(desc="Waehrungscode, default EUR.")
    line_items_json: str = dspy.OutputField(
        desc=(
            "JSON-Array. Jedes Element: {line_number:int, description:str, "
            "quantity:str, unit_price_eur:str, line_total_eur:str, tax_rate_pct:str}. "
            "Leerer Array []-String, wenn keine Positionen ausgelesen werden konnten."
        ),
    )
    confidence: float = dspy.OutputField()
    extraction_notes: str = dspy.OutputField(desc="Ungeklaerte Stellen oder Warnungen.")


# --------------------------------------------------------------------------- #
# Match-Agent — three-way match reasoning
# --------------------------------------------------------------------------- #


class ReasonOverMatch(dspy.Signature):
    """Entscheide ueber das Ergebnis eines Drei-Wege-Abgleichs aus SAP-Daten.
    Gegeben sind die Rechnungspositionen, die zugehoerige Bestellung (PO)
    und die Wareneingaenge. Bestimme outcome=FULL, PARTIAL oder NONE und
    begruende. FULL nur, wenn jede Position Menge, Preis und Wareneingang
    innerhalb der konfigurierten Toleranz uebereinstimmt."""

    invoice_lines_json: str = dspy.InputField(desc="JSON-Array der Rechnungspositionen.")
    po_lines_json: str = dspy.InputField(desc="JSON-Array der PO-Positionen.")
    wareneingang_json: str = dspy.InputField(desc="JSON-Array der Wareneingaenge.")
    tolerance_cents: int = dspy.InputField(desc="Maximal akzeptierte Preisabweichung pro Position in Cent.")

    outcome: Literal["full", "partial", "none"] = dspy.OutputField()
    matched_line_numbers: str = dspy.OutputField(
        desc="JSON-Array der Rechnungs-Positionsnummern, die uebereinstimmen.",
    )
    unmatched_line_numbers: str = dspy.OutputField(desc="JSON-Array der nicht-uebereinstimmenden Positionen.")
    price_variance_cents: int = dspy.OutputField(desc="Absolute Preisabweichung gesamt in Cent.")
    rationale: str = dspy.OutputField(desc="Erklaerung des Ergebnisses, max. 3 Saetze.")


# --------------------------------------------------------------------------- #
# Buchungs-Agent — DATEV posting commentary
# --------------------------------------------------------------------------- #


class ComposePostingCommentary(dspy.Signature):
    """Verfasse einen praezisen, regelkonformen Buchungstext (Buchungstext)
    fuer DATEV. Max. 60 Zeichen. Ton: nuechtern, sachlich, ohne Marketing.
    Enthaelt Kreditor, Belegnummer-Hinweis und Kostenstelle, falls relevant."""

    vendor_name: str = dspy.InputField()
    invoice_number: str = dspy.InputField()
    primary_kostenstelle: str = dspy.InputField(desc="Hauptkostenstelle, oder leer.")
    line_descriptions: str = dspy.InputField(desc="Kommagetrennt, die ersten 3 Positionsbeschreibungen.")

    buchungstext: str = dspy.OutputField(desc="Max. 60 Zeichen, deutsch.")


__all__ = [
    "ClassifyIntake",
    "ComposePostingCommentary",
    "ExtractInvoiceFields",
    "ReasonOverMatch",
    "signature_hash",
]


def all_signature_hashes() -> dict[str, str]:
    """Used on Crew startup to log the prompt-artifact fingerprints."""
    return {
        sig.__name__: signature_hash(sig)
        for sig in (
            ClassifyIntake,
            ExtractInvoiceFields,
            ReasonOverMatch,
            ComposePostingCommentary,
        )
    }


# Silence type checker — dspy.Signature is metaclass-magic.
_: Any = None
