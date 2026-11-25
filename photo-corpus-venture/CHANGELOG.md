# CHANGELOG

Read this cold. Each entry: what changed, why, what we learned, what the next round attacks.

## Round 0 — 2026-11-03 — Setup
- Created file structure: `research/`, `variants/`, `critiques/`, `pitch/`, `SCORECARD.md`, `CHANGELOG.md`, `GRAVEYARD.md`.
- Wrote the seed as `variants/v0.md` with its six load-bearing assumptions listed for falsification.
- Wrote the rubric into `SCORECARD.md`. Founder fit is `[unknown]` until the founder fills it in.
- No scores assigned yet. Phase 1 research runs first so v0 is scored against evidence, not instinct.

### Next
Phase 1: six parallel research tracks (competitive, platform access, customers, unit economics,
BYO-AI, verticals). Each writes `research/<track>.md`. Falsification-first: each track starts by
trying to break the seed's assumptions.

## Round 0 (Phase 1) — 2026-11-03 — Research and baseline scoring of the seed

### What happened
- Seven research tracks ran in parallel, each audited by a fresh agent (tag check, 8 load-bearing sources spot-fetched) and repaired. All seven needed repair; 71–88 distinct sources each. Files: `research/{competitive,platform-access,customers,unit-economics,byo-ai,verticals,ai-why-now}.md`.
- Six adversarial refuters tested the seed's load-bearing assumptions A1–A6 (`research/assumptions/A1–A6.md`). Result: A1 holds; A2–A6 all partial. None broken outright, none clean.
- Three fresh-context critics (investor, builder, target customer) scored v0 without seeing each other or any author reasoning. Totals: 38 / 40 / 40. Median-based total: **39/100**.

### What we learned (the facts that moved scores)
1. **The founder's "already rejected" voice-app claim is half true.** Voice *search* over photos is native (Siri AI, iOS 27, shipped 2026-09-14, English-first, not in EU on iOS). Voice *editing* is unproven in Apple's primary text. The right reason to reject a standalone app is distribution, not feature parity. GRAVEYARD entry corrected.
2. **Google's March 2025 API removal is real and durable (A1 holds)**, but it hurts the seed as much as it helps: no third party can enumerate a Google Photos library; Takeout and the 2,000-item Picker are the only paths. Google Photos is not a DMA core platform service, so there is no legal lever.
3. **Unattended iOS migration does not exist in any shipping product.** Apple shipped the Background Resource Upload extension in iOS 26.1 (2025-10) with unpublished job and runtime limits; 12 months later Immich closed the request as not planned, Ente says it needs a different architecture, Google Photos and Dropbox (help page 2026-09-17) still say keep the app open. The only adopter is a 31-star experimental app. All three critics named this as the gating objection.
4. **The biggest strategic finding: iOS 27's Foundation Models framework lists Claude and Gemini as supported providers with tool calling.** Any iOS app with PhotoKit permission can run a third-party model over the user's *existing* library, on device, with no export. This deletes the premise that BYO-AI requires moving the corpus out. It is available to every developer, so it is not a moat, but it is a wedge that needs no migration.
5. **Nobody pays for the merge itself.** The only merge-priced products (PowerPhotos $39.95 one-time, KinPhotos $49/yr, Mylio Family $480–732/yr with 5 h of human help) publish no customer counts. Money flows to adjacent jobs: scanning ($0.49–1.28/print, $300–1,250 per family order), professional photo organizers ($50–150/hr, projects from ~$1,500, >700 association members), genealogy subs, new-parent apps. On 2026-10-07 Immich v3.3.0 shipped cross-user shared people for free.
6. **Storage is 93–97% of variable infra.** Index-only (originals stay in iCloud/Google) clears 86% GM on a $4 plan; replicated storage that "outlives any account" clears −2% to 53% at market prices. The "storage company" fear is confirmed and is a design choice, not a fate.
7. **MCP is a commodity.** 54,763 active servers in the official registry; 28 Immich MCP repos; PhotoPrism ships MCP in-product; Khoj (the one consumer "your corpus as a tool" company) shut its cloud 2026-04-15 citing the big labs. Only Claude lets a Free user add a custom connector from mobile; ChatGPT and Gemini gate it to web setup and (per secondaries) paid tiers.
8. **Cross-generation face clustering is an open research problem** for child→adult across decades (best 2024 data: 71% TAR at an 8-year gap). Adult↔aged-adult is solved pre-2024. Any product claim must be "assisted, user-confirmed merging".
9. **Verticals mostly fail the thesis**: wherever a corpus already sits outside the camera roll, a vendor owns it and is shipping AI (Verisk, CCC, Axon, Procore, CompanyCam MCP beta 2026-09-09). The surviving overlap is corpora with a legal reason to exist that are *still on phones*: small trades contractors (82%+ of establishments not on CompanyCam, [estimated]), CA small landlords (Civ §1950.5 names photographs), clinicians (46–73% smartphone capture, but PHI).
10. **Retention regime matters as much as category.** Backblaze consumer backup: 91% gross retention on annual terms (~133-month life). RevenueCat Photo & Video: 23% first annual renewal (~15.6-month life), 48% first monthly renewal (~1.9-month life). A system-of-record archive on annual terms behaves like the first; an AI-search layer sold monthly behaves like the last.

