# v3-care — round 3 — BUILDER critique

Written 2026-11-25. Fresh context. Variant scored: `variants/v3-care.md` (written 2026-11-24, before `research/institutional-legacy.md` and `research/family-artifact-market.md` were repaired on 2026-11-25).

## Stance

Builder. I believe shipped demos. I scored Buildability and Economics hardest, checked the 4-week spec line by line, and asked what breaks at scale. Where the variant and the repaired research disagree, the research wins and I say so.

Reading coverage, stated plainly: read in full — SCORECARD.md, variants/v3-care.md, variants/current.md, research/institutional-legacy.md (including its audit log). Read by section — memoir-gift-market.md (bottom line, Q3–Q8), family-artifact-market.md (bottom line, Q2, Q3, Q5, numbers rows), sizing.md (Q4, worked chains), face-regulation.md (Q1–Q3 definitions, Q7 references). Opening summaries plus targeted searches for the variant's cited numbers — grandparent-loop.md, digitization-market.md, unit-economics.md, estate.md, unknowns-r1.md, byo-ai.md, pro-channel.md, customers.md, competitive.md, genealogy-market.md, memory-product-sdk.md, assumptions/A6.md. Searched only (no senior-care, voice or consent content found) — ai-why-now.md, ios-feasibility.md, platform-access.md, trades-and-reddit.md, verticals.md, assumptions/A1–A5. Not read, as instructed: CHANGELOG, other v3 variants, critiques, research/audits/.

## Scores

| # | Dimension | Score | Evidence pointer | One-line reason |
|---|---|---|---|---|
| 1 | Pain | 4 | institutional-legacy.md bottom line 2 and 5; Q3 "What they prove"; Q4 | Operators pay $9–$18 per person per year on the one current list price found; the category's largest identifiable payer is NIH and penalty-fund grants, and the federal "life history" rule is met by the MDS form. |
| 2 | Wedge | 4 | institutional-legacy.md Q5, Q8; digitization-market.md Q6 | The family link needs no migration or app, but value starts only after a 6–8 month path to a pilot, staff must sit in on every resident session, and the only study lost 2 of 6 homes after management turnover. |
| 3 | Why now | 5 | memoir-gift-market.md Q5; institutional-legacy.md Q2 (TSOLife 2025-05-07, LifeLoop Life Story) | Real-time voice at $0.02–$0.14 a minute is a real, dated change; every other dated item in the variant is a competitor shipping, so the change helps incumbents at least as much. |
| 4 | Platform risk | 4 | institutional-legacy.md Q2 (LifeLoop Life Story; MatrixCare lists LifeLoop as a partner), Q5 (marketplace gating); family-artifact-market.md Q5 | No Apple or Google dependency at all, which is new. The category platform is the risk: LifeLoop already ships the staff-facing half inside an existing contract and holds the EHR partner slot. |
| 5 | Compounding asset | 4 | institutional-legacy.md Q8 (2 of 6 homes withdrew); grandparent-loop.md Q1 (4.3% follower pay); family-artifact-market.md Q1 (Nixplay about 1.2%, unverified inputs) | Voice-and-photo records cannot be rebuilt after memory fails, which beats a rebuildable index, but they belong to the family, who mostly do not pay; the payer's deliverable is a PDF. |
| 6 | Distribution | 3 | institutional-legacy.md Q1 (top four operators at most 2.7–3.4% of communities), Q5 (cycle, pilots, marketplace terms unknown) | No non-paid channel with evidence that it produces communities. The one channel is direct sales with every conversion input assumed. |
| 7 | Economics | 4 | institutional-legacy.md bottom line 5, Q3 prices; family-artifact-market.md Q2 (Famileo Pro US $99 a month), Q3 (print prices) | The model is fully tagged and the arithmetic checks, but the price it rests on is 6–12 times the only current life-story list price; at current list prices its own COGS gives −6% to +30% gross margin. |
| 8 | Buildability | 5 | memoir-gift-market.md Q5 (voice stack prices; response of people 70+ unknown; one n=20 single-session study with cognitive impairment); institutional-legacy.md Q5 | The family-only "by Friday" page is a two-week build. The resident interview is unproven on impaired speech (no evidence found in research), the week-4 run is gated by a site, counsel and BAAs, and two acceptance tests cannot be measured inside four weeks. |
| 9 | Ceiling | 2 | institutional-legacy.md bottom line 1, 6; Q8 table | No institutional life-story vendor has a sourced $10M; the largest is about $2M including an unknown share of grants; at the current list price the variant's central licence line is $1.1–$2.2M, not $13.4M. |
| 10 | Founder fit | 5 [unknown] | — | Neutral placeholder; founder has not stated strengths, constraints or runway. |

