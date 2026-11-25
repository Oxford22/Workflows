# v4-frame — The story frame: a gift frame that asks about the pictures

Written 2026-11-25 for round 4. Source codes: **FDM** = `research/frame-device-market.md`, **FAM** = `research/family-artifact-market.md`, **MGM** = `research/memoir-gift-market.md`; an S-number after a code resolves to a URL in §6 of that file. Facts fetched for this file carry their own URL and are listed under Evidence pointers. Verdict up front, because the research is one-sided: **the gap is real and one firmware update wide; $100M does not pencil. The honest number is about $6M of mostly one-time hardware revenue in year five at the centre ($1M at the research-supported end, $30M if the company repeats Aura's first six years), and well under $1M a year as software only [estimated: Ceiling section].** The variant is written out in full so critics can check that rather than take it on trust.

## One line

A Wi-Fi gift frame for a grandparent's kitchen with a speaker, a microphone and one physical button: the family sends photos and scans, the frame shows them, and when the elder presses the button it plays a relative's question about the photo on screen, records the answer, and returns to the family a named, dated, narrated record of that photo in the elder's own voice.

## Customer (payer, user, supplier or audience; how many [tagged]; what they do today; what they pay today)

**Payer: an adult child aged about 40–60.**
- How many: about 67M US adults have a living parent aged 65+ and a dependent child (the "sandwich" subset; adults with a living parent 65+ in total are [unknown]) [estimated: 25% of adults, Pew 2026-08-27, `research/sizing.md` rows 22–23]. The people already buying this object: Skylight claims "more than 12 million customers" across frames and calendars [sourced: FAM S61, 2026-09-30, company release, unaudited]; Aura claims "more than 10 million people" and "4 average contributors per frame" [sourced: FAM S4, read 2026-11-25]; a complaint alleges Nixplay sold over 2.5 million frames to over 2.2 million customers [sourced: FAM S16, 2025-04-22, allegation].
- What they do today: buy a frame once and feed it from their phones. Aura's and Skylight's retail titles end "Gift for Parents & Grandparents" [sourced-secondary: FAM S17, July 2026]. Some buy a memoir gift as well, and it stalls at the parent: about 10 stories per Remento family against 52 weekly prompts [estimated: 1,000,000 stories ÷ 100,000 families, MGM Q2].
- What they pay today: $47.99 for a generic Frameo frame, $109.99 for a Skylight 10" and $139 for an Aura Carver on sale, $199.99 list ($114.99 on Black Friday) for Amazon's Alexa Photo Frame, up to $499 for Aura's Ink 13" [sourced: FDM S4, S1, 2026-11-25; FAM S4]. $99 for Storyworth or Remento [sourced: MGM S1, S11, 2026-11-25]. First-year cost of an elder device with a monthly fee: $689 (GrandPad) and $957 (ElliQ) [estimated: 329.99 + 12 × 29.95; 249 + 12 × 59, FDM rows 8 and 11].

**User: a parent aged about 70–90.**
- How many: about 65M US grandparents, about 41M of them aged 65+ [sourced: AARP 2026-06-16; estimated: 2/3 × 61.2M, `research/sizing.md` row 24]. The count aged 70–90 with home Wi-Fi is [unknown: not collected; a Census single-year-of-age file would resolve it].
- Two facts about this user that the design cannot wish away: 55% of Americans aged 75 and older have disabling hearing loss [sourced: https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing, page updated 2024-09-20, NHANES 2015–2020], and speech recognition is measurably worse on older voices (33.3% word error before fine-tuning in one student project) [sourced-secondary: FDM S31].
- What they do today: look at the frame. No frame on sale lets them answer it. Nine in ten GrandPad purchases are made by a child or caregiver [sourced: FDM S17, 2026-11-19], so the user rarely chooses the device.

**Contributors: siblings and grandchildren.** About 4 per frame on Aura's own figure [sourced: FAM S4]. They send photos, record questions, and confirm names.

## Wedge (first use case adopted without changing habits; the first 10 minutes for each party; day-1 value; day-30 value)

**No habit change for the payer.** They were going to buy a frame; this is a frame. Nothing is migrated: the payer picks a handful of photos, as with any frame.

**Payer, first 10 minutes** (before the frame ships, the gift-setup pattern Aura and Amazon already use [sourced: FAM S5; FDM S1]). (1) In a browser, choose photos through the phone's system picker, which needs no library permission. (2) Photograph a few old prints, front and back, because handwritten backs carry names and dates [`research/digitization-market.md` Q3, Q5]. (3) Type the first names of the family, which the speech recogniser uses as a hint list. (4) Record a question in their own voice on any photo: "Mom, who is standing next to you here?" (5) Text an invite link to siblings.

**Elder, first 10 minutes.** Plug it in. Photos appear with no setup, as on a preloaded Aura or Amazon frame. On a photo that carries a question, the frame shows the asker's name and the question in large type. The elder presses the button, hears the relative ask it, answers, and presses again to send. Nothing is recorded unless the button was pressed, and an answer that is not sent is discarded.

**Contributor, first 10 minutes.** Open the link, add photos, ask a question, hear the first answer.

**Day-1 value.** For the elder and the payer, the same value as any Wi-Fi frame, from the first minute. The first answered photo reaches every contributor as an audio clip with proposed names, place and year; one tap confirms or corrects them.

**Day-30 value.** A set of photos with confirmed names, dates and places, each linked to the clip where the elder said so, searchable by the family and by any AI assistant through an MCP endpoint. How many photos that is after 30 days is [unknown]: no frame has measured it, and the nearest proxy is about 10 recordings per family per year in a product where the elder must open a link [estimated: MGM Q2]. That number is the whole bet (see assumption 1).

**Honest gap.** The research says the variant's "when the elder chooses" sits on the weaker side of the evidence: devices that start the conversation get used (ElliQ, 41–48 interactions a day in a state programme), wake-word devices decay (a three-week Echo study) [sourced: FDM S24, S28; sourced-secondary: FDM S23]. The design answer is a question from a named grandchild on the screen, not a machine prompt and not a wake word. Whether that works is untested.

## Why now (dated changes since 2024, each tagged)

For:
1. **2026-10-28: Amazon announced the Alexa Photo Frame**, a 10.1" gift frame with microphones, voice search and voice notes at $199.99 [sourced: https://www.aboutamazon.com/news/devices/amazon-alexa-photo-frame, 2026-10-28, re-read for this file]. It proves the category leader in voice thinks a frame should have a microphone. The voice note is the giver's, recorded in the phone app; a reviewer writes "Amazon says recording directly on the frame is coming later" [sourced-secondary: https://www.bgr.com/2322517/alexa-photo-frame-review/, 2026-11-20, re-read]. It is also the main threat (see Platform risk).
2. **2026: real-time voice models are priced per minute at cents.** Gemini 3.8 Live $0.023 a minute for both audio directions, OpenAI GPT-Live $0.05, Deepgram's agent $0.075 [sourced: MGM S39, S38, S41; estimated: 0.005 + 0.018]. A spoken follow-up question could not be bought at this price in 2019.
3. **2026-03-27 to 2026-07-08: a frame with two microphones and a 5W speaker went on sale from an unknown brand.** AmivoFrame's store product was published 2026-03-27 and announced 2026-07-08; it lists a quad-core A53, 2GB/16GB, dual microphones, at $169 on sale against $199 [sourced: https://amivoframe.com/products.json and https://amivoframe.com/products/amivoframe-smart-digital-photo-frame, read 2026-11-25; announcement via GlobeNewswire paid placement, 2026-07-08]. So a microphone-equipped frame is something a small company can already source. The same product is evidence against demand: its iOS app has 1 rating [sourced: https://itunes.apple.com/search?term=amivoframe&entity=software&country=us, 2026-11-25].
4. **2026: the memoir category moved to voice and to single photos.** Storyworth shipped a phone interviewer with follow-up questions; Remento launched a photo-anchored ornament on 2026-10-22 at $29.99 [sourced: MGM S1, S76]. Buyers are being taught that a photo can carry a recording.
5. **2026-09-30: Skylight said its "business doubled" and expanded its inventory facility to $75M** [sourced: FAM S61]. Household screens bought as gifts are growing, at least at one company and by its own account.

Against:
6. **2026-07-24: a further 12.5% duty** took the modelled rate on Chinese frames to 37.5% [sourced-secondary: FDM S37, aggregator; the frame's exact tariff subheading is unconfirmed].
7. **2025-04-22: Nixplay was sued for "bait-and-switch"** after moving free features behind its plan [sourced: FAM S16]. A subscription cannot be added later.
8. **November 2025: a class of about 1.2 million Illinois residents was certified against Amazon over Alexa voiceprints** [sourced-secondary: https://blogs.duanemorris.com/classactiondefense/2025/11/26/the-class-action-weekly-wire-episode-128-illinois-federal-judge-certifies-class-of-1-2-million-amazon-alexa-users-in-bipa-class-action/, via search summary 2026-11-25; merits undecided]. Speaker identification is off the table.

Honest reading: items 1–3 help Amazon and any Shenzhen brand at least as much as a seed-stage company. The why-now is real for the category and weak for this entrant.

## Product (core loop; explicitly NOT in v1)

**Core loop.**
1. **Send.** Relatives add photos and scans from a browser link. The frame and the archive hold display-size copies only (the Alexa frame's panel is 1280 × 800 [sourced-secondary: FDM S7]); originals stay on the relatives' phones and cloud accounts.
2. **Ask.** A relative records a question on a photo. If nobody has, the frame may offer one generic question ("Who is in this picture?") at a time of day the elder picked. Questions are shown as large text as well as spoken, because of the hearing-loss figure above.
3. **Answer.** The elder presses the button; a light and a spoken "recording" mark the session; the elder talks; a second press sends. One optional spoken follow-up ("About what year was that?") is generated by a voice model.
4. **Extract.** Speech-to-text with the family's name list as a hint, then a language model proposes a record for that photo: people, place, year, relationship, a one-line caption. Every field points to the clip and the second where it was said.
5. **Confirm.** A relative confirms or corrects with one tap, and can tap a face to say which person is which. No face template is computed anywhere; a name is attached to a photo, or to a rectangle a person drew.
6. **Keep and query.** The family archive holds photo, record, clip and who confirmed it. Export is XMP sidecars plus audio files. An MCP endpoint lets the family's own AI assistant answer "what did Grandma say about the lake house?" [`variants/current.md` core loop item 7; `research/byo-ai.md` Q5].
7. **Print.** An optional book: photo, caption, a QR code that plays the clip (the Remento and Storyworth pattern [sourced: MGM S11, S12]).

**Phase 1 is software on a commodity Android tablet** in a stand, locked to the app, with an on-screen button and a cheap external one. Its only purpose is to measure whether elders answer. The custom frame is built only if they do.

**Explicitly NOT in v1.** A wake word or any always-listening mode. Speaker identification or voice cloning. Face recognition. Video calls or a camera. Reminders, wellness summaries or any monitoring of the elder (AmivoFrame's "Family Letter" [sourced: https://amivoframe.com/, 2026-11-25]). Full-library access on anyone's phone. Storage of originals. A mandatory subscription. Custom hardware before the Phase 1 result. Sale in the EU or UK.

## Business model and pricing (with comparables, tagged)

- **Frame: $179 list, $149 in Q4, no subscription** [estimated: design choice set between Aura Carver at $149 list and the Alexa Photo Frame and AmivoFrame at $199–199.99 list; FDM S1, FAM S4, amivoframe.com 2026-11-25]. The plan below assumes $149 realised. Q4 discounting is deeper than that at the leaders: 21% at Skylight, 42.5% at Amazon within a month of launch [estimated: FDM row 5, row 1].
- **Included for the life of the frame:** photos, family sending, questions, recording, the confirmed archive, export. Included voice-model minutes are capped (see Economics); recording itself is not.
- **Book: $69** [sourced comparable: Remento extra book $69 up to 200 pages, MGM S21, secondary].
- **Family archive plan: $29 a year, optional.** Unlimited spoken follow-ups, AI query, a second frame on the same archive. Comparables: Nixplay Plus $29.99 a year, Skylight Frame Plus $39 a year, Frameo+ $16.99 a year, AmivoFrame Plus $8.90 a month or $379 for the frame with lifetime Plus [sourced: FAM S62b, S62; sourced-secondary: FDM S33c; sourced: amivoframe.com product page, 2026-11-25].
- **What buyers do with such plans:** Aura sells none and says so in its headline [sourced: FAM S4]. Nixplay reached about 1.2% of users paying [estimated: FAM Q1, on inputs not re-verified] and then the lawsuit. Skylight's attach rate is [unknown]; its founder's stated lesson is that "devices that sit unused make subscription value harder to justify" [sourced: FDM S14b, undated]. Every elder device charges $9.95–65 a month and none has a sourced revenue above $10M [sourced: FDM Q2]. The plan is therefore modelled at 1.2–10% attach and treated as a rounding item.
- **Phase 1 kit:** tablet, stand and software sold to pilot families at about hardware cost. It is an experiment, not a product line.

## Distribution (non-paid channels with evidence; one paid channel with CAC math if any)

**Non-paid.**
1. **The contributors.** Each frame puts the product in front of about four adults who did not buy it and who mostly have another set of parents. Aura says private networks "helped to drive 50%" of its 2024 sales [sourced: FAM S2, 2025-04-16, company statement]. This product adds a second exposure: every answered photo is sent to all contributors. Evidence that this loop works for a new brand: none.
2. **Amazon search.** Demand is visible at the shelf: "6K+ bought in past month" on one Skylight listing and on one Aura listing in mid-November [sourced: FDM S4, 2026-11-25]. Amazon was 51% of Nixplay's 2021 sales [sourced: FAM S13]. But Amazon's own frame now sits in the same results at $114.99, and ranking there is earned with reviews and ads.
3. **Gift guides.** Affiliate pages agree Wirecutter favours Aura [sourced-secondary: FDM S44c]; the sales effect of a pick is [unknown]. A frame that records Grandma is an easy story to pitch; that is an argument, not evidence.
4. **Installers.** Professional photo organizers (700+ association members) and senior move managers (over 1,000) already handle the boxes of prints [sourced: thephotomanagers.com and nasmm.org via `research/pro-channel.md` Q1, Q6]. The frame gives them a way to get the prints named. Small.
5. **Carrier and big-box retail, later.** Consumer Cellular put GrandPad in 117 stores on 2026-11-19 [sourced: FDM S17]. Skylight says Costco and Best Buy give "a stamp of quality" with "lower subscription attach rates" [sourced: FDM S14b]. Vendor terms for this category are [unknown]; generic guides cite payment at 60–90 days and chargebacks of 1–5% [sourced-secondary: FDM S46].

**One paid channel, with math.** Sponsored placement on Amazon in Q4. No frame maker discloses acquisition cost [unknown: FDM Q6]. The one sourced photo-app figure is $35 (Qeepsake) and the derived paid-social figure is $65–90 [`research/sizing.md` Q4]. Against a contribution of $35–59 per frame (Economics), $35 leaves $0–24 and $65–90 leaves a loss of $6–55 per frame [estimated: 35.04 − 35; 59.08 − 35; 59.08 − 65; 35.04 − 90]. Paid acquisition at photo-app prices consumes the hardware margin. The business works only if most units come from search position, guides and the contributor loop, which is the slow road: Aura needed nine years to reach "single-digit millions" of frames [estimated: 2025 − 2016, FDM plain statement].

## Economics (per-customer or per-unit COGS; GM; payback; capital needs; cite research rows or derive with tags)

**Per frame, own-brand device, sold on Amazon at $149** [estimated: realised price from Business model].

| Line | Low cost case | High cost case | Tag |
|---|---|---|---|
| White-label 10.1" frame plus microphone-array chip, landed with duty, before freight | $47.69 | $55.26 | [estimated: FDM row 19] |
| Microphones, speaker, button, enclosure change, packaging, freight | $10.00 | $15.00 | [estimated: planning allowance; no quote exists; FDM marks these unknown] |
| Amazon referral fee, 8% or 15% | $11.92 | $22.35 | [estimated: 149 × rate, FDM row 21] |
| Fulfilment | $7.00 | $7.00 | [estimated: allowance; the fee for this size tier is unknown per FDM Q4] |
| Returns: 17% of holiday sales returned, half the value lost | $12.67 | $12.67 | [sourced: FDM S39 for 17%; estimated: 0.17 × 0.5 × 149; the half is an assumption] |
| Cloud, first year, 20 minutes of voice-model time plus storage | $0.64 | $1.68 | [estimated: 20 × 0.023 + 0.18; 20 × 0.075 + 0.18; storage ≤ 1 GB × $0.015 × 12, `research/unit-economics.md` Q7] |
| **Contribution before acquisition and staff** | **$59.08 (40%)** | **$35.04 (24%)** | [estimated: 149 minus the column] |

- Cross-check: Nixplay's filed gross margin was 37.6%, 37.0%, 26.5% and 32.9% across 2020–2023 [sourced: FAM S13; estimated: FAM S14]. The table lands in the same band, which is the point: this is a hardware margin.
- At a 20% deeper Q4 price of $119 the same table gives $34.03 (29%) to $12.09 (10%) [estimated: 119 − 57.69 − 9.52 − 7 − 10.12 − 0.64; 119 − 70.26 − 17.85 − 7 − 10.12 − 1.68].
- **The no-subscription liability.** Twenty minutes a year is the memoir category's completion level applied to two-minute answers [estimated: 10 recordings × 2 minutes; MGM Q2]. An elder who uses the frame the way ElliQ users use theirs would cost far more: three 3-minute sessions a week is 468 minutes, or $10.76–35.10 a year, every year, against a one-time sale [estimated: 3 × 3 × 52; 468 × 0.023; 468 × 0.075]. The best customers are the unprofitable ones. Hence the cap: plain recording and offline transcription are unlimited; live spoken follow-ups are limited unless the family takes the plan. AmivoFrame prices the same liability at $8.90 a month or a $210 lifetime premium [estimated: 379 − 169].
- **Add-ons per frame per year, central case:** 10% buy a $69 book and 5% hold a $29 plan, about $8.35 of revenue [estimated: 0.10 × 69 + 0.05 × 29; both rates are assumptions]. Book cost needs a print quote [unknown]; public softcover list prices of $14.99–24.98 are the only anchor in the research [sourced-secondary: FAM S57].
- **Payback.** There is no payback period: the sale is one-time and acquisition has to be covered by the first-order contribution.

**Capital.**
- Phase 1: 50 pilot households on retail tablets at $160–220 each is $8,000–11,000 of hardware [estimated: 50 × 160; 50 × 220; tablet price sourced-secondary: 9to5toys roundup 2025-11-28 via search summary, a 2025 price; 2026 price unknown].
- First own-brand run of 5,000: $238,000–276,000 before freight and tooling, plus $4,900–12,000 for FCC certification over 4–12 weeks [estimated and sourced: FDM rows 25, 19]. Tooling and safety certification [unknown].
- The central year-five case of 40,000 frames needs $2.3–2.8M of inventory committed before Q4 [estimated: 40,000 × 57.69; 40,000 × 70.26]. The high case of 178,500 frames needs $10.3–12.5M [estimated: 178,500 × the same], which is inventory debt of the kind Skylight took ($15M in 2023, $50M in 2025, $75M in 2026) [sourced: FAM S7, S61].
- A seed round covers the pilot and one 5,000-unit run. Aura raised $6M before it shipped a frame and about $99M in total [sourced: FDM S13b; estimated: 13 + 26 + 60, FAM Q1].

## Platform, incumbent and regulatory risk (the obvious move by Apple, Google, Amazon or the category leader; the law that could close this; why this survives or doesn't)

**Amazon.** The obvious move is one release: on-frame recording, which a reviewer says Amazon has confirmed is coming, then "Alexa, ask Grandma about this photo". Amazon has the microphones, a physical microphone switch, the gift flow, unlimited photo storage for Prime members, people names in Amazon Photos, and a $114.99 price this week [sourced: FDM S1; BGR 2026-11-20]. Echo Show already answers "who is in this photo?" and "tell me more about this photo" [sourced: FDM S5]. What Amazon does not do today: ask, keep the elder's answer as a record, take photos from Google Photos, or play video [sourced-secondary: FDM S7]. Its own developer policy rejects add-ons that collect "private personal information via voice" [sourced: FDM S40c], which closes Echo Show to this product as a third party and says nothing about what Amazon builds itself. **This variant does not survive Amazon shipping the interview.** What would be left is neutrality (iPhone, Google Photos and paper prints, no Prime), which is the ground Aura already holds.

**Aura and Skylight.** Neither lists a microphone; Aura lists a speaker; Skylight's AI assistant is text, for the Calendar [sourced: FDM S13a, S14a]. Adding a microphone is a hardware revision for them and they have the capital (Aura $60M in 2025; Skylight's $75M facility) [sourced: FAM S1, S61]. A search on 2026-11-25 found no voice-recording announcement from either [sourced-secondary: one extended web search, 2026-11-25; absence of evidence only].

**AmivoFrame.** Ships the hardware idea today with the opposite policy: "We do not store audio recordings of your conversations", and family "can never access or read transcripts" [sourced: https://amivoframe.com/pages/privacy, read 2026-11-25]. It talks to the elder; it does not keep what the elder knows. Its traction signal is one app rating.

**ElliQ.** Already interviews its users for a "digital memoir" shared with family [sourced-secondary: https://blog.elliq.com/digital-memoir-feature, via search summary 2026-11-25], at $249 plus $59 a month, with 834 units in its flagship state programme [sourced: FDM S22, S24]. Prior art for the behaviour; not a gift at that price.

**Google and Apple.** Google ended third-party conversational actions on 2023-06-13 and has shipped no new Nest Hub since 2021 [sourced: FDM S41; sourced-secondary: FDM S11b]. Apple announced a 7-inch HomeView hub on 2026-10-13 at a reported $299; its photo features are [unknown] [sourced-secondary: FDM S10]. Neither is needed for the build and neither is the first threat.

**Storyworth and Remento.** Either could sell or co-brand a frame; Remento already sells a photo-anchored physical object.

**A microphone in a kitchen: the law.**
- *Visitors.* California Penal Code §632 punishes recording a "confidential communication" without the consent of all parties with a fine of up to $2,500 per violation, and §637.2 gives a private action for $5,000 per violation [sourced: https://california.public.law/codes/penal_code_section_632 and https://california.public.law/codes/penal_code_section_637.2, read 2026-11-25]. Between 9 and 13 states are counted as all-party, depending on the list [sourced-secondary: search summary of state-law guides, 2026-11-25]. Design response: no recording without a button press, a light and a spoken "recording" at the start, sessions that end on their own, and nothing kept unless the elder presses again. Whether an announced session in a private kitchen is still "confidential" for a visitor who walks in mid-session is untested for this kind of device [unknown: needs counsel].
- *Voiceprints.* Illinois BIPA and Texas CUBI name "voiceprint" [`research/face-regulation.md` Q1–Q2]. The product computes none: the speaker is assumed to be the frame's owner, never recognised. The Illinois class against Amazon is about Voice ID, the feature this design omits.
- *Washington.* The My Health My Data Act counts "voice recordings" from which an identifier template can be extracted as biometric data, treats that as consumer health data, requires consent by a clear affirmative act, and is enforceable privately through the Consumer Protection Act [sourced: RCW 19.373.010 and .090, `research/face-regulation.md` Q3]. The product's core object is a stored recording of a named person. "We extract no template" may not be an answer. Until counsel says otherwise, Washington is sold with a separate recorded consent from the elder, or not sold.
- *Children.* Grandchildren will speak near it. Amazon paid a $25 million civil penalty in 2023 over retained children's Alexa recordings [sourced: https://www.justice.gov/archives/opa/pr/amazon-agrees-injunctive-relief-and-25-million-civil-penalty-alleged-violations-childrens, via search summary 2026-11-25; FTC case page https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3128-amazoncom-alexa-us-v]. The product is sold to adults, records only in owner-started sessions, and gives the family a delete control per clip. That reduces the exposure; it does not remove it.
- *The elder's own consent.* The payer is not the person recorded. An elder with dementia may not be able to consent, and the share of recipients in that position is [unknown]. The second button press is the consent act; the frame can replay everything the family has received. AmivoFrame chose the opposite rule in the name of the elder's "dignity"; some buyers will agree with AmivoFrame.
- *The law that could close this:* a ruling that a stored voice recording of a named person is biometric data without any template (the Washington reading spreading), or a state extending all-party consent rules to announced in-home devices.

## Compounding asset

- **For the family:** each answered photo is a record that cannot be regenerated once the elder has died: who, where, when, in their voice, with the clip as evidence. It grows with every answer, and relatives' confirmations make it more reliable. This is the seed's asset in its smallest true form.
- **For the company:** weaker. Export is open by design, so lock-in is the object on the counter, not the data. Hardware sold once has no renewal. What accumulates is the contributor graph (about four adults per frame) and a record of which questions elders answer. Neither is a moat against Amazon.
- **Across families:** nothing links one family's archive to the next sale except the contributor seeing it work.
- Honest: the asset compounds for the customer and barely for the vendor. v3-gift had the same shape and scored 4 [`critiques/v3-gift-r3-investor.md`].

## Buildability (4-week demo spec for 2 engineers; ugliest technical risk; what is platform-, policy- or licence-gated)

**Demo, two engineers, four weeks, no custom hardware.**
- Week 1: Android app on a retail tablet in lock-task (kiosk) mode [sourced: https://developer.android.com/work/dpc/dedicated-devices/lock-task-mode, page title read 2026-11-25]: slideshow, large on-screen button, external USB or Bluetooth button. Browser uploader with the system photo picker and a front-and-back print capture.
- Week 2: question recording by relatives; press-to-record sessions with light and spoken notice; upload; speech-to-text with the family name list as a hint; record extraction with clip timestamps.
- Week 3: one-tap confirm and tap-the-face screen for relatives; archive with XMP and audio export; MCP endpoint; one live spoken follow-up through a hosted voice model.
- Week 4: ten households with a parent aged 75+ [estimated: design choice], tablets posted to them. Measure: frames with at least one answer in week one; answered photos per frame per week; share of spoken first names transcribed correctly before correction; share of answers a relative had to fix.
- Kill criteria for the demo: fewer than half of elders answer anything unprompted by a visit; or first names are right less than 70% of the time with the hint list [estimated: thresholds are design choices].

**Ugliest technical risk: hearing and being heard.** A quiet 85-year-old voice at one to two metres from a tablet microphone, with a television on, transcribed for proper names. The inputs are bad on both sides: 55% of people 75+ have disabling hearing loss; word error on older speech was 33.3% untuned and 16.5% tuned in the one figure found [sourced: NIDCD; sourced-secondary: FDM S31]. A four-microphone voice processor costs $11.95 at 416 units, chip only [sourced-secondary: FDM S36]; a tablet has nothing like it. The demo may fail for an acoustic reason the real device would fix, and nobody will know which.

**Second risk: the elder never presses the button.** Not technical, and decisive.

**Gated.** Nothing in the demo is gated by Apple, Google or Amazon. The own-brand device is gated by: FCC certification; an ODM willing to add a microphone array at a first-order quantity (minimums for that are [unknown]; plain Frameo frames list from 1 to 100 units [sourced-secondary: FDM S34]); the duty rate; and Amazon as both the main channel and a competitor. Frameo's software licence does not help: its licensees' frames list no microphones and the fee is unpublished [sourced: FDM S33a; FDM Q3]. Echo Show and Nest displays are closed to this product by policy [sourced: FDM S40c, S41].

**Regression against `variants/current.md`:** Buildability of the demo is equal or better (no Photos database, no Takeout). Buildability of the business is worse: it needs tooling, certification, inventory and a Q4.

## Ceiling (path to $100M ARR with tagged inputs and arithmetic; or the honest number it tops out at)

**First, "ARR" is the wrong word.** A frame is sold once. The recurring line below is 0.6–4.3% of revenue in every case [estimated: plan row ÷ total row of the table].

**Pool: branded Wi-Fi gift frames sold in the US per year.** No count exists. Market reports found on 2026-11-25 put the global category anywhere from $9.41 million to $55.16 billion and are unusable [sourced-secondary: search summary of Valuates and Mordor pages, 2026-11-25; low quality]. Built from company figures instead:
- Aura: 997,000 frames by 2022-11-22 and "single-digit millions" by 2025-10-21 [sourced: FAM S3, S1] → 0.34M to 2.74M a year over those 2.92 years [estimated: (2.0M − 0.997M) ÷ 2.92; (9.0M − 0.997M) ÷ 2.92; the 2.0M floor reads "millions" as at least two].
- Skylight: $75M in 2021 [sourced-secondary: FAM S8] → about 0.63M devices at a $120 average [estimated: 75M ÷ 120; the average is an assumption between its $109.99 sale and $139.99 list prices; includes Calendars, so it overstates frames then and understates the company now].
- Nixplay: $20.0M in 2023 [sourced: FAM S14] → about 0.20M at $100 [estimated: 20.04M ÷ 100; $99 Amazon price, FDM S4].
- **Pool: 1.17M to 3.57M a year, 2.0M used as the centre** [estimated: 0.34 + 0.63 + 0.20; 2.74 + 0.63 + 0.20; the centre is a round number inside the band, not a measurement]. Excluded: generic Frameo frames (a promotional post claims 1,000,046 units worldwide in 2020 [sourced-secondary: FDM S33c]) and Amazon's own.

**Reachable share in year five** [estimated: by precedent, stated per case].
- Low, 0.5%: a small brand that exists. AmivoFrame, eight months after its store listing was published (2026-03-27), has one app rating [sourced: amivoframe.com/products.json; iTunes Search API, 2026-11-25].
- Centre, 2%: 40,000 frames, about $6M, roughly Skylight between its third and fourth years ($2M in 2018, $30M in 2019 [sourced-secondary: FAM S8]).
- High, 5%: 178,500 frames a year, slightly above Aura's average over its first six years (about 163,000 a year [estimated: 997,000 ÷ 6.1 years from its autumn-2016 launch to 2022-11-22]), which took about $13M of equity before 2022 [sourced: FAM S3, 2022-11-22].

**Price:** $149 realised [sourced comparable: Aura Carver list, FAM S4].

| | Low | Centre | High |
|---|---|---|---|
| Pool × share = frames a year | 1.17M × 0.5% = 5,850 | 2.0M × 2% = 40,000 | 3.57M × 5% = 178,500 |
| Frames × $149 | $0.87M | $5.96M | $26.60M |
| Books: 5% / 10% / 20% of that year's frames × $69 | $0.02M | $0.28M | $2.46M |
| Plan: installed base (2.5 × year-five frames) × 1.2% / 5% / 10% × $29 | $0.005M | $0.15M | $1.29M |
| **Year-five revenue** | **$0.90M** | **$6.38M** | **$30.35M** |

All rows [estimated: arithmetic on the inputs above; book and plan rates are assumptions except the 1.2%, which is Nixplay's; the 2.5 multiple assumes a straight-line ramp over five years less attrition].

**Sensitivity.** One point of share at the central pool is 20,000 frames, or $2.98M [estimated: 2.0M × 0.01 × 149]. A $30 lower realised price, which is where Skylight and Amazon are this week, cuts every frame line by 20% [estimated: 30 ÷ 149]. A critic taking the research-supported end of each input (1.17M pool, 1% share, $109.99) gets $1.3M [estimated: 1.17M × 0.01 × 109.99], and nothing in the research contradicts that.

**$100M.** 671,000 frames a year at $149 [estimated: FDM row 24]: 19% of the largest pool, 34% of the central one, 57% of the smallest [estimated: 0.671 ÷ 3.57; ÷ 2.0; ÷ 1.17]. That is a company the size of Aura's frame business or larger, built against Amazon, on tens of millions of inventory finance. It does not pencil from a seed round.

**Largest sourced revenue of any comparable.** Filed: Nixplay, $57.9M in FY2021, then down 65% to $20.0M by FY2023, loss-making [sourced: FAM S13, S14]. Claimed and unaudited: Skylight "$300M+" and "more than $500 million", covering Frame, Calendar and Buddy with no split [sourced: FAM S9; sourced-secondary: FAM S10]. Aura: [unknown]. Elder devices: none above $10M [sourced: FDM Q2]. A frame that talks: [unknown]; one app rating.

**Software only.** Three routes, none evidenced:
- A licence to frame brands. Frameo's model is a one-time fee per unit of undisclosed size across 350 brands [sourced: FDM S33a]. At an assumed $1–3 per unit on 5–20% of a Frameo-scale 1.0M units, $0.05–0.6M a year [estimated: 50,000 × 1; 200,000 × 3; the fee is an assumption because no licence price is public]. Those frames have no microphone, so the ODM must change the hardware first.
- An app that turns an old tablet into the frame. Fotoo has 1M+ downloads; visible prices in that niche are $0–10 once [sourced: FDM S33b; sourced-secondary: FDM S33d]. At 2% of a million downloads paying $10, $0.2M in total, not per year [estimated: 1,000,000 × 0.02 × 10; the 2% is an assumption].
- A feature licensed to Aura, Skylight or a memoir company. No source shows a frame maker licensing a feature [unknown: FDM plain statement].
- **Software-only honest number: $0.1–1M a year** [estimated: the first two routes above; the third is unpriced]. It is a feature.

**Honest number for the whole variant: $1–30M of year-five revenue, about $6M at the centre, at a 24–40% contribution margin, almost none of it recurring** [estimated: table above; Economics table]. On the scorecard's calibration that is Ceiling 2–3, the same as the leader, with more capital at risk.

## Load-bearing assumptions (numbered; each with the observable fact that would falsify it)

Every threshold in this list is a design choice [estimated: set by the author, not measured]; the benchmarks they lean on are tagged where they first appear above.

1. **A frame on the counter gets answers that a phone link did not.** Falsified if, in a 50-household pilot with a parent aged 75+, the median frame has fewer than one answered photo a week in weeks five to eight, or fewer than half the frames reach ten confirmed photos in eight weeks.
2. **A relative's recorded question pulls better than a machine prompt.** Falsified if answer rates on relative-asked and frame-asked photos in the same pilot differ by less than a quarter.
3. **Spoken first names survive older voices and kitchen acoustics well enough for one-tap confirmation.** Falsified if fewer than 70% of spoken names are correct with the hint list on the tablet build, and a four-microphone test rig does not lift that above 85%.
4. **Amazon does not ship an elder-facing "tell me about this photo" prompt with saved answers within twelve months.** Falsified by an Amazon devices post or an Alexa Photo Frame release note describing on-frame recording with prompts. The reviewer's report says half of this is already planned.
5. **Aura and Skylight do not ship a microphone-equipped frame within eighteen months.** Falsified by a product page listing one.
6. **Buyers accept a microphone in a parent's kitchen when it is button-only.** Falsified if more than a third of pilot invitations are declined for that stated reason, or return rates on the first run exceed the 17% holiday benchmark by half.
7. **The elder's second press is valid consent and visitors are covered by the announcement.** Falsified by counsel's opinion on California §632 and Washington RCW 19.373, or by any ruling treating a stored voice recording of a named person as biometric data without a template.
8. **A microphone-equipped frame lands at or below $70 all-in at a 5,000-unit order.** Falsified by three ODM quotes above that.
9. **Half or more of units can be sold without paid acquisition.** Falsified if, on the first run, the contributor loop plus organic search produce fewer than one further sale per four frames in six months.
10. **Heavy users can be capped without feeling tricked.** Falsified if more than 10% of support contacts in the first run are about the follow-up limit, or any review uses the words Nixplay's customers used.
11. **The first run can be financed and sold before the next Q4.** Falsified if tooling plus certification plus 5,000 units exceeds $0.5M, or the ODM lead time misses September.
12. **The ceiling is accepted as about $6M unless a frame maker or Amazon is the route to market.** Falsified upward only by a signed licence or supply agreement with a brand selling more than 500,000 frames a year.

## Relationship to variants/current.md (what is kept from the organizer workbench and the index-only engine; what is dropped)

**Kept.**
- *Naming is a prompted human act.* The workbench's client-review screen becomes an object in the kitchen of the one relative who knows the answers. Names are spoken and then confirmed by a second person. No face template exists anywhere in the system [`variants/current.md` round-2 and round-3 merge notes].
- *Evidence-linked, human-confirmed metadata.* Every field carries the clip, the second, and who confirmed it. This is the per-item provenance ledger applied to identity.
- *Index, not storage.* Originals stay where they live; the archive holds display-size copies, records and audio (under 1 GB a frame [estimated: 2,000 photos × 300 KB + 468 minutes × 0.48 MB]).
- *Queryable by AI.* The MCP endpoint and XMP export from the workbench's deliver step.
- *No subscription on the artifact.* The round-3 note, taken literally.
- *The organizer channel,* as installers: an organizer's scans go to the frame, and the answers come back into the organizer's project.

**Dropped.** The Mac workbench, Takeout repair, deduplication, seat and per-project pricing, and the B2B payer. Whole-library indexing: the seed's "corpus indexed where it lives" shrinks to the few hundred photos an elder can speak about. A phone-side selector that uses an on-device index to find photos of unknown people is deferred, because it would bring back the long indexing session [`research/ios-feasibility.md` Q3].

**What regresses, stated plainly.** Economics: 24–40% contribution against the workbench's ~87% [estimated: Economics table here; `variants/current.md` Economics]. Capital: inventory and a Q4, against none. Platform risk: Amazon shipped the adjacent device four weeks ago [estimated: 2026-11-25 − 2026-10-28]. **What improves:** Pain and Wedge (the payer already buys this object, by the million), and the asset (the one thing in fifteen variants that a model cannot regenerate and a platform does not already hold). **Ceiling does not improve.**

**If this variant has a future, it is as a feature with a partner:** the interview-and-record loop licensed to, or built with, a frame maker that already has the inventory finance and the shelf. Nothing in the research shows such a deal exists.

## Evidence pointers (file:section for every claim above)

- Amazon Alexa Photo Frame, Echo Show photo prompts, prices, purchase badges, Alexa+ policy, Google sunset, Apple HomeView: `research/frame-device-market.md` Q1, Q5, rows 1–5, 23; re-read for this file: https://www.aboutamazon.com/news/devices/amazon-alexa-photo-frame (2026-10-28) and https://www.bgr.com/2322517/alexa-photo-frame-review/ (2026-11-20).
- Elder devices (ElliQ, GrandPad, ViewClix, Komp, JubileeTV, Claris), usage studies, speech-recognition error, smart-speaker ownership: `research/frame-device-market.md` Q2, Q7, rows 8–16.
- Supply side, landed cost, duty, certification, microphone chip, Frameo licensing, crowdfunding, capital precedents, returns, Amazon fees, retail terms: `research/frame-device-market.md` Q3, Q4, Q6, rows 17–25, and its plain statement.
- Aura, Skylight and Nixplay units, revenue, margins, funding, prices, plans, the Nixplay suit, channel shares, seasonality: `research/family-artifact-market.md` Q1, Q7, rows 1–14.
- Grandparent counts, device ownership, contact channels: `research/family-artifact-market.md` Q5; `research/sizing.md` Q2, rows 22–24.
- Memoir category prices, completion proxy, Storyworth Voice, Remento ornament, voice-model prices per minute, studies of older adults and AI voice: `research/memoir-gift-market.md` Q1, Q2, Q4, Q5, Q8.
- Why phone interviews failed: `critiques/v3-gift-r3-investor.md`, `-customer.md`, `-builder.md` (most damaging objections).
- Acquisition cost anchors: `research/sizing.md` Q4. Storage price and retention regimes: `research/unit-economics.md` Q6–Q7.
- Biometric law, voiceprint definitions, Washington My Health My Data Act: `research/face-regulation.md` Q1–Q3, risk table; `research/unknowns-r1.md` Q8.
- Prints front and back; self-serve tagging at 0.10 per scan [sourced: Photomyne filing via the file cited]: `research/digitization-market.md` Q3, Q5, Q6.
- MCP as a commodity; phone-side indexing limits: `research/byo-ai.md` Q5; `research/ios-feasibility.md` Q1–Q4.
- Fetched for this file on 2026-11-25: https://amivoframe.com/ , https://amivoframe.com/products.json , https://amivoframe.com/products/amivoframe-smart-digital-photo-frame , https://amivoframe.com/pages/privacy ; AmivoFrame announcement, GlobeNewswire paid placement dated 2026-07-08, read at https://pr.dailyastorian.com/article/AmivoFrame-Introduces-a-Smart-Digital-Photo-Frame-for-Parents-and-Grandparents/6a4e3ca21f33de42266d6e22 ; iTunes Search API for "amivoframe"; https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing ; https://california.public.law/codes/penal_code_section_632 and `_637.2`; https://developer.android.com/work/dpc/dedicated-devices/lock-task-mode (title only; body did not render).
- Known only through search summaries on 2026-11-25 (secondary): the Illinois class certification against Amazon (Duane Morris, 2025-11-26); the 2023 Amazon Alexa children's-recordings penalty (justice.gov and ftc.gov pages returned empty or 404 to direct fetch); ElliQ's memoir feature (blog.elliq.com); counts of all-party-consent states; market-report sizes; a 2025 retail tablet price.
- Not resolved: US frame units per year; any frame maker's acquisition cost or return rate; ODM minimums and price for a microphone-equipped frame; tooling and safety-certification cost; book print cost; the number of US adults aged 70–90 with home Wi-Fi; dementia prevalence among frame recipients; whether a classic Alexa skill can capture long free speech; Amazon's date for on-frame recording; Amazon search pages (blocked to this client on 2026-11-25, so AmivoFrame's Amazon presence is unchecked). `research/contents-claims.md` was absent when this file was finished and is not needed for it.
