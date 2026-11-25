# v4-claims — round 4 — cold seed investor

Written 2026-11-25. Variant scored: `variants/v4-claims.md`. Fresh context: I have not read the CHANGELOG, the other v4 variants, or any critique.

## Stance

Default is no. I am scoring who pays, how much, why now, the wedge, the distribution, and what must be true for a $1B+ outcome. Ceiling, Distribution and Platform risk are scored hardest. The variant was written before `research/contents-claims.md` was audited and repaired; where the two disagree, the research wins and the disagreement is listed below.

**What I read.** In full: `SCORECARD.md`, `variants/v4-claims.md`, `research/contents-claims.md` (including its audit log). Opening and bottom-line sections, plus every section the variant cites: `ai-data-licensing.md`, `frame-device-market.md`, `family-artifact-market.md`, `memoir-gift-market.md`, `face-regulation.md` (Q1, Q7), `sizing.md` (Q4, Q5, section 3), `unit-economics.md` (Q1, Q3, Q7), `ios-feasibility.md` (Q2–Q4, feasibility table), `platform-access.md` (Q1 limited library, Q4 Picker), `memory-product-sdk.md` (Q6), `unknowns-r1.md` (Q3, Q5), `verticals.md` §2.2 (insurance claims). The remaining research files and `assumptions/A1–A6` were keyword-searched for insurance, inventory, adjuster and evidence-packet material only; nothing in them bears on this variant beyond what `SCORECARD.md` already summarises. `variants/current.md` was read for the base it claims to keep.

## Verdict in one line

Pass. The author already says so ("a module or a feature, not a company"), and the repaired research makes the number smaller than the author wrote, not larger.

## Where the variant and the repaired research disagree (research wins)

| # | Variant says | Repaired research says | Effect |
|---|---|---|---|
| 1 | Pool of 40,000–80,000 households a year, central 60,000; "hard upper bound" 130,000–150,000 | Both withdrawn (audit S4, U6). Fire segment 25,000–50,000 in an average year, about 60,000 in a peak wildfire year; water/wind and flood are unsized assumption ranges; arithmetic ceiling 400,000–600,000 from a 2016 input (2.2) | Every line of the variant's Ceiling uses a withdrawn input. Failed claim |
| 2 | "$100M needs 2.4–2.8× the hard upper bound" | No hard upper bound exists. 358,000 paying households is 7–14× the fire segment (358,000 ÷ 50,000 and ÷ 25,000) | Conclusion survives, the stated arithmetic does not |
| 3 | Line C prices carriers at ContentsTrack's $36–45 a job; "carrier-side job prices are lower" | ContentsTrack is contractor pack-out software; what carriers pay per contents claim is [unknown] (2.3, 2.7, audit S6) | Line C has no supported input. Failed claim |
| 4 | XactContents $950–1,900 a seat-year | Withdrawn; price [unknown] (2.3) | Failed claim |
| 5 | Contents specialists $800–8,000 flat | Withdrawn; the one sourced example charges 10% of recovery (2018, one practitioner) (2.3) | Failed claim |
| 6 | NAPIA about 600–750 members | Withdrawn; [unknown] (2.3). The variant's "own search" excerpt of an undated article does not restore it | Failed claim |
| 7 | "38% in one survey admitted overstating a home claim" | Withdrawn; the sourced figure is 17%, 14 countries, home and auto, 2014 (2.6, audit S7) | Failed claim |
| 8 | Largest comparable revenue: Enservio $41–56M, Encircle about $9.9M | Withdrawn everywhere; Enservio and Encircle revenue [unknown] (section 4, audit S5) | No sourced comparable revenue exists at any size |
| 9 | Sensitivity (b): 60,000 × $300 = $18M | Withdrawn (audit U1, S3); no stand-alone post-loss inventory price has been observed being paid | Failed claim |
| 10 | Florida's wording reaches paid preparation; "Florida done-for-you service" excluded from v1 | Florida expressly excludes "a person who photographs or inventories damaged personal property" who does not solicit or negotiate (2.6, audit S1). Open point: "damaged" versus destroyed | The variant is over-cautious here; one objection is weaker than written |
| 11 | SB 495 as a dated change that shrinks the job (Why now 2); "Colorado 65% (2022)" | At the default coverage ratio the California percentage did not move; the cap rose by $100,000 and binds only above about $833,000 of dwelling limit. Colorado enactment year dropped as unverified (2.1, audit S2, U12) | The statutory why-now is weaker in both directions |
| 12 | "73% did not receive 100%"; itemizing share "half to three-quarters" | Corrected to "roughly half": 53% (report) to 56.37% (export) told to list every item (audit S8) | The high case of Line A uses a withdrawn share |
| 13 | "United Policyholders recommended Bevel at a workshop" | A local news story reposted on uphelp.org reports suggestions made at a survivors' meeting; "this is not a United Policyholders endorsement" (2.4, audit S14) | The channel is less locked up than written, and less proven |
| 14 | Research "says so in terms: 'These are features Bevel could add in weeks; they are not a company'" | That sentence is now marked as the researcher's judgment, not evidence (2.8(c), audit U14) | Still my view; not a sourced fact |
| 15 | No mention of Loti | Loti, a public-adjuster firm, gives away an AI inventory "from your photos" and sells a $100/month self-service claim suite (2.4) | A second free tool, and proof that a professional buyer builds its own. The variant's pro channel is weaker than written |