**Total: 40** (with founder fit at the flagged neutral 5).

## Variant claims that fail against the repaired research

The research wins on each of these.

1. **"Engagement software: $39–$650 per community per month."** Withdrawn in the repair: it joined a streaming add-on to an EHR. What stands: add-ons $39–$99 a month; EHR-class tools $450–$650 per location a month; LifeLoop's price unknown [institutional-legacy.md Q2].
2. **"Current prices: [unknown]" for life-story programmes, and the $40–$154 per resident band as the comparable.** The repair found a current price: LifeBio group licences at $149 (census 100–199) and $349 (300–399), labelled "Monthly Billing", which is about $9–$18 per person per year if monthly [institutional-legacy.md bottom line 5, Q3]. The variant's $108 list is 6–12 times that [estimated: 108 ÷ 17.88; 108 ÷ 8.98]. The $40–$154 band is 2017 pricing from one trade article.
3. **"Both sit inside LifeBio's 2017 band of $2,000–$10,000 per community."** True for 2017. Against 2026 list, $6,480 for 60 residents is 3.6 times what LifeBio charges for a census of 100–199 [estimated: 6,480 ÷ 1,788].
4. **Hospice bereavement pool "$334M, about $257 per hospice death."** Withdrawn. Now at most $283M (2023) to $311M (2024 scale), $219–$234 per decedent [institutional-legacy.md Q4]. The hospice counts are also stale: 6,706 hospices and 1.82M beneficiaries in 2024, not 6,535 and 1.7M [Q1].
5. **"About $530 per resident per year ... three to thirteen times any price found."** Withdrawn as false as written; the multiples run from 1.2 to 59 [institutional-legacy.md Q8].
6. **"The central licence line ($13.4M) sits inside the research file's own $7.5–28.3M, and the total sits inside the $5–45M cap."** Both withdrawn. The arithmetic range is about $1.7M to $85M at LifeLoop-level penetration, and what argues against the high end is behaviour, not arithmetic [institutional-legacy.md bottom line 6, Q8].
7. **"LifeBio earns about $42,000 per employee, the signature of a service ... the AI interviewer removes interviewer labour."** The repair says this ratio "cannot be read as a commercial margin signal": the numerator may include NIH grant income and the headcount may include grant-funded staff [institutional-legacy.md Q8]. The variant's explanation of why its margin beats the incumbent's has no base.
8. **LifeBio as "the base rate" at about $2M.** Understated in the wrong direction. LifeBio has 7 NIA awards totalling $5,371,563 (FY2020–26) plus $305,739 of penalty funds; identified public funding is more than 2.5 times its one reported revenue year [institutional-legacy.md bottom line 2, Q8]. The variant cites two grants as product history and never says that grants are the category's sustaining payer.
9. **"Nobody found runs the interview over the family's own photographs and stores a per-photo record."** Narrower after repair. Memory Murals already tags people and dates per photo from a spoken story at $99.99 a year (100+ downloads); GoodTimes is published prior art; Remento is moving recordings onto individual photos [memoir-gift-market.md Q4]. The gap that remains is the combination with a phone or tablet interviewer and a book.
10. **"Top four operators hold 2.7%."** Now an upper bound of 2.7–3.4%, because the numerator includes independent living and CCRCs [institutional-legacy.md Q1]. Direction holds.
11. **"LifeLoop serves 4,700+ communities."** A vendor self-claim, unchanged across 2026 releases and not reconcilable with its parts [institutional-legacy.md Q2]. The 8.4% "precedent" penetration inherits that weakness.

