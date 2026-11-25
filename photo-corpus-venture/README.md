# Photo-corpus venture search

A seed-stage idea search, run as a hostile iteration loop. The seed idea is a user-owned,
AI-indexed photo/media corpus (migrated out of Apple/Google, queryable by any AI model).

This directory is the state. Nothing important lives only in a chat transcript.

## Layout

| Path | What it holds |
|---|---|
| `variants/v0.md` | The seed idea, as received, untouched |
| `variants/current.md` | The current best variant after each round |
| `variants/<name>.md` | Every variant generated, winner or loser |
| `critiques/<variant>-<round>.md` | Fresh-context critic output: scores + single most damaging objection |
| `research/<track>.md` | One file per research question, every number tagged, every claim dated and sourced |
| `SCORECARD.md` | The rubric, and the score of every variant with evidence pointers |
| `CHANGELOG.md` | Per-round log: what changed, why, what was learned, readable cold |
| `GRAVEYARD.md` | Every rejected variant with the reason it died |
| `pitch/` | Final deliverables, written only after the stop condition |

## Number tagging

Every number is tagged one of:

- `[sourced: <url>]` — a primary or near-primary source, with date
- `[estimated: <method>]` — a derivation; the method must be reproducible from the stated inputs
- `[unknown]` — we looked and could not find it

A fabricated number is a failed round.

## Operating rules (abridged)

1. Falsify first. For each load-bearing assumption, look for evidence it's wrong before evidence it's right.
2. Critique with fresh eyes. Each critique is a separate subagent that sees the variant and the rubric, not the author's reasoning.
3. Diverge before converging. Each round produces at least 3 materially different variants.
4. No invented customer quotes, no invented TAM. "Unknown" is a valid answer.
5. Argue positions, not personas. No roleplay of real people.
