"""Structured logging via structlog.

Single source of truth: every log line is JSON, every line carries
`correlation_id`, `service`, `environment`. Correlation ID lives in a
ContextVar so it propagates across awaits without manual threading.

Discipline:
    - Never log invoice content fields unless config.log_invoice_content=True.
    - Never log secrets — pydantic-settings SecretStr won't serialize, that's
      the first line of defense; the second is the redaction processor below.
    - Errors are logged with `exc_info=True` and a typed `error_type` key
      so downstream alerting can fan out by exception class.
"""

from __future__ import annotations

import logging
import sys
from contextvars import ContextVar
from typing import Any

import structlog
from structlog.contextvars import bind_contextvars, clear_contextvars
from structlog.types import EventDict, Processor

from putsch_orchestration.config import Settings, get_settings

_correlation_id_var: ContextVar[str | None] = ContextVar("correlation_id", default=None)

# Keys that must never appear in a log line, even if a caller passes them.
_FORBIDDEN_KEYS = frozenset(
    {
        "iban",
        "ust_id",
        "raw_text",
        "litellm_api_key",
        "datev_password",
        "sap_password",
        "email_password",
    }
)

# Keys that are redacted unless log_invoice_content=True.
_CONTENT_KEYS = frozenset(
    {
        "invoice_text",
        "ocr_text",
        "line_description",
        "vendor_name",
        "email_body",
    }
)


def _redact_processor(_: Any, __: str, event_dict: EventDict) -> EventDict:
    """Strip forbidden keys; redact content keys per config."""
    settings = get_settings()
    placeholder = settings.pii_redaction_placeholder
    log_content = settings.log_invoice_content

    for key in list(event_dict.keys()):
        if key in _FORBIDDEN_KEYS:
            event_dict[key] = placeholder
        elif key in _CONTENT_KEYS and not log_content:
            event_dict[key] = placeholder
    return event_dict


def _bind_runtime_context(_: Any, __: str, event_dict: EventDict) -> EventDict:
    """Inject service/env/correlation on every event."""
    settings = get_settings()
    event_dict.setdefault("service", settings.service_name)
    event_dict.setdefault("environment", settings.environment.value)
    cid = _correlation_id_var.get()
    if cid is not None:
        event_dict.setdefault("correlation_id", cid)
    return event_dict


def configure_logging(settings: Settings | None = None) -> None:
    """Idempotent logging setup. Call once at process start.

    Tests can call this after monkeypatching env without leaking state — the
    structlog config is global, but ContextVars are not.
    """
    s = settings or get_settings()

    timestamper = structlog.processors.TimeStamper(fmt="iso", utc=True)
    processors: list[Processor] = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        timestamper,
        _bind_runtime_context,
        _redact_processor,
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer(),
    ]

    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, s.log_level)
        ),
        context_class=dict,
        logger_factory=structlog.WriteLoggerFactory(file=sys.stdout),
        cache_logger_on_first_use=True,
    )

    # Route stdlib logging through structlog too — picks up CrewAI's internal logs.
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, s.log_level),
    )


def set_correlation_id(correlation_id: str) -> None:
    """Bind a correlation ID for the current async task and downstream calls."""
    _correlation_id_var.set(correlation_id)
    bind_contextvars(correlation_id=correlation_id)


def clear_correlation_id() -> None:
    _correlation_id_var.set(None)
    clear_contextvars()


def get_logger(name: str | None = None) -> structlog.stdlib.BoundLogger:
    return structlog.get_logger(name)


__all__ = [
    "clear_correlation_id",
    "configure_logging",
    "get_logger",
    "set_correlation_id",
]
