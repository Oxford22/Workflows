# v3-care — round 3 critique — TARGET CUSTOMER

Written 2026-11-25. Fresh context. Read: SCORECARD.md, variants/v3-care.md, variants/current.md (for what is kept), every file in research/ and research/assumptions/ (not research/audits/). Not read: CHANGELOG, other v3 variants, other critiques.

## Stance

I am the executive director of a 120-resident assisted-living and memory-care community, one of 25 run by a regional operator. I already pay for a resident-engagement platform. My life-enrichment team is three people and turns over constantly. I am judged on occupancy, family satisfaction scores and survey results. I sign software under $10,000 a year; anything larger goes to corporate. Pain, Wedge and Distribution are scored hardest.

Where the variant and the repaired research disagree, the research wins. The variant was written 2026-11-24; `research/institutional-legacy.md` and `research/family-artifact-market.md` were repaired 2026-11-25. The disagreements are listed under "Failed or superseded claims".

## What this looks like from my desk

- **Cost versus today.** At the variant's list price my building is 120 x $9 x 12 = $12,960 a year [estimated: variant pricing table]. That is over my signing limit, over the top of the variant's own 2017 LifeBio band ($10,000), and 7.2 times the only current dedicated-vendor list price for my census: LifeBio's group licence for 100-199 people at $149, labelled monthly billing, i.e. $1,788 a year [estimated: 12,960 / 1,788; institutional-legacy.md Q3, bottom line 5]. The per-admission alternative is about 58 move-ins x $149 = $8,600 a year [estimated: 120 x 48% turnover x $149], under my limit but still 4.8 times LifeBio's list and billed whether or not the family finishes.
- **What I already have.** My engagement vendor sells "Life Story" as an onboarding feature (2025-11-03) and made its AI layer generally available on 2026-11-17, eight days ago [variant Why now 3; institutional-legacy.md Q2]. Whether Life Story is bundled is [unknown] in the research, but it is in my contract's catalogue and needs no new BAA, no new login and no legal review.
- **What I give up.** Nothing is switched off. I add a vendor, a BAA, a consent sheet per resident, a new incident category (an AI recording a resident with dementia in a private room), and staff time the variant does not price: 45 minutes of supervised sessions at onboarding plus 120 minutes a year per enrolled resident, about 170 staff hours a year in my building at 60% enrolment [estimated: 72 enrolled x 2 h + 35 new x 0.75 h; session counts from variant Product 3]. The variant says the product removes "six staff hours per resident"; with a person present at every resident session it cuts that to about 2.75 hours in year one, not to zero.
- **Who I trust.** Corporate, my existing platform, and peers with survey or family-satisfaction results. The variant offers none: TSOLife's "six weeks" length-of-stay claim is the company's own, and Cochrane finds a small care-home effect in 3 studies of 193 people [institutional-legacy.md Q4].
- **If the start-up dies.** The PDF in my document store survives. The hosted family archive and the recordings do not, and the category's record is poor: MemoryWell is a redirect stub, HereAfter AI went offline in 2026, Storii pivoted to an EHR [institutional-legacy.md Q3; memoir-gift-market.md Q3]. I would be the one explaining to a daughter where her mother's recordings went.
- **Would the resident take part?** 44% of assisted-living residents have dementia [institutional-legacy.md Q1]. The studies on older adults and AI interviewers have 13, 20, 41 and 11 participants; the 13 were cognitively intact with a mean age of 65.8 [memoir-gift-market.md Q5]. Honest answer: some of my assisted-living residents, with a daughter beside them, yes. My memory-care wing: not as an interviewee. The product there is a family questionnaire.
- **Would the family take part?** In move-in week they already half-fill my paper form. The best research cross-checks are weaker than the variant's 60% enrolment and "two to seven relatives": Caremerge reports 80,000+ family members for 60,000+ residents, about 1.3 per resident [estimated: institutional-legacy.md Q2]; Famileo's care-home channel has about 55,000 families across 2,700 establishments, about 20 per home, and that count has not grown since 2021 [estimated: 55,000 / 2,700; family-artifact-market.md Q2]. Self-serve naming elsewhere runs at 0.10 tags per scan [digitization-market.md Q6].
- **Would I recommend it to a peer?** Not yet. I would let my life-enrichment director run a free pilot on one wing with families who volunteer. I would not sign, and I would not carry it to corporate without a number that moves a family-satisfaction score.

## Scores

