# v4-data — round 4 critique — cold seed investor

Written 2026-11-25. Fresh context. Read: SCORECARD.md; variants/v4-data.md; research/ai-data-licensing.md in full (repaired version, including the audit log in its section 7); the sections of research/sizing.md (Q1, Q3, Q4, numbers table, worked chains), research/unit-economics.md (Q1–Q7), research/face-regulation.md (Q1–Q7, risk table) and research/ios-feasibility.md (Q1–Q9, feasibility table) that the variant cites; the bottom lines of frame-device-market.md, contents-claims.md, family-artifact-market.md and memoir-gift-market.md; the verdict or assumption sections of the remaining research files and research/assumptions/A1–A6; the first 80 lines of variants/current.md. Not read: CHANGELOG, other v4 variants, any critique, research/audits/. The remaining research files were not read line by line; nothing in them bears on data licensing (a search for Kled, Wirestock, training data, guideline 5.1.2 and data broker found the topic only in ai-data-licensing.md, with passing mentions in three others).

## Stance

Default no. Who pays, how much, why now, what is the wedge, what is the distribution, what must be true for $1B. This variant is a two-sided marketplace: consumers supply photos, model builders pay. My first test for any marketplace is evidence of demand-side budget for the specific thing being sold. There is none here, and the variant says so itself. I score what the evidence supports, not the candour.

## The variant was written before its research was repaired. The research wins.

The repair of research/ai-data-licensing.md withdrew or corrected inputs that carry the variant's arithmetic. Failed claims, in order of weight:

