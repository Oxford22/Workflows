"""Trust boundaries and prompt-injection defenses.

See ADR-002 for the threat model and the rationale for each layer.

Single source of truth for three structural defenses:

    TaintedText                — typed envelope marking external-origin
                                 strings. The type-system fence.
    wrap_external_content      — the rendering helper that frames a
                                 string inside <external_content
                                 source="..."> tags for LLM consumption.
                                 Every DSPy InputField that carries
                                 external content routes through this.
    strip_instruction_patterns — write-time sanitizer for content going
                                 to long-lived external storage
                                 (Langfuse session metadata, Graphiti
                                 facts, OTel span attributes).

The defenses compose. We do not pick one. The instruction hierarchy
("untrusted text never reaches the agent's instruction channel; it
reaches a data channel the agent is told to interpret, not obey") is
the policy; this module is the mechanism.

Adding a new SourceTag is an ADR-level change: it means we trust a new
origin to produce content we'll feed to the model. Removing a pattern
from `_INJECTION_PATTERNS` is also ADR-level — patterns are added more
freely than they are removed.
"""

from __future__ import annotations

import re
from typing import Final, Literal

from pydantic import BaseModel, ConfigDict

SourceTag = Literal[
    "ocr",
    "email",
    "sap_po",
    "sap_kreditor",
    "sap_wareneingang",
    "datev_field",
    "user_input",
    "unknown",
]
"""Provenance tags for tainted content. Adding a new tag means we trust
that origin to produce content we will feed to the model as *data*
(never as directive). Use `unknown` only as a transitional placeholder;
calls observed at runtime trigger a structured warning log so they can
be retagged to their actual origin."""


class TaintedText(BaseModel):
    """Wrapper for any text whose content cannot be trusted as instruction.

    Type-level enforcement of the trust boundary. Code that wants to feed
    a TaintedText into an LLM prompt must call `wrap_external_content()`
    (or the helper `.wrap_for_prompt()`). Code that wants the raw value
    for a non-LLM sink (DATEV payload write, UI render, ZIP archive)
    accesses `.value` explicitly — and an audit grep over `.value` finds
    every such site, which is the point.

    Defense in depth: this is the type-system fence. The other layers are
    write-time sanitization at memory/obs hooks (`strip_instruction_patterns`)
    and prompt-time wrapping at the DSPy boundary (`wrap_external_content`).
    See ADR-002.
    """

    model_config = ConfigDict(frozen=True, extra="forbid")

    value: str
    source: SourceTag
    correlation_id: str | None = None

    def wrap_for_prompt(self) -> str:
        """Return the LLM-safe rendering: tagged as data, never instruction."""
        return wrap_external_content(self.value, source=self.source)

    def __len__(self) -> int:
        return len(self.value)