### Walls hit
- No iPhone in this environment: the measured unattended-upload run the builder critic demands cannot be produced here. It becomes a kill criterion in the build plan, not a research task.
- Reddit, Google Trends, help.openai.com and several press sites block the crawler; search-volume and ChatGPT consumer-tier facts are [unknown] pending a human browser check.
- Founder fit is [unknown] on every scorecard. Questionnaire below.

### Decision
Weakest dimension is **Wedge (2)**. Round 1 generates variants where first value needs no migration, or where the migration is done by someone already paid to do it.

### Founder questionnaire (fills rubric dimension 10)
1. Have you shipped an iOS app that uses PhotoKit at full-library scale? A Mac app?
2. Have you shipped ML indexing (embeddings, face models) in production?
3. Months of runway, team size today, and whether you can hire a second engineer before revenue.
4. Would you personally sell to and support professional photo organizers, estate attorneys, or senior move managers? Or only build consumer self-serve?
5. Geography (US? EU, where Siri AI is absent on iOS?), and any unfair access (a photo-organizer network, a scanning-service relationship, a genealogy community).

### Next
Round 1: four materially different variants, each attacking Wedge; six gap-research tracks exposed by the critics; twelve fresh critics (investor / builder / target customer per variant).

## Round 1 — 2026-11-03 — Attack on Wedge

