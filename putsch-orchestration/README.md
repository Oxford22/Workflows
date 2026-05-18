# Putsch Orchestration

The CrewAI + LangGraph orchestration spine for Putsch Group's AP
(Eingangsrechnung) workflow. This package is the **substrate** that the
rest of the Putsch agentic stack — Docling, the Magentic-One-pattern
swarm, Langfuse, Zep+Graphiti, DSPy — plugs into. It is not a tutorial.

> This README documents *why* the package is shaped the way it is.
> API reference belongs next to the code; what matters here is the
> architectural decisions that the next senior engineer to inherit this
> repo will be tempted to overturn.

## TL;DR

- **CrewAI** owns the *team* metaphor inside one business process. Four
  specialists (Eingangs-, OCR-, Match-, Buchungs-Agent) plus a manager-agent
  collaborate on one Eingangsrechnung.
- **LangGraph** owns the *process* the Crew runs inside. Durable state in
  Postgres, retries, `interrupt()` for human approval, audit replay.
- **The Crew is a node.** Every Crew kickoff is a checkpoint boundary.
  No in-flight Crew survives a process crash — by design.
- Everything else is wired so the remaining modules (memory, observability,
  prompt compilation) plug in without retrofitting.

## Why hybrid (not CrewAI-alone, not LangGraph-alone)

See `ADR-001-crewai-langgraph-hybrid.md` for the long form. The short
version: CrewAI gives us a clean role-based interface that maps directly
to how Putsch's back office is staffed; LangGraph gives us durable
execution that survives the things that actually break in production
(process restart, week-long approval cycles, mid-workflow tool
unavailability). Each framework's weakness is exactly the other's
strength. The pattern most Fortune 500 production teams converged on in
2026 is the hybrid; this package is that pattern, applied.

## The spine

```
                                                          (LangGraph supervisor)
                  +-----------+      +---------+      +--------------+      +---------+      +----------+
   START -------> |  ingest   | ---> | extract | ---> | route_after  | ---> |  post   | ---> | finalize | --> END
                  +-----------+      +---------+      |   _extract   |      +---------+      +----------+
                                       (AP Crew)      +--------------+         (AP Crew)
                                                            |
                                                            v
                                                      +---------+
                                                      |  match  |  (AP Crew)
                                                      +---------+
                                                            |
                                                            v
                                                +-------------------+
                                                | route_after_match |
                                                +-------------------+
                                                  |    |        |
                                            auto  |    | partial| match exception
                                                  v    v        v
                                              +------+ +--------+
                                              | post | |  human  |   <-- interrupt(); days OK
                                              +------+ |approval|
                                                       +--------+
```

Six nodes. Each is async. Each is a checkpoint boundary. The Crew is
**reused across three nodes** (extract, match, post) — the Crew dispatches
on the current `InvoiceStatus`. That's deliberate: the Crew owns the AP
domain knowledge; the graph owns the process. One Crew, three uses.

## The deliberate constraints

These look like limitations until you've debugged an agent crash at 3am.

1. **Crews are nouns; workflows are verbs.** The AP Crew is a *thing*; the
   graph is the *process* that uses it. Don't put workflow logic inside the
   Crew. Don't put domain knowledge inside the graph.
2. **No in-flight Crew survives a process restart.** Recovery resumes
   from the last node boundary. Sub-Crew checkpoints would be cute and
   expensive; we don't ship them.
3. **Manager-agent is not an orchestrator.** The CrewAI manager-agent
   routes *within* a Crew. The LangGraph supervisor routes *across*
   them. Mixing the two is the most common architecture mistake in the
   space.
4. **HITL is first-class, not an exception path.** `human_approval` is a
   normal node. `interrupt()` is as natural as autonomous transition.
   Most production agent failures are retrofitted HITL; this one is
   built in from the first commit.
5. **Agents communicate via Pydantic envelopes.** Strings between agents
   are grounds for rejection in code review. The LLM sees a rendered
   prompt; the Python code sees a `Match Input`/`MatchOutput` pair.

## Where the other modules plug in

The orchestration spine is designed so each future module slots in
without retrofit:

| Module                | Plug-in seam                                                     |
| --------------------- | ---------------------------------------------------------------- |
| Docling layer         | `crews/ap/tools.py` — Email-MCP returns Docling-extracted text   |
| Magentic-One swarm    | Wraps inside a future `crews/swarm/` package; same CrewAsNode    |
| Langfuse              | `obs_hooks.py` exporter swap (`otel_exporter=otlp`)              |
| Zep + Graphiti memory | `memory_hooks.py` — replace `NoopMemoryHooks` with the real impl |
| DSPy compilation      | `crews/ap/signatures.py` is already DSPy; compile artefacts      |

Each seam is a tested interface today. The placeholder implementations
are no-ops, not stubs that throw — the graph runs end-to-end with them.

## Quick start

```bash
# 1. Bring up Postgres + LiteLLM stub.
docker-compose up -d postgres litellm

# 2. Local dev — install with the dev extras.
pip install -e .[dev]
cp .env.example .env

# 3. Run the unit suite. No network, no DB.
pytest -m "not integration and not chaos and not slow"

# 4. Run the integration suite (in-memory checkpointer).
pytest -m integration

# 5. Drain a synthetic invoice end-to-end.
python -m putsch_orchestration run-once \
    --source-uri s3://test/demo.pdf \
    --raw-text "$(cat samples/clean.txt)"
```

## Operational notes

- **Type discipline:** `mypy --strict src tests` must pass. PRs that
  add `Any` or `# type: ignore` without justification get rejected.
- **Logging:** structlog JSON, every line carries `correlation_id` and
  `service`. Invoice content (OCR text, vendor names, IBANs) is
  redacted by default — set `PUTSCH_LOG_INVOICE_CONTENT=true` only in
  local dev with synthetic data, and only with Betriebsrat sign-off in
  staging. Production must never enable this without a written change.
- **Retries:** every external call is wrapped in tenacity + a per-system
  circuit breaker. The breaker state is per-instance, not global — the
  unit tests can force-open it to drill the failure path.
- **HITL durability:** `interrupt()` is the only way humans enter the
  loop. Resume payloads are validated at the boundary; a malformed
  resume raises `NodeError` and the supervisor records it on history.

## Where to look first

1. `src/putsch_orchestration/state.py` — the contract every other file
   depends on. Read this once before touching anything else.
2. `src/putsch_orchestration/crews/node.py` — the Crew-as-Node public
   API. Treat changes here like a public-API bump: ADR + minor version.
3. `src/putsch_orchestration/graph.py` — the supervisor topology.
4. `ADR-001-crewai-langgraph-hybrid.md` — the architectural rationale.
   Read this before proposing "let's just use CrewAI / LangGraph alone".