| Dimension | Score | Evidence pointer | One-line reason |
|---|---|---|---|
| 1 Pain | 4 | research/institutional-legacy.md bottom line 1-2, 5; Q3 "What they prove"; Q8 | New residents arrive unknown at every move-in and operators do pay, but the current operator-paid list price is about $9-$18 per person per year, the largest dedicated vendor is at about $2M after 23 years, and the largest identifiable payer is NIH ($5.37M to LifeBio), not operators. |
| 2 Wedge | 4 | research/institutional-legacy.md Q5, Q8 (NIHR: 2 of 6 homes withdrew); research/memoir-gift-market.md Q5; research/digitization-market.md Q6 | Day-1 page from family inputs alone is well designed, but value needs three parties to act (family in move-in week, staff, a supervised resident), no completion data exists, and at list price the first step for a 120-resident building is a corporate procurement, not my signature. |
| 3 Why now | 5 | research/memoir-gift-market.md Q5 (voice at $0.023-$0.143 per minute, 2026 price pages); research/institutional-legacy.md Q2 (TSOLife $43M, 2025-05; LifeLoop Life Story) | Dated and real, but the same dated events are the incumbents shipping it; occupancy rising 20 straight quarters removes urgency. |
| 4 Platform risk | 3 | research/institutional-legacy.md Q2, Q8 "Free substitutes and bundling"; research/family-artifact-market.md Q5 | Apple and Google are irrelevant, which is new; the category leader already in my building has shipped Life Story, an AI layer, a family photo app and mailed photo postcards, and the variant concedes the operator will not defend this line item. |
| 5 Compounding asset | 4 | research/institutional-legacy.md Q6; research/grandparent-loop.md Q1, Q4 (4.3% follower pay); research/family-artifact-market.md Q1 (Nixplay about 1.2%) | The narrated photo record is irreplaceable once memory fails, but it belongs to the family, who do not pay; my switching cost is a PDF. |
| 6 Distribution | 3 | research/institutional-legacy.md Q1 (top four at most 2.7%-3.4%), Q5 (6-8 months to pilot plus 3-month trial; conversion unknown; marketplace fees unknown); research/family-artifact-market.md Q2 (care-home families flat at about 55,000, 2021-2026) | No non-paid channel is evidenced to reach operators; the family link feeds a consumer line, not communities; the one paid channel is direct sales on assumed inputs into a long tail. |
| 7 Economics | 5 | research/memoir-gift-market.md Q5; research/family-artifact-market.md Q3; research/institutional-legacy.md Q3 (2026 LifeBio list price) | Arithmetic checks and is fully tagged (81% GM, 19-month payback), but the revenue line assumes $108 per unit against a current sourced list price of $9-$18, customer success is 10 assumed hours per site, and my staff time is left out. |
| 8 Buildability | 6 | research/memoir-gift-market.md Q4 (GoodTimes prototype; Memory Murals ships voice tagging), Q5 (ten priced voice stacks); research/assumptions/A2.md (no migration needed here) | Family link to one-page summary is demoable in four weeks with off-the-shelf parts and no platform gate; the week-4 run with 10 residents inside a licensed community is not, because of my consent paperwork and counsel, and BAA availability for real-time voice is [unknown]. |
| 9 Ceiling | 2 | research/institutional-legacy.md bottom line 1, 6; Q8 table | Variant's own range is $3-36M and it says $100M does not pencil; at its central 5.5% penetration the current sourced price gives about $1.1M-$2.2M, and no institutional life-story vendor has a sourced $10M. |
| 10 Founder fit | 5 [unknown] | — | Not stated by the founder. |

**Total: 41** (founder fit a flagged neutral 5).

## Failed or superseded claims in the variant (research wins)

