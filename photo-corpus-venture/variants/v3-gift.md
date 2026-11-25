# v3-gift — Gifted photo memoir with an AI interviewer (the archive is what remains)

Written 2026-11-24 for round 3. Tags: `[sourced: url or research file §, date]`, `[sourced-secondary: …]`, `[estimated: method]`, `[unknown]`. Research files are cited as `file Qn`; pages I fetched myself on 2026-11-24 are cited by URL. `research/institutional-legacy.md` arrived after the first draft; its Q3, Q6, Q7 and Q8 were then read and the institutional lines rewritten.

## One line

An adult child buys a parent a year of short, scheduled conversations with an AI interviewer about the family's own photographs ("Who is the woman on the left? Where was this?"); the family gets a printed photo book with the parent's voice behind every page, and keeps a named, dated, narrated archive that any AI can query. The honest size of this business on today's evidence is about $2–24M a year, not $100M (see Ceiling).

## Customer (payer, user, audience; how many [tagged]; what they do today; what they pay today)

**Payer: an adult child aged ~40–60.**
- At least ~67M US adults have a living parent aged 65+ [estimated: 0.25 × 267M adults, a lower bound because the Pew question also requires a dependent child; research/sizing.md Q2, Pew 2026-08-27]. 54% of people in their 40s and 45% in their 50s are in that position [sourced: pewresearch.org short-read 2026-08-27 via sizing.md Q2].
- What they buy today for that parent: a memoir gift at $69 / $99 / $199 (Storyworth) or $99 (Remento) [sourced: storyworth.com and remento.co, 2026-11-24, via research/memoir-gift-market.md Q1–Q2]; a Wi-Fi frame at $59–499 (Frameo-class $59.48, Aura $149–499, Skylight ~$140) [sourced: auraframes.com 2026-11-24; sourced-secondary: Amazon estimator July 2026; via research/family-artifact-market.md Q1]; a printed family gazette at $9.99–13.99/month in the US (Famileo) [sourced: famileo.com en-US, 2026-11-24, via family-artifact-market.md Q2].
- Occasion spend exists: Mother's Day 2026 $38B and $284.25 per person; Father's Day 2026 $27.9B, with 34% wanting a gift that "creates a special memory" [sourced: NRF 2026-04-21 and 2026-06-10 via memoir-gift-market.md Q6].

**User: the parent, aged ~70–90.**
- 61.2M US residents are 65+ [sourced: census.gov press release 2025-06-26 via sizing.md Q1]. About 41M of them are grandparents [estimated: 0.667 × 61.2M; sizing.md Q2].
- 79% of people 65+ own a smartphone and 14% own a non-smartphone cellphone [sourced: Pew mobile fact sheet, survey Jan–Jun 2026, via family-artifact-market.md Q5]. The 75+ split for 2026 is [unknown]; the last figure found is 43% for 2021 [sourced-secondary: unverified search summary, family-artifact-market.md Q5].
- The clock: 1,683,192 US deaths at age 75+ in 2023 [estimated: 798,188 + 885,004; CDC data brief 521 via sizing.md Q2]. Each is a person who could have named the faces.
- What the user does today: nothing with the photos. When naming is left to self-serve, Photomyne's users tag 0.10 times per scan [estimated: 3.3M taggings ÷ 32.7M scans, Photomyne H1 2026 report via research/digitization-market.md Q6].

**Audience: the extended family.** About 4 people connect to each Aura frame [sourced: TechCrunch 2022-11-22 via family-artifact-market.md Q1] and about 7 relatives post to each Famileo gazette [estimated: ~2M users ÷ 280,000 families; famileo.com and Bretagne Économique 2025-12-12 via family-artifact-market.md Q2].

