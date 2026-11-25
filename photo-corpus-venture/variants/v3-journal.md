# v3-journal — The family journal: printed monthly from every relative's phone

Written 2026-11-24 for round 3. Research read: `research/family-artifact-market.md` (R13), `research/institutional-legacy.md` (R14), `research/memoir-gift-market.md` (R12), plus the round 0–2 files named in the pointers. Web checks made today are tagged with their URL and "2026-11-24". Convention: GM % = contribution ÷ sticker price, payment fees counted as cost (same as `research/unit-economics.md` Q7).

**Stated up front:** the research does not support a nine-figure outcome for this variant. R13's own verdict is "a €2–15M business in a decade, with thin gross margin" for a printed-journal venture. This file argues the best honest version of the idea, shows where two inputs are better than R13 assumed (postage and US price), and lands at $4–16M ARR, not $100M.

## One line

Adult children pay about $12 a month for a 24-page printed journal mailed to a grandparent; each relative's phone proposes that month's photos on-device, the relative approves with a tap and speaks a caption, the grandparent answers by phone from a number printed on the back page, and every approved photo, caption and reply accumulates into a named, dated, narrated family archive that no face template was needed to build.

## Customer (payer, user, audience; how many [tagged]; what they do today; what they pay today)

**Payer.** An adult child aged ~30–55, usually a parent of young children. Pool indicator: a quarter of US adults have a living parent 65+ and a minor or supported child, about 67M adults [sourced: Pew 2026-08-27 via research/sizing.md Q2 and row 22; count estimated there]. How many are one-per-family organisers: [unknown].

