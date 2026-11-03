# SCORECARD

## Rubric (1–10 each; every score needs an evidence pointer)

| # | Dimension | What a 10 looks like | What a 3 looks like |
|---|---|---|---|
| 1 | Pain | Acute, frequent, currently paid for with money or hours | Nice-to-have; nobody pays today |
| 2 | Wedge | First use case adopted without changing habits | Requires behavior change before any value |
| 3 | Why now | A specific, dated change in the world since 2024 that makes this possible/necessary | Could have been built in 2019 |
| 4 | Platform risk | Survives Apple/Google shipping the obvious feature | Dies the day a WWDC slide shows it |
| 5 | Compounding asset | Data, network, or workflow that gets harder to replace with every month of use | Fully replaceable; no switching cost |
| 6 | Distribution | A credible non-paid acquisition channel with evidence it works | Paid ads only |
| 7 | Economics | Gross margin and payback modeled with tagged numbers | Numbers absent or untagged |
| 8 | Buildability | Core loop demoable in 4 weeks by 2 engineers | Needs a platform partnership or a research breakthrough |
| 9 | Ceiling | Believable path to $100M ARR with the math | TAM is a hand-wave |
| 10 | Founder fit | Strengths/constraints/runway stated by founder and matched | Unknown |

Founder fit is scored as [unknown] until the founder fills in strengths, constraints and runway.
A score of 5 is used as a neutral placeholder in totals and flagged.

## Scoring rules
- Each score must point to a file in `research/` or `critiques/` that justifies it.
- Scores come from fresh-context critics, not from the author of the variant.
- When multiple critics score the same variant, the scorecard records the median and the spread.

## Scores

| Variant | Round | 1 Pain | 2 Wedge | 3 Why now | 4 Platform | 5 Asset | 6 Distrib | 7 Econ | 8 Build | 9 Ceiling | 10 Fit | Total | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| v0 (seed) | 0 | 4 (4–5) | **2** (2–3) | 5 (5–6) | 3 (3–4) | 4 (3–5) | 3 (3–3) | 5 (4–5) | 5 (3–6) | 3 (2–3) | 5 [unknown] | **39** | critiques/v0-r0-{investor,builder,customer}.md; research/assumptions/A1–A6.md |
| v1-federation (family index, no migration) | 1 | 3 (3–4) | 4 (4–5) | 5 (5–6) | 4 (3–4) | 4 (4–4) | 3 (3–4) | 6 (6–6) | 6 (6–6) | 3 (2–3) | 5 [unknown] | 43 | critiques/v1-federation-r1-*.md |
| **v1-organizer (pro consolidation workbench, B2B2C)** | 1 | 5 (5–6) | 6 (5–6) | 5 (4–5) | 4 (4–5) | 4 (3–4) | 4 (4–6) | 6 (5–6) | 6 (6–6) | **2** (2–3) | 5 [unknown] | **47** | critiques/v1-organizer-r1-*.md |
| v1-estate (bereavement event wedge) | 1 | 4 (4–5) | 4 (3–5) | 4 (4–5) | 4 (3–4) | 3 (3–3) | 3 (3–4) | 5 (5–6) | 4 (3–5) | 3 (2–3) | 5 [unknown] | 39 | critiques/v1-estate-r1-*.md |
| v1-trades (camera-roll job memory, vertical) | 1 | 5 (5–6) | 6 (5–6) | 5 (5–5) | 3 (3–4) | 4 (3–4) | 3 (3–3) | 7 (6–7) | 6 (5–7) | 3 (2–4) | 5 [unknown] | 47 | critiques/v1-trades-r1-*.md |

Cell format: median (min–max) across the three critics. Totals use medians; founder fit is a flagged neutral 5.

## Round 0 evidence summary (why v0 scores 39)

