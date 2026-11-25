# v4-data — round 4 — BUILDER critique

Written 2026-11-25. Fresh context. Variant scored: `variants/v4-data.md` (consented camera-roll licensing; free private archive paid for by AI builders).

## Stance

Builder. I believe only shipped demos. I scored Buildability and Economics hardest and read the 4-week spec line by line for research problems and platform, capital and licence gates.

**What I read.** In full: `SCORECARD.md`, `variants/v4-data.md`, `research/ai-data-licensing.md` (including the audit log). By section: `ios-feasibility.md` Q1–Q9 and both tables; `unknowns-r1.md` Q3–Q10 and summary table; `face-regulation.md` Q1–Q7 and risk table; `sizing.md` Q3–Q4 and numbers table; `unit-economics.md` rows the variant cites (Q1, Q2, Q3, Q7); `platform-access.md` Q1; `assumptions/A2.md` §5. Bottom lines only: `contents-claims.md`, `frame-device-market.md`, `family-artifact-market.md`, `memoir-gift-market.md`. Headings plus keyword search only: the remaining research files. `variants/current.md`: grep for the kept parts and the leader's ceiling. Not read: CHANGELOG, other v4 variants, any critique, `research/audits/`.

**The variant predates the repair of its own research file. Where they disagree the research wins.** The disagreements are listed first because they move most of the variant's arithmetic.

## Variant numbers that the repaired research contradicts or no longer supports