### What happened
- Six gap-research tracks the round-0 critics exposed, each audited and repaired: `research/{face-regulation,pro-channel,estate,sizing,ios-feasibility,trades-and-reddit}.md`.
- Four materially different variants, each delivering first value without a user-run migration: `v1-federation` (index-only family search across relatives' phones), `v1-organizer` (Mac workbench sold to professional photo organizers, B2B2C), `v1-estate` (bereavement event wedge), `v1-trades` (camera-roll job memory for small contractors).
- Twelve fresh-context critics (investor / builder / target customer per variant). Median totals: organizer 47, trades 47, federation 43, estate 39. Seed was 39.

### What we learned
1. **Wedge is fixable; Ceiling is the wall.** Every variant lifted Wedge to 4–6 by removing the migration step. Every variant then scored Ceiling 2–3: no evidence-backed path past ~$10–35M ARR. The seat business for organizers caps at ~$9.8M at 100% penetration of ~7,800 adjacent professionals.
2. **Nobody pays to merge, on the record.** 156 Reddit posts and 178 comments across r/GooglePhotos, r/DataHoarder, r/Genealogy, r/widowers, r/Divorce, r/selfhosted, r/ios: not one poster paid, or was told to pay, anyone to merge libraries. Money appears only for scanning hardware/services and storage plans (`research/trades-and-reddit.md` Part B).
3. **The platforms already sit on both sides of mixed households.** The Google Photos iOS app has full-library access, partner sharing and face groups, so "only we can span iPhone and Android" is false. What remains is product policy: one partner, private face labels, Apple's one Shared Library (`research/ios-feasibility.md` Q6: no Apple statement that People names cross Shared Library participants).
4. **On-device indexing on iOS 27 is feasible but not unattended.** 30,000 photos: ~15 min floor, 38–57 min central, in a user-initiated Continued Processing session that the Camera app kills; the background Neural Engine entitlement has no documented request path; Apple's optimized-storage copies (~1536×2048) are sufficient for embeddings and ordinary faces without any download (`research/ios-feasibility.md` Q2–Q4).
5. **Face regulation is a design constraint, not a blocker.** G.T. v. Samsung (7th Cir., Aug 2026) makes on-device templates a defensible design; named identities for living people need per-subject consent (BIPA written release, GDPR Art. 9); geofencing IL/TX/WA/EU for server-side matching removes 12.7% of the US population from server features (`research/face-regulation.md` risk table). MyHeritage auto-names 0% of living people.
6. **Money flows at scale in three adjacent places**: digitization (Legacybox 2M+ families; iMemories 1M+ families, acquired by Ancestry 2025-07-30; Photomyne $17.0M FY2025, +30%, H1 2026 +59%), genealogy subscriptions ($240–480/yr), and the grandparent invite loop (FamilyAlbum ¥17.1B Lifestyle segment). All three vendors gate the post-scan archive behind their own $50–80/yr cloud; none sells the consolidation step (`research/pro-channel.md` Q5).
7. **The estate channel is owned.** Tukios collects relatives' phone photos for tribute videos at 10,000+ funeral homes; Empathy ($162M raised, 8 of 10 top carriers) has no photo feature and chose not to build one (`research/estate.md` Q6).
8. **Sizing inputs now exist** (`research/sizing.md`): ~80M US households (band 50–110M) pay for photo-bearing cloud; 28–47M cross-platform households [estimated]; ~2.1–2.5M deaths/yr with smartphones; 80–100M households with undigitized prints [estimated: assumption]. $100M ARR at $60/yr needs 1.67M households, ~8% of cross-platform payers. Derived paid-UA CAC for a photo app ≈ $65–90 against a $42 annual-plan LTV (Adapty); Qeepsake's disclosed $35 is the only sourced anchor.
9. **Search demand is still [unknown]**: every keyword-volume route (Trends API, Ubersuggest, Semrush, AnswerThePublic, Wordstream) failed from this environment. A human with a Google Ads account resolves it in ten minutes.

### Decision
Winner: **v1-organizer → `variants/current.md`**, with the index-only engine from v1-federation, the tribute-pack module from v1-estate, the evidence-packet feature from v1-trades, and the consent architecture carried in. Losers to GRAVEYARD with salvage notes.

Weakest dimension: **Ceiling (2)**. Round 2 generates variants that start from a pool where money already flows at scale (prints, genealogy, grandparent loop, memory-product companies as a B2B channel) and keep the organizer channel as one route to market.

### Walls hit
- Reddit via arctic-shift worked for 9 of 12 subreddits; r/iphone, r/GriefSupport, r/declutter, r/ProfessionalOrganizers returned 422 on every query. Facebook groups unreachable.
- Several variant writers and critics exhausted their web-search budget; unresolved items are tagged [unknown] in the variant files and listed per critique.
- Still no iPhone: the 30k-asset indexing run and the Apple Data & Privacy export check are kill criteria for the build plan, not research tasks.

## Round 2 — 2026-11-03 to 2026-11-24 — Attack on Ceiling

### What happened
- Five gap-research tracks, each audited and repaired: `research/{digitization-market,genealogy-market,grandparent-loop,memory-product-sdk,unknowns-r1}.md`.
- Four variants, each starting from a pool where money already flows: `v2-prints`, `v2-genealogy`, `v2-grandparent`, `v2-sdk`. Each was required to show $100M arithmetic or state its honest cap.
- Twelve fresh-context critics. Six ran on 2026-11-03; six (all of grandparent and SDK) failed when usage credits ran out and were re-run on 2026-11-24 with the same prompts. Research dates are unchanged (2026-11-03).
- Median totals: prints 45, genealogy 45, grandparent 41, SDK 35. **No variant beat `v1-organizer` at 47.** Rounds without improvement: 1.

### What we learned
1. **Each pool is real and each caps well short of $100M.** Stated honest ceilings: prints $25–45M US; genealogy $8–30M; grandparent loop $5–10M per its own research file; SDK $5–15M. Critics scored Ceiling 2–3 on all four.
2. **People pay for backup and artifacts, not for naming.** Photomyne is the only audited P&L in digitization: $17.0M FY2025 revenue, ~402k paying subscribers and slipping (411k → 408k → 402k), monthly actives down 19% year on year, marketing at 64–68% of revenue, still loss-making. Its users tag 0.10 times per scan and share 0.31 times per scan. Revenue growth came from a ~50% price rise and deferred-revenue recognition, not new households.
3. **Ancestry made the scan a loss leader.** It bought iMemories on 2025-07-30 and launched AncestryPreserve at RootsTech 2026: $20 kit, $0.49/photo, scans land in the tree gallery. MyHeritage's $49.90/yr Photo plan bundles scanning; PhotoDater is free; Photo Discoveries shipped 2026-07-21.
4. **Genealogy is closed.** ~3–4.8M paying subscribers worldwide, flat since 2020. Ancestry has no public API and re-platformed its partner API on 2026-05-05. FamilySearch write access requires Solutions Program certification. Neither Apple Photos nor Google Photos rebuilds People from XMP, so a third party cannot put a name where the customer's tree or library lives.
5. **The grandparent loop is a subsidy, not a mechanic an entrant can copy.** FamilyAlbum: 30M registered, 12M monthly actives, 65% of Japanese births, free unlimited storage of originals, ~5% segment margin, ad spend 13–15% of segment sales. Only 4.3% of new members pay as followers. Tinybeans' "multigenerational archive" pivot left core paid subscribers flat at ~50k. Open face models reach 30.7% true-accept on infants aged 0–6 months.
6. **The SDK buyer set is empty.** Shutterfly, CEWE, Mixbook and Chatbooks all shipped in-house curation in 2025–2026, mostly on Apple's free Vision aesthetics API. iOS has no sanctioned way for an SDK to hold one index shared across companies' apps. Google partnered with Fujifilm directly (2026-09-30).
7. **Ten cheap unknowns closed** (see SCORECARD). The two that change the build: MobileCLIP weights are research-only (use SigLIP 2 or TinyCLIP), and on-device face templates are not a liability shield by themselves (Doe v. Apple's Local Device Class survived summary judgment on 2026-09-30, even as the 7th Circuit cleared Samsung on 2026-08-07).

### Decision
`variants/current.md` keeps the organizer workbench as its base, with round-2 merge notes appended. All four round-2 variants go to GRAVEYARD with salvage notes.

The pattern across three rounds: every variant that charges for organizing, naming or merging caps at Ceiling 2–3. Round 3 changes what is sold. Variants must monetize an **artifact or a moment** people already pay for at scale, and keep the archive as the retention asset behind it. Candidates: a gifted, AI-interviewed photo memoir for an aging parent (Storyworth and Remento sell at $99; Aura and Skylight sell gift frames to grandparents); a printed family journal mailed to grandparents (Famileo, Neveo); an institutional legacy program for senior living and hospice (LifeBio, Storii, Famileo's care-home channel). None of these comparables were researched in rounds 0–2.

### Walls hit
- Usage credits ran out mid-round on 2026-11-03; the round resumed on 2026-11-24 after a model change. The three-week gap means price and product facts dated 2026-11-03 should be re-checked before the pitch is used.
- The direct page-fetch tool was withdrawn from this session; research agents now use web search plus curl through the proxy. Sites that block non-browser clients stay [unknown].
- To limit spend, rounds from here run three variants (the minimum), three narrow research tracks, and nine critics.

## Round 3 — 2026-11-24 to 2026-11-25 — Sell the artifact or the moment

### What happened
- Three research tracks on comparables no earlier round covered, each audited and repaired: `research/{memoir-gift-market,family-artifact-market,institutional-legacy}.md`. Raw audit findings are kept in `research/audits/`.
- Three variants that monetize an artifact or a moment and keep the archive behind it: `v3-gift` (an adult child gifts a parent a year of AI-led interviews about the family's photos, with a book), `v3-journal` (a printed monthly family journal assembled from every relative's phone), `v3-care` (a legacy program that senior-living operators and hospices pay for per resident).
- Nine fresh-context critics. Median totals: gift 43, journal 41, care 41. **No variant beat `v1-organizer` at 47.** Rounds without improvement: 2.
- The container restarted mid-round and stopped the workflow. Research, audits and variants had been written to disk and were committed; two research repairs and all nine critics were re-run.

### What we learned
1. **The gifted memoir is a real purchase and a small category.** Storyworth advertises 1,000,000+ books since 2013 with a 13-person team; its revenue is undisclosed. The largest sourced figure in the category is Remento's ">$7 million in sales" (founder statement, aired 2026-03-25, unaudited). The failure list is long: Artifact, HereAfter AI, StoryFile, StoryTerrace, LifeBook, No Story Lost, Eternos, Autobiographer.
2. **Both of the gift variant's wedges already ship.** Storyworth's "Magic Interviews" phones the elder and asks follow-ups, on a landline if needed, and uses photos as prompts. Remento launched a photo-anchored product on 2026-10-22. Memory Murals tags people and dates from speech for $99.99 a year.
3. **Voice AI is cheap; elders finishing is the problem.** A year of AI interviews costs about $6–22 per recipient. Remento families record about 10 stories against 52 prompts. The only study of AI voice conversations over personal photos had 13 participants with a mean age of 65.8.
4. **Frames are the nine-figure business in "family photos for grandparents", and they are hardware.** Skylight claims $300M+ and, more recently, over $500M a year (both unaudited) across 12M customers. Nixplay filed $57.9M for FY2021 and $20.0M for FY2023. Aura has sold "single-digit millions" of frames, is profitable, and charges no subscription. Payers reject recurring fees on the artifact: Nixplay reached about 1.2% paid and drew a bait-and-switch lawsuit when it forced the issue.
5. **Printed family journals work in France and nowhere else.** Famileo: €15.3M in 2025 after ten years, ~280,000 families. Its US iOS app has ~110 ratings against 5,322 in France; the whole US category is about 7,500 families. At public US print and First-Class postage prices a journal costs $9.24–10.09 to make and mail against a $9.99 price.
6. **Institutions pay little for life stories.** LifeBio, about 25 years old, reports over $2M revenue with 48 employees and NIH grant support; its current list price works out to ~$9–18 per person per year. LifeLoop, in 4,700+ communities, ships a Life Story feature whose AI layer went generally available on 2026-11-17.
7. **A direct statement from an operator:** Aura's CTO, 2025-10-21: companies that tried "the private photo network on its own" were "not being able to find a business model for it". Lalo shut in July 2023 because "no one wanted to pay for this".
8. **What got better:** all three variants scored Buildability 6 because nothing in them waits on Apple or Google, and names come from a prompted human, which removes the face-template problem.

### Decision
`variants/current.md` keeps the organizer workbench as base, with round-3 merge notes appended. All three round-3 variants go to GRAVEYARD with salvage notes.

After fifteen scored variants the result is consistent: consumer family-memory software caps at roughly $5–45M on evidence. Nine-figure revenue near this idea exists only for platform owners (storage), hardware (frames), record owners (Ancestry), print logistics, a subsidized parent (MIXI), and one business vertical (CompanyCam).

Round 4 therefore leaves the family-pays-for-memories model and probes three places where large money is evidenced: AI model builders paying for consented camera-roll data; the gift frame itself, with the elder interview built in; and the insurance contents claim, where pooled household camera rolls are evidence.

### Walls hit
- Container restart on 2026-11-25 cost one workflow run. From here every completed step is committed and pushed before the next begins.
- sec.gov, Similarweb, several French registries and print-quote calculators block automated clients; those facts are tagged secondary or [unknown] in the files.
