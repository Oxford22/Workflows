# v4-claims — The contents claim from the camera roll

Written 2026-11-25 for round 4. Research base: `research/contents-claims.md` (written the same day; read in full before the dependent sections were drafted). Numbers this variant fetched itself and that no research file carries are marked "own fetch, 2026-11-25"; critics should not let a score rise on them. Where this file and the research file disagree, the research file wins.

**Verdict up front.** The pain is the most acute of any variant so far and the camera-roll evidence is real. The business is not: a funded team (Bevel) already builds the inventory from old family photos, free, and reached more than 25% of Los Angeles fire survivors [sourced-secondary: contents-claims.md 2.4]; the national pool is about 40,000–80,000 households a year [estimated: contents-claims.md 2.2]; statutes are shrinking the job. $100M does not pencil. Honest ceiling: **$0.5–5M ARR, central about $1.5M** [estimated: Ceiling section]. This is a module or a feature, not a company.

## One line

After a fire, theft or flood, each household member and relative runs an on-device search of their own photo library for pictures taken at the lost home; only the photos they approve are uploaded; a vision model turns them into a room-by-room item list in which every line carries the photo and capture date that proves it; the household confirms, prices and exports it in the insurer's format.

## Customer (payer, user, supplier or audience; how many [tagged]; what they do today; what they pay today)

**Payer.** First: the professional already paid to work the claim (public adjuster, policyholder attorney, independent contents specialist), per claim file or per seat. Second: the household, for a flat fee. Later and unproven: carriers. **User:** the policyholder. **Suppliers:** household members and relatives, who contribute photos from their own phones.