**Who else serves this customer.** Storyworth: 1,000,000+ books printed and 40M stories in 13 years; revenue undisclosed, ~$13.5–45M a year [sourced: storyworth.com 2026-11-24; estimated: memoir-gift-market.md Q1 scenario A, low confidence]. Remento: more than $7M in sales in under a year after its March 2025 TV deal [sourced-secondary: Primetimer 2026-06-05 via memoir-gift-market.md Q2]. Tell Mel: an AI phone interviewer from $39 [sourced: tellmel.ai, 2026-11-24]. Memory Murals: photo-first stories with people tags, typed or spoken by the user, $69/year founding price, sold as a gift [sourced: https://memorymurals.com/, 2026-11-24]. None runs an interviewer over the family's photos and emits a per-photo record of who, when, where and the story [sourced: memoir-gift-market.md Q4 table; Memory Murals and Tell Mel home pages re-checked 2026-11-24].

## Wedge (first use case adopted without changing habits; the first 10 minutes for the payer and for the elder/resident; day-1 value; day-30 value)

**First use case.** A gift purchase the payer already makes at this price (above), delivered through a phone call the parent already knows how to answer. No app for the parent, no library migration for anyone, no platform API: the family adds only the photos it chooses.

**The payer's first 10 minutes.**
1. Buy on the web; pick the parent's name, phone number and two preferred call times.
2. Add 20 starter photos from the phone's system photo picker (no full-library permission), or photograph prints front and back in the mobile browser.
3. Send one link to siblings and cousins: "add photos for Mum's book".
4. Print the gift card. It carries one phone number and one sentence: "Call this number when you are ready; it will ask you about our family photographs."

**The parent's first 10 minutes.**
1. The parent places the first call. An inbound first call matters legally (see Buildability) and for trust: only 19% of US adults generally answer a call from an unknown number, and 67% let it go to voicemail and then check [sourced: https://www.pewresearch.org/short-reads/2020/12/14/most-americans-dont-answer-cellphone-calls-from-unknown-numbers/, survey July 2020].
2. The interviewer says it is an AI, says the family will hear the recording, asks for agreement to record and to be called at the chosen times, and records the answer.
3. It asks about the first photo. On a smartphone or tablet the parent taps a texted link and sees the photo while talking. On a landline the parent looks at "photo 1" in a printed, numbered photo booklet mailed with the gift, and the interviewer also describes the picture.
4. Later calls come from the same saved number at the agreed time. A missed call gets a voicemail and two retries.

**Day-1 value.** Within an hour of the first call the payer and every contributing relative receive one photo with names, an approximate date, a place and a two-minute audio clip of the parent telling it. That clip is the product demo and the referral.

**Day-30 value.** Four or five calls done (calls are weekly for the first eight weeks); 8–15 photos annotated [estimated: assumption of 2–3 photos per 6-minute call; no measurement exists, the 4-week demo measures it]; a family feed where relatives correct spellings and add the next photos; a visible queue ("23 photos waiting for Grandpa").

**Honest limit on "no habit change".** Answering a scheduled call from a saved number is an existing habit; talking to a machine about family is not. How people over 70 respond to an AI phone interviewer is [unknown] at product scale: the only research found has 41, 11 and 20 participants and reports privacy and "false empathy" concerns [sourced-secondary: publisher snippets via memoir-gift-market.md Q5].

## Why now (dated changes since 2024, each tagged)

1. **Real-time voice models went from expensive to cents.** OpenAI's Realtime API launched 2024-10-01 at about $0.06 per minute of audio in and $0.24 per minute out [sourced-secondary: openai.com launch post via search summary, 2024-10]. On 2026-11-24 the list prices are $0.05 per active minute (OpenAI GPT-Live) and $0.023 per minute for both directions (Gemini 3.8 Live) [sourced: vendor price pages via memoir-gift-market.md Q5]. A year of 26 six-minute calls costs $6–22 including telephony [estimated: memoir-gift-market.md Q5].
2. **The legal rule for AI calls is now written down.** FCC Declaratory Ruling 24-17 (adopted 2024-02-02, released 2024-02-08) confirms that AI-generated voices are "artificial or prerecorded voice" under the TCPA and need "the prior express consent of the called party" [sourced: https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf, read 2026-11-24]. A product can be designed to it; before 2024 the status was arguable.
3. **The category leader shipped a phone interviewer in 2026**, which shows the format is commercially acceptable: Storyworth Voice with "Magic Interviews" on "any phone, even a landline" [sourced: storyworth.com and its help pages, 2026-11-24, via memoir-gift-market.md Q1]. This is also the largest threat (see Platform and incumbent risk).
4. **Voice-first beat writing-first in the market.** Remento went from $620,000 lifetime sales before March 2025 to more than $7M in the following year by letting the parent speak instead of write [sourced-secondary: recap press via memoir-gift-market.md Q2].
5. **Self-serve naming was measured and failed.** 0.10 tags per scan at Photomyne, H1 2026 [estimated: digitization-market.md Q6]. The names have to be asked for.
6. **Face-template law tightened in 2026.** Doe v. Apple (S.D. Ill., order of 2026-09-30) let the on-device class proceed after G.T. v. Samsung (7th Cir., 2026-08-07) [sourced-secondary and sourced: research/unknowns-r1.md Q8]. A product whose names come from a person speaking needs no face template to name anyone.
7. **Per-photo understanding is nearly free.** Captioning 22,000 images costs $0.69 in batch [estimated: research/unit-economics.md Q3], so describing 300 chosen photos and reading the handwriting on their backs is under one cent of model cost [estimated: 300 ÷ 22,000 × $0.69].
8. **The archive is usable by an outside AI.** Claude accepts a custom connector on its Free tier from mobile [sourced: support.claude.com via research/byo-ai.md Q2, 2026-11-03]. ChatGPT and Gemini still need web setup and probably a paid plan [sourced and unknown: byo-ai.md Q2].
9. **Counter-signals.** The avatar and audio-only versions of this idea died: HereAfter AI went offline in 2026, StoryFile filed Chapter 11 in May 2024, Artifact shut down [sourced and sourced-secondary: memoir-gift-market.md Q3, Q8]. Every survivor with disclosed scale sells a printed book. AI voice-clone scams make an unexpected AI call to an older person a trust problem; a sourced rate for 65+ is [unknown] (only vendor blogs found, 2026-11-24).

## Product (core loop; explicitly NOT in v1)

**Core loop.**
1. **Collect.** Relatives add photos by link: system picker for phone photos, a browser capture flow for prints that takes the front and then the back. The archive stores only these chosen photos, capped at 300 per gift [estimated: design choice; 300 × ~3 MB ≈ 0.9 GB].
2. **Prepare.** A vision model writes a neutral description of each photo, counts and locates the people (detection boxes only, no face embeddings), and reads any handwriting on the back. Photos are ordered so that related ones follow each other.
3. **Interview.** 26 calls of about six minutes over 12 months: weekly for the first eight weeks, then every two to three weeks [estimated: design choice, matching the 26 × 6-minute cost model in memoir-gift-market.md Q5]. One photo at a time. The interviewer asks who, when, where, then one follow-up, and spells names back.
4. **Structure.** Each answer becomes a record: people (name as spoken, relationship, position in the picture), date or date range with a confidence, place, the story text, and the audio clip. Uncertain answers are stored as uncertain.
5. **Review.** The family feed shows each new record. Relatives fix spellings, merge "Aunt Ruthie" with "Ruth Kowalski", and mark people as deceased or living.
6. **Publish.** At month 12 (or earlier on request) an 8×10 hardcover: one photo per spread, names, date, place, the story, and a QR code that plays the parent telling it. Extra copies can be ordered.
7. **Keep.** The archive stays readable by the family at no charge. A paid renewal keeps the interviewer calling at a slower pace, lets relatives add more photos, and turns on search and the MCP endpoint. Export is always available: photos with embedded XMP names and dates, audio files, and a text file per photo.

**Explicitly NOT in v1.**
- No whole-library import, Takeout, iCloud export or dedupe (that is the pro edition).
- No face recognition. Optional on-device clustering to find "more photos of Ruth" comes later and only with consent.
- No voice cloning, no avatar, no "talk to Grandma after she is gone".
- No speaker-identification model; the interviewer and the caller are recorded on separate channels instead.
- No outbound call before the parent has called in or agreed on a recorded line.
- No native app. No EU or UK launch. No calls to people the payer says have dementia without a family member on the line.

## Business model and pricing (with comparables, tagged)

| Item | Price | Comparable |
|---|---|---|
| Gift: 12 months of interviews, up to 300 photos, one hardcover book, family feed | $149 list; $129 in holiday, Mother's Day and Father's Day windows [estimated: design choice] | Storyworth Color $99 and Unlimited $199 (the tier that lists Magic Interviews on the home page); Remento $99; Tell Mel Standard $129 for 12 interview hours [sourced: memoir-gift-market.md Q1–Q3] |
| Extra book | $69 [estimated: design choice] | Remento $69–99; Storyworth $79 [sourced-secondary: memoir-gift-market.md Q1–Q2] |
| Second storyteller in the same family | $99 [estimated: design choice] | Remento "50% off your second purchase" [sourced: remento.co via memoir-gift-market.md Q2] |
| Renewal ("keep asking"): 12 calls a year, new photos, search, MCP endpoint | $59/year [estimated: design choice] | Storyworth $99; Remento $99/year or $12/month; Tell Mel from $39/year; Skylight Frame Plus $39/year; Memory Murals $69/year [sourced: memoir-gift-market.md Q1–Q3; family-artifact-market.md Q1; memorymurals.com 2026-11-24] |
| Pro edition for organizers | $390/year seat plus $29 per project [sourced: variants/current.md, Business model] | see current.md |
| Senior living and hospice licence | Not priced in v1; treated as distribution, not revenue | Life-story programmes sold to facilities at $2,000–10,000 per community per year, or $40–154 per resident per year (2017 prices) [sourced and estimated: iadvanceseniorcare.com 2017-01-14 via research/institutional-legacy.md Q3]; Famileo Pro US from $99/month per community of up to 50 beds [sourced: famileopro.com via family-artifact-market.md Q2] |
| Price check from the institutional vendor's consumer shop | — | LifeBio sells an app at $149, app plus book at $299, and a phone interview plus book at $699 [sourced: shop.lifebio.com via institutional-legacy.md Q3] |

- Expected revenue per gift in year 1 is about $149 [estimated: 0.7 × $129 + 0.3 × $149 = $135 net price, plus 0.2 extra books × $69 = $13.80; the 70% sale share and the 0.2 are assumptions]. Check against the one disclosed figure: Remento's average order was $119 on a $99 list price [sourced-secondary: recap site, low quality, memoir-gift-market.md Q2].
- Read access is free forever because both leaders promise it ("Your stories are yours forever") [sourced: remento.co via memoir-gift-market.md Q2] and because frame buyers punished a fee added later: Nixplay reached about 1.2% paid and was sued in April 2025 [estimated and sourced: family-artifact-market.md Q1].

## Distribution (non-paid channels with evidence; one paid channel with CAC math if any)

**Non-paid.**
1. **The gift exposes the product to the whole family every week.** Each record goes to every contributing relative as a photo plus a voice clip. Evidence that a multi-relative artifact for a grandparent spreads without ads: Famileo says 70% of subscriptions come from word of mouth [sourced: Bpifrance portrait via family-artifact-market.md Q2]; Aura says its private sharing networks drove 50% of 2024 sales [sourced: TechCrunch 2025-04-16 via family-artifact-market.md Q1]. Our own rate is [unknown]. The repeat purchase is built in: a payer has up to four parents and in-laws.
2. **Gift guides and reviews.** Storyworth's reach was built on them (Wirecutter 2025-06-09, WSJ 2022-10-07) [sourced-secondary: memoir-gift-market.md Q1]. The category is crowded with vendor-written comparison pages [sourced: memoir-gift-market.md Q8; seen again in search results 2026-11-24], so this channel is contested.
3. **Organizers and move managers** already inside the family's boxes: 700+ Photo Managers members and "over 1,000" NASMM members [sourced: research/pro-channel.md Q1, Q6 via current.md]. Small, but they scan fronts and backs and can sell the interview year as an add-on.
4. **Senior living, hospice, Area Agencies on Aging.** Storii's site lists all three as buyer pages [sourced: https://www.storii.com/, 2026-11-24]; LifeBio says it has worked with "over 200 organizations" [sourced-secondary: press release via search, 2026-10-23]. The research verdict is that this channel stays small: LifeBio reports "over $2 million in revenue with 48 employees" after about two decades, Storii's facility product became care-management software, and the dominant engagement vendor (LifeLoop, 4,700+ communities) already includes a "Life Story" feature [sourced-secondary and sourced: institutional-legacy.md bottom line, Q3]. No US community was found billing families for a legacy programme [unknown: institutional-legacy.md Q6]. Use: a place to meet families (the Famileo pattern), not a payer.

**One paid channel: host-read podcast ads**, the channel Storyworth still uses in November 2026 [sourced-secondary: promo-code aggregator via memoir-gift-market.md Q1].
- CPM $24–26 for a 60-second host read [sourced: Libsyn guide via memoir-gift-market.md Q7].
- CAC = CPM ÷ orders per 1,000 downloads. At 0.5 orders per 1,000, CAC = $50 [estimated: 25 ÷ 0.5]. Break-even against first-order contribution of $68 needs at least 0.37 orders per 1,000 downloads [estimated: 25 ÷ 68]. The real conversion is [unknown]; no memoir company discloses CAC [sourced: memoir-gift-market.md Q7].
- Cross-checks: Qeepsake's disclosed CAC is $35 [sourced: Tinybeans Q3 FY26 filing via sizing.md Q4]; a derived paid-install CAC for photo apps is $65–90 [estimated: sizing.md Q4]. Paid acquisition is therefore roughly break-even on the first order and needs the family loop to make money.

**Seasonality.** "Holiday gifting drives much of the company's annual customer acquisition" at Storyworth [sourced-secondary: HNGN 2026-04-30 via memoir-gift-market.md Q1]; Nixplay filed "significantly stronger sales in our third and fourth fiscal quarters" [sourced: SEC offering circular 2023-03-20 via family-artifact-market.md Q1]. The Q4, May and June shares are [unknown]. Consequences: ad prices peak when we must buy; activations and support peak in January; cash arrives up to 12 months before the book is printed.

## Economics (per-customer COGS including print, postage and voice minutes where relevant; GM; payback; cite research rows or derive with tags)

**Per gift, year 1 (revenue ≈ $149 [estimated above]).**

| Cost line | Central | Range | Tag |
|---|---|---|---|
| Voice model plus telephony, 156 minutes, with 25% added for retries and voicemail | $12.5 | $7.2–27.9 | [estimated: memoir-gift-market.md Q5 totals of $5.77 (Gemini), $9.98 (OpenAI), $22.29 (Vapi) × 1.25; the 25% is an assumption] |
| Vision, transcription clean-up, story drafting, storage (~1 GB on R2), texts | $3.2 | — | [estimated: assumption of $2 model cost and $1 messaging; storage 1 GB × $0.015 × 12 = $0.18 from unit-economics.md Q1] |
| Book: 8×10 imagewrap hardcover, 100 pages | $35.91 (Standard Color) | $21.31 (Economy Color) | [estimated: $22.99 + 76 × $0.17; $15.99 + 76 × $0.07; list prices for one copy with a 24-page base, https://www.blurb.com/pricing, 2026-11-24]. Contract price at volume [unknown: needs an RFQ] |
| Book postage, Media Mail, 2 lb | $5.13 | — | [sourced: https://pe.usps.com/text/dmm300/Notice123.htm, effective 2026-10-04] |
| Printed photo booklet for phone-only parents, sent with 40% of gifts | $3.8 | — | [estimated: 0.40 × ($7.00 print + $2.27–2.56 flat postage), family-artifact-market.md Q3; the 40% is an assumption above the 21% of 65+ without a smartphone] |
| Gift card mailer | $1.8 | — | [estimated: $0.82 stamp (Notice 123) + ~$1 print, assumption] |
| Card fees | $4.62 | — | [estimated: 2.9% × $149 + $0.30; stripe.com via unit-economics.md Q7] |
| Human support | $6 | — | [estimated: assumption; older users and gift buyers will phone] |
| Extra books (0.2 per gift) | $8.21 | — | [estimated: 0.2 × ($35.91 + $5.13)] |
| **Total** | **$81.2** | $58.4–96.6 | [estimated: sum; low = Gemini voice and Economy book; high = Vapi voice] |

- **Gross margin: 46% central; 35–61% across the range** [estimated: (149 − 81.2) ÷ 149; (149 − 96.6) ÷ 149; (149 − 58.4) ÷ 149]. The book is the largest line, not the AI. This is far below the 86% of the index-only engine [estimated: unit-economics.md Q7] and below Remento's on-air "86% profit margin", whose basis is unstated [sourced-secondary: recap site, low quality].
- **First-order contribution: about $68** [estimated: 149 − 81.2]. A gift business has to pay back on the first order because the renewal is unproven, so the maximum tolerable CAC is about $68, or about $85 with the Economy book [estimated: 149 − 63.7, where 63.7 = 81.2 − 14.6 − 0.2 × 14.6].
- **Renewal year ($59):** voice for 72 minutes $3.3–12.9, card fees $2.01, storage $0.18, support $2 → COGS $7.5–17.1, gross margin 71–87% [estimated: 72 ÷ 156 × the year-1 voice range; 2.9% × 59 + 0.30].
- **Unfinished gifts.** If a parent stops answering, no book is printed and cost falls by up to $41, but so do referrals and renewals. Completion in this category is undisclosed; the proxies are ~16 stories per Remento order against 52 prompts, and ~40 stories per Storyworth book [estimated: memoir-gift-market.md Q1–Q2]. Breakage is not counted as margin here.
- **Storage stays small by design:** a few hundred chosen photos and under three hours of audio per family, about 1 GB [estimated: 300 × 3 MB + 156 min at ~64 kbps]. No whole libraries of originals.

## Platform and incumbent risk (the obvious feature Apple/Google or the category leader could ship; why this survives or doesn't)

- **Storyworth is the real risk, and it is one release away.** It already has a phone interviewer with follow-up questions, photo prompts ("Discover the stories behind the photos"), a monthly family photo newsletter, 1,000,000+ books of distribution and a 13-person profitable team [sourced: storyworth.com 2026-11-24; YC directory; memoir-gift-market.md Q1]. Pointing Magic Interviews at an uploaded photo and saving "who, when, where" as fields is a feature. The research file's own verdict is that the gap is "feature-sized" [sourced: memoir-gift-market.md bottom line 4].
- **Remento is the second.** Relatives can already submit photos as prompts, and it announced a Legacybox digitisation partnership around May 2025 [sourced and sourced-secondary: memoir-gift-market.md Q2]. It has no live interviewer today.
- **Why this might survive.** (a) Their output unit is a chapter; photos are illustrations and nothing is stored as structured identity. Ours is the per-photo record and the people graph. (b) They have no reason to build the archive: both give away access after the year and earn on the next gift. (c) The landline path with a printed, numbered photo booklet is operational work a software-only competitor may skip. (d) Corrections by relatives accumulate into a family name list that makes later calls and later relatives' photos better. None of these is a technical barrier. The honest statement is that this survives only by being the photo product while the incumbents stay memoir products, and that is their choice, not ours.
- **Ancestry** could ship an interviewer over Tree Gallery photos. It already lets users tag people in photos and attach up to 14 minutes of audio (Storymaker Studio, 2023) and sells the scan at $0.49 a photo [sourced-secondary and sourced: memoir-gift-market.md Q4; digitization-market.md Q3]. It scans fronts only [sourced: ancestry.com offer page via digitization-market.md Q3].
- **Apple and Google.** Neither sells a gift to a third person or places calls to a relative. Both can describe and search the account holder's own photos. A user can already hold up a print to an assistant's live voice mode and talk about it; nothing saves that as a family record. Whether either adds "ask a relative about this photo" is [unknown]; research/assumptions/A4.md records no such roadmap item.
- **A swarm of small AI memory apps** (Memory Murals, Tell Mel, Autobiographer, Life-Story.ai, Storii, companion-call services such as ElderVoice at $25 and $49 a month) [sourced: vendor sites, 2026-11-24, and memoir-gift-market.md Q3]. None discloses traction. They raise the cost of every search click and gift-guide slot.

## Compounding asset

- **Per family: the only copy of what the parent said.** Names for faces nobody else can name, dates, places, and the voice. It cannot be regenerated by a model and, after the parent dies, cannot be recreated at all. This is the first asset in three rounds that is not rebuildable for cents (compare the index: byo-ai.md Q5, unit-economics.md Q3).
- **Per family: the people graph and name list**, corrected by relatives. Every new photo added by a cousin can be matched to known names by a person, and later, with consent, by an on-device model.
- **Switching cost is deliberately low for reading and high for continuing.** Export is open (XMP `PersonInImage`, audio, text) [sourced: research/ios-feasibility.md Q9 for the format]. What does not move is the weekly habit, the relatives' feed and the queue of unanswered photos.
- **Company level:** interview technique data (which question gets a name, which gets a story, when a call should end), answer-rate data by call time and channel. Useful, but a competitor with more calls (Storyworth) accumulates it faster.
- **Honest limit:** a finished book is also a finished reason to pay. Qeepsake's CEO says of baby books, "As you complete your baby book… you're more likely to churn" [sourced-secondary: transcript 2026-04-29 via research/grandparent-loop.md Q2].

## Buildability (4-week demo spec for 2 engineers; ugliest technical risk; what is platform- or policy-gated)

**Demo, two engineers, four weeks.**
- Week 1: web upload by link; browser capture of print fronts and backs; vision description, people boxes, handwriting OCR; photo ordering.
- Week 2: voice agent on a hosted real-time model through a telephony provider. Inbound consent call, scheduled outbound calls with retries and voicemail, tap-to-talk web page that shows the photo, dual-channel recording.
- Week 3: structuring pipeline from transcript to per-photo record; spell-back for names; family feed with corrections, deceased/living flag; weekly digest with audio.
- Week 4: book PDF with QR codes, sent to a print API; read-only MCP endpoint over the records; pilot with 10 real parents aged 70+ recruited from friends and family.
- Acceptance (thresholds are choices, not benchmarks): at least 70% of scheduled calls completed within three attempts; at least 2 photos per call with one named person each; at least 95% of names spelled correctly after one family review; no parent asks to stop because the caller felt like a scam.

**Ugliest technical risk: getting proper names and the right face from an old voice on a narrowband phone line.** The whole product is the names. Speech recognition is weakest on surnames, nicknames and place names, and telephone audio makes it worse; accuracy for speakers over 75 on a landline is [unknown] and must be measured in week 2. A 2026 review of the nearest product reports stories with changed names [sourced-secondary: review-site summaries found via search, 2026-11-24, low quality]. "The woman on the left" must be tied to a detection box without the interviewer and the parent seeing the same thing. Mitigations: spell-back, the numbered booklet, a GEDCOM or typed name list from the family, and relatives' review. If names are wrong in the printed book, the gift is ruined in front of the whole family.

**Second risk: answer rate.** If parents do not pick up, nothing else matters. Kill criterion: fewer than 50% of scheduled calls completed across the pilot.

**Policy- and platform-gated.**
- TCPA: prior express consent of the called party before any AI-voice call [sourced: FCC 24-17]. The payer cannot give it for the parent. Hence the inbound first call.
- FCC's 2024 proposal to require AI disclosure on calls was not final as of October 2026 [sourced-secondary: vendor compliance guides via search, 2026-11-24]; the product discloses on every call anyway.
- Call recording: 11 or 12 states require all parties' consent, California among them (Penal Code §632 and §632.7) [sourced-secondary: Justia 50-state survey via search, 2026-11-24]. Consent is asked and recorded at the start of each call.
- Voice as biometric data: Illinois and Texas both list "voiceprint" in the statutory definition of a biometric identifier [sourced: FindLaw 740 ILCS 14/10 and Tex. Bus. & Com. Code §503.001 via research/face-regulation.md Q1–Q2]. No voiceprint is computed; no voice is cloned.
- Carrier spam labelling and text-message sender registration: required in practice; cost and lead time [unknown].
- People named in stories who never agreed to be in an archive: names typed or spoken by a relative are not biometric data, but a stored face rectangle plus a name is untested [unknown: face-regulation.md Q7].
- Nothing is gated by Apple or Google.

## Ceiling (path to $100M ARR with tagged inputs and arithmetic; or the honest number it tops out at)

**Pool.** 61.2M US residents aged 65+ are the people a gift can be bought for [sourced: Census 2025-06-26]; at least ~67M adults could be the buyer [estimated: sizing.md Q2].

**What the category sells today.**
- Storyworth: 150,000–500,000 plans a year [estimated: memoir-gift-market.md Q1 scenario A; both key inputs are assumptions].
- Remento: about 59,000 orders a year [estimated: $7M ÷ $119 average order; both sourced-secondary].
- Category: about 210,000–560,000 gifts a year, or 0.34–0.91% of people 65+ each year, worth about $20–52M [estimated: sums of the two rows; ÷ 61.2M; $13.5–45M + $7M; the long tail is unknown and small].

**Reachable share.** The only entrant benchmark is Remento, which reached 12–39% of Storyworth's estimated volume after a network television appearance [estimated: 59,000 ÷ 500,000; 59,000 ÷ 150,000]. Without that event, 5–15% of category units by year five is the assumption used here [estimated: assumption set below the Remento benchmark].

**Arithmetic (pool × reachable share × price).**
- Gifts: 61.2M × 0.34–0.91% × 5–15% = 10,500–84,000 a year; central 40,000 [estimated]. At $149: $1.6M–12.5M; central $6.0M [estimated].
- Renewal base at steady state = gifts × first renewal ÷ (1 − later retention). First renewal 5–25% and later retention 70–80% are assumptions; no memoir company discloses either [unknown: memoir-gift-market.md Q7]. The bounds used are Nixplay's ~1.2% paid on a gifted artifact, the 23% first annual renewal of photo apps, and Qeepsake's 79% retention [estimated and sourced: family-artifact-market.md Q1; unit-economics.md Q6; grandparent-loop.md Q2]. Central: 40,000 × 0.15 ÷ 0.25 = 24,000 payers × $59 = $1.4M. Range $0.1M–6.2M [estimated: 10,500 × 0.05 ÷ 0.30 × 59; 84,000 × 0.25 ÷ 0.20 × 59].
- Pro edition through organizers: $0.7–3M [estimated: variants/current.md Ceiling].
- Institutions: $0–2M; central $0.5M [estimated: assumption capped at LifeBio's "over $2 million" after two decades; the whole channel at LifeLoop-level penetration of 8.4% and $40–150 per resident per year is $7.5–28.3M, institutional-legacy.md Q8].
- **Honest total: about $2–24M a year; central about $9M** [estimated: 1.6 + 0.1 + 0.7 + 0 = 2.4; 6.0 + 1.4 + 0.7 + 0.5 = 8.6; 12.5 + 6.2 + 3.0 + 2.0 = 23.7].

**What $100M would take.** Revenue per annual gift at steady state is about $184 [estimated: 149 + 59 × 0.15 ÷ 0.25]. $100M needs about 542,000 gifts a year [estimated: 100M ÷ 184], which is 0.89% of everyone 65+ every year, 1.1–3.6 times Storyworth's estimated annual volume, and 97–259% of the whole category as estimated above [estimated: 542 ÷ 500; 542 ÷ 150; 542 ÷ 559; 542 ÷ 209].

**Sensitivity.**
- Price $199 instead of $149: 427,000 gifts a year still needed [estimated: 100M ÷ (199 + 35.4)].
- A 25% share of the category's top estimate: 140,000 gifts × $184 = $26M [estimated].
- The category doubles and we hold 25%: $52M [estimated: 280,000 × 184]. There is no evidence for either condition.

**Largest sourced revenue of any comparable.**
- Memoir gifts: Remento, more than $7M in under a year [sourced-secondary: founder statement on television via press]. Storyworth has never disclosed revenue.
- Printed family journals: Famileo, €15.3M in 2025 after ten years [sourced-secondary: Ouest-France via family-artifact-market.md Q2].
- Institutional life-story programmes: LifeBio, "over $2 million" (2023) [sourced-secondary: founder interview summary via institutional-legacy.md Q3].
- Gifted frames: Nixplay, $57,865,975 in FY2021, then $20,038,285 in FY2023 [sourced: SEC filings via family-artifact-market.md Q1]. Skylight's "$300M+" is unaudited and calendar-led [sourced: company job listing via family-artifact-market.md Q1].

**Verdict.** $100M does not pencil. The evidence supports a $2–24M business, most likely high single digits, with a real asset behind it. Three observations would raise it: Storyworth's revenue disclosed at the top of its estimated range; a pilot in which phone interviews about photos finish at more than twice the category's completion; a payer-reimbursed code for life-story work in care settings, which does not exist today [sourced: institutional-legacy.md Q8].

## Load-bearing assumptions (numbered; each with the observable fact that would falsify it)

1. **Parents aged 70–90 will take scheduled calls from an AI and talk.** Falsified if fewer than 50% of scheduled calls are completed in a 10-family pilot, or more than 2 of 10 parents ask to stop.
2. **A photo is a better prompt than a question.** Falsified if photo calls yield fewer than 2 named photos per call, or if parents prefer telling unprompted stories and ignore the picture.
3. **Names and dates come out right.** Falsified if name accuracy after one family review is below 95% on the pilot's records, or a pilot family rejects the proof of the book for wrong names.
4. **Adult children will pay $129–149 when Storyworth and Remento cost $99.** Falsified if a landing-page price test shows conversion at $149 below half of conversion at $99.
5. **The family wants the archive, not only the book.** Falsified if fewer than 30% of contributing relatives open the feed in month 3, or first renewal is below 10% in the first cohort. Every scaled product in the category sells the book [sourced: memoir-gift-market.md Q4].
6. **The weekly clip produces referrals.** Falsified if fewer than 1 in 10 gifts leads to a second purchase in the same extended family within 12 months.
7. **Storyworth and Remento do not ship per-photo interviews with saved names within 12 months.** Falsified by a release note or help page describing an interviewer that asks about an uploaded photo and stores who is in it.
8. **First-order contribution stays near $68.** Falsified if contract print quotes exceed $36 for the 100-page colour hardcover, or measured voice cost with retries exceeds $28 per gift.
9. **Paid CAC can be held under $68.** Falsified if the first three podcast placements return fewer than 0.37 orders per 1,000 downloads.
10. **Consent can be collected from the parent without killing activation.** Falsified if more than 30% of gifted parents never place the first inbound call within 30 days.
11. **Recording and naming living relatives in stories creates no liability the product cannot carry.** Falsified by a ruling that a stored face rectangle plus a name is a biometric identifier, or by a state action against a memoir service over recorded calls.
12. **The honest ceiling is accepted at $2–24M unless one of the three observations in the Ceiling verdict appears.**

## Relationship to variants/current.md (what is kept from the organizer workbench and the index-only engine; what is dropped)

**Kept.**
- The client-review screen. In current.md it is step 5 of the workbench; here it is the product, with the parent's voice as the main input and relatives as correctors. This applies the round-2 note that naming is a prompted, human act.
- The consent rules: named living people by human entry or consent; deceased flag; no templates on servers; server-side matching off in IL, TX, WA and the EU.
- The delivery formats: XMP `PersonInImage`, import back into Apple Photos and Google Photos albums, optional hosted archive with an MCP endpoint.
- The index-only engine, as a later helper on a relative's own phone or Mac: with permission it suggests which of their photos belong in the parent's queue (old photos, photos near already-named ones). Originals stay where they are.
- The organizer workbench as the pro edition. An organizer who is already scanning a family's boxes, fronts and backs, loads the selection and sells the interview year on top of a $1,500–4,000 project [sourced: pro-channel.md Q2 via current.md].
- Front-and-back capture of prints; GEDCOM import for the name list; the tribute pack, which an interviewed archive supplies ready-made.

**Dropped.**
- Takeout repair, library dedupe and whole-library ingest as the consumer product.
- Seat pricing as the main revenue line. It remains a small side line.
- Mac-first. The consumer product is web and telephone.
- Face clustering as the default way to find people.
- The claim that organizing is what the family pays for.

## Evidence pointers (file:section for every claim above)

- Payer and user pools, sandwich generation, 65+ population, grandparents, deaths by age: research/sizing.md Q1 (Census line), Q2.
- Smartphone ownership 65+, AARP grandparent data: research/family-artifact-market.md Q5; research/grandparent-loop.md Q4.
- Storyworth facts, prices, Voice and Magic Interviews, revenue scenarios, completion proxies, channels, seasonality: research/memoir-gift-market.md Q1, Q8, numbers table. Home page re-read 2026-11-24: https://www.storyworth.com/.
- Remento facts, photo prompts, Legacybox partnership, average order, margin claim: research/memoir-gift-market.md Q2.
- Tell Mel, Storii, Autobiographer, failures (HereAfter, StoryFile, Artifact, StoryTerrace): research/memoir-gift-market.md Q3, Q8. Re-read 2026-11-24: https://www.tellmel.ai/ (no family-photo feature on the home page; landline; 26 countries, 10 languages), https://www.storii.com/ (hospice and Area Agency on Aging pages; up to 3 automated calls a week).
- Gap statement and table of who names people in photos: research/memoir-gift-market.md Q4. Added 2026-11-24: https://memorymurals.com/ (photo-first stories, people tags, $69/year, gift option).
- Voice and telephony prices, 156-minute cost, small studies of older adults: research/memoir-gift-market.md Q5.
- Gift spending, price anchors, CAC proxies, affiliate rates, podcast CPM: research/memoir-gift-market.md Q6–Q7.
- Frames (Aura, Skylight, Nixplay filings, paid attach, lawsuit), journals (Famileo, Neveo), print and postage for a 20-page booklet, word-of-mouth shares: research/family-artifact-market.md Q1–Q3, Q7.
- Photomyne tag rate, Ancestry scan price and fronts-only scanning: research/digitization-market.md Q3, Q6.
- Qeepsake churn quote and retention, Tinybeans CAC: research/grandparent-loop.md Q2; research/sizing.md Q4.
- Retention regimes, Stripe fees, R2 price, caption cost, index-only margin: research/unit-economics.md Q1, Q3, Q6, Q7.
- Face-template law, consent architecture, rectangle-plus-name unknown: research/face-regulation.md Q1, Q7; research/unknowns-r1.md Q8.
- MCP access by assistant: research/byo-ai.md Q2, §3.
- Organizer channel, project prices, pro edition pricing and ceiling: variants/current.md; research/pro-channel.md Q1, Q2, Q6.
- Institutional vendors, prices, family-as-payer, channel ceiling: research/institutional-legacy.md bottom line, Q3, Q6, Q8.
- Tribute collection by funeral homes (context for the tribute pack): research/estate.md Q6.
- Fetched for this variant on 2026-11-24: FCC 24-17 (https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf); Pew on unknown callers (URL in Wedge); Blurb price list (https://www.blurb.com/pricing); USPS Notice 123 (https://pe.usps.com/text/dmm300/Notice123.htm); https://www.eldervoice.com/ (AI companion calls for a parent at $25 and $49 a month; a higher tier is listed at $99).
- Seen only as search summaries on 2026-11-24 (not read at source): OpenAI Realtime launch prices (openai.com/index/introducing-the-realtime-api); state call-recording consent counts (justia.com 50-state survey); status of the FCC AI-disclosure proposal (vendor guides); LifeBio "over 200 organizations" (natlawreview.com press release); Remento review reporting changed names (keepsakeproject.co, evermemory.ai).
- Not resolved: completion and renewal rates for any memoir company; CAC for any memoir company; how people over 70 respond to an AI phone interviewer; speech-recognition accuracy on elderly speech over landlines; contract print prices; carrier registration cost; whether any US care community would bill or refer families for this.
