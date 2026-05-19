"""12-factor configuration via pydantic-settings.

All endpoints, secrets, and tuning knobs flow through environment
variables. No hardcoded URLs, no hardcoded model names, no fallback to
prod endpoints in dev — every value is explicit. Boot fails fast on
missing required config (`PUTSCH_DATABASE_URL`, model endpoints).

Two settings groups:
    Settings              — top-level, loaded once at import time.
    ModelBindingSettings  — per-agent model routing, exposed to models.py.
"""

from __future__ import annotations

from enum import Enum
from functools import lru_cache
from typing import Annotated, Literal, Self

from pydantic import Field, HttpUrl, PostgresDsn, SecretStr, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(str, Enum):
    LOCAL = "local"
    STAGING = "staging"
    PROD = "prod"


# --------------------------------------------------------------------------- #
# Model binding — one source of truth for "which model runs which task".
# --------------------------------------------------------------------------- #


class ModelBinding(BaseSettings):
    """A single (agent_role -> model) binding.

    Strings are LiteLLM model identifiers (e.g. 'mistral/mistral-large-2',
    'openai/gpt-4o', 'huggingface/Qwen/Qwen2.5-72B-Instruct'). The choice
    of provider lives in env, not in code; defaults below are the
    architectural decision baked into this module.
    """

    model_config = SettingsConfigDict(extra="forbid")

    reasoning: str = "mistral/mistral-large-2"
    """Used by manager-agent, match-agent, supervisor routing."""

    german_extraction: str = "huggingface/Qwen/Qwen2.5-72B-Instruct"
    """OCR-Agent and any agent that parses German invoice prose."""

    sap_rfc_generation: str = "huggingface/Qwen/Qwen2.5-Coder-32B-Instruct"
    """Match-Agent fallback when SAP RFC composition is required."""

    german_prose: str = "mistral/mistral-medium-3.5"
    """Buchungs-Agent for commentary in postings; lower latency target."""


# --------------------------------------------------------------------------- #
# Top-level settings.
# --------------------------------------------------------------------------- #


class Settings(BaseSettings):
    """Top-level application settings.

    All env vars are prefixed `PUTSCH_`. Nested settings (e.g. model bindings)
    use double-underscore: `PUTSCH_MODELS__REASONING=mistral/...`.
    """

    model_config = SettingsConfigDict(
        env_prefix="PUTSCH_",
        env_nested_delimiter="__",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # --- Runtime ---
    environment: Environment = Environment.LOCAL
    service_name: str = "putsch-ap-orchestrator"
    """Used in OTel resource attributes and structlog `service` field."""

    # --- Persistence ---
    database_url: PostgresDsn
    """LangGraph PostgresSaver DSN. Required — no in-memory fallback in prod."""

    checkpoint_namespace: str = "ap"
    """Logical partition inside PostgresSaver; lets one DB host multiple Crew workflows."""

    # --- LLM proxy ---
    litellm_base_url: HttpUrl
    """LiteLLM proxy URL. We never call provider APIs directly."""

    litellm_api_key: SecretStr
    """Master key for the LiteLLM proxy."""

    # --- MCP endpoints ---
    sap_mcp_url: HttpUrl
    """SAP-MCP server (PO + Wareneingang + Kreditor lookup)."""
    datev_mcp_url: HttpUrl
    """DATEV-MCP server (Buchung)."""
    email_mcp_url: HttpUrl
    """Email-MCP server (Eingangs-Agent intake)."""
    mcp_timeout_seconds: float = Field(default=30.0, gt=0)

    # --- HITL thresholds ---
    autonomous_post_threshold_cents: int = Field(
        default=10_000_00,
        ge=0,
        description=(
            "Postings strictly above this threshold require Sachbearbeiter approval "
            "even on a full three-way match. Default 10,000 EUR per Putsch finance policy."
        ),
    )
    abteilungsleiter_threshold_cents: int = Field(default=50_000_00, ge=0)
    geschaeftsfuehrer_threshold_cents: int = Field(default=250_000_00, ge=0)

    # --- Retry / circuit-breaker tuning ---
    tool_retry_attempts: int = Field(default=4, ge=1, le=10)
    tool_retry_base_delay_seconds: float = Field(default=0.5, gt=0)
    circuit_breaker_failure_threshold: int = Field(default=5, ge=1)
    circuit_breaker_reset_seconds: float = Field(default=60.0, gt=0)

    # --- Observability ---
    otel_exporter: Literal["stdout", "otlp"] = "stdout"
    otel_otlp_endpoint: HttpUrl | None = None
    """Required when otel_exporter='otlp'. Validated below."""
    log_level: Literal["DEBUG", "INFO", "WARN", "ERROR"] = "INFO"

    # --- GDPR / privacy ---
    log_invoice_content: bool = Field(
        default=False,
        description=(
            "When False (default and recommended), OCR text, line item descriptions, "
            "and IBANs are redacted from logs and observability spans. Set True only "
            "in local dev with synthetic data. Production toggling requires Betriebsrat "
            "sign-off — this is a compliance fence, not a debugging convenience."
        ),
    )
    pii_redaction_placeholder: Annotated[str, Field(min_length=1)] = "[REDACTED]"

    # --- Models ---
    models: ModelBinding = Field(default_factory=ModelBinding)

    @model_validator(mode="after")
    def _otlp_endpoint_required_when_selected(self) -> Self:
        if self.otel_exporter == "otlp" and self.otel_otlp_endpoint is None:
            raise ValueError("otel_exporter='otlp' requires otel_otlp_endpoint to be set")
        return self


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Singleton accessor.

    `lru_cache` makes this importable from tests with monkeypatched env
    by calling `get_settings.cache_clear()` first.
    """
    return Settings()  # type: ignore[call-arg]


__all__ = ["Environment", "ModelBinding", "Settings", "get_settings"]