**How many.**
- Homeowners policy base: about 61.6M HO-3/HO-5 policies [estimated: 49.3M policies in Treasury's dataset ÷ 0.80 premium share; contents-claims.md 2.2]. Renters and condo counts [unknown: contents-claims.md §5].
- Claims a year: property damage about 3.4M; fire and lightning about 129,000 at a mean severity of $101,092; theft about 68,000 at $6,184 [estimated: 61.6M × Verisk/ISO 2020–2024 frequencies 5.48, 0.21 and 0.11 per 100 house-years; sourced severities: iii.org via contents-claims.md 2.2].
- Households a year whose contents loss is large enough (≥ $25,000) to need a detailed list: **40,000–80,000, central 60,000**; hard upper bound 130,000–150,000 in a peak catastrophe year [estimated: contents-claims.md 2.2; the 25–50% share of fire claims above the threshold is that file's assumption, not a sourced figure]. Cross-check on the catastrophe part: wildfires have destroyed more than 130,600 structures since 2005, about 6,200 a year [sourced: https://headwaterseconomics.org/natural-hazards/structures-destroyed-by-wildfire/, updated 2026-04, own fetch 2026-11-25; estimated: 130,600 ÷ 21 years].
- Of those, the share still asked to itemize after statutory and voluntary advances: roughly half to three-quarters, from one event (Los Angeles, 12 months: 53% must list every item; 27% received 100% with no list) [sourced: United Policyholders 12-month LA survey, 2026-03, via contents-claims.md 2.1].
- Share with usable pre-loss interior photos across household and relatives: [unknown: no survey found; contents-claims.md §5]. This is the variant's central factual gap.
- Professional buyers: 1,697 active Texas public-adjuster licences in mid-2026 [sourced-secondary: claimos.net via contents-claims.md 2.3]; NAPIA about 600–750 members [sourced-secondary: contents-claims.md 2.3; search excerpt of an undated article, own search 2026-11-25]; national count [unknown]. Licensing exists in 46 states [sourced: https://www.napia.com/uppa, own fetch 2026-11-25].

**What they do today.** Write the list from memory into a spreadsheet, room by room. In the Department of Angels survey of 2,443 adults in the Los Angeles fire areas, 51% of insured respondents said itemization had been difficult, the most common problem named [sourced-secondary: uphelp.org repost dated 2026-03-27 of a press summary of the January 2026 report, own fetch 2026-11-25]. United Policyholders already tells survivors that "Friends and family may have photos taken inside your home", and lists negotiating a cash-out "at or just below your contents policy limits" among its timesavers, to avoid the list altogether [sourced: uphelp.org home-inventory tips via contents-claims.md 2.5; page re-read 2026-11-25]. Of 540 Los Angeles respondents, 15.9% hired a public adjuster, 16.1% an attorney, 7.8% a contents specialist, 43.7% no one; 18% were sent a specialist by the carrier [sourced: UP 12-month summary data, contents-claims.md 2.3, 2.1]. More than 25% of Palisades and Eaton survivors used Bevel, which is free to them [sourced-secondary: contents-claims.md 2.4].

**What they pay today.** Public adjusters: 10–20% of recovery, capped at 10% in Texas and in Florida emergencies [sourced: Tex. Ins. Code §4102.104; F.S. 626.854(11)(b) via contents-claims.md 2.3]. Contents specialists: $800–8,000 flat [sourced-secondary, low quality: contents-claims.md 2.3]. Paid AI tools: ProofList $59 (50 photos), $149 (150), $279 (300), $499 (unlimited), one-off, 25 photos free [sourced: https://proof-list.com/, own fetch 2026-11-25]. Professional tool: Contents.team $299 per organization per month, 1,000 items included, then $0.80 an item, exports "XactContents-format XLSX and PDF" [sourced: https://contents.team/blog/encircle-alternative, 2026-05-11, own fetch 2026-11-25]. Bevel: $0 [sourced: bevelmade.com via contents-claims.md 2.4; home page re-read 2026-11-25]. No forum post was found in which a household paid a stand-alone fee for an inventory tool after a loss [sourced: contents-claims.md 2.5].

## Wedge (first use case adopted without changing habits; the first 10 minutes for each party; day-1 value; day-30 value)

**First use case.** The household must produce the list anyway and is already told to look through old photos. The product replaces scrolling years of camera roll with one query. No library is migrated, no archive is built, nobody changes where their photos live.

**First 10 minutes, household lead.** Install the iOS app; enter the loss address and the years lived there; grant library access. The app asks PhotoKit for assets whose stored location falls inside a radius of the address within those dates (a metadata query, no model), then runs Apple's free on-device scene classifier to separate interiors [sourced: research/ios-feasibility.md feasibility table, "Image labels without NPU: Vision classification (free)"]. Wall-clock for the metadata query on a 30,000-item library: [unknown: not measured; expected to be far below the 38–57 minute embedding pass in ios-feasibility.md Q3, which is only needed for photos with no location]. The lead sees a grid grouped by visual similarity, answers "which room is this?" for each group, deselects anything private, and uploads the rest. By minute ten the first room has a draft item list with thumbnails.

**First 10 minutes, relative.** Opens an invite link, installs, and runs the same query with the address already filled in. They see only their own matching photos, approve the ones to contribute, and are done. Nothing else leaves their phone. Android relatives and anyone who declines the app use a web upload of hand-picked photos; that path has no location search (the Google Photos Picker strips GPS) [sourced: variants/current.md Why now 1; research/platform-access.md Q4].

**First 10 minutes, professional.** Creates a claim file, texts the invite to the client, and watches evidence arrive by room. They edit lines, set age and condition, and export.

**Day-1 value.** A room-by-room evidence gallery and a draft item list, free. It is a memory aid even if no line is ever priced.

**Day-30 value.** A deduplicated, priced, attested schedule (quantity, description, brand, age, original cost, replacement cost, source, photo and capture date per line) submitted before the proof-of-loss date, which in California cannot be set sooner than 100 days after a state-of-emergency loss [sourced: Cal. Ins. Code §2051.5 via contents-claims.md 2.1]. In California the list is what unlocks the last 40% of the contents limit after the 60% advance [sourced: §10103.7(b) via contents-claims.md 2.1; confirmed in the Department of Insurance 2026 Annual Notice, 2026-01-09, own fetch].

**Honest limits of the wedge.** (1) A photo proves an item existed on a date, not that it was present or undamaged at the loss; one insurer refused a ring shown in pre-loss photos [sourced: reddit thread 1lx99dn via contents-claims.md 2.5]. (2) 24% of Los Angeles respondents had to state when or where each item was obtained [sourced: contents-claims.md 2.6]. (3) Candid photos do not show the insides of closets, drawers and kitchens, where much of the item count sits; the share of contents value that candid photos recover is [unknown: no study; the 4-week demo measures it].

## Why now (dated changes since 2024, each tagged)

1. **2025-01: Palisades and Eaton fires.** More than 16,000 structures destroyed; 38,737 residential claims; $23.41B paid on them by July 2026 [sourced: UCLA Lewis Center 2025-02; CDI 2026-07 via contents-claims.md 2.2]. The itemization problem became a public issue.
2. **2025-10-10: California SB 495 signed; in force 2026-01-01.** Insurers must offer at least 60% of the contents limit, up to $350,000, without an itemized claim after a state-of-emergency total loss; the insured may itemize for the rest; policy forms comply from 2026-07-01 [sourced: Cal. Ins. Code §10103.7 via contents-claims.md 2.1; CDI 2026 Annual Notice, own fetch]. Colorado is at 65% (2022) and Oregon at 70% (2023) [sourced: C.R.S. 10-4-110.8; Or. Laws 2023 ch. 85 via contents-claims.md 2.1]. This cuts against the variant: each step removes the households with least to gain from a list.
3. **2025-01 to 2026-08: Bevel.** Built within hours of the Palisades fire; extracts items from old family photos, videos and receipts; free to survivors; then raised a $6M seed to become a high-net-worth brokerage [sourced: bevelmade.com; sourced-secondary: devcuration.com 2026-08-28 via contents-claims.md 2.4]. Proof of demand, and proof that the best-adopted team does not charge for the inventory.
4. **2025-12-17: Encircle shut its free consumer inventory app** to focus on paid contractor software [sourced-secondary: contents-claims.md 2.8].
5. **2026: paid photo-to-schedule tools appeared.** ProofList (founded after the Los Angeles fires) and Contents.team (comparison post 2026-05-11) [sourced: own fetches above]. Photo-to-priced-line is now a commodity step.
6. **2026-03-30: a public step-by-step guide shows a survivor building the inventory with a general AI assistant** from a folder of photos, receipts and order history [sourced: https://davidbramante.substack.com/p/lost-your-home-in-a-fire-use-ai-to, 2026-03-30, own fetch]. The general assistant is a substitute.
7. **2026: manipulated claim media.** NICB's 2026 threat assessment reports mentions of AI in questionable claims up more than 1,400% from 2025 to mid-2026; a Verisk survey found 36% of consumers would consider altering a claim image [sourced-secondary: search excerpts of a 2026-11-16 trade report and a March 2026 Verisk study, own search 2026-11-25; neither page was read directly]. Dated, device-origin evidence per line is the one thing this variant adds that incumbents do not stress [sourced: contents-claims.md 2.6].
8. **Cost.** Listing the objects in one photo with a mid-tier vision model costs about $0.003–0.007 [estimated: 1,120 image + 300 prompt tokens in, 600 out, at Gemini 3.6/3.8 Flash $0.75/$3.75 per 1M through 2026-12-31 and $1.50/$7.50 after; prices sourced in research/unit-economics.md Q3].

Could it have been built in 2019? The location query, yes. The item extraction at this cost, no. The demand-side change (items 1–3) helps a free incumbent more than a new paid entrant.

## Product (core loop; explicitly NOT in v1)

**Core loop.**
1. **Claim file**: address(es), dates of residence, type of loss, carrier, state. State decides which mode is offered (see regulatory risk).
2. **On-device search** per participant: location radius + date range from PhotoKit metadata; scene filter; optional embedding pass (SigLIP 2, Apache-2.0 [sourced: research/unknowns-r1.md Q5]) to find look-alike rooms among photos with no location. Nothing is uploaded at this step.
3. **Human selection**: the participant approves photos; rooms are named by a prompted person, never inferred.
4. **Upload of approved photos only**, downscaled; device-size local copies are about 1536×2048 and are enough for object listing without pulling originals from iCloud [sourced-secondary: research/ios-feasibility.md Q4, one field measurement; estimated sufficiency].
5. **Item listing** by a vision model: one line per object with the source photo, crop, capture date and contributor.
6. **Instance merge**: the same sofa in dozens of photos becomes one line with all of them attached as evidence; the household confirms merges and quantities.
7. **Household review**: add what no photo shows, set age and condition, accept or replace price suggestions with a linked comparable. Every line is attested by the policyholder; lines with no evidence are marked "from memory".
8. **Export**: spreadsheet and PDF in the columns adjusters use; grouped categories where the state requires insurers to accept them (California §2061(a)(3)) [sourced: contents-claims.md 2.1]; an evidence appendix with capture dates and file hashes.

**Explicitly NOT in v1.** Any percentage-of-recovery price; staff who build the list or speak to the insurer; coverage advice; Florida done-for-you service; face recognition of any kind (faces are detected on device only to blur them in the export; whether detection alone raises a biometric issue is not settled in research/face-regulation.md and is treated as [unknown]); storage of anything except approved photos, deleted when the claim closes or at 36 months (California's replacement-cost window [sourced: §2051.5 via contents-claims.md 2.1]); an Android app; a pre-loss subscription; price guarantees; generated or enhanced images.

## Business model and pricing (with comparables, tagged)

- **Household: search, gallery and draft list free; $199 flat for the priced, attested export** [estimated: between ProofList's $149 and $279 tiers; own fetch]. The free part has to exist because Bevel is free [sourced: contents-claims.md 2.4]. Whether anyone pays $199 beside a free alternative is unproven [unknown].
- **Professional: $299 per organization per month, or $199 per claim file** [estimated: matched to Contents.team's $299 with 1,000 items; own fetch]. Carrier-side job prices are lower: Verisk ContentsTrack $36–45 a job; XactContents $950–1,900 a seat-year [sourced and sourced-secondary: contents-claims.md 2.3].
- **Share of incremental recovery: not offered by the company.** In California a public adjuster is anyone who "for compensation, acts on behalf of or aids in any manner, an insured in negotiating for or effecting the settlement of a claim"; Florida covers anyone who "for money ... directly or indirectly prepares, completes, or files an insurance claim" [sourced: Cal. Ins. Code §15007; F.S. 626.854(1) via contents-claims.md 2.6]. The NAIC model's own wording is "Acts or aids ... on behalf of an insured in negotiating for, or effecting the settlement of, a claim", with an optional 10% catastrophe cap and a drafting note that "A majority of the states do not require a cap on fees" [sourced: NAIC Model 228 text, 2005–2006 copy at https://insurance.maryland.gov/Producer/Documents/NAIC-MODEL-LAW-PUBLICADJUSTERS.pdf, own fetch; the research file could only reach a search excerpt]. NAPIA lists "Requests a percentage of your insurance settlement for 'claim help'" as a red flag for unlicensed practice and says only a licensed adjuster or attorney may represent an insured "in the preparation, presentation, or negotiation" of a claim [sourced: https://www.napia.com/uppa, own fetch]. A contingent price therefore belongs to licensed adjusters who use the tool and charge their own capped fee. Running a licensed contents-only adjusting firm is a different company (see Ceiling, sensitivity).
- **Carriers (later):** per job, only if the evidence trail cuts cycle time or fraud referrals; price [unknown: what carriers pay Enservio per claim is undisclosed, contents-claims.md 2.7].
- **Pre-loss tool:** free, not a revenue line. A dozen-plus AI inventory apps sell below $60 a year with no disclosed traction; sponsor-funded ones were abandoned [sourced: contents-claims.md 2.4, 2.8].

## Distribution (non-paid channels with evidence; one paid channel with CAC math if any)

**Non-paid.**
1. **Policyholder nonprofits.** United Policyholders recommended Bevel at a workshop and hosts live events and webinars for survivors; Bevel runs its own WhatsApp group [sourced: contents-claims.md 2.4; bevelmade.com home, own re-read]. This channel works, and it is occupied by a free tool with a United Policyholders liaison quoted on its home page.
2. **Public adjusters, attorneys, contents specialists.** They served 15.9%, 16.1% and 7.8% of Los Angeles respondents [sourced: contents-claims.md 2.3]. At a capped contingency they gain from a fuller contents line and already pay for software (Contents.team). Few buyers; their software spend is [unknown].
3. **The invite itself.** Each claim file asks several relatives to install. It is a loop only inside a disaster zone, where neighbours share tools; outside one, the relatives have no claim of their own.
4. **Restoration contractors and insurance agents.** Weak. Contractors photograph what survived, not pre-loss rooms [sourced: contents-claims.md 2.7]. No evidence found that agents refer claim tools [unknown].
5. **Free pre-loss tool as lead generation: the arithmetic fails.** A household's chance of a large contents loss in a year is about 0.1% [estimated: 60,000 ÷ 61.6M]. One million installs would yield about 1,000 such losses a year [estimated: 1,000,000 × 0.097%], before retention.

**One paid channel, with math.** Search ads on post-loss queries. Contribution on a $199 sale is about $146 (Economics), so break-even CAC is $146 and, at a 2% click-to-purchase rate, break-even cost per click is about $2.90 [estimated: 146 × 0.02; the 2% is an assumption]. Actual cost per click for these keywords is [unknown: research/sizing.md Q5, every keyword route failed]; the other bidders are public adjusters and attorneys whose fee on one claim is thousands of dollars, so the price is likely above break-even. The only sourced photo-app CAC is $35 and the derived band is $65–90 [sourced and estimated: research/sizing.md Q4]. There is no repeat purchase to recover a miss.

**Between disasters.** Single-house fires are the steady base: about 129,000 fire and lightning claims a year, roughly 350 a day, spread nationally [estimated: 129,000 ÷ 365]. They are reachable only through professionals who already see them, which is why the professional seat comes first. Catastrophes arrive without schedule; one Florida audit saw public-adjuster licences rise 77% in a year after four hurricanes [sourced-secondary: contents-claims.md 2.8]. A seed-stage team has to hold costs flat through quiet years and cannot plan revenue on the peaks.

## Economics (per-customer or per-unit COGS; GM; payback; capital needs; cite research rows or derive with tags)

Per claim file, central case of 1,500 approved photos and 500 item lines. Items per household are anchored on Bevel's "3M+ items" across an implied 4,000–10,000 households, i.e. 300–750 [estimated: 3,000,000 ÷ 4,000 to 10,000; contents-claims.md 2.4].

| Cost line | Low | Central | High | Tag |
|---|---|---|---|---|
| Item listing (500 / 1,500 / 3,000 photos) | $1.65 | $9.90 | $19.80 | [estimated: $0.0033–0.0066 per photo, Why now 8] |
| Price lookups (300 / 500 / 750 items) | $3.00 | $10.00 | $30.00 | [estimated: $0.01–0.04 per item, an assumption; grounded-search price not in research] |
| Storage of approved photos, 36 months | $0.80 | $2.40 | $4.90 | [estimated: 1.5 / 4.5 / 9 GB × $0.015 per GB-month × 36; R2 price sourced in research/unit-economics.md Q1] |
| Card fee on $199 | $6.07 | $6.07 | $6.07 | [estimated: 2.9% + $0.30; sourced in unit-economics.md Q7] |
| Support | $10 | $25 | $50 | [estimated: assumption; a customer who has just lost a home] |
| **Total** | **$21.50** | **$53.40** | **$110.80** | [estimated: sums] |

- **Gross margin at $199:** 89% / 73% / 44% [estimated: (199 − total) ÷ 199]. Contribution, central: $146.
- **Free users are the real cost.** If nine households use the free gallery and draft list for each one that buys the export, and the free tier runs the item listing, compute adds about $9.90 × 9 = $89 per paid file and margin falls to about 28% [estimated: (199 − 53.40 − 89.10) ÷ 199; the 9:1 ratio is an assumption]. The free tier must therefore stop before item listing for most photos, which weakens it against Bevel.
- **Professional seat:** $3,588 a year; a firm running 24 claim files a year costs about $22 each in compute and storage, so gross margin is about 85% before support [estimated: (3,588 − 24 × 22) ÷ 3,588; 24 files is an assumption].
- **On-device search:** no server cost; originals stay where they are, as in the index-only row of research/unit-economics.md Q7.
- **Payback:** one-off purchase, so payback is the day of sale if CAC is below $146 [estimated: table above], and never otherwise. No retention, no LTV beyond a second claim.
- **Capital:** two engineers and one claims-literate founder for 18 months is about $0.9M [estimated: 3 × $200,000 loaded × 1.5 years; an assumption]. The spend is small; the problem is that revenue at the central ceiling does not cover it either.

## Platform, incumbent and regulatory risk (the obvious move by Apple, Google, Amazon or the category leader; the law that could close this; why this survives or doesn't)

- **Category leader.** Bevel accepts uploads of old family photos today and could add "invite relatives" and per-line dates in weeks; the research file says so in terms: "These are features Bevel could add in weeks; they are not a company" [sourced: contents-claims.md 2.8]. Bevel has the nonprofit channel, press, SOC 2, carrier contacts and $6M, and gives the tool away to feed a brokerage.
- **Apple and Google.** Both libraries already search by place and date; a survivor can search the address in Photos, select all and share. Apple's guideline 5.1.1(iii) steers apps to the picker instead of full-library access [sourced: research/memory-product-sdk.md Q6], and a user may grant only limited access, which removes the automatic search and leaves this product equal to an upload form. Neither platform needs to ship anything for the differentiator to be thin.
- **General assistants.** The 2026-03-30 guide (Why now 6) shows the whole job done with a general assistant and a folder.
- **The law that could close it.** California's bill began at 100% of contents without a list and was amended to 60% [sourced-secondary: contents-claims.md 2.1]. If states move to 100% for declared disasters, the catastrophe segment vanishes and only single-house fires remain (Colorado already requires 30% on any total loss) [sourced: contents-claims.md 2.1].
- **Licensing.** Florida's wording reaches paid preparation "regardless of how that person describes" the service. Self-serve software for a flat fee is how Bevel, ProofList and the apps operate and no enforcement was found, but no regulator has opined either [unknown: contents-claims.md 2.6]. The pro edition is sold to licence holders, which is the safe side.
- **Carrier incentive.** A fuller list raises indemnity on the coverage where under-claiming is routine; carrier vendors sell cycle time and fraud detection, not larger payouts [sourced-secondary: contents-claims.md 2.7]. Expect neutrality at best. About 14 insurer groups declined even the voluntary 75% advance in Los Angeles [sourced: CDI list of 2025-03-05 via contents-claims.md 2.1].
- **Fraud exposure.** Contents is a known soft-fraud line (38% in one survey admitted overstating a home claim) and carriers screen lists line by line [sourced-secondary: contents-claims.md 2.6]. A tool that surfaces every background object invites that scrutiny and could be named in a padded claim. Controls: no line without either evidence or an explicit "from memory" mark; policyholder attestation per export; original capture metadata and hashes kept; no image generation or enhancement; prices always linked to a dated comparable.
- **Location reliability.** How accurate a phone's stored photo location is indoors was not found for photo metadata [unknown: one search and a NIST conference paper, no usable figure, 2026-11-25]. Research prototypes report roughly 2–3 m with dedicated Wi-Fi or beacon methods [sourced-secondary: search excerpt of arXiv 2006.02251], which says little about a camera roll. The design does not rely on precision: a wide radius, a scene filter, and a person confirming each room. Photos saved from Messages reach the library only if auto-save is on, and whether their metadata survives is [unknown: research/unknowns-r1.md Q3]. The share of a library with no location at all is [unknown].
- **Survives?** As a company, no. As the evidence step inside someone else's claim workflow, yes.

## Compounding asset

- **Per household:** an evidence-linked inventory that is useful for up to 36 months of replacement-cost claims in California [sourced: §2051.5 via contents-claims.md 2.1], then again as the starting inventory of the rebuilt home. One event per household per decade or longer.
- **Per professional:** claim files, carrier-by-carrier notes on what format and evidence each adjuster accepted. Modest switching cost.
- **Company level:** an item-to-price table with accepted comparables. Enservio has "more than $10 billion in contents claims history" and Bevel "3M+ items" [sourced: contents-claims.md 2.3, 2.4]; a new entrant starts at zero and behind.
- **What does not compound:** the pooled family corpus. It is collected for one claim and deleted. The seed's asset (a living, confirmed family archive) is used once here and thrown away. This is weaker than the organizer's client ledgers in `variants/current.md`.

## Buildability (4-week demo spec for 2 engineers; ugliest technical risk; what is platform-, policy- or licence-gated)

**Demo (iOS 27 app + web review, two engineers).**
- Week 1: claim file, invite links; PhotoKit location-and-date query; Vision scene filter; selection grid; upload of approved, downscaled photos.
- Week 2: item listing with crops, capture date and contributor per line; room naming by prompt; web review board for the household.
- Week 3: instance merge across photos and contributors (embedding similarity on crops + same room + human confirm); quantity handling for grouped categories; price suggestion with linked comparable.
- Week 4: export (spreadsheet + PDF + evidence appendix with hashes); test on five intact homes: build the inventory from the family's camera rolls, then walk the house and count.
- **Acceptance:** measured share of walk-through replacement value recovered from candid photos (the unknown the whole variant rests on); duplicate lines under 5% after human merge [estimated: threshold is a judgment]; zero lines without evidence or a "from memory" mark.

**Ugliest technical risk: instance identity and time.** The same lamp appears in sixty photos over nine years; the sofa was replaced in 2021; the bicycle in the hallway belonged to a guest. The tool must produce one line per owned object as of the loss date, and a wrong merge either under-claims or pads. No shipped tool was found that documents how it handles this [unknown]. Second: recall. If candid photos recover a small share of contents value, the product is a memory aid, not an inventory.

**Gated.** Platform: full-library permission and review under guideline 5.1.1(iii); the unattended embedding pass needs a foreground session that the Camera app kills [sourced: research/ios-feasibility.md Q2–Q3]; Android deferred, so mixed-platform families fall back to manual upload. Policy: none for the flat-fee self-serve tool, on current reading. Licence: any contingent fee or done-for-you service needs a public-adjuster licence per state.

## Ceiling (path to $100M ARR with tagged inputs and arithmetic; or the honest number it tops out at)

**Line A, households, flat fee.** Pool × still itemizing × usable photos × paying share × price.

| Case | Pool | Still itemizing | Usable photos | Paying | Price | Revenue |
|---|---|---|---|---|---|---|
| Low | 40,000 | 53% | 50% | 7.8% | $149 | $0.12M |
| Central | 60,000 | 63% | 50% | 10% | $199 | $0.38M |
| High | 80,000 | 73% | 50% | 25% | $279 | $2.04M |

Tags: pool [estimated: contents-claims.md 2.2]; itemizing share [sourced: 53% must list every item, 73% did not receive 100%, one event]; usable photos [unknown; 50% is the research file's assumption]; paying share low = share who hired a contents specialist [sourced], high = Bevel's adoption when free, applied to a paid product, which is generous [estimated]; prices [sourced: ProofList tiers, own fetch]. Arithmetic: 40,000 × 0.53 × 0.5 × 0.078 × 149 = $123,000; 60,000 × 0.63 × 0.5 × 0.10 × 199 = $376,000; 80,000 × 0.73 × 0.5 × 0.25 × 279 = $2,037,000. Every case assumes national reach of every such household.

**Line B, professionals.** Large-loss households already served by an adjuster, attorney or contents specialist: 60,000 × 39.8% ≈ 23,900 [estimated: 15.9 + 16.1 + 7.8, Los Angeles shares applied nationally, overlap ignored; both are stretches]. At 10–30% reach [estimated: assumption] and $150–300 per file [estimated: Contents.team's $299 a month spread over 1–2 files]: 23,900 × 0.10 × 150 = **$0.36M** to 23,900 × 0.30 × 300 = **$2.15M**; central 20% × $200 = $0.96M.

**Line C, carriers.** Every fire and lightning claim at ContentsTrack's job price: 129,000 × $36–45 = $4.6–5.8M at 100% [estimated]. Reach 0–10% with incentives against: **$0–0.6M**; $0.2M is carried in the central total as a judgment, not a derivation.

**Line D, pre-loss.** $0 (Distribution 5).

**Honest total: $0.5M–$4.8M ARR, central about $1.5M** [estimated: 0.12 + 0.36 + 0; 0.38 + 0.96 + 0.2; 2.04 + 2.15 + 0.58].

**Sensitivity.** (a) Hard upper-bound pool in a peak year, high case otherwise: 150,000 × 0.73 × 0.5 × 0.25 × 279 = $3.8M on line A [estimated]. (b) Every large-loss household pays $300: 60,000 × 300 = $18M; at the hard upper bound, 150,000 × 300 = $45M [estimated: contents-claims.md numbers table for the first]. (c) Become a licensed contents-only adjusting firm at 10% of the increment: households that hire a public adjuster ≈ 60,000 × 15.9% = 9,540 a year [estimated]; at a 5% share (477 files) and a $5,000–10,000 fee [estimated: 10% of half to all of a $100,000 increment, i.e. 40% of an assumed $250,000 contents limit; the limit is illustrative, no average is published] → $2.4–4.8M of lumpy services revenue under per-state licences and 10% caps in Texas and Florida emergencies.

**$100M check.** At $279 it needs 358,000 paying households a year, 2.4–2.8× the hard upper bound of every fire claim plus a peak catastrophe year [estimated: 100,000,000 ÷ 279; ÷ 150,000 and 130,000]. It does not pencil under any input the research supports.

**Largest sourced revenue of any comparable:** none is primary-sourced. Third-party estimates for Enservio, after 20-plus years and 250-plus carriers, run $41–56M [low-quality estimators, never relied on alone: contents-claims.md §3]; Encircle about $9.9M [single low-quality estimator]; Bevel reports no revenue from its inventory tool and pivoted to brokerage [sourced-secondary: contents-claims.md 2.4].

**Regression statement.** Ceiling does not improve on `variants/current.md` ($3–12M [estimated: its Ceiling section]); the central case here is lower.

## Load-bearing assumptions (numbered; each with the observable fact that would falsify it)

Every threshold below is a judgment call set by this variant [estimated: assumption], not a sourced benchmark.

1. **Pooled camera rolls recover a large share of contents value.** Falsified if the five-home test recovers under 40% of walk-through replacement value from candid photos.
2. **Relatives' photos add materially to the household's own.** Falsified if, in the same test, relatives' contributions add under 10% of evidenced lines.
3. **Location metadata finds the home's photos.** Falsified if under 60% of a test family's known at-home photos are returned by the radius-and-date query, or if most participants grant only limited library access.
4. **Someone pays beside a free Bevel.** Falsified if, in the first disaster zone served, fewer than 5% of households who build a free draft buy the export, or if Bevel ships relative invites and per-line dated evidence.
5. **Professionals buy per file.** Falsified if 20 interviews with public adjusters, attorneys and contents specialists yield fewer than 5 willing to pay $150 or more per claim file, or if Contents.team adds client-side camera-roll collection.
6. **Insurers accept photo-derived lines.** Falsified if pilot claims show adjusters routinely rejecting lines whose only proof is a dated candid photo, or demanding purchase date and place for most lines.
7. **Flat-fee self-serve software is not public adjusting.** Falsified by a department of insurance bulletin or enforcement action against any inventory tool, most likely in Florida.
8. **Statutes stop short of 100%.** Falsified by a chaptered bill in California, Colorado or Oregon requiring full contents limits without itemization after declared disasters.
9. **Instance merge can be made trustworthy with human confirmation.** Falsified if test households cannot get duplicates below 5% within two hours of review.
10. **The steady base (single-house fires) is reachable through professionals.** Falsified if pro accounts outside catastrophe zones run fewer than one claim file a month.
11. **The tool is not implicated in padded claims.** Falsified by one carrier special-investigation referral that cites the tool's output as the source of unsupported lines.

## Relationship to variants/current.md (what is kept from the organizer workbench and the index-only engine; what is dropped)

**Kept.** The index-only engine: search runs where the photos live, originals never move, only approved items are uploaded. The client-review link: relatives answer prompts and contribute from their own phones. The evidence packet salvaged from v1-trades: dated, hash-stamped exports, which here becomes the product. Naming by prompted humans: rooms and items are confirmed by a person; no face template is computed and no person is named. The professional-first sale: a small set of paid practitioners before any consumer.

**Dropped.** The Mac workbench, Takeout repair and library dedupe; identity and People work of every kind; the family vault and any recurring family fee; the organizer association as the first channel.

**Regressions, stated.** (1) The asset is used once and deleted; Compounding asset is weaker than the base. (2) An Apple dependency returns: full-library permission and guideline 5.1.1(iii) decide whether the differentiator exists, where round 3 had none. (3) Android is deferred again, so the multi-relative merge fails in mixed families, the fault that hurt v1-federation. (4) Ceiling is not improved. No whole-library migration and no storage of whole libraries: both constraints hold.

**Best use if kept.** A "claim evidence pack" module in the base product: organizers and their clients already hold an indexed family corpus, and a household with one can produce the evidence gallery in minutes. Photo organizers acting as paid contents specialists would need to stay clear of Florida's definition.

## Evidence pointers (file:section for every claim above)

- Policy base, claim frequencies and severities, fire counts, Los Angeles claim totals, pool estimate, funnel: research/contents-claims.md 2.2, §4 numbers table and funnel.
- Statutory advances (CA §10103.7, §2061, §2051.5; CO; OR), insurer behaviour in Los Angeles, United Policyholders survey figures: research/contents-claims.md 2.1; CDI 2026 Annual Notice (insurance.ca.gov, 2026-01-09, own fetch).
- Who is paid today, fee caps, licence counts, vendor prices: research/contents-claims.md 2.3, 2.7, §3 comparables.
- Bevel, pre-loss apps, absence of a pooled-relatives feature: research/contents-claims.md 2.4; bevelmade.com home page (own re-read 2026-11-25).
- Behaviour and forum evidence, United Policyholders guidance: research/contents-claims.md 2.5.
- Public-adjuster definitions, acceptance of photo-derived lists, fraud controls: research/contents-claims.md 2.6; NAIC Model 228 (Maryland mirror) and napia.com/uppa (own fetches).
- Graveyard, legislative trend, what survives falsification: research/contents-claims.md 2.8.
- Own fetches not in any research file (2026-11-25): proof-list.com (prices, sources accepted); contents.team/blog/encircle-alternative (2026-05-11; price, export format); headwaterseconomics.org structures page (updated 2026-04); davidbramante.substack.com guide (2026-03-30); uphelp.org repost of 2026-03-27 (Department of Angels survey); search excerpts only for NICB and Verisk fraud figures and for indoor positioning.
- On-device search, throughput, local copy size, foreground limits: research/ios-feasibility.md Q2–Q4 and feasibility table. Messages photos: research/unknowns-r1.md Q3. Model licence: research/unknowns-r1.md Q5. Picker and GPS: research/platform-access.md Q4. Guideline 5.1.1(iii): research/memory-product-sdk.md Q6.
- Vision model prices, R2 storage price, card fees, index-only margin: research/unit-economics.md Q1, Q3, Q7. CAC anchors and missing keyword data: research/sizing.md Q4, Q5.
- Face processing constraints: research/face-regulation.md Q1, Q7.
- Base variant, evidence packet, client-review link, organizer ceiling: variants/current.md (Ceiling; merge notes).
- Open unknowns that would move the answer: share of contents value recoverable from candid photos; share of loss households with usable pooled photos; willingness to pay beside a free tool; keyword cost per click; national public-adjuster count; any regulator's view of paid inventory software; average contents claim and limit.
