"""MCP-backed tools for the AP Crew.

Three external systems:
    SAP-MCP    PO lookup, Wareneingang lookup, Kreditor master-data lookup
    DATEV-MCP  Buchung (posting) submission
    Email-MCP  Inbound message + attachment retrieval

Every tool:
    - async (CrewAI's sync internals wrapped at the agent layer)
    - typed in/out via Pydantic
    - wrapped in tenacity retry (exponential backoff, jitter)
    - guarded by a per-system circuit breaker
    - emits a tool span via obs_hooks.tool_span
    - never logs IBAN, USt-ID, or raw invoice content (those keys are
      stripped by the redaction processor; we double-check at call sites)

Tools are *not* CrewAI BaseTool subclasses here — we expose plain async
callables and adapt them to CrewAI's tool interface inside agents.py.
That keeps the tool implementation framework-agnostic; a future swap to
LlamaIndex or AutoGen reuses every line of this file.
"""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any

import httpx
from pydantic import BaseModel, ConfigDict, Field
from tenacity import (
    AsyncRetrying,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential_jitter,
)

from putsch_orchestration.circuit import AsyncCircuitBreaker, CircuitOpenError
from putsch_orchestration.config import Settings, get_settings
from putsch_orchestration.logging_setup import get_logger
from putsch_orchestration.obs_hooks import tool_span
from putsch_orchestration.state import ToolError

_log = get_logger(__name__)


# --------------------------------------------------------------------------- #
# Tool input/output schemas
# --------------------------------------------------------------------------- #


