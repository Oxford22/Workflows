# v2-grandparent — Round 2 critique — COLD SEED INVESTOR

Critic run 2026-11-24 against research gathered 2026-11-03 (three weeks stale; the Tinybeans Q1 FY27 4C of 2026-10-28 and the 2026-11-03 securities notice were unread then and are still unread here).

## Stance

Default is no. I am asked to fund a paid convenience layer on top of a job that the category leader does free, for a customer (new parent) who ages out, with a second payer (grandparent) that the research says does not pay. I score Ceiling, Distribution and Platform risk hardest.

Reading coverage, stated plainly: read in full — SCORECARD.md, variants/v2-grandparent.md, research/grandparent-loop.md, research/sizing.md, research/assumptions/A3.md, research/assumptions/A4.md. Read the sections the variant cites — customers.md Q1(c), Q1(h), Q2, Q3; unit-economics.md Q6, Q7; face-regulation.md Q6, Q7, risk table; ios-feasibility.md Q2–Q7; unknowns-r1.md Q1, Q4–Q10, summary table; memory-product-sdk.md Q6, Q7; ai-why-now.md Q3 (face models). Keyword-searched only (newborn / grandparent / FamilyAlbum / Tinybeans / the specific numbers cited) — competitive.md, digitization-market.md, genealogy-market.md, platform-access.md, trades-and-reddit.md, A2.md. Not opened beyond a zero-hit keyword search — byo-ai.md, estate.md, pro-channel.md, verticals.md, A1.md, A5.md, A6.md (none carries newborn-loop evidence; their content reaches this critique only through the SCORECARD summaries). variants/current.md: headings and the "What Round 2 must change" paragraph only. No CHANGELOG, no other v2 variant, no critique was read.

## Scores

| # | Dimension | Score | Evidence pointer | One-line reason |
|---|---|---|---|---|
| 1 | Pain | 5 | grandparent-loop.md Q1, Q2; customers.md Q1(h); A3.md verdict (iii) | The base job (show the grandparents the baby) is real and paid for, but in the US it is paid at Tinybeans scale ($4.82M subscription revenue, core subs flat at ~49.8k) and done free at FamilyAlbum; the pain this variant removes is one step, the second upload. |
| 2 | Wedge | 4 | ai-why-now.md Q3 (Hossain et al., IJCB 2025); ios-feasibility.md Q2; customers.md Q1(c) | Parent must install a new app, grant full-library access and open it daily (no unattended indexing); the "auto-found" headline rests on infant faces, where the research's only benchmark is 30.7% TAR at 0–6 months; the variant itself calls day-1 value "modest". |
| 3 | Why now | 4 | grandparent-loop.md Q1 (FamilyAlbum launched April 2015), Q2; A4.md Against #1, #5 | Nothing dated makes a newborn feed newly possible; the list is competitors repositioning (Tinybeans' repositioning did not move its paid base), a counter-signal (Shared Albums to Android), and enablers every developer and both incumbents get too. |
| 4 | Platform risk | 3 | grandparent-loop.md Q1 and Q3 store table; customers.md Q1(c); A4.md Against #1; unknowns-r1.md Q1 | FamilyAlbum ships fortnightly, already runs face recognition for per-child pages and added a Memories screen in Oct 2026; Google partner sharing already auto-shares "only photos containing selected people" (to one partner); survival is argued from MIXI's business model, not from anything it cannot build. |
| 5 | Compounding asset | 4 | face-regulation.md Q7 (un-named share, assumptions); SCORECARD round-0 row (index rebuildable for <$1); grandparent-loop.md Q6 implication | By design it is not the system of record, exports the names, and keeps templates on-device; what is left is a names-and-rectangles graph that grows at the rate relatives sign consent screens. |
| 6 | Distribution | 3 | grandparent-loop.md Q4, Q5, rows 20a–20c; sizing.md Q4 row 33, Q5 | The loop brings viewers, not new families; relatives per family and invite acceptance are undisclosed by everyone; the one operator that scaled it also spent ¥1.9–2.0B/yr on ads and ran the segment at a loss; the registry CAC of $35–50 is an assumption. |
| 7 | Economics | 5 | unit-economics.md Q6, Q7 (A-index-only row); grandparent-loop.md Q2; customers.md Q1(h) reconciliation warning | Per-payer model is tagged and the arithmetic checks, but the free tier (10 relatives, notifications, grandparent support) is not carried by the payers in the model, and both payback inputs (CAC, life) are assumptions. |
| 8 | Buildability | 5 | ai-why-now.md Q3; ios-feasibility.md Q2, Q3; unknowns-r1.md Q4, Q5 | Find + send + web feed is a 2-week build; find + feed + second phone + print scan + search + connector + a ten-family pilot with a "week-4 return rate" acceptance test is not a 4-week demo; AdaFace and SigLIP 2 iPhone latency are both [unknown]. |
| 9 | Ceiling | 2 | grandparent-loop.md §4 verdict and row 46; sizing.md "Ceiling arithmetic"; digitization-market.md audit item 3; customers.md Q1(h) | No path to $100M (the variant says so), and its "honest" $25–45M sits 3–5x above the research's own verdict for this exact shape ($5–10M), on contradicted or withdrawn inputs. Scored 2 per the rule. |
| 10 | Founder fit | 5 [unknown] | — | Founder has not stated strengths, constraints or runway. |