**Recipient.** A grandparent aged ~70+. About 65M US grandparents of all ages [sourced: AARP 2026-06-16 via sizing.md row 24]; ~41M aged 65+ [estimated: 2/3 × 61.2M, Pew 2026-09-09 and Census via sizing.md row 24]. Sub-pools where paper has an edge over a screen:
- 29% of grandparents have a grandchild 500+ miles away [sourced: AARP June 2026, n=3,283, via family-artifact-market.md Q5] → ~12M of the 65+ pool [estimated: 0.29 × 41M; the AARP share is for all grandparents, applied to 65+ as an assumption].
- 21% of 65+ do not own a smartphone [estimated: 100 − 79, Pew 2026 via family-artifact-market.md Q7] → ~8.6M grandparents 65+ [estimated: 0.21 × 41M]. Smartphone ownership at 75+ in 2026: [unknown; Pew publishes only 65+].
- Home broadband among 65+ (a frame needs Wi-Fi, not a smartphone): [unknown at source]; two secondary summaries of Pew give 64% and 70% and disagree [sourced-secondary: search 2026-11-24; the Pew page https://www.pewresearch.org/short-reads/2026/01/08/internet-use-smartphone-ownership-digital-divides-in-u-s/ was fetched and shows no 65+ broadband figure in its text].
- Assisted-living and nursing-home residents: 2,256,424 [estimated: 1,016,424 + 1,240,000; NCAL June 2026 and KFF July 2025 via institutional-legacy.md Q1, Q8].

**Contributors.** Siblings, cousins, grandchildren. At Famileo, about 7 app users per subscribed family [estimated: "près de deux millions d'utilisateurs" ÷ 280,000 families; family-artifact-market.md Q2].

**What they do today.** Grandparents 65+ keep in touch in person 60%, by phone 55%, text 46%, video call 34%, social media 13%; mail is not among the listed channels [sourced: AARP June 2026 via family-artifact-market.md Q5]. Families buy a Wi-Fi frame once, or post to a private feed (FamilyAlbum: 30M registered, 20% in North America [sourced: MIXI 2026-05-07 via research/grandparent-loop.md Q1]), or text photos.

**What they pay today.**
- Frames, one time, no subscription: Frameo-based frames from $59.48; Aura $149–499; Skylight Frame ~$140 [sourced and sourced-secondary: family-artifact-market.md Q1, numbers rows 2, 14].
- Printed journals: Famileo US $9.99 / $11.99 / $13.99 per month, after a $2 rise citing postage and paper; France €5.99–7.99 [sourced: famileo.com via family-artifact-market.md Q2]. Hug Letters $14.99/month, 30 photos, mailed every 4 weeks [sourced: https://www.hugletters.com/, 2026-11-24]. The Family Press $16.95/month [sourced: family-artifact-market.md Q2]. Lineage (US, founded 2026) $24.99/month billed annually or $29.99 monthly [sourced-secondary: search extract of https://lineagepost.com/, 2026-11-24]; "First journal from $14.95" [sourced: lineagepost.com meta description, 2026-11-24]. FamilyPost (Netherlands, 12 languages) from €7.99/month, worldwide shipping included [sourced: https://getfamilypost.com/, 2026-11-24]. NanaGram mails 3 to 25 prints for $8.99–24.99/month [sourced: https://nanagram.co/, 2026-11-24].
- Gift budgets: Mother's Day 2026 $284.25 per person; Father's Day 2026 $226.58; 45% of Father's Day shoppers interested in a subscription box [sourced: NRF via memoir-gift-market.md Q6]. Grandparent-directed photo-gift spend: [unknown].

## Wedge (first use case adopted without changing habits; the first 10 minutes for the payer and for the elder/resident; day-1 value; day-30 value)

**No migration, no library upload.** The payer already takes the photos; the grandparent already opens the mail. The new acts are one app install, one photo-permission prompt and one address.

**First 10 minutes, payer.**
1. Install, type the grandparent's name and postal address.
2. Grant photo access. The app scores only the last ~45 days on the phone: Apple's Vision aesthetics request (iOS 18+) [sourced: research/memory-product-sdk.md Q3], screenshots and documents excluded, near-duplicates collapsed, face *detection* (a count of faces, no embedding) used as a "people are in it" signal. A month is a few hundred photos; at the 76 ms/image central figure that is under a minute in the foreground [estimated: 500 × 76 ms = 38 s; research/ios-feasibility.md Q3], so the 30,000-photo wall-clock and the background-entitlement problem (ios-feasibility.md Q2) do not arise.
3. Twelve proposals appear. Tap to approve, swipe to swap, hold to speak a caption ("Mia's first soccer game"). Only approved images leave the phone, resized for print.
4. Send the family link by text. A relative who will not install anything opens the link, which invokes the system photo picker in the browser, or texts or emails photos to the family's number (NanaGram's international plans are "powered by email" [sourced: nanagram.co, 2026-11-24]).
5. Pay by card or Apple Pay. The first issue goes to print within 48 hours instead of waiting for month end; the payer sees the PDF proof immediately.

**First 10 minutes, elder.** An envelope arrives. Nothing to install, charge or log into. The back page prints one phone number and a QR code: "Call and tell us about any photo." A landline works. The call is recorded, transcribed and posted to the family; next month's issue prints it as "Grandma says". Each issue also carries one older photo with a question ("Who is this, and when?"), which is the archive's naming step done by a prompted human (the round-2 lesson: 0.10 tags per scan when naming is self-serve [research/digitization-market.md Q6]).

**Day-1 value.** Payer: a proof of issue 1 and one obligation discharged. Honest limit: the elder's value starts on day ~5–7, when paper arrives [estimated: assumption, 48 h to print plus First-Class delivery; not measured].

**Day-30 value.** A push on the 25th: "November is ready: approve 9 photos." Issue 2 carries the grandparent's replies. The family has a private feed of ~25 approved, captioned photos per month and the first voice clips. If nobody approves anything, nothing unapproved is ever printed; the issue is filled from the archive page, replies and birthdays.

**Honest gap.** "Nobody has to make it" is a slogan; someone still taps approve. Whether selection effort is what makes journal subscribers quit is [unknown]: Famileo names paper and postage, Neveo names acquisition cost, and 40% of Chatbooks cancellation reasons "had nothing to do with the product" [sourced and sourced-secondary: family-artifact-market.md Q2, Q4].

## Why now (dated changes since 2024, each tagged)

1. **2024-09, iOS 18:** Vision's image-aesthetics request gives any app free on-device photo scoring [sourced: developer.apple.com via memory-product-sdk.md Q3]. It makes selection cheap for us and for every incumbent.
2. **2025-03-31:** Google removed third-party read of Google Photos libraries; a journal cannot pull a relative's photos server-side, so collection has to happen on the phone or through a picker [sourced: research/platform-access.md Q4; assumption A1 holds].
3. **2025-03 to 2025-04:** Nixplay moved sync behind a paywall and was sued on 2025-04-22; ~1.2% of its users pay [sourced/estimated: family-artifact-market.md Q1]. Aura sells on "No subscription fees" and was profitable in 2024 [sourced: same]. Recurring revenue from the screen is rejected; a consumable is the only recurring artifact in this job.
4. **2025–2026:** Famileo reached 280,000 families and €15.3M (2025), growing ~9%, and is live in the US with a senior-living offer from $99/month per community [sourced and sourced-secondary: family-artifact-market.md Q2].
5. **2026:** new entrants are seeding the category: FamilyPost's app was released 2026-04-30, has 32 ratings on the Dutch store and 0 on the US store, and its landing page notes that "Paid ad clicks land on this page" [sourced: iTunes lookup id 6760652389 and getfamilypost.com source, 2026-11-24]; Lineage lists a 2026 founding [sourced-secondary: search 2026-11-24]. This is also evidence of crowding.
6. **2026:** phone voice agents cost $0.05/min (GPT-Live) and Storyworth's "Magic Interviews" already works on a landline [sourced: memoir-gift-market.md Q5, bottom line 3], so a reply line an 85-year-old can use costs cents.
7. **2026-06:** AARP counts ~65M grandparents spending $2,654 a year on grandchildren [sourced: family-artifact-market.md Q5].
8. **Counter-signals.** USPS prices effective 2026-10-04 put a 3 oz retail flat at $2.27 [sourced: https://pe.usps.com/text/dmm300/Notice123.htm, 2026-11-24]; Famileo raised US prices for that reason. Chatbooks' designer reports 150K subscriptions cancelled in 2025 [sourced-secondary: family-artifact-market.md Q2]. Famileo's first gazette was in 2015 [sourced: family-artifact-market.md Q2]: most of this could have been built then. What is new is on-device proposal, the voice reply and the archive behind it.

## Product (core loop; explicitly NOT in v1)

**Core loop, monthly.**
1. **Propose (on device).** Each contributor's phone ranks its own last-month photos; originals never leave the phone. Index-only engine from `variants/current.md`, shrunk to one month and with no face embeddings.
2. **Approve and caption.** One tap per photo; caption by voice, transcribed on device. Names enter the archive as words a relative said or typed.
3. **Assemble.** Server lays out a 24-page digest-size (5.5 × 8.5 in) booklet, large type, one "from the archive" page, one page of the grandparent's replies, birthdays.
4. **Print and mail.** Variable-data digital print, enveloped, First-Class.
5. **Reply.** Phone number and QR on the back page; voice in, transcript and audio out to the family; optional follow-up question from a voice agent.
6. **Accumulate.** Approved photos (a few hundred per family-year), captions, replies and dates form the archive: exportable as files with XMP captions, queryable through an MCP endpoint (works on Claude Free today; other assistants are gated [research/byo-ai.md §3]). An annual bound volume is offered each December and a memorial edition when a recipient dies (the tribute-pack module in current.md).

**Explicitly NOT in v1.** Face recognition or any face template; whole-library indexing or search; storing anything not approved for print; an Android app (Android relatives use the link and picker); frames or other hardware; a care-home dashboard; AI-written text (the words are the family's; AI only cleans transcripts); memoir interviews; international shipping.

## Business model and pricing (with comparables, tagged)

- **Journal: $11.99/month or $119/year, one recipient address** [estimated: set at Famileo's US middle tier $11.99; below Hug Letters $14.99, The Family Press $16.95 and Lineage $24.99–29.99; sources in Customer]. At the brief's $8 floor GM falls to 40% (Economics).
- **Large-format edition (8.5 × 11): $15.99/month** [estimated: digest price plus the $1.46 postage difference between a commercial flat and a commercial letter, rounded up; Notice 123].
- **Second address, same journal: +$6/month** [estimated: assumption; FamilyPost charges its full plan price, €7.99–14.99, per extra address (getfamilypost.com, 2026-11-24)].
- **First issue $4.95** [estimated: matches Neveo's €4.95 and The Family Press's $4.95 first-issue offers; family-artifact-market.md Q2].
- **Family kitty:** contributors split the bill, as at Famileo and FamilyPost [sourced: same].
- **Annual bound volume: $49** [estimated: assumption; Chatbooks hardcover $24 per monthly book (memory-product-sdk.md Q7), Storyworth $99 including one book (memoir-gift-market.md)].
- **Payment outside in-app purchase.** A printed journal is a physical good: "you must use purchase methods other than in-app purchase" [sourced: App Store Review Guideline 3.1.3(e), https://developer.apple.com/app-store/review/guidelines/, 2026-11-24]. No 15–30% platform fee.
- **Senior living:** free to the community in v1; families pay. Famileo's home-pays model makes the family's paid plan free when the grandparent moves in, a structural leak [sourced/inference: family-artifact-market.md Q2].

## Distribution (non-paid channels with evidence; one paid channel with CAC math if any)

**Non-paid.**
1. **Contributor loop.** "70% of subscriptions from word of mouth" at Famileo [sourced: Bpifrance portrait via family-artifact-market.md Q2]. Every journal has ~7 contributors [estimated above], many with a second set of parents. Conversion of contributors into payers for another grandparent: [unknown; no operator discloses it].
2. **The artifact on the table.** Each issue's back page carries a start code. Evidence it spreads is vendor anecdote only [FamilyPost founder copy, getfamilypost.com].
3. **Gift moments.** December, Mother's Day, Father's Day and Grandparents Day; gift checkout with a scheduled first issue. Frame sales show the season: Nixplay reports "significantly stronger sales in our third and fourth fiscal quarters" [sourced: SEC filing via family-artifact-market.md Q1].
4. **Senior living as a seed channel.** Famileo began in care homes and has 2,700 partner establishments [sourced: family-artifact-market.md Q2]. US base: 41,465 assisted-living communities, ~17,830 with 26+ units [sourced/estimated: institutional-legacy.md Q1]. Offer: a free page for the community's calendar inside each resident's family journal and a code card at move-in. Reality: 6–8 months to a pilot (single anecdote), staff turnover 34.5–71.9%, LifeLoop in 4,700+ communities already mails photo postcards, and no US operator has announced Famileo [sourced-secondary: institutional-legacy.md Q2, Q5; family-artifact-market.md Q5].
5. **Photo organizers** (the current.md channel) offer the journal at project hand-off and supply scanned prints for the archive page. About 700 members; a trickle [research/pro-channel.md Q1].

**One paid channel: Meta gift ads with the $4.95 first issue.** Neveo says social ads are "très chers" and its main channel [sourced: family-artifact-market.md Q2]. No journal CAC is published [unknown]. Anchors: Qeepsake $35; Tinybeans $19–100; derived paid-UA cost for a photo subscription $65–90 [sourced/estimated: sizing.md Q4; grandparent-loop.md Q5]. Contribution $7.07/month (Economics) → payback 5.0 months at $35, 9.2 at $65, 12.7 at $90 [estimated: CAC ÷ 7.07]. Subscriber life is [unknown]; at a 3:1 LTV:CAC rule the maximum CAC is $19 for an 8-month life, $42 for 18 months, $85 for 36 months [estimated: life × 7.07 ÷ 3]. Paid acquisition works only if the median life is at least ~18 months and CAC is at or below Qeepsake's.

## Economics (per-customer COGS including print, postage and voice minutes where relevant; GM; payback; cite research rows or derive with tags)

**Format decides postage.** R13 costed an 8.5 × 11 journal as a First-Class flat at $2.27–2.56. A 5.5 × 8.5 booklet in a 6 × 9 envelope is a letter: not more than 11-1/2 in long, 6-1/8 in high, 1/4 in thick, and up to 3.5 oz [sourced: https://pe.usps.com/text/dmm300/201.htm, 2026-11-24]. Weight ≈ 1.8 oz [estimated: 6 letter sheets × 0.0603 m² × 118 gsm = 43 g, plus ~7 g envelope (assumption)]. Prices effective 2026-10-04 [sourced: Notice 123, 2026-11-24]: metered single-piece letter, 2 oz, $1.07; commercial automation letter, one price up to 3.5 oz, $0.621 (5-digit), $0.672 (3-digit), $0.707 (mixed); commercial automation flat, 3 oz, mixed, $2.165. Commercial letter prices need "a single mailing of at least 500 pieces" [sourced: https://pe.usps.com/text/dmm300/233.htm, 2026-11-24]. Whether a stapled booklet in an envelope passes as automation-compatible: [unknown; needs a USPS mailpiece design review].

**Print.** Public single-copy prices: Blurb $7.00 for a 20-page 8.5 × 11 magazine [sourced: family-artifact-market.md Q3]; "$3–5 for one copy" of a 24-page 5.5 × 8.5 booklet and "under $1.50 at 500+" identical copies [sourced-secondary: search extract of https://yourbookpress.com/saddle-stitch-book-printing, 2026-11-24]; $1.72 each at 100 identical copies [sourced-secondary: search extract of https://www.55printing.com/booklets/, 2026-11-24]. Contract price for booklets that are each unique: [unknown; needs an RFQ, as R13 unknown 5 says]. Scenario input $2.50, bracket $1.50–3.50 [estimated: assumption between the static-run and single-copy list prices].

| Per subscriber-month, $11.99 monthly plan | At scale (≥500 pieces per mailing) | Pilot (<500) | Tag |
|---|---|---|---|
| Print, 24 pp digest | $2.50 | $4.00 | [estimated: assumption; midpoint of $3–5] |
| Envelope, inserting | $0.25 | $0.25 | [estimated: assumption] |
| Postage | $0.71 | $1.07 | [sourced: Notice 123] |
| Card fee | $0.65 | $0.65 | [estimated: 2.9% × 11.99 + 0.30; Stripe via unit-economics.md Q7] |
| Voice reply, 5 min | $0.30 | $0.30 | [estimated: 5 × $0.05 GPT-Live + 5 × ($0.0085 + $0.0025) Twilio; memoir-gift-market.md Q5] |
| Storage of approved photos | $0.04 | $0.04 | [estimated: 25 photos × 3 MB × 36 months = 2.7 GB × $0.015 R2; unit-economics.md Q1] |
| Reprints, lost mail (2%) | $0.07 | $0.11 | [estimated: assumption 2% × print + envelope + postage] |
| Support | $0.40 | $0.40 | [estimated: assumption] |
| **COGS** | **$4.92** | **$6.82** | [estimated: sum] |
| **Contribution; GM** | **$7.07; 59%** | **$5.17; 43%** | [estimated] |

- Sensitivity: print at $1.50 → GM 67%; at $3.50 → 50%. Annual plan ($9.92/month, card fee $0.31) → GM 54%. At $9.99 monthly → 51%; at $8 → 40% [estimated: same table, price and fee changed]. Large format mailed as a flat without a price rise → 47% before any extra print cost [estimated: + $1.46 postage].
- Checks against operators: R13's scenario was 46% at $9.99 with flat postage; Famileo says "On marge peu"; PlanetArt (FreePrints) reports 44.2% gross margin and Nixplay 37% [sourced: family-artifact-market.md Q1–Q3; Crowe HAF report 2025-05-21, https://www.claranova.com/wp-content/uploads/2025/06/2025_05_21_Report-independent-Expert_Crowe-HAF_ENG.pdf, fetched 2026-11-24]. The 59% rests on two unverified inputs, the contract print price and letter-rate eligibility.
- First issue at $4.95: about break-even at scale, a loss of ~$1.7 at pilot cost [estimated: 4.95 − (COGS − 0.65 + 0.44 card fee)].
- Storage never becomes the cost: ~0.9 GB per family-year [estimated: 25 × 3 MB × 12].
- Retention: [unknown]. Regimes on record: self-purchased print subscriptions cancel heavily (Chatbooks 66–86% of subscription orders [sourced-secondary: one employee's case study, family-artifact-market.md Q2]); the two gift-to-a-third-party journals have grown for ten years but publish no churn (a French-language search today found none [unknown]). A floor exists that no product fixes: recipients are 70+ and die or move into care; annual rate for this base [unknown; SSA life table not reachable from this session].
- What breaks at scale: print quality control, address hygiene (USPS Move Update is required for presort [DMM 233]) and December peaks.

## Platform and incumbent risk (the obvious feature Apple/Google or the category leader could ship; why this survives or doesn't)

- **FamilyAlbum is the kill slide.** It already holds every relative's uploads, builds a monthly book from last month's photos at $7.99 and offers copies for grandparents [sourced-secondary: family-artifact-market.md Q4, Q6; search extract of blog.family-album.com, 2026-11-24]. "Mail it to Grandma every month" is one release for a team that shipped 12 releases between June and November 2026 [grandparent-loop.md Q1]. This variant has no defence beyond focus on the elder's reply loop and on multi-household families.
- **Famileo or FamilyPost add "suggested from your camera roll".** FamilyPost already fills date and place "automatically from your photo" and sells an AI writing assistant [sourced: getfamilypost.com, 2026-11-24]. R13 Q4: automatic selection has been table stakes in single-user print since 2015; proposals across several relatives' phones were not found in any shipping product. A lead of months, not a moat.
- **Frames are the substitute at a one-time price** ($59 and up, no subscription). Paper keeps homes without Wi-Fi, residents of care settings and people who will not use a screen; the size of that residue is [unknown] (Customer).
- **Apple.** Guideline 5.1.1(iii): "Where possible, use the out-of-process picker or a share sheet rather than requesting full access to protected resources like Photos" [sourced: App Store Review Guidelines, 2026-11-24]. Proposal needs full-library read. How App Review treats this purpose is [unknown]; the share of users who grant full rather than limited access is [unknown; no published figure found, search 2026-11-24]. Fallbacks, in order: limited-library selection; the system picker with our ranking applied to whatever the user picks; a share-sheet extension from Photos; text or email in. Under any fallback the product is Famileo with nicer captions. If Apple adds suggested ordering to the picker, every competitor gets proposal for free.
- **Google Play** allows broad photo access only when "core functionality revolves around broad access to Photos and Videos" and requires a declaration [sourced: platform-access.md Q8]; hence Android is link-and-picker in v1.
- **Google Photos Premium Print Series** is alive at $6.99 for 10 prints to oneself [family-artifact-market.md Q6]; Shutterfly closed Groovebook and is in distress [same; memory-product-sdk.md Q1]. Neither mails to a third party from several contributors today.
- **Biometrics.** No templates are computed, so BIPA, CUBI and GDPR Art. 9 exposure is avoided by construction (research/face-regulation.md Q7; research/unknowns-r1.md Q8: on-device templates are not a shield by themselves). Face detection without embedding is used only as a count; whether a regulator would see a bounding box as biometric is [unknown], as current.md already notes.

## Compounding asset

- **Per family:** ~300 approved photos a year [estimated: 25 per issue × 12; the per-issue count is a design choice], each with a human caption, a date, the contributor's identity, and sometimes the grandparent's spoken account. This is the named, narrated layer rounds 0–2 could not get anyone to produce, made as a by-product of a paid artifact. It is small by design and cannot be rebuilt by re-indexing a library.
- **The elder's voice.** Replies are recorded once; after a death they are irreplaceable. This is the real switching cost and it is also an obligation: export must always work.
- **The family graph:** who contributes, who is related to whom, postal addresses, birthdays.
- **Physical back catalogue:** issues on a shelf, annual volumes.
- **Company level:** selection feedback (which proposals get approved) and print-and-mail operations at letter rate. Both are copyable.
- Honest: the subscription ends when the recipient dies. Continuation paths (the other grandparents; an annual family volume; the archive at a storage-grade annual price) are unproven, and R12 and R13 show completed-artifact products churn at completion (Qeepsake) [grandparent-loop.md Q7].

## Buildability (4-week demo spec for 2 engineers; ugliest technical risk; what is platform- or policy-gated)

- **Week 1.** iOS app: PhotoKit fetch by creation date for the last 45 days; Vision aesthetics score, utility-image exclusion, feature-print near-duplicate collapse, face-rectangle count; pick 12 spread across days; approve, swap, voice caption with on-device speech recognition; upload approved images only. Sensitive-content screening before anything is proposed.
- **Week 2.** Family group; web link for contributors that opens the system picker; inbound MMS and email; layout engine (HTML to imposed PDF, 24 pages, large type).
- **Week 3.** Print and mail through a local digital printer or a mail API (prices not checked [unknown]); a phone line per family with recording and transcription; replies appear in the app and in the next layout.
- **Week 4.** Twenty pilot families, two issues each; archive export (files + XMP captions) and the MCP endpoint from current.md; a mock annual volume.
- **Acceptance.** At least 70% of proposed photos approved without a swap; median payer time on issue 2 at most 2 minutes; at least half of recipients leave one or more voice replies in 30 days; a written contract quote that puts print + envelope + postage at or below $3.50 [all thresholds estimated: chosen so the "less work" and 59% GM claims are tested, not assumed].
- **Ugliest risk.** Not model quality: operations. Unique booklets at low volume, addressed to elderly people who move, to hospital and care addresses, through a postal service with a 500-piece minimum for the cheap rate. Second: without face recognition the proposer cannot tell the grandchildren from a colleague's birthday; it will propose wrong photos, and one embarrassing print ends a subscription. Third: iOS will not run the monthly proposal unattended; it runs when the push is opened (seconds for one month of photos), so a relative who ignores the push contributes nothing.
- **Platform- or policy-gated.** App Review of the full-library purpose (5.1.1(iii)); Google Play's photo-permission declaration; a USPS commercial permit, barcode and Move Update compliance; carrier registration for SMS. None needs a partnership.

## Ceiling (path to $100M ARR with tagged inputs and arithmetic; or the honest number it tops out at)

**Inputs.**
- Pool: ~41M US grandparents aged 65+ [estimated: sizing.md row 24].
- Price: $11.99/month or $119/year → ~$130 per family-year [estimated: (143.88 + 119) ÷ 2; the 50/50 plan mix is an assumption]. Comparable: Famileo US $9.99–13.99. Famileo's realised French B2C revenue is ~€53–56 per family-year [estimated: family-artifact-market.md Q3].
- Reachable share, anchored at both ends. France after ten years: 280,000 Famileo families against 15.49M people aged 65+ [sourced: World Bank SP.POP.65UP.TO, 2025 value, https://api.worldbank.org/v2/country/FRA;USA/indicator/SP.POP.65UP.TO?format=json, 2026-11-24] = 1.8 families per 100 people 65+ [estimated; overstated, since some families are in Belgium, Spain and the UK]. Scaled by the US/France 65+ ratio of 4.03 (2024 values 60.96M ÷ 15.18M, same source) → 1.13M US families at French parity = 2.8% of the 41M pool [estimated]. US today: Famileo US ≈ 4,500 families [estimated: 110 ÷ 5,322 iOS ratings × 220,000 B2C families; assumes ratings track subscribers; low confidence]; Neveo US ≈ 1,500 [estimated: 94 ÷ 1,273 ratings × 20,000]; The Family Press 520; Hug Letters 1,000 [sourced: family-artifact-market.md Q2] → about 7,500 families, 0.018% of the pool, ~$1M a year [estimated: 7,500 × $130].

**Arithmetic: 41M × share × $130.**

| Scenario | Share of pool | Families | ARR | What it assumes |
|---|---|---|---|---|
| A. Three times today's whole US category | 0.055% | 22,500 | $2.9M | [estimated: 3 × 7,500 × 130] |
| B. A quarter-percent of the pool | 0.24% | 100,000 | $13.0M | Five times Neveo's 20,000 subscribers after eight years [estimated] |
| C. Famileo's absolute size, in the US | 0.68% | 280,000 | $36.4M | What Famileo built in ten years with a care-home seed channel, at €5.99 [estimated] |
| D. French parity | 2.8% | 1,130,000 | $147M | No evidence; the two French-speaking leaders have 110 and 94 US iOS ratings [estimated] |

- **$100M needs 769,000 paying families** [estimated: 100M ÷ 130] = 1.9% of the pool = 68% of French parity, at roughly twice the French price, in a market where a $59 frame does the job once.
- **Add-ons.** Annual volume at 30% attach × $49 = +$15 per family-year [estimated: attach is an assumption]; second addresses at 15% × $72 = +$11 [estimated: assumption]; together about +20%. Senior living as revenue: 17,830 communities × 8.4% (LifeLoop-level penetration) × $99 × 12 = $1.8M [estimated: institutional-legacy.md Q1, Q8; Famileo Pro US list price]; R14's whole institutional life-story ceiling at that penetration is $7.5–28M.
- **Sensitivity.** Each 0.1 point of pool share is 41,000 families and $5.3M. Each $1/month of price is ±9% [estimated: 12 ÷ 130]. At Famileo's realised French revenue per family (~€54, read as $54 with no FX applied) every row falls 58% [estimated: 1 − 54 ÷ 130]. Holding 100,000 families at 40% annual churn needs 40,000 gross adds a year, $1.4–2.6M at a $35–65 CAC; holding 769,000 needs 308,000 adds, $11–20M a year [estimated: S × c × CAC; churn is an assumption].
- **Largest sourced revenue of any comparable.** Printed family journals: Famileo €15.3M (2025) [sourced-secondary], "près de 14 millions" for 2024 read directly [sourced: family-artifact-market.md §3]. Frames: Nixplay $57.9M filed for FY2021, $20.0M by FY2023; Skylight $75M (2021, press) and "$300M+" (company listing, unaudited, calendar-led) [same]. Mobile print for oneself: PlanetArt (FreePrints) $395.0M in FY2024, of which mobile apps 44% ≈ $174M [estimated: 0.44 × 395.0], revenue down 1.7% in FY2023 and 2.7% in FY2024, marketing 22.7% of revenue; the whole business was priced at $169.5M of equity, about 0.43× revenue [sourced: Crowe HAF report, 2025-05-21, fetched 2026-11-24; ratio estimated], and the sale closed 2025-06-30 [sourced-secondary: search extract of Claranova's BusinessWire release, 2026-11-24]. No recurring print-to-a-grandparent business anywhere has a sourced revenue above €16M.
- **Honest number.** Scenarios A–B with add-ons: **$4–16M ARR in five to seven years** [estimated: 2.9–13.0 × 1.2 = 3.5–15.6]. $35–45M requires matching Famileo's absolute French base in a country where Famileo itself has not. **$100M does not pencil** on any research-supported input. A critic taking the US-evidence end (today's category, tripled) gets ~$3M, and that is a fair reading.
- **What this variant is.** A cash-generating artifact with better evidence of payment than any earlier variant, and a way to get the named archive built as a by-product. It is not a fix for Ceiling.

## Load-bearing assumptions (numbered; each with the observable fact that would falsify it)

1. **Selection effort drives contributor drop-off and churn.** Falsified if: in the pilot, families using proposals do not contribute more photos or renew more often than a manual-upload control arm over three issues.
2. **Enough users grant full photo access.** Falsified if: under 50% of iOS installers grant full access, or App Review rejects the purpose string under 5.1.1(iii).
3. **Proposals are good without face recognition.** Falsified if: under 70% of proposed photos are approved without a swap, or more than 1 issue in 50 draws a "wrong photo printed" complaint.
4. **The journal mails as an automation letter at $0.62–0.71.** Falsified by: a USPS mailpiece design ruling that the enveloped booklet is nonmachinable or a flat.
5. **Unique 24-page booklets print for at most $2.50 under contract.** Falsified by: three RFQs at 10,000 copies a month all above $3.50.
6. **Gift-to-a-third-party journals retain far better than self-purchased print.** Falsified if: fewer than 60% of paying families are still paying at month 6, or median life is under 18 months.
7. **US adult children will pay ~$12/month when a $59 frame exists.** Falsified if: paid conversion from the $4.95 first issue to month 2 is under 40%, or blended CAC exceeds $65 after the first $50k of spend.
8. **Grandparents will reply by phone.** Falsified if: fewer than 30% of recipients call at least once in the first two issues.
9. **Contributors convert to payers for the other grandparents.** Falsified if: fewer than 5% of journals produce a second paid journal within 12 months.
10. **FamilyAlbum and Famileo do not ship multi-phone proposal with monthly mailing to a grandparent in the US within 12 months.** Falsified by: an App Store release note or pricing page showing it.
11. **Senior living works as distribution without becoming the payer.** Falsified if: no community among the first 20 approached will hand out codes without a contract, or communities insist on a home-pays model.
12. **The archive matters to retention or to a later sale.** Falsified if: annual-volume attach is under 10%, or fewer than 20% of families whose recipient dies keep any paid plan.

## Relationship to variants/current.md (what is kept from the organizer workbench and the index-only engine; what is dropped)

- **Kept.** The index-only, on-device engine (originals stay on the phone; here scoped to one month and stripped of face embeddings). Naming as a prompted human act: the client-review screen becomes the contributor's caption and the grandparent's reply line. The consent architecture, taken to its limit (no templates at all). XMP and MCP export. The organizer channel as one small route and as the source of scanned prints for the archive page. The tribute pack, as the memorial edition.
- **Dropped.** The Mac workbench as the product; Takeout repair, Photos.sqlite reading and dedupe; per-seat and per-project pricing; face clustering; the organizer as first customer; the hosted vault as something sold separately.
- **Changed.** What is sold: a printed artifact on a monthly gift subscription, not organizing. The archive is the residue of the artifact.
- **Not regressed.** Wedge: no user-run migration. Economics: no library storage (~0.9 GB per family-year). Names: from captions and voice, not from faces.

## Evidence pointers (file:section for every claim above)

- Journal and frame incumbents, prices, subscribers, revenue, dead and alive print subscriptions, auto-assembly table, US traction, falsification: research/family-artifact-market.md Q1–Q7, §3 comparables, §4 rows 11–32, §5 unknowns.
- Senior-living counts, LifeLoop, Famileo Pro, sales cycle, turnover, institutional ceiling: research/institutional-legacy.md Q1, Q2, Q5, Q6, Q8.
- Voice costs, landline interviews, gift spending, completion churn: research/memoir-gift-market.md bottom line, Q5, Q6, Q7.
- Grandparent, 65+ and sandwich-generation counts; CAC anchors: research/sizing.md Q2, Q4, rows 11, 22, 24.
- Stripe, R2, retention regimes, GM convention: research/unit-economics.md Q1, Q6, Q7.
- FamilyAlbum scale and release cadence, follower-pay 4.3%, Qeepsake and Tinybeans CAC and churn: research/grandparent-loop.md Q1, Q4, Q5, Q7.
- No-template rule, Samsung and Doe v. Apple: research/face-regulation.md Q7 and risk table; research/unknowns-r1.md Q8.
- One-month on-device scoring time, background limits: research/ios-feasibility.md Q2, Q3. Vision aesthetics API, incumbent curation, Chatbooks prices, Shutterfly condition: research/memory-product-sdk.md Q1, Q3, Q6, Q7.
- Google Photos API removal, iOS limited library, Google Play photo-permission policy: research/platform-access.md Q1, Q4, Q8.
- Tagging rate when naming is self-serve: research/digitization-market.md Q6. Tribute pack and funeral channel: research/estate.md Q6. MCP access by assistant: research/byo-ai.md §3. Organizer channel size: research/pro-channel.md Q1.
- What killed the round-2 variants (ceilings recomputed from the research-supported end; full-library permission; FamilyAlbum as the free incumbent): critiques/v2-grandparent-r2-{investor,builder,customer}.md; critiques/v2-prints-r2-investor.md; SCORECARD.md round-2 summary.
- Fetched 2026-11-24 for this file: USPS Notice 123 (effective 2026-10-04), DMM 201 and DMM 233 at pe.usps.com; App Store Review Guidelines 3.1.3(e) and 5.1.1(iii); Crowe HAF independent expert report on the PlanetArt sale (claranova.com, dated 2025-05-21); getfamilypost.com and iTunes lookup id 6760652389; hugletters.com; nanagram.co; lineagepost.com (meta description only; body renders client-side); World Bank SP.POP.65UP.TO for France and the US; Pew short read of 2026-01-08.
- Seen only as search extracts today: yourbookpress.com and 55printing.com booklet prices; Lineage's $24.99/$29.99 and founding year; FamilyAlbum's AI-built monthly book with copies for grandparents; Pew 65+ home-broadband figures (two values, unverified).
- Looked for and not found: Famileo or Neveo churn; iOS full-versus-limited photo-access grant rates; a contract price for variable-data booklets; NanaGram subscriber or revenue figures; SSA mortality table (blocked) for the recipient-death floor; BusinessWire's PlanetArt releases (access denied; the Crowe report was used instead).