class POLine(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    line_number: int
    material_number: str
    description: str
    quantity_ordered: Decimal
    quantity_received: Decimal
    unit_price_cents: int
    currency: str = "EUR"
    sachkonto: str
    kostenstelle: str | None = None


class POLookupResult(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    found: bool
    po_number: str | None = None
    kreditor_number: str | None = None
    lines: tuple[POLine, ...] = Field(default_factory=tuple)


class WareneingangEntry(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    wareneingang_number: str
    po_line_number: int
    quantity_received: Decimal
    received_at: str
    """ISO-8601 date string; we keep as str across the MCP boundary."""


class WareneingangLookupResult(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    po_number: str
    entries: tuple[WareneingangEntry, ...]


class KreditorLookupResult(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    found: bool
    kreditor_number: str | None = None
    name: str | None = None
    ust_id: str | None = None
    iban: str | None = None


class DATEVPosting(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    kreditor_number: str
    invoice_number: str
    invoice_date_iso: str
    total_amount_cents: int
    currency: str
    buchungstext: str = Field(max_length=60)
    line_postings_json: str
    """JSON string carrying line-level Sachkonto/Kostenstelle splits."""
    idempotency_key: str
    """ULID. Required — DATEV deduplicates on this server-side."""


class DATEVPostResult(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    success: bool
    datev_belegnummer: str | None = None
    error_code: str | None = None
    error_message: str | None = None


class EmailMessage(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid")
    message_id: str
    sender: str
    subject: str
    received_at: str
    attachment_uris: tuple[str, ...]


# --------------------------------------------------------------------------- #
# MCP client — thin async HTTP client, one per external system
# --------------------------------------------------------------------------- #


@dataclass
class _MCPClient:
    """Thin async client for one MCP server.

    MCP transport here is HTTP+JSON for simplicity; a future swap to
    streamable-HTTP or stdio is contained inside this class.
    """

    base_url: str
    timeout_s: float
    breaker: AsyncCircuitBreaker
    name: str
    _http: httpx.AsyncClient = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._http = httpx.AsyncClient(
            base_url=self.base_url,
            timeout=self.timeout_s,
            headers={"Accept": "application/json"},
        )

    async def aclose(self) -> None:
        await self._http.aclose()

    async def call(
        self,
        method: str,
        params: Mapping[str, Any],
        *,
        correlation_id: str,
    ) -> dict[str, Any]:
        body = {"method": method, "params": dict(params)}

        async def _do_request() -> dict[str, Any]:
            async with tool_span(
                f"{self.name}.{method}",
                correlation_id,
                extra={"mcp.server": self.name, "mcp.method": method},
            ):
                resp = await self._http.post(
                    "/rpc", json=body, headers={"X-Correlation-Id": correlation_id}
                )
                if resp.status_code >= 500:
                    raise ToolError(
                        f"{self.name}.{method} returned {resp.status_code}",
                        correlation_id=correlation_id,
                    )
                if resp.status_code >= 400:
                    # 4xx is not retried — caller has malformed input.
                    raise ToolError(
                        f"{self.name}.{method} client error {resp.status_code}",
                        correlation_id=correlation_id,
                    )
                data = resp.json()
                if not isinstance(data, dict):
                    raise ToolError(
                        f"{self.name}.{method} non-dict response",
                        correlation_id=correlation_id,
                    )
                return data

        # Retry: only on 5xx / network. ToolError on 4xx is not retried.
        async for attempt in AsyncRetrying(
            stop=stop_after_attempt(get_settings().tool_retry_attempts),
            wait=wait_exponential_jitter(
                initial=get_settings().tool_retry_base_delay_seconds, max=8.0
            ),
            retry=retry_if_exception_type((httpx.TransportError, httpx.TimeoutException)),
            reraise=True,
        ):
            with attempt:
                return await self.breaker.call(_do_request)

        # Unreachable — AsyncRetrying with reraise=True either returns or raises.
        raise ToolError(
            f"{self.name}.{method} retries exhausted", correlation_id=correlation_id
        )


# --------------------------------------------------------------------------- #
# Tool registry — one builder per (settings instance), cached
# --------------------------------------------------------------------------- #


@dataclass
class APToolset:
    """Concrete async tool callables used by AP agents.

    Construct with `build_ap_toolset(settings)`. Closes underlying HTTP
    clients on `aclose()` — call from the graph shutdown hook.
    """

    sap: _MCPClient
    datev: _MCPClient
    email: _MCPClient

    async def aclose(self) -> None:
        await self.sap.aclose()
        await self.datev.aclose()
        await self.email.aclose()

    # --- SAP-MCP wrappers ---

    async def lookup_po_by_vendor_and_invoice(
        self, *, kreditor_number: str, invoice_number: str, correlation_id: str
    ) -> POLookupResult:
        data = await self.sap.call(
            "po.lookup_by_invoice_ref",
            {"kreditor_number": kreditor_number, "invoice_number": invoice_number},
            correlation_id=correlation_id,
        )
        return POLookupResult.model_validate(data)

    async def lookup_wareneingang(
        self, *, po_number: str, correlation_id: str
    ) -> WareneingangLookupResult:
        data = await self.sap.call(
            "wareneingang.list_for_po",
            {"po_number": po_number},
            correlation_id=correlation_id,
        )
        return WareneingangLookupResult.model_validate(data)

    async def lookup_kreditor(
        self, *, name_hint: str, ust_id: str | None, correlation_id: str
    ) -> KreditorLookupResult:
        data = await self.sap.call(
            "kreditor.lookup",
            {"name_hint": name_hint, "ust_id": ust_id or ""},
            correlation_id=correlation_id,
        )
        return KreditorLookupResult.model_validate(data)

    # --- DATEV-MCP wrappers ---

    async def submit_posting(
        self, *, posting: DATEVPosting, correlation_id: str
    ) -> DATEVPostResult:
        data = await self.datev.call(
            "buchung.create",
            posting.model_dump(),
            correlation_id=correlation_id,
        )
        return DATEVPostResult.model_validate(data)

    # --- Email-MCP wrappers ---

    async def fetch_message(
        self, *, message_id: str, correlation_id: str
    ) -> EmailMessage:
        data = await self.email.call(
            "message.fetch",
            {"message_id": message_id},
            correlation_id=correlation_id,
        )
        return EmailMessage.model_validate(data)


def build_ap_toolset(settings: Settings | None = None) -> APToolset:
    s = settings or get_settings()
    return APToolset(
        sap=_MCPClient(
            base_url=str(s.sap_mcp_url),
            timeout_s=s.mcp_timeout_seconds,
            breaker=AsyncCircuitBreaker(
                name="sap-mcp",
                failure_threshold=s.circuit_breaker_failure_threshold,
                reset_seconds=s.circuit_breaker_reset_seconds,
            ),
            name="sap",
        ),
        datev=_MCPClient(
            base_url=str(s.datev_mcp_url),
            timeout_s=s.mcp_timeout_seconds,
            breaker=AsyncCircuitBreaker(
                name="datev-mcp",
                failure_threshold=s.circuit_breaker_failure_threshold,
                reset_seconds=s.circuit_breaker_reset_seconds,
            ),
            name="datev",
        ),
        email=_MCPClient(
            base_url=str(s.email_mcp_url),
            timeout_s=s.mcp_timeout_seconds,
            breaker=AsyncCircuitBreaker(
                name="email-mcp",
                failure_threshold=s.circuit_breaker_failure_threshold,
                reset_seconds=s.circuit_breaker_reset_seconds,
            ),
            name="email",
        ),
    )


__all__ = [
    "APToolset",
    "CircuitOpenError",
    "DATEVPostResult",
    "DATEVPosting",
    "EmailMessage",
    "KreditorLookupResult",
    "POLine",
    "POLookupResult",
    "WareneingangEntry",
    "WareneingangLookupResult",
    "build_ap_toolset",
]