| # | Variant says | Repaired research says | Pointer | Effect |
|---|---|---|---|---|
| 1 | 12.7% of a roll is eligible; about 400 items per supplier (Kled corpus ÷ head-count) | **Withdrawn.** The divisor was a later head-count. Share licensable by exclusion: 33.8% / 45.0% / 65.9%, i.e. 540 / 1,414 / 2,069 items. Kled's realized acceptance is a ceiling of 20% of uploads, i.e. 628 items on a base roll | ai-data-licensing.md Q6; audit log item 20 | Every per-roll and Ceiling figure in the variant is built on a withdrawn input |
| 2 | Freepik's $0.02–0.04 is "the only closed per-image price found"; base price $0.03 | Two paid prices exist: Freepik $0.02–0.04 (bulk archive) and Adobe $0.06–0.16 (commissioned). Research base is $0.05 | Q1 Adobe, Freepik; audit log item 17 | Base price understated by the variant's own source |
| 3 | A base roll grosses $12 per sale; owner gets $6 | $70.70 gross at list ($10.80–$331.04); $18.84 at Kled's realized acceptance and $0.03. Research is explicit that these are price-list figures and "no buyer is on record paying these prices for camera-roll photos" | Q6 table and limits | Unit table is stale; see recomputation under Economics |
| 4 | Labs "have stopped" buying off-the-shelf stills: Shutterstock data offering down 91% in Q3 2026 | 91% is one quarter. Nine months: down 60%; DDS trailing twelve months $123.7M. Both sellers cite recognition timing; Getty forecasts recovery to $55M by 2029; "whether 2025 was the peak is [unknown]" | Bottom line 3; Q1; audit log items 1, 21 | "Stopped" is a failed claim; "fell in 2026 to date" is what is supported |
| 5 | Getty's Chapter 11 listed as demand evidence | "Getty's Chapter 11 is a balance-sheet event and is not evidence about demand" (warrant judgments, failed merger, $239M debt service) | Q1 Getty; audit log item 18 | Failed claim |
| 6 | "A catalog sells to each large buyer once [ai-data-licensing.md Q3]" | "Not tested by any source." GoPro's terms say footage "can be purchased more than once" | Q3 first bullet; audit log item 21 | The variant's decay-to-refresh model rests on an untested hypothesis |
| 7 | "Private individuals' camera rolls: none disclosed by anyone"; Photobucket is "the one platform that tried" | GoPro disclosed $2M of AI licensing revenue in Q2 2026 from opted-in personal cloud video at a 50% share; six consumer-archive cases were found, two paid the individual. For personal **stills** there is still no figure | Bottom line 1, 5; Q1 GoPro; audit log item 16 | The closest precedent is missing from the variant. It is video, from a paid cloud, and the Q3 release itemizes nothing |
| 8 | Video at $0.55–$2 per minute ("one aggregator puts 2026 realized rates near $0.55") | The $0.55 figure is withdrawn (source behind a bot check). The only realized yield is GoPro's: at most $0.067 per opted-in minute, 2–7% of the $1–4 list range | Q3 video; audit log item 23 | The variant's video upside ($1.8–12M) has no surviving price input |
| 9 | Delete Act: "$200 per consumer per day" for failing to register | Two separate fines: $200 per day unregistered; $200 per day per undeleted request | Q4; audit log item 25 | Smaller registration exposure than stated; deletion exposure scales with requests |
| 10 | Earnings per full sale "$0.96 low, $3.00 base, $31.40 high" | Pre-repair table. Now $2.16 / $24.74 / $165.52 to the individual at list; $6.28 or $4.58 at Kled's observed contributor rate ($0.01, $0.0073) | Q6 | "Most suppliers will never reach the $25 cash-out" depends on the withdrawn inputs |
| 11 | Private use is "on-device only; free; no server cost", with a tool "Claude or Gemini can call" | Third-party models through Foundation Models are billed to the developer per token; with App Attest "usage bills to your workspace", so the whole install base shares one organization's rate limits and monthly spend cap. Apple's free Private Cloud Compute tier has an unpublished daily per-user cap and ends at 2M first-time downloads. The variant's base case needs 2.5M installs | ios-feasibility.md Q1 (credentials and billing; rate limits; PCC limits) | Failed claim. The free tier has a per-query cost the Economics table omits |
| 12 | Indexing 30,000 photos takes "about 15 minutes at the floor and 38–57 minutes centrally" | That is Scenario A: MobileCLIP-S2 plus faces, **no OCR**. MobileCLIP weights are research-only; SigLIP 2 has no published iPhone latency. The week-1 spec adds OCR and document flags: Scenario B is 2.5 h floor, 2.7 h central, 4.1 h derated | ios-feasibility.md Q3; unknowns-r1.md Q5 | The quoted time does not belong to the build that is specified |
| 13 | App Store gate is 5.1.2(i) | Also 5.1.2(vi): data from Photo APIs "may not be used for marketing, advertising or use-based data mining, including by third parties"; and 5.1.1(iii): prefer the picker over full library access | assumptions/A2.md §5 | Three clauses, not one |

Checked and correct: 243M US adult smartphone users, 48% over 1,000 photos, 3,139 items, CPI $2.79 (sizing.md rows 11–12, 25, 30); R2 $0.015 and $0.69 per 22,000 images (unit-economics.md Q1, Q3); Getty 4.4% → 3.4% (lender deck); Kled 1,971 US ratings; Wirestock $40M run-rate; Kled's 2026-09-30 quote; the Nigeria 94.2% sample.

**Direction of the errors.** Items 1–3 understate price-list value per roll by about 1.6× to 6×. Items 4–6 overstate how dead the demand is. None of this rescues the idea: the repaired research's own bottom line 1 is that the evidence does not support a nine-figure outcome, and its Q6 says each figure "needs a sale; one seller of personal media has reported any."

## Scores