Claims the research does not cover at all (variant's own fetches or pointers to another variant; not contradicted, not confirmed): FCC 24-17 on AI voices (cited only via variants/v3-gift.md); HIPAA covered-entity and personal-representative text; state recording-consent counts; the 25-month and 18-month stays and the 488,000 move-ins; the "six staff hours per resident" figure (2017, a vendor founder's statement); LifeLoop Life Story's 2025-11-03 launch date and Olia; Porchlight, StoriedLife, ElderVoice; referral-agency fees. No research file contains a finding on TCPA, call-recording consent, BAA availability for voice APIs, or speech-recognition accuracy on impaired speech.

Numbers that check: all Economics and Ceiling arithmetic reproduces (5,595 minutes; $1,260 COGS; 81% and 71% margins; $1.17 CAC per $1; 19 months; $13.4M, $2.9M, $0.7M; 41% for $100M). Voice, print and storage inputs match memoir-gift-market.md Q5, family-artifact-market.md Q3 and unit-economics.md Q1. The research recommends a 30% allowance for retries and abandoned calls [memoir-gift-market.md Q5]; the variant leaves it out, which moves central voice cost from $358 to about $465 [estimated: 358 × 1.3].

## The 4-week demo spec, line by line

| Spec line | Verdict | Why |
|---|---|---|
| W1 roster entry, CSV import | Build | Nothing gated. |
| W1 family link, system-picker upload | Build | Nothing gated. The first text to the family contact needs sender registration and consent wording; not researched. For ten families, send by email. |
| W1 browser print capture, front then back | Build | Glare and skew are ordinary work. |
| W1 authorization and assent capture | Policy-gated | The code is a form. The content is a HIPAA authorization plus a state-law question of who signs for a resident with dementia, and a pilot site's counsel must accept it. The variant's own assumption 8 says this is untested. |
| W1 photo description and handwriting OCR | Build, with a gate | Photos tied to a resident are health information once the summary enters the care record, so the vision vendor needs a BAA too. Not researched. |
| W2 real-time voice over WebRTC, photo on screen | Build with a healthy speaker; research problem with the target user | Whether any real-time voice API signs a BAA is [unknown] in the variant and absent from research. Accuracy on hearing loss, slow or dysarthric speech and dementia: no evidence found. Turn-taking with long pauses and a television in the room is tuning nobody has measured. |
| W2 phone path for relatives | Build, policy-gated | Outbound AI calls need prior express consent; recording needs all-party consent in some states. Designable; no research file covers it. |
| W2 "stop-word handling" | Research problem as specified | Detecting that a person with dementia is distressed or wants to stop is not keyword matching. The safe design is that the human in the room stops the session, which makes the human mandatory. |
| W2 tablet in the resident's room | Not costed | Whose tablet, who charges it, who carries it to the room. No hardware line in COGS. |
| W3 per-photo records, confidence, "resident's account" flag | Build | Entity matching across sessions ("Bill", "Dad", "William") is moderate work. |
| W3 relative review screen | Build | The acceptance test "zero unconfirmed resident statements" depends on relatives reviewing quickly. The prior for unprompted naming is 0.10 tags per scan [digitization-market.md Q6]. |
| W3 one page, starters, 60-second briefing | Build | This half is what a solo founder shipped in 2026 and what LifeBio generates overnight, by the variant's own account. |
| W3 export "into the care system's document store" | Platform-gated beyond a manual upload | PointClickCare requires the partner programme, technical validation, per-facility approval and an annual minimum; MatrixCare already lists LifeLoop [institutional-legacy.md Q5]. In the demo this is a download button. |
| W4 booklet PDF | Build | Print cost matches the Blurb list price. |
| W4 archive page, XMP export, MCP endpoint | Cut | The MCP endpoint proves nothing about the loop. |
| W4 supervised run, 10 residents, one community | Policy-gated | Needs a licensed community, its counsel, a BAA, and representative signatures inside week 4. The one vendor-side account puts first contact to pilot at 6–8 months [institutional-legacy.md Q5, single anecdote]. A friendly independent site could be faster; the variant names none. |
| Acceptance: 12 records per resident by day 30; aide recall check | Cannot be met in 4 weeks | A run that starts in week 4 reports day-30 results in week 8. As written this is an 8–9 week plan. |

