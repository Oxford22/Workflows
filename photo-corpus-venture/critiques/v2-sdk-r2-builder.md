# Critique — v2-sdk, round 2, BUILDER lens

Written 2026-11-24 from a fresh context. Research read is dated 2026-11-03. Read: SCORECARD.md, variants/v2-sdk.md, variants/current.md (for what is kept), research/memory-product-sdk.md in full, and the sections of research/ios-feasibility.md, face-regulation.md, unknowns-r1.md, unit-economics.md, platform-access.md, pro-channel.md, ai-why-now.md, competitive.md, digitization-market.md, estate.md, grandparent-loop.md, sizing.md, customers.md and assumptions/A2, A4, A5 that the variant cites. The remaining research files were checked by heading and by search for the variant's claims, not read line by line. Not read: CHANGELOG, other v2 variants, any critique.

## Stance

Builder. I believe only shipped demos. I score the smallest thing that proves the core loop, the ugliest technical risk, and what breaks under load (cost, support, data-loss liability, legal exposure). Buildability and Economics are scored hardest.

## Scores

| # | Dimension | Score | Evidence pointer | One-line reason |
|---|---|---|---|---|
| 1 | Pain | 3 | research/memory-product-sdk.md Q2, Q3, Q5 | Hosts absorbed the Google removal "with help articles, not product changes"; the only selection-step metric is one Mixbook PR; no host pays any third-party curation vendor. |
| 2 | Wedge | 3 | research/memory-product-sdk.md Q6; research/assumptions/A2.md Against #5 | No habit change for the end user, but the buyer must embed outside code in its order flow, move from the out-of-process picker to a full-library grant against 5.1.1(iii), and add a 5.1.2(i) third-party-AI disclosure before any value appears. |
| 3 | Why now | 3 | research/memory-product-sdk.md bottom line, Q3; research/ai-why-now.md §6 | The dated changes are real (Vision aesthetics 2024-09, Google removal 2025-03-31, Mixbook 2026-06), and every one of them is the reason hosts built this themselves. |
| 4 | Platform risk | 2 | research/memory-product-sdk.md Q4, Q5, Q6 | Apple's free picker already has search and multi-select and Apple steers apps away from the grant this needs; Mixbook, CEWE, Shutterfly and Google/Fujifilm shipped the feature in 2025–2026. |
| 5 | Compounding asset | 3 | research/memory-product-sdk.md Q5 (CEWE charter); research/byo-ai.md Q5 | Index is discarded after each order and the models are commodity; the cross-host telemetry model has no evidence of size or of hosts agreeing to feed a vendor that serves their competitors. |
| 6 | Distribution | 3 | research/pro-channel.md Q1 (sponsor lists by year); research/memory-product-sdk.md Q5 | No evidenced channel to a host buyer: open-core conversion is admitted [unknown], and the TPM focus group reaches organizers, not Shutterfly or Mixbook, neither of which is on any sponsor list. |
| 7 | Economics | 4 | research/unit-economics.md Q3(a), Q7; research/memory-product-sdk.md Q4, Q7 | Zero marginal compute is real and the numbers are tagged, but every price is an untested assumption, the payback figure contradicts the variant's own margin line, and the hosts that might adopt are licence-only. |
| 8 | Buildability | 5 | research/ios-feasibility.md Q3, Q4, unknown #6; research/unknowns-r1.md Q5, Q8; research/face-regulation.md Q1 | A windowed on-device picker is a four-week build; the thing that proves the loop (a host A/B on completed orders) is partner-gated, the face half is policy-gated, and the latency and overlap acceptance numbers rest on models the SDK cannot ship. |
| 9 | Ceiling | 2 | research/memory-product-sdk.md Q7; variant's own Ceiling arithmetic | The variant's evidenced corner is $1.3M and its plausible case about $3M; research says "single-digit millions"; the stated $5–15M is above both. |
| 10 | Founder fit | 5 [unknown] | — | Founder has not stated strengths, constraints or runway. |

**Total: 33 / 100** (founder fit is a flagged neutral 5).

## Numbers checked against the research

Claims that fail or are unsupported:

