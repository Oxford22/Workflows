"""Observability hooks — OTel spans, the seam where Langfuse will plug in.

Every Crew kickoff and every LangGraph node opens a span. Spans propagate
the correlation_id via the W3C trace context and carry domain attributes:
    invoice.correlation_id    ULID
    invoice.status            current InvoiceStatus
    crew.name                 e.g. 'ap'
    node.name                 e.g. 'extract'
    invoice.amount_cents      when total_amount is set
    invoice.requires_human    bool

PII discipline: we never put OCR text, vendor names, or line descriptions
on span attributes. The Langfuse integration will write these into Langfuse
session metadata via a different code path (Langfuse runs inside the EU
trust boundary; OTel collectors generally do not).

Trust-boundary discipline (ADR-002): the persistence path sanitizes BEFORE
storage, not on read. Any string attribute that originated from external
content (OCR, SAP free text, email) must be passed through
`safe_attribute()` at the call site. This is sanitize-on-write — the
defense for the Langfuse-feedback-loop threat where a later debugging
agent re-ingests injected text from session metadata. Future Langfuse
integration MUST use the same helper for session metadata writes."""

from __future__ import annotations

from collections.abc import AsyncIterator, Mapping
from contextlib import asynccontextmanager
from typing import Any

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)
from opentelemetry.trace import Span, Status, StatusCode, Tracer

from putsch_orchestration.config import Settings, get_settings
from putsch_orchestration.logging_setup import get_logger
from putsch_orchestration.sanitize import strip_instruction_patterns
from putsch_orchestration.state import InvoiceState

_log = get_logger(__name__)

_tracer: Tracer | None = None
_initialized = False


def configure_tracing(settings: Settings | None = None) -> None:
    """Idempotent OTel setup. Call once at process start.

    Two exporters supported via config.otel_exporter:
        'stdout' — local dev; writes span JSON to stdout
        'otlp'   — production; pushes to the OTel collector that fans out
                   to Langfuse (PII-aware) and the metrics pipeline.

    Both run with batched processors; tests use SimpleSpanProcessor under
    a pytest fixture so spans flush synchronously.
    """
    global _tracer, _initialized
    if _initialized:
        return

    s = settings or get_settings()
    resource = Resource.create(
        {
            "service.name": s.service_name,
            "deployment.environment": s.environment.value,
        }
    )
    provider = TracerProvider(resource=resource)

    if s.otel_exporter == "stdout":
        provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
    elif s.otel_exporter == "otlp":
        endpoint = s.otel_otlp_endpoint
        if endpoint is None:
            raise RuntimeError(
                "otel_exporter='otlp' but otel_otlp_endpoint is not set"
            )
        provider.add_span_processor(BatchSpanProcessor(OTLPSpanExporter(endpoint=str(endpoint))))

    trace.set_tracer_provider(provider)
    _tracer = trace.get_tracer("putsch.orchestration")
    _initialized = True
    _log.info("obs.configured", exporter=s.otel_exporter)


def _tracer_or_default() -> Tracer:
    if _tracer is None:
        return trace.get_tracer("putsch.orchestration")
    return _tracer


def safe_attribute(value: str | int | float | bool) -> str | int | float | bool:
    """Sanitize a value before attaching it to an OTel span attribute.

    Numeric and bool values pass through unchanged. String values are run
    through `strip_instruction_patterns` so injected instructions cannot
    survive into long-lived traces and cannot be re-ingested by future
    debugging agents reading the trace store.

    Per ADR-002, this is the canonical write-time sanitizer for any
    observability sink — OTel attributes today, Langfuse session metadata
    when that module ships. Never put a tainted string on a span without
    running it through this helper."""
    if isinstance(value, str):
        return strip_instruction_patterns(value)
    return value


def _domain_attributes(state: InvoiceState) -> dict[str, Any]:
    """Domain attributes that are always safe to attach to a span."""
    attrs: dict[str, Any] = {
        "invoice.correlation_id": state.correlation_id,
        "invoice.thread_id": state.thread_id,
        "invoice.status": state.status.value,
        "invoice.intake_channel": state.intake_channel.value,
        "invoice.requires_human": state.requires_human,
        "invoice.retry_count": state.retry_count,
    }
    if state.total_amount is not None:
        attrs["invoice.amount_cents"] = state.total_amount.amount_cents
        attrs["invoice.currency"] = state.total_amount.currency
    if state.vendor is not None:
        # Kreditor number is a stable internal ID, not PII.
        attrs["invoice.kreditor_number"] = state.vendor.kreditor_number
    if state.three_way_match is not None:
        attrs["invoice.match_outcome"] = state.three_way_match.outcome.value
    return attrs


@asynccontextmanager
async def crew_span(
    crew_name: str,
    state: InvoiceState,
    *,
    extra: Mapping[str, Any] | None = None,
) -> AsyncIterator[Span]:
    """Span for a Crew kickoff. Use inside a `Crew-as-Node` wrapper."""
    tr = _tracer_or_default()
    with tr.start_as_current_span(f"crew.{crew_name}") as span:
        span.set_attributes(_domain_attributes(state))
        span.set_attribute("crew.name", crew_name)
        if extra:
            for k, v in extra.items():
                span.set_attribute(k, v)
        try:
            yield span
        except Exception as exc:
            span.set_status(Status(StatusCode.ERROR, str(exc)))
            span.record_exception(exc)
            raise


@asynccontextmanager
async def node_span(
    node_name: str,
    state: InvoiceState,
    *,
    extra: Mapping[str, Any] | None = None,
) -> AsyncIterator[Span]:
    tr = _tracer_or_default()
    with tr.start_as_current_span(f"node.{node_name}") as span:
        span.set_attributes(_domain_attributes(state))
        span.set_attribute("node.name", node_name)
        if extra:
            for k, v in extra.items():
                span.set_attribute(k, v)
        try:
            yield span
        except Exception as exc:
            span.set_status(Status(StatusCode.ERROR, str(exc)))
            span.record_exception(exc)
            raise


@asynccontextmanager
async def tool_span(
    tool_name: str,
    correlation_id: str,
    *,
    extra: Mapping[str, Any] | None = None,
) -> AsyncIterator[Span]:
    """Span for an MCP tool call."""
    tr = _tracer_or_default()
    with tr.start_as_current_span(f"tool.{tool_name}") as span:
        span.set_attribute("tool.name", tool_name)
        span.set_attribute("invoice.correlation_id", correlation_id)
        if extra:
            for k, v in extra.items():
                span.set_attribute(k, v)
        try:
            yield span
        except Exception as exc:
            span.set_status(Status(StatusCode.ERROR, str(exc)))
            span.record_exception(exc)
            raise


__all__ = ["configure_tracing", "crew_span", "node_span", "safe_attribute", "tool_span"]
