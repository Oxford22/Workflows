# v2-sdk — Round 2 critique — COLD SEED INVESTOR

Critic date 2026-11-24. Research read was gathered 2026-11-03 and is dated per finding.
Variant scored: `variants/v2-sdk.md`. Rubric: `SCORECARD.md`.

Coverage note: `research/memory-product-sdk.md` and `research/sizing.md` were read end to end (they carry every Ceiling input). The other 22 research files were not read end to end; each number the variant cites from them was looked up at the cited section and checked. Anything below marked "verified" was found in the file named; anything not listed was not checked.

## Stance

Default is no. This is a component vendor selling to 15-25 named companies, the largest of which have shipped the same feature in-house on free Apple calls inside the last 18 months. The variant says so itself and prices its own ceiling at $5-15M. A seed fund does not underwrite that, and the research file the variant is built on ends with "The round-2 SDK variant should be killed or re-shaped as a first-party app that exports to these companies, not a library they embed" (memory-product-sdk.md, bottom line). The variant is unusually honest; honesty is not a market.

## Scores

| # | Dimension | Score | Evidence pointer | One-line reason |
|---|---|---|---|---|
| 1 | Pain | 3 | memory-product-sdk.md Q2 ("weak evidence of pain and no evidence of willingness to pay"), Q3 (only Mixbook's own PR quantifies the selection step) | Buyers spend engineering on curation, but none pays a vendor for it and no host has published selection-step drop-off. |
| 2 | Wedge | 4 | memory-product-sdk.md Q6 (per-host SDK permitted; host owns the full-library grant, 5.1.1(iii), 5.1.2(i) disclosure); ios-feasibility.md Q3 Scenario A inputs | No end-user habit change, but the buyer must move from Apple's free picker to a full-library grant, embed third-party code in its order flow and pay counsel; that is the habit change, and it sits with the party that pays. |
| 3 | Why now | 4 | memory-product-sdk.md Q3 (Vision aesthetics iOS 18+), Q5 (Mixbook 2026-06, CEWE MAIC 2025, Google to Fujifilm 2026-09); face-regulation.md Q1 (G.T. v. Samsung 2026-08) | Every dated change is real and every one is equally available to the host; the dates explain why hosts built, not why they would buy. |
| 4 | Platform risk | 2 | memory-product-sdk.md Q4 ("the market price of 'let a user pick photos from a cloud' is zero"), Q5, Q6; assumptions/A4.md Against #4-#5 | Dies on one WWDC slide (suggested ordering in PHPicker) and is already mostly dead to incumbent builds; Apple's written guidance steers hosts away from the grant the SDK needs. |
| 5 | Compounding asset | 3 | byo-ai.md Q5 (commodity layer); unit-economics.md Q3 (index rebuildable for cents); memory-product-sdk.md Q5 (CEWE third-party stance) | Window index is worthless after the order; the cross-host ranking model needs hosts to send keep/swap telemetry to a vendor that serves their competitors, and its value is [unknown] until two hosts are live. |
| 6 | Distribution | 2 | memory-product-sdk.md Q5 (no curation-vendor partnership or RFP found for any named buyer), bottom line; pro-channel.md Q1 sponsor lists | Enterprise sales into a short list with zero evidenced buyers; the open-core route has "none [unknown]" conversion evidence by the variant's own tag; the organizer channel does not reach these buyers. |
| 7 | Economics | 5 | unit-economics.md Q3, Q7 (index-only GM); memory-product-sdk.md Q4 (comparables are flat $10-79/mo seats; pickers are free) | No storage line and a tagged model, but licence, per-order fee, pass-through, integration cost and close rate are all assumption-tagged with no comparable, and one payback figure is wrong (below). |
| 8 | Buildability | 7 | ios-feasibility.md Q3 (per-image inputs); unknowns-r1.md Q5 (SigLIP2 Apache, AdaFace MIT); memory-product-sdk.md Q3 (Vision request) | Four-week demo is credible on documented APIs; that is also why Mixbook built it. AdaFace on-device latency and Android remain unmeasured. |
| 9 | Ceiling | 2 | memory-product-sdk.md Q7 ("The ceiling is single-digit millions ARR unless the SDK captures something the vendor cannot build"); sizing.md Q4 row 33 (consumer route closed) | Variant concedes $100M does not pencil; its $5-15M headline is above its own evidenced arithmetic and rests on a contradicted revenue pool and a stale order count. |
| 10 | Founder fit | 5 [unknown] | none (founder questionnaire unanswered) | Neutral placeholder. |

**Total: 37 / 100** (founder fit is a flagged neutral 5).

## Numbers checked against the research

Failed or unsupported:

1. **"~$4-5B of Western photo-merchandise revenue"** (value-based upside, $40-50M). memory-product-sdk.md Q7 bounds observable revenue at "at least ~$2.1B" and "at most ~$3.9B if all of Vista's $1.82B were photo products (it is not)". The variant's pool is above the research's upper bound. On $2.1-3.0B the same 5% lift x 20% share gives $21-30M, and still needs every host to adopt and pay on measured lift. Failed claim.
2. **"~30M sourced orders/yr" floor.** memory-product-sdk.md Q7 says of the same figure: "30M is an assumption, not a sourced number". The variant relabels it "sourced" by adding Shutterfly's FY2018 order count (23,626k, a fact not present in any research file, eight years old, covering all products) to CEWE's 2025 photobook count (6.32M, books only). The variant itself says Shutterfly orders were "declining 3-10%/yr"; compounding that for eight years gives 10-18.5M, and Q1 2026 revenue was -8% YoY (memory-product-sdk.md Q1). It is neither a floor nor current. Stale input, mixed units.
3. **"Honest number: $5-15M ARR."** The variant's own plausible lines sum to $1.8M usage + $1.2M licences + $0.26M server = about $3.3M; its "evidenced corner" is about $1.3M. Getting to $5M needs the $7.2M per-MAU line, which the variant calls "the stretch" and "unlikely", on hosts it says "all ... ship their own photo AI". memory-product-sdk.md Q7 says "no per-MAU ceiling can be derived honestly". The headline is not supported by the variant's own arithmetic; the supported range is roughly $1-4M.
4. **"Licences: 20 hosts x $60k."** The same document counts 15-25 plausible hosts worldwide and assumes 20-40% of the pool adopts. 20-40% of 15-25 is 3-10 hosts, or $0.18-0.6M. At the stated close rate of 3 hosts per AE-year, 20 hosts is about seven years with no churn.
5. **"Payback 15 months" on a licence-only host.** The formula uses 85% contribution; the Economics section gives 55% ($33k) for that same host. At 55% payback is about 22 months; net of the $10-20k per-host counsel cost the variant lists separately, 31-55 months in year-one terms.
6. **The $285k worked example** assumes a host with 5M orders/yr. Only Shutterfly (2018) and CEWE clear that in the evidence, and the variant says neither will adopt. For the "defensible slice" the research supports far less: Chatbooks at $3.9-20M revenue and $15-24/book is 0.16-1.3M books/yr; Mixbook's "20 million+ projects printed" over "20 years" averages about 1M/yr and Mixbook has already built; Tinybeans e-commerce is $767k/yr (memory-product-sdk.md Q1, Q7; grandparent-loop.md Q2). The three-month payback applies to a customer that is not in the reachable set.
7. **"Shutterfly/Mixbook product managers who already sponsor or attend adjacent trade events."** pro-channel.md Q1 sponsor lists show Fujifilm (2024), Epson, Miller's, WHCC, Printique; neither Shutterfly nor Mixbook appears. Unsupported.
8. **CEWE quote.** The research quote is "Images are not transferred to public albums, servers outside the scope of the GDPR or to third parties for marketing purposes". The variant shortens it to "Images are not transferred ... to third parties" and calls it a charter that "forbids third parties touching images". The qualifier was dropped; the bar is overstated (in the pessimistic direction, but it is still a misquote).
9. **Vista $1.8B in the one-line pitch.** memory-product-sdk.md Q1: consumer photo share of Vista is "not disclosed [unknown]". It should not sit in a sentence about companies that "earn billions from the order the selection feeds".

Verified as stated: CEWE 2025 figures and 11.6% Photofinishing EBIT margin; Shutterfly Q1 2026 revenue, debt and 12.5% notes; Mixbook Story Mode claims; Chatbooks Picker friction; Photomyne library deal (digitization-market.md Q1: ILS 318k, ~5,000 subscriptions, three years; B2B $271k H1 2026); FamilyAlbum 12M MAU (customers.md Q1(h)); Tinybeans e-commerce $767k FY26 (grandparent-loop.md Q2); Shutterfly BIPA $6.75M (face-regulation.md Q1); App Groups same-team rule; 12-month window timing (76 ms x 2,400 = about 3 min; the research flags the 30 ms fetch term as "the single largest uncertainty", unmeasured); consumer CAC $65-90 against $42.4 LTV (sizing.md rows 32-33); Live Member Focus Group $1,500 (pro-channel.md Q1). ThisLife $25M rests on a Wikipedia secondary in competitive.md Q5, not a primary.

## Most damaging objection

**The customer set is the intersection of "has enough orders to matter" and "has not already built it", and the research shows that intersection is empty.** The hosts with volume (Shutterfly, CEWE, Mixbook, Google/Fujifilm) all shipped in-house curation between 2025 and 2026-10 on Apple's free Vision call or their own AI team (memory-product-sdk.md Q5). The hosts the variant retreats to (Chatbooks, Tinybeans, tribute and memoir companies) have evidenced volume of at most roughly 1-3M orders a year combined, which at $0.15 is under $0.5M of usage revenue; and Chatbooks already ships "Smart Select". No named buyer has ever announced a third-party curation vendor, and the one partnership in the category has the platform supplying curation, not buying it (Google to Fujifilm, 2026-09-30). The variant's first load-bearing assumption is the entire business and has no supporting observation.

## Weakest dimension

**Ceiling (2)**, tied with Distribution and Platform risk at 2. Ceiling is the one that cannot be fixed by execution: the variant's own math needs 667M orders a year at $0.15 for $100M, which is 7-11 times its own assumed Western pool, and its supported range is $1-4M. This does not answer the round-1 instruction to start from a pool where money flows at scale and show the arithmetic; it starts from such a pool and shows the take rate on it is negligible.

## Unknowns research could resolve before the next round

1. Has any photo-book, print, tribute or memoir company publicly licensed a third-party photo-selection or curation SDK or API since 2023 (press releases, vendor case studies, job posts naming a vendor), and at what price?
2. What are the annual order or book counts for the second-tier hosts: Chatbooks, FreePrints/PlanetArt, Artifact Uprising, Photobox/Albelli (Storio group annual report), and Walgreens/CVS/Walmart Photo?
3. What share of orders at Shutterfly, CEWE, FreePrints or Chatbooks originates in the mobile app rather than web or desktop (CEWE capital-markets material, Shutterfly bond offering documents, PlanetArt disclosures)?
4. Does `PHPickerViewController` search on iOS 26/27 match People names, and did iOS 27 PhotosUI or any WWDC26 session add suggested, "best of" or aesthetics-sorted ordering inside the picker?
5. Is there any published selection-step abandonment or conversion figure for photo-book creation (Baymard, HCI literature, Cimpress or CEWE investor-day decks) other than Mixbook's 2026-06-11 press release?

## Three questions for the founder

1. Name the one second-tier host whose product lead you can reach this month. Why would they sign a $60k licence plus counsel fees for something a 55-141-person Mixbook built on a free Apple call?
2. If WWDC 2027 adds suggested ordering to the system picker, what exactly do you invoice for in July 2027?
3. Your own arithmetic tops out below $15M and mine puts the supported range at $1-4M. Is this a venture raise, or a bootstrapped component aimed at a ThisLife-style acquisition, and if the latter, why is it in front of a seed fund?