# The patterns below catch the most common prompt-injection vectors observed
# in OCR output, free-text DATEV fields, and email bodies. The list is
# intentionally conservative — false positives (stripping a legitimate line
# that looks like an injection) are acceptable; false negatives are not.
#
# Patterns are case-insensitive and line-anchored where the attack
# typically starts a line. Multi-language coverage: German and English are
# both in scope because both appear in Putsch's invoice corpus.
_INJECTION_PATTERNS: Final[tuple[re.Pattern[str], ...]] = (
    # Bracketed/HTML-style system tags.
    re.compile(r"(?im)^\s*\[?\s*system\s*[:\]]"),
    re.compile(r"(?im)<\s*/?\s*system\b"),
    re.compile(r"(?im)\[\s*/?\s*(system|assistant|user)\s*\]"),
    # "Note to processor" / "Hinweis an Sachbearbeiter" patterns.
    re.compile(r"(?im)^\s*note to (the )?(processor|agent|reviewer|ap (clerk|processor))"),
    re.compile(
        r"(?im)^\s*hinweis (an|für) (den|die|das)? ?(prozessor|agent|"
        r"sachbearbeiter|kreditorenbuchhaltung)"
    ),
    re.compile(r"(?im)^\s*anweisung\s*[:]"),
    re.compile(r"(?im)^\s*system\s+(note|instruction|directive|hinweis)"),
    # Direct override attempts.
    re.compile(
        r"(?im)\bignore\s+(all\s+|the\s+|any\s+|previous\s+|prior\s+|above\s+|earlier\s+)*"
        r"(prior\s+|earlier\s+|previous\s+)?instructions?\b"
    ),
    re.compile(r"(?im)\bdisregard\s+(all\s+|the\s+|previous\s+|prior\s+)?(instructions?|context)"),
    re.compile(r"(?im)\b(do\s+not|never)\s+(apply|use|run|enforce)\s+(pii\s+)?redaction"),
    re.compile(
        r"(?im)\bdisable\s+(the\s+)?(obs_hooks?|hitl|human[_\s-]?approval|"
        r"interrupt|redaction|sanitizer|approval[_\s-]?cascade)"
    ),
    # Trust-list / approval bypass.
    re.compile(r"(?im)\bauto[-\s]?trust(\s+list|ed)?\b"),
    re.compile(
        r"(?im)\b(pre[-\s]?approved|prior(\s+verbal)?\s+(approval|authorization)|"
        r"out[-\s]of[-\s]band\s+(approval|sign[-\s]?off))\b"
    ),
    re.compile(
        r"(?im)\b(skip|bypass|omit)\s+(the\s+)?(human[_\s-]?approval|interrupt|"
        r"approval(\s+(step|cascade))?)\b"
    ),
    # IBAN / payment manipulation. These are the high-fraud-value vectors.
    re.compile(r"(?im)\b(set|update|change|replace)\s+(the\s+)?iban\s+to\b"),
    re.compile(r"(?im)\biban\s*[:=]\s*[A-Z]{2}\s*\d{2}(?:\s*[A-Z0-9]){11,30}"),
    # Decision-role spoofing.
    re.compile(
        r"(?im)\b(set|change|override)\s+(posting)?\s*decided[_\s-]?by\s+to\s+"
        r"['\"]?(geschaeftsfuehrer|gesch.ftsf.hrer|ceo|cfo|abteilungsleiter)"
    ),
    # Tool-call exfiltration markers.
    re.compile(r"(?im)\b(send|post|submit|email|exfiltrate)\s+.*\bto\s+https?://[^\s]+"),
    re.compile(r"(?im)\bwebhook[_\s-]?url\s*[:=]"),
)


def wrap_external_content(
    text: str,
    *,
    source: SourceTag,
) -> str:
    """Frame external-origin text for LLM consumption.

    Wraps the content in <external_content source="..."> tags. The
    DSPy signature instructions in `crews/ap/signatures.py` declare,
    in German and English, that nothing inside these tags is a
    directive. This function is the single rendering helper for that
    convention.

    Defense in depth: known-injection patterns are also stripped at
    this seam. The wrap is the primary protection (the model is
    instructed to ignore directives inside the tags); the strip is the
    second line (the most blatant patterns are removed before the model
    ever sees them).

    Code-review rule: a bare string going into a `dspy.Predict()` call
    is a failure. Either the input is `TaintedText` (and we use
    `.wrap_for_prompt()`) or the input is plain trusted text (and we
    pass it directly). If you don't know which, it's tainted.
    """
    cleaned = strip_instruction_patterns(text)
    return (
        f'<external_content source="{source}">\n'
        f"{cleaned}\n"
        f"</external_content>"
    )


def strip_instruction_patterns(text: str) -> str:
    """Replace lines matching known injection patterns with a placeholder.

    Called at two seams:
        1. `wrap_external_content` — at prompt-build time.
        2. Memory and observability write paths — before persisting any
           tainted string to Langfuse session metadata or Graphiti facts
           or OTel span attributes.

    Returns the text with offending lines replaced by a visible
    redaction placeholder. We do NOT silently drop — leaving a marker
    in logs and traces is critical for incident-response triage.

    The function is intentionally simple: line-level pattern matching,
    no model-based detection. Faster, audit-friendly, and trivially
    testable. A future enhancement (instruction-detection classifier,
    per the threat model) would slot in as an additional pass; this
    function remains the floor.
    """
    out_lines: list[str] = []
    for line in text.splitlines():
        if any(p.search(line) for p in _INJECTION_PATTERNS):
            out_lines.append("[STRIPPED: matched injection pattern]")
        else:
            out_lines.append(line)
    return "\n".join(out_lines)


__all__ = [
    "SourceTag",
    "TaintedText",
    "strip_instruction_patterns",
    "wrap_external_content",
]