**Total: 40 / 100** (founder fit is a flagged neutral 5).

## Claims checked against the research

Verified as stated: US births 3,628,934 (grandparent-loop.md S54); FamilyAlbum 30M registered, 12M MAU, 65% Japan, >40% overseas, ~20% North America; US price points; Lifestyle ¥17,159M and ¥876M (5.1%); Tinybeans ARPU $75, Qeepsake $64, CAC $35 / $100 → $19; Babylist terms; sizing.md rows 12, 17, 19, 21, 22, 24; paid-UA CAC $65–90; index-only 86% GM; IL+TX 12.7%; the G.T. v. Samsung and Doe v. Apple outcomes. Every sum in the Economics and Ceiling sections reproduces.

Failed claims (the research contradicts or does not support them):

1. **"The only consumer pool where money already flows at nine figures to a photo-sharing subscription" / "proven subscription pool ≈ $114M".** The ¥17,159M is the whole Lifestyle segment — FamilyAlbum plus minimo, mixi and mixi2, and inside FamilyAlbum GPS trackers, prints, New Year cards and ads. FamilyAlbum-only revenue, Premium subscriber count and the premium/prints split are all [unknown] (grandparent-loop.md Q1, §6 item 1). Q3 alone, the New Year card quarter, is roughly a third of the year. This is a segment, not a subscription pool.
2. **"No published open-model benchmark" for infant faces.** The file the variant cites has one: Hossain et al. (IJCB 2025), infants and toddlers 0–3 with FaceNet/ArcFace/MagFace/CosFace, TAR@0.1%FAR 30.7% for 0–6 months, 64.7% at 2.5–3 years (ai-why-now.md Q3; secondary, abstract only). It is a longitudinal test, not same-week clustering, but it is the only number and it points the wrong way for a ≥90% precision gate.
3. **Follower billing as +$7.7 of ARPU (3 relatives × 4.3% × $60).** The 4.3% is the share of June-2025 new members who were paying followers, not the probability that a given relative pays; and one subscription covers the whole album, so a paying follower replaces the parent's payment rather than adding to it (grandparent-loop.md Q1, S3 p.12, S12).
4. **30% of paying families attach a $99 grandparent Archive tier.** No source. The research's net finding is the opposite: "no evidence that grandparents refuse apps; the evidence is that they refuse to *pay* for them, which is why both incumbents make the parent the single payer" (grandparent-loop.md Q7).
5. **Paid conversion ~10% (95k ÷ 1M).** The 95k includes 45,525 Qeepsake subscribers bought in Nov 2025. Tinybeans core is 49,793; the FY25 KPI slide gives 51K paid on 0.86M MAU, about 6% (customers.md Q1(h); grandparent-loop.md Q2).
6. **Life of 4.8–6.6 years in the "evidenced corner".** The 96% is an unreconciled vendor KPI; the same vendor's 93% is defined as monthly, which implies about 14 months (customers.md Q1(h) reconciliation warning). The category median first annual renewal is 23% (unit-economics.md Q6). The 60% age-out retention is the variant's own assumption.
7. **Enrolment of 10–20% of US births.** No source. The variant's own estimate for FamilyAlbum in North America is ~5% of births a year, with free unlimited storage and segment ad spend at 13–15% of sales. The Tinybeans "~8% of births" divides a worldwide cumulative vendor claim by US births.
8. **Withdrawn numbers still used:** "~93k at Q4 FY26" (grandparent-loop.md row 37, withdrawn); "−97% share price since 2021" (row 38a, withdrawn; only −69.6% over one year stands); "Legacybox ~200k families/yr" (digitization-market.md audit item 3, withdrawn; a floor of ~180k/yr, trend unknown).
9. **Mis-tagged or stale:** Google One Standard 200 GB at $2.99 cited to unknowns-r1.md Q7, which withdrew $2.99 in favour of $4.99 (CNBC, secondary); "11 free photo prints up to 3 times per month" tagged [sourced] when the research downgraded it to unverified secondary (S22, 403); Tinybeans Family $119.99 appears only in the FY25 deck, not on the current storefront; "a baby-photo app is the textbook case" for READ_MEDIA_IMAGES is the variant's reading, not a policy statement (memory-product-sdk.md Q6).

