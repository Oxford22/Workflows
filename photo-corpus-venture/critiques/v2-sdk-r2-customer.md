# v2-sdk — Round 2 critique — TARGET CUSTOMER

Written 2026-11-24. Research read was gathered 2026-11-03 (21 days old; dated per finding). Fresh context: read SCORECARD.md, variants/v2-sdk.md, variants/current.md (skim, for the "kept" claims), research/memory-product-sdk.md in full, and in the other 18 research files plus research/assumptions/A1–A6 the summaries, verdicts and every section the variant cites (ios-feasibility Q2–Q5, Q7; unknowns-r1 Q5, Q8; face-regulation Q1, Q6, Q7; unit-economics Q3, Q7; sizing Q4 and worked chains; grandparent-loop Q1–Q2; customers Q1(h), Q3; pro-channel Q1; digitization-market Q1; estate Q6, Q8; genealogy-market Q1, Q3; platform-access Q1, Q4, Q8; competitive Q1, Q3, Q5; byo-ai Q5; ai-why-now §6). Not read line by line: trades-and-reddit.md and verticals.md beyond headers (no section bears on this variant). CHANGELOG, other v2 variants and other critiques were not opened.

## Stance

I am the VP of Product at a photo-book company with $100–300M revenue. Our Google Photos import stopped working as a library connection in March 2025, our mobile funnel loses most users at photo selection, and my 40 engineers have shipped one AI feature in two years. I am the best-case buyer this variant has: I cannot build fast, and I have the pain it names. I score on: would I take the first step, what I give up, whom I trust, what happens if the vendor dies, cost versus today, and whether I would recommend it to a peer. Pain, Wedge and Distribution are scored hardest.

One thing to say up front: the research has no data on any buyer in my revenue tier. The buyer table jumps from Mixbook/Chatbooks (roughly $4–20M, aggregator estimates) to Shutterfly/CEWE/Vista (roughly $0.9–1.8B); "Walgreens/CVS/Walmart photo, Minted, Printique, Photobox/Albelli — volumes/revenue [unknown]" (memory-product-sdk.md Q1, last row). The variant's "defensible slice" is described from the outside.

## Scores

