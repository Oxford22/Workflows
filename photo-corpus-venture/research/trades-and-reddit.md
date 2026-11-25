# Gap Track R6 — Small-trades vertical sizing + Reddit evidence of the family-archive pain

Written 2026-11-03; repaired 2026-11-03 after audit (see "Audit log" at the end). All access dates are
2026-11-03 unless stated; source dates are the publication dates of the cited pages or datasets. Builds on
`research/verticals.md` §2.1 and §6 (read first); the denominator difference between the two files is
reconciled in A2 below.

Method note. In both the original pass and the repair pass the shared WebSearch budget was exhausted
(original: after the first 14 queries of this track; repair: on every one of 13 queries attempted) [sourced:
WebSearch tool responses "this turn's web search budget is used up (limit: 200 WebSearch calls per turn,
shared by every agent in it)", 2026-11-03]. Everything else came from (a) direct WebFetch of pages whose
URLs could be named, (b) Census / StatCan / ONS bulk files downloaded with curl and parsed locally, and
(c) the arctic-shift public Reddit archive API (`arctic-shift.photon-reddit.com/api/posts/search`,
`/api/comments/search`), which the brief names as a fallback. reddit.com and old.reddit.com refused both
curl (HTTP 403 / 302) and WebFetch ("unable to fetch"); pullpush.io returned HTTP 522 on every attempt
(original pass). The original pass did not keep a call log, so its own counts of arctic-shift successes and
"Timeout. Maybe slow down a bit" (HTTP 422) failures are [unknown — reported from memory as 9 and
"roughly 25"; not logged]. The repair pass logged every call: see the "arctic-shift call log" table in §4,
[sourced: scratchpad `as/log*.txt`, 2026-11-03]. The archive only answered reliably when called one
query every 25-30 s; bursts returned 422. Subreddit coverage after repair is stated in the Part B header.

---

## 1. Questions asked

Part A (trades)
- A1. How many US construction/trades establishments have 1-9 employees (CBP, NAICS 23 and subsectors)? How many nonemployer construction firms (NES)? UK/CA equivalents.
- A2. CompanyCam penetration (customer count 2024-2026), pricing changes, camera-roll import, MCP beta, AI tagging/search roadmap; competitor photo/AI features; photo-documentation startups 2024-2026.
- A3. Evidence that small contractors lose money for lack of photo proof; insurer requirements; statutes of repose (5 states); attorney retention advice.
- A4. Does Apple Photos / Siri natural-language search (or Google "Ask Photos") already solve "find the Smith kitchen rough-in photos" from a camera roll? What can't it do?
- A5. Pricing/distribution norms for 1-9 employee trades SaaS; association member counts; supply-house partnerships; where small contractors find software.

Part B (family archive)
- B1. Dated, scored Reddit posts across the named subreddits showing the merge / inherit / scan / organize pain, and whether money changes hands (including what commenters tell posters to pay).

