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