| # | Dimension | Score | Evidence pointer | One-line reason |
|---|---|---|---|---|
| 1 | Pain | 4 | memory-product-sdk.md Q2 ("weak evidence of pain and no evidence of willingness to pay"), Q3 (only Mixbook's PR quantifies selection), Q5 (no buyer has a third-party curation vendor) | The pain is paid for in in-house engineering hours, not vendor money, and the half of my pain that is Google import is explicitly out of scope (A1.md holds, 0.75; variant "NOT in v1"). |
| 2 | Wedge | 3 | memory-product-sdk.md Q6 (host owns the full-access grant, 5.1.1(iii), 5.1.2(i), privacy manifest); ios-feasibility.md Q3 (76 ms/image central; 38–57 min for 30k) and Q4 (share of assets with no local copy [unknown]) | No habit change for my end user, but my first step is a new full-library prompt, a multi-minute foreground index and a consent screen at the step where I already lose users, for a lift tagged [unknown]. |
| 3 | Why now | 5 | memory-product-sdk.md Q3 (Vision aesthetics request, iOS 18.0+; Mixbook Story Mode 2026-06-11); ai-why-now.md §6 | Real dated changes, and each one is a reason for me to build on free primitives at least as much as a reason to buy. |
| 4 | Platform risk | 3 | memory-product-sdk.md Q4 ("the market price of 'let a user pick photos from a cloud' is zero"), Q6 (WWDC20 10641: "For most apps the answer is no"), Q5 (hosts build) | Apple steers hosts away from the grant the SDK needs; one "suggested" sort in the system picker and I remove the SDK with relief. |
| 5 | Compounding asset | 3 | byo-ai.md Q5 (commodity layer); memory-product-sdk.md Q4 (culling sold flat because marginal cost is ~zero); unknowns-r1.md Q5 (open models) | The index is discarded after each order; the only cross-host asset needs my customers' keep/swap telemetry to train a model my competitors use, which I would refuse. |
| 6 | Distribution | 2 | memory-product-sdk.md Q5 (no partnership or RFP found; Mixbook, CEWE, Shutterfly, Chatbooks, Google/Fujifilm all built); pro-channel.md Q1 (TPM sponsor lists 2023–2026) | No channel with evidence; the TPM route to "Shutterfly/Mixbook product managers" is not supported by the research; no reference host exists. |
| 7 | Economics | 5 | unit-economics.md Q3 (compute rows), Q7; memory-product-sdk.md Q4, Q7 (flat-rate comparables; 11.6% EBIT margin) | Modeled and tagged, but every price is an assumption, the payback for the reachable hosts is misstated, and my annual fee is close to my one-off build cost. |
| 8 | Buildability | 6 | ios-feasibility.md Q3 (AdaFace Core ML iPhone latency [unknown]), Q7 (Android portable but separate build); unknowns-r1.md Q5 (SigLIP2 iPhone latency [unknown]) | A 4-week iOS demo is credible on documented APIs; what I would buy (iOS + Android + web parity, App Review cleared) is not in the 4 weeks. |
| 9 | Ceiling | 2 | memory-product-sdk.md Q7 ("single-digit millions ARR unless the SDK captures something the vendor cannot build") | The variant's own evidenced corner is ~$1.3M; its "$5–15M" needs a line it calls the stretch. |
| 10 | Founder fit | 5 [unknown] | — | Not stated by founder; neutral placeholder. |

**Total: 38 / 100** (4+3+5+3+3+2+5+6+2+5; founder fit is a flagged neutral 5).

## Number check against the research

Confirmed as stated (spot-checked): CEWE 2025 figures and 11.6% Photofinishing EBIT margin; Cimpress/Vista $1,824.3M and T&D $334.0M; Shutterfly Q1 2026 $313.5M, −8%, $2.4B debt, 12.5% notes; Everypixel $0.60, Rekognition $1.00/$0.80, Photoroom $0.02, Narrative $10–60, Imagen; Chatbooks Picker friction quotes; App Groups same-team rule; Photomyne library deal (~5,000 seats, ILS 318k, ~$7/seat-year, B2B $271k H1 2026); Tukios upload link; Shutterfly BIPA $6.75M; 12.7% IL+TX; FamilyAlbum 12M MAU and ¥17,159M; Tinybeans $767k (+646%) and 0.86M MAU (FY25); Ancestry and MyHeritage subscriber floors; immich-go 7.1k stars (A3.md), Immich 118k, 54,763 registry servers; ThisLife $25M; MobileCLIP relicence 2025-02-24; 2,400 × 76 ms ≈ 3 min; all Ceiling multiplications.

Failed or unsupported:

1. **"Honest number: $5–15M ARR."** The variant's central lines sum to about $3.3M ($1.8M orders + $1.2M licences + $0.26M server-side). The range is reached only by adding the $7.2M per-MAU line, which the variant labels "the stretch" and which assumes 15M adopting MAU when the named pool (FamilyAlbum 12M, Tinybeans 0.86M, Ancestry 3M+ subscribers) totals about 16–17M and all three ship their own photo AI (grandparent-loop.md Q1–Q2; genealogy-market.md Q3). Research says "single-digit millions" (memory-product-sdk.md Q7). Supported number: roughly $1–3M.
2. **Payback "15 months" for a licence-only host.** Computed at 85% contribution, but the Economics section gives that same host 55% ($33k). At 55% it is 60 ÷ (33 ÷ 12) ≈ 22 months; with the $10–20k per-host counsel cost the variant lists separately, year-one contribution is $13–23k and payback is 31–55 months. These are the hosts the variant calls its defensible slice.
3. **"~$4–5B of Western photo-merchandise revenue"** (value-based upside). Research bounds it at ≥ ~$2.1B and ≤ ~$3.9B, the upper bound only "if all of Vista's $1.82B were photo products (it is not)", plus low hundreds of millions for the small vendors (memory-product-sdk.md Q7). The $40–50M upside is overstated by roughly 1.3–2×.
4. **"≈30M sourced orders/yr" floor.** 23.6M of it is Shutterfly Consumer in 2018, from the variant's own fetch (not in the research), predating the Snapfish merger and eight years old; the variant itself says orders were declining 3–10%/yr, and Q1 2026 revenue is −8%. It is a 2018 figure, not a 2026 floor.
5. **Compute "~$0.04 per 1,000 images"** is derived in the same sentence as "$0.04 + $0.03 per 22,000 → $3.2/M", which is $0.0032 per 1,000. A 12× unit slip; conservative, immaterial to the conclusion, but it is wrong.
6. **"~100-person company" / "100-person Mixbook."** The research audit withdrew that phrasing: headcount is 55 / 112 / 141 by conflicting aggregators, true size [unknown] (memory-product-sdk.md Q5, audit log).
7. **TPM as a route to "Shutterfly/Mixbook product managers who already sponsor or attend adjacent trade events."** Neither company appears on any TPM sponsor list 2023–2026; Fujifilm appears in 2024, Epson/WHCC/Printique in 2025, none of them in 2026 (pro-channel.md Q1).
8. **"3 min central" index time** rests on per-image figures for MobileCLIP-S2 and an unnamed secondary "20–40 ms" source; the variant ships SigLIP2-base and AdaFace, whose iPhone latencies are both [unknown] (unknowns-r1.md Q5; ios-feasibility.md Q3). And it holds only for the date window: a "photos of this person" window needs faces across the whole library, which is the 38–57 minute session (ios-feasibility.md Q3) the variant says sank v1-federation.
9. **CEWE quote elided.** "Images are not transferred ... to third parties" drops "for marketing purposes"; "CEWE's charter forbids third parties touching images" over-reads it (memory-product-sdk.md Q5). The slip runs against the variant, so it does not inflate anything.
10. **Biometric posture.** The variant summarises Doe v. Apple as rejecting encryption "once templates sync". The research records that the Local Device Class also survives and that whether Apple controls on-device faceprints is a jury question (unknowns-r1.md Q8). On-device-never-synced is not yet a safe harbour for the host, and under the variant's contract the host is the "private entity".

Not checkable against research (variant's own 2026-11-03 fetches): Shutterfly FY2018 10-K metrics, Cloudinary Plus pricing, WWDC20 10652 and WWDC23 10107 transcripts.

## Most damaging objection

To get the day-1 value, I have to take Apple's free, out-of-process, no-prompt picker out of my order flow and put in its place a full-library permission prompt, then a foreground index of about 3 to 4.5 minutes on an iPhone 15-class phone (the variant's own central and derated figures, built on two model latencies the research marks [unknown]), then a separate biometric consent screen if I want the people features. All three land on the exact screen where I already lose most of my mobile users.

In return I get a lift the variant tags [unknown], on iOS only, with an App Review outcome tagged [unknown], with my company named as the BIPA "private entity" in an industry where Shutterfly paid $6.75M for face grouping, and with no effect on my Google Photos import, which is listed under "explicitly NOT in v1".

If I refuse the new grant, the fallback "picker mode" drops people-balance and window indexing. What remains is pHash dedupe plus Apple's free Vision aesthetics score, which the variant says my engineers can build in four weeks and which a company of 55–141 people already shipped in June. The research's own bottom line is that this variant "should be killed or re-shaped as a first-party app that exports to these companies, not a library they embed" (memory-product-sdk.md, bottom line and Q6).

What I would actually do: take the demo meeting, ask for a no-fee pilot in picker mode after peak season, and pay nothing until a lift is measured. That is at least six months of no revenue for the vendor, and the mode I would pilot is the one with the least differentiation.

## Weakest dimension

**Distribution (2), tied with Ceiling (2).** I name Distribution because the evidence runs against it rather than merely being absent: every named buyer that cared built in-house in 2025–2026, no buyer has announced a curation vendor or an RFP, the one non-paid route argued in detail does not reach the people it claims to reach, and there is no reference host. As a buyer I would ask "who else in my industry runs this in production?" and the answer today is the vendor's own organizer workbench. Ceiling is equally low, but the variant states that honestly.

## Unknowns research could resolve before the next round

1. What share of iOS users choose "Allow Full Access" rather than "Limit Access" or "Don't Allow" when a photo-print or photo-book app requests Photos permission on iOS 17–27? Any published opt-in rate from an app developer, analytics vendor or study.
2. Do the current iOS apps of Shutterfly, Snapfish, Chatbooks, FreePrints, Mixbook and Artifact Uprising request full-library access or use only PHPickerViewController? (App Store privacy labels, purpose strings, observed prompt behaviour.) This decides whether the SDK needs a new grant at each host.
3. Has any photo-merchandise company published mobile-app share of orders or selection-step abandonment? (Shutterfly 10-Ks before 2019, CEWE capital-markets-day decks, Cimpress investor days, Photobox/Albelli, PlanetArt/FreePrints.)
4. Which white-label photo-commerce platforms power retailer and mid-size photo apps (for example ip.labs, Taopix, Printbox, Photo Finale, Pixfizz), what do they charge, who are their customers, and do they already bundle auto-curation? The research did not look at this layer; it is either the real channel (five platform vendors instead of twenty hosts) or the incumbent that already covers my tier.
5. Does PHPickerViewController on iOS 26/27 expose People-name search, suggested or curated selections, or any ranking filter (PHPickerFilter / PHPickerConfiguration reference and PhotosUI release notes; the variant's fetches returned 404)?

## Three questions for the founder

1. You call an acquisition on the ThisLife pattern "the good outcome". If you are bought by one of my competitors, or you run out of money, what do I hold on that day: source escrow, a perpetual licence, and a picker that keeps working in my checkout without your licence server?
2. Will you run a no-fee pilot in picker mode in my app and be paid only on measured lift in completed orders, and will you walk away if the lift is under the 3% you name as your own falsifier?
3. My customers' keep/swap telemetry trains a model my competitors also get. If I opt out, do I still get the product at the same price, and if every host opts out, what is left that my two engineers and Apple's Vision request cannot reproduce in a quarter?