1. **Price support.** Variant: life-story programmes cost "$40-$154 per resident per year", "Current prices: [unknown]", and $108 "sits inside LifeBio's 2017 band". Repaired research: LifeBio's 2026 list licence is about $9-$18 per person per year if billed monthly; the 2017 prices come from one trade article [institutional-legacy.md bottom line 5, Q3]. The variant's list price is 6 to 12 times the only current figure. Failed.
2. **"$39-$650 per community per month" for engagement software.** Withdrawn in the research (it joined a streaming add-on to an EHR); the dominant platform's price is [unknown] [institutional-legacy.md Q2]. Failed.
3. **Hospice bereavement pool "$334M, about $257 per death".** Withdrawn; now at most $283M-$311M and $219-$234 per decedent [institutional-legacy.md Q4]. Failed. Hospice counts are also stale: 6,706 providers and 1.82M beneficiaries in 2024, not 6,535 and 1.7M.
4. **"$530 per resident is three to thirteen times any price found."** Withdrawn as false; it is 1.2 times MemoryWell's $450 and 30 to 59 times LifeBio's current list [institutional-legacy.md Q8]. Failed.
5. **"The central licence line sits inside the research file's own $7.5-28.3M, and the total sits inside the $5-45M cap."** Both withdrawn. The arithmetic range is about $1.7M-$85M at 8.4% penetration; what holds the number down is vendor behaviour, not a price ceiling [institutional-legacy.md bottom line 6, Q8]. Failed as cited; the low conclusion survives.
6. **Ceiling low case uses $40 as the floor.** The sourced floor is now $9. Low case becomes about $0.4M [estimated: 2,256,424 x 2% x $9], not $1.8M.
7. **LifeBio as "the base rate" at about $2M, and "$42,000 per employee, the signature of a service".** The $2M may include grants (up to 39% of it), "mostly self-funded" is contradicted, and the per-employee reading is downgraded [institutional-legacy.md Q3, Q8]. The base rate is worse than the variant states.
8. **Top four operators "hold 2.7%".** Restated as an upper bound of 2.7%-3.4% [institutional-legacy.md Q1]. Minor; direction holds.
9. **Not contradicted:** Famileo €15.3M for 2025 and Famileo Pro US at $99 a month per 50 beds [family-artifact-market.md Q2]; voice prices [memoir-gift-market.md Q5]; the economics arithmetic (5,595 minutes, $1,260 COGS, 81%, 19 months) recomputes correctly.
10. **Missing from the variant:** Famileo's care-home family count has been flat at about 55,000 since 2021 [family-artifact-market.md Q2], which weakens "the institution is distribution"; and NIH and penalty-fund grants are the sustaining payer for the dedicated vendors [institutional-legacy.md bottom line 2].

## Most damaging objection

At list price this is a $12,960-a-year purchase for my 120-resident building, 7.2 times the current list price of the nearest dedicated vendor ($1,788 for my census) and above my $10,000 signature, for a job that the engagement platform I already pay for lists as a feature and updated eight days ago. So it leaves my desk and becomes a 25-community corporate decision worth roughly $160,000-$320,000 a year [estimated: 25 x $6,480 to 25 x $12,960], run as a multi-month bake-off against a vendor already under contract, with no outcome evidence on occupancy, family satisfaction or survey results, while asking my three-person team for about 170 supervised hours a year. The price that makes the variant's economics work is supported only by 2017 figures from one trade article; the repaired research puts today's operator-paid price at $9-$18 per person per year, at which the 60-resident model earns about $1,080 against $1,260 of cost [estimated: 60 x $18 versus variant COGS table].

## Weakest dimension

**Ceiling (2).** The variant's own honest number is $3-36M and a seed-stage plan of $2-5M; the repaired research removes the support for its central price. From my seat the two that would actually stop the purchase are Distribution (3) and Platform risk (3): there is no route to me that does not run through corporate or my existing vendor, and my existing vendor already ships the staff-facing half.

## Strongest dimension

**Buildability (6).** This is the first variant in three rounds with no dependency on Apple or Google, no library migration and no face recognition. The family-side loop (link, chosen photos, short voice interview, one-page summary by Friday) uses parts that are priced and on sale today at $0.023-$0.143 per minute, and a 2024 prototype and one shipping app show the photo-conversation idea works with older adults who are cognitively intact [memoir-gift-market.md Q4, Q5]. The day-1 page built from family inputs alone is the one piece I could try without touching a resident.

## Unknowns to research

1. Is LifeLoop's Life Story and "AI-enhanced Resident Onboarding" included in the base subscription or sold as an add-on, and what does LifeLoop cost per community per month? (Search public procurement records for county nursing homes, state veterans' homes and housing-authority board minutes.)
2. What do operators pay TSOLife per resident or per community, and has any independent party verified its "six weeks longer length of stay" claim or linked any life-story programme to family-satisfaction or occupancy results?
3. Is LifeBio's $149 / $349 "Monthly Billing" group licence charged per month or per year, is it a live offer, and what are the other census tiers?
4. What share of family contacts activate a care-community family app or link within 30 days of move-in (LifeLoop, Caremerge, Famileo Pro), and how many relatives per resident take part?
5. Which real-time voice APIs sign a HIPAA business associate agreement at list price, and which states' assisted-living or long-term-care rules restrict electronic recording in a resident's room or require roommate and representative consent?

## Three questions for the founder

1. My platform vendor already has Life Story and an AI layer. In a 90-day, 10-community bake-off run by my regional VP, what do you show that they cannot ship in one release, and what do you charge once theirs is free?
2. Who sits with the resident? You need about 170 supervised hours a year in my building from a team of three that turns over most years. Will you supply that person, or is the real product a family-only questionnaire?
3. When a resident with dementia says something false or distressing on a recording and her daughter complains to the state, whose incident is it? Will you sign a BAA, indemnify the community, and put the recordings in escrow so families keep them if you shut down?