| Dim | Median | The fact that set the score | Pointer |
|---|---|---|---|
| Pain | 4 | Hours are real and recur 2019–2026, but nobody was found paying for the merge itself; adjacent spend (scanning $0.49–1.28/print, organizers $50–150/hr, Tinybeans $75 ARPU) is for other jobs | research/assumptions/A3.md; research/customers.md Q1(g), Q2 |
| Wedge | 2 | Both wedges need full-library migration first; 12 months after Apple shipped the iOS 26.1 Background Resource Upload extension, no major app (Ente, Immich, Google Photos, Dropbox) has made unattended initial upload work | research/assumptions/A2.md; research/platform-access.md Q2 |
| Why now | 5 | Dated changes exist (MCP 2024-11, iOS 26.1 extension 2025-10, caption cost ~16–20x down) but each helps Apple/Google at least as much; cross-generation faces has no why-now (score 2) | research/ai-why-now.md §6 |
| Platform risk | 3 | Apple and Google already ship *closed* AI over their corpora (Gemini↔Photos 2025-03; Siri AI 2026-09); iOS 27 Foundation Models lets any app run Claude/Gemini with tool calling over the user's existing library, removing the need to migrate at all | research/assumptions/A4.md Against #4–#5 |
| Compounding asset | 4 | Index rebuildable for <$1; MCP is a commodity (54,763 active registry servers; 28 Immich MCP repos); only user-confirmed cross-account identities and voice notes could compound, and v0 doesn't price them | research/byo-ai.md Q5; research/unit-economics.md Q3 |
| Distribution | 3 | No evidenced non-paid channel; organizer channel is ~700 members at 1–3 clients/month; max tolerable CAC on a monthly plan is $3–9 (RevenueCat Photo & Video first monthly renewal 48%) | research/customers.md Q1(e); research/unit-economics.md Q6–Q7 |
| Economics | 5 | Fully tagged model: storage is 93–97% of variable infra; replicated "outlives any account" storage yields −2% to 53% GM at market prices; single-copy B2 clears 59–74%; index-only clears 86% | research/unit-economics.md Q7; research/assumptions/A5.md |
| Buildability | 5 (3–6) | Widest disagreement. Mac+Takeout demo is 4 weeks; the product as written (unattended iOS migration + automatic cross-generation faces) is unproven / open research | research/assumptions/A2.md; research/ai-why-now.md Q3 |
| Ceiling | 3 | No $100M math anywhere; Ente 21,807 paid, Tinybeans ~95k paid at $6.5M revenue; every consumer whole-library storage independent is small, flat, subsidized or dead | research/competitive.md Q5; research/unit-economics.md Q6 |
| Founder fit | 5 | [unknown] — founder questionnaire in CHANGELOG | — |

## Assumption ledger (from research/assumptions/)

| ID | Assumption | Verdict | Conf | One-line reason |
|---|---|---|---|---|
| A1 | Google removed 3rd-party library read (2025-03-31) and it's durable | holds | 0.75 | Google's own updates page; no DMA lever (Photos is not a designated core platform service) |
| A2 | Full-library export off iOS is feasible with acceptable friction | partial | 0.72 | Feasible on paper (iOS 26.1/27 extension); no major app has shipped it; Mac path works but is fragile |
| A3 | A segment pays for the merged multi-relative archive | partial | 0.60 | Pain recurs; money flows to adjacent jobs (scanning, organizers, legacy), not to "merge" |
| A4 | Apple/Google won't ship merge + open AI access | partial | 0.60 | Merge clause holds; "AI access" shipped closed by both; Apple gives every app Claude/Gemini over the existing library |
| A5 | Storage+index per 100GB clears 60% GM at ≤$10/mo | partial | 0.70 | Index-only 86%; single-copy B2 59–74%; replicated ≤53% |
| A6 | Assistants let consumers attach a private corpus with low friction | partial | 0.60 | Claude: Free tier, mobile, no review. ChatGPT/Gemini: web-only setup, tier gates, US/English |

## Contradictions resolved (primary wins)

