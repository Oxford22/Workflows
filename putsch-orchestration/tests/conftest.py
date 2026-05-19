"""Shared pytest fixtures.

The hard requirement: every test that touches state must work against an
in-memory checkpointer (`MemorySaver`) — Postgres lives in docker-compose
and is exercised by the integration / chaos suites only.
"""

from __future__ import annotations

import os
from collections.abc import AsyncIterator, Iterator
from decimal import Decimal
from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest

# Set test-friendly env BEFORE importing the package so pydantic-settings
# picks it up. Pytest auto-imports conftest before test modules.
os.environ.setdefault("PUTSCH_DATABASE_URL", "postgresql://test:test@localhost:5432/test")
os.environ.setdefault("PUTSCH_LITELLM_BASE_URL", "http://localhost:4000")
os.environ.setdefault("PUTSCH_LITELLM_API_KEY", "test-key")
os.environ.setdefault("PUTSCH_SAP_MCP_URL", "http://localhost:6001")
os.environ.setdefault("PUTSCH_DATEV_MCP_URL", "http://localhost:6002")
os.environ.setdefault("PUTSCH_EMAIL_MCP_URL", "http://localhost:6003")
os.environ.setdefault("PUTSCH_LOG_LEVEL", "WARN")
os.environ.setdefault("PUTSCH_OTEL_EXPORTER", "stdout")

from putsch_orchestration.config import get_settings  # noqa: E402
from putsch_orchestration.crews.ap.crew import APCrew  # noqa: E402
from putsch_orchestration.crews.ap.tasks import (  # noqa: E402
    IntakeOutput,
    MatchOutput,
    OCRLineItem,
    OCROutput,
)
from putsch_orchestration.crews.ap.tools import (  # noqa: E402
    APToolset,
    DATEVPostResult,
    KreditorLookupResult,
    POLine,
    POLookupResult,
    WareneingangEntry,
    WareneingangLookupResult,
)
from putsch_orchestration.logging_setup import configure_logging  # noqa: E402
from putsch_orchestration.sanitize import TaintedText  # noqa: E402
from putsch_orchestration.state import (  # noqa: E402
    IntakeChannel,
    InvoiceState,
    MatchOutcome,
)


@pytest.fixture(autouse=True)
def _logging() -> None:
    configure_logging()


@pytest.fixture
def settings() -> Any:
    get_settings.cache_clear()
    return get_settings()


@pytest.fixture
def fresh_state() -> InvoiceState:
    return InvoiceState(
        thread_id="01HNYZ8GZJKB6MGAZQQHEKQQ00",
        intake_channel=IntakeChannel.EMAIL,
        source_uri="s3://test/clean-invoice.pdf",
        raw_text=TaintedText(
            value=(
                "Rechnung Nr. 2026-1001\n"
                "Datum: 18.05.2026\n"
                "Mustermann GmbH, Hagen\n"
                "USt-ID: DE123456789\n"
                "Position 1: Stahlträger HEB-200 — 5 Stk x 100,00 EUR = 500,00 EUR\n"
                "Gesamt: 595,00 EUR inkl. 19% USt"
            ),
            source="ocr",
        ),
    )


@pytest.fixture
def mock_toolset() -> MagicMock:
    """A MagicMock APToolset with sensible defaults.

    Individual tests override the bits they care about; the defaults
    correspond to the 'clean match' scenario.
    """
    tools = MagicMock(spec=APToolset)
    tools.lookup_kreditor = AsyncMock(
        return_value=KreditorLookupResult(
            found=True,
            kreditor_number="K-100001",
            name="Mustermann GmbH",
            ust_id="DE123456789",
            iban=None,
        )
    )
    tools.lookup_po_by_vendor_and_invoice = AsyncMock(
        return_value=POLookupResult(
            found=True,
            po_number="PO-2026-555",
            kreditor_number="K-100001",
            lines=(
                POLine(
                    line_number=1,
                    material_number="HEB-200",
                    description="Stahltraeger HEB-200",
                    quantity_ordered=Decimal("5"),
                    quantity_received=Decimal("5"),
                    unit_price_cents=10000,
                    currency="EUR",
                    sachkonto="3400",
                    kostenstelle="KS-1100",
                ),
            ),
        )
    )
    tools.lookup_wareneingang = AsyncMock(
        return_value=WareneingangLookupResult(
            po_number="PO-2026-555",
            entries=(
                WareneingangEntry(
                    wareneingang_number="WE-700",
                    po_line_number=1,
                    quantity_received=Decimal("5"),
                    received_at="2026-05-17",
                ),
            ),
        )
    )
    tools.submit_posting = AsyncMock(
        return_value=DATEVPostResult(
            success=True,
            datev_belegnummer="DATEV-9001",
        )
    )
    tools.aclose = AsyncMock()
    return tools