**Smallest thing that proves the core loop:** family link, 10–20 photos, two family voice sessions, the "by Friday" page. Two engineers, two weeks, no resident recording, no tablet, no in-room consent. That demo is credible. It also proves the half that LifeLoop, LifeBio and a free solo entrant already have. The half that is new (the resident answering about photos) is the half with no evidence.

## What breaks at scale

The variant's central case is about 124,000 residents, roughly 3,000 communities [estimated: 124,103 ÷ about 40 per site]. Ten thousand communities would be $47M at the variant's prices and is above its own ceiling, so I use 3,000.

- **Staff presence is the real cost, and it lands on the customer.** Every resident session needs "a person present". At 36 enrolled residents that is about 85 hours a year per site if staff are that person [estimated: (36 × 120 + 17 × 45) ÷ 60]. Today's baseline is an intake form, not six hours per resident. The product adds staff time in a workforce turning over at 34–72% a year [institutional-legacy.md Q5].
- **Site onboarding does not amortise.** Ten hours a year per site is assumed. At 3,000 sites that is 30,000 hours, about 15 people, before any family support [estimated: 3,000 × 10 ÷ 2,000]. The variant's own margin falsifier is 20 hours.
- **Family support is not in COGS.** 36 residents × 2–7 relatives is 72–250 family accounts per site, 216,000–750,000 at 3,000 sites [estimated]. Upload, consent, audio and "my sister changed Dad's story" tickets go to the vendor, not the community.
- **Custody of irreplaceable recordings, free, forever.** "Stays readable at no charge" after discharge or death is a perpetual duty with no revenue behind it for the 94–99% of families who do not upgrade. HereAfter AI is the cautionary case: site offline, recordings by email request only [memoir-gift-market.md Q3].
- **Dual role under HIPAA.** The company holds the record as the community's business associate and then sells the family a $59 upgrade from it. Whether that marketing use is allowed without a separate authorization, and who controls the archive when relatives disagree, is not addressed. No research covers it.
- **Voice recordings as biometric data.** The privacy section tests faces only. Washington's My Health My Data Act lists "voice recordings" from which a template can be extracted as biometric data and as consumer health data, with a private right of action through the consumer protection act [face-regulation.md Q3]. Washington is also one of the all-party recording states the variant names. Stored voice clips are the product.
- **Confabulation in the care record.** The mitigation is relative confirmation, which is the step least likely to be completed. The variant says this itself.
- **Print and voice do not break.** About 59,600 booklets and roughly 17M voice minutes a year at the central case cost about $0.7M and $1.1M [estimated: 59,600 × $12; 5,595 × 3,000 × $0.064]. These are the lines the variant models best and they matter least.

## Most damaging objection

**At the prices operators are shown to pay today, the product's own cost of serving a site is about equal to the revenue from that site.**

The variant prices a 60-resident community at $6,480 a year and models $1,260 of COGS, of which $600 is site onboarding that does not shrink with AI. Its comparables for that price are 2017 figures and a range the research has withdrawn. The two current list prices in the repaired research are LifeBio at $149 a month for a census of 100–199 [institutional-legacy.md bottom line 5] and Famileo Pro US from $99 a month for up to 50 beds [family-artifact-market.md Q2]. That is $1,188–$1,788 a year per community. Against the variant's own $1,260 COGS, gross margin is −6% to +30% [estimated: (1,188 − 1,260) ÷ 1,188; (1,788 − 1,260) ÷ 1,788]. One seller's 45 sites become $53,000–$80,000 of new revenue for $250,000 of selling cost, $3.1–$4.7 of CAC per dollar of revenue, with no payback at that margin [estimated: 45 × 1,188; 45 × 1,788; 250,000 ÷ each]. The central licence ceiling falls from $13.4M to $1.1–$2.2M [estimated: 124,103 × $8.98; × $17.88].