- CompanyCam customers: 170,000 [sourced: companycam.com/press, 2024-02-28] (not 140,000).
- Ente paying share: 21,807 paid / 490,639 registered ≈ 4.4%, ~$1.41M revenue [sourced: ente.com/open, 2026-11-03]; competitive.md's 11% illustration is withdrawn.
- A6 status: partial (0.60) per research/assumptions/A6.md; ai-why-now.md's "holds" is superseded.
- A4 status for v0: partial (0.60) — merge clause holds, open-AI clause eroded. verticals.md's "broken" applies to verticals only (CompanyCam MCP beta 2026-09-09).
- Siri AI languages: Apple newsroom 2026-09-14 says English at launch; apple.com footnote lists six languages "to start". Recorded as English-first, six languages rolling.
- Photo Managers: >700 members [sourced: einpresswire 2024-02, secondary]; rates $50–150/hr (association articles 2026-04/08).
- CAC anchor: Qeepsake CAC $35 [sourced: Tinybeans Q3 FY26 ASX filing] is the one sourced photo-app CAC; unit-economics.md's [unknown] is superseded for sensitivity purposes.
- Caption cost per 100k photos (Gemini 2.5 Flash-Lite): $6–13 depending on image resolution assumption (768 px vs 1024 px). Both are tagged; use the range.
- Google One 200 GB tier: customers.md says $4.99 (CNBC 2026-02-28); unit-economics.md lists 100 GB $1.99 and 400 GB "AI Plus" $4.99. Open — to verify on one.google.com.

## Round 1 evidence summary (why the top moved 39 → 47 and stalled on Ceiling)

| Variant | What lifted it | What capped it | Pointer |
|---|---|---|---|
| v1-organizer (winner, 47) | Wedge 6: slots into a workflow the organizer is already paid for; Buildability 6: Mac-first, osxphotos names+regions, Takeout repair; Economics 6: compute on the organizer's Mac | Ceiling 2: seat cap ≈ $9.8M at 100% of ~7,800 adjacent pros; realistic $3–12M; projects per organizer per year [unknown]; hourly-billing organizers lose from automation; Mylio dropped off the 2026 TPM sponsor list | critiques/v1-organizer-r1-investor.md; research/pro-channel.md Q1, Q7 |
| v1-trades (47) | Economics 7 (per-company SaaS, index-only); Wedge 6 | Platform 3: CompanyCam already ships GPS-matched camera-roll import (Magic Uploader), text scanning, an MCP server, and raised $415M; crew photos arrive by iMessage and are invisible to PhotoKit; $12/mo pricing tops out at $17–34M | critiques/v1-trades-r1-*.md; research/trades-and-reddit.md A2, A4 |
| v1-federation (43) | Economics/Buildability 6: index-only, on-device, 86% GM | Pain 3: 156 Reddit posts / 178 comments, nobody pays or is told to pay for a merge; Google Photos is already installed on the iPhone side of mixed households; Android index deferred; on-device wall-clock 38–57 min central, Camera kills the task | critiques/v1-federation-r1-*.md; research/ios-feasibility.md Q3; research/trades-and-reddit.md Part B |
| v1-estate (39) | Pain 4–5 at the event | Tukios already collects relatives' phone photos for tribute videos at 10,000+ funeral homes; Apple Data & Privacy export contents unverified; most decedents have no Legacy Contact; one-time $149 needs ~1M estates/yr for $100M | critiques/v1-estate-r1-*.md; research/estate.md funnel table |

Rule reminder: v1-trades tied v1-organizer on median total; the tie went to organizer on mean critic total (47.3 vs 46.7) and because trades' lowest scores are structural (incumbent has shipped the feature; crew photos unreachable).

## Weakest dimension (drives next round)
**Ceiling (2–3 on every round-1 variant).** No variant has an evidence-backed path past ~$10–35M ARR. Round 2 variants must start from a pool where money already flows at scale (research/sizing.md worked chains; research/pro-channel.md Q5; research/customers.md Q1(h)) and show the $100M arithmetic with tagged inputs, or state the honest cap.