| Dimension | Score | Evidence pointer | One-line reason |
|---|---|---|---|
| 1 Pain | 3 | ai-data-licensing.md bottom line 1, Q3 ("Stills from camera rolls"), Q5 surveys; SCORECARD round-1 row v1-federation | The payer's pain is real for rights-cleared catalogs and custom capture, not for this asset: Kled says the upload button collected "the data people already had, not the data labs actually needed". The supplier's pain is v1-federation's (Pain 3) and the platform already gives search free. Nobody pays today for people-free camera-roll stills |
| 2 Wedge | 3 | ai-data-licensing.md Q2 Kled reviews, Q3 premium attributes, Q6; ios-feasibility.md Q2, Q5 | No migration, which is good. But the supplier must grant full-library access to an app that sells data (a Kled one-star theme), pass an ID check, and review 628–1,414 items one screen at a time for $5–35. The buyer gets nothing until the corpus is large, and the terms offered (non-exclusive, revocable) are the opposite of what sellers report buyers pay for (exclusive, perpetual, to spec). Requires iOS 27: 16–36% of iOS devices at end of October 2026 |
| 3 Why now | 4 | ai-data-licensing.md Q1 legal demand drivers, Q1 GoPro, Q3, Q7 | Dated changes exist (EU summary enforceable 2026-08-02; Bartz 2026-07-20; GoPro program 2025-07-30). All five legal drivers are copyright or transparency drivers and "do not create demand for personal photos". The one dated event about this exact asset is Kled demoting it on 2026-09-30. The variant's "peaked in 2025" is withdrawn, so this is not a 3 |
| 4 Platform risk | 2 | ai-data-licensing.md Q1 (Meta, $0), Q4 Apple and Google Play, Q4 Delete Act; assumptions/A2.md §5; sizing.md row 26 | Three of the largest buyers own the supply (Meta takes opted-in camera rolls for $0; Google holds 4 trillion photos). Three App Store clauses cut against the app. A registered data broker with a privacy-archive brand is the FTC deception fact pattern (face-regulation.md Q5). Kled can add on-device indexing in a release, and GoPro already runs the same 50% program on its own cloud |
| 5 Compounding asset | 3 | ai-data-licensing.md Q3, Q5, Q6 scale test; byo-ai.md Q5 via SCORECARD | A non-exclusive, revocable, people-free corpus that shrinks on every withdrawal and is smaller than the one Kled already lists (200M files). The index is rebuildable for cents. The consent ledger is real but nobody has asked for it. Not a 2 only because "sells once" is untested, so refresh revenue cannot be ruled out |
| 6 Distribution | 3 | ai-data-licensing.md Q2 (Kled ratings, Sensor Tower band), Q5 (fraud, r/beermoney); sizing.md row 30 | The cash hook pulls installs and brings fraud with it (94.2% in one region; 10 of 11 forum posts removed). The variant then disowns that hook and relies on a free archive, which has no evidenced channel. Paid: the variant's own math says it does not pay back. Buyer side: no named buyer, RFP or price sheet in two searches |
| 7 Economics | 3 | ai-data-licensing.md Q6 table and limits, Q2 Kled payout, Q1 GoPro yield; ios-feasibility.md Q1; unit-economics.md Q3 | Numbers are tagged, which keeps it off the floor. But the unit table is built on a withdrawn input, the revenue line has no observed buyer price for this asset, and three cost lines are missing or assumed (see below) |
| 8 Buildability | 5 | ios-feasibility.md Q1–Q4 and feasibility table; unknowns-r1.md Q4, Q5; ai-data-licensing.md Q5 provenance, unknown 5 | The supply-side app is a 4-week build with no platform partnership. The loop is not closed by the demo: the buyer half is demand-gated, and three items in the spec are research problems (see line-by-line) |
| 9 Ceiling | 2 | ai-data-licensing.md bottom line 1–2, Q6 scale test, §3 "largest sourced annual revenue" | No revenue figure exists for personal still photos from anyone. Variant's own number: $4M gross, decaying. Recomputed on repaired inputs: $6–24M gross a year at the base, all at list prices nobody has paid. Transaction revenue, not ARR |
| 10 Founder fit | 5 [unknown] | — | Not stated by the founder |

**Total: 33** (3 + 3 + 4 + 2 + 3 + 3 + 3 + 5 + 2 + 5). Founder fit is a flagged neutral 5.

## Economics, recomputed on the repaired research

All rows [estimated]; method shown. Cost assumptions are the variant's own unless marked.