| # | Variant says | Repaired research says | Pointer | Effect |
|---|---|---|---|---|
| 1 | 12.7% of a roll is eligible, about 400 of 3,139 items | Withdrawn. Rebuilt by exclusion: 33.8% / 45.0% / 65.9%, base 1,414 items. Kled's realized acceptance is at most 20%, or 628 items | Q6 table, Q6 limits, audit item 20 | Every per-roll and Ceiling figure in the variant is built on a withdrawn number |
| 2 | One full sale grosses $12 per roll; owner gets $6 at 50% | Base $70.70 gross, $24.74 to the owner at 35%; bracket $10.80 to $331.04; at realized acceptance $18.84 at $0.03 | Q6 table, numbers rows 35–36 | Variant understates price-list value per roll by 1.6 to 5.9 times |
| 3 | Earnings per sale "$0.96 low, $3.00 base, $31.40 high" cited to the Q6 table | The Q6 table now reads $2.16 / $24.74 / $165.52 | Q6 table | Citation no longer matches its source |
| 4 | Freepik's $0.02–0.04 is the only closed per-image price | Adobe paid $0.06–0.16 per commissioned photo (secondary); research base price is now $0.05 | Q1 Adobe, audit item 17 | Price input is low, though Adobe's is a shot-to-brief price, not an archive price |
| 5 | "Private individuals' camera rolls: none disclosed by anyone" | GoPro disclosed $2M of AI content licensing revenue in Q2 2026 from opted-in subscriber video, 50% share. Stills remain [unknown] | Bottom line 1, Q1 GoPro, audit item 16 | The variant missed its closest precedent, which uses the same 50% split |
| 6 | Buyers "have stopped" buying stills; Shutterstock's data offering "fell 91% in Q3 2026" | 91% is one quarter. Nine months: down 60%. Q2 was down 11%. Shutterstock cites delivery timing | Q1 table, bottom line 3 | Overstated |
| 7 | Getty's Chapter 11 listed as demand evidence | "A balance-sheet event and is not evidence about demand"; Getty forecasts Other revenue back to $55M by 2029 | Q1 Getty, audit item 18 | Withdrawn as evidence |
| 8 | "Off-the-shelf stills demand peaked in 2025"; the window "is closing" | "Whether 2025 was the peak is [unknown]" | Bottom line 3, audit items 1, 21 | Not established |
| 9 | "A catalog sells to each large buyer once" cited to Q3 | Restated as an untested hypothesis; GoPro says footage "can be purchased more than once" | Q3 first bullet, audit item 21 | The ÷3 years and the "then only refresh" step are assumptions |
| 10 | Video at $0.55 a minute realized; video adds $1.8–12M a year | The $0.55 figure and "video holds better" are withdrawn. The only realized yield is GoPro's, at most $0.067 per opted-in minute | Q3 video, audit item 23 | Video line has no supported price |
| 11 | Delete Act: "$200 per consumer per day" for failure to register | Two separate fines: $200 per day unregistered; $200 per day per undeleted request | Q4 Delete Act, audit item 25 | Corrected |
| 12 | Photobucket was "the one platform that tried" | Six cases; EyeEm/Freepik changed terms, GoPro runs an opt-in and was paid | Q1 "Deals sourced from private individuals" | Precedent set is wider than stated |
| 13 | Paid acquisition "does not pay back": $14 CAC against $3.85 contribution | On repaired inputs, contribution per sale is about $6.60 at realized acceptance and about $30 at the research base [estimated: gross $18.84 or $70.70, 50% to owner, variant's cost lines scaled] | Q6; variant Economics table | Payback is 2.1 sales or 0.5 sale, conditional on a sale nobody has recorded |

Net effect: the repair moved the per-roll numbers in the variant's favour and added the one realized precedent. It added no buyer. Research Q6 states the limit directly: "No buyer is on record paying these prices for camera-roll photos." The verdict does not change.

Claims that rest on the variant's own fetches and are not in any research file, so I could not check them: Pixel 10 C2PA signing, Apple's "Reference Image" mode, the Google Photos training statement (search summary only), App Attest, Stripe Connect and Identity pricing, the Google Play photo-permission policy. They are tagged with URLs. None carries the Ceiling.

Claims that check out: 243M US adult smartphone users, 48% over 1,000 photos, 3,139 and 1,598 items, $2.79 CPI, about 80M paying households (sizing.md rows 11–17, 25, 30); R2 at $0.015, $0.69 per 22,000 images, 200 GB at $2.99, Ente 21,807 paid of 490,639 (unit-economics.md Q1, Q3, Q5, Q6); indexing 15 minutes floor and 38–57 minutes central, Camera kills the task (ios-feasibility.md Q2, Q3); subject-not-uploader consent under BIPA and CUBI (face-regulation.md Q1, Q2); Wirestock six buyers and $40M run-rate, Freepik two buyers, Kled's V3 quote, Nigeria 94.2%, Reklaim 78% (ai-data-licensing.md Q2, Q5, Q6).

## Ceiling, recomputed from the research-supported end of each input

Variant method: gross per year = suppliers × eligible items × price × buyers ÷ years.

| Input | Variant base | Research-supported end | Why |
|---|---|---|---|
| Suppliers | 500,000 | No evidenced figure for a US-only, iPhone-only entrant with no cash-first hook. 500,000 is Kled's unverified global claim; Kled has 1,971 US ratings and a footprint in Southeast Asia and Nigeria | ai-data-licensing.md Q2, Q5 |
| Eligible items per roll | 400 (withdrawn) | 628, the realized-acceptance ceiling; 1,414 is a price-list figure by exclusion | Q6 limits |
| Price per image | $0.03 | $0.02–0.04 for a bulk archive (closed, 2024, tagged stock). $0.05 is the research base but leans on a commissioned price. Kled pays contributors $0.01 | Q6, Q3 price trend |
| Buyers | 2 | 0 on record for personal stills. 2 is Freepik's count for a tagged stock archive | Q1, Q3 |
| Years | 3, bought once | Untested | Q3 |

| Case | Arithmetic | Gross per year | Company net |
|---|---|---|---|
| Low | 250,000 × 540 × $0.02 × 1 ÷ 3 | $0.9M | $0.45M at 50% |
| Realized acceptance | 500,000 × 628 × $0.03 × 2 ÷ 3 | $6.3M | $3.1M at 50% |
| Research price-list base | 500,000 × 1,414 × $0.05 × 2 ÷ 3 | $23.6M | $11.8M at 50%; $15.3M at a 35% owner share |
| Every input at its high end | 1,000,000 × 2,069 × $0.16 × 6 ÷ 5 | $397M | not credited |

All rows [estimated: my arithmetic on ai-data-licensing.md Q6 inputs and the variant's method]. The last row is not research-supported at any input: one million suppliers is twice an unverified global company claim; 65.9% assumes screenshots and people images overlap completely; $0.16 is the top of a shot-to-brief price; six buyers is Wirestock's count for mostly custom work.

Demand-side bound, independent of supply: what is disclosed in this neighbourhood in 2026 is Shutterstock DDS at $123.7M trailing twelve months (a ceiling that includes Giphy and Studios), Getty AI licensing at about $33M, Wirestock at a $40M run-rate (mostly custom), and GoPro at $2M in one quarter. About $200M in total, none of it for personal still photos. $100M would be half of all disclosed spend, taken by the one asset class with no disclosed revenue. The realized anchor for personal media is GoPro: 2.42M paying subscribers, 13M hours in its cloud, 500,000+ hours opted in, $2M in the single quarter disclosed and nothing itemized in Q3. Annualised that is $8M [estimated: 4 × $2M, if it repeated, which is not shown], for a public company that already had the corpus, the subscribers and the brand.

Research's own scale test: $100M gross is 2.0 billion image licences a year at $0.05, or 5.3 million roll-sales at realized acceptance. That is more than ten times Kled's claimed global contributor count selling a whole roll every year [estimated: 5.3M ÷ 500,000]. Kled's entire 200M-file corpus grosses $6M to $10M per full non-exclusive sale at $0.03 to $0.05.

Evidenced cap: $6–24M gross a year, $3–15M net to the company, transactional, with no recorded first sale. That sits at the bottom of the $5–45M band that has meant Ceiling 2–3 in earlier rounds, and it is not recurring. The variant's own "$4M" is too low on repaired inputs and is built on a withdrawn number; under the scoring rule that alone is a 2. Recomputed, it is still a 2.

## Scores

| Dimension | Score | Evidence pointer | One-line reason |
|---|---|---|---|
| 1 Pain | 3 | ai-data-licensing.md bottom line 1; Q3 "Stills from camera rolls"; Q6 limits; SCORECARD round-1 summary (v1-federation Pain 3) | Nobody is on record paying for this asset; the leader says labs do not need it; the supplier has no pain at all and gets AI search free from the platform |
| 2 Wedge | 3 | ios-feasibility.md Q2, Q3; ai-data-licensing.md Q2 (Kled reviews), Q3 | Supply side keeps its habits but must grant full-library access, sit through a 15–57 minute session the Camera kills, and pass an ID check for $6–25; the buy side has no first use case, it wants capture to a brief |
| 3 Why now | 4 | ai-data-licensing.md Q1 legal demand drivers; Q3; Q7 rows 2–3; bottom line 1 | Dated changes exist, but all five legal drivers are copyright or transparency drivers that do not create demand for personal photos, and the dated market signal (Kled, 2026-09-30) runs against; GoPro's Q2 2026 revenue is the one dated positive and the variant missed it |
| 4 Platform risk | 2 | ai-data-licensing.md Q4 (Apple 5.1.2(i), Google Play, Delete Act, FTC), Q1 (Meta at $0, GoPro, Photobucket), Q2 (Kled); face-regulation.md Q1, Q5 | Meta already takes opted-in camera rolls for nothing; any paid consumer cloud can copy GoPro's toggle; Apple's guideline text is a standing removal clause; Kled holds the corpus under an exclusive perpetual licence; data-broker registration contradicts the brand |
| 5 Compounding asset | 3 | ai-data-licensing.md Q3 (resale untested), Q5 provenance (C2PA "does not support attribution"); SCORECARD round-0 row 5 (index rebuildable for under $1) | Non-exclusive files leave with the first sale; the ledger shrinks with every withdrawal and DROP request; confirmed names, the seed's one asset, are excluded by design |
| 6 Distribution | 2 | ai-data-licensing.md Q5 (CNIL 3.9% under EUR 1 a month, 65% uncomfortable, fraud, r/beermoney removals), Q2 (Kled 1,971 US ratings), Q3 (no RFP, no buyer statement); sizing.md row 30 | The supply hook that is evidenced brings fraud and is the one the variant declines to use; the one evidenced channel from current.md is dropped; the buy side is a short list of accounts with no recorded purchase |
| 7 Economics | 4 | ai-data-licensing.md Q6 table and limits, broker margins; unit-economics.md Q1, Q3, Q7; sizing.md Q4 | Fully tagged and candid, 64–79% contribution margin, but the unit rests on a withdrawn input, fixed costs (indemnity, counsel, DROP) are omitted or [unknown], and revenue is per-transaction with sale frequency unobserved |
| 8 Buildability | 5 | ios-feasibility.md Q1–Q4, feasibility table; SCORECARD "Unknowns resolved" rows 4–5; ai-data-licensing.md Q4 Apple | No partnership or breakthrough needed and the on-device index is documented; the four-week plan is crowded (signed capture, server screen, buyer console) and the loop cannot be demonstrated end to end without a buyer and an App Review pass |
| 9 Ceiling | 2 | ai-data-licensing.md Q6 scale test, section 3 "Largest sourced annual revenue", Q1 GoPro; recomputation above | Evidenced cap $6–24M gross, $3–15M net, non-recurring, with zero recorded sales of the asset; the variant's own figure uses a withdrawn input |
| 10 Founder fit | 5 [unknown] | — | Placeholder |

**Total: 33** (leader: 47).

## Most damaging objection

The only party who would pay has already told the best-positioned seller that it does not want this asset, and the variant proposes to rebuild that seller's supply side from zero.

Kled has what this variant would spend its seed assembling: 500,000 claimed contributors, a 200M-file consented camera-roll corpus under an exclusive perpetual licence, ID checks, face masking, a fraud detector and $10M raised. On 2026-09-30 it moved its home screen away from camera-roll upload because that "could only collect the data people already had, not the data labs actually needed" (ai-data-licensing.md bottom line 1, Q3). No one has disclosed a dollar of revenue from licensing private individuals' still photos (section 3). The single realized number for any personal media is GoPro's $2M in one quarter, at most $4 per opted-in hour, 2% to 7% of creator list rates, from a company that started with 2.42M paying subscribers and 13M hours already in its cloud (Q1, Q3). The three largest potential buyers own camera-roll platforms and one of them collects opted-in rolls for $0 (Q1).

What the variant adds (matching before upload, a library-context provenance score, a non-cash reason to keep the app) improves supply quality. Supply is not the constraint: the variant's own pool is 97 billion eligible items and the research-corrected figure is larger. A better supply side for a product with no recorded buyer is not a company. The variant reaches the same conclusion in its own words ("the payer exists, but not for this asset"), and the repaired research, which is more favourable per roll, does not overturn it.

## Weakest dimension

**Ceiling (2)**, tied at 2 with Platform risk and Distribution. Ceiling is the binding one because it fails on the demand side, which no product change in the variant addresses: $100M needs 2.0 billion licences a year or 5.3 million roll-sales, and the whole of Kled's corpus is worth $6–10M per full sale.

## Strongest dimension

**Buildability (5)**, excluding the founder-fit placeholder. The on-device index needs no platform partnership, and the route is documented: PhotoKit previews at about 1536×2048, a user-started session of 15 to 57 minutes for 30,000 photos, SigLIP 2 or TinyCLIP under permissive licences (ios-feasibility.md Q3, Q4; SCORECARD unknowns rows 4–5). The better reason is what the demo measures. The four-week plan ends in four numbers that decide the idea and that no source publishes: the eligible share of 20 real libraries, the people-and-minors miss rate on 2,000 hand-labelled items, the catch rate on 500 planted images, and one written price from a buyer. Research lists the first as an open unknown (ai-data-licensing.md unknown 8). That is a cheap, honest kill test, and it is the only part of this variant worth money.

## Unknowns research could resolve before the next round

1. Has any AI lab, robotics company or dataset buyer published or been reported paying a per-image price for consented personal camera-roll stills in 2026: an RFP, a dataset card, procurement terms, or a named Kled buyer and Kled revenue figure?
2. What did GoPro's AI content licensing programme earn after Q2 2026, at what price per hour, how many of the 500,000+ opted-in hours were actually licensed, to whom, was any footage bought more than once, and what share of invited subscribers opted in?
3. Is there any measured breakdown of real phone camera rolls after the 2019 Thomson study (n above 100 libraries) giving the shares with identifiable faces, minors, screenshots, documents and receipts, near-duplicates, and minutes of video?
4. Has Apple or Google rejected or removed any app in 2025–2026 for licensing users' photos, audio or video to third-party AI trainers under App Review guideline 5.1.2(i) or the Play User Data policy, and what did the developer change to get back in?
5. Are Kled (Nitrility Inc.), Wirestock, Troveo or GoPro listed on the California data-broker registry, and has the CPPA said whether licensing a consumer's own photos that incidentally show other people makes the marketplace a data broker?

## Three questions for the founder

1. Before any code: which data-partnerships lead, by name, will put a per-image price in writing for a 1,000-item people-free camera-roll sample, and what specification did they ask for? If the specification is capture to a brief, why is this not simply a late entry against Kled and Wirestock?
2. The seed's promise was "user-owned, private". Are you prepared to appear on California's public data-broker registry and to sign buyer indemnities for a screening miss, when a 0.1% miss rate on a 200M-item corpus is 200,000 items and one of them can be a child's face? What is the indemnity budget, and who underwrites it?
3. If a buyer does exist, GoPro has shown the winning shape: an existing paid cloud, an opt-in toggle and a 50% share. Why does an app that must acquire every supplier at $7–28 beat Apple, Google, Amazon, Dropbox, Shutterfly or Ente adding that toggle, and what do you own in month 24 that Kled cannot ship in one release?