@pytest.fixture
def patched_dspy(monkeypatch: pytest.MonkeyPatch) -> dict[str, Any]:
    """Patch the four DSPy runner functions in `crews.ap.crew`.

    Returning the dict lets a test override one runner per scenario.
    """
    from putsch_orchestration.crews.ap import crew as crew_mod

    state: dict[str, Any] = {
        "intake": IntakeOutput(
            document_kind="eingangsrechnung",
            vendor_name_guess="Mustermann GmbH",
            confidence=0.95,
            reasoning="Header enthaelt Rechnungsnummer und Kreditor.",
        ),
        "ocr": OCROutput(
            invoice_number="2026-1001",
            invoice_date_iso="2026-05-18",
            vendor_name="Mustermann GmbH",
            vendor_ust_id="DE123456789",
            total_amount_eur=Decimal("595.00"),
            currency="EUR",
            line_items=(
                OCRLineItem(
                    line_number=1,
                    description="Stahltraeger HEB-200",
                    quantity=Decimal("5"),
                    unit_price_eur=Decimal("100.00"),
                    line_total_eur=Decimal("500.00"),
                    tax_rate_pct=Decimal("19"),
                ),
            ),
            confidence=0.92,
            extraction_notes="",
        ),
        "match": MatchOutput(
            outcome=MatchOutcome.FULL,
            matched_line_numbers=(1,),
            unmatched_line_numbers=(),
            price_variance_cents=0,
            rationale="Alle Positionen stimmen ueberein.",
        ),
        "commentary": "K-100001 RN 2026-1001 KS-1100",
    }

    monkeypatch.setattr(crew_mod, "_run_classify_intake", lambda **_: state["intake"])
    monkeypatch.setattr(crew_mod, "_run_extract_fields", lambda **_: state["ocr"])
    monkeypatch.setattr(crew_mod, "_run_match_reasoning", lambda **_: state["match"])
    monkeypatch.setattr(crew_mod, "_run_compose_commentary", lambda **_: state["commentary"])
    return state


@pytest.fixture
async def ap_crew(
    mock_toolset: MagicMock,
    patched_dspy: dict[str, Any],  # noqa: ARG001
) -> AsyncIterator[APCrew]:
    """An APCrew instance with mocked toolset and DSPy.

    The CrewAI Agent objects are *not* mocked — they construct against
    the real LiteLLM stub. We never call `.kickoff()` on them in unit
    tests; the Crew's actual work routes through DSPy modules which we
    mock above.
    """
    crew = APCrew(name="ap", toolset=mock_toolset, agents=None, _dspy_configured=True)
    crew._settings = get_settings()
    yield crew
    await crew.aclose()


@pytest.fixture
def thread_config() -> dict[str, Any]:
    return {"configurable": {"thread_id": "test-thread-1"}}


@pytest.fixture
def _block_real_network(monkeypatch: pytest.MonkeyPatch) -> Iterator[None]:
    """Belt and braces: forbid httpx.AsyncClient.send during unit tests.

    Integration / chaos tests opt back in by overriding this fixture.
    """
    import httpx

    async def _forbidden(*args: object, **kwargs: object) -> Any:
        raise RuntimeError("real network call in unit test — mock the toolset")

    monkeypatch.setattr(httpx.AsyncClient, "send", _forbidden, raising=True)
    yield
