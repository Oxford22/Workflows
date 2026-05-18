"""Crews — the team metaphor for in-process agent workflows.

Each subpackage under `crews/` is one Crew. The AP Crew (Eingangsrechnung)
is the first; future Crews — Auftragsbearbeitung, Zoll, Stammdaten —
follow the same shape:

    crews/<name>/
        signatures.py   DSPy signatures, the typed prompt artifacts
        tools.py        MCP wrappers with retry + circuit breaker
        tasks.py        Typed CrewAI Task inputs/outputs
        agents.py       Specialists, manager
        crew.py         Crew assembly + async kickoff

`crews/node.py` exposes the Crew-as-Node contract: the public API that
turns any Crew into a LangGraph node. Treat that file like a public API.
"""

from __future__ import annotations

from putsch_orchestration.crews.node import (
    CrewAsNode,
    CrewKickoffResult,
    build_crew_node,
)

__all__ = ["CrewAsNode", "CrewKickoffResult", "build_crew_node"]