Numbers the variant fetched itself and no research file carries (ProofList $59–499, Contents.team $299/month, "46 states", NICB 1,400%, Verisk 36%, NAIC Model 228 text) raise no score here, as the variant itself asks.

Arithmetic I re-ran and found correct on the variant's own inputs: per-photo cost $0.0033–0.0066 (prices in unit-economics.md Q3); COGS table sums $21.5 / $53.4 / $110.8; margins 89% / 73% / 44%; free-tier margin 28%; pro-seat margin 85%; Lines A and B; totals $0.48M / $1.54M / $4.77M.

## Ceiling, recomputed from the research-supported end

| Line | Inputs (all from contents-claims.md unless noted) | Result |
|---|---|---|
| A. Households at the variant's $199 | Fire segment 25,000–50,000 [estimated, assumption-driven: 2.2] × told to itemize 53–56% [sourced: 2.1] × usable photos 50% [unknown; the variant's own assumption] × 7.8% who hired a contents specialist [sourced: 2.3] × $199 [variant's price; not observed paid] | 25,000 × 0.53 × 0.5 × 0.078 × 199 = $0.10M to 50,000 × 0.5637 × 0.5 × 0.078 × 199 = $0.22M |
| A′. Research's own top-down | 25,000–50,000 × 7.8% × $600 (Loti's $100/month list price × an assumed 6 months) | $1.2M–$2.3M (section 4 scenario row); $4.7M with an illustrative 100,000 all-peril households |
| B. Professionals | 25,000–50,000 × 39.8% served by an adjuster, attorney or specialist (overlap ignored) × 10–30% reach [assumption] × $150–300 per file [assumption] | $0.15M–$1.8M; mid-point 37,500 × 0.398 × 0.20 × 200 = $0.60M |
| C. Carriers | Per-claim price [unknown] | $0 |
| D. Pre-loss | Graveyard in 2.8 | $0 |

**Evidenced cap: about $0.3M–$2M at the variant's prices, $1.2M–$4.7M on the research's most generous observed inputs.** Every row assumes national reach of every qualifying household against two free tools. This is below the $5–45M band that earned 2–3 in earlier rounds and below the standing leader's $3–12M. The only route to eight figures in the research is contingency pricing as a licensed public adjuster ($20–39M at observed adoption, section 4), which is a per-state licensed services firm with 10% caps in Texas, Florida emergencies and Utah catastrophes, and which the variant excludes.

## Scores

