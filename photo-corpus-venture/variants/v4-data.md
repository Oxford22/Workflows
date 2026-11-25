# v4-data — Consented camera-roll licensing: a free private archive paid for by AI builders

Written 2026-11-25 for round 4. Primary input: `research/ai-data-licensing.md` (written 2026-11-25, read in full). Eight further pages were fetched for this file (attestation, store policy, payout costs, Kled's dataset list) and are tagged with their own URLs. Verdict up front, because the research is one-sided: **the payer exists, but not for this asset. $100M does not pencil; the honest number is about $4M of gross licensing a year at the centre for about three years, then refresh revenue of about $1M a year at the research-supported end.** The variant is written out in full so the critics can check that conclusion rather than take it on trust.

## One line

A free iPhone app indexes your existing library where it lives (no upload, no migration), gives you private search and a bring-your-own-AI tool, and lets you opt reviewed, people-free photos and clips into a licensing pool; AI model builders pay for spec-matched, consent-recorded, provenance-scored sets, and the owner gets half.

## Customer (payer, user, supplier or audience; how many [tagged]; what they do today; what they pay today)

**Payer: a data-partnerships or data-acquisition lead at a model builder.**
- How many: Wirestock supplies "six of the largest foundation model makers" [sourced: https://techcrunch.com/2026/05/14/wirestock-raises-23m-to-supply-multi-modal-data-to-ai-labs/, 2026-05-14]; Defined.ai named five Big Tech buyers [sourced: Reuters 2024-04-05 mirror, via ai-data-licensing.md Q2]; Freepik's archive sold to two [sourced: same Reuters item, ai-data-licensing.md Q1]. The count of image and video model builders with a data budget beyond those is [unknown]. Synthetic-data companies as buyers of camera-roll stills: [unknown: no deal, price or statement found in ai-data-licensing.md or in one extended search on 2026-11-25].
- Three of the largest potential buyers own camera-roll platforms and do not need a broker. Meta asks Facebook users to opt unposted camera-roll photos into cloud processing and pays $0 [sourced: TechCrunch 2025-06-27, ai-data-licensing.md Q1]. Google holds "more than 4 trillion photos" [sourced: blog.google 2020-11-11, sizing.md row 26] and says it does not train generative models outside Google Photos on personal Photos data [sourced-secondary: https://support.google.com/photos/answer/15344015, via search summary 2026-11-25; live text not read].
- What they do today and pay today: catalog deals with stock libraries at "$25 million to $50 million each" initially (Shutterstock, 2023–2024) and $65M total value for two multi-year Getty licences (Q4 2025) [sourced / sourced-secondary: ai-data-licensing.md Q1]; bulk stills at $0.02–0.04 per image (Freepik, the only closed per-image price found) [sourced: ai-data-licensing.md §4 row 9]; curated sets at $1–2 per image (Defined.ai, 2024) [sourced: row 11]; unpublished video at $1–4 per minute [sourced-secondary: row 12]; and, increasingly, commissioned capture at $7–25 an hour of contributor pay [sourced-secondary, low quality: ai-data-licensing.md Q3].
- What they have stopped doing: buying off-the-shelf stills. Shutterstock's data offering fell 91% in Q3 2026; Getty's AI-licensing share fell from 4.4% (FY2025) to 3.4% (twelve months to Q2 2026) and Getty filed Chapter 11 on 2026-10-21 [sourced: SEC filings, ai-data-licensing.md bottom line 2–3].

**Supplier and user: an adult with a large camera roll.**
- How many: about 243M US adult smartphone users [estimated: 267M adults × 91% ownership, sizing.md rows 11–12]; 48% say they have more than 1,000 photos on the phone [sourced: CNBC 2026-02-28 relaying Mixbook, sizing.md Q3], so about 117M [estimated: 243M × 0.48]. Average roll 3,139 items (2023, n=1,967); another figure says 1,598 [sourced / sourced-secondary: sizing.md row 25].
- What they do today: pay Apple or Google for storage (about 80M US households pay for a photo-bearing cloud plan [estimated: sizing.md row 17]) and get AI search free from the platform (Siri AI on iOS 27, Ask Photos) [SCORECARD round-0 summary]. They earn nothing from their photos. The ones who try earn about $0.0073 per photo on Kled [estimated: $1.10 ÷ 151, public forum post https://reddit.com/r/beermoney/comments/1r1mybn/made_110_uploading_151_photos_on_kled_ios_only/, 2026-02-11].
- The family archive is the retention surface, not the product sold.

## Wedge (first use case adopted without changing habits; the first 10 minutes for each party; day-1 value; day-30 value)

**No habit change on the supply side.** The library stays in Apple Photos. The user never runs an export. This is the index-only engine in `variants/current.md` (merge notes), on the phone.

**Supplier, first 10 minutes.** (1) Install, grant full-library access, tap Index; the app works through local preview copies in a user-started session that takes about 15 minutes at the floor and 38–57 minutes centrally for 30,000 photos, and that the Camera app can kill [estimated: ios-feasibility.md Q3; unknowns-r1.md row 4]. (2) Search works on whatever is indexed so far. (3) A "what could be licensed" screen shows counts after the default exclusions: anything with a detected face or body, anything that looks like a minor, screenshots, documents, receipts, duplicates and bursts. On Kled's realized figure that leaves about 400 of 3,139 items [estimated: 200M corpus files ÷ 500,000 contributors, ai-data-licensing.md Q6]. (4) The screen states the money plainly: about $6 for a whole base roll each time a buyer takes it [estimated: 400 × $0.03 × 50% owner share]. Nothing has left the phone.

**Supplier, day 1 and day 30.** Day 1: private search and an on-device tool that Claude or Gemini can call through iOS 27's Foundation Models framework [sourced: ios-feasibility.md Q1]. This is also what the platform gives free, so day-1 value is weak (Pain is not improved over v1-federation, which scored Pain 3). Day 30: a buyer's spec has matched some items; the user reviews them one screen at a time, opts in, and only those originals upload. A ledger shows what was licensed to whom, with a withdraw button.

**Buyer, first 10 minutes.** A datasheet and a count query ("street scenes, no people, US, 2019–2026, camera originals"). Matching runs on the server over embeddings and coarse labels of eligible items that suppliers have chosen to list; originals are not there. Reason for the server-side match: iOS gives no dependable background wake to query phones (ios-feasibility.md Q2). Listing costs at most about 5 MB of embeddings per supplier even if every item were listed [estimated: 3,139 items × 768 dims × 2 bytes].

**Buyer, day 1 and day 30.** Day 1: counts, and a 1,000-item sample (a design choice) with per-item manifests. Day 30: a delivered set with, per item, the consent record, capture metadata, a library-context provenance score (defined under Product), the screening results with a measured miss rate, and a revocation feed the buyer must honour.

**Honest gap.** The leading seller of exactly this corpus moved its home screen away from camera-roll upload on 2026-09-30 because it "could only collect the data people already had, not the data labs actually needed" [sourced: https://www.kled.ai/blog/kled-v3-is-here, 2026-09-30, ai-data-licensing.md bottom line 1]. Spec-matching over a listed index narrows that gap. It does not close it: the items are still things people already shot.

## Why now (dated changes since 2024, each tagged)

For:
1. 2025-08-02 and 2026-08-02: the EU AI Act's public training-content summary became mandatory, then enforceable, with fines up to 3% of turnover or EUR 15M [sourced: EC FAQ, ai-data-licensing.md §4 row 23]. Buyers now have to describe where data came from.
2. 2026-07-20: final approval of the $1.5B Bartz v. Anthropic settlement, about $3,000 per work [sourced: Authors Guild 2026-07-21, ai-data-licensing.md row 22]. A vendor's reading is that it "was driven by acquisition, not by training itself" [sourced: troveo.ai, 2026].
3. 2025-09: Pixel 10 became the first phone to sign every native-camera photo with C2PA Content Credentials, at Assurance Level 2 [sourced: https://security.googleblog.com/2025/09/pixel-android-trusted-images-c2pa-content-credentials.html, 2025-09]. 2026-09-09: Apple shipped an opt-in, Apple-only "Reference Image" mode on the iPhone 18 Pro main camera [sourced-secondary: https://www.lumethic.com/en/articles/smartphones-c2pa-content-credentials, updated 2026-09-16; no apple.com page read].
4. 2026-09: iOS 27 lets any app run on-device indexing and a third-party model with tool calling over the library in place [sourced: ios-feasibility.md Q1; CHANGELOG round 0 item 4].
5. 2026: supply and capital showed up. Kled claims 500,000+ opt-in contributors and a 200M-file "Consented Camera-Roll Corpus"; its site banner says $10M raised, a review site quoting the company says $14M [sourced: https://www.kled.ai/datasets, 2026-11-25; sourced-secondary: ai-data-licensing.md Q2]. Wirestock raised $23M on a $40M run-rate (2026-05-14) [sourced: TechCrunch].

Against, and heavier:
6. Off-the-shelf stills demand peaked in 2025 (Shutterstock data offering down 91% in Q3 2026; Getty Chapter 11 on 2026-10-21) [sourced: ai-data-licensing.md Q1, Q3].
7. 2026-09-30: Kled's pivot to a task feed (above). Wirestock's CEO: "then it turned into a lot of custom requests" [sourced: TechCrunch 2026-05-14].
8. 2026-08-01: California data brokers must process DROP deletion requests every 45 days; 2026-04-22: amended COPPA rule compliance date [sourced / sourced-secondary: ai-data-licensing.md Q4].
9. The five legal demand drivers are copyright or transparency drivers. Personal photos never had a copyright problem, so those drivers do not create demand for them [ai-data-licensing.md Q1, legal demand drivers].

Reading: the window for selling existing stills opened in 2023 (Shutterstock's first deals, Wirestock's pivot) and is closing [ai-data-licensing.md Q1–Q3]. This scores as a why-now for the category leader in 2024, not for an entrant in 2027.

## Product (core loop; explicitly NOT in v1)

**Core loop.**
1. **Index in place.** PhotoKit read of the existing library from local previews (about 1536×2048 observed, enough for embeddings) [sourced-secondary: ios-feasibility.md Q4]; SigLIP 2 or TinyCLIP embeddings (MobileCLIP weights are research-only) [unknowns-r1.md row 5]; Vision labels and OCR; face *detection* only, to exclude. No face embedding is computed or stored anywhere.
2. **Private use.** Search, and a Foundation Models tool so the user's own Claude or Gemini session can query the index. On-device only; free; no server cost.
3. **Eligibility.** Default exclusions as in the wedge. Nothing is eligible until the user has looked at it.
4. **Library-context provenance score.** Evidence an upload-only marketplace cannot see: the item sits in a time-ordered run from the same device, with a Live Photo pair or burst siblings, consistent location track and years of neighbours [estimated: design inference from the PhotoKit surface in platform-access.md Q1; accuracy unmeasured]. It is a score, not proof.
5. **List, match, review, upload.** Embeddings and labels of eligible items are listed; buyers' specs match on the server; the user reviews matched items; only those originals upload, about 1 GB per supplier [estimated: 400 × 2.5 MB, sizing.md Q3]. Uploads carry an App Attest assertion that they came from an unmodified copy of the app on a real device [sourced: https://developer.apple.com/tutorials/data/documentation/devicecheck/establishing-your-app-s-integrity.json, read 2026-11-25].
6. **Second screen on the server.** Faces, minors, text and personal details, stock and web matches, AI-image detection. Kled's own figures show why: one region's 10-million-upload sample was 94.2% fraudulent [sourced: Premium Times 2026-05-05, ai-data-licensing.md Q5].
7. **Attested capture (new photos only).** An in-app camera signs at capture. Kled already sells this class as "Camera-Original Phone Photos (1M photos) ... never imported from a camera roll" for synthetic-image detection [sourced: https://www.kled.ai/datasets, 2026-11-25]. The market's own provenance product excludes the archive.
8. **Ledger, payout, revocation.** Half of each licence to the owner; cash-out at $25 [estimated: design choice; Kled also uses a $25 minimum, ai-data-licensing.md Q2]; withdrawal propagates to buyers' datasets through a revocation feed (trained models are not unwound, and the licence says so).

**What attestation is technically possible.**

| Layer | iOS | Android | What it proves |
|---|---|---|---|
| App and device integrity | App Attest [sourced: Apple doc above] | Play Integrity [unknown: doc page fetched 2026-11-25, only navigation rendered] | Upload came from the real app; says nothing about the photo |
| Capture signature on existing photos | None. "No iPhone supports C2PA"; iPhone 18 Pro Reference Image is opt-in, main camera only, Apple-only format [sourced-secondary: lumethic, 2026-09-16] | Pixel 10 and 11 native camera, default on [sourced: Google security blog 2025-09]; Samsung S25/S26 sign only AI edits [sourced-secondary: lumethic] | Signed by that camera app; a signature "doesn't prove anything about whether the file is trustworthy" [sourced: https://hackerfactor.com/blog/index.php?/archives/1077-Google-Pixel-10-and-Massive-C2PA-Failures.html, 2025-09-05]; a rooted-device signing flaw was reported in August 2026 [sourced-secondary: search summary, 2026-11-25; not verified] |
| Capture signature on new photos | In-app camera with a hardware-held key; "an app cannot reach the hardware root of trust" [sourced-secondary: lumethic] | Same, or native on Pixel | Captured in our app at a time; not that the scene is unstaged |
| Library context | Score from neighbours (step 4) | Same | Plausibility; forgeable by scripted import |

So for the seed's asset, the existing roll, cryptographic capture attestation is close to unavailable in the US: iPhones are about 52% of the market [sourced: StatCounter Oct 2026, sizing.md row 13] and carry none; share of Pixel 10/11 photos in rolls [unknown].

**Explicitly NOT in v1.** Identifiable people in any licensed item (see legal gates; a release flow is specified but off). Minors, with or without a parent's consent. Screenshots, documents and receipts, although Kled lists "Documents & Receipts" and "Screens & Apps" datasets, so the default exclusions remove categories with listed demand [sourced: kled.ai/datasets, 2026-11-25]. Face clustering and person search (a stated regression in the private product). EU, UK, and people-content anywhere. Android. A hosted index or remote MCP endpoint in the free tier. Commissioned capture tasks (see Ceiling: that is where the money is, and it is not this venture).

## Business model and pricing (with comparables, tagged)

- **Buyer price, catalog:** $0.03 per image per non-exclusive licence [sourced: midpoint of Freepik's closed $0.02–0.04, ai-data-licensing.md row 9]. No newer closed per-image price exists [unknown: ai-data-licensing.md Q3; one further extended search on 2026-11-25 returned only broker and SEO pages, one of which marks image demand "Falling" (low quality)].
- **Buyer price, spec-matched sets with manifests:** list $0.25 per image [estimated: assumption between Freepik's closed bulk price and Defined.ai's 2024 $1–2 curated price; no closed 2026 comparable, so the Ceiling does not use it].
- **Video:** $1 per minute list [sourced-secondary: Bloomberg 2025-01-10, "mostly $1 to $2"; one aggregator puts 2026 realized rates near $0.55 (low quality), ai-data-licensing.md Q3].
- **Owner share: 50%** by design [sourced: top of Getty's 20–50% contributor band, ai-data-licensing.md row 8]. The market norm is lower: 20–30% at one Defined.ai supplier [sourced: row 11]. The higher share is the price of asking people to license family-archive photos at all.
- **If sold through an aggregator instead of direct**, the company is the "owner" and receives 20–30% of the deal [sourced: same].
- **Free tier:** on-device index, search and tool. A paid hosted endpoint at $39.99 a year is possible (current.md's vault price) and is not relied on.
- **Earnings a typical roll produces.** Per full sale: $0.96 low, $3.00 base, $31.40 high at market owner shares [estimated: ai-data-licensing.md Q6 table]; $6.00 at this variant's 50% on the base roll. That is about two months of a 200 GB plan at $2.99 [estimated: 6 ÷ 2.99; plan price per unit-economics.md Q5]. Over a lifetime with two to six buyers: $12–36 [estimated: 6 × 2; 6 × 6]. After that, 38–305 new eligible items a year earn $0.57–4.57 per buyer per year [estimated: 300 photos a year (Rise Above's global per-capita figure, a lower bound) to 2,400 a year (the heavy reference user), both in unit-economics.md Q2, × 12.7% × $0.03 × 50%]. Video might add $1.65–17 per sale to the owner on an unverified eligible share [estimated: 8 GB of video in a 16 GB roll (sizing.md Q3) ÷ 60–170 MB per minute (sourced-secondary and conflicting: unit-economics.md Q2; same range in a search summary of MacRumors and iMore, 2026-11-25) = 47–133 minutes; × 12.7% eligible (assumed equal to stills, [unknown]) = 6–17 minutes; × $0.55–2 × 50%].
- **Does that motivate anyone?** As income, no. The people it does motivate are the ones a marketplace least wants: nine of ten forum posts about Kled in early 2026 were removed as referral promotion, and fraud tracked the cash [sourced / estimated: ai-data-licensing.md Q5]. The design answer is that the archive is the reason to install and the money is a token. No survey on willingness to sell personal photos to AI firms exists [unknown]; the nearest figure is 65% uncomfortable with AI training on personal data (n=11,000) [sourced-secondary: ai-data-licensing.md row 30].

## Distribution (non-paid channels with evidence; one paid channel with CAC math if any)

**Buyers.** Direct sales to a short list (six to a few dozen accounts). No channel problem; a demand problem.

**Suppliers, non-paid.**
1. The "get paid" hook pulls installs: Neon took 75,000 downloads in a day and reached No. 2 in Social Networking; Kled claims 500,000 contributors [sourced: ai-data-licensing.md Q2, Q5]. The same hook brought Neon's breach within days and Kled's fraud. Kled's US App Store listing has about 2,000 ratings [sourced: ai-data-licensing.md Q2], which sits oddly beside 500,000 contributors; active US suppliers [unknown].
2. A privacy-first archive brand: Ente, the nearest independent, has 490,639 registered accounts in total [sourced: ente.com/open via SCORECARD]. That brand and a data-sales business pull against each other (see reputational risk).
3. The organizer channel in current.md does not transfer. An organizer paid to protect a family's photos will not recommend an app that sells them [estimated: judgment; untested].

**One paid channel.** Apple Ads, Photo & Video median CPI $2.79 [sourced: sizing.md row 30]. If 20% of installs finish indexing, review and an ID check [estimated: assumption; range 10–40%; no data], CAC per active supplier is about $14 ($7–28) [estimated: 2.79 ÷ 0.20; ÷ 0.40; ÷ 0.10]. Contribution per full-catalog sale is $3.85 (Economics). Payback takes 3.6 full sales [estimated: 13.95 ÷ 3.85]; Freepik found two buyers. **Paid acquisition does not pay back.**

## Economics (per-customer or per-unit COGS; GM; payback; capital needs; cite research rows or derive with tags)

Unit: one active supplier, one full non-exclusive sale of a base roll (400 stills [estimated: ai-data-licensing.md Q6]).

| Line | 50% owner share | 25% owner share | Tag |
|---|---|---|---|
| Gross | $12.00 | $12.00 | [estimated: 400 × $0.03, ai-data-licensing.md Q6] |
| To owner | $6.00 | $3.00 | [estimated] |
| Storage of opted-in originals, 1 GB for a year | $0.18 | $0.18 | [estimated: 1 GB × $0.015 (R2) × 12, unit-economics.md Q7; $0.08 on B2] |
| Machine screening | $0.01 | $0.01 | [estimated: $0.69 per 22,000 images (unit-economics.md Q3) × 400] |
| Human QA on a 5% sample | $0.40 | $0.40 | [estimated: assumption, 20 items × $0.02] |
| ID check, $1.50 once, over 3 years | $0.50 | $0.50 | [sourced: https://stripe.com/identity, 2026-11-25; 3 years is an assumption] |
| Payout rail | $0.56 | $0.28 | [estimated: ($2 per active account + 0.25% + $0.25) on a $25 cash-out = $2.31 = 9.25%; sourced: https://stripe.com/connect/pricing, 2026-11-25] |
| Support | $0.50 | $0.50 | [estimated: assumption] |
| **Contribution** | **$3.85** | **$7.13** | [estimated: 12 − 6 − 2.15; 12 − 3 − 1.87] |
| As % of net revenue | 64% | 79% | [estimated: 3.85 ÷ 6; 7.13 ÷ 9] |

- **Upload cost versus index-only.** Index-only costs nothing until a sale. Uploading opted-in originals is cheap ($0.18 a year per supplier). Storage is not the problem here, unlike the seed. A hosted index for the free tier would cost $1.92 a year per user [estimated: $0.16 × 12, unit-economics.md Q7] and wipe out half a sale, which is why the free tier stays on the device.
- **A $3 balance cannot be paid out economically**: the rail costs $2.26 [estimated: 2 + 0.0075 + 0.25]. Hence the $25 threshold, which a base roll reaches after four to five full sales at 50% [estimated: 25 ÷ 6]. Most suppliers will never be paid in cash. That is a consumer-protection and press risk in its own right.
- **Fixed costs the table omits:** privacy counsel, buyer contracts with indemnities (Getty indemnifies customers for release failures [sourced: Getty FY2025 10-K, ai-data-licensing.md Q4]), data-broker registration and DROP processing, security review for lab procurement. Cost of indemnity cover [unknown].
- **Margin comparables:** Shutterstock company-wide cost of revenue 41% (2025); data-line margin [unknown] [sourced: ai-data-licensing.md row 4]. Reklaim 78% gross margin on C$4.99M [sourced-secondary: row 29].
- **Capital:** about $2.4M for 18 months [estimated: assumption, 5 people × $200K loaded × 1.5 years = $1.5M, plus $0.5M legal and compliance, $0.4M supply and sales]. Comparable: Kled raised $10–14M, reached a 200M-file corpus, and pivoted.

## Platform, incumbent and regulatory risk (the obvious move by Apple, Google, Amazon or the category leader; the law that could close this; why this survives or doesn't)

**Why the named incumbents do not already own this.**

| Who | Why not | Evidence |
|---|---|---|
| Shutterstock, Getty | Sold released, captioned professional catalogs once to each large buyer; no relationship with private rolls; that line is now collapsing | ai-data-licensing.md Q1, Q3 |
| Wirestock | Started with off-the-shelf creator content, moved to custom requests; $40M run-rate comes with that shift [sourced: TechCrunch 2026-05-14] | ai-data-licensing.md Q2 |
| Troveo | Video from creators and companies, 95% exclusive, about $2,900 paid per licensor [estimated: $20M ÷ 7,000] | ai-data-licensing.md Q2 |
| **Kled** | **It does own this.** 500,000 claimed contributors, a 200M-file consented camera-roll corpus, face masking, ID checks, a fraud detector [sourced: kled.ai, 2026-09-30 and 2026-11-25; company claims]. It then demoted the upload button | ai-data-licensing.md Q2, Q3 |

What this variant has that Kled lacks: matching before upload, library-context provenance, and a reason to keep the app that is not cash. Those improve supply quality and cost. None creates demand. Kled can add on-device indexing in a release.

**Obvious platform moves.** Meta already collects opted-in camera rolls for nothing. Google could change its Photos training promise (its privacy policy was updated on 2026-10-16 [sourced-secondary: search summary, 2026-11-25; not verified]). Apple could remove the app: guideline 5.1.2(i) requires explicit permission for sharing with third-party AI and says data "may only be shared with third parties to improve the app or serve advertising" [sourced: developer.apple.com guidelines, ai-data-licensing.md Q4]. Kled and Neon are live, so Apple tolerates the category today. Google Play bars selling personal and sensitive user data with a carve-out for "User-initiated transfer" [sourced: same]; broad photo access is allowed only where core function needs it, mandatory since 2025-05-28 [sourced: https://support.google.com/googleplay/android-developer/answer/14115180, read 2026-11-25].

**Legal gates and the design answer to each.**
- **Faces (BIPA, CUBI).** A photo is not a biometric identifier; a face-geometry scan derived from it is, and consent must come from the subject, not the uploader [face-regulation.md Q1–Q2]. Buyers want the check done upstream (Troveo verifies every hour for BIPA and CUBI) [sourced: troveo.ai]. Answer: no people at all in v1. Residual: detector misses. Miss rate [unknown] until measured.
- **Releases for identifiable people.** Possible later through current.md's review link with an e-signature per living named person. Completion is [unknown] (current.md assumption 8). Camera-roll photos of friends carry no releases today [ai-data-licensing.md Q4].
- **Minors.** COPPA's definition of personal information includes a photo or video with a child's image [sourced: 16 CFR 312.2]. Excluded outright.
- **Bystanders and GDPR.** The uploader's consent is not the bystander's; Art. 9 needs the data subject's explicit consent; the household exemption does not cover sale [face-regulation.md Q4]. EU and UK are out of v1.
- **California Delete Act.** A broker sells personal information of consumers it has no direct relationship with; people who slip through in a supplier's photos fit that [sourced: privacy.ca.gov, ai-data-licensing.md Q4]. Answer: register, run DROP on the 45-day cycle (30 days from 2027-01-01). Failure to register costs $200 per consumer per day [sourced-secondary: TrustArc 2026-07-31]. Registration fee [unknown: not checked].
- **FTC.** The base cases are Everalbum (model deletion, 20-year order) and Match/OkCupid–Clarifai (2026) [face-regulation.md Q5]. A privacy-branded archive that sells data is the fact pattern for a deception claim unless consent is separate, express and literal.
- **Precedent.** The one platform that tried to license a consumer photo archive, Photobucket, was sued about eight months later and has no confirmed deal [estimated / sourced: ai-data-licensing.md bottom line 5].

**Reputational risk of "selling family photos".** The headline writes itself. Neon went dark a day after going viral; Meta's camera-roll prompt drew privacy coverage at a price of $0; 65% say they are uncomfortable [sources above]. Being listed on California's public data-broker registry is incompatible with the seed's "user-owned, private" positioning. **This is a regression against every prior variant and is stated as such.**

**Survives or not.** The people-free design survives the law. It does not survive the demand evidence.

## Compounding asset

- A consent and provenance ledger per item, a revocation feed buyers have integrated, and a history of which specs matched what.
- It compounds weakly. A catalog sells to each large buyer once [ai-data-licensing.md Q3]. After that only new items sell: about 10% of an average roll a year at the lower-bound capture rate [estimated: 300 ÷ 3,139], and only if buyers come back for refreshes, which Shutterstock's 2026 data line does not show. The asset also shrinks: every withdrawal and DROP request removes items.
- The private archive compounds for the user (search history, notes) but is rebuildable for cents, as SCORECARD already records [byo-ai.md Q5].
- Human-confirmed names, the seed's best asset, cannot be sold here at all: they attach to people, and people are excluded.

## Buildability (4-week demo spec for 2 engineers; ugliest technical risk; what is platform-, policy- or licence-gated)

- **Week 1.** iOS 27 app: PhotoKit read, resumable user-started indexing from local previews, SigLIP 2 embeddings, Vision labels, face detection for exclusion, screenshot and document flags, duplicate grouping.
- **Week 2.** Private search; Foundation Models tool for Claude or Gemini; eligibility screen with honest earnings; library-context score.
- **Week 3.** Listing of embeddings and labels; buyer console with count queries; review-and-upload of matched originals with App Attest; per-item manifest; server screen.
- **Week 4.** In-app signed capture; ledger and revocation feed (no live payouts); a datasheet for three design-partner buyers.
- **Measurements that decide it** (test sizes are design choices). On 20 volunteer libraries: eligible share (research assumes 12.7%; no measured split of a roll exists [unknown: ai-data-licensing.md unknown 7]); miss rate of the people and minors screen on a hand-labelled 2,000-item sample; catch rate when 500 AI-generated, stock and saved-from-web images are planted in a test library. And one commercial test: a written price from any buyer for a people-free camera-roll set.
- **Ugliest technical risk.** One child's face or one bank statement in a delivered set. Every legal gate above turns on the screen's miss rate, and it has to hold across millions of items; a 0.1% miss rate on a 200M-item corpus is 200,000 items [estimated: 200M × 0.001]. Second: the provenance score is forgeable by scripted import into a library. Third: the Camera app kills the indexing session [unknowns-r1.md row 4].
- **Gated.** Apple review under 5.1.2(i); Google Play user-data policy (Android deferred); California data-broker registration; each buyer's legal and security review; a C2PA signing SDK for iOS (licence and maturity [unknown: not checked]). Nothing needs a platform partnership. The four-week build is not the hard part; the first purchase order is.

## Ceiling (path to $100M ARR with tagged inputs and arithmetic; or the honest number it tops out at)

**Pool.** 243M US adult smartphone users × 3,139 items × 12.7% eligible ≈ 97 billion eligible items [estimated: inputs above]. Supply is not the constraint. Reachable suppliers and paying buyers are.

**Method.** Gross per year = suppliers × eligible items × price × number of buyers who take the catalog ÷ years over which they buy. Buyers: Freepik found two, Wirestock serves six [sourced].

| Case | Suppliers | Items | Price | Buyers ÷ years | Gross per year | Basis for reachable share |
|---|---|---|---|---|---|---|
| Low | 250,000 | 240 | $0.02 | 1 ÷ 3 | $0.4M | Half of Kled's claimed global count, reached without a cash-first hook; low row of ai-data-licensing.md Q6 |
| Base | 500,000 | 400 | $0.03 | 2 ÷ 3 | $4.0M | Kled's claimed count (0.2% of US adult smartphone users, and Kled's is global); needs about 2.5M installs at 20% activation, five times Ente's registered base [estimated: 500,000 ÷ 243M; 500,000 ÷ 0.20; 2.5M ÷ 490,639] |
| High | 1,000,000 | 400 | $0.04 | 6 ÷ 5 | $19.2M | Twice Kled's claim; every one of Wirestock's six buyers takes the whole catalog at Freepik's top price [estimated: assumption] |

[estimated: 250,000 × 240 × 0.02 ÷ 3; 500,000 × 400 × 0.03 × 2 ÷ 3; 1,000,000 × 400 × 0.04 × 6 ÷ 5]

- **Company net revenue** at a 50% owner share: $0.2M / $2.0M / $9.6M; at the market's 25%: $0.3M / $3.0M / $14.4M [estimated].
- **After the first sales, only refresh remains.** At the lower-bound capture rate (38 new eligible items a year): base 500,000 × 38 × $0.03 × 2 = $1.1M a year; high 1,000,000 × 38 × $0.04 × 6 = $9.1M [estimated]. At the heavy-user rate (305 items) the base is $9.2M [estimated: 500,000 × 305 × 0.03 × 2], but that rate does not fit a 3,139-item average roll, and every figure assumes each buyer re-buys every year [unknown]. This is the only part that behaves like ARR.
- **Video** might add $1.8–12M a year gross [estimated: base 500,000 × 10 min × $0.55 × 2 ÷ 3; high 1,000,000 × 10 min × $1 × 6 ÷ 5; the 10 eligible minutes per roll is an unverified assumption].
- **Demand-side cross-check.** What is left of disclosed spending in this neighbourhood in 2026: Shutterstock DDS about $124M annualised [estimated: $93.0M for nine months ÷ 0.75; an upper bound that includes Giphy and Studios], Getty AI licensing about $33M [estimated: ai-data-licensing.md row 6], Wirestock $40M run-rate. Total about $197M. A 2–5% share for a seed entrant with an unreleased, people-free corpus is $3.9–9.9M [estimated]. Consistent with the base case.
- **Sensitivity.** Gross is linear in each input. From the base, $100M needs 25×: for example five times the suppliers (2.5M, five times Kled's claim), 2.5 times the price ($0.075, with no closed comparable and the largest seller's data line down 91%), and twice the buyers. Research's own scale test: 3.33 billion image licences a year at $0.03, or 8.3 million roll-sales at $12 [estimated: ai-data-licensing.md Q6].
- **Largest sourced revenue of any comparable.** Stock libraries: Shutterstock DDS $203.3M in FY2025, an upper bound, professional contributors, falling 46% in the first nine months of 2026. Startups: Wirestock, $40M run-rate, self-reported, mostly custom work. Private individuals' camera rolls: none disclosed by anyone [unknown] [sourced: ai-data-licensing.md §3].
- **The subscription this replaced.** Ente's 4.4% paid share on the base case's 2.5M installs at $39.99 would be $4.4M ARR [estimated: 2,500,000 × 0.044 × 39.99]. The data line does not beat the consumer subscription it was meant to escape.

**Honest number: about $4M of gross licensing a year at the centre ($2–3M net), for roughly three years, then about $1M a year of refresh at the research-supported end. Generous end about $19M gross, or about $30M with video** [estimated: the three cases and the video line above]. It is transaction revenue, not ARR. $100M does not pencil. The route to more money is commissioned capture (Wirestock's path, Kled V3), which is paid gig work, needs no archive, and tops out on evidence at Wirestock's self-reported $40M run-rate. That is a different company.

## Load-bearing assumptions (numbered; each with the observable fact that would falsify it)

Thresholds below are chosen kill criteria [estimated: assumption], not measurements.

1. **Some lab will pay for people-free camera-roll stills in 2027.** Falsified if: none of ten data-partnership leads gives a written price for a sample set; or Kled delists its camera-roll corpus.
2. **The price holds at $0.02–0.04.** Falsified by: any 2026–2027 closed deal below $0.01, or Shutterstock's data line staying down more than 80% for four quarters.
3. **At least two buyers take the catalog.** Falsified if: after twelve months of selling, one or none has.
4. **About 12.7% of a roll is eligible after exclusions.** Falsified if: the 20-library test shows under 5%.
5. **The screen's miss rate for people, minors and personal details can be driven below what buyers' counsel accept.** Falsified if: the 2,000-item test shows over 0.5% misses, or a buyer requires a zero-miss warranty.
6. **Library-context provenance separates real rolls from planted content.** Falsified if: the planted-image test catches under 95%, or a scripted import defeats it.
7. **People will keep the app for the archive, not the cash.** Falsified if: fewer than 20% of installers who have earned nothing open the app in month two (threshold is an assumption; no benchmark for a free archive exists [unknown]), or opt-in is under 10% of indexed users.
8. **A privacy archive and a data-licensing business can share one brand.** Falsified by: review-bombing or press on launch; opt-in under 10%; an organizer or privacy outlet publicly warning against it.
9. **Apple keeps tolerating the category.** Falsified by: removal of Kled, Neon or this app under 5.1.2(i).
10. **Registering as a data broker and running DROP is survivable at seed stage.** Falsified if: compliance exceeds 20% of net revenue, or a buyer refuses a registered broker.
11. **No platform owner opens its own paid or unpaid opt-in at scale.** Already half false (Meta, 2025-06). Fully falsified by Google or Apple shipping a contribute toggle.
12. **The ceiling is accepted as about $4M unless the company becomes a task marketplace.** Falsified upward only by a signed catalog deal above $5M or a closed per-image price above $0.25.

## Relationship to variants/current.md (what is kept from the organizer workbench and the index-only engine; what is dropped)

**Kept.** The index-only engine, originals left in place (merge note 1). The per-item provenance ledger and the hash-stamped evidence export, reused as the buyer manifest. The review link with per-person e-signature, reused as the release flow and switched off in v1. The rule that names come from prompted humans and that no face template is the identity signal; here it is stricter, since no face embedding is computed at all. The model-licence fix (SigLIP 2 or TinyCLIP).

**Dropped.** The organizer as customer and channel. The Mac-first workbench, Takeout repair and dedupe-for-delivery. The family vault as revenue. Face clustering and person search. The family as payer.

**Constraints checked.** No user-run migration: holds. No storing whole libraries of originals: holds (about 1 GB of opted-in items per supplier [estimated: 400 × 2.5 MB]). Names from prompted humans: holds, trivially, because people are excluded.

**Regressions, stated.** Platform and regulatory risk is worse than the leader's (App Store removal clause, data-broker registration, FTC deception exposure, buyer indemnities). Pain for the user is no better than v1-federation's. Trust is worse. Distribution loses the one evidenced channel. Ceiling does not improve on the leader's $3–12M [estimated: variants/current.md Ceiling]: the centre here is about $4M gross and it decays.

**Salvage if killed.** (a) Matching against a listed index before any upload, as a privacy pattern for any future sharing feature. (b) The library-context provenance score, as a feature of the evidence-packet export, which matters for the insurance-claims variant in this round. (c) The measured split of a real camera roll into people, minors, screenshots, documents and the rest, which no source publishes.

## Evidence pointers (file:section for every claim above)

- Deal sizes, per-image and per-minute prices, Shutterstock and Getty filings, Photobucket, legal demand drivers: research/ai-data-licensing.md Q1, §3 deals table, §4 rows 1–13, 22–23.
- Kled, Wirestock, Troveo, Protege, Defined.ai, Neon, Reklaim: research/ai-data-licensing.md Q2, §3 marketplaces table, rows 14–21, 29. Kled dataset list, "Camera-Original" class and funding banner: https://www.kled.ai/datasets (fetched 2026-11-25).
- Demand by modality, the shift to custom capture, price trend: research/ai-data-licensing.md Q3, Q7.
- Legal and store-policy gates: research/ai-data-licensing.md Q4; research/face-regulation.md Q1–Q5, Q7, risk table; Google Play photo-permission policy https://support.google.com/googleplay/android-developer/answer/14115180 (fetched 2026-11-25).
- Supply side, fraud, forum earnings, discomfort survey: research/ai-data-licensing.md Q5, rows 18, 20, 30.
- Roll economics and the $100M scale test: research/ai-data-licensing.md Q6, rows 25–28.
- Roll size, US population and smartphone inputs, OS share, CPI, Ente and retention benchmarks: research/sizing.md Q3, Q4, §3 rows 11–14, 17, 25–27, 30; research/unit-economics.md Q2, Q6.
- Storage, screening and index-only costs: research/unit-economics.md Q1, Q3, Q7.
- On-device indexing limits, preview resolution, Foundation Models tool: research/ios-feasibility.md Q1–Q4, feasibility table; research/unknowns-r1.md rows 4, 5.
- Attestation: Google security blog 2025-09 (fetched); Apple DeviceCheck/App Attest doc (fetched); lumethic.com phone and Reference Image articles (fetched, vendor source, secondary); hackerfactor.com 2025-09-05 (fetched); rooted-Pixel flaw and Apple Reference Image details (search summaries only).
- Payout and ID costs: https://stripe.com/connect/pricing and https://stripe.com/identity (fetched 2026-11-25).
- Why consumer family-memory software caps, and why a private photo network has no business model: SCORECARD.md rounds 0–3; research/family-artifact-market.md bottom line and Q1; research/memoir-gift-market.md bottom line.
- Kept and dropped parts: variants/current.md core loop, merge notes for rounds 1–3.
- Not resolved: any buyer-side price for camera-roll images in 2026; Kled's revenue and named buyers; measured eligible share of a roll; screen miss rates; indemnity cost; CPPA registration fee; Play Integrity doc text; C2PA iOS SDK licence; whether synthetic-data companies buy stills; eligible video minutes per roll. `research/frame-device-market.md` and `research/contents-claims.md` belong to the other two round-4 briefs and were not used.