## The single most damaging objection

**The ceiling the variant calls "honest" is three to five times what its own research file concludes, and the gap is made of four inputs the research contradicts.** grandparent-loop.md §4 was written for exactly this shape and ends: "The honest base case for an index-only entrant on this loop alone is Tinybeans-shaped — roughly $5–10M revenue — not $100M." The variant reports $25–45M US by assuming (i) 10–20% of US births enrol, when FamilyAlbum's North American run-rate is ~5% on the variant's own arithmetic and was bought with free unlimited storage of originals, the one promise index-in-place gives up; (ii) 10% of enrolled families pay, when Tinybeans core is about 6%; (iii) a paid life of 4.8–6.6 years, from vendor KPIs the research flags as unreconciled; and (iv) a $99 grandparent tier attaching at 30%, when both incumbents concluded grandparents do not pay.

Re-running the variant's own sensitivity line with the research-supported end of each input — births 3.63M × enrolled 5–15% × paid 5–10% × life 1.3–4.8 years × $60 — gives roughly $0.7M–$16M, centred on single-digit millions. That is Tinybeans: about 95k paid, fourteen years after its 2012 founding (competitive.md Q5) and after buying Qeepsake, "organic growth has stalled", A$7.33M market capitalisation. It is a small business competing with a free product from a company that ships every two weeks. It is not a seed-fund outcome, and no pilot result short of Backblaze-grade retention (assumption 13) changes that.

## Weakest dimension

**Ceiling (2).** Distribution (3) and Platform risk (3) are close behind and are the reasons the ceiling is low: the loop recruits viewers rather than families, and the incumbent can copy the differentiator in a release.

## Unknowns research could resolve before the next round

1. What is FamilyAlbum's Premium subscriber count or paying rate, and FamilyAlbum-only revenue split by premium / prints / GPS / ads? (MIXI FY2026 Q4 results deck and FY2027 Q1/Q2 decks; the Q4 deck also carries the "comments and stickers posted" chart.)
2. How many new families per year does FamilyAlbum register in the US, and how many relatives join per album? (Search: FamilyAlbum US users families per album; MIXI "WAF" weekly active families; Sensor Tower / data.ai US downloads for us.mitene.)
3. What precision and recall do current on-device face models reach on infants aged 0–12 months within a 30–90 day window? (Hossain et al. IJCB 2025 full text; "infant face recognition" + "newborn face clustering" benchmarks; how Apple Photos and Google Photos group babies.)
4. Do FamilyAlbum, Tinybeans or Google Photos already suggest or auto-add a child's new camera-roll photos? (FamilyAlbum release notes and help centre for "auto upload" / "suggested photos" / AI search; Google Photos live albums and partner sharing "selected people"; Tinybeans' AI organisation launch status.)
5. What do Tinybeans' Q1 FY27 4C (2026-10-28) and FY26 annual report show for core Tinybeans subscribers, the 6-account Family tier's uptake, and the purpose of the 2026-11-03 securities issue? (ASX: TNY announcements; any broker or press relay since 2026-11-03.)

## Three questions for the founder

1. FamilyAlbum is free, unlimited, keeps the originals and is already on the grandparents' phones. Your free tier keeps 30 days and stores nothing. Name the specific family that picks yours at the birth, and tell me what they say when their friend asks why they are not using the free one.
2. If the pilot shows infant-face clustering below your 85% floor and "find" falls back to time-and-location plus a daily confirm, what is left that a parent would pay $59 for, and would you still build this?
3. Your own honest number is $25–45M and the research says $5–10M. Are you asking for venture money for a business you believe tops out there, or is there a second act you have not written down — and if so, what is the evidence for it today?