Falsification stance. For A1 I looked for evidence the 1-9 segment is smaller than the "most contractors
are tiny" folk claim; it is not: 81.5% of US payroll establishments [estimated: 664,231 / 814,557, CBP 2023
below] and 95.9% of all US construction establishments including nonemployers [estimated: 3,539,821 /
3,690,147, below] are 1-9 or zero-employee; Canada (92.8%) and the UK (97.8%) match [estimated: A1 below].
For A2 I looked for evidence that CompanyCam already covers the long tail: its About page says 140k+
[sourced: companycam.com/about, accessed 2026-11-03], lower than the 170k it claimed on 2024-02-28
[sourced: companycam.com/press, 2024-02-28, via verticals.md], and every penetration ceiling against the
nonemployer-inclusive US base is under 6% (3.8-5.9%, table in A2) [estimated: A2 below]. For A4 I looked
for evidence Apple or Google already solves the contractor retrieval case (both solve object/scene/person
retrieval; neither has a job or customer entity, and Siri's photo search is an iOS 27 beta). For B1 I looked
for posts where nobody pays (most of them) and, in the repair pass, read 7 family-segment comment threads
for what posters were told to pay (nothing, in every case — see Part B).

---

## 2. Findings

### A1. Establishment counts by size class

**US, County Business Patterns 2023 (released 2025-06-26), US file `cbp23us.txt`, all legal forms**
[sourced: https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23us.zip, 2023 data, parsed locally 2026-11-03].
CBP counts establishments with paid employees; the "<5" class includes establishments that had
payroll but zero employees in the March pay period.

| NAICS | Description | Establishments | <5 emp | 5-9 emp | 1-9 (sum) | 1-9 share | 10-19 | 20-49 | 50+ | Employees |
|---|---|---|---|---|---|---|---|---|---|---|
| 23 | Construction | 814,557 | 536,259 | 127,972 | 664,231 | 81.5% | 75,854 | 49,046 | 25,426 | 7,659,459 |
| 236 | Construction of buildings | 254,630 | 187,982 | 34,268 | 222,250 | 87.3% | 17,788 | 10,005 | 4,587 | 1,621,439 |
| 237 | Heavy & civil | 38,612 | 17,623 | 6,702 | 24,325 | 63.0% | 5,307 | 5,015 | 3,965 | 1,051,261 |
| 238 | Specialty trade contractors | 521,315 | 330,654 | 87,002 | 417,656 | 80.1% | 52,759 | 34,026 | 16,874 | 4,986,759 |
| 238210 | Electrical contractors | 83,342 | 48,799 | 15,277 | 64,076 | 76.9% | 9,329 | 6,300 | 3,637 | 1,015,983 |
| 238220 | Plumbing/HVAC contractors | 111,207 | 64,871 | 20,587 | 85,458 | 76.8% | 13,148 | 8,384 | 4,217 | 1,214,761 |
| all | US all industries | 8,361,342 | 4,639,650 | 1,465,355 | 6,105,005 | 73.0% | — | — | — | 139,831,742 |

All counts [sourced: cbp23us.txt as above]; the "1-9 (sum)" and share columns are [estimated: <5 + 5-9,
divided by establishments, from the same file].

Cross-check: CPWR's April 2026 Data Bulletin, using the 2023 CBP state file, reports "81.7% employed 1 to
9 employees" as the 2014-2023 average and a 2023 figure of 81.2% (down from 82.1% in 2014), and "Over 90%
of construction payroll establishments have fewer than 20 employees"; it also says nonemployer
establishments "accounted for 78.1% of all construction establishments in 2021" [sourced:
https://www.cpwr.com/wp-content/uploads/DataBulletin-April2026.pdf, April 2026, text extracted locally].
My 81.5% from the US file sits between CPWR's two figures; the small gap is the state-file vs US-file basis.

**US, Nonemployer Statistics 2022 (latest bulk file available; 2023 is pending re-release on 2017 NAICS)**
[sourced: https://www2.census.gov/programs-surveys/nonemployer-statistics/datasets/2022/historical-datasets/nonemp22us.zip, 2022 data, parsed locally 2026-11-03;
re-release note sourced: https://www.census.gov/data/developers/data-sets/nonemp-api.2023.html via search snippet, 2026-11-03].

| NAICS | Nonemployer establishments | Receipts ($K) |
|---|---|---|
| 23 Construction | 2,875,590 | 238,039,583 |
| 236 | 919,062 | 98,684,329 |
| 237 | 40,000 | 5,420,581 |
| 238 Specialty trade | 1,916,528 | 133,934,673 |
| all industries | 29,811,495 | 1,726,773,355 |

Note the NES construction threshold is receipts of $1 or more (vs $1,000 elsewhere), so this count
includes very marginal filers [sourced: Census NES description via search snippet, 2026-11-03].

**Derived universe.** Employer establishments with 1-9 employees + nonemployer establishments =
664,231 + 2,875,590 = 3,539,821, which is 95.9% of the 3,690,147 construction establishments of any
size (814,557 + 2,875,590) [estimated: sums of the CBP 2023 and NES 2022 figures above; mixes two
reference years and the CBP "establishment" vs NES "establishment" definitions, so treat as ±2%].
Average receipts per nonemployer construction establishment: $82,780 [estimated: 238,039,583K / 2,875,590].

**UK, Business Population Estimates 2025 (start 2025), Table 5, section F Construction**
[sourced: https://assets.publishing.service.gov.uk/media/68dbccc9c487360cc70c9f4e/BPE_2025_detailed_tables.xlsx, published 2025-10-02, parsed locally 2026-11-03]:
all businesses 885,485; employers 193,675; no employees (unregistered) 500,325; no employees
(registered) 191,485; 1 employee 18,285; 2-4 employees 125,780; 5-9 employees 29,675; 10-19 12,145;
20-49 5,410. So 1-9 employees = 173,740 (89.7% of employers; 19.6% of all) and 0-9 = 865,550 = 97.8%
of all construction businesses [estimated: 18,285 + 125,780 + 29,675 = 173,740; 173,740 + 500,325 +
191,485 = 865,550; 865,550 / 885,485 = 97.75%; the draft's 865,565 was an addition slip of 15].

**Canada, Canadian Business Counts, June 2026 (released 2026-08-14), Canada total, NAICS 23**
[sourced: https://www150.statcan.gc.ca/n1/tbl/csv/33101174-eng.zip (Table 33-10-1174-01, "with employees")
and https://www150.statcan.gc.ca/n1/tbl/csv/33101175-eng.zip (Table 33-10-1175-01, "without employees"),
reference period 2026-01 per the CSV, released 2026-08-14 per StatCan's cube list
https://www150.statcan.gc.ca/t1/wds/rest/getAllCubesListLite, all parsed locally 2026-11-03]:

| NAICS | With employees (total) | 1-4 | 5-9 | 1-9 (sum) | 1-9 share of employers | Without employees | 0-9 share of all |
|---|---|---|---|---|---|---|---|
| 23 Construction | 159,672 | 98,704 | 30,622 | 129,326 | 81.0% | 262,066 | 92.8% |
| 236 Construction of buildings | 49,695 | 32,687 | 9,289 | 41,976 | 84.5% | 97,381 | — |
| 238 Specialty trade contractors | 101,223 | 61,874 | 19,953 | 81,827 | 80.8% | 137,833 | — |

Counts [sourced: the two StatCan tables above]; sums and shares [estimated: 1-4 + 5-9; (1-9 + without
employees) / (with + without employees) = 391,392 / 421,738 = 92.8%]. The Canadian "with employees"
table has the same 1-9 share as the US CBP (81.0% vs 81.5%). Note: the business-counts series is
re-issued under a new table number every six months (33-10-0661 = Dec 2022 ... 33-10-1174 = June 2026),
which is why the draft's single attempt at 33-10-0810-01 hit an unrelated table.

### A2. CompanyCam penetration, pricing, camera-roll import, MCP, AI roadmap; competitors

**Customer count.** The About page says "with 140k+ contractors and pros using it" and "Over 1 Billion
photos have been taken in CompanyCam" [sourced: https://companycam.com/about, accessed 2026-11-03]. The
press page's only 2025-2026 items say "a trusted partner to tens of thousands of contracting businesses"
(2025-08-22, Series C) and "provides jobsite documentation and AI productivity tools to tens-of-thousands of
construction and home service businesses" (2026-03-02, acquisition) [sourced: https://companycam.com/press,
2025-08-22 and 2026-03-02, re-read 2026-11-03]. These are LOWER than the "over 170,000 contractors" of
2024-02-28 cited in verticals.md. A third-party review notes the same disagreement and adds "285,000+ pros
(Instagram bio)" [secondary: https://theroofingbrief.com/companycam-review/, 2026-10-19]. CompanyCam is
private, so there is no SEC filing; PitchBook/Crunchbase could not be reached without search budget.
Interpretation: "140k+ contractors and pros" (About) and "tens of thousands of businesses" (press) are
consistent if ~140k is users/pros and tens-of-thousands is paying companies; the 170k (2024) figure likely
counted users too. Paying-company count: [unknown].

Penetration ceilings (numerator is global and may count users, so these are upper bounds)
[estimated: 140,000 and 170,000 divided by the bases named]:

| Base | Count | Source | 140k | 170k |
|---|---|---|---|---|
| US construction employer establishments (CBP 2023) | 814,557 | cbp23us.zip | 17.2% | 20.9% |
| US construction establishments, BLS QCEW 2024 annual avg, private (verticals.md §2.1 Q4) | 938,478 | verticals.md | 14.9% | 18.1% |
| US 1-9-employee establishments (CBP 2023) | 664,231 | cbp23us.zip | 21.1% | 25.6% |
| US nonemployers alone (NES 2022) | 2,875,590 | nonemp22us.zip | 4.9% | 5.9% |
| US small-trades universe (nonemployer + 1-9) | 3,539,821 | estimated above | 4.0% | 4.8% |
| US all establishments incl. nonemployers | 3,690,147 | estimated above | 3.8% | 4.6% |

Reconciliation with verticals.md: that file uses BLS QCEW 2024 (938,478 establishments, which counts
reporting units covered by unemployment insurance, annual average) and gets an 18% ceiling; this file uses
CBP 2023 (814,557, establishments with payroll in the March pay period) and gets 17-21%. Both are genuine
official counts on different definitions and years; the 124k gap is a definitional difference, not an error
[estimated: 938,478 − 814,557 = 123,921]. Verdict: against the base that actually describes "small
trades" (nonemployers + 1-9), CompanyCam's ceiling is under 6% on every row that includes nonemployers.
The non-CompanyCam population is at least ~3.5M establishments [estimated: 3,690,147 − 170,000 =
3,520,147; assumes every CompanyCam customer is a distinct US establishment, which overstates penetration].

**Pricing (2026-11-03) — conflict resolved in the review's favour.** The pricing page's plan cards carry
machine-readable prices that the page's JavaScript renders: Core `data-monthly="79"` / `data-yearly="63"`,
Crew `data-monthly="149"` / `data-yearly="119"`, Scale `data-monthly="299"` / `data-yearly="249"`,
additional users `data-monthly-user="34"` / `data-yearly-user="29"` on every card, Enterprise "Custom
Rates"; the separate "Compare Plans" table still prints "63 /month", "129 /month", "199 /month"; and the
page's own JavaScript fallback defaults (used only if the attributes are missing) are the older set
79/63, 149/129, 249/199 with a code comment reading "USD $79/$63 base, $34/$29 add'l user ... USD $149/$119
... USD $249/$199" [sourced: raw HTML of https://companycam.com/pricing, downloaded with curl 2026-11-03;
WebFetch's text rendering shows only the Compare Plans figures because the card prices are injected by
script]. So the live card prices are $79/$63 (Core), $149/$119 (Crew), $299/$249 (Scale) monthly/annual,
1/3/3 users, extra users $34/$29, AI credits 10/100/unlimited [sourced: same page; user and credit counts
from the rendered text]. The Compare Plans header is stale, exactly as the review says; the review further
claims the Scale rise happened on 2026-09-17 and that accounts that joined before then keep $249/$199
[secondary: theroofingbrief.com, 2026-10-19]; the page itself contains no price-change or grandfathering
statement [sourced: grep of the raw HTML for "grandfather", "Sept", "joined before": no matches]. The
annual toggle says "save 20%" [sourced: companycam.com/pricing]. FAQ: "As long as you're a CompanyCam
customer, your photos stay in your account"; "If you ever cancel, you can export your photos before your
access ends"; "No. Your job photos are stored in the cloud, so they don't clog your camera roll" [sourced:
https://companycam.com/pricing, accessed 2026-11-03]. The 2026-09-17 date of the rise: [secondary only].

**Camera-roll import (help center).** "Uploading Existing Photos and Videos": on mobile, tap "Upload
Photos" then "Select Photos Manually" or a date range; "you'll need to grant the CompanyCam app access
to your device's gallery or camera roll"; "Photo dates are set based on your file's EXIF data"; with EXIF
"CompanyCam uses the date it was originally taken", without it "the photo will show the date you uploaded
it"; "The Magic Uploader brings in up to 100 photos at a time" and can "pull in photos taken at the
Project's address"; "You can't select all photos at once when uploading manually"; "The Magic Uploader
doesn't include videos from your camera roll" [sourced:
https://help.companycam.com/en/articles/6828411-uploading-existing-photos-and-videos, "Updated this week" on 2026-11-03].
So: the incumbent already does GPS-matched bulk import from the camera roll, 100 at a time, with capture
dates preserved. It does not say location metadata is preserved on manual uploads.
Related capture features: "Date/time and GPS stamps add the exact time, date, and location to the corner
of every photo you take" (mobile only; cannot be removed once added) [sourced:
https://help.companycam.com/en/articles/7045817-adding-date-time-and-gps-coordinate-stamps-to-photos];
"Saving Photos and Videos to Your Camera Roll Automatically" exists as an article (body not read)
[sourced: https://help.companycam.com/en/collections/19746674-camera-settings]; "Text Scanning lets you
copy text straight out of a photo in the CompanyCam mobile app" — paste into description/comment; the
article does not say scanned text becomes searchable; "available on select plans" [sourced:
https://help.companycam.com/en/articles/10943941-scanning-text-on-photos, "Updated today" on 2026-11-03].

**MCP beta (2026-09-09).** Verbatim: "If ChatGPT or Claude already has a spot in your workday,
CompanyCam's MCP Server can give those conversations access to supported information from your CompanyCam
account"; "With read-and-write access, supported CompanyCam updates can also become part of the routine"
(the post repeats the thought as "...supported CompanyCam actions can become part of the same workflow"
and "...can also become part of those workflows"); "CompanyCam's MCP Server is currently in Beta, and
supported capabilities can change"; the only assistants named are ChatGPT and Claude; the post does not say
which plans include it and does not describe photo search, only reviewing "available photo documentation
before responding" [sourced: https://companycam.com/resources/blog/ways-contractors-use-companycam-mcp-ai-daily-tasks, "Sep 09, 2026", re-read 2026-11-03].

**AI tagging/search roadmap.** Nothing new on press (2025-2026 items mention "field-ready AI", "embed AI
into every workflow", "AI shortcuts", none mention search or tagging) [sourced: companycam.com/press,
2025-08-22, 2026-03-02]. Features page: "Create reports, checklists, captions, and updates without typing a
word with AI"; the word "search" does not appear in the rendered text [sourced: https://companycam.com/features, accessed 2026-11-03].
The only roadmap statement remains the Nov-2025 "enhanced photo tagging and search" quote in verticals.md
[secondary: siliconprairienews, 2025-11-22]. Community requests for description search (2026-10-22) and
customer search (2026-10-28) are in verticals.md §2.1.

**Competitors (photo + AI).**
- Jobber: Plus tier "Store and organize unlimited photos and videos from every job"; AI: Jobber AI
  Voice, AI Chat, AI Receptionist add-on $29/mo; "Image search: Not mentioned" [sourced: https://getjobber.com/pricing/, accessed 2026-11-03].
- Housecall Pro: Essentials includes "Photo reports & annotations" ("Mark up job photos with drawings
  and notes, then build a clean report in a few taps"); every plan "AI team members to automate your
  work"; CSR AI add-on; no image search [sourced: https://www.housecallpro.com/pricing/, accessed 2026-11-03].
- ServiceTitan: the features index lists "Equipment Scanning", "Field Findings", "Daily Logs", "Document
  Management" and "Titan Intelligence"; the only image-related sentence is "Accelerate data entry with
  equipment nameplate scanning"; no sentence about photos or photo search [sourced:
  https://www.servicetitan.com/features, accessed 2026-11-03; /titan-intelligence returned 404]. Field Pro
  "equipment recognition" per the 10-K filed 2026-03-25 is in verticals.md.
- Buildertrend: [unknown] — buildertrend.com/pricing (403 on WebFetch and curl), /features (403),
  /newsroom (403), help.buildertrend.com (connection reset), Capterra (403), SoftwareAdvice (403), GetApp
  (404), Google Play listing (page text truncated to 38 characters), Wikipedia (404) — ten attempts, no
  readable source.
- Photo-documentation startups 2024-2026: Y Combinator's construction directory lists Opusense AI (P2025,
  "Generates organized field inspection reports from on-site voice notes and photos, in real time") and
  Albiware (S2022, field documentation for damage-repair contractors); the older photo-capture entries
  (Bulldozair S2016, PlanGrid W2012) are marked acquired [sourced:
  https://www.ycombinator.com/companies/industry/construction, accessed 2026-11-03]. Beyond YC and the
  verticals.md §2.12 names (Klutch, OnSite, BuildPass, Hardline, Terial): [unknown — no search budget].

### A3. Dispute / evidence pain

**Industry surveys.** The only payment survey reachable by URL is Levelset's 2019 National Construction
Payments Report ("based on a survey of 500+ construction professionals"): "50% of contractors complain
they are not paid on time"; "40% say that back charges, deductions, and other withholdings frequently get
tacked on after a project is finished"; "42% report always being stuck paying for labor, vendors, and
materials before they receive payment on a job"; "35% of contractors dip into personal savings and credit
to make ends meet" [sourced: https://www.levelset.com/tools/national-construction-payments-report/, 2019].
It does not ask about photo evidence. No survey quantifying money lost specifically for lack of photos was
found: Levelset's three post sitemaps contain no later payment report; Rabbet (two URLs) and Procore "How We
Build Now" (two URLs) returned 404 [unknown]. Vendor-authored evidence (not a survey): CompanyCam's
2026-09-18 post says "One national roofing enterprise shared that a single rework project cost them
$70,000" "because they lacked adequate documentation of the underlayment"; "Disputes are one of the most
common payouts that eat away at the margins of roofing and exterior businesses"; "disputes often strain
operating budgets because customers withhold significant final payments"; "With insurance work, thorough
documentation is the currency for getting paid out what the job is worth" [sourced:
https://companycam.com/resources/blog/compounding-cost-of-inconsistent-documentation, 2026-09-18; vendor
marketing, single unnamed anecdote].

**Insurer requirements.** No insurer page stating a contractor-side photo-evidence requirement was
reached: The Hartford construction-risk page returned 503 twice; Next Insurance's blog index has no
documentation post. The nearest insurer statement is policyholder-side: "Your insurer will want to see
proof of damage from a disaster or accident"; "Failure to thoroughly document that damage may result in a
lower payout or a denied claim"; recommended documentation includes "Photographs of the scene, damaged
goods, destroyed property" [sourced:
https://www.insureon.com/blog/mistakes-small-business-owners-make-when-filing-insurance-claims, "Updated: July 31, 2026"].
Contractor-specific insurer requirements: [unknown].

**Regulator advice.** Massachusetts' consumer-affairs office advises contractors to take photos before,
during and after every job and note the dates, as evidence should a dispute arise [secondary: search
snippet of https://www.mass.gov/news/contractor-vs-homeowner-how-to-keep-your-business-and-reputation-intact; page returned HTTP 403 on fetch; wording paraphrased, undated].

**Forum threads (quoted by URL).**
- ContractorTalk (fetched in full with curl, 2026-11-03; 33 posts dated 2010-03-22 to 2010-07-21): one
  contractor writes "I like to take pictures as I go for several reasons. CYA is a major one. Like a i did a
  bathroom a while back took pictures of the tub before I started and then when I was all don and thru the
  way of the job. it was fine perfect white nice tub. About two days later i get a call saying I had chipped
  thier tub. I was like no way I will bring the disk." [sourced:
  https://www.contractortalk.com/threads/permission-to-use-pictures-of-homes-youve-done.75552/, 2010;
  verbatim incl. typos]. Another: "Before and After photos are great. I always find myself saying I wish I
  would have took a[...]" [sourced: same thread, 2010].
- Mike Holt electricians' forum: photos of work "buried in the wall" later helped locate hidden junction
  boxes; photos "can also document damaged shipments, damage caused by other trades, site conditions/
  weather, accidents"; GCs "withhold payments over claimed incomplete work" [secondary: search snippets of
  https://forums.mikeholt.com/threads/pictures-before-drywall.38544/ and https://forums.mikeholt.com/threads/photos.12360/; pages returned HTTP 403 on WebFetch and curl in both passes; undated].

**Reddit trade subs (primary, via arctic-shift; quoted by URL).**
- r/Contractor, "what's worth taking pictures of before starting a job?" (2026-10-12, score 8, 22
  comments): the poster opens with how easy it is for a small pre-existing issue to turn into an argument
  with a customer. In the 22 comments (2026-10-12/13): one explicitly says photographing existing damage,
  the meter, shutoffs and the whole room avoids a "you scratched my cabinet" fight; one firm attaches
  existing-condition photos to the contract as an exhibit and calls it cheap insurance; one makes the
  client sign a pre-work condition report "like a rental car check"; one crew takes "over 100" photos on
  larger site visits; two say photos are free so take plenty; one commenter, in two separate remarks,
  accuses the poster of "trying to sell something" / "buy your shitty app"; one commenter recommends the app
  MagicPlan; no comment names CompanyCam, Google Photos or Apple Photos, and no dollar amount appears
  [sourced: https://www.reddit.com/r/Contractor/comments/1x4fpst/whats_worth_taking_pictures_of_before_starting_a/ and
  https://arctic-shift.photon-reddit.com/api/comments/search?link_id=1x4fpst, 2026-10-12/13; post later
  flagged `removal_type: reddit` in the archive; MagicPlan and single-accuser corrections per the auditor's
  re-read of all 22 comments and this pass's re-fetch, see Audit log].
- r/Contractor, "Remediation company committing fraud" (2026-10-02, score 278, 106 comments): homeowner
  side; a $5k deductible and a $5k invoice are in dispute after a plumber-recommended remediation
  [sourced: /r/Contractor/comments/1ww7h2v/remediation_company_committing_fraud/, 2026-10-02].
- r/HVAC, "I'm tired of the BS" (2026-10-14, score 315, 136 comments): "I'm tired of having a morning
  meeting everyday because someone didn't take enough pictures" — i.e. photo documentation is an enforced
  management routine at shops, resented by techs [sourced: /r/HVAC/comments/1x5hi5q/im_tired_of_the_bs/, 2026-10-14].
- r/HVAC warranty threads: "Who do i appeal to" (2026-10-16; appealing a Weil-McLain warranty denial) and
  "Lennox core control water damage" (2026-09-03; "about 30" warranty claims this year on one customer's
  sites) show the manufacturer-warranty path where photo evidence is demanded [sourced:
  /r/HVAC/comments/1x7bhn2/, /r/HVAC/comments/1w69rrw/, dates as given].
- r/electricians, "Job logs" (2026-05-20, score 1, 2 comments): "The crew that started it isn't always the
  ones to finish. Even sometimes guys forget what they did 8 months ago. We take a lot of videos and
  pictures but I feel like there's a better way to go about this" [sourced:
  /r/electricians/comments/1tihiv4/job_logs/, 2026-05-20].
- r/Plumbing: [unknown] — arctic-shift returned 422 on every attempt (original pass: 6; repair pass: 3
  more, see call log).
Verdict: the "photos as dispute insurance" norm is live and specific (meter, shutoffs, four corners per
room, signed condition report), it is practised with the phone camera and "saved with the job date", and
the only dedicated app named in the r/Contractor thread is MagicPlan (once) — which is both the opportunity
and the objection (one commenter assumes anyone asking is selling software).

**Statutes of repose, five big states.** Each verified against the statute text or a dated code
reproduction in the repair pass; the survey column is the 08/2024 compilation the draft used [sourced:
https://www.sdvfenchurch.com/state-survey/statutes-of-limitations-and-repose-for-construction-related-claims/, page dated 2026-08-20, disclaimer "current as of 08/2024"].

| State | Repose period | Statute | Trigger / notes | 2025-2026 currency check |
|---|---|---|---|---|
| California | 10 yrs (latent); 4 yrs patent | CCP §337.15; §337.1 | substantial completion | "more than 10 years after the substantial completion of the development or improvement" [secondary: https://codes.findlaw.com/ca/code-of-civil-procedure/ccp-sect-337-15/, "Current as of January 01, 2026"; leginfo.legislature.ca.gov returned 403 twice] |
| Texas | 10 yrs private (8 yrs gov't); **6 yrs** residential where the contractor gave a written 1-2-6 warranty | CPRC §16.009 (§16.008); §16.009(a-2),(a-3) added by HB 2024 (88th Leg., 2023) | substantial completion; written claim in-period extends 2 yrs (1 yr gov't) | HB 2024 enrolled text: "the claimant must bring the suit not later than six years after the substantial completion of the improvement" if the warranty gives "one year for workmanship and materials; two years for plumbing, electrical, heating, and air-conditioning delivery systems; and six years for major structural components"; applies to improvements whose work begins on or after the effective date (2023-09-01 absent a two-thirds vote) [sourced: https://capitol.texas.gov/tlodocs/88R/billtext/html/HB02024F.htm, 2023]; the 08/2024 survey already post-dates this, but did not list the 6-year track |
| Florida | 7 yrs | Fla. Stat. §95.11(3)(b) | earliest of temporary CO, CO, certificate of completion, or abandonment; latent-defect discovery rule for the 4-yr limitation | 2025 statutes: "In any event, the action must be commenced within 7 years after the date the authority having jurisdiction issues a temporary certificate of occupancy, a certificate of occupancy, or a certificate of completion, or the date of abandonment of construction if not completed, whichever date is earliest"; history line ends "s. 2, ch. 2025-81; s. 41, ch. 2025-153" — amended in 2025 but the 7-year figure stands [sourced: https://www.flsenate.gov/Laws/Statutes/2025/95.11, 2025] |
| New York | none | — | 3-yr limitation CPLR §214; §214-d notice for design pros >10 yrs | CPLR 214: "The following actions must be commenced within three years" incl. "an action to recover damages for an injury to property except as provided in section 214-c" and non-medical malpractice; no construction repose in §214 [sourced: https://www.nysenate.gov/legislation/laws/CVP/214, accessed 2026-11-03] |
| Illinois | 10 yrs | 735 ILCS 5/13-214 | from the act or omission; 4 yrs from discovery within the 10 | "No action based upon tort, contract or otherwise may be brought against any person ... after 10 years have elapsed from the time of such act or omission" [secondary: https://codes.findlaw.com/il/chapter-735-civil-procedure/il-st-sect-735-5-13-214/, "Current as of January 01, 2025"; ilga.gov returned 503 twice] |

**Attorney retention advice.** "Builders in Texas should keep most project-specific records for 13 years
after substantial completion"; the project-records list includes "Progress photos and field reports";
financial/tax 7 years; employment 7 years after termination; capital assets "Life of asset + 7 years"
[sourced: https://www.ftworthconstruction.lawyer/how-long-to-keep-construction-documents/, 2025-10-23].
NSPE guidance: preserve project documents "not less than the Statute of Repose ... plus three years"
[sourced: NSPE Document Retention Guidelines white paper, PDF dated 2016-06-01, as cited in verticals.md
§2.1; not re-fetched this pass]. Effective horizon for photos: 10-13 years in CA/TX/IL (9 years for Texas
residential work under a 1-2-6 warranty), 7-10 in FL, open-ended in NY [estimated: repose table above
+ NSPE 3-year buffer, or the 13-year attorney advice, whichever is longer; TX residential = 6 + 3].

### A4. Does Apple Photos / Siri (or Google Ask Photos) already solve the contractor case?

**What ships — Apple, 2024.** Apple: "Natural language search gives users the ability to search for just
about anything" by describing it (the draft's wording "In the Photos app, users can search for just about
anything by simply describing what they're looking for" was a paraphrase and is withdrawn); the example is
"Maya skateboarding in a tie-dye shirt"; search works across videos and offers smart completion
suggestions; available on "iPhone 16, iPhone 16 Plus, iPhone 16 Pro, iPhone 16 Pro Max, iPhone 15 Pro,
iPhone 15 Pro Max, iPad with A17 Pro or M1 and later, and Mac with M1 and later" [sourced:
https://www.apple.com/newsroom/2024/10/apple-intelligence-is-available-today-on-iphone-ipad-and-mac/, 2024-10-28, re-read 2026-11-03].
MacRumors: example queries "car next to lake", "yellow flowers in vase by window", "Mum in green hat with
wine glass"; "Searches use people you've already identified through the People and Pets features"; "The
Photos app must index your library first" and indexing "happens on your device" [sourced:
https://www.macrumors.com/how-to/ios-use-natural-language-search-photos/, 2024-10-25]. Early testers
reported failures on "at night"/"after dark" and "yellow car" [secondary: inkl and MacRumors forum via
search snippets, late 2024].

**What changed 2025-2026 — Apple.** iOS 26 (announced 2025-06-09): "the Photos app is updated to feature
separate tabs for Library and Collections views"; "visual intelligence now extends to a user's iPhone
screen, making it easy to search and take action across apps"; the announcement does not mention photo
search changes [sourced: https://www.apple.com/newsroom/2025/06/apple-elevates-the-iphone-experience-with-ios-26/, 2025-06-09].
Siri specifically: Apple's Apple Intelligence page (read 2026-11-03) describes "Siri AI": "Siri understands
your personal context"; "Search for a photo from years ago, easily locate an email buried in your inbox, or
pull up the details from a note you saved"; image caption "Show me photos from the last time I went to
Spain"; "Ask Siri AI about virtually anything on your display with a screenshot"; footnote: "Siri AI is
available in beta in iOS 27, iPadOS 27, macOS 27, watchOS 27, and visionOS 27", "requires an Apple
Intelligence–enabled device set to a supported language", "Siri AI will not be initially available in the
EU on iOS, iPadOS, and watchOS", "Siri AI is not available for users under 13", "Available in English,
French, Japanese, Korean, Portuguese, and Spanish to start", and "Expanded access to such features will be
available for a fee in the future" [sourced: https://www.apple.com/apple-intelligence/, accessed
2026-11-03]. So as of 2026-11-03 Siri photo search is a beta, device-gated, non-EU feature whose examples
are personal (trips, people, dates); Apple's own iPhone User Guide article "Search for photos on iPhone"
could not be read (five fetch attempts, incl. a versioned URL, returned only the guide's table of contents).
iCloud Shared Photo Library: "a separate iCloud library that up to six users can collaborate on,
contribute to, and enjoy" [sourced: https://www.apple.com/newsroom/2022/06/apple-unveils-new-ways-to-share-and-communicate-in-ios-16/, 2022-06-06].

**What ships — Google.** "Ask Photos" is "a powerful tool that uses Gemini models to search through your
massive photo gallery"; "Google Photos now has an Ask button to help you do more with your images";
example queries "what hiking trail is this?", "find my photos that feel like spring", "find more photos like
this", "can you narrow this down to photos taken in the Columbia river gorge"; it "can also transcribe
images of text, such as handwritten recipes"; "The Ask button in Google Photos is available on iOS and
Android to eligible users in the U.S."; "Ask Photos is available in a number of countries and languages"
[sourced: https://blog.google/products-and-platforms/products/photos/ask-button-ask-photos-tips/, 2026-02-10].
Still footnoted "Available in select countries to eligible users" on 2026-10-29 [sourced:
https://blog.google/products-and-platforms/products/photos/halloween-tricks-2026/, 2026-10-29]. Google's
Ask Photos help article (support.google.com/photos/answer/15057331) and the 2024 launch post both returned
404 on fetch.

**What neither can do (argued from the published feature lists above, not from a device test).** Neither
Apple Photos/Siri nor Ask Photos has a "job" or "customer" entity, so "the Smith kitchen rough-in photos"
resolves only if the user already made an album named Smith, or if the location index maps the address; a
visual query can return rough-in plumbing but cannot tell the Smith job from the Jones job on the same
street. Neither has a crew concept: a sole proprietor's library is private to one account, and a 2-5 person
shop's photos sit in 2-5 unlinked libraries (Apple's Shared Library is designed for a family group of up to
six users [sourced: Apple newsroom 2022-06-06, above]; Google's Partner sharing is one-to-one and is what
r/GooglePhotos commenters recommend for merging two people's libraries — see Part B comment threads). Neither
has an "evidence packet" export: there is no one-tap bundle of GPS + timestamp + unmodified originals + hash
for a customer dispute, which is exactly what CompanyCam's burned-in stamps and galleries provide.

**Contractor commentary on using Apple/Google Photos for work (primary, via arctic-shift, repair pass).**
- r/electricians, "CompanyCam" (2024-12-28, score 0, 17 comments): "Right now all our photos on our
  company phones/tablets get synced thru Google Photos, but it looks like there's more functionality with
  CompanyCam. What are your feelings?" [sourced: /r/electricians/comments/1hodggq/companycam/, 2024-12-28].
- r/electricians, "Company cam or something like it" (2025-09-17, score 0, 2 comments): "I am a one man
  shop (with office help) ... like most of our phones, my phone is packed with job site photos. I try to
  organize them on google drive but it's getting hard to keep up with." [sourced:
  /r/electricians/comments/1njcit9/company_cam_or_something_like_it/, 2025-09-17].
- r/electricians, "What kind of tablet/laptop do you guys carry in the field?" (2024-02-03, score 16, 35
  comments): "I don't have an iPhone. Pictures don't sync, notes don't sync, everything has to be done
  manually through Google drive or Google photos." [sourced: /r/electricians/comments/1ai9ya1/, 2024-02-03].
- r/HVAC, "Developer trying to help HVAC buddy - are small shops always this chaotic?" (2025-12-23, score 0,
  6 comments): the owner's day ends "8 PM: Starts creating invoices from photos and memory" [sourced:
  /r/HVAC/comments/1pu8gk1/, 2025-12-23].
- Comment threads on the three r/electricians posts (read in full this pass): on 1hodggq (18 archived
  comments, 7 authors, 2024-12-28 to 2025-01-23) users of CompanyCam say "we have about 16 people on it and
  love it. It's great but a little pricey", "Hands down one of the best apps I use for the business", praise
  annotation ("Big red circle and line arrow to a text box"), PDF reports and offline favourites; the poster
  asks "Is it worth paying for the top of the line version?"; alternatives offered are "a shared drive with
  folders for each job", OneNote ("free unless you run out of space"), and a vendor pitch for TaskTag's free
  plan [sourced: https://arctic-shift.photon-reddit.com/api/comments/search?link_id=1hodggq, 2024-12-28..2025-01-23].
  On 1njcit9 (3 comments) both substantive replies are vendor pitches — Jobtable "it's $59/month" and TaskTag
  ("If your photos live in your camera roll and Drive, you'll always be digging") [sourced: ...?link_id=1njcit9,
  2025-09-17 and 2026-02-16]. On 1ai9ya1 (40 comments) the answers are OneDrive/SharePoint ("OneDrive my man!",
  score 7), OneNote, Samsung quick-share, "logging in to the iCloud web interface on your PC", and rugged
  tablets at "$450"-"$499" refurbished [sourced: ...?link_id=1ai9ya1, 2024-02-04..2025-11-12]. On 1tihiv4 (3
  comments) nobody names a tool; the one substantive reply says notes are "only valuable to the note taker"
  and recommends a consistent install system instead [sourced: ...?link_id=1tihiv4, 2026-05-20].

Verdict: Apple and Google solve "what is in this picture" (Apple on 2024+ hardware; Google for "eligible
users" in select countries); Siri's personal-context photo search is an iOS 27 beta; none solves "which job,
for whom, show me the evidence, share with the crew", and electricians describe exactly that gap in their
own words (phones "packed with job site photos", organised by hand in Google Drive). The 2026 iPhone base
split by Apple-Intelligence capability is [unknown].

### A5. Pricing and distribution norms (1-9 employee trades SaaS)

**Entry prices (USD/month).**
- Jobber Core $29 billed annually / $39 one-year commitment / $49 monthly, 1 user; Connect $99-$139 for 1
  user; Grow $149-$199 for 1 user; Plus $399-$499 for 5 users; "Add users for $29/mo each"; AI Receptionist
  add-on $29/mo [sourced: https://getjobber.com/pricing/, accessed 2026-11-03].
- Housecall Pro Basic $59 annual / $79 monthly, 1 user; Essentials $149 / $189, 5 users; Max $299 / $329,
  8 users, extra users $35 [sourced: https://www.housecallpro.com/pricing/, accessed 2026-11-03].
- CompanyCam Core $63 annual / $79 monthly, 1 user (2-user limit); Crew $119 / $149, 3 users; Scale
  $249 / $299, 3 users; +$29 / $34 per extra user (see A2 for the resolved conflict).
- Floor for a one-person shop is therefore $29-$79/month depending on billing term; a 3-5 person shop pays
  $119-$199/month on annual billing (CompanyCam Crew 3 users $119, +2 users $177; Jobber Grow 1 user $149 +
  $29/user; Housecall Pro Essentials 5 users $149) [estimated: from the three pricing pages above].

**Trade associations (member counts).**
- PHCC: "approximately 3,300 plumbing and HVACR open shop and union businesses" and 65,000 technicians;
  "Approximately 125 state and local association affiliates"; founded 1883 [sourced: https://www.phccweb.org/about/, accessed 2026-11-03].
- ACCA: "60,000 professionals - over 3,000 company members" [sourced: https://www.acca.org/about, accessed 2026-11-03].
- NECA member-firm count: [unknown] — necanet.org/about-us (HTTP 403 on WebFetch and curl), /membership
  (403), necaconvention.org/about-neca (404), ecmag.com/about-us (404). What is findable: "NECA currently
  has 119 local chapters across the United States" [secondary: https://en.wikipedia.org/wiki/National_Electrical_Contractors_Association, citing necanet.org retrieved 2024-01-08];
  the national body's FY2024 total revenue was $49,095,132, member count not stated on the 990 summary
  [sourced: https://projects.propublica.org/nonprofits/organizations/530115267, FY ending Dec 2024].
- Association reach vs universe: PHCC + ACCA ≈ 6,300 companies vs 111,207 plumbing/HVAC employer
  establishments = ~5.7% [estimated: 6,300 / 111,207; overlap between the two bodies unknown], so
  associations reach a thin, larger-shop slice, not the 1-9 long tail.

**Supply-house partnerships.** CompanyCam's integrations page lists 20 partners: AccuLynx, Jobber,
JobNimbus, JobTread, Leap, QuickBooks Online, Roofr, ServiceTitan, Tugger, Eagleview, LeadPerfection,
LeadScout, HighLevel, ContractorHub, naturalForms, CQ, Ingage, SRS Roof Hub, Smartsheet, Aspire; the only
distributor-linked name is "SRS Roof Hub" (the page does not describe SRS; it is flagged on the name alone);
Ferguson, Johnstone, ABC Supply and Beacon do not appear [sourced: https://companycam.com/integrations,
accessed 2026-11-03]. The 2025-2026 press items mention no distributor or supply house [sourced:
companycam.com/press, re-read 2026-11-03]. The two PRNewswire items below are software integration
partnerships, not supply-house channels. Supply houses as a distribution channel for small-trades SaaS:
[unknown beyond the SRS Roof Hub integration].

**Where small contractors discover software.** Facebook groups, YouTube, trade shows: [unknown] — no
source reached in either pass (Facebook is not fetchable; CompanyCam's YouTube channel pages returned no
subscriber/video counts in two fetches; no search budget). Observed distribution mechanics on vendor
pages: self-serve free trials (CompanyCam "offers a 14-day free trial" [secondary: theroofingbrief.com,
2026-10-19]; Jobber/Housecall Pro trial buttons [sourced: their pricing pages]), and partner integrations
(CompanyCam-ContractorHUB 2026-08-04; CompanyCam-Infinity Home Services multi-brand rollout 2026-09-16)
[sourced:
https://www.prnewswire.com/news-releases/contractorhub-and-companycam-enter-integration-partnership-reimagining-the-potential-of-every-jobsite-photo-302841968.html, 2026-08-04;
https://www.prnewswire.com/news-releases/companycam-and-infinity-home-services-partner-to-bring-a-new-standard-of-productivity-and-transparency-to-job-sites-302877370.html, 2026-09-16; headlines only].
Reddit itself is a discovery channel in the data: the two r/electricians CompanyCam threads above are
contractors asking peers before buying.

### Part A sizing table (summary)

| Segment | Count | Basis | Tag |
|---|---|---|---|
| US construction employer establishments, 1-9 employees | 664,231 | CBP 2023 | [sourced: cbp23us.zip] + [estimated: <5 + 5-9] |
| of which specialty trade (238) | 417,656 | CBP 2023 | same |
| of which electrical (238210) | 64,076 | CBP 2023 | same |
| of which plumbing/HVAC (238220) | 85,458 | CBP 2023 | same |
| US construction nonemployers | 2,875,590 | NES 2022 | [sourced: nonemp22us.zip] |
| US small-trades universe (nonemployer + 1-9) | 3,539,821 | CBP 2023 + NES 2022 | [estimated: sum] |
| CompanyCam contractors/pros | 140,000+ | About page | [sourced: companycam.com/about] |
| CompanyCam ceiling vs small-trades universe | 4.0-4.8% | 140k-170k / 3,539,821 | [estimated] |
| UK construction businesses 0-9 employees | 865,550 | BPE 2025 | [sourced: BPE_2025_detailed_tables.xlsx] + [estimated: sum] |
| Canada construction, with employees, 1-9 | 129,326 | CBC June 2026 | [sourced: 33-10-1174-01] + [estimated: 1-4 + 5-9] |
| Canada construction, without employees | 262,066 | CBC June 2026 | [sourced: 33-10-1175-01] |
| Canada small-trades universe (0-9) | 391,392 (92.8% of 421,738) | CBC June 2026 | [estimated: sum] |
| Entry price, 1-user plan, annual billing | $29-$63/mo | Jobber, HCP, CompanyCam | [sourced: three pricing pages] |
| PHCC + ACCA company members | ~6,300 | association pages | [sourced] |

---

### Part B. Reddit evidence (arctic-shift archive; scores and comment counts as archived)

Permalinks are relative to reddit.com. Dates are UTC. "Money" = any price, paid service or paid
subscription stated in the post text as returned (first ~125 characters plus the extractor's scan, for the
original eight segments; full selftext for the repair-pass segments); comment threads are reported
separately in "What posters were told to pay". Posts are quoted by URL only; no usernames.

Coverage after repair: of the 12 requested subreddits, 9 returned data (r/GooglePhotos, r/DataHoarder,
r/Genealogy, r/widowers, r/Divorce, r/selfhosted, r/ios, plus the trade subs r/Contractor, r/HVAC and
r/electricians); r/iphone, r/GriefSupport, r/declutter, r/ProfessionalOrganizers and r/Plumbing never
returned anything but HTTP 422 (see call log). Of the requested queries, "merge accounts", "parents
photos", "combine family photos", "two icloud accounts" (r/ios) were run; "deceased iphone photos",
"husband's photos", "takeout nightmare", "scan old photos service" and "photo organizer worth it" all
returned 422 on every attempt (2-3 each).
Comment threads read: 12 with comments (1x4fpst, 1hodggq, 1njcit9, 1ai9ya1, 1tihiv4, 1xdy99s, 1t2gshr,
1x382m7, 1xemakt, 1x2j95n, 1wnclv0, 1tylhuc) plus 161t3a5, which has none archived — 264 comments in all
[estimated: 22+18+3+40+3 = 86 trade; 6+9+14+6+43+99+1 = 178 family; 86 + 178 = 264; per-thread counts are in
the two comment tables]. Facebook: not
fetchable from this environment and no search budget, so the "Facebook" half of the brief's title is unmet
[unknown].

**Segment 1 — r/GooglePhotos, query "merge accounts" (15 hits returned, 15 tabulated, 2023-11 to 2026-10)**
[sourced: https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=GooglePhotos&query=merge%20accounts&limit=15&sort=desc, accessed 2026-11-03]

| Segment | Post URL | Date | Score / comments | Paraphrase | Money mentioned |
|---|---|---|---|---|---|
| couple merge | /r/googlephotos/comments/1xdy99s/merge_2_accounts/ | 2026-10-24 | 1 / 6 | Has "a few terabytes" in "my 2tb account"; thought adding wife's account would merge them | pays for a 2 TB plan (stated); no price given |
| account transfer | /r/googlephotos/comments/1wct712/transfer_of_google_photos_to_another_google/ | 2026-09-10 | 2 / 5 | Needs to move photos to another account keeping date/time | none |
| takeout | /r/googlephotos/comments/1us5vjm/help_me_with_google_takeout/ | 2026-07-09 | 0 / 11 | Needs help using Takeout | none |
| multi-account | /r/googlephotos/comments/1t2gshr/i_have_2_x_accounts_i_want_to_merge_and_delete_1/ | 2026-05-03 | 1 / 9 | Had 3 accounts, wants to merge to one | none |
| multi-account | /r/googlephotos/comments/1rjjc3m/help_i_have_multiple_accounts_and_there_are/ | 2026-03-03 | 0 / 5 | Same pictures backed up on several accounts from different life periods | none |
| multi-account | /r/googlephotos/comments/1qry2sf/merge_of_two_google_photos_libraries_from/ | 2026-01-31 | 2 / 6 | Two libraries, personal and other; wants a merge | none |
| life event | /r/googlephotos/comments/1m5vml6/duplicate_photos_between_2_accounts/ | 2025-07-21 | 0 / 2 | Got married, new email with married name, duplicates across accounts | none |
| parent | /r/googlephotos/comments/1hwd678/my_mom_accidentally_created_two_google_photo/ | 2025-01-08 | 1 / 6 | Mom logged in with a non-Gmail address on the old phone; two accounts | none |
| multi-account | /r/googlephotos/comments/1fiwfd5/multiple_accounts_with_same_backup/ | 2024-09-17 | 1 / 1 | 3 accounts backed up the same photos | none |
| parent | /r/googlephotos/comments/1fey42p/merge_photos_from_2_google_photos_accounts/ | 2024-09-12 | 1 / 1 | Mom's free 15 GB account capped; merge into another | free tier cap (15 GB) |
| work/personal | /r/googlephotos/comments/1e93onx/syncing_google_photos_between_two_google_accounts/ | 2024-07-22 | 1 / 2 | Gmail plus Workspace business account; wants sync | Workspace (paid) implied |
| migration | /r/googlephotos/comments/199r2do/migrating_problems/ | 2024-01-18 | 2 / 2 | Uploaded to Drive on account 1, trying to move | none |
| family | /r/googlephotos/comments/19088uv/merge_organize_family_accounts/ | 2024-01-06 | 1 / 5 | Wants to merge/organize family accounts | none |
| multi-account | /r/googlephotos/comments/18inqde/3_gmail_accounts_full_with_photos_need/ | 2023-12-15 | 1 / 2 | 3 Gmail accounts full of photos | none |
| multi-account | /r/googlephotos/comments/186je4l/how_to_merge_multiple_google_photo_accounts/ | 2023-11-29 | 2 / 2 | Wants a real person's answer on merging accounts | none |

**Segment 2 — r/GooglePhotos, query "parents photos" (11 hits returned, 9 tabulated, 2026-04 to 2026-10)**
[sourced: ...?subreddit=GooglePhotos&query=parents%20photos&limit=11&sort=desc, accessed 2026-11-03].
The original pass tabulated 9 of the 11 hits and did not record the other 2; a re-run of the same query on the
repair pass returned HTTP 422 (call log), so those 2 hits are [unknown] and the segment's denominator is 9.

| Segment | Post URL | Date | Score / comments | Paraphrase | Money mentioned |
|---|---|---|---|---|---|
| parent | /r/googlephotos/comments/1x382m7/photos_lost/ | 2026-10-11 | 9 / 12 | Parents' storage full; turned off backup and deleted; photos lost | storage full (free tier) |
| parent | /r/googlephotos/comments/1x5zhb3/is_this_spam/ | 2026-10-14 | 0 / 10 | Parents got "You missed photos from [name]" email; is it spam | none |
| transfer | /r/googlephotos/comments/1wsa9ul/how_do_i_transfer_photos_from_an_account_to/ | 2026-09-28 | 1 / 1 | Two accounts on both phones; how to transfer | none |
| self-host | /r/googlephotos/comments/1vrf8hw/immich_cross_server_shared_albums_finally_here/ | 2026-08-18 | 20 / 2 | Immich cross-server shared albums shipped (exit from Google) | none |
| parent | /r/googlephotos/comments/1uzwa1j/problems_with_syncing_on_google_photos/ | 2026-07-18 | 2 / 9 | All photos show up on parents' device; can't fix | none |
| account risk | /r/googlephotos/comments/1u33o7q/what_triggers_google_to_disable_accounts_due_to/ | 2026-06-11 | 58 / 34 | Parent worried about account disablement over baby photos | none |
| account risk | /r/googlephotos/comments/1umllji/google_photos_flagging_baby_bathing_photos/ | 2026-07-03 | 53 / 35 | Worried about flagged baby bath photos | none |
| family plan | /r/googlephotos/comments/1t2y79h/deleting_photos_from_google_drive/ | 2026-05-03 | 0 / 4 | Pays for first-tier storage and shares it with family | "I pay for extra storage" (first tier; no $) |
| student | /r/googlephotos/comments/1ss00ex/account_troubles/ | 2026-04-21 | 1 / 4 | School email being deleted with ~200 GB of photos | "buy storage"/"paying monthly" implied |

**Segment 3 — r/widowers, query "photos" (14 hits returned, 14 accounted for, all 2026-10)**
[sourced: ...?subreddit=widowers&query=photos&limit=14&sort=desc, accessed 2026-11-03]

| Segment | Post URL | Date | Score / comments | Paraphrase | Money mentioned |
|---|---|---|---|---|---|
| bereaved | /r/widowers/comments/1xep922/a_girl_found_on_his_phone/ | 2026-10-25 | 43 / 14 | Day 6 alone; "Finally got into his photos" and found messages | none |
| bereaved | /r/widowers/comments/1xj00ny/creating_ai_photos/ | 2026-10-29 | 6 / 22 | Using ChatGPT to create photos of late husband and self | none (ChatGPT) |
| bereaved | /r/widowers/comments/1xet9w2/still_cant_look_at_photos_and_read_messages_after/ | 2026-10-25 | 24 / 5 | A year on, cannot look at photos or messages | none |
| bereaved | /r/widowers/comments/1wy5ams/a_long_but_worthwhile_day/ | 2026-10-06 | 47 / 8 | Assembling photos for the funeral tribute montage | none |
| bereaved | /r/widowers/comments/1wvn1p9/looking_through_photos/ | 2026-10-02 | 7 / 4 | Looking through hospital photos/videos | none |
| bereaved | /r/widowers/comments/1xigssn/i_lost_my_soulmate_at_29/ | 2026-10-31 | 32 / 16 | Lost husband at a 5K; photos referenced | none |
| (8 further hits are grief posts where "photos" is incidental; URLs: 1xd4j49, 1x96dyv, 1x8ebms, 1x6rdzf, 1x6raco, 1x5xgus, 1wwrwnr, 1wvksuo) | | 2026-10 | 5-57 / 2-62 | — | none |

**Segment 4 — r/Divorce, query "photos icloud" (15 hits returned, 15 accounted for, 2020-12 to 2026-03)**
[sourced: ...?subreddit=Divorce&query=photos%20icloud&limit=15&sort=desc, accessed 2026-11-03]

| Segment | Post URL | Date | Score / comments | Paraphrase | Money mentioned |
|---|---|---|---|---|---|
| divorce | /r/Divorce/comments/1s4lilj/decoupling_electronic_lives/ | 2026-03-26 | 2 / 2 | How to separate electronically; all family stuff in shared iCloud | none |
| divorce | /r/Divorce/comments/1ors3k6/hurts_my_heart/ | 2025-11-08 | 5 / 0 | Ex ended up with the computer holding the kids' pictures; own copy corrupted | none |
| divorce | /r/Divorce/comments/1l3puo2/my_exwife_wants_me_to_keep_copies_of_all_of_our/ | 2025-06-05 | 0 / 5 | Ex wants him to keep copies of all their photos | none |
| divorce | /r/Divorce/comments/161t3a5/how_to_get_a_copy_of_her_apple_photo_album/ | 2023-08-26 | 1 / 0 | Ex holds "all 600Gb of the family photos" in her iCloud; separation agreement has a clause; how to get a copy | 600 GB (storage, not $) |
| divorce | /r/Divorce/comments/xu3r2y/cheating_ex_wants_me_to_give_her_all_of_our/ | 2022-10-02 | 5 / 18 | Ex wants all shared photos; iCloud family account, external drive discussed | none |
| divorce | /r/Divorce/comments/yao3ri/photos/ | 2022-10-22 | 6 / 4 | What to do with iCloud photos on divorce | none |
| divorce | /r/Divorce/comments/1b7uiba/parents_have_been_divorced_for_over_5_years_i/ | 2024-03-06 | 5 / 4 | Adult child; parents' iCloud photos | none |
| divorce | /r/Divorce/comments/1bnb86o/filed_divorce_now_being_hacked_and_stalked/ | 2024-03-25 | 5 / 1 | Shared iCloud as a stalking vector after filing | none |
| (7 further hits where iCloud is incidental; one mentions $40,000 legal fees unrelated to photos) | | 2020-2025 | 1-15 / 1-22 | — | $40,000 legal fees (not photos) |

**Segment 5 — r/DataHoarder, query "family photos" (14 hits returned, 10 tabulated, 2026-09 to 2026-10)**
[sourced: ...?subreddit=DataHoarder&query=family%20photos&limit=14&sort=desc, accessed 2026-11-03].
The original pass tabulated 10 of the 14 hits and did not record the other 4; a re-run on the repair pass
returned HTTP 422 (call log), so those 4 are [unknown] and the segment's denominator is 10.

| Segment | Post URL | Date | Score / comments | Paraphrase | Money mentioned |
|---|---|---|---|---|---|
| takeout | /r/DataHoarder/comments/1wnclv0/google_photos_takeout_horror_story_300_gb_in_159/ | 2026-09-22 | 197 / 87 | "+300 GB in 159 archives, dead downloads, sleepless nights" getting own data out | "I keep paying Google" (paid storage, no price) |
| scanning | /r/DataHoarder/comments/1x2j95n/best_photo_scanner_for_hundreds_of_old_family/ | 2026-10-10 | 44 / 43 | Big stack of old family photos to digitize | Epson FastFoto named, no price |
| scanning | /r/DataHoarder/comments/1x2i45l/photo_scanning_with_autosplitter_just_got_way/ | 2026-10-10 | 21 / 7 | Months of scanning with AutoSplitter software | AutoSplitter (paid software), no price |
| scanning | /r/DataHoarder/comments/1wz3zse/can_anyone_recommend_a_decent_scanner_for_photos/ | 2026-10-06 | 6 / 16 | Scanner for family photos | "$200 or less" budget |
| phone backup | /r/DataHoarder/comments/1x7htbb/phone_photos_are_the_weak_link_in_my_321_how_do/ | 2026-10-16 | 6 / 18 | Phone photos are the messy leg of 3-2-1 backup | none |
| exit Google | /r/DataHoarder/comments/1x02m9o/nasdas_or/ | 2026-10-07 | 2 / 1 | Wants all photos off Google Photos onto own NAS | none |
| legacy | /r/DataHoarder/comments/1wkjk0k/longterm_cheap_storage_of_video_and_audio_files/ | 2026-09-19 | 15 / 25 | Disabled, broke, keeping memories for child in case of death | M-Disc 100 GB named, no price |
| archive product | (image post, removed) "I built a private archive for family photos/videos — what would make you trust it" | 2026-10-04 | 0 / 1 | Builder asking what earns trust for long-term preservation | none |
| recovery | /r/DataHoarder/comments/1ws3qhp/deleted_data_recovery_after_yearsurgent_help/ | 2026-09-28 | 0 / 6 | Irreplaceable family photos on a 2009 PC | none |
| storage cost | /r/DataHoarder/comments/1wy8aai/whats_the_best_digital_storage_method_balance/ | 2026-10-05 | 1 / 23 | External drives for family files | HDD "like £80~ per TB" |

**Segment 6 — r/Genealogy, query "scan photos" (13 hits returned, 13 accounted for, 2026-04 to 2026-10)**
[sourced: ...?subreddit=Genealogy&query=scan%20photos&limit=13&sort=desc, accessed 2026-11-03]

| Segment | Post URL | Date | Score / comments | Paraphrase | Money mentioned |
|---|---|---|---|---|---|
| service demand | /r/Genealogy/comments/1xemakt/help_finding_a_personservice_to_digitize_photos/ | 2026-10-24 | 4 / 7 | Wants a person/service to digitize photos and letters while capturing names from an older relative; the post was removed by moderators as "self-promotion or advertising" (see comment threads) | "photo scanning services" (no price) |
| boxes | /r/Genealogy/comments/1vxjbjs/1000s_of_photos_in_boxes_need_guidance_on_what_to/ | 2026-08-24 | 46 / 43 | Thousands of snapshots of family and friends, many now deceased | none |
| dedupe | /r/Genealogy/comments/1vnl2ak/organizing_dated_and_undated_duplicate_photos/ | 2026-08-13 | 1 / 0 | Photos from 4 deceased relatives, many duplicates, some undated | none |
| backlog | /r/Genealogy/comments/1v0pfhb/how_do_you_handle_the_oldphoto_side_of_your/ | 2026-07-19 | 1 / 2 | Inherited boxes; scan as you go or backlog | none |
| preservation | /r/Genealogy/comments/1uvi0at/thoughts_on_thoughtfully_preserving_and/ | 2026-07-13 | 10 / 11 | Inherited early-1900s albums; wants to digitize on a budget | "keep to a budget" |
| loss | /r/Genealogy/comments/1um5wac/starting_over_because_lost_documentsphotos/ | 2026-07-03 | 15 / 4 | Lost documents/photos; starting over | "paid genealogy websites" |
| hardware | /r/Genealogy/comments/1ufoe93/all_in_one_or_separate_printer_and_photo_scanner/ | 2026-06-25 | 0 / 11 | Printer vs dedicated photo scanner | "around $500" budget |
| context | /r/Genealogy/comments/1ubnb7n/how_do_you_keep_the_story_attached_to_scanned/ | 2026-06-21 | 5 / 5 | How to keep the story attached to scanned photos | none |
| memorial | /r/Genealogy/comments/1tylhuc/memorial_book_life_untold_vs_memorygram_vs/ | 2026-06-06 | 1 / 1 | Mom died; comparing memorial-book services | Life Untold, Memorygram (paid services, no price) |
| (4 further: tintypes 1t30tzc, family history book 1sr0iw7, two-sided scanning 1sb15nb, Philadelphia album hosting 1x4ako8) | | 2026-04 to 2026-10 | 1-9 / 2-7 | — | Ancestry paywall mentioned once |

**Segment 7 — r/Contractor, query "pictures", after 2025-01-01 (10 hits returned, 10 accounted for, 2026-09 to 2026-10)**
[sourced: ...?subreddit=Contractor&query=pictures&after=2025-01-01&limit=10&sort=desc, accessed 2026-11-03]

| Segment | Post URL | Date | Score / comments | Paraphrase | Money mentioned |
|---|---|---|---|---|---|
| contractor dispute | /r/Contractor/comments/1x4fpst/whats_worth_taking_pictures_of_before_starting_a/ | 2026-10-12 | 8 / 22 | What to photograph before a job so a pre-existing issue doesn't become a customer argument (see A3 for the comment thread) | none |
| homeowner dispute | /r/Contractor/comments/1ww7h2v/remediation_company_committing_fraud/ | 2026-10-02 | 278 / 106 | Plumber-recommended remediation firm accused of fraud | $5k deductible; $5k invoice |
| homeowner | /r/Contractor/comments/1wwo1jx/stair_post_installation_followup_cut_my_losses_or/ | 2026-10-03 | 1 / 3 | Took more pictures; paid $680 for 3 posts; fix or cut losses | $680 |
| homeowner | /r/Contractor/comments/1wj5wk8/xenon_glass_with_visible_circles/ | 2026-09-17 | 8 / 14 | Defect in new windows | 12k |
| homeowner | /r/Contractor/comments/1xc4iu6/question_about_fascia_wrap/ | 2026-10-22 | 1 / 0 | Is this fascia wrap acceptable | 3k |
| (5 further homeowner Q&A posts with pictures: 1xgvqls, 1xfajt7, 1xbxnm4, 1wj77pr, 1wfkvrl) | | 2026-09/10 | 0-1 / 0-11 | — | none |

**Segment 8 — r/HVAC, query "pictures", after 2026-06-01 (10 hits returned, 10 accounted for, 2026-09 to 2026-10)**
[sourced: ...?subreddit=HVAC&query=pictures&after=2026-06-01&limit=10&sort=desc, accessed 2026-11-03]

| Segment | Post URL | Date | Score / comments | Paraphrase | Money mentioned |
|---|---|---|---|---|---|
| tech / management | /r/HVAC/comments/1x5hi5q/im_tired_of_the_bs/ | 2026-10-14 | 315 / 136 | Daily morning meeting because someone didn't take enough pictures | none |
| warranty | /r/HVAC/comments/1x7bhn2/who_do_i_appeal_to/ | 2026-10-16 | 1 / 1 | Appealing a manufacturer warranty denial | none |
| warranty | /r/HVAC/comments/1w69rrw/lennox_core_control_water_damage/ | 2026-09-03 | 2 / 7 | ~30 warranty claims this year on one multi-site customer | none |
| other contractor's work | /r/HVAC/comments/1xize5q/wanna_see_a_burnt_new_install_we_did_not_install/ | 2026-10-29 | 38 / 34 | Documenting a competitor's failed install | none |
| callbacks | /r/HVAC/comments/1wcyvti/i_hope_whoever_did_this_is_proud_s/ | 2026-09-10 | 98 / 37 | Prior tech's bad work; callbacks | none |
| (5 further: 1x76m6j, 1x5f350, 1wz8uom, 1wvcbyo, 1wgj3x5 — not about documentation) | | 2026-09/10 | 3-104 / 11-36 | — | none |

**Segment 9 — r/selfhosted, query "family photos" (15 hits returned, 15 accounted for, 2026-10-21 to 2026-10-30; repair pass)**
[sourced: https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=selfhosted&query=family%20photos&limit=15&sort=desc, accessed 2026-11-03; 14 of the 15 are flagged `removal_type: moderator` in the archive with the title rewritten to "removed_by_moderator", so titles below are from the archived selftext]

| Segment | Post URL | Date | Score / comments | Paraphrase | Money mentioned |
|---|---|---|---|---|---|
| legacy / death | /r/selfhosted/comments/1xjcv7t/ | 2026-10-30 | 824 / 353 | "I'm thinking about death" — a self-hoster whose family is not technical asks what happens to the self-hosted data (incl. photos) when he is gone | none |
| cloud-ban fear | /r/selfhosted/comments/1xez4ro/ | 2026-10-25 | 6 / 12 | "horrific stories lately about automated cloud bans (Google, Apple, Notion) locking people out of 10+ years of family photos" | none |
| family backup | /r/selfhosted/comments/1xdmmhn/ | 2026-10-23 | 16 / 32 | Family backs up "precious photos and videos" to Synology Photos; owner frustrated with it | none |
| family Immich | /r/selfhosted/comments/1xfh06w/ | 2026-10-25 | 0 / 33 | Wants Immich on Proxmox with accounts for friends and family | none |
| builder | /r/selfhosted/comments/1xdy5kd/ | 2026-10-24 | 20 / 29 | Kinnect v1.1.0, an open-source family-sharing project | none (open source) |
| builder | /r/selfhosted/comments/1xfq5np/ | 2026-10-26 | 0 / 31 | "Airlock Photos: a self-hosted home for your photo collection", second public release | none |
| builder | /r/selfhosted/comments/1xbqpij/ | 2026-10-21 | 0 / 26 | Developer of "Pixels: Self-Hosted Photos", a third-party Immich client | none |
| builder | /r/selfhosted/comments/1xhtyjh/ | 2026-10-28 | 1 / 4 | "Latent Frames", a photo viewer for a NAS on iPhone/iPad | none |
| (7 further hits where family photos are incidental: 1xjc03h, 1xixjnb, 1xg8g06, 1xe76b6, 1xck22e, 1xbftxa and one Tailscale/Cloudflare post) | | 2026-10 | 0-13 / 3-45 | — | none |

Pattern: four of the fifteen are developers announcing self-hosted photo tools and the top post (score 824)
is about what happens to a family archive when its one technical member dies — the inheritance pain seen
from the builder's side, with no money mentioned anywhere.

**Segment 10 — r/ios, query "two icloud accounts" (15 hits returned, 15 accounted for, 2025-11 to 2026-10; repair pass)**
[sourced: ...?subreddit=ios&query=two%20icloud%20accounts&limit=15&sort=desc, accessed 2026-11-03]

| Segment | Post URL | Date | Score / comments | Paraphrase | Money mentioned |
|---|---|---|---|---|---|
| backup exit | /r/ios/comments/1sbpeq0/looking_for_an_ios_app_to_sync_icloud_photos_to/ | 2026-04-03 | 4 / 6 | Wants a two-way mirror of the iCloud Photo Library to a Ugreen NAS as a "failsafe" copy | NAS owned (no price) |
| two accounts | /r/ios/comments/1wwf4xk/two_apple_accounts_became_inaccessible_on_the/ | 2026-10-03 | 1 / 4 | Created a second iCloud account on a new iPad; both accounts now locked in "Request Access" | none |
| two regions | /r/ios/comments/1ww7t65/moved_from_us_to_nz_can_i_access_icloudapple_pay/ | 2026-10-02 | 0 / 4 | Moved countries; needs two region accounts | none |
| (12 further hits are keychain, mail, feature-list and account-security posts where "two accounts" is incidental: 1xb8emr, 1wlz93i, 1wk919h, 1vbyp5p, 1vb36nq, 1u0nez0, 1u0kv85, 1sqvwhf, 1s425i1, 1pycvlq, 1pdh69u, 1p1wmwv) | | 2025-11 to 2026-10 | 0-131 / 0-37 | — | none |

Pattern: the query did not surface a "merge two iCloud photo libraries" thread on r/ios; the only photo
post is an exit-to-NAS post.

**Segment 11 — r/electricians, query "pictures before", after 2025-01-01 (15 hits returned, 15 accounted for, 2025-09 to 2026-10; repair pass)**
[sourced: ...?subreddit=electricians&query=pictures%20before&after=2025-01-01&limit=15&sort=desc, accessed 2026-11-03]

| Segment | Post URL | Date | Score / comments | Paraphrase | Money mentioned |
|---|---|---|---|---|---|
| documentation system | /r/electricians/comments/1tihiv4/job_logs/ | 2026-05-20 | 1 / 2 | Growing shop; crews hand off jobs; "guys forget what they did 8 months ago"; "We take a lot of videos and pictures" but wants a system | none |
| past-customer mapping | /r/electricians/comments/1pyjna3/do_you_guys_track_where_youve_worked_before/ | 2025-12-29 | 1 / 1 | Wants an app that photographs old paper invoices and maps past customers; "couldn't find anything" | none |
| homeowner verification | /r/electricians/comments/1uradh5/ev_charger_installation_is_this_done_correctly/ | 2026-07-09 | 0 / 31 | "Before and after pictures attached. Is this done correctly" | none |
| DIY | /r/electricians/comments/1nkie56/electric_socket_replacement/ | 2025-09-18 | 0 / 7 | "I took pictures before removing the wires" | none |
| (11 further hits are homeowner/DIY fault questions or unrelated: 1x838mj, 1wdu76f, 1vn3ua0, 1thaw7y, 1szfudz, 1s5nh7l, 1s2ojfd, 1r3v3na, 1qp2jch, 1pathjg, 1p8nhl6) | | 2025-11 to 2026-10 | 0-43 / 1-15 | — | none |

**Segment 12 — r/electricians, query "google photos" (15 hits returned, 15 accounted for, 2023-01 to 2025-10; repair pass)**
[sourced: ...?subreddit=electricians&query=google%20photos&limit=15&sort=desc, accessed 2026-11-03]

| Segment | Post URL | Date | Score / comments | Paraphrase | Money mentioned |
|---|---|---|---|---|---|
| Google Photos at work | /r/electricians/comments/1hodggq/companycam/ | 2024-12-28 | 0 / 17 | Shop's photos "get synced thru Google Photos"; considering CompanyCam for "more functionality" | CompanyCam (price not stated in post) |
| camera roll overflow | /r/electricians/comments/1njcit9/company_cam_or_something_like_it/ | 2025-09-17 | 0 / 2 | One-man shop; phone "packed with job site photos"; organises in Google Drive, "getting hard to keep up" | iPad bought (no price); CompanyCam considered |
| sync friction | /r/electricians/comments/1ai9ya1/what_kind_of_tabletlaptop_do_you_guys_carry_in_the_field/ | 2024-02-03 | 16 / 35 | No iPhone: "Pictures don't sync, notes don't sync, everything has to be done manually through Google drive or Google photos" | none |
| (12 further hits matched "Google" in another sense — Nest, Google Ads, Google My Business, SEO pitches — 1oitd21, 1k4dggd, 1jvh2k3, 1ig23o0, 1ig23o9, 1fi7esd, 1cz5thm, 1avzvyj, 1aeajei, 19e46uf, 167p6ee, 104apo4) | | 2023-01 to 2025-10 | 0-6 / 1-10 | — | none |

A parallel r/HVAC "google photos" query (15 hits, 2019-12 to 2026-02) matched only "Google" in the
Nest/Ads sense; the one relevant hit is the 2025-12-23 small-shop post whose owner "Starts creating invoices
from photos and memory" at 8 PM [sourced: ...?subreddit=HVAC&query=google%20photos&limit=15&sort=desc;
/r/HVAC/comments/1pu8gk1/, 2025-12-23]. The same query on r/Contractor returned 422.

**What posters were told to pay — comment threads read (repair pass; family segments).** Eight threads
requested, seven returned comments (161t3a5 has none archived); all comments read in full, quoted by thread URL only.

| Thread (post) | Comments archived / read | What commenters told the poster to do | Money named by commenters |
|---|---|---|---|
| 1xdy99s merge two Google accounts (2026-10-24) | 6 / 6 | Use Partner sharing: share all photos from her account, accept, turn on "Save to your library"; adding her to the family plan needs "shared storage" enabled; she must use her own 15 GB before the 2 TB | none — free built-in features; the 2 TB plan is the poster's existing cost |
| 1t2gshr merge 3 accounts into 1 (2026-05-03) | 9 / 9 | "Google Partner Share to copy them to the account you want to keep", enable auto-save, wait, disconnect; "Export with Google Takeout and upload to new account should work"; storage-accounting bug warned about | none |
| 1x382m7 parents' photos lost (2026-10-11) | 14 / 14 | Check Google Photos trash; try takeout.google.com; should have checked storage levels before deleting | none |
| 1xemakt wants a person/service to digitize photos and letters (2026-10-24) | 6 / 6 | Moderator removed the post as "self-promotion or advertising" (sub rule); one substantive reply: treat digitizing and oral-history capture as two separate tasks and find "someone who has the equipment and expertise" | none — no price named by anyone |
| 1x2j95n best scanner for hundreds of old family photos (2026-10-10) | 43 / 43 | Used Epson flatbeds "<$50" / "no more than $75" on eBay; VueScan "over $100 ... worth every single penny"; a camera rig may be "cheaper than a scanner"; "Then & There: Scan & Date" one-off purchase; one commenter, apparently a scanning-service operator, says ".025/photo is dangerously low cost. Plenty of folks out there who will pay a premium" | $50-$75 hardware; >$100 software; $0.025/photo as a too-low service price |
| 1wnclv0 Takeout horror story, 300 GB (2026-09-22) | 99 / 99 | Request 50 GB archives not 2 GB; export to Drive/OneDrive/Dropbox and pull with rclone; "cheap vps" as a download relay; immich-go / takeout-helper tools; "I pay for 2Tb"; "I pay for additional Google storage"; OneDrive "6TB with the family plan"; "Google photos is a scam. They keep your files hostage so you keep paying forever" | storage subscriptions (no prices); a VPS (no price); no service fee |
| 161t3a5 ex holds 600 GB in iCloud (2023-08-26) | 0 / 0 | archive holds no comments (post shows 0 comments) | — |
| 1tylhuc memorial-book services (2026-06-06) | 1 / 1 (third attempt; 422 ×2 before) | The only reply, a moderator: "I wouldn't use either one"; Life Untold and Memorygram flood the sub with "crappy marketing posts" and "we delete any posts that mention them" | none |

Trade-segment threads read: 1x4fpst (22 comments, A3); 1hodggq (18), 1njcit9 (3), 1ai9ya1 (40), 1tihiv4 (3) —
see A4 for content [sourced: arctic-shift comments/search for each link_id, accessed 2026-11-03].

[sourced: https://arctic-shift.photon-reddit.com/api/comments/search?link_id=<id>&limit=50..100 for each id above, accessed 2026-11-03; comment dates 2026-05-03 to 2026-10-25].

Reading: in seven threads and 178 comments [estimated: 6+9+14+6+43+99+1], nobody tells a poster to pay a
person or service to merge, transfer, recover or organise a digital library; the advice is always a free
built-in feature (Partner sharing, Takeout, trash) or a tool. Money is named only for scanning hardware and
software, and the one service price point that appears is offered by a vendor, not a buyer.

**Where money changes hands.** Denominators, stated once: the original eight segments returned 102 hits
of which 96 are tabulated or listed by ID above (Segment 2 has 2 and Segment 5 has 4 unrecorded hits); the
repair pass added four segments with 60 hits (15 + 15 + 15 + 15), all accounted for; so the post base is
156 tabulated/listed posts from 162 hits [estimated: 15+9+14+15+10+13+10+10 = 96; 96 + 60 = 156; 102 + 60 =
162]. Money columns for the original eight segments were built from the first ~125 characters of each
post plus the extractor's scan; the four new segments from full selftext. Comments: 264 read across 12
threads (86 trade + 178 family) [estimated: 22+18+3+40+3 = 86; 6+9+14+6+43+99+1 = 178].
- Trades: the only dollar figures are homeowners' job costs in dispute ($680; $5k/$5k; 3k; 12k). No
  contractor post or comment names a price for a documentation tool; "photos are free" appears twice in
  1x4fpst; two r/electricians posts weigh CompanyCam against Google Photos/Drive without naming its price
  (their comment threads do: CompanyCam "a little pricey" from a 16-user shop, "Is it worth paying for the
  top of the line version?", and two vendor pitches incl. Jobtable at "$59/month" — the only subscription price
  stated anywhere in the trade sample, by a vendor; plus refurbished rugged tablets at $450-$499).
- Paid cloud storage: stated as a current cost, without a price, in 5 posts (1xdy99s 2 TB plan; 1wnclv0 "I
  keep paying Google"; 1t2y79h "I pay for extra storage"; 1ss00ex school account with ~200 GB; 1e93onx
  Workspace) and by several 1wnclv0 commenters ("I pay for 2Tb", "6TB with the family plan") [estimated:
  count of rows above]. That is 5 of 156 posts — a recurring, not "near-universal", mention; no post or
  comment states a dollar figure for storage.
- Scanning hardware/software: $200 and $500 stated budgets (posts); $50-$75 used flatbeds and >$100
  VueScan (comments); Epson FastFoto, AutoSplitter, M-Disc named without prices; one vendor-side service
  price point ($0.025/photo, called too low) in comments; one post explicitly seeking a paid digitising
  person/service (1xemakt) was removed by moderators as advertising and received no price.
- Memorial-book services (Life Untold, Memorygram) in one post, no price; the only comment is a moderator
  saying the sub deletes posts naming them because of their marketing spam.
- Organizer/consultant fees for merging, transferring, inheriting or organising a digital library: none
  in 156 posts and none in 178 family-thread comments [sourced: counts across the tables above].
- Divorce: the only dollar figure ($40,000) is legal fees unrelated to photos; the photo posts describe
  negotiation over copies, not payment.
Pattern: people already pay the platform for storage and pay for hardware to digitise paper; when they ask
how to merge, move or recover a digital library they are told to use free built-in features, and nobody in
this sample reports paying — or being told to pay — anyone to do it. That is the gap a service would have
to create demand for, not harvest.

---

## 3. Numbers table

| Number | Context | Tag |
|---|---|---|
| 814,557 | US construction employer establishments, 2023 | [sourced: cbp23us.zip, 2023] |
| 938,478 | US construction establishments, BLS QCEW 2024 private annual average (verticals.md denominator) | [sourced: BLS QCEW via verticals.md §2.1 Q4] |
| 536,259 / 127,972 | NAICS 23 establishments with <5 / 5-9 employees | [sourced: cbp23us.zip] |
| 664,231; 81.5% | NAICS 23 establishments 1-9; share | [estimated: <5 + 5-9 from cbp23us.zip] |
| 521,315; 417,656; 80.1% | NAICS 238 establishments; 1-9; share | [sourced + estimated as above] |
| 83,342 / 64,076 | 238210 electrical establishments / 1-9 | [sourced + estimated] |
| 111,207 / 85,458 | 238220 plumbing-HVAC establishments / 1-9 | [sourced + estimated] |
| 7,659,459 | NAICS 23 employees (CBP 2023) | [sourced: cbp23us.zip] |
| 81.7%; 81.2%; 82.1% | CPWR: 1-9 share of payroll establishments, 2014-23 avg; 2023; 2014 | [sourced: CPWR Data Bulletin, April 2026] |
| 78.1% | Nonemployers as share of all construction establishments, 2021 | [sourced: CPWR, April 2026] |
| 2,875,590 | NAICS 23 nonemployer establishments, 2022 | [sourced: nonemp22us.zip, 2022] |
| $238.0B | NAICS 23 nonemployer receipts, 2022 | [sourced: nonemp22us.zip] |
| 1,916,528 | NAICS 238 nonemployers, 2022 | [sourced: nonemp22us.zip] |
| $82,780 | Receipts per nonemployer construction establishment | [estimated: 238,039,583K / 2,875,590] |
| 3,539,821; 95.9% | Small-trades universe (nonemployer + 1-9); share of 3,690,147 | [estimated: CBP 2023 + NES 2022] |
| 3,520,147 | Establishments not on CompanyCam, lower bound | [estimated: 3,690,147 − 170,000] |
| 885,485; 173,740; 865,550; 97.8% | UK construction businesses: all; 1-9 employees; 0-9; 0-9 share | [sourced: BPE 2025 Table 5] + [estimated: sums] |
| 159,672; 98,704; 30,622; 129,326; 81.0% | Canada construction with employees: total; 1-4; 5-9; 1-9; share | [sourced: StatCan 33-10-1174-01, June 2026] + [estimated: sum/ratio] |
| 262,066; 421,738; 391,392; 92.8% | Canada construction without employees; all; 0-9; 0-9 share | [sourced: StatCan 33-10-1175-01] + [estimated: sums] |
| 101,223; 81,827; 137,833 | Canada specialty trade (238): employers; 1-9; without employees | [sourced: StatCan tables above] + [estimated: sum] |
| 140,000+ | CompanyCam "contractors and pros" | [sourced: companycam.com/about, 2026-11-03] |
| 170,000+ | CompanyCam "contractors", 2024-02-28 | [sourced: companycam.com/press via verticals.md] |
| 1 billion+ | Photos taken in CompanyCam | [sourced: companycam.com/about] |
| 285,000+ | CompanyCam "pros" (Instagram bio) | [secondary: theroofingbrief.com, 2026-10-19] |
| 17.2 / 14.9 / 21.1 / 4.9 / 4.0 / 3.8% | CompanyCam ceiling (140k) vs CBP / QCEW / 1-9 / nonemployers / small-trades universe / all | [estimated: A2 table] |
| 20.9 / 18.1 / 25.6 / 5.9 / 4.8 / 4.6% | Same with 170k | [estimated: A2 table] |
| $79/$63; $149/$119; $299/$249; $34/$29 | CompanyCam Core/Crew/Scale monthly/annual; extra user, plan-card data attributes | [sourced: companycam.com/pricing raw HTML, 2026-11-03] |
| 63 / 129 / 199 | CompanyCam "Compare Plans" table (stale) | [sourced: companycam.com/pricing, 2026-11-03] |
| 2026-09-17 | Claimed date of Scale price rise; grandfathered $249/$199 | [secondary: theroofingbrief.com, 2026-10-19] |
| 100 | Magic Uploader photos per batch | [sourced: help.companycam.com/…/6828411] |
| 20; 1 | CompanyCam integration partners listed; distributor-linked name (SRS Roof Hub) | [sourced: companycam.com/integrations, 2026-11-03] |
| $29 / $39 / $49 | Jobber Core annual / 1-yr / monthly | [sourced: getjobber.com/pricing] |
| $29 | Jobber extra user; AI Receptionist add-on | [sourced: getjobber.com/pricing] |
| $59 / $79; $149 / $189; $299 / $329; $35 | Housecall Pro Basic, Essentials, Max (annual/monthly); extra user | [sourced: housecallpro.com/pricing] |
| ~3,300; 65,000; ~125 | PHCC businesses; technicians; chapters | [sourced: phccweb.org/about] |
| 60,000; 3,000+ | ACCA professionals; company members | [sourced: acca.org/about] |
| 119 | NECA local chapters | [secondary: Wikipedia citing necanet.org, retrieved 2024-01-08] |
| $49,095,132 | NECA national FY2024 total revenue | [sourced: ProPublica Nonprofit Explorer, EIN 53-0115267] |
| ~5.7% | PHCC+ACCA companies / 238220 establishments | [estimated: 6,300 / 111,207] |
| 50%; 40%; 42%; 35%; 500+ | Levelset 2019 payment survey: not paid on time; back charges after completion; pay before paid; dip into savings; sample | [sourced: levelset.com/tools/national-construction-payments-report/, 2019] |
| $70,000 | One roofing enterprise's rework cost for lack of underlayment documentation | [sourced: companycam.com blog, 2026-09-18; vendor anecdote] |
| 10 / 10 (6 residential w/ warranty) / 7 / none / 10 | Repose years CA / TX / FL / NY / IL | [sourced: statute texts and dated code copies, A3 table] |
| 2023-09-01 | Texas HB 2024 effective date (absent two-thirds vote) | [sourced: capitol.texas.gov HB02024F, 2023] |
| 13 years | Attorney retention advice (TX) incl. progress photos | [sourced: ftworthconstruction.lawyer, 2025-10-23] |
| repose + 3 years | NSPE retention guidance | [sourced: NSPE white paper 2016-06-01 via verticals.md] |
| 6 | Users per iCloud Shared Photo Library | [sourced: Apple newsroom, 2022-06-06] |
| iOS 27 (beta) | Siri AI photo search availability | [sourced: apple.com/apple-intelligence, 2026-11-03] |
| 2010-03-22 to 2010-07-21; 33 | ContractorTalk thread 75552 post dates; posts | [sourced: contractortalk.com thread, fetched 2026-11-03] |
| 315 / 136 | Score / comments, r/HVAC "tired of the BS" (not enough pictures) | [sourced: arctic-shift, post 1x5hi5q, 2026-10-14] |
| 8 / 22; 1; 1; 2 | r/Contractor 1x4fpst score/comments; comments naming MagicPlan; naming CompanyCam/Google/Apple Photos (none); commenters suspecting a sales pitch | [sourced: arctic-shift comments/search?link_id=1x4fpst, re-read 2026-11-03] |
| 17; 35; 2 | Comments on r/electricians 1hodggq, 1ai9ya1, 1njcit9 | [sourced: arctic-shift, dates in A4] |
| 197 / 87 | Score / comments, Takeout horror story | [sourced: arctic-shift, post 1wnclv0, 2026-09-22] |
| 600 GB | Family photos held by ex in iCloud | [sourced: arctic-shift, post 161t3a5, 2023-08-26] |
| $200; $500 | Stated scanner budgets | [sourced: arctic-shift, posts 1wz3zse, 1ufoe93] |
| $75; <$50; "over $100" | Used Epson flatbeds; VueScan, per 1x2j95n commenters | [sourced: arctic-shift comments/search?link_id=1x2j95n, 2026-10-10/11] |
| $0.025/photo | Scanning-service price point one commenter calls "dangerously low" | [sourced: arctic-shift comments 1x2j95n, 2026-10-11; commenter appears to run a scanning service] |
| 162; 156; 96; 60 | Reddit posts: hits returned (12 segments); tabulated/listed; of which original eight segments; new four | [estimated: per-segment headers in Part B] |
| 264 | Comments read across 12 threads (11 with comments) | [estimated: 22+18+3+40+3+6+9+14+6+43+99+1] |
| 824 / 353 | Score / comments, r/selfhosted "what happens to your selfhosted data when you're gone" | [sourced: arctic-shift, post 1xjcv7t, 2026-10-30] |
| 0 / 17; 0 / 2; 16 / 35 | r/electricians CompanyCam-vs-Google-Photos threads score/comments | [sourced: arctic-shift, 1hodggq, 1njcit9, 1ai9ya1] |
| $59/month | Jobtable, pitched by a vendor in 1njcit9 comments | [sourced: arctic-shift comments 1njcit9, 2025-09-17] |
| 16 | Users at one shop that finds CompanyCam "a little pricey" | [sourced: arctic-shift comments 1hodggq, 2024-12-29] |
| 5 of 156 | Posts stating a current paid-storage cost (no price) | [estimated: count in money block] |
| 0 | Posts or comments reporting payment to merge/inherit/organize a digital library | [sourced: count across 156 posts and 178 family-thread comments] |
| 51; 19; 32 | arctic-shift repair-pass calls; HTTP 200; failed (30 × 422, 2 × 400) — by batch: probes 1/2, batch 1 10/10, batch 2 2/10, batch 3 2/10, batch 4 4/0 | [sourced: call log, §4] |
| 13 | WebSearch calls refused for budget in the repair pass (original pass: 14 completed before exhaustion) | [sourced: tool responses, 2026-11-03] |

---

## 4. Unknowns and what was tried

| Unknown | What was tried |
|---|---|
| CompanyCam paying-company count 2025-2026 | press page re-read (2025-08-22 and 2026-03-02 both say "tens of thousands" of businesses), About page (140k+ pros); company is private (no SEC filing); PitchBook/Crunchbase need search budget, which was exhausted |
| Exact date of CompanyCam's Scale price rise and the grandfathering terms | pricing page raw HTML confirms the new card prices but contains no date or grandfathering text (grep for "grandfather", "Sept", "joined before": none); only the 2026-10-19 review states 2026-09-17 |
| CompanyCam MCP plan eligibility; whether OCR text is searchable | blog and help articles read; neither states it |
| Survey quantifying money lost for lack of photos | Levelset 2019 report found (payment timing only; no photo question); Levelset post sitemaps ×3 and resource-hub sitemap scanned (no later report); Rabbet ×2, Procore ×2, Levelset /payment-report/, /research/, /blog/construction-payment-report/ all 404 |
| Insurer photo-evidence requirements for contractors | Hartford construction-risk page 503 ×2; Next Insurance blog index has no documentation post; Insureon has only policyholder-side advice (quoted) |
| Mike Holt forum quotes by URL | forums.mikeholt.com 403 on WebFetch (original) and curl (repair) |
| r/Plumbing threads | arctic-shift 422: original pass (count unlogged), repair pass 3 attempts (plumbing_pictures, plumbing_photos, plumbing2) |
| r/iphone, r/GriefSupport, r/declutter, r/ProfessionalOrganizers | arctic-shift 422 on every attempt: r/iphone ×3 (deceased ×2, husband, two icloud), r/GriefSupport ×3, r/declutter ×3, r/ProfessionalOrganizers ×3 (call log below) |
| Queries "deceased iphone photos", "husband's photos", "takeout nightmare", "scan old photos service", "photo organizer worth it" | each attempted 2-3 times across batches; all 422 (call log) |
| The 2 untabulated r/GooglePhotos "parents photos" hits and 4 untabulated r/DataHoarder "family photos" hits | not recorded by the original pass; re-runs on the repair pass returned 422 |
| Comments on 161t3a5 (divorce 600 GB) | 200 but the archive holds no comments for it (post shows 0 comments); 1tylhuc succeeded on the third attempt (1 comment) |
| Facebook-group evidence (family or trades) | facebook.com is not fetchable from this environment; no search budget in either pass |
| Contractor commentary on Apple Photos specifically | the r/electricians threads found concern Google Photos / camera roll; no Apple Photos thread surfaced; r/Contractor "google photos" 422 |
| Apple's own description of Photos search in 2026 | iPhone User Guide "Search for photos" fetched 5 times (3 offsets, 1 versioned URL, 1 Shared Library article) — only the TOC rendered; Apple Intelligence page used instead |
| Share of 2026 iPhone base with Apple Intelligence | not researched (no budget) |
| Facebook groups / YouTube / supply houses / trade shows as discovery channels | Facebook not fetchable; youtube.com/@CompanyCam and /about rendered no counts; no search budget; integrations page gives one distributor name (SRS Roof Hub) |
| NECA member-firm count | necanet.org/about-us (403 WebFetch + curl), /membership (403), necaconvention.org/about-neca (404), ecmag.com/about-us (404); Wikipedia (119 chapters) and ProPublica 990 (revenue only) used |
| Buildertrend photo/AI features and pricing | buildertrend.com/pricing (403 ×2), /features (403), /newsroom (403), help.buildertrend.com (reset), Capterra (403), SoftwareAdvice (403), GetApp (404), Google Play (truncated), Wikipedia (404) |
| Photo-documentation startups 2024-2026 beyond YC and verticals.md | YC construction directory read (Opusense AI P2025); no search budget for Crunchbase/press |
| Scanning-service prices paid by Redditors | none stated in any post; one commenter's $0.025/photo price point (1x2j95n) is the only service price seen; providers' price lists not fetched |
| Canada (resolved) | 33-10-0810-01 was the wrong table; the cube list revealed 33-10-1174/1175-01 (June 2026) — see A1 |

**arctic-shift call log, repair pass 2026-11-03** [sourced: scratchpad `as/log.txt`, `log2.txt`, `log3.txt`, `log4.txt`, written by the batch scripts]. Spacing 25-30 s between calls; 422 = "Timeout. Maybe slow down a bit".

| Batch | Call | Endpoint / parameters | HTTP |
|---|---|---|---|
| probe | selfhosted | posts r/selfhosted "family photos" limit 15 | 200 |
| probe | ios (probe) | posts r/ios "two icloud accounts" | 422 |
| probe | iphone (probe) | posts r/iphone "deceased photos" | 422 |
| 1 | ios_two_icloud | posts r/ios "two icloud accounts" limit 15 | 200 |
| 1 | iphone_deceased | posts r/iphone "deceased photos" | 422 |
| 1 | griefsupport_photos | posts r/GriefSupport "photos phone" | 422 |
| 1 | declutter_photos | posts r/declutter "photos" | 422 |
| 1 | proorg_photos | posts r/ProfessionalOrganizers "photo" | 422 |
| 1 | plumbing_pictures | posts r/Plumbing "pictures before" after 2025-01-01 | 422 |
| 1 | electricians_pictures | posts r/electricians "pictures before" after 2025-01-01 | 200 |
| 1 | gp_combine_family | posts r/GooglePhotos "combine family photos" | 200 |
| 1 | gp_takeout_nightmare | posts r/GooglePhotos "takeout nightmare" | 422 |
| 1 | dh_scan_service | posts r/DataHoarder "scan old photos service" | 422 |
| 1 | ios_husband | posts r/iphone "husband photos" | 422 |
| 1 | gen_organizer_worth | posts r/Genealogy "photo organizer worth it" | 422 |
| 1 | c_1xemakt | comments link_id=1xemakt | 200 |
| 1 | c_1xdy99s | comments link_id=1xdy99s | 200 |
| 1 | c_161t3a5 | comments link_id=161t3a5 (0 comments archived) | 200 |
| 1 | c_1x2j95n | comments link_id=1x2j95n | 200 |
| 1 | c_1wnclv0 | comments link_id=1wnclv0 | 200 |
| 1 | c_1t2gshr | comments link_id=1t2gshr | 200 |
| 1 | c_1tylhuc | comments link_id=1tylhuc | 422 |
| 1 | c_1x382m7 | comments link_id=1x382m7 | 200 |
| 2 | contractor_googlephotos | posts r/Contractor "google photos" | 422 |
| 2 | hvac_googlephotos | posts r/HVAC "google photos" | 200 |
| 2 | electricians_googlephotos | posts r/electricians "google photos" | 200 |
| 2 | plumbing_photos | posts r/Plumbing "photos customer" after 2025-01-01 | 422 |
| 2 | electricians_photos | posts r/electricians "photos customer" after 2025-01-01 | 422 |
| 2 | iphone_two_icloud | posts r/iphone "two icloud accounts" | 422 |
| 2 | ios_family_photos | posts r/ios "family photos icloud" | 422 |
| 2 | grief_photos | posts r/GriefSupport "photos" after 2026-06-01 | 422 |
| 2 | declutter_digital | posts r/declutter "digital photos" | 422 |
| 2 | proorg_photo2 | posts r/ProfessionalOrganizers "photos" | 422 |
| 2 | c_contractor_gp_comments | comments r/Contractor query "google photos" (HTTP 400: query param not accepted) | 400 |
| 2 | c_hvac_gp_comments | comments r/HVAC query "google photos" (HTTP 400) | 400 |
| 3 | gp_parents_photos | posts r/GooglePhotos "parents photos" limit 11 (re-run) | 422 |
| 3 | dh_family_photos | posts r/DataHoarder "family photos" limit 14 (re-run) | 422 |
| 3 | c_1x4fpst | comments link_id=1x4fpst (re-fetch, 22) | 200 |
| 3 | iphone_deceased2 | posts r/iphone "deceased photos" (retry) | 422 |
| 3 | griefsupport2 | posts r/GriefSupport "photos phone" (retry) | 422 |
| 3 | declutter2 | posts r/declutter "photos" after 2025-01-01 (retry) | 422 |
| 3 | proorg2 | posts r/ProfessionalOrganizers "photo" (retry) | 422 |
| 3 | plumbing2 | posts r/Plumbing "pictures before" after 2025-06-01 (retry) | 422 |
| 3 | gp_takeout2 | posts r/GooglePhotos "takeout nightmare" (retry) | 422 |
| 3 | dh_scan2 | posts r/DataHoarder "scan old photos service" (retry) | 422 |
| 3 | gen_worth2 | posts r/Genealogy "photo organizer worth it" (retry) | 422 |
| 3 | c_1tylhuc2 | comments link_id=1tylhuc (retry, 1 comment) | 200 |
| 4 | c_1hodggq | comments link_id=1hodggq (18) | 200 |
| 4 | c_1njcit9 | comments link_id=1njcit9 (3) | 200 |
| 4 | c_1ai9ya1 | comments link_id=1ai9ya1 (40) | 200 |
| 4 | c_1tihiv4 | comments link_id=1tihiv4 (3) | 200 |

Totals: 51 calls, 19 returned 200, 32 failed (422 or 400) [sourced: the log files above].

---

## 5. Source list (access date 2026-11-03)

Primary / near-primary
1. https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23us.zip — CBP 2023 US file (released 2025-06-26)
2. https://www2.census.gov/programs-surveys/nonemployer-statistics/datasets/2022/historical-datasets/nonemp22us.zip — NES 2022 US file
3. https://www.cpwr.com/wp-content/uploads/DataBulletin-April2026.pdf — CPWR Data Bulletin, April 2026
4. https://assets.publishing.service.gov.uk/media/68dbccc9c487360cc70c9f4e/BPE_2025_detailed_tables.xlsx — UK BPE 2025 (2025-10-02)
4a. https://www150.statcan.gc.ca/n1/tbl/csv/33101174-eng.zip and https://www150.statcan.gc.ca/n1/tbl/csv/33101175-eng.zip — Canadian Business Counts, with / without employees, June 2026 (released 2026-08-14); table list from https://www150.statcan.gc.ca/t1/wds/rest/getAllCubesListLite
5. https://companycam.com/about — 140k+ contractors and pros; 1B+ photos
6. https://companycam.com/press — 2025-08-22 Series C; 2026-03-02 acquisition
7. https://companycam.com/pricing — plan-card data attributes (raw HTML), Compare Plans table, FAQ
8. https://companycam.com/features — feature copy
8a. https://companycam.com/integrations — 20 partners incl. SRS Roof Hub
8b. https://companycam.com/resources/blog/compounding-cost-of-inconsistent-documentation — 2026-09-18 (vendor)
9. https://companycam.com/resources/blog/ways-contractors-use-companycam-mcp-ai-daily-tasks — MCP beta, 2026-09-09 (quotes re-verified)
10. https://help.companycam.com/en/articles/6828411-uploading-existing-photos-and-videos — camera-roll import
11. https://help.companycam.com/en/articles/7045817-adding-date-time-and-gps-coordinate-stamps-to-photos — stamps
12. https://help.companycam.com/en/articles/10943941-scanning-text-on-photos — OCR
13. https://help.companycam.com/en/collections/19746674-camera-settings — article list
14. https://getjobber.com/pricing/ — Jobber pricing
15. https://www.housecallpro.com/pricing/ — Housecall Pro pricing
15a. https://www.servicetitan.com/features — feature index ("equipment nameplate scanning")
15b. https://www.ycombinator.com/companies/industry/construction — Opusense AI (P2025), Albiware (S2022)
16. https://www.phccweb.org/about/ — PHCC
17. https://www.acca.org/about — ACCA
17a. https://projects.propublica.org/nonprofits/organizations/530115267 — NECA national 990 summary (FY2024)
18. https://www.sdvfenchurch.com/state-survey/statutes-of-limitations-and-repose-for-construction-related-claims/ — repose survey (current as of 08/2024; page dated 2026-08-20)
18a. https://capitol.texas.gov/tlodocs/88R/billtext/html/HB02024F.htm — Texas HB 2024 (2023), 6-year residential repose
18b. https://www.flsenate.gov/Laws/Statutes/2025/95.11 — Florida §95.11 (2025), 7-year repose; history through ch. 2025-153
18c. https://www.nysenate.gov/legislation/laws/CVP/214 — NY CPLR 214
19. https://www.ftworthconstruction.lawyer/how-long-to-keep-construction-documents/ — 13-year advice, 2025-10-23
19a. https://www.levelset.com/tools/national-construction-payments-report/ — 2019 payment survey (500+)
19b. https://www.insureon.com/blog/mistakes-small-business-owners-make-when-filing-insurance-claims — insurer documentation advice, updated 2026-07-31
19c. https://www.contractortalk.com/threads/permission-to-use-pictures-of-homes-youve-done.75552/ — 2010 thread, fetched in full with curl (bathtub anecdote)
20. https://www.apple.com/newsroom/2024/10/apple-intelligence-is-available-today-on-iphone-ipad-and-mac/ — 2024-10-28 (quote corrected)
20a. https://www.apple.com/newsroom/2025/06/apple-elevates-the-iphone-experience-with-ios-26/ — 2025-06-09
20b. https://www.apple.com/apple-intelligence/ — Siri AI photo search, iOS 27 beta footnotes (accessed 2026-11-03)
20c. https://www.apple.com/newsroom/2022/06/apple-unveils-new-ways-to-share-and-communicate-in-ios-16/ — Shared Library "up to six users", 2022-06-06
20d. https://blog.google/products-and-platforms/products/photos/ask-button-ask-photos-tips/ — Ask Photos, 2026-02-10
20e. https://blog.google/products-and-platforms/products/photos/halloween-tricks-2026/ — Ask Photos availability footnote, 2026-10-29
21. https://www.macrumors.com/how-to/ios-use-natural-language-search-photos/ — 2024-10-25
22. https://arctic-shift.photon-reddit.com/api/posts/search and /api/comments/search — every successful call listed in the §4 call log; original-pass parameters in the Part B headers
22a. https://www.reddit.com/r/Contractor/comments/1x4fpst/whats_worth_taking_pictures_of_before_starting_a/ — 2026-10-12 (content via arctic-shift)
22b. https://www.reddit.com/r/HVAC/comments/1x5hi5q/im_tired_of_the_bs/ — 2026-10-14 (content via arctic-shift)
22c. https://www.reddit.com/r/electricians/comments/1hodggq/companycam/ — 2024-12-28; /r/electricians/comments/1njcit9/ — 2025-09-17; /r/electricians/comments/1ai9ya1/ — 2024-02-03; /r/electricians/comments/1tihiv4/ — 2026-05-20 (content via arctic-shift)
23. https://www.prnewswire.com/news-releases/contractorhub-and-companycam-enter-integration-partnership-reimagining-the-potential-of-every-jobsite-photo-302841968.html — 2026-08-04 (headline via search)
24. https://www.prnewswire.com/news-releases/companycam-and-infinity-home-services-partner-to-bring-a-new-standard-of-productivity-and-transparency-to-job-sites-302877370.html — 2026-09-16 (headline via search)

Secondary
25. https://theroofingbrief.com/companycam-review/ — 2026-10-19 (pricing claims now corroborated by the pricing page's data attributes; 285k Instagram figure; 14-day trial)
26. https://www.mass.gov/news/contractor-vs-homeowner-how-to-keep-your-business-and-reputation-intact — snippet only (403 on fetch)
27. https://forums.mikeholt.com/threads/pictures-before-drywall.38544/ and /threads/photos.12360/ — snippets only (403 on WebFetch and curl)
28. https://www.census.gov/data/developers/data-sets/nonemp-api.2023.html — NES 2023 re-release note (snippet)
29. https://www.census.gov/newsroom/press-releases/2025/2023-county-business-patterns.html — CBP 2023 release date (snippet)
30. https://codes.findlaw.com/ca/code-of-civil-procedure/ccp-sect-337-15/ — CCP 337.15, "Current as of January 01, 2026"
31. https://codes.findlaw.com/il/chapter-735-civil-procedure/il-st-sect-735-5-13-214/ — 735 ILCS 5/13-214, "Current as of January 01, 2025"
32. https://en.wikipedia.org/wiki/National_Electrical_Contractors_Association — 119 chapters
33. verticals.md §2.1 (BLS QCEW 938,478; NSPE white paper; CompanyCam 170k press quote; siliconprairienews roadmap quote)

Blocked / failed (both passes): reddit.com and old.reddit.com (403/302, WebFetch refused), api.pullpush.io
(522), api.census.gov (requires key), buildertrend.com/pricing, /features, /newsroom (403), help.buildertrend.com
(connection reset), Capterra/SoftwareAdvice Buildertrend (403), GetApp (404), Google Play Buildertrend
(truncated), Wikipedia Buildertrend (404), necanet.org/about-us and /membership (403), necaconvention.org
(404), ecmag.com/about-us (404), support.apple.com iPhone guide "Search for photos" and "Shared Library"
(five fetches returned only the TOC), support.google.com/photos/answer/15057331 (404),
blog.google/products/photos/ask-photos-gemini/ (404), leginfo.legislature.ca.gov (403 ×2), ilga.gov (503 ×2),
statutes.capitol.texas.gov CP.16.htm (navigation only), law.justia.com TX/CA (403), levelset.com/payment-report/
and /research/ and /blog/construction-payment-report/ (404), rabbet.com (404 ×2), procore.com how-we-build-now
(404 ×2), thehartford.com construction-risk-management (503 ×2), servicetitan.com/titan-intelligence and
/features/mobile-app (404), youtube.com/@CompanyCam (no counts rendered), play.google.com CompanyCam id guess
(404), StatCan table search page (404), WebSearch (budget exhausted, 13/13 queries refused in the repair pass).

## Audit log

Repair pass 2026-11-03. Each auditor finding, what was done, and where in the file.

**Untagged numbers**
1. Method-note process counts ("9 queries", "roughly 25", "7 of 12 subreddits") — the original pass kept no log, so its counts are now marked [unknown — reported from memory]; the repair pass logged every arctic-shift call and the counts are tagged to the log table in §4; subreddit coverage is restated in the Part B header from that log.
2. "81.5% ... 96%" in the falsification stance — now tagged [estimated] with the exact ratios (95.9%, not 96%).
3. "140k+ ... under 5%" — tagged to About page and press page; "under 5%" corrected to "under 6% (3.8-5.9%)" so it agrees with the A2 table; the 170k figure is tagged to the 2024-02-28 press item via verticals.md.
4. "$129/$199 'Compare Plans' header stale" — the whole pricing paragraph was rewritten from the raw HTML, which carries the card prices as data attributes; the review's claim is now corroborated by a primary source and the figures are tagged to it.
5. "NSPE: repose + 3 years (verticals.md)" — now tagged [sourced: NSPE Document Retention Guidelines white paper, 2016-06-01, via verticals.md; not re-fetched].
6. "Shared Library ... up to six people" — now tagged [sourced: Apple newsroom 2022-06-06, "up to six users"].
7. Segment 2 header 11 hits vs 9 rows — header now reads "11 hits returned, 9 tabulated" with a note that the 2 unrecorded hits are [unknown] (re-run returned 422); the segment denominator is 9.
8. Segment 5 header 14 hits vs 10 rows — same treatment: "14 hits returned, 10 tabulated", 4 unrecorded hits [unknown], denominator 10.
9. 102 vs 82 vs 96 denominator — the "Where money changes hands" block now states the arithmetic once (102 hits, 96 tabulated/listed in the original eight segments; +60 from four new segments = 156 of 162) and every later count uses 156 posts / 264 comments; the unexplained "82" is gone.
10. "422 on 6 attempts / 14 attempts" in Unknowns — replaced by the logged counts in the §4 call log; the original pass's unlogged counts are marked as such.
11. "first 14 queries" / "CompanyCam 14 days [secondary]" — kept; the 14-day trial is now quoted from the review ("offers a 14-day free trial").

**Suspect claims**
1. UK 0-9 = 865,565 — recomputed: 865,550 (97.75%); corrected in A1, the sizing table and the numbers table, with the arithmetic shown.
2. "under 5%" vs 5.9% — corrected to "under 6%" everywhere; the A2 ceiling table now lists every base.
3. 1x4fpst comments — re-fetched all 22 this pass: one commenter names MagicPlan ("I use magicplan on my iPhone ... Photos and videos are free haha"); the two accusation remarks ("They are trying to sell something", "Nobody wants to buy your shitty app") are one author (same `author_fullname`), and a second commenter says "OP is pushing something" — the text now says "one commenter, in two separate remarks" plus "a second commenter suspects a pitch", and "nobody names a dedicated app" is withdrawn in favour of "the only dedicated app named is MagicPlan (once)". No comment names CompanyCam, Google Photos or Apple Photos (confirmed).
4. MCP "read-and-write" quote — replaced with the three verbatim sentences from the re-read page ("...supported CompanyCam updates can also become part of the routine" etc.).
5. Apple "search for just about anything by simply describing" — replaced with the verbatim "Natural language search gives users the ability to search for just about anything"; the draft's wording is explicitly withdrawn as a paraphrase.
6. 102/82/96 denominators and the comment-free money column — denominators fixed as in item 9 above; the money column's basis (first ~125 chars + scan for the original eight segments; full selftext for the new four) is stated in the Part B preamble; seven family-segment comment threads (178 comments, incl. 1tylhuc's single comment; 161t3a5 has none) and four trade threads (64 comments) were read this pass and reported in "What posters were told to pay".
7. CompanyCam pricing conflict — resolved from the raw HTML (card attributes $79/$63, $149/$119, $299/$249, +$34/$29; Compare Plans table 63/129/199 stale; JS fallbacks 79/63, 149/129, 249/199); A5's "3-5 person shop" range and the sizing-table entry recomputed from the card prices.
8. 814,557 (CBP 2023) vs 938,478 (QCEW 2024) — reconciliation paragraph added to A2 with both ceilings in the table; the QCEW figure is now also in the numbers table.
9. A4 staleness — added iOS 26 announcement (2025-06-09), Apple Intelligence page with Siri AI footnotes (iOS 27 beta, non-EU, "for a fee in the future"), Google Ask Photos (2026-02-10, 2026-10-29), Shared Library sourcing, and four pieces of primary contractor commentary on Google Photos/camera roll from r/electricians and r/HVAC. Apple's own guide article remained unreadable (five attempts) and this is stated.
10. Repose survey staleness — every state re-verified against statute text or a dated code copy; Texas HB 2024's 6-year residential track added; Florida's 2025 amendments (ch. 2025-81, 2025-153) noted with the 7-year figure unchanged; CA/IL from FindLaw copies dated 2026-01-01 / 2025-01-01 because the legislature sites returned 403/503.
11. 1xdy99s money column — reworded to "pays for a 2 TB plan (stated); no price given"; the money summary now separates "storage plan stated, no price" from priced items and no longer calls paid storage "near-universal".

**Broken/misquoted sources**
- MCP blog: quote fixed (above).
- Apple newsroom 2024-10: quote fixed (above).
- arctic-shift posts/search URLs: non-reproducibility acknowledged in the method note; this pass's successful calls are listed with parameters in the §4 call log, and 18 post IDs were independently confirmed by the auditor via /api/posts/ids.
- CPWR PDF: unchanged (auditor confirmed all figures).
- reddit.com permalinks: unchanged; stated as content-via-archive.

**Missing vs brief**
- A1 Canada: found and added (StatCan 33-10-1174-01 / 33-10-1175-01, June 2026, released 2026-08-14), with a note on why the first attempt hit the wrong table.
- A2 customer count: press page re-read (two 2025-2026 items quoted verbatim); SEC not applicable (private); PitchBook unreachable without search — stated.
- A2 competitors: Buildertrend ten attempts, all blocked — listed; ServiceTitan features index read ("equipment nameplate scanning"); YC directory read (Opusense AI P2025, Albiware S2022).
- A3 surveys: Levelset 2019 report found and quoted; Rabbet/Procore 404s listed; CompanyCam vendor anecdote ($70,000) added with its vendor tag; insurer requirement: Insureon quote added, Hartford/Next tried, contractor-specific requirement left [unknown].
- A3 forum threads: ContractorTalk thread fetched in full with curl and quoted verbatim by URL with its 2010 dates; Mike Holt still 403 (kept as secondary); r/electricians reached (four threads); r/Plumbing still 422 on every attempt.
- A3 repose currency: done (above).
- A4 Siri / Ask Photos / 2025-26 / contractor commentary: done (above).
- A5 NECA: four more URLs tried (all 403/404); Wikipedia chapter count and ProPublica 990 revenue added as what is findable; member count stays [unknown]. Supply houses: CompanyCam integrations page read (SRS Roof Hub only). Facebook/YouTube/trade shows: two YouTube fetches failed; stays [unknown] with tries listed.
- Part B subreddits: r/selfhosted, r/ios and r/electricians added; r/iphone, r/GriefSupport, r/declutter, r/ProfessionalOrganizers, r/Plumbing each attempted 2-3 times and never answered (422) — logged.
- Part B queries: "combine family photos" and "two icloud accounts" run; the five others attempted 2-3 times each, all 422 — logged.
- Part B "told to pay": seven family-segment comment threads read (1xdy99s, 1t2gshr, 1x382m7, 1xemakt, 1x2j95n, 1wnclv0; 161t3a5 has no archived comments) and reported.
- Part B Facebook: still not fetchable and no search budget; stated once in the Part B header, not silently dropped.
- Part B money denominator: fixed (156 posts / 264 comments, arithmetic shown in the money block).
- Output format: both tables kept in the requested shape; new segments use the same columns.

**Not done / still open after this pass** (all stated as [unknown] in §4): CompanyCam paying-company count; the 2026-09-17 price-rise date (secondary only); Buildertrend features; NECA member count; contractor-specific insurer photo requirements; a dispute survey quantifying losses for lack of photos; Facebook-group evidence; discovery-channel evidence; five requested subreddits and five requested queries that the archive never answered.
