# Critique — v2-grandparent, round 2, BUILDER

Written 2026-11-24 by a fresh-context critic. Inputs read: SCORECARD.md, variants/v2-grandparent.md, variants/current.md (not needed beyond the variant's own "Kept" list), research/ (grandparent-loop, ios-feasibility, face-regulation, unknowns-r1, unit-economics, ai-why-now Q3, sizing Q4, platform-access Q1–Q2, memory-product-sdk Q6, customers Q1(c)/(h), competitive Q5, digitization-market Q4, assumptions A2–A4, A6; the remaining tracks were searched for terms the variant relies on rather than read end to end). Not read: CHANGELOG, other v2 variants, any critique.

Date caveat: the research is dated 2026-11-03, three weeks old. Nothing was re-fetched. Items most likely to have moved since: Tinybeans' 3 Nov securities issue and Q1 FY27 4C, FamilyAlbum releases after v23.2.0, and the Doe v. Apple amended class notice (due 2026-10-14).

## Stance

Builder. I believe shipped demos. I score Buildability and Economics hardest, and I read the 4-week spec line by line for research problems, platform gates and policy gates. I also ask what breaks at 10k families.

## Scores

| # | Dimension | Score | Evidence pointer | One-line reason |
|---|---|---|---|---|
| 1 | Pain | 4 | research/customers.md Q1(h); research/assumptions/A3.md verdict (iii); research/grandparent-loop.md Q6 | The category is paid ($59–75/yr, ~¥17.1B segment), but the pain this variant removes is the manual pick and second upload on top of a free, unlimited, 4.9-rated incumbent; the variant itself calls it "a convenience gain, not a new job". |
| 2 | Wedge | 5 | research/platform-access.md Q1 (Limited Library); research/assumptions/A2.md Against #5; research/ios-feasibility.md Q2 | No migration and relatives need no install, which is real. But the parent must grant full-library access (iOS offers Limited; guideline 5.1.1(iii) prefers the picker), and "found for you" only runs when the parent opens the app. |
| 3 | Why now | 4 | research/ai-why-now.md Q3; research/unknowns-r1.md Q8; research/ios-feasibility.md Q2 | Find-and-send over PhotoKit with on-device faces was buildable in 2019–2020. The dated items are incumbent posture and a legal ruling that the same research shows is not settled; iOS 27 actually tightened background Neural Engine access. |
| 4 | Platform risk | 3 | research/grandparent-loop.md Q1 (S6 face recognition, per-child pages), Q3 (12 releases Jun–Nov 2026); research/customers.md Q1(c) | FamilyAlbum already runs face recognition and ships fortnightly; Google Partner Sharing already offers "Only photos containing selected people"; Apple opened Shared Albums to Android on 2026-06-08. The differentiator is one release note away. |
| 5 | Compounding asset | 4 | research/face-regulation.md Q7 (rules 1–2, un-named share 19–46% on assumed inputs); research/ios-feasibility.md Q9; research/unit-economics.md Q3 | Index is rebuildable for cents; the identity graph compounds only at the rate of consent, and on-device-only templates do not travel to a new phone or a second device. |
| 6 | Distribution | 4 | research/grandparent-loop.md Q1 (ad spend S3 p.30), Q4, Q5, Q2 ("organic growth has stalled") | The loop is evidenced for acquiring viewers at one operator, with ¥1.9–2.0B/yr of segment ad spend and negative EBITDA in FY2024–25. Relatives per family, acceptance and time-to-second-member are disclosed by nobody. |
| 7 | Economics | 5 | research/unit-economics.md Q6, Q7 (A-index-only row); research/sizing.md Q4 | Infra is sourced and cheap (index-only 86% GM). The lines that decide the P&L are assumptions: support $4, notifications $0.10/mo, CAC $35–50, a 4.8-year life. The free base that the variant's own 10% paid conversion implies is not in the contribution figure. |
| 8 | Buildability | 5 | research/ai-why-now.md Q3 (infants); research/ios-feasibility.md Q2, Q3, Q9; research/face-regulation.md Q7 rule 1 | A degraded core loop (recent roll, baby-ish face plus time, one-tap send, browser feed) is a 4-week build. The spec as written is three demos plus a cohort study, its headline is a research problem, and its acceptance criteria cannot be measured inside the four weeks. |
| 9 | Ceiling | 3 | research/grandparent-loop.md §4 verdict, Q1 (4.3% follower billing) | The arithmetic is shown and honest about missing $100M, but the central case assumes enrolment about 3x the variant's own estimate of FamilyAlbum's North America rate, and the research's own base case for this exact shape is $5–10M. |
| 10 | Founder fit | 5 [unknown] | — | Not stated by the founder. Neutral placeholder. |

**Total: 42** (founder fit is a flagged neutral 5).

## Claims checked against the research

Failed or unsupported:

1. **"Infant faces in months 0–12 … have no published open-model benchmark [unknown]" and "every benchmark in research/ is adults or children ≥2 years."** Contradicted by research/ai-why-now.md Q3: Hossain et al. (IJCB 2025), infants and toddlers 0–3 years with FaceNet/ArcFace/MagFace/CosFace, TAR@0.1%FAR of 30.7% for 0–6 months and 64.7% for 2.5–3 years (secondary, abstract only). The benchmark exists in the file the variant cites, and it is bad.
2. **"On-device-only templates are now the litigated safe design."** research/unknowns-r1.md Q8: in Doe v. Apple (order of 2026-09-30) the Local Device Class survived summary judgment, whether Apple controls on-device faceprints is a jury question, and "G.T. is not the silver bullet that Apple believes it to be". G.T. v. Samsung footnote 2 assumes without deciding that the templates are biometric identifiers. On-device is the better design, not a settled safe one.
3. **"The 38–57-minute full-library session the round-1 builders measured … [sourced]."** research/ios-feasibility.md Q3 tags it [estimated] from assumed per-image costs; nothing was measured.
4. **Tinybeans "a −97% share price since 2021 [sourced]."** Withdrawn in research/grandparent-loop.md Q2 and row 38a; only the one-year −69.57% stands.
5. **"A$1.64M cash."** The research figure is US$1.64M (grandparent-loop.md Q2).
6. **"~93k at Q4 FY26."** Withdrawn and superseded by ~95k (grandparent-loop.md row 37).
7. **"11 free photo prints up to 3 times per month [sourced: BusinessWire]."** The research marks this unverified (HTTP 403); the verified hook is 8 free prints a month (2022).
8. **Blended ARPU $97.** The 4.3% is the share of June-2025 new paying members who were followers (grandparent-loop.md Q1, S3 p.12), and one subscription covers the whole album. It is a substitute payer, not an added one. Removing the $7.7 leaves about $90, and that still rests on a 30% Archive attach rate with no evidence.
9. **"Honest number $25–45M US."** research/grandparent-loop.md §4 concludes the honest base case for an index-only entrant on this loop alone is "roughly $5–10M". Re-running the variant's formula at its own estimate of FamilyAlbum's North America rate (about 5% of births, 10% paid, 4.8–6.6-year life, $60–97) gives roughly $5–12M [critic's arithmetic on the variant's inputs].
10. **"Server-side matching off in IL/TX/WA/EU (12.7% of the US population)."** The 12.7% in face-regulation.md Q7 is Illinois plus Texas only.
11. **"FamilyAlbum has the same constraint (parents upload manually), so parity."** No evidence found in research on whether FamilyAlbum has auto-upload or suggested photos. This is the claim the whole wedge is measured against and it is unverified.
12. **Android: "a baby-photo app is the textbook case"** for `READ_MEDIA_IMAGES`. research/memory-product-sdk.md Q6 quotes the policy as allowing the permission only when pickers "are not sufficient"; a sharing app where a picker works is the contested case, not the textbook one. (Android capture is v1.1, so this does not gate the demo.)
13. **Qeepsake "79% retention → 4.8 years."** Both customers.md Q1(h) and grandparent-loop.md Q2 flag the Tinybeans/Qeepsake retention KPIs as unreconciled (the glossary defines retention monthly). Every LTV/CAC figure above 1.3 years of life rests on this.
14. **Registry CAC $35–50.** An assumption between two unrelated anchors. The Babylist deal ran to December 2024 with a 10-day exit and is absent from FY26 releases (grandparent-loop.md Q5); the research's own paid-UA estimate is $65–90 and "underwater" (sizing.md Q4).

Confirmed: US births 3,628,934; FamilyAlbum 30M registered, 12M MAU, 65% Japan, >40% overseas, US pricing; MIXI segment ¥17,159M and 5.1% margin; Tinybeans ~95k paid and ~1M active families; RevenueCat 23% first annual renewal and 22.2% trial-to-paid; index-only $0.16/mo and 86% GM; vector hosting $0.05 and incremental indexing $0.007; Stripe and App Store fees; the payback and required-base arithmetic all recompute correctly from the stated inputs.

## The 4-week demo spec, line by line

| Spec line | Verdict | Why |
|---|---|---|
| W1: PhotoKit change observation over the recent roll | Buildable | Standard API; a few hundred items is under a minute at the research's 76 ms central estimate (ios-feasibility.md Q3). Requires `.authorized`; a parent who picks Limited gets FamilyAlbum's manual flow. |
| W1: AdaFace via Core ML, infant cluster | **Research problem** | 30.7% TAR for 0–6 months (ai-why-now.md Q3). No latency figure exists for any ArcFace/AdaFace Core ML port on an iPhone (ios-feasibility.md Q3). A one-baby household can probably be served by "any small face plus recency", but then nothing identity-specific is being built. |
| W1: SigLIP 2 Base on-device | Buildable, unmeasured | Apache-2.0 confirmed; iPhone latency [unknown] (unknowns-r1.md Q5). Not needed for the core loop; cut it. |
| W1: 300 KB derivative and upload | Buildable for photos | The optimized local copy is enough (ios-feasibility.md Q4). Video is absent from the spec; iCloud-only video originals must be downloaded and transcoded on device, and video is a large part of what grandparents want. |
| W2: magic-link browser feed, reactions, comments, voice notes | Buildable | A no-account link is a bearer token to a child's photos. Forwarding and link-preview fetchers need a design before 10 real families use it. |
| W2: SMS notifications | **Policy-gated** | No evidence found in research on US carrier registration or on texting a relative who never opted in. From general knowledge, registration takes days to weeks and app-initiated invites to non-consenting numbers raise TCPA questions; treat as unverified and research it. The share-sheet route (parent sends the link) avoids both. |
| W2: "that's me" screen with BIPA 15(b) e-signature text | Policy-gated | Engineers can build the screen; the text needs counsel (face-regulation.md Q5, Q7). Low risk for a 10-family pilot outside IL/TX/WA/EU. |
| W3: second phone, cross-member face suggestions, zero templates off-device | **Underspecified** | face-regulation.md Q7 rule 1 states the cost of on-device-only as "no server-side cross-library clustering; web client loses faces". The only compliant route is each phone re-deriving templates from shared derivatives and seeding from name labels. That is a design to invent, not a week-3 task. |
| W3: v2-prints scan flow "reused" | Schedule risk | It reuses code from another variant's demo that does not exist yet. This is a second product inside week 3. |
| W3: names written as XMP/keywords to the scanner's own library | **Platform-gated on iPhone** | The evidence for keyword import is osxphotos on macOS (ios-feasibility.md Q9). No evidence found that an iOS app can write keywords or names to existing Photos assets. New scans can carry embedded XMP; existing assets cannot be labelled. |
| W4: natural-language search, Claude connector link | Buildable, off the critical path | A6 holds on Claude Free. It proves nothing about the loop; cut it from the demo. |
| W4: ten families from a prenatal class; grandparent weekly return "over 4 weeks" | **Impossible in the window** | A prenatal class has no baby to photograph. A week-4 return rate needs four weeks after onboarding. Add TestFlight beta review. The acceptance thresholds and the kill criterion cannot be read before roughly week 9–10. |

The smallest thing that proves the core loop: iPhone only, recent roll only, "photos with a small face from today" plus one-tap confirm, share-sheet link, browser feed with reactions, email digest. Two engineers, four weeks to build, then six weeks with ten families who already have a newborn. Drop Scan, Join, Ask and the connector until grandparent weekly return is known.

## What breaks at 10k families

- **Cost.** Infra is negligible. Notifications are not: the $0.10/mo is an assumption, and daily texts to six relatives would be a multiple of it [critic's estimate, no SMS price in research]. Browser-only grandparents on iPhone have no free push channel short of adding a web app to the Home Screen, which is an install. Email digests become the retention channel.
- **Support.** About 60k relatives on bearer links, with lost links, new phones and spam-foldered digests. At 10% paid, 1,000 payers ($59k ARR) carry support for 10,000 families. The $4/family/yr is tagged as a guess, and it is applied only to payers.
- **Data-loss liability.** The product is not the system of record but will be perceived as one ("the archive that outlives the feed"). The free tier keeps 30 days of history, so grandparents will watch photos disappear. If a parent's originals are lost, the family holds 300 KB copies. A replaced phone loses its on-device templates and clusters unless they go into a device backup, which contradicts "zero templates off-device".
- **Legal exposure.** Every face in every scanned photo is templated on-device, including other people's children; the defence is G.T. v. Samsung alone, and the Local Device Class in Doe v. Apple is going to a jury. Named rectangles held on the server are derived from those templates; whether that is "biometric information" under BIPA is not addressed in the research. One leaked feed link to a child's photos is the reputational event (Peekaboo Moments, grandparent-loop.md Q3).

## Most damaging objection

The only thing this product does that FamilyAlbum does not is "your phone already found today's photos of Mia", and that feature rests on recognising a newborn. The research the variant cites reports 30.7% TAR@0.1%FAR for infants 0–6 months on ArcFace-class models (ai-why-now.md Q3), while the variant states that no such benchmark exists. The variant's own fallback is time-and-location plus a daily confirm. In that state, and with indexing running only when the parent opens the app (ios-feasibility.md Q2) and only if they granted full-library access against guideline 5.1.1(iii), the entrant is FamilyAlbum's manual pick without free unlimited storage of originals. And if a simple "infant face plus recency" detector turns out to be good enough for a one-baby household, FamilyAlbum, which already runs face recognition for per-child pages and shipped 12 releases between June and November 2026 (grandparent-loop.md Q1, Q3), can ship the same thing as a release note. Either way the wedge has no period in which it is both working and exclusive.

## Weakest dimension

**Platform risk (3)**, tied numerically with Ceiling (3). Platform is named because it gates the wedge itself: the ingredients already sit with the incumbent and with Google Partner Sharing ("Only photos containing selected people", customers.md Q1(c)). Ceiling at 3 follows from the research's own $5–10M base case.

## Unknowns to research before the next round

1. What is the measured accuracy of open, commercially licensed face models (AdaFace, MagFace) on infants 0–12 months at gaps of 7, 30 and 90 days in a closed household set (Hossain et al., IJCB 2025 full text, per-age-bin and short-gap results), and are AdaFace's released weights cleared for commercial use given their training data?
2. Does FamilyAlbum, Tinybeans or Google Photos already auto-suggest or auto-add new camera-roll photos of a chosen child (FamilyAlbum auto-upload or suggested photos; Google Photos auto-updating shared albums by face group), and can link viewers see them without an account?
3. What share of iOS users choose "Allow Full Access" versus "Limit Access" when a photo-sharing app asks for the library, and are there documented App Review rejections under 5.1.1(iii) for sharing apps requesting full access?
4. What are current US A2P 10DLC and toll-free verification timelines and per-message costs, how do the TCPA and carrier rules treat app-sent invitation texts to relatives who have not opted in, and which channel (email digest, SMS, push) do FamilyAlbum and Tinybeans use for relatives?
5. Has any court or regulator treated name labels or face rectangles derived from on-device templates and stored on a company server as "biometric information" under 740 ILCS 14/10, and what is the trial schedule for the Local Device Class in Doe v. Apple?

## Three questions for the founder

1. If infant recognition does not hold in the first 90 days and launch is "baby-ish face plus one-tap confirm", what is the reason a parent picks this over FamilyAlbum's free unlimited album, stated in one sentence you would put on the App Store page?
2. The honest schedule is four weeks of build plus about six weeks of measurement with families who already have a newborn. Do you have runway for roughly ten to twelve weeks before the first read, and do you have a route to ten such families (doula, lactation consultant, parent group) rather than a prenatal class?
3. Will you launch with Illinois, Texas, Washington and the EU switched off for anything that names a living person, pay for biometric counsel before the consent screen ships, and who answers the grandparents' support email?
