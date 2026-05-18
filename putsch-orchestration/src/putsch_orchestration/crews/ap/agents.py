"""AP Crew specialists.

Four specialists plus a manager-agent. Each specialist:
    - has a stable role identifier (mirrors AgentRole in models.py)
    - resolves its LLM via models.resolve_model — no hardcoded model strings
    - declares German role/goal/backstory for the CrewAI team metaphor
    - is wired to one DSPy module (the actual prompt artifact)

The German role text exists for CrewAI internal mechanics (manager-agent
prompts other agents using these descriptions). The real prompt work is
done by the DSPy modules in `signatures.py`.

Manager-agent routes within the Crew when a specialist signals a recoverable
exception (e.g. OCR confidence < 0.7 -> ask for re-extract; PO not found ->
ask Match-Agent to try a Kreditor lookup first). The manager DOES NOT
decide whether to escalate to a human — that's the LangGraph supervisor's
job. Mixing these is the most common AP-automation architecture mistake.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from crewai import LLM, Agent

from putsch_orchestration.config import Settings, get_settings
from putsch_orchestration.crews.ap.tools import APToolset
from putsch_orchestration.logging_setup import get_logger
from putsch_orchestration.models import AgentRole, ModelHandle, resolve_model

_log = get_logger(__name__)


def _make_llm(handle: ModelHandle) -> LLM:
    """Construct the CrewAI LLM wrapper. Routes through LiteLLM."""
    return LLM(
        model=handle.model,
        base_url=handle.api_base,
        api_key=handle.api_key,
    )


@dataclass(frozen=True)
class APAgents:
    """The bundle of AP Crew specialists, ready to assemble into a Crew."""

    eingangs: Agent
    ocr: Agent
    match: Agent
    buchung: Agent
    manager: Agent
    handles: dict[AgentRole, ModelHandle] = field(default_factory=dict)


def build_ap_agents(
    *,
    toolset: APToolset,  # noqa: ARG001
    settings: Settings | None = None,
) -> APAgents:
    """Construct all five AP agents from current settings.

    `toolset` is passed in but agents in this version don't get raw CrewAI
    tool wrappers — every external call happens inside the Crew kickoff
    coordinator (crew.py), keeping I/O on async paths and out of CrewAI's
    sync tool-call loop. The toolset reference is reserved so future agent
    revisions (e.g. CrewAI-native MCP support post-1.10) can wire tools
    onto agents without changing this signature.
    """
    s = settings or get_settings()

    eingangs_handle = resolve_model(AgentRole.EINGANGS_AGENT, s)
    ocr_handle = resolve_model(AgentRole.OCR_AGENT, s)
    match_handle = resolve_model(AgentRole.MATCH_AGENT, s)
    buchung_handle = resolve_model(AgentRole.BUCHUNGS_AGENT, s)
    manager_handle = resolve_model(AgentRole.MANAGER_AGENT, s)

    eingangs = Agent(
        role="Eingangs-Agent",
        goal=(
            "Eingehende Dokumente zuverlaessig als Eingangsrechnung erkennen "
            "und den Absender (Kreditor) erstklassifizieren."
        ),
        backstory=(
            "Du bist die erste Station der Kreditorenbuchhaltung der Putsch Group. "
            "Du behandelst Belege aus Email und Belege online. Du raetst nicht — "
            "im Zweifel markierst du das Dokument zur menschlichen Pruefung."
        ),
        llm=_make_llm(eingangs_handle),
        allow_delegation=False,
        verbose=False,
        max_iter=3,
    )

    ocr = Agent(
        role="OCR-Agent",
        goal=(
            "Strukturierte Rechnungsfelder mit kalibrierter Konfidenz aus dem "
            "OCR-Rohtext extrahieren. Bei Unsicherheit lieber das Feld leer "
            "lassen als raten."
        ),
        backstory=(
            "Du arbeitest direkt nach der Docling-Extraktion. Du beherrschst "
            "deutsche Rechnungsformate, USt-Satzgruppen (19/7/0) und das "
            "deutsche Zahlenformat (1.234,56)."
        ),
        llm=_make_llm(ocr_handle),
        allow_delegation=False,
        verbose=False,
        max_iter=2,
    )

    match = Agent(
        role="Match-Agent",
        goal=(
            "Drei-Wege-Abgleich zwischen Rechnung, Bestellung und Wareneingang "
            "durchfuehren und das Ergebnis sauber begruenden."
        ),
        backstory=(
            "Du kennst SAP MM. Du weisst, dass nicht jede Abweichung eine "
            "Exception ist — Preistoleranzen, Mengen-Rundungen und Teil-"
            "Wareneingaenge sind normal. Aber dolose Abweichungen markierst "
            "du sofort."
        ),
        llm=_make_llm(match_handle),
        allow_delegation=False,
        verbose=False,
        max_iter=3,
    )

    buchung = Agent(
        role="Buchungs-Agent",
        goal=(
            "Praezise, regelkonforme DATEV-Buchungstexte verfassen und die "
            "Buchung idempotent gegen DATEV einreichen."
        ),
        backstory=(
            "Du verfasst Buchungstexte, die ein Sachbearbeiter ohne Rueckfrage "
            "freigeben kann: nuechtern, vollstaendig, max. 60 Zeichen."
        ),
        llm=_make_llm(buchung_handle),
        allow_delegation=False,
        verbose=False,
        max_iter=2,
    )

    manager = Agent(
        role="AP-Manager-Agent",
        goal=(
            "Den Workflow innerhalb der AP-Crew orchestrieren: bei "
            "Spezialisten-Rueckfragen die richtige Folgeschritte einleiten."
        ),
        backstory=(
            "Du bist der erfahrene Kreditorenbuchhaltung-Teamleiter. Du "
            "entscheidest NICHT, ob eine Rechnung an einen Sachbearbeiter "
            "geht — das macht der uebergeordnete Workflow. Du entscheidest, "
            "ob das Team die Rechnung intern weiter bearbeiten kann."
        ),
        llm=_make_llm(manager_handle),
        allow_delegation=True,
        verbose=False,
        max_iter=5,
    )

    handles = {
        AgentRole.EINGANGS_AGENT: eingangs_handle,
        AgentRole.OCR_AGENT: ocr_handle,
        AgentRole.MATCH_AGENT: match_handle,
        AgentRole.BUCHUNGS_AGENT: buchung_handle,
        AgentRole.MANAGER_AGENT: manager_handle,
    }
    _log.info(
        "ap.agents.built",
        models={role.value: h.model for role, h in handles.items()},
    )

    return APAgents(
        eingangs=eingangs,
        ocr=ocr,
        match=match,
        buchung=buchung,
        manager=manager,
        handles=handles,
    )


def _agent_role_descriptor(agent: Agent) -> dict[str, Any]:
    """Used in tests + logs; never logs invoice content."""
    return {
        "role": agent.role,
        "goal": agent.goal,
        "model": getattr(getattr(agent, "llm", None), "model", "unknown"),
    }


__all__ = ["APAgents", "build_ap_agents"]
