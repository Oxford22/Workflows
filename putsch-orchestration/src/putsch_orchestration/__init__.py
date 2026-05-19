"""Putsch Group orchestration spine.

CrewAI + LangGraph hybrid: CrewAI Crews are durable LangGraph nodes. State,
checkpoints, retries, and human-in-the-loop are owned by the graph; the team
metaphor inside a single business process is owned by the Crew.

Public surface area is intentionally small. Anything not exported here is an
implementation detail and may change without an ADR.
"""

from __future__ import annotations

from putsch_orchestration.sanitize import (
    SourceTag,
    TaintedText,
    strip_instruction_patterns,
    wrap_external_content,
)
from putsch_orchestration.state import (
    AgentMessage,
    CheckpointError,
    CrewError,
    InterruptError,
    InvoiceState,
    InvoiceStatus,
    LineItem,
    MatchOutcome,
    NodeError,
    OrchestrationError,
    PostingDecision,
    ThreeWayMatch,
)

__all__ = [
    "AgentMessage",
    "CheckpointError",
    "CrewError",
    "InterruptError",
    "InvoiceState",
    "InvoiceStatus",
    "LineItem",
    "MatchOutcome",
    "NodeError",
    "OrchestrationError",
    "PostingDecision",
    "SourceTag",
    "TaintedText",
    "ThreeWayMatch",
    "strip_instruction_patterns",
    "wrap_external_content",
]

__version__ = "0.1.0"
