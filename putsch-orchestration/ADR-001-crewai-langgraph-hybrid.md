# ADR-001: CrewAI + LangGraph hybrid orchestration

| Status   | Accepted                                                      |
| -------- | ------------------------------------------------------------- |
| Date     | 2026-05-18                                                    |
| Authors  | AI Platform team, Putsch Group                                |
| Deciders | Architect, Leiter Kreditorenbuchhaltung, Betriebsrat liaison  |

## Context

Putsch Group is building production-grade agentic automation for the AP
(Accounts Payable / Kreditorenbuchhaltung) function. The first workflow
to be automated is **Eingangsrechnung** end-to-end: intake from email
and Belege online, OCR via Docling, three-way match against SAP PO and
Wareneingang, posting to DATEV, exception routing.

The workflow has properties that pull in two directions:

1. **Team-shaped work.** The way Putsch's back office is staffed maps
   one-to-one onto agent roles: Kreditorenbuchhaltung-Agent,
   Auftragsbearbeitungs-Agent, Zoll-Agent, Stammdaten-Agent. A
   framework that gives us first-class role-and-team abstractions
   reduces the design-to-code gap dramatically.
2. **Durable, auditable, long-running execution.** Approvals can take
   days (Sachbearbeiter → Abteilungsleiter → Geschäftsführer cascade
   for invoices over €250k). Processes must survive pod restarts,
   tool outages, and DATEV maintenance windows. Every state transition
   must be replayable for audit, including GoBD-compliant trails.

No single framework excels at both.

## Decision

We adopt a **hybrid orchestration**:

- **CrewAI** owns the role-and-team abstraction *inside* a single business
  process. A "Crew" is a thing — a typed bundle of specialists, manager,
  and tools. The AP Crew packages the four AP specialists and the
  manager-agent that routes within them.
- **LangGraph** owns the durable-execution backbone *across* business
  processes. Postgres-backed checkpointing, `interrupt()` for
  human-in-the-loop, retry semantics, audit replay, conditional edges.
- **Crew-as-Node** is the integration pattern: every CrewAI Crew exposes
  an async `kickoff(state) -> CrewKickoffResult` method, wrapped by
  `build_crew_node()` into the LangGraph node interface.

Concretely:

```
LangGraph supervisor:
    START -> ingest -> extract(AP Crew) -> match(AP Crew) -> ...
                                                ↓
                            human_approval (interrupt)
                                                ↓
                                  post(AP Crew) -> finalize -> END
```

The same `APCrew` instance backs the `extract`, `match`, and `post`
nodes — the Crew dispatches internally on the current `InvoiceStatus`.
The graph decides *when* to apply the Crew; the Crew owns *how*.

## Rejected alternatives

### 1. CrewAI-alone

**Why it's tempting.** ~45,900 GitHub stars, MIT-licensed, native MCP +
A2A in v1.10.1, a roughly 60% reduction in code volume versus LangGraph
for the same hello-world Crew. ~450M monthly workflow executions in
production globally. Maps directly to how the Putsch back office is
organized; whoever inherits this repo will look at the LangGraph code
and ask "why do we need the verbose part?"

**Why we rejected it.**

- **No durable execution.** CrewAI's checkpointing is lightweight and
  in-process. A pod restart mid-workflow loses the work. A week-long
  approval cycle cannot be modeled cleanly. We cannot ship a system to a
  Mittelstand customer whose AP workflow regularly involves
  multi-day waits if the workflow vanishes on a redeploy.
- **Cyclic/conditional flows are painful.** Putsch's AP process is not
  linear — partial-match-with-vendor-clarification-and-resubmit is a
  real branch. CrewAI's hierarchical-process mode handles routing
  inside a Crew but not across them; we'd end up writing our own
  state machine on top, which is exactly what LangGraph already is.
- **HITL is retrofit.** CrewAI human-input flows assume a synchronous
  prompt-response cycle. Production HITL at Putsch is asynchronous:
  Sachbearbeiter receives a Teams notification, opens an internal tool
  days later, approves. `interrupt()` + checkpointed state matches
  this exactly; CrewAI's pattern would require us to invent durability.
- **Audit replay is thin.** Reproducing a posting from six months ago,
  byte-for-byte, against the same model weights and prompts, requires
  the runtime to log every transition with the prompt-artifact hash.
  LangGraph's checkpointing is built for this; CrewAI's is not.

**The trap.** "CrewAI-alone works in our prototype." Yes — every
agent framework works in the prototype. Production breaks on the failure
modes the prototype skips: process crashes, week-long approval cycles,
tool outages mid-workflow, replay-after-six-months audits. CrewAI's
strengths (team metaphor, declarative roles) are still ours; we just
don't let CrewAI own the spine.

### 2. LangGraph-alone

**Why it's tempting.** 34.5M monthly PyPI downloads — ~7× CrewAI's
production footprint. LangGraph 1.0 GA (Oct 2025) ships everything we
need on the durability side. Verified enterprise deployments at Klarna,
Uber, LinkedIn, BlackRock, Cisco, JPMorgan. On Princeton's HAL benchmark,
framework choice swings GAIA scores by 7+ points on identical models;
LangGraph sits at the top of that distribution. If we were betting on
one framework's longevity, this is it.

**Why we rejected it.**