1. **Payback "15 months" on a licence-only host.** The Distribution section computes it as 60k ÷ (60k × 0.85 ÷ 12). The Economics section puts the same host at $33k contribution, 55%. On the variant's own margin the payback is 60k ÷ (33k ÷ 12) ≈ 22 months. Add the $10–20k of counsel per host that the variant lists under "what breaks at scale" but leaves out of contribution, and year-one contribution is $13–23k, which is a 31–55 month payback.
2. **The $285k worked example describes a host the variant says will not adopt.** It needs 5M orders a year. The only sourced volumes at that scale are Shutterfly (23.6M orders, 2018) and CEWE (6.32M photobooks), and the Ceiling section excludes CEWE, Mixbook and "probably" Shutterfly. Chatbooks at $3.9–20M revenue and $15 a book is at most about 1.3M books a year (memory-product-sdk.md Q1, Q7). The adoptable tier is licence plus tens of thousands in usage.
3. **"≤5 minutes for a 12-month window on an iPhone 15" is not supported.** The 76 ms per image comes from ios-feasibility.md Q3 Scenario A, whose embedding figure is MobileCLIP-S2 or an unnamed-model secondary and whose face-embedding figure is Apple's own 2021 model. The SDK must ship SigLIP2 (iPhone latency [unknown], unknowns-r1.md Q5) and AdaFace (iPhone latency [unknown], ios-feasibility.md Q3 and unknown #6). The budget also leaves out the Vision aesthetics request and pHash; no latency for either appears anywhere in the research.
4. **The 2,400-asset window is the light-user case.** 200 photos a month is tagged in unit-economics.md Q2 as a judgment anchored on a 2015 figure, with about 600 a month as the active-taker upper bound. At 600 a month the window is 7,200 assets: 9.1 minutes central and 13.7 derated on the variant's own 76 ms, in the foreground, with the user watching. Photo-book buyers are more likely heavy shooters than average ones.
5. **Doe v. Apple is summarised too favourably.** The variant says the ruling rejected encryption as a shield "once templates sync". Per unknowns-r1.md Q8 the Local Device Class also survived summary judgment, control over on-device faceprints is a jury question, and the court wrote that "G.T. is not the silver bullet". The control theory rests on testimony that Apple "decides whether faceprints are created, where they are stored". A host that embeds a face-clustering SDK makes exactly those decisions.
6. **"Consent screen component (BIPA 15(b) text)" does not do what the line implies.** Section 15(b) requires a written release "executed by the subject" (face-regulation.md Q1). A screen shown to the keeper covers the keeper. Templates for everyone else in the window are computed before anyone taps a face. The "anonymous clusters are fine" position is tagged in face-regulation.md Q7 as an inference with no case found.
7. **Server compute "~$0.04 per 1,000 images" contradicts its own derivation.** The same line derives $3.2 per million, which is $0.0032 per 1,000; unit-economics.md Q3(a) gives $0.04–0.11 per 22,000 images. The error overstates cost roughly 4–12 times, so it does not hurt margin, but the number is wrong.
8. **"Honest number: $5–15M ARR."** The variant's evidenced corner is $1.3M; its plausible pool and share give $1.8M plus $1.2M of licences. Reaching $5M needs $0.50 an order or the $7.2M per-MAU line, which the variant itself calls "the stretch" for hosts that ship their own photo AI. memory-product-sdk.md Q7 concludes "single-digit millions ARR".
9. **TPM as a route to host product managers.** pro-channel.md Q1 lists sponsors by year. Shutterfly and Mixbook appear in none. Fujifilm appears in 2024, Epson, WHCC and Printique in 2025, and none of the four in 2026. The $1,500 focus group is with organizer members.
10. **The "30M sourced orders" floor is eight years old.** The Shutterfly orders and AOV come from a FY2018 10-K that is not in any research file, so I could not check it there. Shutterfly's Q1 2026 revenue was down 8% year on year (memory-product-sdk.md Q1). It is a 2018 data point, not a 2026 floor.
11. **Minor.** Why now #3 calls Mixbook "a ~100-person company"; the research audit withdrew that for a 55–141 range with true size [unknown].

Claims that hold: the App Groups same-team rule and the per-host restructure (memory-product-sdk.md Q6); the CEWE, Vista, Tukios, Ancestry, FamilyAlbum, Tinybeans and Photomyne figures; the Everypixel, Rekognition, Narrative and Imagen prices; the MobileCLIP relicensing; the iOS 27 background Neural Engine restriction; the G.T. v. Samsung holding; the arithmetic of 2,400 × 76 ms.

## The 4-week demo spec, line by line