| # | Dimension | Score | Evidence pointer | One-line reason |
|---|---|---|---|---|
| 1 | Pain | 6 | contents-claims.md 2.1 (53–56% told to list every item; "half of policyholders struggle with itemization lists"; 40% of the contents limit at stake in California), 2.3 (15.9% / 16.1% / 7.8% hired help at 10–33% contingency), 2.5 (no post found paying a stand-alone fee) | Acute and paid for in hours and contingency fees; not frequent (about 0.04–0.08% of policies a year), and nobody was found paying for the inventory itself |
| 2 | Wedge | 5 | contents-claims.md 2.5 (United Policyholders already tells survivors relatives may hold photos), 2.4 (Bevel and Loti accept uploaded old photos today); platform-access.md Q1 (limited library), Q4 (Picker strips GPS); funnel row "usable pre-loss interior photos" [unknown] | The household must do the job anyway, but the differentiator needs relatives with no claim to install an app and grant full-library access, and Android relatives fall back to an upload form |
| 3 | Why now | 4 | unit-economics.md Q3 (vision prices); contents-claims.md 2.1 (SB 495 changed the cap, not the percentage), 2.4 (Bevel, 2025-01) | The cost change is real and dated; the demand-side changes arm a free incumbent, the statutory change is misdescribed, and the fraud why-now rests on unread search excerpts |
| 4 | Platform risk | 2 | contents-claims.md 2.4 (Bevel free, $6M seed, ">25%" of survivors as a company claim; Loti free; three hackathon prototypes), 2.3 (XactContents multi-object recognition), 2.8 (legislative trend; voluntary 75–100% advances); memory-product-sdk.md Q6 (guideline 5.1.1(iii)); verticals.md §2.2 (Verisk XactAI labels photos at $29/user/month) | The category leader ships most of this free, a professional buyer has built its own, Apple Photos already searches by place and date, and the variant's own answer to "survives?" is "as a company, no" |
| 5 | Compounding asset | 2 | variants/v4-claims.md Compounding asset and Regressions (1); contents-claims.md 2.3 (Enservio's 2016 price database), 2.4 (Bevel "3M+ items") | The corpus is collected for one claim and deleted; no repeat purchase; the price table starts behind two incumbents |
| 6 | Distribution | 2 | contents-claims.md 2.4 (survivor channel occupied by a free tool), 2.7 (public-adjuster count and software spend [unknown]; Loti built its own), 2.8 (demand spikes with catastrophes); sizing.md Q5 (keyword cost [unknown], every route failed), Q4 (derived CAC $65–90, directional) | No channel is evidenced for a paid entrant: the non-paid one works for a free competitor, the paid one bids against adjusters whose fee per claim is thousands, and there is no second purchase to recover a miss |
| 7 | Economics | 5 | unit-economics.md Q1, Q3, Q7 (R2, vision and card prices; arithmetic verified); contents-claims.md section 4 revenue scenarios (observed prices are $0, $100/month, 10% contingency) | COGS is cleanly tagged and 73% central margin checks out, but the $199 price has never been observed being paid, support and price-lookup lines are assumptions, the free tier drags margin to 28%, and revenue at the cap does not cover a three-person team |
| 8 | Buildability | 7 | ios-feasibility.md Q4 and feasibility table (local 1536×2048 copies, free Vision classification); unknowns-r1.md Q5 (SigLIP 2, Apache-2.0); contents-claims.md 2.4 (weekend prototypes exist) | A two-engineer, four-week demo with no partnership and a measurable acceptance test; instance merge over time is hard but human-confirmed. The ease is also the absence of a moat |
| 9 | Ceiling | 1 | contents-claims.md 2.2 (pool withdrawn and re-derived), section 4 revenue scenarios ($1.2–2.3M at observed price and adoption), audit log S3–S6; recomputation above | Built on withdrawn inputs (which alone caps it at 2) and it recomputes to $0.3–5M, below every earlier variant; no contents-inventory vendor has a sourced revenue figure at any size |
| 10 | Founder fit | 5 [unknown] | — | Not stated by the founder; neutral placeholder |

**Total: 39 / 100.**

## Most damaging objection

The product charges $199 to people who have just lost a home for an increment over something a funded team already gives them free. Bevel extracts items from old family photos, prices them and exports the spreadsheet at no charge, and a funding digest relays its claim that more than a quarter of Los Angeles survivors used it; Loti, a public-adjuster firm, gives away the same step and keeps its paid tier for the claim suite. What v4-claims adds is an automatic location search across relatives' iPhones and a capture date on each line. The research could not find one person who paid a stand-alone fee for inventory help after a loss, and at the only adoption rate and the only software list price it did observe (7.8% and $100 a month), the whole national fire segment is $1.2–2.3M a year before it is split with two free tools. On the repaired pool the variant's own household line is about $0.1–0.2M. The team it specifies costs $0.6M a year.

## Weakest dimension

**Ceiling (1).** The pool, the carrier price and the comparable revenues the variant used were all withdrawn in the research repair, and the recomputed cap is $0.3–5M.

## Strongest dimension

**Buildability (7).** The core loop needs no platform partnership, no licence and no research breakthrough: a metadata filter on location and date, Apple's free on-device classifier, a commodity vision call at well under a cent a photo, and a human confirming every merge. The four-week plan ends in a real measurement (inventory from camera rolls against a walk-through of five intact homes) that would settle the variant's central unknown. Pain (6) is the runner-up and is the best-evidenced pain of any variant so far.

## Unknowns research could resolve before the next round

1. What share of a household's contents replacement value is visible in candid pre-loss photos pooled from the household and relatives? Search for any published recall or uplift figure from Bevel, Loti, Adjusto or an academic home-inventory-from-photos study.
2. What do carriers pay per contents claim or per seat to Enservio, XactContents, Hosta or Adjusto? Search public-entity vendor contracts (Citizens Property Insurance in Florida, California FAIR Plan, state procurement portals) and rate-filing expense exhibits.
3. How many licensed public adjusters are there nationally, and what do they pay per claim file for software? Search NIPR and state open-data licence rosters (Florida, California, New York) and list prices of adjuster claim-management tools.
4. Has Bevel or Loti shipped relative invites, an iCloud or Google Photos connection, or per-line capture dates, and does either disclose users or paid conversion? Search App Store release notes, product changelogs and Loti Suite subscriber statements.
5. What share of fire claims pay $25,000 or more under Coverage C, and what is the average contents payment? Search California Department of Insurance wildfire data calls and NAIC or ISO fast-track tables that split Coverage C from Coverage A.

## Three questions for the founder

1. If Bevel ships "invite relatives" and a capture date per line next month, what is left that a household pays $199 for?
2. Name the first twenty professionals who would pay per claim file. Why would each of them not do what Loti did and build it, or send clients to Bevel for nothing?
3. The only eight-figure path in your own research is a licensed contents-adjusting firm on contingency. Are you willing to run that business, state by state? If not, why is this a company and not the claim-evidence module in the organizer workbench that you describe at the end?