- **No role abstraction.** Every agent team has to be rebuilt from
  graph primitives. We would write the AP Crew as a 200-line
  StateGraph with four "specialist" nodes hand-wired together, then do
  the same thing again for the AP Crew, the Zoll Crew, the Stammdaten
  Crew. That's ~800 lines of mechanical glue per Crew that CrewAI
  generates from ~80 lines of role definitions.
- **Manager-agent pattern is absent.** CrewAI's hierarchical process
  with a manager-agent is exactly how Putsch's actual back office
  operates (Teamleiter routes the team's work). Rebuilding this
  primitive in LangGraph means writing a supervisor-of-specialists
  inside each Crew — *and* having a supervisor-of-Crews at the
  top — which doubles the conceptual load on the team.
- **Code legibility for the domain expert.** A CrewAI agent definition
  reads like a role description; a LangGraph node reads like a state-
  machine handler. The Putsch finance team must be able to read the
  agent definitions and recognize their own organizational chart.
  LangGraph alone trades that legibility for graph machinery the
  finance team has no reason to learn.
- **DSPy integration is more idiomatic against an agent role.** Wiring
  DSPy modules per LangGraph node would distribute prompt artifacts
  across the graph instead of clustering them by domain — making the
  AP Crew's prompts a different file family from the Match Crew's
  prompts. CrewAI's role-centric model gives us one place per role
  for the prompt artifact.

**The trap.** "LangGraph has every primitive we need." Technically true,
which is exactly the problem. We would spend half the project building
abstractions on top of LangGraph that CrewAI already gives us, and the
other half explaining those abstractions to the finance domain experts
whose process we're encoding.

### 3. Microsoft Agent Framework (AutoGen + Semantic Kernel)

Reaches v1.0 GA in April 2026. Only worth considering if Putsch
standardizes on .NET / Azure. Putsch is Python + on-prem + Frankfurt-
hosted; the Microsoft framework would force a stack change in the
opposite direction from our actual constraints (Mistral La Plateforme +
on-prem HF inference, no Azure dependency). Not adopted.

## Consequences

### Positive

- **Domain legibility.** AP analysts can read `crews/ap/agents.py` and
  recognize their team. They can read `graph.py` and recognize the
  invoice lifecycle. Each file maps to one mental model.
- **Durability without sacrificing role abstraction.** LangGraph's
  checkpointing covers our durability story end-to-end; CrewAI's role
  abstraction covers our legibility story.
- **Easy module plug-in.** Memory, observability, prompt compilation
  each have a single integration point each. No retrofit.
- **Composable across future Crews.** Adding the Auftragsbearbeitung
  Crew is `crews/auftrag/` plus a new graph node. The pattern is set.

### Negative

- **Two mental models.** Engineers need to internalize where role logic
  lives (inside Crew) vs. where process logic lives (inside graph).
  This is solved with documentation and code review; the README and
  this ADR exist for exactly that reason.
- **Two upgrade paths.** Each framework versions independently; we
  track both. Mitigation: pin both in `pyproject.toml`, run a weekly
  upgrade-readiness CI job that tries the next minor of each.
- **Marginal verbosity.** A pure-CrewAI prototype is ~80 lines for the
  same workflow; we ship more code. We accept that — the extra code is
  durability, audit, and the typed seams future modules need.

## Migration paths if either framework stalls

We track both frameworks' health. Indicators that we would consider
migrating:

- **CrewAI stalls / forks.** The role abstraction lives in
  `crews/ap/agents.py`. If CrewAI development stops, the role
  metaphors there can be re-targeted at LangGraph's `Send` API or at
  LangChain agent classes without changing the graph spine. The
  Crew-as-Node interface insulates the supervisor from the change.
- **LangGraph stalls.** The graph spine lives in `graph.py`. The Crew
  contract returns `CrewKickoffResult` updates that compose into a
  partial state dict; that dict shape is framework-independent. We
  could re-target the spine onto Temporal, Inngest, or a hand-rolled
  Postgres-backed durable engine without touching the Crew.

The Crew-as-Node interface is the strategic abstraction that keeps
both migration paths cheap. Treating it like a public API — versioning,
documenting, testing — is non-negotiable.

## Open questions, intentionally deferred

- **Sub-Crew checkpoints.** We currently checkpoint at Crew boundaries.
  Sub-Crew checkpoints (mid-Crew state preservation) might help for
  long-running OCR jobs but would complicate recovery. Revisit when
  median Crew kickoff exceeds 60s; today it's under 8s.
- **Manager-agent vs. supervisor edge cases.** Today the manager-agent
  is confined to routing *within* the AP Crew. If a manager-agent
  reasons across Crews (e.g. "this invoice should go to the
  Auftragsbearbeitung Crew instead"), that's a graph-level decision —
  the supervisor must own it. Revisit if cross-Crew routing becomes
  common; current evidence is that it won't.
- **Streaming `interrupt()`.** LangGraph 0.4 (April 2026) adds richer
  streaming support around interrupts. The current `interrupt()` -
  resume payload pattern is sufficient for the human-approval UI; we
  re-evaluate when the UI module begins demanding partial-state
  streaming.

## Decision review

This ADR is reviewed annually or on any of:
- CrewAI or LangGraph major-version bump
- A new Crew added to the system (does the pattern still scale?)
- A production incident traceable to the hybrid pattern itself
