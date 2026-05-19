"""AP Crew — Eingangsrechnung (incoming invoice) processing.

Specialists:
    Eingangs-Agent    intake from Email-MCP / Belege online
    OCR-Agent         Docling extraction wrapper
    Match-Agent       Drei-Wege-Abgleich against SAP PO + Wareneingang
    Buchungs-Agent    DATEV posting + commentary

Process: hierarchical. A Manager-Agent routes within the Crew when a
specialist signals an exception (e.g. OCR-Agent flags low confidence,
Match-Agent finds no PO). Cross-process decisions — autonomous post vs.
human approval, Sachbearbeiter vs. Abteilungsleiter routing — are
decided by the LangGraph supervisor, never by the manager-agent.
"""

from __future__ import annotations

from putsch_orchestration.crews.ap.crew import APCrew

__all__ = ["APCrew"]
