"""Async circuit breaker.

Three states: CLOSED (pass through), OPEN (reject immediately), HALF_OPEN
(allow one probe). Transitions:

    CLOSED   --failure_threshold consecutive failures--> OPEN
    OPEN     --reset_seconds elapsed--------------------> HALF_OPEN
    HALF_OPEN--success--> CLOSED;  --failure--> OPEN

Why we built our own instead of pulling in `pybreaker` or `circuitbreaker`:
both are sync-first and stash state in module globals, which makes resetting
per-test painful and per-instance configuration impossible. This is ~80 lines
and easier to audit.
"""

from __future__ import annotations

import asyncio
import enum
import time
from collections.abc import Awaitable, Callable
from dataclasses import dataclass, field
from typing import TypeVar

from putsch_orchestration.logging_setup import get_logger
from putsch_orchestration.state import ToolError

T = TypeVar("T")

_log = get_logger(__name__)


class CircuitState(str, enum.Enum):
    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


class CircuitOpenError(ToolError):
    """Raised when a call is rejected because the circuit is OPEN.

    Subclass of ToolError so the calling node's exception handler treats
    it like any other tool failure (route to exception state), rather
    than as something inherently fatal."""


@dataclass
class AsyncCircuitBreaker:
    """Per-instance async circuit breaker. One per external dependency.

    Usage:
        sap_breaker = AsyncCircuitBreaker(name="sap-mcp", failure_threshold=5)
        result = await sap_breaker.call(sap_client.lookup_po, po_number)
    """

    name: str
    failure_threshold: int = 5
    reset_seconds: float = 60.0

    _state: CircuitState = field(default=CircuitState.CLOSED, init=False)
    _consecutive_failures: int = field(default=0, init=False)
    _opened_at: float | None = field(default=None, init=False)
    _lock: asyncio.Lock = field(default_factory=asyncio.Lock, init=False, repr=False)

    @property
    def state(self) -> CircuitState:
        return self._state

    async def _transition_if_due(self) -> None:
        """Move OPEN -> HALF_OPEN once the cooldown has elapsed."""
        if self._state is CircuitState.OPEN and self._opened_at is not None:
            if time.monotonic() - self._opened_at >= self.reset_seconds:
                self._state = CircuitState.HALF_OPEN
                _log.info("circuit.half_open", circuit=self.name)

    async def call(
        self, func: Callable[..., Awaitable[T]], /, *args: object, **kwargs: object
    ) -> T:
        async with self._lock:
            await self._transition_if_due()
            if self._state is CircuitState.OPEN:
                raise CircuitOpenError(f"circuit '{self.name}' is OPEN")

        try:
            result = await func(*args, **kwargs)
        except Exception:
            async with self._lock:
                self._consecutive_failures += 1
                if (
                    self._state is CircuitState.HALF_OPEN
                    or self._consecutive_failures >= self.failure_threshold
                ):
                    self._state = CircuitState.OPEN
                    self._opened_at = time.monotonic()
                    _log.warning(
                        "circuit.opened",
                        circuit=self.name,
                        consecutive_failures=self._consecutive_failures,
                    )
            raise
        else:
            async with self._lock:
                if self._state is CircuitState.HALF_OPEN:
                    _log.info("circuit.closed", circuit=self.name)
                self._state = CircuitState.CLOSED
                self._consecutive_failures = 0
                self._opened_at = None
            return result

    def force_open(self) -> None:
        """Test hook: force the circuit OPEN."""
        self._state = CircuitState.OPEN
        self._opened_at = time.monotonic()

    def reset(self) -> None:
        """Test hook: force CLOSED, zero counters."""
        self._state = CircuitState.CLOSED
        self._consecutive_failures = 0
        self._opened_at = None


__all__ = ["AsyncCircuitBreaker", "CircuitOpenError", "CircuitState"]