| Line | Verdict | Why |
|---|---|---|
| W1 windowed PhotoKit enumeration, `.fastFormat`, network off | Buildable | Documented API. Share of assets with no local copy on optimized-storage phones is [unknown] (ios-feasibility.md Q4); the local-thumbnail behaviour rests on a 2016 community report. |
| W1 pHash, burst, edit and variant collapse "ported from current.md step 3" | Buildable, but not a port | current.md step 3 is a one-line spec; the repository holds no code. This is a first implementation. |
| W1 SigLIP2-base Core ML export | Buildable, unmeasured | No iPhone latency published (unknowns-r1.md Q5). On-disk size and in-process memory are not in the research; the SDK runs inside the host's process, so its memory ceiling and crash rate become the host's. |
| W1 Vision aesthetics request | Buildable | iOS 18+. Latency not in the research. |
| W2 Vision face rectangles, AdaFace Core ML port, clustering | Buildable, unmeasured | The variant marks latency [unknown]. iOS 27 serialises concurrent Neural Engine predictions per one developer report (ios-feasibility.md Q3), so the stages cannot run in parallel. |
| W2 consent screen, BIPA 15(b) text, deceased flag | Policy-gated | See failed claim 6. Engineering can render the screen; it cannot make the keeper's tap a release from the subject. |
| W2 diversity-constrained ranker, tap-a-face filter | Buildable | Ordinary product work. |
| W3 picker UI, selection object, sample host app with a 20-page layout | Buildable | A full week for two engineers on its own. |
| W3 contribution-link web page, proxy, dedupe on the keeper's device | Cut it | A backend, a web uploader and a sync path into the app, in the same week as the picker UI. It also puts relatives' photos on our proxy, which makes us a processor the host must disclose under 5.1.2(i) and gives us data-loss liability the "never storing originals" line says we avoid. |
| W4 ten real camera rolls "from the organizer network" | Founder-gated | The network is assumed, not held. Each owner must hand-pick 60 from thousands to create ground truth. |
| Acceptance: ≥60% overlap with the owner's top 60 | Research problem | The variant says "no benchmark exists". Nobody has measured how much one owner agrees with themselves on a second pass, so 60% may be above the noise ceiling. |
| Acceptance: ≤5 min on an iPhone 15 | Unsupported | See failed claims 3 and 4. |
| Acceptance: zero face vectors leave the device | Buildable and checkable | Network capture is a fair test. |
| Android deferred | Gates the sale | Shutterfly has "10M+" Play installs and Chatbooks "1M+" (memory-product-sdk.md Q1); a second-tier host will ask for parity, which is a second build on LiteRT or ONNX. |
| Not in the spec: an A/B on a host's completed orders | Partner-gated | This is the variant's own day-1 value and its load-bearing assumption 2. Two engineers cannot produce it without a host's engineering team, legal review and App Review of the host's build. |

**What breaks under load.** The variant says "nothing on compute". True, and it is the wrong place to look. (a) Support: the SDK sits in a host's checkout funnel through the holiday peak, and 0.1 FTE a year per host does not cover an in-process ML library across annual iOS changes such as the iOS 27 Neural Engine restriction. (b) Liability: a crash or a bad selection costs the host orders, and the host will want an SLA from a two-person vendor. (c) Legal: the host is the BIPA "private entity", has already paid once in Shutterfly's case, and will price that into the contract or strike the face feature. (d) Access: a user who grants limited rather than full access gives the SDK only the photos they picked (platform-access.md Q1), and the share of users who do so is not in the research.

## Most damaging objection

**The four-week build proves the one thing no buyer in the evidence needs proved, and the thing that would prove the business cannot be built by two engineers.** The demo uses only free Apple APIs and open models. That is the recipe Mixbook shipped in 2026-06, CEWE rolled out to all subsidiaries in 2025 and Shutterfly ships as Autofill "Best Photos" (memory-product-sdk.md Q5); the variant concedes "a host's engineers can build the same four weeks". The proof that matters is a lift in completed orders inside a host's flow. Getting it requires a host to put outside code in its checkout, swap Apple's picker for a full-library grant, add a third-party-AI disclosure, and, for the face half, accept BIPA exposure in an industry where Shutterfly paid $6.75M and where on-device faceprints went to a jury in Doe v. Apple on 2026-09-30. The hosts with volume have built it. The hosts left over are licence-only at $60k, with $33k contribution before counsel and a payback of 22 months or more against the 15 the variant states.

## Weakest dimension

**Ceiling (2), tied with Platform risk (2).** Ceiling is the one the variant's own arithmetic closes: $1.3M evidenced, about $3M plausible, and no route to $100M.

## Unknowns research could resolve before the next round

1. What are the measured Core ML latency, on-disk size and peak memory of the SigLIP2-base-patch16-256 image tower, an AdaFace IR-50 or IR-101 port, and Vision `CalculateImageAestheticsScoresRequest` on an iPhone 13 and iPhone 15?
2. What share of iOS users choose full rather than limited Photos access when a photo-print or photo-book app asks (any published opt-in rate since iOS 17)?
3. Has App Review approved or rejected any photo-book or print app under guideline 5.1.1(iii) for requesting full library access since 2024, and has any rejection cited a third-party SDK?
4. Which third-party SDKs do Chatbooks, FreePrints, Printique, Artifact Uprising, Tinybeans and Storyworth embed in their iOS apps today (privacy manifests or app SDK inventories), and is any of them a photo-selection or ML vendor?
5. What does the Doe v. Apple order of 2026-09-30 (S.D. Ill. 3:20-cv-00421, Doc. 373) hold about "control" of on-device faceprints for the Local Device Class, and has any Illinois state court followed or rejected G.T. v. Samsung since 2026-08-07?

## Three questions for the founder

1. Do you have a named product or engineering decision-maker at any of the eight second-tier hosts who would let two outside engineers ship code into their order flow before a holiday code freeze? If not, what gets the first pilot?
2. Would you drop the face half entirely (dedupe, aesthetics and day or event diversity only) to take BIPA and subject consent out of the host's legal review? If so, is what remains worth $60k a year next to Apple's free aesthetics call?
3. Can you fund 12–18 months to a first signed host, at $10–20k of counsel per deal, for a business whose own arithmetic tops out at about $3M? If the real plan is an acquisition, who is the acquirer and why would they not hire two iOS engineers instead?