The prices above that level in the research were paid by someone else (penalty funds at $9,186–$10,366 per home) or abandoned by the vendor (MemoryWell's $450 per story). LifeLoop bundles the staff-facing half into a contract the operator already has, and a free entrant exists. A four-week demo proves the loop runs. It does not touch the question that decides the business: whether any operator pays five times the going rate, from its own budget, for the half of the product that is new. Twenty operator conversations answer that before any code, and the variant lists them as assumption 1 without having held one.

## Weakest dimension

**Ceiling (2).** The variant concedes $100M does not pencil and plans on $2–5M in year five. After the repair the picture is worse than the variant states: its $17M central rests on a price 6–12 times current list, its two "sits inside the research range" sentences cite withdrawn claims, and the largest dedicated vendor's roughly $2M may be substantially grant income. Distribution (3) is next: no channel is shown to produce communities.

## Strongest dimension

**Buildability (5), tied with Why now (5).** This is the first variant in three rounds with no Apple or Google gate, no library migration, no face embeddings and no on-device inference. The voice stack is priced from vendor pages at $6–$22 per person-year for mid-priced configurations [memoir-gift-market.md Q5], and the family-only loop is a two-week build that shows a real artifact to a real director. It stays at 5 because the differentiating half, an AI interviewing residents with dementia in their rooms, has no accuracy evidence, needs BAAs nobody has verified, and can only be tested inside a licensed building with counsel's consent.

## Unknowns research could resolve before the next round

1. Which real-time voice APIs (OpenAI GPT-Live and Realtime, Gemini Live on Vertex, ElevenLabs Agents, Deepgram Voice Agent, Vapi, Retell) and which telephony and recording products (Twilio Voice) are covered by a HIPAA business associate agreement, at what plan tier, minimum commitment and data-retention setting?
2. What word error rates do 2025–2026 speech recognition and speech-to-speech models report on older adults with dementia, dysarthria or hearing loss (DementiaBank Pitt corpus, TORGO, UASpeech, Speech Accessibility Project results)?
3. Is LifeBio's $149 / $349 "Monthly Billing" group licence charged per month or per year, and what do LifeLoop (Life Story, Olia) and TSOLife charge per community or per resident, as shown in public procurement records (state veterans' homes, county nursing homes, board minutes) or in penalty-fund (CMP) applications outside Tennessee? Do current CMP reinvestment rules still fund projects at $9,000–$10,000 per home?
4. Do stored voice recordings of residents count as biometric or consumer health data when no voiceprint is computed (Washington My Health My Data Act, Illinois BIPA "voiceprint", Texas CUBI), and may a HIPAA business associate keep a family archive after discharge and market a paid upgrade to relatives without a separate authorization (45 CFR 164.508(a)(3), 164.504(e))?
5. What share of families complete a move-in-week digital intake task within seven days at communities using LifeLoop Life Story, LifeBio or Porchlight, and how many communities does Porchlight have, with how many converted from free to paid?

## Three questions for the founder

1. Name one licensed community whose executive director and counsel will let you record ten residents in their rooms within 60 days. Who signs for the residents with dementia, and has that person seen the authorization?
2. If operators will pay only what LifeBio and Famileo Pro list today, about $1,200–$1,800 a site, is the community your customer or your distribution? If it is distribution, why charge it at all when a free entrant exists, and what is the family-side business then?
3. The path is roughly 9–11 months of selling plus a compliance programme (BAAs, security review, recording-consent counsel) before the first paid rollout. What is your runway, and who on the team has sold to senior-living operators or run a HIPAA programme before?