| Line | Variant (400 items, $0.03) | Realized acceptance (628 items, $0.03) | List by exclusion (1,414 items, $0.05) |
|---|---|---|---|
| Gross per full sale | $12.00 | $18.84 | $70.70 |
| To owner at 50% | $6.00 | $9.42 | $35.35 |
| Storage, 2.5 MB an item, R2, 12 months | $0.18 | $0.28 | $0.64 |
| Machine screen ($0.69 per 22,000) | $0.01 | $0.02 | $0.04 |
| Human QA, 5% sample at $0.02 | $0.40 | $0.63 | $1.41 |
| ID check, amortized | $0.50 | $0.50 | $0.50 |
| Payout rail (9.25% under $25; one $2.34 cash-out above) | $0.56 | $0.87 | $2.34 |
| Support | $0.50 | $0.50 | $0.50 |
| **Contribution** | **$3.85** | **$6.62** | **$29.92** |
| Full sales to pay back $14 CAC | 3.6 | 2.1 | 0.5 |
| Same row with human review of every item at $0.02 | −$3.75 | −$5.31 | $3.05 |

What the table hides:

1. **Every column assumes a sale.** The only realized yield for personal media is GoPro's, 2–7% of list (ai-data-licensing.md Q3). Kled pays contributors $0.01 a photo (Q2), which at its usual share implies a buyer price near or below Freepik's floor, if there is a buyer at all [estimated: inference; Kled's buyer price is unknown].
2. **Sample QA does not buy the warranty buyers ask for.** Shutterstock requires a release for every recognizable person "even ... blurred in the background"; Troveo verifies every hour for BIPA and CUBI (Q4). A 5% sample says nothing about the other 95%. Review of every item turns the realized-acceptance column negative. The $0.02 per item is the variant's assumption; no source.
3. **The ID check is acquisition cost, not amortized COGS.** With 94.2% fraud in one region, the check has to come before listing or the buyer console's counts are fiction. At $1.50 on every applicant, 2.5M installs at 20% activation is up to $0.75M–$3.75M before the first sale [estimated: $1.50 × 500,000 to 2.5M].
4. **The free tier is not free.** Claude or Gemini calls through Foundation Models bill the developer (ios-feasibility.md Q1). Cost per query is not in the research [no evidence found].
5. **Fixed costs are unpriced.** Indemnity cover, broker registration fee and security review are all [unknown] in the variant. The $0.5M legal line is an assumption.
6. **Capital against return.** $2.4M buys 18 months to reach what Kled reached on $10M and then walked away from. Company net at the recomputed base is $3–12M a year for about three years [estimated: half of $6.3M and $23.6M gross].

## The 4-week demo spec, line by line

| Week | Item | Verdict | Why |
|---|---|---|---|
| 1 | PhotoKit read, indexing from local previews | Buildable | ios-feasibility.md Q3–Q4. Local preview size is undocumented (about 1536×2048 observed once); share of assets with no local copy is unknown |
| 1 | "Resumable user-started indexing" | Buildable in the foreground only | Background Neural Engine use needs an entitlement with no request path and no known grant; a continued task expires after about 30 s without progress and is killed by the Camera, and expiry is final (unknowns-r1.md Q4). The honest UX is "leave the app open on a charger" |
| 1 | SigLIP 2 embeddings | Buildable, unmeasured | Apache-2.0, but no iPhone latency exists (unknowns-r1.md Q5). The quoted 15–57 minutes is for a model the product may not ship |
| 1 | Vision labels and OCR, document flags | Buildable, slow | OCR on every image takes 2.5–4.1 h for 30,000 photos (ios-feasibility.md Q3 Scenario B). The variant quotes Scenario A |
| 1 | Face detection for exclusion; "anything that looks like a minor" | **Research problem** | No miss rate is cited for any detector on small, occluded or background faces, and none for age. The only minor-related accuracy number I found in what I read is 30.7% TAR for open face models on infants (SCORECARD round 2), which is recognition, not detection. The variant's kill criterion (0.5%) is 3–7 items per supplier per delivery [estimated: 0.005 × 628; × 1,414] |
| 2 | Private search | Buildable | Same engine as v1-federation |
| 2 | Foundation Models tool for Claude or Gemini | Buildable, beta, billed | Packages are beta or preview; usage bills to the developer and shares one organization's limits (ios-feasibility.md Q1). Needs an Apple-Intelligence device for the on-device model: an estimated 50–60% of active iPhones (Q5) |
| 2 | Eligibility screen "with honest earnings" | Buildable, number unknown | The honest number is between $4.58 and $35 depending on which row of Q6 is believed. There is no buyer price to display |
| 2 | Library-context provenance score | **Research problem** | The variant tags it "accuracy unmeasured" and "forgeable by scripted import". No source shows a buyer wants it. C2PA does not attribute content to a person and metadata can be stripped (ai-data-licensing.md Q5) |
| 3 | Listing of embeddings and labels | Buildable | Note: an embedding of a private photo leaves the phone before the user has reviewed the item for sale. That needs its own consent screen (face-regulation.md Q5, FTC pattern) |
| 3 | Buyer console with count queries | Buildable | A count over zero ID-verified suppliers. Cold start is not addressed |
| 3 | Review-and-upload with App Attest; manifest | Buildable | App Attest proves the app, not the photo (variant's own table) |
| 3 | Server screen: faces, minors, text, personal details, stock and web matches, AI-image detection | **Not a one-week item; two parts are research problems; one is licence-gated** | Stock and web matching needs a licensed reverse-image index; cost per lookup is not in the research [no evidence found]. AI-image detection: the only figure is Kled's own claim (98.4% of bad actors within ten uploads). Server-side face analysis also moves the company off the on-device defence in G.T. v. Samsung (face-regulation.md Q1); whether detection without a template is a "scan of face geometry" is not addressed in the research [no evidence found] |
| 4 | In-app signed capture | Licence-gated, and off-thesis | iOS signing SDK licence and maturity are [unknown] in the variant. It captures new photos only. Kled already sells this class and it "excludes the archive by design" (ai-data-licensing.md Q5) |
| 4 | Ledger and revocation feed, no live payouts | Buildable as a mock | No buyer has agreed to honour a revocation feed. Kled's licence is "perpetual and irrevocable" (Q2) |
| 4 | "A datasheet for three design-partner buyers" | **Demand-gated** | No named buyer, RFP, price sheet or procurement term was found in two searches (ai-data-licensing.md unknown 5). Two engineers cannot build this line |
| Test | 20 volunteer libraries; hand-labelled 2,000-item sample | Possible, with a catch | Someone has to look at volunteers' private photos, including the people and children in them, to label ground truth. That contradicts "nothing has left the phone" and needs its own consent |
| Test | "A written price from any buyer" | **Demand-gated** | This is the only test that matters and it is a sales task with no lead list |

Summary: weeks 1–2 are a real four-week-class build on their own. Week 3 is two to three weeks of work. Week 4's commercial line cannot be built. The ugliest technical risk is the one the variant names: the screen's miss rate at scale. On the recomputed base corpus, 0.1% is about 707,000 items [estimated: 500,000 × 1,414 × 0.001].

## What breaks at 10,000 and at 500,000 suppliers

- **Fraud.** One region's 10-million-upload sample was 94.2% fraudulent (ai-data-licensing.md Q5). The provenance score is the variant's answer and it is unmeasured.
- **Support.** 27 of Kled's 100 most recent US reviews are one-star; themes are low pay, payouts stuck in review and bans at withdrawal (Q2). The variant budgets $0.50 a supplier.
- **Balances that never pay out.** At the realized-acceptance row a supplier needs three full sales to reach $25. Holding small balances indefinitely has consumer-protection and unclaimed-property implications that the research does not cover [no evidence found].
- **Data-loss liability.** Neon exposed recordings and phone numbers within a day of going viral (Q2). This product would hold opted-in originals with capture metadata, including location, for every supplier.
- **Deletion requests.** DROP runs every 45 days, 30 from 2027-01-01 (Q4). How a broker that deliberately holds no face index finds a bystander's image in a people-free corpus is not addressed [no evidence found].
- **Store removal.** One App Review decision under 5.1.2(i) or 5.1.2(vi) ends supply. Neither Kled nor Neon has been removed by Apple (Q4).
- **Buyer indemnities.** Getty indemnifies customers for release failures (Q4). A seed-stage company cannot carry that for a statistical screen. Cost of cover is [unknown].

## Most damaging objection

**The four-week demo proves the half of the loop that is already proven and cannot prove the half that is not.** Kled has already built the supply side at a scale this venture's base case only matches: 500,000 claimed contributors, a 200-million-file "Consented Camera-Roll Corpus", ID checks, face masking and a fraud detector, on $10M. Eight weeks ago it replaced the upload button with a task feed because the corpus was "the data people already had, not the data labs actually needed", and it pays contributors $0.01 a photo. The variant's additions (match before upload, a provenance score, an archive as the reason to stay) lower supply cost and, in the variant's own words, "none creates demand". The spec's only commercial deliverable is "a datasheet for three design-partner buyers"; the research found no buyer, RFP, price sheet or procurement term for this asset in two searches, and no revenue figure for personal still photos from anyone. After four weeks and $2.4M the company would own a smaller copy of an asset whose owner could not sell it.

## Weakest dimension

**Ceiling (2)**, tied with Platform risk (2). Ceiling is named because it is the dimension round 4 was meant to lift, and it did not: the variant's own centre ($4M gross, decaying) is below the leader's $3–12M ARR, and the repaired research raises price-list arithmetic to $6–24M without supplying a single buyer who has paid it. The scale test in the research is 2.0 billion image licences a year at $0.05 for $100M.

## Strongest dimension

**Buildability (5).** The supply-side engine is the index-only build that scored 6 in round 1, made easier by dropping face clustering, with no platform partnership and no storage cost until a sale. It loses a point against the leader because the loop needs a buyer to close, week 3 is overloaded, and the screen, the provenance score and AI-image detection are unmeasured research items.

## Unknowns research could resolve before the next round

1. Has any model builder or dataset buyer published, in 2026, a price, RFP, dataset card or procurement term for consented consumer camera-roll stills? Specifically: who has bought Kled's "Consented Camera-Roll Corpus (200M files)" and at what price per file, and what did GoPro's AI licensing program earn in Q3–Q4 2026 and for how many hours?
2. What false-negative rates are published for face, person and age detectors on consumer photos with small, occluded, background and child faces (for example recall on the WIDER FACE hard set for the detectors available on iOS, and under-18 error for open age estimators)?
3. Does server-side face detection without a stored template count as a "scan of face geometry" under Illinois BIPA or a "record of face geometry" under Texas CUBI? Search detection-only rulings since 2022, including Zellmer v. Meta (9th Cir.).
4. Has Apple rejected or removed any app under guideline 5.1.2(i) or 5.1.2(vi) for licensing photo-library content to AI developers, and what do Kled's (App Store id 6752585718) privacy labels declare as data shared with third parties?
5. What do commercial reverse-image or stock-match APIs and AI-image detection APIs charge per image in 2026, and what miss rates do they publish? Is the combined screening cost above or below a $0.03 image?

## Three questions for the founder

1. Can you name one data-partnerships or data-acquisition lead at a model builder who will take a call in the next two weeks and put a price for a people-free consumer camera-roll set in writing? If not, who on the team does buyer-side sales, and what have they sold to a lab before?
2. Are you willing to appear on California's public data-broker registry and to sign buyer indemnities for a statistical people screen, and how much runway is set aside for counsel, cover and compliance before the first purchase order?
3. If the first three buyers say what Kled and Wirestock heard ("we want capture to our spec, not your archive"), do you want to run a paid task marketplace? If not, what dated result ends this variant?
