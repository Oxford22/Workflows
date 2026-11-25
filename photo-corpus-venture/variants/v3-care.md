# v3-care — Legacy program for senior living and hospice (institution pays per resident)

Written 2026-11-24 for round 3. Tags: `[sourced: url or research file §, date]`, `[sourced-secondary: …]`, `[estimated: method]`, `[unknown]`. Research files are cited as `file Qn`. Pages I fetched myself on 2026-11-24 are cited by URL. Thesis line from the brief: "Every resident arrives with a life; the community should know it by Friday."

## One line

At move-in or hospice admission the family gets a link, adds the photos it chooses, and an AI interviewer talks with the family and the resident about those photos; staff get a one-page life story and conversation starters within the week, the family gets a named, narrated photo archive and a printed booklet, and the community pays per occupied unit per month. On today's evidence this is a $3–36M business, central about $17M [estimated: Ceiling table], and the research file written for it says no vendor in the category has a sourced revenue of $10M [sourced: research/institutional-legacy.md bottom line 1].

## Customer (payer, user, audience; how many [tagged]; what they do today; what they pay today)

**Payer: the operator.** The signer is an executive director or a regional VP; the champion is the life-enrichment or memory-care director.
- Assisted living: 41,465 communities, 1,016,424 residents, 33 units on average, 44% of residents with Alzheimer's or other dementia, average charge $74,400 a year [sourced: NCAL Fast Facts June 2026 via research/institutional-legacy.md Q1]. About 17,830 communities have 26 or more units [estimated: 43% × 41,465; institutional-legacy.md Q1]. 57.3% are chain-affiliated [sourced: ahcancal.org via institutional-legacy.md Q1]. The top four operators hold 2.7% of communities [estimated: institutional-legacy.md Q1], so there is no "land five logos" route.
- Nursing homes: 14,742 facilities, about 1.24M residents [sourced: KFF July 2025 via institutional-legacy.md Q1].
- Hospice: 6,535 providers, 1.7M Medicare beneficiaries in 2023 [sourced: MedPAC March 2025 via institutional-legacy.md Q1]; 1.3M people died in hospice in 2024 [sourced: Alliance for Care at Home 2025 via research/estate.md Q6]. Median length of stay is 18 days [sourced: https://www.medpac.gov/wp-content/uploads/2025/03/Mar25_Ch9_MedPAC_Report_To_Congress_SEC.pdf, March 2025, read 2026-11-24].
- Move-ins: about 488,000 a year in assisted living [estimated: 1,016,424 × 12 ÷ 25; NIC median stay 25 months, memory care 18 months, sourced-secondary: https://www.mmcginvest.com/post/u-s-assisted-living-market-outlook-2026-to-2030-industry-analysis-occupancy-costs-regulation-an, read 2026-11-24; 554,000 at the 22-month figure repeated on consumer sites].

**Users.** The resident (often cognitively impaired); two to seven relatives per resident (about 4 people connect to each Aura frame and about 7 post to each Famileo gazette [sourced and estimated: research/family-artifact-market.md Q1–Q2]); front-line aides, where turnover is 71.9% a year by one survey and 34.5% by another [sourced-secondary: McKnight's 2026-11-12 and SHN 2026-01-30 via institutional-legacy.md Q5].

**What they do today.** A paper or EHR "social history" form at intake. Federal rule requires the nursing-home assessment to cover "life history and preferences" [sourced: 42 CFR 483.20(b)(1) via institutional-legacy.md Q4]; it is met with the MDS instrument and an interview, not a narrative. LifeBio's founder put staff effort for a full life story at "about six hours per resident" [sourced: https://www.iadvanceseniorcare.com/story-of-my-life/, 2017-01-14, re-read 2026-11-24]. Hospices run legacy projects with volunteers, chaplains and social workers; these are customary, not required (see Why now 8).

**What they pay today.**
- Engagement software: $39–$650 per community per month across Rendever, USR Engage, StoriiCare, WelcomeHome; LifeLoop is quote-only [sourced and sourced-secondary: institutional-legacy.md Q2].
- Life-story programmes: LifeBio about $2,000 a year for under 50 people and $5,000–$10,000 for a large campus; Storii $2,500–$4,000 a year; MemoryWell $450 per story (all 2017) [sourced: iadvanceseniorcare.com 2017-01-14 via institutional-legacy.md Q3]. That is $40–$154 per resident per year [estimated: institutional-legacy.md Q3]. Current prices: [unknown].
- Famileo Pro in the US: from $99 per month per community of up to 50 beds [sourced: famileopro.com via family-artifact-market.md Q2].
- Technology overall: 3.8% of operating budget, about $2,830 per resident per year [sourced: Ziegler May 2025; estimated: institutional-legacy.md Q2]. Activities consumables: $9–$23 per resident per month, forum anecdotes only [sourced-secondary, weak: institutional-legacy.md Q2].
- The large per-move-in cheque goes to referral agencies: 85–100% of the first month's rent and care, up to $12,000 for dementia care [sourced: https://captimes.com/news/government/a-place-for-mom-assisted-living-referrals-draw-wisconsin-scrutiny/article_c6ff34f7-326f-4e60-802b-cb27e516d63c.html, 2025-06-17, quoting a state association]. That is a sales budget, not a programme budget; whether any of it can be redirected to a move-in programme is [unknown].
- Hospice bereavement: Medicare does not pay for it; the cost pool is about $334M a year, or about $257 per hospice death, mostly salaries [sourced and estimated: institutional-legacy.md Q4]. A funeral-home aftercare card programme sells at $25 per family [sourced: aftercare.com via estate.md Q6].

## Wedge (first use case adopted without changing habits; the first 10 minutes for the payer and for the elder/resident; day-1 value; day-30 value)

**First use case.** The move-in packet already contains a life-history form that the family half fills in. The product replaces that form with a link. No library migration, no app for the resident, no platform API: the family adds only the photos it chooses.

**The payer's first 10 minutes (life-enrichment director).**
1. Enter one new resident (name, room, move-in date, the family contact from the admission agreement) or upload the roster as a CSV.
2. The system texts and emails the family contact a link, and prints a QR card for the welcome folder.
3. The director picks who receives the one-page summary (care team, dining, activities) and prints the consent sheet for the resident's representative.

**The family's first 10 minutes.** Open the link; sign the authorization (see Product, consent); add 10–20 photos with the phone's system picker or photograph prints front and back in the browser; answer three spoken questions about the first photo; forward the link to siblings [estimated: design choices; no completion data exists].

**The resident's first 10 minutes.** Day two or three after move-in, in the resident's own room, with an aide or relative present: a tablet shows one family photo and the interviewer asks who is in it. The interviewer says it is an AI, asks for agreement each session, and stops when asked [estimated: design choice; day two or three is chosen to avoid move-in day itself].

**Day-1 value (for the payer).** The "by Friday" page is built from the family's inputs alone, before the resident says anything: preferred name, people who matter, work, places, five conversation starters, three things to avoid [estimated: design choice]. It prints on one sheet for the room and the care binder.

**Day-30 value.** 15–30 photos with names, dates, places and a voice clip [estimated: assumption of 2–3 photos per 10–15-minute session over 6–10 sessions; no measurement exists]; a shift briefing for new aides; a family feed; a print-ready 40-page booklet; input for the first care conference.

**Honest limits on "no habit change".**
- Staff must open the page. The one life-story programme studied in care homes lost two of six homes after management turnover [sourced-secondary: NIHR study accounts via institutional-legacy.md Q8].
- A solo founder in this exact category reports that activity directors' first questions were "what does it cost, and who has time to set it up" [sourced: https://www.geekwire.com/2026/startup-spotlight-porchlight-uses-ai-to-help-foster-human-connection-in-senior-care/, 2026-10-01].
- How people over 70, and people with dementia, respond to an AI interviewer is [unknown] at product scale; the studies found have 41, 11 and 20 participants [sourced-secondary: research/memoir-gift-market.md Q5].
- In hospice the median stay is 18 days [sourced: MedPAC, above], so the resident-interview loop does not fit. There the family is the interviewee and the output is a bereavement keepsake.

## Why now (dated changes since 2024, each tagged)

1. **Voice interviewing costs cents.** List prices on 2026-11-24: $0.023 per minute (Gemini 3.8 Live, both directions), $0.05 per active minute (OpenAI GPT-Live), $0.096–$0.143 all-in on Vapi, plus $0.014 per minute outbound telephony [sourced: vendor price pages via memoir-gift-market.md Q5]. The six staff hours per resident are the cost this removes.
2. **2025-05-08: TSOLife raised a $43M Series B ($52M in total)** for a platform that turns recorded resident interviews into profiles; named customers include Brookdale, Benchmark and Sagora; the CEO claims it extends length of stay "by more than six weeks" [sourced: https://www.mcknightsseniorliving.com/news/tsolife-secures-43-million-in-series-b-funding-to-further-growth-ai-tools-in-senior-living/, 2025-05-08]. Its model was trained on 100,000 hours of on-site audio [sourced: https://seniorhousingnews.com/2025/05/07/tsolife-raises-40m-in-series-b-funding-to-fuel-growth-ai-evolution/, 2025-05-07]. It reports data on over 125,000 residents in three years [sourced-secondary: search extract of the funding release, 2025-05-07]. The length-of-stay claim is the company's own; no independent check was found.
3. **2025-11-03: LifeLoop launched Life Story**, "a new resident onboarding tool", paired with "AI-enhanced Resident Onboarding" [sourced: https://www.prnewswire.com/news-releases/powering-a-new-era-of-agingwhere-proactive-engagement-and-whole-person-wellness-end-social-isolation-and-loneliness-302601174.html, 2025-11-03]. **2026-11-17: LifeLoop made its AI layer Olia generally available** [sourced: https://www.prnewswire.com/news-releases/lifeloop-launches-olia-the-ai-companion-for-senior-living-that-moves-teams-from-insight-to-action-302941013.html, 2026-11-17]. LifeLoop serves 4,700+ communities [sourced: PR Newswire 2026-10-06 via institutional-legacy.md Q2]. This validates the moment (onboarding) and makes the staff-facing half a bundled feature.
4. **2026: free and near-free entrants.** Porchlight, founded 2026 by one person, is "free while communities try it" [sourced: GeekWire 2026-10-01, above]. StoriedLife sells "Life-Story Programs for Senior Living" with "co-branding & bulk plans" [sourced: https://storiedlife.ai/partners/senior-living/, read 2026-11-24]. ElderVoice sells AI wellness calls to facilities and advertises EHR integrations [sourced: https://www.eldervoice.com/landing/care-facilities, read 2026-11-24].
5. **LifeBio already generates the staff page with AI.** "With a single conversation, LifeBio automatically generates a … digital care file overnight — powered by AI"; families "order a Life Story Book"; "used in hundreds" of organisations [sourced: https://www.lifebio.org/health-care-senior-living/, read 2026-11-24]. The app came from a $2.49M NIA grant [sourced: https://www.prnewswire.com/news-releases/new-app-uses-artificial-intelligence-ai-voice-and-visual-prompts-coupled-with-reminiscence-therapy-to-enhance-quality-care-and-quality-of-life-for-older-adults-301406998.html, 2021-10-25]; a further $2.9M NIA grant funds a trial with 84 caregiver pairs [sourced: https://www.gmu.edu/news/2025-10/nih-grant-george-mason-researcher-refines-ai-storytelling-tool-dementia-care, 2025-10].
6. **2024-02-08: the FCC ruled AI voices are "artificial or prerecorded voice" under the TCPA**, so outbound AI calls need prior express consent [sourced: FCC 24-17 via variants/v3-gift.md Why now 2]. The rule is now designable.
7. **Staff churn makes staff-run programmes unsustainable**: 71.9% turnover and 39% of new hires gone within 90 days [sourced-secondary: McKnight's 2026-11-12 via institutional-legacy.md Q5].
8. **Regulatory drivers, real versus customary.** Real: "life history" in the nursing-home assessment (42 CFR 483.20(b)(1)); activities based on the assessment (483.24(c)); a hospice bereavement programme for "up to 1 year" (418.64(d)) [sourced: institutional-legacy.md Q4]. Customary only: a narrative, photos, a book, a legacy project, the "13 months" bereavement figure, and any third-party tool. Memory care has no national rule; a 50-state count is [unknown] [institutional-legacy.md Q4]. CMS's GUIDE dementia model (2024-07-01) requires person-centred care plans but covers community-dwelling beneficiaries, not long-term nursing-home residents or hospice patients [sourced-secondary: search extract of cms.gov GUIDE pages, 2026-11-24]. No payer reimburses this [institutional-legacy.md Q8].
9. **Counter-signals.** MemoryWell's site is a redirect stub; Storii became an EHR; HereAfter AI went offline in 2026 [sourced: institutional-legacy.md Q3; memoir-gift-market.md Q3]. Assisted-living occupancy has risen for twenty straight quarters [sourced-secondary: MMCG, above], which weakens "move-in differentiation" as an urgent purchase. The evidence base is thin: reminiscence shows a small quality-of-life effect in care homes (SMD 0.46, 3 studies, 193 people) and none overall [sourced: Cochrane 2018 via institutional-legacy.md Q4].

## Product (core loop; explicitly NOT in v1)

**Core loop.**
1. **Enrol.** Roster entry or CSV. The resident, or the resident's representative, signs an authorization that names what is recorded, who sees the summary and who owns the archive.
2. **Collect.** Relatives add up to 300 chosen photos by link (system picker; print capture, front then back) [estimated: design choice, same cap as variants/v3-gift.md; about 1 GB]. A vision model describes each photo, locates people with detection boxes only and reads handwriting on backs. No face embeddings.
3. **Interview.** The family by phone or browser (two sessions of about 15 minutes). The resident on a community tablet (three sessions in the first two weeks, then about 10 minutes a month), one photo at a time, with a person present [estimated: design choice; these session counts drive the 75 and 120 minutes in Economics].
4. **Structure.** Each answer becomes a per-photo record: names as spoken, relationship, date range with a confidence, place, story text, audio clip. Unverified resident statements are marked "resident's account" and never written into the care record as fact until a relative confirms.
5. **Deliver to staff.** One page and five conversation starters; a 60-second audio briefing for a new aide [estimated: design choice]; export as PDF and CSV into the care system's document store.
6. **Deliver to family.** The archive page, a 40-page booklet (print-ready PDF; one printed copy per enrolled resident) [estimated: design choice; costed in Economics], and export with XMP names and dates.
7. **Hospice variant.** Family interviews in the first days; the keepsake booklet is produced by the bereavement team's 30-day contact [estimated: design choice] and is part of the bereavement plan that runs "up to 1 year" [sourced: 42 CFR 418.64(d) via institutional-legacy.md Q4].
8. **After discharge or death.** The archive belongs to the family and stays readable at no charge. The community's copy of the summary is deleted on its retention schedule. The family may pay to keep adding to it.

**Consent, capacity and privacy design (decided before any code).**
- **HIPAA.** A covered entity is a provider "who transmits any health information in electronic form in connection with a transaction covered by this subchapter" [sourced: https://www.law.cornell.edu/cfr/text/45/160.103, read 2026-11-24]. Medicare-certified hospices and nursing facilities meet that test [estimated: inference; they bill Medicare electronically]. A vendor that "creates, receives, maintains, or transmits protected health information" on their behalf is a business associate [sourced: same]. A private-pay assisted-living community that files no electronic claims may not be a covered entity [sourced-secondary: vendor guide via search extract, 2026-11-24], but chains ask for a business associate agreement regardless; a competitor states "We review Business Associate Agreements case by case" [sourced: eldervoice.com, above]. Consequence: sign BAAs, and use only voice, transcription and hosting vendors that sign one. Which real-time voice APIs offer a BAA is [unknown: not verified this session].
- **Who consents for a resident with dementia.** 44% of assisted-living residents have dementia [sourced: NCAL, above]. Under HIPAA, a person with authority under state law to make health-care decisions for an adult is treated as the personal representative [sourced: https://www.law.cornell.edu/cfr/text/45/164.502, §164.502(g)(2), read 2026-11-24]. In nursing homes a designated resident representative exercises delegated rights, and a court-appointed representative does so for a resident adjudged incompetent [sourced: https://www.law.cornell.edu/cfr/text/42/483.10, §483.10(b)(3) and (b)(7), read 2026-11-24]. Design: written authorization from the resident if able, otherwise from the representative; spoken assent from the resident at the start of every session; the session ends on refusal or distress; residents flagged with moderate or severe impairment are interviewed only with a relative or staff member present, and the family is the primary source.
- **Recording.** Some states require every party's consent; California, Pennsylvania and Washington are named in every list read, and counts run from 9 to 12 depending on how hybrid states are counted [sourced-secondary: search extracts, 2026-11-24]. For interstate calls "the strictest standard generally applies" [sourced: https://ktslaw.com/en/blog/globalprivacy-and-cybersecuritylaw/2024/7/wiretap-laws-in-the-united-states, 2024-07]. Design: announce and record consent on every call and session in every state. Residents have a right to privacy in "oral (that is, spoken)" communications [sourced: 42 CFR 483.10(h), above], so sessions run in a private room, not in common areas, and never capture a roommate.
- **Faces.** Names come from people speaking. No face template is created, so the BIPA questions in research/face-regulation.md Q7 and research/unknowns-r1.md Q8 do not arise for v1 [estimated: inference from the statute's "scan of face geometry"; no case on spoken names attached to photo regions was found].

**Explicitly NOT in v1.** Whole-library import or dedupe; face recognition; voice cloning or avatars; unsupervised calls to a resident's room phone; any clinical or outcome claim; billing families through the community's invoice; EHR write-back beyond a document upload; home care, health plans, the UK and France.

## Business model and pricing (with comparables, tagged)

| Item | Price | Comparable |
|---|---|---|
| Community licence | $9 per occupied unit per month ($108 a year), minimum $250 per community per month [estimated: design choice] | $40–$154 per resident per year for life story in 2017 [estimated: institutional-legacy.md Q3]; StoriiCare $10 per client per month plus $450 per location [sourced-secondary: institutional-legacy.md Q2]; engagement tools $39–$650 per community per month [institutional-legacy.md Q2]; Famileo Pro US from $99 per month up to 50 beds [sourced: family-artifact-market.md Q2] |
| Per-admission alternative | $149 per move-in, 12 months included [estimated: design choice] | MemoryWell $450 per story in 2017, then left the market [sourced: institutional-legacy.md Q3]; LifeBio consumer app $149, app plus book $299 [sourced: shop.lifebio.com via institutional-legacy.md Q3] |
| Hospice | $40 per enrolled family [estimated: design choice] | $257 bereavement cost per death, mostly salary [estimated: institutional-legacy.md Q4]; aftercare cards $25 per family [sourced: estate.md Q6]; StoryCorps Legacy and one visiting-nurse programme are free to patients [sourced and sourced-secondary: institutional-legacy.md Q3; search extract of vermontvisitingnurses.org, 2026-11-24] |
| Family "keep and extend" | $59 a year; hardcover $69 [sourced: variants/v3-gift.md pricing table, same product line] | Storyworth renewal $99; Remento $99 a year; Skylight Frame Plus $39 a year [sourced: memoir-gift-market.md Q1–Q2; family-artifact-market.md Q1] |

- A 60-resident community pays $6,480 a year [estimated: 60 × $108]. The average assisted-living community has about 25 residents [estimated: 1,016,424 ÷ 41,465] and would pay the $3,000 minimum [estimated: 12 × $250]. Both sit inside LifeBio's 2017 band of $2,000–$10,000 per community.
- If operators insist on paying per enrolled resident instead of per occupied unit, revenue falls by the non-enrolled share. Enrolment rate is [unknown]; 60% is used as an assumption below.
- The family line is small by design. No US example was found of a community billing families for a legacy programme, and ancillary fees are litigated ($16M settlement) [unknown and sourced: institutional-legacy.md Q6]. In France the establishment pays and families use Famileo free [sourced-secondary: institutional-legacy.md Q6].

## Distribution (non-paid channels with evidence; one paid channel with CAC math if any)

**Non-paid.**
1. **The family link is the referral.** Each enrolment puts the product in front of several adult children, each with other parents and in-laws. This feeds the consumer gift line (v3-gift), not more communities. Conversion is [unknown].
2. **Trade press covers this category for free.** McKnight's, Senior Housing News and GeekWire ran the TSOLife, LifeLoop and Porchlight stories cited above. Coverage is evidence of editorial appetite, not of sales.
3. **Senior move managers and photo organizers are present in move-in week.** NASMM has "over 1,000 members" and tells families to "Ask your Move Manager about digitizing your photos" [sourced: research/pro-channel.md Q6 via variants/current.md]. They can start the family link while sorting the boxes.
4. **EHR marketplaces.** PointClickCare's marketplace requires a partner programme, technical validation, per-facility approval and an annual minimum commitment; fees are not public [sourced-secondary and unknown: institutional-legacy.md Q5]. A small vendor advertises PointClickCare, MatrixCare and Yardi integrations [sourced: eldervoice.com, above], so entry is possible. LifeLoop has no partner route found and sells its own Life Story; treat it as a competitor, not a channel.
5. **Hospice foundations and volunteers.** StoryCorps Legacy shows the non-profit partner route [sourced: institutional-legacy.md Q3]. It sets a price expectation of zero.

**One paid channel: direct sales to regional operators.**
- Cycle: 6–8 months from first contact to pilot, then a 3-month trial; one operator ran a 90-day, 10-community, three-vendor bake-off [sourced-secondary, single anecdotes: institutional-legacy.md Q5]. Incumbent rollouts are announced at 38 and 53 communities per operator [sourced: institutional-legacy.md Q5].
- CAC, on assumptions: one seller plus travel costs $250,000 a year [estimated: assumption] and closes 3 operators averaging 15 communities [estimated: assumption; well below the incumbent's 38–53]. New revenue = 45 × $4,740 = $213,000 [estimated: $4,740 is the midpoint of $3,000 and $6,480]. CAC = $1.17 per $1 of annual revenue [estimated: 250,000 ÷ 213,000]. Payback at 75% gross margin is about 19 months [estimated: 1.17 ÷ 0.75 × 12]. Every input except the cycle length is an assumption; logo retention is [unknown], and the only study found lost two of six homes.

## Economics (per-customer COGS including print, postage and voice minutes where relevant; GM; payback; cite research rows or derive with tags)

**Per community per year, steady state: 60 residents, 36 enrolled (60% [assumption]), 17 new enrolments a year [estimated: 60 × 48% turnover × 60%; turnover = 12 ÷ 25 months]. Revenue $6,480.**

| Cost line | Central | Range | Tag |
|---|---|---|---|
| Voice minutes: 17 × 75 min onboarding + 36 × 120 min a year = 5,595 min | $358 | $129–$800 | [estimated: × $0.064 (OpenAI $0.05 + Twilio $0.014), × $0.023 (Gemini), × $0.143 (Vapi high); memoir-gift-market.md Q5; tablet sessions need no telephony, so central is slightly high] |
| Vision, transcription clean-up, drafting | $72 | — | [estimated: assumption of $2 per enrolled resident a year] |
| Storage, about 1 GB per enrolled resident | $6 | — | [estimated: 36 × $0.18; research/unit-economics.md Q1] |
| Printed booklet, 40 pages, one per new enrolment | $204 | — | [estimated: 17 × ($7.00 + 20 × $0.20 + $1 freight); Blurb magazine list price via family-artifact-market.md Q3; freight is an assumption for a monthly box to the community] |
| Customer success and re-training | $600 | $300–$1,200 | [estimated: assumption of 10 hours at $60; driven by 71.9% staff turnover] |
| Payment and invoicing | $20 | — | [estimated: assumption; ACH] |
| **Total** | **$1,260** | $731–$2,302 | [estimated: sum] |

- **Gross margin: 81% central, 64–89% across the range** [estimated: (6,480 − 1,260) ÷ 6,480; (6,480 − 2,302) ÷ 6,480; (6,480 − 731) ÷ 6,480]. First year is lower, about 76%, because all 36 residents are onboarded at once [estimated: + 19 × 75 × $0.064 + 19 × $12 = $319].
- **Small communities are worse.** At 25 residents and the $3,000 minimum, COGS is about $870 and margin about 71% [estimated: 2,325 min × $0.064 = $149; $30 models; 7 × $12 booklets; $600 success; $7 other]. Customer success is fixed per site, and 57% of communities have 25 or fewer units [sourced: NCAL size mix via institutional-legacy.md Q1].
- **Not in COGS but real:** security and HIPAA audit costs, and any marketplace minimum [unknown: institutional-legacy.md Q5].
- **Hospice ($40 per family):** two 15-minute family calls $1.92, models $1, booklet $12, card fees and support $3 → about $18, margin about 55% [estimated: 30 × $0.064; assumptions for the rest].
- **Family upgrade:** renewal margin 71–87% and first hardcover roughly break-even at list print prices [estimated: v3-gift.md Economics; Blurb 8×10 hardcover list $41 for the base book, https://www.blurb.com/pricing, read 2026-11-24].
- **Why the incumbent's margin is poor and this one is not.** LifeBio earns about $42,000 per employee [estimated: institutional-legacy.md Q8], the signature of a service. The AI interviewer removes interviewer labour. It does not remove site onboarding, which is the line that grows with staff turnover.
- **Payback:** about 19 months on the sales assumptions above [estimated: Distribution, CAC arithmetic]. Storage of whole libraries: none.

## Platform and incumbent risk (the obvious feature Apple/Google or the category leader could ship; why this survives or doesn't)

- **Apple and Google are not the risk.** Neither sells to operators, interviews a resident or prints a care summary. This is the one variant in three rounds where a WWDC slide is irrelevant.
- **LifeLoop is the risk, and it has shipped half of this.** Life Story (2025-11-03), an AI layer (2026-11-17), a family app with photo sharing and mailed photo postcards [sourced-secondary: family-artifact-market.md Q5], and 4,700+ communities. Adding "family uploads photos, AI asks about them" is a release, sold at zero marginal price inside an existing contract.
- **TSOLife** owns "interview becomes resident profile" at the largest operators with $52M raised [sourced: McKnight's 2025-05-08, above]. Its buyer story is length of stay and operations, which is a budget; ours is legacy and family, which mostly is not.
- **LifeBio** already ships the AI-generated staff page, an action plan and a family book order, with federal research funding, and is still at about $2M [sourced-secondary: institutional-legacy.md Q3]. That is the base rate for this exact product.
- **Free entrants** (Porchlight) and memoir brands with bulk plans (StoriedLife; Storyworth and Remento could follow) set the price floor near zero for the resident-facing half.
- **Why it might survive.** (a) Nobody found runs the interview over the family's own photographs and stores a per-photo record of who, when, where and the story [sourced: memoir-gift-market.md Q4]. (b) The family owns the archive and keeps it after discharge, which an operator's engagement vendor has no reason to build. (c) The printed booklet is a visible artifact at a care conference and a funeral. None of these is a technical barrier, and none answers the budget problem. The honest statement: this survives as a family product that communities distribute, not as a line item operators defend.
- **Channel dependence.** If the product reaches the care record through an EHR marketplace, the EHR vendor sets terms and can list a rival.

## Compounding asset

- **Per resident and family:** named, dated, narrated photo records and voice clips. They cannot be rebuilt after the resident's memory fails or after death. This is the only strong asset, and it belongs to the family.
- **Timing against the stay.** The median assisted-living stay is 25 months and memory care 18 [sourced-secondary: MMCG, above]. The community's use of the record ends at discharge; the family's begins there. Retention therefore has to be earned on the family side, where paid attach is [unknown] and analogues run 1.2–6% (Ceiling).
- **Per community:** the habit of a one-page briefing and the document-store integration. Switching cost is low because the output is a PDF.
- **Company level:** a playbook of which photo prompts work at each stage of impairment. Training models on resident recordings is ruled out; LifeLoop states that resident data is not used to train its AI [sourced-secondary: search extract of the Olia release, 2026-11-17], and that sets the norm.
- **Honest:** the summary engine is a commodity that one person built in 2026 [sourced: GeekWire 2026-10-01, above]. What compounds is the family archive, which is the consumer asset of v3-gift reached through a different door.

## Buildability (4-week demo spec for 2 engineers; ugliest technical risk; what is platform- or policy-gated)

**Demo.**
- Week 1: roster entry and CSV import; family link with system-picker upload and browser print capture (front, then back); authorization and assent capture; per-photo description and handwriting OCR.
- Week 2: the interviewer. Browser and tablet over WebRTC to a real-time voice model with the photo on screen; phone path for relatives; consent script; two-channel recording; stop-word handling.
- Week 3: structuring into per-photo records with confidence and "resident's account" flags; relative review screen; the one-page summary, conversation starters and 60-second aide briefing; PDF and CSV export.
- Week 4: booklet PDF; family archive page with XMP export and an MCP endpoint [sourced: research/byo-ai.md §3 A6, Claude Free custom connector]; a supervised run with 10 residents and their families in one community.
- Acceptance: summary delivered within 4 days of the family link for at least 8 of 10 residents; at least 12 photo records per resident by day 30; zero unconfirmed resident statements in the staff page; aides in a blind check recall 3 facts per resident [estimated: thresholds are design choices].

**Ugliest technical risk.** Interviewing people with hearing loss, slow or dysarthric speech and dementia. Speech-recognition accuracy on these voices is [unknown]. Confabulated answers can enter a care record as fact. A model that invents a life detail in a summary read by 20 aides is a safety and trust failure. Mitigation is procedural (relative confirmation, flags), which costs family effort and may cut completion.

**Second risk.** The sales cycle (9–11 months to a paid rollout [estimated: 6–8 + 3 months; institutional-legacy.md Q5]) is longer than a seed company's feedback loop needs.

**Policy- or platform-gated.** BAAs from voice and hosting vendors [unknown]; operator legal review of recording in resident rooms; all-party recording states; TCPA consent for outbound AI calls; EHR marketplace validation and fees [unknown]; any outcome claim needs a study. Nothing is gated by Apple or Google.

## Ceiling (path to $100M ARR with tagged inputs and arithmetic; or the honest number it tops out at)

**Pool.** 2,256,424 residents in assisted living and nursing homes [estimated: 1,016,424 + 1,240,000; institutional-legacy.md Q8]. 1.3M hospice deaths a year [sourced: estate.md Q6].

**Reachable share, by precedent rather than hope.**
- 2%: a funded start-up at year five, below TSOLife's count [estimated: assumption; no precedent data for a seed-stage entrant].
- 5.5%: TSOLife's 125,000 residents in three years [estimated: 125,000 ÷ 2,256,424; the count is cumulative and sourced-secondary, so the concurrent share is lower].
- 8.4%: LifeLoop's 4,700 communities after three decades and a private-equity roll-up [estimated: institutional-legacy.md Q8; overstated because the count includes Canada and independent living].

**Price.** $40 (LifeBio 2017 floor), $108 (this variant's list), $150 (top of the 2017 band) per resident per year [estimated and sourced: institutional-legacy.md Q3].

| Line | Low | Central | High | Method |
|---|---|---|---|---|
| Community licences | $1.8M | $13.4M | $28.3M | [estimated: 2,256,424 × 2% × $40; × 5.5% × $108; × 8.36% × $150] |
| Hospice | $0.65M | $2.9M | $6.5M | [estimated: 1.3M × 2% × $25; × 5.5% × $40; × 8.36% × $60] |
| Family upgrades | $0.1M | $0.7M | $1.3M | [estimated: enrolled residents × 4.3% paying × $59 plus 10% of new families × $69; central = 124,103 × 4.3% × $59 + 59,600 × 10% × $69, where 59,600 = 124,103 × 48% turnover; low uses 45,128 residents, 1.2% paying and 5% buying a book; high uses 188,637 residents and 6%; paying shares from FamilyAlbum followers 4.3%, Tinybeans about 6%, Nixplay 1.2%: research/grandparent-loop.md Q1, Q4; family-artifact-market.md Q1] |
| **Total** | **about $2.6M** | **about $17M** | **about $36M** | [estimated: column sums] |

- **Sensitivity.** Each point of resident penetration at $108 is $2.4M [estimated: 22,564 × $108]. Each $10 of price at 5.5% is $1.2M [estimated: 124,103 × $10]. Per-enrolled pricing at 60% enrolment cuts the licence line to $8.0M central [estimated: 13.4 × 0.6], and the central total to about $11.6M.
- **What $100M requires.** 925,900 residents at $108, which is 41% of every assisted-living and nursing-home resident in the US [estimated: 100,000,000 ÷ 108 ÷ 2,256,424]. Or about $530 per resident per year at LifeLoop-level penetration, three to thirteen times any price found [estimated: institutional-legacy.md Q8]. Neither is credible.
- **Largest sourced revenue of any comparable.** Dedicated life-story vendor: LifeBio, "over $2 million" with 48 employees in 2023, about two decades in [sourced-secondary: institutional-legacy.md Q3]. Adjacent family-photo business with a care-home channel: Famileo, €15.3M in 2025, of which the care-home share is about €3.1–3.7M [sourced-secondary and estimated: 20–24% × €15.3M; family-artifact-market.md Q2]. TSOLife and LifeLoop: revenue [unknown]; TSOLife's $52M raised is a funding figure, not a revenue figure. No institutional life-story vendor has a sourced $10M [institutional-legacy.md §3].
- **Does the consumer line rescue it?** The Famileo pattern says the institution is distribution and families pay outside it. That is v3-gift, whose own honest range is about $2–24M [sourced: variants/v3-gift.md One line]. Care communities as a feeder: 59,600 new enrolled families a year at the central case × 5 relatives × 2% buying a $149 gift for another elder = about $0.9M [estimated: every factor after the first is an assumption]. It helps CAC; it does not change the order of magnitude.
- **International.** England's care homes hold 354,125 residents in responding providers [sourced: DHSC Nov 2025 via institutional-legacy.md Q1], about 16% of the US pool [estimated: 354,125 ÷ 2,256,424]. France is Famileo's home market. Neither moves the total by a multiple.
- **Honest number: $3–36M, central about $17M, at a penetration that the best-funded specialist (TSOLife, $52M raised) reports only as a cumulative count; a seed-stage company should plan on $2–5M in year five** [estimated: low column total $2.6M; 2% × $108 = $4.9M]. $100M does not pencil. The central licence line ($13.4M) sits inside the research file's own $7.5–28.3M, and the total sits inside the $5–45M cap that every earlier variant hit.

## Load-bearing assumptions (numbered; each with the observable fact that would falsify it)

1. **Operators will pay $108 per unit per year for a legacy programme.** Falsified if: in 20 operator conversations fewer than 5 name a budget line, or pilots convert only when the price is cut below $40. [estimated: threshold is a design choice]
2. **A budget exists outside activities consumables** (sales and marketing, or length of stay). Falsified if: no operator will fund it from marketing, and TSOLife's "six weeks" claim stays unverified by any independent study through 2027. [estimated: threshold is a design choice]
3. **An AI can interview residents with mild to moderate impairment usefully.** Falsified if: in the 10-resident run fewer than half the sessions yield one confirmed photo record, or relatives correct more than 30% of statements. [estimated: threshold is a design choice]
4. **Families complete the link in move-in week.** Falsified if: fewer than 50% of family contacts add at least 5 photos within 7 days across the first 100 enrolments. Prior: self-serve naming runs at 0.10 tags per scan [estimated: research/digitization-market.md Q6]. Threshold: [estimated: design choice].
5. **Staff read and use the page.** Falsified if: a blind check at day 30 shows aides recall fewer than 2 facts per resident, or page opens fall below one per resident per week after month two. [estimated: threshold is a design choice]
6. **LifeLoop and TSOLife do not ship family photo interviews within 12 months.** Falsified by: a release note or press release describing family photo upload with AI-led questions. [estimated: threshold is a design choice]
7. **Voice and hosting vendors will sign BAAs at list price.** Falsified if: no real-time voice API offers a BAA, forcing a slower transcribe-then-speak pipeline or an enterprise contract minimum. [estimated: threshold is a design choice]
8. **Authorization by a representative plus session assent satisfies operator counsel in all-party-consent states.** Falsified if: two or more regional operators' counsel refuse in-room recording outright. [estimated: threshold is a design choice]
9. **Sites stay.** Falsified if: first-year community renewal is below 70%, or more than a third of pilots lapse after the champion leaves (the NIHR pattern). [estimated: threshold is a design choice]
10. **Hospices will pay per family.** Falsified if: hospices approached treat $40 as outside the bereavement budget because free volunteer programmes exist; 10 conversations settle it. [estimated: threshold is a design choice]
11. **Paid family attach reaches at least 4%.** Falsified if: fewer than 2% of enrolled families pay $59 within 60 days of discharge or death in the first 500. [estimated: threshold is a design choice]
12. **Gross margin holds above 70% at the average 25-resident community.** Falsified if: measured customer-success time exceeds 20 hours per site per year. [estimated: threshold is a design choice]
13. **The ceiling is accepted as about $17M central.** Falsified upward only by: a payer reimbursement code for life-story work, or a top-ten operator contracting portfolio-wide at list price. [estimated: Ceiling table]

## Relationship to variants/current.md (what is kept from the organizer workbench and the index-only engine; what is dropped)

**Kept.**
- The review screen where relatives answer "who is this?" is the centre of the product, as the round-2 merge notes require ("naming is a prompted, human act").
- The consent architecture: no server-side face matching, living people named only by people, deceased flag, deletion schedules.
- Print capture front and back; XMP export; the optional family vault with an MCP endpoint; index-only handling of anything the family does not choose to upload.
- The organizer workbench as back office: when a family wants the whole house of boxes and libraries done at downsizing, the job is referred to an organizer or senior move manager using the workbench, at the organizer's price. The tribute-pack module becomes the hospice keepsake.

**Dropped.**
- The Mac workbench as the product, seat pricing as the revenue, and The Photo Managers as the main channel.
- Takeout repair, Photos.sqlite reading, dedupe and face clustering in v1.
- Any claim that organizing is what is sold. The community buys a staff briefing and a family artifact; the archive is what remains.

**What this variant does not fix.** Ceiling. It moves the payer from a 7,800-person profession to 56,207 facilities [estimated: institutional-legacy.md Q8] and still lands in the same band, because the institutional price is $40–$154 per resident and the incumbents bundle the staff-facing half.

## Evidence pointers (file:section for every claim above)

- Facility, resident, hospice and operator counts; chain share; size mix: research/institutional-legacy.md Q1, §5. Hospice deaths and bereavement rule: research/estate.md Q6. Hospice median stay: MedPAC March 2025 (URL above).
- Engagement and life-story prices, technology and activities budgets: institutional-legacy.md Q2, Q3. Famileo Pro US price, Famileo revenue and B2B share: research/family-artifact-market.md Q2, Q3.
- Why LifeBio and Storii stayed small; pivots; study evidence; staff turnover: institutional-legacy.md Q3, Q5, Q8; six staff hours per resident: iadvanceseniorcare.com 2017-01-14 (URL above).
- Regulatory drivers and evidence base: institutional-legacy.md Q4. GUIDE model: search extract only.
- Sales cycles, pilots, marketplace gating: institutional-legacy.md Q5. Family as payer, ancillary-fee litigation: institutional-legacy.md Q6.
- Incumbent moves 2025–2026 (TSOLife, LifeLoop Life Story and Olia, Porchlight, StoriedLife, ElderVoice, LifeBio AI care file and NIA grants): URLs in Why now, all read 2026-11-24.
- Referral fees per move-in: Cap Times 2025-06-17 (URL above). Length of stay and occupancy trend: MMCG outlook citing NIC (secondary, URL above).
- HIPAA definitions: 45 CFR 160.103 and 164.502(g)(2). Resident representative and privacy: 42 CFR 483.10(b), (h). Recording consent: Kilpatrick Townsend 2024-07 and search extracts. AI-voice calls: FCC 24-17 via variants/v3-gift.md.
- Voice, telephony and model costs; small-study evidence on older adults and AI interviewers; the photo-record gap: research/memoir-gift-market.md Q4, Q5. Print cost: family-artifact-market.md Q3; blurb.com/pricing.
- Face-template law and why names come from people: research/face-regulation.md Q7; research/unknowns-r1.md Q8. Self-serve naming rate: research/digitization-market.md Q6.
- Paid-attach analogues: research/grandparent-loop.md Q1, Q4; family-artifact-market.md Q1 (Nixplay). Retention regimes: research/unit-economics.md Q6–Q7. Storage cost: unit-economics.md Q1.
- MCP endpoint and connector access: research/byo-ai.md §3. Organizer and move-manager channel: research/pro-channel.md Q6 via variants/current.md.
- Consumer line and its range: variants/v3-gift.md. Ceiling arithmetic baseline: institutional-legacy.md Q8; research/sizing.md worked chains.
- Not resolved: current LifeBio, TSOLife and LifeLoop prices and revenue; whether Life Story is bundled; BAA availability for real-time voice APIs; marketplace fees; enrolment and paid-attach rates; speech-recognition accuracy on impaired speech; any operator willing to fund this from marketing; a 50-state count of all-party recording and memory-care history rules.
