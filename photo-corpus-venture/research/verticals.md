# Track F — Verticals with a compliance driver

Written 2026-11-03; repaired 2026-11-03 after hostile audit (see "Audit log" at the end). All web
access dates are 2026-11-03 unless stated. Source dates are the publication dates of the cited pages,
not today's date.

Method note: the shared WebSearch budget was already exhausted when this repair round started (every
WebSearch call returned "this turn's web search budget is used up" [sourced: WebSearch tool response,
2026-11-03]), so all new evidence in this version comes from direct WebFetch of primary pages whose
URLs could be named without a search engine (vendor pricing/press/blog/community pages, SEC 10-K filings,
statute mirrors, CFR, BLS data files, PubMed via the PubMed tool) plus local text extraction of
downloaded PDFs. Where only a search-engine snippet from the prior round existed and no URL survived,
the number is now tagged `[unknown]` rather than `[secondary]`. Pages that returned 403/404/429/503
are listed at the end of section 7. A bash `curl` probe of three blocked pages was denied by the
sandbox's bot-check policy and was not retried.

Thesis under test: photo corpora that already live OUTSIDE the consumer camera roll, where a
regulation or contract forces retention, and where "ask an AI about my photos" is unsolved.

---

## 1. Questions asked

Per vertical (construction, insurance claims, property inspection/management, clinical wound/derm,
law-enforcement body-worn camera, real estate, field service/utilities, auto dealers/body shops,
agriculture, legal e-discovery, education/childcare):

- Q1. Who owns the corpus today (vendor, pricing, funding/ARR if public)?
- Q2. What is the compliance/retention driver, and does it name photographs?
- Q3. Is natural-language / AI search over the photos solved? Evidence of demand or vendor roadmap?
- Q4. Where is the data NOT vendor-owned (still in a camera roll / iMessage with a business reason to index)?
- Q5. Pricing and distribution norms.
- Q6. Rank verticals on (a) corpus still in camera roll, (b) legal reason to keep, (c) someone already paying, (d) no incumbent AI search.
- Q7. Startups founded 2024-2026 doing "AI photo search for <vertical>": where has the land grab happened?

Falsification stance: for each vertical I looked first for evidence that (i) a vendor already owns the
corpus, (ii) no regulation actually names photos, and (iii) an incumbent already shipped AI search.
For the 2026 state of incumbents I read 2026-dated press, blog, community and SEC pages rather than
relying on the Nov-2025 article the first draft leaned on.

---

## 2. Findings per vertical

### 2.1 Construction / trades

**Q1 Corpus owners.**
- CompanyCam. Series C announced 2025-08-22, led by B Capital, amount undisclosed by the company
  [sourced: https://companycam.com/press, 2025-08-22]. PitchBook data reported by local press puts the
  round at $415M and valuation at $2B [sourced: https://siliconprairienews.com/2025/11/companycam-reaches-unicorn-status-with-2-billion-valuation-a-first-for-a-nebraska-startup/, 2025-11-22; secondary for the PitchBook figures].
  Customer scale: "over 170,000 contractors" as of 2024-02-28 [sourced: companycam.com/press,
  2024-02-28; 2.7 years old, likely understated today]; the latest press item (2026-03-02, Beam
  acquisition) says only "tens-of-thousands of construction and home service businesses" and gives no
  count [sourced: companycam.com/press, 2026-03-02]; "over 100,000 users" and "over 350 million photos"
  at Series B [sourced: companycam.com/press, 2021-10-26]. No 2025 or 2026 customer count was published
  on the press page; a current figure is [unknown].
  ARR: company said "north of $20 million" ARR in July 2022 [sourced: siliconprairienews, 2025-11-22
  quoting a 2022 statement]; a third-party estimate of $68M ARR for 2024 exists [secondary, estimated by
  getlatka.com, undated; not corroborated by the company].
  Pricing (annual billing): Core $63/mo (1 user), Crew $129/mo (3 users), Scale $199/mo (3 users),
  additional user $29/mo; AI credits 10 / 100 / unlimited by tier. The pricing FAQ says "AI features
  are included in Crew, Scale, and Enterprise" even though the Core column shows 10 AI credits — the
  page is internally inconsistent on whether Core has AI [sourced: https://companycam.com/pricing, accessed 2026-11-03].
  Retention: "As long as you're a CompanyCam customer, your photos stay in your account" [sourced:
  companycam.com/pricing FAQ, accessed 2026-11-03]; "Unlimited cloud storage means you can capture every
  aspect of your work—without worrying about a full camera roll" [sourced: https://companycam.com/features, accessed 2026-11-03; the pricing page does not mention storage].
- Procore (public). FY2025 10-K (filed 2026-02-24): "We generated revenue of $1.3 billion in 2025,
  $1.2 billion in 2024, and $1.0 billion in 2023"; 17,850 customers at 2025-12-31 (17,088 at 2024-12-31;
  company will stop disclosing this total in 2026); 2,710 customers above $100,000 ARR; the platform
  stores "photos of their active projects on an interactive map" and offers "agentic AI capabilities"
  [sourced: https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm, filed 2026-02-24].
  "Photo intelligence" (not "Photo AI") announced at Groundbreak 2025-10-15, described as analysing
  jobsite photos to summarise progress and surface safety insights inside Procore Assist; Agent Builder
  "open beta and available to all customers" [sourced: https://www.procore.com/press/procore-advances-the-future-of-construction-with-new-ai-innovations, 2025-10-15; paraphrase, not verbatim].
- OpenSpace. Pricing is quote-based: "OpenSpace pricing is based on your annual construction volume
  (ACV) and the subscription tier you choose"; tiers Core / Enterprise / Track add-on, no prices shown
  [sourced: https://www.openspace.ai/pricing/, accessed 2026-11-03]. $102M Series D on 2022-03-02 at a
  $902M valuation [secondary: https://www.teardown.ai/companies/openspace citing Bloomberg; openspace.ai/news does not state this]. User/footage counts are inconsistent even within the one secondary source:
  teardown.ai reports "275,000+ users and 43B+ sq ft" from a Nov-2025 release and also notes a Dec-2025
  company review claiming ~350,000 users and 50B+ sq ft, and calls both "marketing numbers rather than
  audited metrics" [secondary: teardown.ai, accessed 2026-11-03; range 275k-350k users, 43-50B sq ft;
  neither pair is on openspace.ai/news]. ARR: Latka estimate $56.7M for 2023 [secondary, uncorroborated].
  News page items run 2026-09-15 to 2026-10-28; "OpenSpace Expands Platform with AI Agents and Progress
  Tracking" 2026-09-30 describes "giving agents the visual and spatial context to assist with real work"
  and does not describe natural-language search over captures [sourced: https://www.openspace.ai/news/openspace-expands-platform-with-ai-agents-and-progress-tracking/, 2026-09-30].
- Buildots. $45M Series D, 2025-05-29, led by Qumra; total raised $166M [sourced: https://buildots.com/blog/buildots-raises-45m-in-series-d-funding/, 2025-05-29]. Pricing: [unknown] (buildots.com/pricing returned 404).
- Fieldwire. Basic $0 (5 users, 3 projects, 100 sheets); Pro $39, Business $64, Business Plus $89 per
  user/month billed annually; no AI/photo search described [sourced: https://www.fieldwire.com/pricing/, accessed 2026-11-03].
- HOVER. Construction tab: Starter = pay per project, no subscription; Pro $999/yr; Business $2,999/yr;
  Enterprise custom. Per-scan fees by product (Starter / Pro / Business): Exterior $59-$299 / $39-$279 /
  $79-$189; Roof $29-$69 / $9-$49 / $39 flat; Interior $29-$89 / $9-$69 / $49 flat; Blueprint Exterior
  $99-$299 / $79-$279 / $189 flat; Blueprint Roof $49-$149 / $29-$129 / $99 flat; Pro gets "$20 off every
  project". So the overall per-job range is $9 (Pro roof/interior floor) to $299 (Starter exterior
  ceiling), not "$9-$89" as the first draft said. The Pro plan on the Insurance tab (labelled "Adjuster
  Pro" in the auditor's fetch) offers "Access unlimited project history for reference and audits". No AI
  or search mentioned [sourced: https://hover.to/pricing, accessed 2026-11-03]. Funding: [unknown] — press
  page lists only 2025 product items [sourced: https://hover.to/press, items dated 2025-04].

**Q2 Compliance driver.** No statute found that requires contractors to retain photographs per se. Three
indirect drivers were checked:
- Statutes of repose (litigation defense). California CCP §337.15: action for latent construction
  deficiency barred more than 10 years after substantial completion [sourced: https://california.public.law/codes/ca_civ_proc_code_section_337.15, accessed 2026-11-03].
  Texas CPRC §16.009: claims up to 10 years after substantial completion, extendable to 12; a Texas
  construction lawyer recommends keeping project records including progress photos 13 years
  [sourced: https://www.ftworthconstruction.lawyer/how-long-to-keep-construction-documents/, 2025-10-23; law-firm blog, not statute text].
  NSPE guidance: preserve project documents "not less than the Statute of Repose ... plus three years"
  [sourced: NSPE Document Retention Guidelines white paper, PDF dated 2016-06-01].
  Effective horizon: 13-15 years [estimated: the two repose periods in this file (CA 10 yrs; TX 10 yrs
  extendable to 12) plus the NSPE 3-year buffer = 13 to 15 years; the first draft's "6-13" used a 6-year
  lower bound that no cited source supports and is withdrawn].
- Mechanics lien law (named in the brief). California Civil Code §8416 lists what a claim of mechanics
  lien must contain (demand, owner, kind of work, employer, site description, address, proof of service,
  statutory notice); photographs are not mentioned [sourced: https://california.public.law/codes/ca_civ_code_section_8416, accessed 2026-11-03]. Verdict: lien law creates deadlines and notices, not a photo-retention duty. Other states: [unknown] this round.
- Evidence rules (named in the brief). FRE 901(a): "the proponent must produce evidence sufficient to
  support a finding that the item is what the proponent claims it is"; 901(b)(1) testimony of a witness
  with knowledge; 901(b)(9) evidence that a process or system produces an accurate result; photographs
  are not named in Rule 901 [sourced: https://www.law.cornell.edu/rules/fre/rule_901, accessed 2026-11-03].
  FRE 1001(c): "A 'photograph' means a photographic image or its equivalent stored in any form";
  1001(d): "An 'original' of a photograph includes the negative or a print from it" [sourced: https://www.law.cornell.edu/rules/fre/rule_1001, accessed 2026-11-03]. Verdict: evidence rules make an
  original, authenticable photo valuable in a dispute (timestamp, location, chain of custody) but impose
  no retention period.
- Insurer requirements for contractors (named in the brief). No carrier document specifying photo
  documentation for contractor-submitted claims was retrieved [unknown]. Indirect evidence: HOVER's
  insurance page sells a "comprehensive claims package, including measurements, plans, and damage
  photos" that passes "directly into Xactimate, ClaimsConnect, and SettleAssist", and claims "5 of 5 top
  adjusting firms trust Hover" [sourced: https://hover.to/insurance, accessed 2026-11-03; vendor marketing].
Verdict: strong practical reason, weak mandate. The retention horizon (13-15 years, estimated above) is
far beyond what a camera roll or an iMessage thread survives.

**Q3 AI search solved? (2026 state, re-checked this round).** Not shipped as natural-language photo
search by the incumbents read, but CompanyCam has opened an MCP channel that changes the picture.
- CompanyCam. The features page still has no occurrence of the word "search"; AI is described as
  "Create reports, checklists, captions, and updates without typing a word" [sourced: companycam.com/features, accessed 2026-11-03].
  The help center has an "AI Tools" section (9 articles) but no release-notes feed [sourced: https://help.companycam.com/, accessed 2026-11-03].
  CompanyCam MCP Server: "CompanyCam's MCP Server can give those conversations access to supported
  information from your CompanyCam account"; named assistants are ChatGPT and Claude; "With
  read-and-write access, supported CompanyCam updates can also become part of the routine"; "currently
  in Beta, and supported capabilities can change"; the post does not describe photo search, only
  reviewing "available photo documentation" [sourced: https://companycam.com/resources/blog/ways-contractors-use-companycam-mcp-ai-daily-tasks, 2026-09-09].
  A follow-up post says an MCP connection can "pull context from your CRM or CompanyCam" and that AI
  answers can reference "project and customer data, job photos, timesheets" [sourced: https://companycam.com/resources/blog/ai-strategy-business-data, 2026-10-01].
  The public API exposes list-photos endpoints (`/photos`, `/projects/{id}/photos`) and tags; the API
  docs do not mention an MCP server [sourced: https://companycam.readme.io/llms.txt, accessed 2026-11-03].
  Demand evidence from CompanyCam's own community (Product Wishlist forum): "Description Search in
  Global Search" (2026-10-22): "If i want to find a slab photo from the color name i am unable to. This
  should definitely be a part of the global search." — no staff reply [sourced: https://community.companycam.com/threads/description-search-in-global-search.331/, 2026-10-22];
  "Search by Customer" (~2026-10-28): "search or filter projects by customer directly from the main page"
  [sourced: https://community.companycam.com/threads/search-by-customer.340/, dated "Wednesday" on a page read 2026-11-03];
  "Date Added - Camera Roll" (~2026-11-01): user wants the upload flow to "show dates while browsing the
  camera roll"; staff reply confirms camera-roll import exists and "Uploaded photos keep their original
  capture date" [sourced: https://community.companycam.com/threads/date-added-camera-roll.345/, dated "Sunday" on a page read 2026-11-03].
  Stated roadmap (unchanged): "300% growth in AI actions" and plans for "enhanced photo tagging and
  search" [sourced: siliconprairienews, 2025-11-22].
  Verdict for CompanyCam, 2026-11-03: no natural-language photo search shipped on public pages; users
  are still asking for description search; but any Claude/ChatGPT user can already attach a CompanyCam
  account via MCP (beta), which is the seed's "BYO-AI" wedge delivered by the incumbent.
- Procore. FY2025 10-K describes photos-on-a-map and agentic AI, not photo search [sourced: pcor-20251231.htm, filed 2026-02-24].
  2026-10-21 "Voice-First AI Mobile App": crews "can ask questions about project drawings,
  specifications, RFIs, submittals, daily logs" and get spoken answers; AI glasses (future) would
  "capture first-person photos and access information about those images". Photos are not in the list of
  things the shipped app answers about [sourced: https://www.procore.com/press/procore-launches-voice-first-ai-mobile-app-built-for-the-jobsite, 2026-10-21].
  A Procore community thread asking for text-in-photo search surfaced in the prior round's search; it is
  undated in this file and the page returned 503 on both fetch attempts [secondary: https://community.procore.com/s/question/0D58V00007oxaEESAY; content not verified].
- OpenSpace: "AI Agents" (2026-09-30) and "Live Location" (2026-09-17) headlines; no conversational
  "ask" over photos described on the pages read [sourced: openspace.ai/news, 2026-09-17 and 2026-09-30].
Verdict: window is open for photo-level NL retrieval, but the incumbent's MCP beta means a third party
can already be the "AI on top" of a CompanyCam corpus without owning the corpus — which is exactly the
position a seed company would otherwise try to build.

**Q4 Not vendor-owned.** Fraction of US contractors using CompanyCam vs. camera roll: still [unknown]
as a measured figure, but an upper bound is now possible.
- Denominator: BLS QCEW 2024 annual averages, private ownership: NAICS 23 (Construction) 938,478
  establishments, 8,135,442 employees; NAICS 238 (Specialty trade contractors) 588,440 establishments,
  5,151,234 employees [sourced: https://data.bls.gov/cew/data/api/2024/a/industry/23.csv and .../238.csv, 2024 annual, accessed 2026-11-03].
- Upper bound on CompanyCam penetration: 18% of all US construction establishments [estimated: 170,000
  "contractors" (Feb 2024, company figure, includes non-US and may count users not firms) / 938,478 US
  private construction establishments (QCEW 2024) = 0.181]; or 29% of specialty-trade establishments
  [estimated: 170,000 / 588,440 = 0.289]. Both are ceilings: the numerator is global and stale, the
  denominator excludes sole proprietors with no employees. The true share is lower and [unknown].
- Qualitative evidence that the long tail is in camera rolls and chats: CompanyCam's own 2026 blog:
  "If those photos live in individual camera rolls or chats that only certain people can access";
  "At the time, the pictures were spread across individual camera rolls."; "His team sent photos into a
  WhatsApp group for each job" [sourced: https://companycam.com/resources/blog/find-job-photos, 2026-09-14; vendor-authored, no statistics].
  A competitor blog: "A photo buried in a text thread or personal gallery has no business value when you
  need it under pressure"; photos kept in "personal camera rolls, text threads, or email attachments"
  "may be inaccessible when disputes arise" [sourced: https://www.terial.com/blog-posts/job-site-photo-documentation-workflow, 2026-08-18; vendor-authored; no statistics on page].
  A CompanyCam blog cites a JBKnowledge ConTech figure of ">90% of construction firms use smartphones on
  job sites" [secondary; report itself not retrieved].

**Q5 Pricing/distribution.** Per-company tiers with included seats ($63-$199/mo) or per-user ($39-$89)
[sourced above]. Distribution: self-serve web signup with free trial on the pricing page (CompanyCam,
Fieldwire, HOVER "Try for free") [sourced: the three pricing pages, accessed 2026-11-03], plus integrations
(Jobber, Roofr, DroneDeploy partnerships on CompanyCam press page, 2021-2022). Trade-association
channels: [unknown] this round (no association page fetched for construction).

### 2.2 Insurance claims (property and auto)

**Q1 Corpus owners.** Verisk/Xactimate (property), CCC (auto), Tractable, Snapsheet, CoreLogic/Cotality, HOVER insurance tier.
- Verisk XactAI: "Introductory pricing: $29 per user/month billed annually, or $39 month to month";
  photo labeling = "images described automatically" inside Xactimate; no photo search listed
  [sourced: https://www.xactware.com/home/xactai.html, accessed 2026-11-03]. Launch date: reported as
  Oct 2025 in the prior round's search snippet; the iireporter article body was empty on fetch, the Verisk
  newsroom pages returned no items, and xactware.com/news redirects to verisk.com/en-us/news (empty on
  fetch) — date uncorroborated [secondary: iireporter.com snippet; treat as unverified].
- CCC: "800M vehicle damage photos", "17M+ Claims Processed Annually", "30,500+ Collision Repairers"
  [sourced: https://www.cccis.com/, accessed 2026-11-03].
- Tractable: $65M Series E led by SoftBank Vision Fund 2, 2023-07-18; "more than $7 billion in
  annualized auto and home repairs"; "over 20" insurers/automakers [sourced: https://www.insightpartners.com/ideas/tractable-ai-raises-65m-..., 2023-07-18]. ARR estimates ($79.4M, 2024) are third-party [secondary: getlatka]. Pricing: [unknown] (enterprise).
- Snapsheet: "Trusted by 170+ customers & investors, including 16 of the top 20 P&C carriers"; AI agents
  configurable "at the prompt-level entirely in natural language"; claim files "quickly searchable"
  (documents, notes, communications — photos not mentioned); named a Luminary in Celent's 2026 NA P&C
  Claims Systems report [sourced: https://www.snapsheetclaims.com/, accessed 2026-11-03]. Total funding
  and revenue: [unknown] — the first draft's "$103M-$107M" and "aggregators disagree by 5x" came from
  search snippets with no retained URL and are withdrawn. Pricing: [unknown].
- CoreLogic, now Cotality: insurance products Workspace, UnderwritingCenter, Weather Insight, Dispatch,
  Scope; marketing on "Agentic AI"; no photo search described; pricing [unknown]
  [sourced: https://www.cotality.com/insurance, accessed 2026-11-03; cotality.com/insurance/claims returned 404].

**Q2 Compliance driver.** NAIC Market Conduct Record Retention and Production Model Regulation (MO-910,
2004). Section 6.A: "A claim file and accompanying records shall be maintained for the calendar year in
which the claim is closed plus three (3) years" — the clock starts at claim closure, not the current
year, so long-tail claims carry a materially longer horizon; claim files must be "maintained so as to
show clearly the inception, handling and disposition of each claim"; drafting note that some states use
five years. (The "current year plus three (3) years" language the first draft quoted is the Section 4/5
policy/underwriting/producer-records rule, not the claim-file rule.) Photographs are absent from the
Section 6.A(1) item list; they fall under "accompanying records" [sourced: https://content.naic.org/sites/default/files/model-law-910.pdf, 2004, text extracted locally and re-verified by auditor]. State rules vary (3-5 years) [secondary].

**Q3 AI search solved?** Photo understanding is the most advanced here: Tractable and CCC do
photo-to-estimate; XactAI auto-labels photos; Snapsheet markets prompt-configured agents. Natural-language
retrieval across a carrier's historical photo corpus is not advertised on the pages read [sourced:
xactware XactAI page; cccis.com; snapsheetclaims.com, accessed 2026-11-03]. The corpus sits inside
carrier/vendor systems, so a third party cannot index it without a vendor deal.

**Q4 Not vendor-owned.** Denominator: BLS counts 389,700 "claims adjusters, appraisers, examiners, and
investigators" jobs in 2025 (median pay $78,020, May 2025); for the auto-damage appraiser subset
(~13,500 jobs) 2% are self-employed [sourced: https://www.bls.gov/ooh/business-and-financial/claims-adjusters-appraisers-examiners-and-investigators.htm, 2025 data, accessed 2026-11-03]. The number of
independent (non-staff) adjusters is [unknown]: naiia.com sits behind a bot-check and state licensee
counts were not reachable without search. Whether adjusters keep personal copies of claim photos is
[unknown]. Public adjusters: NAIC draft model (2024) says records "maintained for at least five (5)
years after the termination of the transaction" [secondary: NAIC public adjuster draft 2024-06-18 via prior-round search; not re-fetched].

**Q5 Pricing/distribution.** Per-user/month ($29-$39 XactAI add-on), per-job (HOVER $9-$299 by tier and
scan type), enterprise contracts with carriers. Distribution is carrier-driven; adjusters use what the
carrier mandates; HOVER sells into adjusting firms and integrates into Xactimate/ClaimsConnect/
SettleAssist [sourced: hover.to/insurance, accessed 2026-11-03].

### 2.3 Property management / landlords / home inspection

**Q1 Corpus owners.**
- HappyCo: quote-only pricing, "THE COMPLETE AI-LED PLATFORM", "Reporting & AI Insights"; no photo
  search [sourced: https://happy.co/pricing, accessed 2026-11-03]; "HappyCo does not publish pricing, so
  pricing is quote-based" [sourced: https://www.buildium.com/blog/best-property-management-inspection-software/, 2026-08-18].
- zInspector: 15-day free trial; prices not on public page [sourced: https://www.zinspector.com/pricing,
  accessed 2026-11-03]; "zInspector prices per unit, so the cost depends on your portfolio size"
  [sourced: buildium.com blog, 2026-08-18]. The first draft's "$60/mo for 100 units" is not on the
  Buildium page as fetched and is withdrawn: [unknown].
- Spectora (home inspectors): $109/mo or $1,090/yr; +$99/mo per additional inspector; Advanced add-on
  $4/inspection [sourced: https://www.spectora.com/pricing/, accessed 2026-11-03]; "used by over 12,000
  inspectors"; Match (early access): "Speak your observations, snap photos as you go." and "Match pairs
  what you say with comments you've already reviewed and approved in your template."; "Inspectors in
  early access are seeing up to 25% time savings per inspection" [sourced: https://www.spectora.com/, accessed 2026-11-03; quotes now verified verbatim on the homepage].
- Inspect Point (fire/life-safety inspections, named in the brief): inspectpoint.com returned HTTP 429
  on three attempts (home, /pricing, /features); pricing, funding and features [unknown].

**Q2 Compliance driver — the strongest explicit photo mandate found in this track.**
California Civil Code §1950.5, as amended by AB 2801 (2023-2024 session), chaptered 2024-09-19 as
Chapter 280, Statutes of 2024 [sourced: https://calmatters.digitaldemocracy.org/bills/ca_202320240ab2801, accessed 2026-11-03]:
- (g)(1): "For tenancies that begin on or after July 1, 2025, the landlord shall take photographs of the
  unit immediately before, or at the inception of, the tenancy."
- (g)(2): "Beginning April 1, 2025, the landlord shall take photographs of the unit ... prior to any
  repairs or cleanings for which the landlord will make a deduction" and "within a reasonable time after
  such repairs or cleanings are completed."
- (h)(2)(D): landlord "shall provide photographs taken pursuant to subdivision (g)" with the itemized
  statement, deliverable "by mail, email, computer flash drive" [sourced: https://california.public.law/codes/ca_civ_code_section_1950.5, accessed 2026-11-03].
This is a statute that names photographs, sets a capture event, and forces delivery. Other states:
[unknown] this round. Home-inspector record retention: Texas 22 TAC §535.222 covers report content, not
retention years [sourced: https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-535-222]; other states [unknown].

**Q3 AI search solved?** No AI photo search found at HappyCo, zInspector, or Spectora pages read. Spectora's
AI is text-assist and voice capture.

**Q4 Not vendor-owned.** Small landlords (the long tail subject to §1950.5) have no mandated tool; the
natural capture device is a phone. Denominator attempts: the Census API (ACS B25003 renter-occupied
units for California) requires an API key, and both QuickFacts URLs returned 403, so the count of CA
rental units / landlords is [unknown]; the California Apartment Association homepage states no member or
unit count [sourced: https://caanet.org/, accessed 2026-11-03]. Fraction of CA landlords using a PM app:
[unknown]. The statute creates a per-tenancy before/after pair that must be retrievable years later at
deposit disputes.

**Q5 Pricing/distribution.** Per-unit/month for PM software (quote-based), per-inspector/month for
inspectors ($109). Distribution evidence: NARPM (property managers' association) lists "2026 Premier
Partners" Enterprise Bank & Trust, LendingOne, PetScreening and Yardi, plus ~22 partner logos including
Buildium, AppFolio, Rent Manager, Propertyware, Apartments.com and Doorloop, and runs a "Find Affiliate
Members" vendor directory [sourced: https://www.narpm.org/, accessed 2026-11-03] — i.e., association
sponsorship is an established channel for PM software. Landlord-association channel for small
landlords (CAA): no vendor program visible on the homepage [sourced: caanet.org, accessed 2026-11-03].

### 2.4 Clinical: wound care and dermatology

**Q1 Corpus owners.**
- Swift Medical: $8M round 2024-01-29 (BDC Women in Tech fund, Virgo); "over 4,000 healthcare facilities";
  "over 20,000 clinical users"; "over 20 million wound images" [sourced: https://hitconsultant.net/2024/01/29/swift-medical-secures-8m-to-power-ai-driven-wound-care/, 2024-01-29; trade press quoting the release].
- Net Health Tissue Analytics: "15M+ Images Analyzed"; one home-health customer (attributed to Kaiser
  Permanente) captures 250,000-300,000 wound images per month; no pricing; no search feature described
  [sourced: https://www.nethealth.com/wound-care/tissue-analytics/, accessed 2026-11-03]. Pricing: [unknown].
- DermEngine: lists "Advanced Visual Image Search", mole-matching, Evolution Tracker; HIPAA/SOC2/GDPR;
  quote pricing [sourced: https://www.dermengine.com/, accessed 2026-11-03].
- Miiskin Pro: "$10 usage per consultation request", HIPAA badge; no AI search [sourced: https://miiskin.com/pro/, accessed 2026-11-03].
- Wound-EMR price range: [unknown] — the first draft's "$400-$1,200/mo" came from a competitor blog with
  no retained URL and is withdrawn.

**Q2 Compliance driver.** Two layers, neither photo-specific:
- HIPAA 45 CFR §164.530(j)(2): covered entity "must retain the documentation required by paragraph
  (j)(1) ... for six years from the date of its creation or the date when it last was in effect,
  whichever is later" [sourced: https://www.law.cornell.edu/cfr/text/45/164.530, accessed 2026-11-03].
  This is the Privacy Rule's documentation requirement (policies, notices, complaints), not a
  medical-record or clinical-photo retention rule. HHS FAQ 580 (which says HIPAA itself sets no medical
  record retention period) returned 403 again this round.
- State medical-record retention (the actual driver). California Health & Safety Code §123145: licensed
  providers that cease operation must "preserve records for a minimum of seven years following discharge
  of the patient" (minors: at least one year past age 18, never less than seven years) [sourced: https://california.public.law/codes/ca_health_and_safety_code_section_123145, accessed 2026-11-03; note the
  section's trigger is cessation of operation]. Texas 22 TAC §165.1 (the medical-board record rule) shows
  as "Repealed ... eff. 1/9/2025" on the Cornell mirror; its successor text was not retrieved [sourced:
  https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-165-1, accessed 2026-11-03] — Texas period [unknown].
  Whether clinical photographs are part of the "record" is not stated in either text [partial].
Clinical photos are PHI, so any third-party index needs a BAA.

**Q3 AI search solved?** Partially: DermEngine advertises visual image search; wound vendors advertise
measurement and ambient documentation, not retrieval.

**Q4 Not vendor-owned — now evidenced.** According to PubMed (articles retrieved via the PubMed tool,
2026-11-03):
- US dermatologists (n=153, surveyed May-Aug 2015): 61.8% use medical photography every day; "Nearly
  half (46%) use smartphone cameras"; "Emailing and texting photographs with patients or colleagues are
  common (69.1%)"; "Only 23.7% adhere to a photography protocol" [sourced: Milam & Leger, JEADV 2018, [DOI](https://doi.org/10.1111/jdv.14839), published 2018-03-06].
- French plastic surgeons (n=86): "Photographs taken were stored in their smartphones (50%) or synced
  with virtual storage (25.6%)" [sourced: Djian et al., Ann Chir Plast Esthet 2018, [DOI](https://doi.org/10.1016/j.anplas.2018.06.005), 2018-07-09].
- Indian dermatologists (n=119): "Most respondents used personal smartphone (72.9%, 86/118) for imaging";
  shared "most commonly in professional WhatsApp groups (86.3%, 101/117)" [sourced: Janagond & Inamadar, Indian Dermatol Online J 2021, [DOI](https://doi.org/10.4103/idoj.IDOJ_99_21), 2021-07-14].
- Israeli plastic surgeons (n=74): "93% of them stated that they use smartphone photography in their
  daily practice" [sourced: Yanko et al., Adv Skin Wound Care 2025, [DOI](https://doi.org/10.1097/ASW.0000000000000342), 2025-09-02].
- Mayo Clinic's rationale for its own capture app: clinical photos "are often taken using the native
  camera app on the device and transmitted using relatively insecure methods (eg, SMS text message and
  email) that do not preserve images as part of the electronic medical records" [sourced: Wyatt et al., J Med Internet Res 2020, [DOI](https://doi.org/10.2196/14412), 2020-05-12].
Verdict: the personal-phone corpus is real and documented (46-73% smartphone capture across surveys;
50% stored on the phone in one), but it is PHI and the fix institutions choose is an EHR-integrated
capture app, not a retrospective index of personal camera rolls.

**Q5 Pricing/distribution.** Enterprise sales to health systems; per-consult for teledermatology
($10/consult Miiskin). Distribution channels beyond direct sales: [unknown].

### 2.5 Law enforcement body-worn camera

**Q1.** Axon (public). FY2025 10-K (filed 2026-02-25): net sales $2,779.5M in 2025 vs $2,082.5M in 2024;
Software and Services segment $1,202.7M in 2025 vs $861.2M in 2024; annual recurring revenue "totaled
$1.3 billion" at 2025-12-31; Axon Evidence is "a secure, cloud-based platform that enables public safety
to efficiently store, manage and share critical evidence"; Axon Assistant is listed among software
offerings; "We offer systems and tools that incorporate AI technologies, including generative AI"
[sourced: https://www.sec.gov/Archives/edgar/data/1069183/000162828026011360/axon-20251231.htm, filed 2026-02-25].
Product page: "Store without limits"; "With tools like Auto-Tagging, files arrive organized, searchable"
[sourced: https://www.axon.com/products/axon-evidence, accessed 2026-11-03]. List pricing: [unknown] (bundled agency contracts; not in the 10-K).
**Q2.** Michigan MCL 780.316 (eff. 2018-01-08): retain evidentiary recordings "not less than 30 days";
complaint-related "not less than 3 years"; ongoing investigations until completion
[sourced: https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-780-316]. California: 60 days
non-evidentiary, 2 years evidentiary (Penal Code §832.18); Minnesota: 90 days, 1 year for use-of-force
(Minn. Stat. §13.825) [sourced: https://www.axon.com/resources/body-camera-laws-by-state, 2024-10-16;
vendor summary of statutes; the page does not cover Texas]. Texas Occ. Code §1701.655 minimum retention:
[unknown] — statutes.capitol.texas.gov (two URL forms), texas.public.law and codes.findlaw.com (two URL
forms) all returned navigation/index pages without section text; the first draft's "90 days" is withdrawn.
**Q3.** Closed market; Axon already ships AI tagging/search and is the system of record. Not open to a startup.
**Q4.** None in camera roll by policy.
**Q5.** Agency contracts, multi-year bundles; ARR $1.3B (Axon 10-K, above).

### 2.6 Real estate (listing/appraisal)

**Q1.** Matterport (CoStar, public). CoStar FY2025 10-K (filed 2026-02-26): total revenue $3,247M in
2025 vs $2,736M in 2024; Matterport acquired February 2025; "$147 million of revenue from the Matterport
Acquisition" contributed to 2025 Other Commercial Real Estate revenue; services "sold on a subscription
basis"; marketed with "AI powered property insights" [sourced: https://www.sec.gov/Archives/edgar/data/1057352/000105735226000020/csgp-20251231.htm, filed 2026-02-26]. List pricing: [unknown] —
matterport.com/pricing (nav-only render), /plans (404) and two support-article URLs (404) failed.
**Q2.** USPAP Record Keeping Rule (appraiser workfile retention): [unknown] — appraisalfoundation.org
home and /pages/uspap render only store/FAQ content and identify the 2024 edition as current; the rule
text is behind the paid document; no state-board mirror could be located without search. No retention
driver for listing photos found.
**Q3-Q5.** [unknown]. Low priority: listing photos are marketing assets with short useful life.

### 2.7 Field service / utilities

**Q1.** ServiceTitan (public). FY2026 10-K (year ended 2026-01-31, filed 2026-03-25): "Our revenue was
$961.0 million and $771.9 million for fiscal 2026 and fiscal 2025"; approximately 10,800 active customers
"representing over 97% of our annualized billings"; Field Pro "pairs an AI-powered field technician
coaching solution with AI-powered pre-job briefs and equipment recognition"; no photo search described
[sourced: https://www.sec.gov/Archives/edgar/data/1638826/000163882626000028/ttan-20260131.htm, filed 2026-03-25].
Pricing page: per-technician, plans Starter / Essentials / The Works, no prices shown [sourced: https://www.servicetitan.com/pricing, accessed 2026-11-03].
**Q2.** Gas pipeline: 49 CFR §192.491 — maps/records of cathodically protected piping "retained for as
long as the pipeline remains in service"; test/survey/inspection records "at least 5 years"
[sourced: https://www.law.cornell.edu/cfr/text/49/192.491, accessed 2026-11-03]. Photographs are not
named. Electric (NERC/FERC) and water (state PUC) inspection-record rules: [unknown] — not researched
this round.
**Q3-Q4.** [unknown]. Large utilities use enterprise asset systems; small contractors use
ServiceTitan/Jobber/camera roll (not quantified).
**Q5.** Per-technician SaaS (ServiceTitan); channels beyond direct sales [unknown].

### 2.8 Automotive dealers / body shops

**Q1.** Body shops: CCC, 800M vehicle damage photos, 30,500+ collision repairers [sourced: cccis.com,
2026-11-03]. Dealers (reconditioning/inspection photos): Rapid Recon claims "more than 5,192 dealerships
and more than 249,941 users within those dealerships actively engage with Rapid Recon daily"; no photo
AI or search described [sourced: https://www.rapidrecon.com/, accessed 2026-11-03].
**Q2.** Insurer DRP contracts requiring photo documentation for body shops: [unknown] — no DRP contract
text retrieved. Dealer-side retention driver for recon photos: [unknown] (none found; FTC Used Car Rule
not researched).
**Q3.** Photo-based AI estimating is mature (CCC, Tractable). Land already grabbed on the body-shop side.
**Q5.** Enterprise/per-shop SaaS; channels [unknown].

### 2.9 Agriculture (crop insurance loss adjustment)

**Q1.** No vendor identified this round [unknown].
**Q2.** FCIC loss-adjustment handbooks are the retention/documentation driver. The general Loss Adjustment
Manual (LAM) could not be located on RMA's redesigned site (the "Crop Loss Adjustment Standards" listing
shows 412 handbooks; the LAM is not among the first page) [sourced: https://www.rma.usda.gov/policy-procedure/crop-loss-adjustment-standards, accessed 2026-11-03]. One crop-specific handbook was read:
Grape Loss Adjustment Standards Handbook FCIC-25230, issued 2026-09-30 for 2027 and succeeding crop
years; its only photo language is "Attach a sketch map or aerial photograph to identify the total unit"
and "Indicate on the aerial photograph or sketch map, the disposition of acreage destroyed" — no
requirement to photograph damage [sourced: https://www.rma.usda.gov/sites/default/files/2026-09/2027%2025230%20Grape%20Loss%20Adjustment%20Standards%20Handbook.pdf, 2026-09-30, text extracted locally].
Verdict (one handbook): weak photo driver. The LAM itself: [unknown].
**Q3-Q5.** [unknown].

### 2.10 Legal e-discovery

**Q1.** Relativity aiR: AI review, collections including "mobile collections"; no image/visual search
named on the product page; pricing by committed data volume, "no per-user fees" [sourced: https://www.relativity.com/data-solutions/air/ and https://www.relativity.com/pricing/, accessed 2026-11-03].
**Q2.** Preservation duty is matter-specific (legal hold), not a standing retention rule. FRE 901/1001
(section 2.1) govern authentication of photographs once collected.
**Q3.** Image search over mobile collections: not evidenced on the pages read [partial].
Observation: this is where consumer camera rolls get collected wholesale, but per matter, by vendors.

### 2.11 Education / childcare

**Q1.** Brightwheel: "160,000+ reviews", "thousands of" programs, quote-based pricing, "AI assistant"
for support [sourced: https://mybrightwheel.com/, accessed 2026-11-03]. Procare: "Request Pricing" page,
"one low monthly price", no amount, no photo mention [sourced: https://www.procaresoftware.com/pricing/, accessed 2026-11-03]. Lillio (formerly HiMama): "Reviewed by 35,000+ happy customers"; "Trusted by thousands of
childcare providers"; "2.1B moments shared with families"; pricing page 404 [sourced: https://www.lillio.com/, accessed 2026-11-03].
**Q2.** No retention rule for childcare photos found; the rules surfaced are disclosure/consent rules
[secondary: childcarecomp.com via prior-round search]. Photo storage limits on free tiers are a vendor policy, not law.
**Q3.** Not evidenced.
Verdict: no compliance driver; drop.

### 2.12 Startups founded 2024-2026 ("AI photo search for <vertical>")

Construction (the only vertical where the prior round's searches ran):
- Klutch (Seattle): product page says "Query any document and get instant answers", receipts logged by
  "texting photos", warranty flows where homeowners "share photos/videos for fast assessment" — an
  agent/document product, not photo-corpus search [sourced: https://www.klutch.ai/, accessed 2026-11-03].
  $8M seed (2025) [secondary: geekwire snippet; page 403 on two attempts; unverified].
- OnSite (Singapore): S$1.7M seed, article 2026-04-09; messaging platform that organizes "voice notes,
  photographs, and text" by project/location/timeline [sourced: https://itbrief.asia/story/onsite-raises-s-1-7-million-to-build-ai-for-construction, 2026-04-09].
- BuildPass (Australia/US): site describes a GC platform with "BuildPass Agent" that can search records
  and build reports with user approval; "more than 1,000 general contractors"; "80,000+ workers across US
  jobsites"; no photo/computer-vision language on the homepage [sourced: https://www.buildpass.ai/, accessed 2026-11-03]. $7.5M seed Oct 2024 [secondary: businessnewsaustralia snippet; page 403; unverified].
- Hardline: $2M pre-seed May 2026, voice-to-project-records ("VoiceOps") [sourced: https://www.landbase.com/blog/ai-construction-startups-hiring-fastest, accessed 2026-11-03; secondary list].
- Q4 2025 contech funding list (PermitFlow $54M, Attentive.AI $30.5M, Unlimited $12M, ConCntric $10M,
  Kojo $10M, Planera $8M): none is a photo-search product [sourced: https://www.constructiondive.com/news/construction-tech-funding-Q4-2025/808986/, published 2026-01-07].
Insurance claims, property management, clinical, inspection, field service, legal, childcare, auto,
agriculture: [unknown] — no search was possible this round, and no startup directory could be read
without one. This is an absence of research, not evidence of absence.
Pattern (construction only): new money goes to capture-side assistants (voice, messaging ingestion),
agents over documents, and drawings/takeoff computer vision. No funded startup found whose product is
"index the existing photo corpus and let you ask questions" for contractors. The incumbent's own move
(CompanyCam MCP beta, 2026-09-09) is the closest thing to that product.

---

## 3. Seed assumptions tested

| Assumption | Status | Evidence |
|---|---|---|
| T1. Vertical photo corpora already live outside the camera roll | partial | True where a vendor exists (CompanyCam "170,000 contractors" as of Feb 2024, likely understated; CCC 800M photos; Swift 20M images; Axon). Long tail: CompanyCam penetration is at most 18% of US construction establishments [estimated, section 2.1 Q4]; clinician surveys show 46-73% smartphone capture and 50% phone-only storage in one cohort [sourced: PubMed, section 2.4]. |
| T2. A regulation/contract forces retention of those photos | partial | Only one statute found that names photographs: CA Civ §1950.5(g)-(h) (AB 2801, 2024). Everything else is indirect: statutes of repose (10 yrs CA/TX), NAIC claim-closure +3 yrs, state medical-record rules (CA 7 yrs), HIPAA 6-yr documentation (not photo-specific), PHMSA life-of-pipeline, BWC 30 days-3 yrs, FRE 901/1001 (authentication, no period), lien law (no photo content). |
| T3. AI search over those corpora is unsolved | partial | No shipped NL photo search found at CompanyCam (features page, community requests dated 2026-10-22 to 2026-11-01), Procore (10-K; 2026-10-21 voice app answers about docs, not photos), Xactimate, HappyCo, Spectora, ServiceTitan as of pages read 2026-11-03. But CompanyCam MCP Server (beta, 2026-09-09) already exposes account data to ChatGPT/Claude; Procore Photo intelligence (2025-10-15); XactAI auto-labels; DermEngine visual search; Axon auto-tagging. Window is open at the photo-retrieval layer only. |
| v0 A3. A segment exists for whom indexed photos are an acute, paid pain | holds (for verticals) | Contractors pay $63-$199/mo for photo documentation (CompanyCam pricing 2026-11-03); inspectors $109/mo (Spectora); adjusters $29-$39/user/mo for XactAI; users publicly request description search (CompanyCam community, 2026-10-22). Payment is for capture/organize/report, not yet for search. |
| v0 A4. Incumbents will not ship the obvious feature | broken (for verticals) | CompanyCam shipped an MCP beta (2026-09-09) and states a tagging/search roadmap (2025-11-22); Procore shipped Photo intelligence (2025-10-15) and a voice Q&A app (2026-10-21). Timing of full NL photo search: [unknown] — no method yields a date; the first draft's "12-24 months" is withdrawn. |
| v0 A5. Unit economics clear the price point | unknown | Not tested in this track; vertical price points are 6-21x consumer storage tiers [estimated: CompanyCam Core $63/mo divided by iCloud+ 2 TB $9.99/mo = 6.3x and by iCloud+ 200 GB $2.99/mo = 21x; iCloud prices sourced: https://support.apple.com/en-us/108047, accessed 2026-11-03], which relaxes the constraint. |
| v0 A6. Assistants will accept a private corpus as a tool | partial (new) | CompanyCam's MCP post names ChatGPT and Claude as the assistants it connects to [sourced: companycam.com blog, 2026-09-09] — evidence that the MCP route works for a vertical vendor, and that the vendor rather than a third party is the one holding it. |

---

## 4. Numbers table

| Number | Context | Tag |
|---|---|---|
| 0 | WebSearch calls available in this repair round | [sourced: WebSearch tool response "budget is used up", 2026-11-03] |
| $63 / $129 / $199 per month | CompanyCam Core/Crew/Scale, annual billing | [sourced: companycam.com/pricing, 2026-11-03] |
| $29/user/mo | CompanyCam additional user | [sourced: companycam.com/pricing, 2026-11-03] |
| 10 / 100 / unlimited | CompanyCam AI credits by tier | [sourced: companycam.com/pricing, 2026-11-03] |
| 170,000 contractors | CompanyCam customers, as of Feb 2024 (stale; likely understated) | [sourced: companycam.com/press, 2024-02-28] |
| "tens-of-thousands" of businesses | CompanyCam customer scale in latest press item | [sourced: companycam.com/press, 2026-03-02] |
| 100,000 users; 350M photos | CompanyCam at Series B | [sourced: companycam.com/press, 2021-10-26] |
| $30M | CompanyCam Series B | [sourced: companycam.com/press, 2021-10-26] |
| $415M; $2B | CompanyCam Series C size; valuation (PitchBook) | [secondary: siliconprairienews, 2025-11-22] |
| >$20M ARR (Jul 2022) | CompanyCam | [sourced: siliconprairienews quoting company, 2025-11-22] |
| $68M ARR (2024) | CompanyCam | [secondary estimate: getlatka, undated] |
| 300% | Growth in CompanyCam "AI actions", year to Nov 2025 | [sourced: siliconprairienews, 2025-11-22] |
| 2026-09-09 | CompanyCam MCP Server (beta) blog post date | [sourced: companycam.com/resources/blog/ways-contractors-use-companycam-mcp-ai-daily-tasks] |
| 2026-10-22; ~2026-10-28; ~2026-11-01 | CompanyCam community search/camera-roll feature requests | [sourced: community.companycam.com threads 331, 340, 345; latter two dated by relative weekday on page read 2026-11-03] |
| 938,478 establishments; 8,135,442 employees | US private NAICS 23 construction, 2024 annual avg | [sourced: data.bls.gov/cew/data/api/2024/a/industry/23.csv, accessed 2026-11-03] |
| 588,440 establishments; 5,151,234 employees | US private NAICS 238 specialty trade, 2024 annual avg | [sourced: data.bls.gov/cew/data/api/2024/a/industry/238.csv, accessed 2026-11-03] |
| ≤18% ; ≤29% | Upper bound of CompanyCam penetration of US construction / specialty-trade establishments | [estimated: 170,000 / 938,478 = 0.181; 170,000 / 588,440 = 0.289; numerator global and Feb-2024, so ceilings] |
| $1.3B / $1.2B / $1.0B | Procore revenue 2025 / 2024 / 2023 | [sourced: Procore 10-K, filed 2026-02-24] |
| 17,850; 2,710 | Procore customers; customers >$100k ARR, at 2025-12-31 | [sourced: Procore 10-K, filed 2026-02-24] |
| 2025-10-15; 2026-10-21 | Procore Photo intelligence release; voice-first AI app release | [sourced: procore.com/press, those dates] |
| $102M; $902M; 2022-03-02 | OpenSpace Series D, valuation, date | [secondary: teardown.ai citing Bloomberg] |
| 275,000-350,000 users; 43-50B sq ft | OpenSpace, Nov-Dec 2025 (source disagrees with itself) | [secondary: teardown.ai; "marketing numbers rather than audited metrics"] |
| $56.7M ARR (2023) | OpenSpace | [secondary estimate: Latka via teardown.ai; uncorroborated] |
| $45M; $166M | Buildots Series D; total raised | [sourced: buildots.com blog, 2025-05-29] |
| $0 / $39 / $64 / $89 per user/mo | Fieldwire tiers, annual | [sourced: fieldwire.com/pricing, 2026-11-03] |
| 5 users / 3 projects / 100 sheets | Fieldwire free tier limits | [sourced: fieldwire.com/pricing, 2026-11-03] |
| $999/yr; $2,999/yr | HOVER Pro, Business subscriptions | [sourced: hover.to/pricing, 2026-11-03] |
| $9-$299 per job | HOVER per-scan fee range across Starter/Pro/Business and scan types ($9 Pro roof/interior floor; $299 Starter exterior ceiling); Pro $20 off | [sourced: hover.to/pricing, 2026-11-03] |
| 5 of 5 | Top adjusting firms using HOVER (vendor claim) | [sourced: hover.to/insurance, 2026-11-03] |
| $29 / $39 per user/mo | XactAI annual / monthly | [sourced: xactware.com/home/xactai.html, 2026-11-03] |
| 800M photos; 17M+ claims/yr; 30,500+ repairers | CCC | [sourced: cccis.com, 2026-11-03] |
| $65M; $7B; 20+ | Tractable Series E; annualized repairs processed; customers | [sourced: insightpartners.com, 2023-07-18] |
| $79.4M ARR | Tractable 2024 | [secondary estimate: getlatka] |
| 170+; 16 of top 20 | Snapsheet customers & investors; top-20 P&C carriers served | [sourced: snapsheetclaims.com, 2026-11-03] |
| Snapsheet funding; revenue | — | [unknown] (prior-round snippet numbers withdrawn; no URL) |
| 389,700; $78,020 | US claims adjusters/appraisers/examiners/investigators jobs 2025; median pay May 2025 | [sourced: bls.gov OOH, 2025 data] |
| 13,500; 2% | Auto damage appraiser jobs 2025; self-employed share | [sourced: bls.gov OOH, 2025 data] |
| calendar year of claim closure + 3 years (some states 5) | NAIC MO-910 §6.A claim-file retention | [sourced: NAIC model-law-910.pdf, 2004] |
| 10 years | CA CCP §337.15 repose | [sourced: california.public.law, 2026-11-03] |
| 10 years (to 12); 13 years recommended | TX CPRC §16.009; lawyer's retention advice | [sourced: ftworthconstruction.lawyer, 2025-10-23] |
| repose + 3 years | NSPE retention guidance | [sourced: NSPE white paper, 2016-06-01] |
| 13-15 years | Effective photo-retention horizon for contractors | [estimated: 10-12 yr repose (CA/TX above) + NSPE 3 yrs] |
| 8 items, 0 photographs | CA Civ §8416 required contents of a mechanics lien claim | [sourced: california.public.law, 2026-11-03] |
| 20 years | FRE 901(b)(8) ancient-document threshold (only number in Rule 901) | [sourced: law.cornell.edu/rules/fre/rule_901, 2026-11-03] |
| $109/mo; $1,090/yr; $99/mo extra inspector; $4/inspection | Spectora | [sourced: spectora.com/pricing, 2026-11-03] |
| 12,000+; up to 25% | Spectora inspectors; Match early-access time saving claim | [sourced: spectora.com, 2026-11-03] |
| zInspector per-unit price | — | [unknown] (Buildium 2026-08-18 says "prices per unit", no figure) |
| 2024-09-19; Ch. 280 | AB 2801 chaptered date; chapter number | [sourced: calmatters.digitaldemocracy.org, accessed 2026-11-03] |
| 2025-04-01; 2025-07-01 | CA Civ §1950.5 photo mandate operative dates | [sourced: california.public.law, 2026-11-03] |
| CA rental units / landlords | — | [unknown] (Census API needs key; QuickFacts 403) |
| ~22; 4 | NARPM partner logos; 2026 Premier Partners | [sourced: narpm.org, 2026-11-03] |
| 6 years | HIPAA §164.530(j)(2) documentation retention (not photo-specific) | [sourced: law.cornell.edu, 2026-11-03] |
| 7 years | CA H&S §123145 medical-record preservation (licensees ceasing operation) | [sourced: california.public.law, 2026-11-03] |
| 2025-01-09 | TX 22 TAC §165.1 repeal effective date (successor not retrieved) | [sourced: law.cornell.edu Texas regs, 2026-11-03] |
| $8M; 4,000 facilities; 20,000 users; 20M images | Swift Medical | [sourced: hitconsultant.net, 2024-01-29] |
| 15M+ images; 250k-300k images/month (one customer) | Net Health Tissue Analytics | [sourced: nethealth.com, 2026-11-03] |
| $10 per consultation | Miiskin Pro | [sourced: miiskin.com/pro, 2026-11-03] |
| Wound EMR price range | — | [unknown] (first-draft figure withdrawn; no URL) |
| 153; 61.8%; 46%; 69.1%; 23.7% | US dermatologists surveyed; daily photo use; smartphone camera; email/text sharing; protocol adherence | [sourced: PubMed, Milam & Leger 2018, doi:10.1111/jdv.14839] |
| 86; 50%; 25.6% | French plastic surgeons; photos stored on smartphone; synced to cloud | [sourced: PubMed, Djian 2018, doi:10.1016/j.anplas.2018.06.005] |
| 119; 72.9%; 86.3% | Indian dermatologists; personal smartphone; WhatsApp-group sharing | [sourced: PubMed, Janagond 2021, doi:10.4103/idoj.IDOJ_99_21] |
| 74; 93% | Israeli plastic surgeons; daily smartphone photography | [sourced: PubMed, Yanko 2025, doi:10.1097/ASW.0000000000000342] |
| $2,779.5M / $2,082.5M | Axon net sales 2025 / 2024 | [sourced: Axon 10-K, filed 2026-02-25] |
| $1,202.7M / $861.2M; $1.3B | Axon Software & Services net sales 2025 / 2024; ARR at 2025-12-31 | [sourced: Axon 10-K, filed 2026-02-25] |
| 30 days; 3 years; 2018-01-08 | MI MCL 780.316 BWC retention; effective date | [sourced: legislature.mi.gov, 2026-11-03] |
| 60 days / 2 years (CA); 90 days / 1 year (MN) | BWC retention | [sourced: axon.com state-law page, 2024-10-16] |
| TX BWC minimum retention | — | [unknown] (five statute URLs returned index pages only) |
| $3,247M / $2,736M; $147M | CoStar revenue 2025 / 2024; 2025 revenue from Matterport acquisition | [sourced: CoStar 10-K, filed 2026-02-26] |
| Matterport list pricing; USPAP workfile retention | — | [unknown] |
| $961.0M / $771.9M; ~10,800 | ServiceTitan revenue FY2026 / FY2025; active customers at 2026-01-31 | [sourced: ServiceTitan 10-K, filed 2026-03-25] |
| life of pipeline; 5 years | 49 CFR §192.491 | [sourced: law.cornell.edu, 2026-11-03] |
| 5,192; 249,941 | Rapid Recon dealerships; users | [sourced: rapidrecon.com, 2026-11-03] |
| FCIC-25230; 2026-09-30; 412 | Grape LASH number; issue date; handbooks listed on RMA page | [sourced: rma.usda.gov, 2026-11-03] |
| 160,000+ reviews | Brightwheel | [sourced: mybrightwheel.com, 2026-11-03] |
| 35,000+ reviews; 2.1B moments | Lillio (HiMama) | [sourced: lillio.com, 2026-11-03] |
| 1,000+ GCs; 80,000+ US workers | BuildPass | [sourced: buildpass.ai, 2026-11-03] |
| $8M (2025) | Klutch seed | [secondary: geekwire snippet; page 403; unverified] |
| S$1.7M (2026-04-09) | OnSite seed | [sourced: itbrief.asia, 2026-04-09] |
| $7.5M (Oct 2024) | BuildPass seed | [secondary: businessnewsaustralia snippet; page 403; unverified] |
| $2M (May 2026) | Hardline pre-seed | [sourced: landbase.com list, 2026-11-03; secondary] |
| >90% | Construction firms using smartphones on site (JBKnowledge) | [secondary: CompanyCam blog citing report] |
| $0.99 / $2.99 / $9.99 / $29.99 / $59.99 per month | iCloud+ 50GB / 200GB / 2TB / 6TB / 12TB, US | [sourced: support.apple.com/en-us/108047, 2026-11-03] |
| 6-21x | Vertical price (CompanyCam Core $63) vs consumer storage (iCloud+ 2TB $9.99; 200GB $2.99) | [estimated: 63/9.99 = 6.3; 63/2.99 = 21.1] |
| Fraction of US contractors on CompanyCam vs camera roll (true value) | — | [unknown]; ceiling estimated above |
| Fraction of CA landlords using a PM app; independent-adjuster count | — | [unknown] |
| HOVER funding; Axon Evidence list price; HappyCo/zInspector/Brightwheel/Procare/Lillio/Inspect Point/Buildots/OpenSpace/Tractable/Snapsheet/Net Health list prices | — | [unknown] |

---

## 5. Unknowns we could not resolve

1. The load-bearing one: the true fraction of small contractors (or CA landlords, or independent
   adjusters) whose working photo corpus lives only in a phone camera roll / iMessage. Only a ceiling for
   CompanyCam penetration (≤18% of US construction establishments) could be estimated. Needs the
   JBKnowledge ConTech report or a primary survey.
2. Statute/rule texts not retrievable without search: Texas Occ. Code §1701.655; USPAP Record Keeping
   Rule; the general FCIC Loss Adjustment Manual (only the Grape handbook was read); HHS FAQ 580 (403);
   successor to Texas 22 TAC §165.1; medical-record retention in states other than California.
3. Whether CompanyCam has shipped natural-language photo search behind login. Public pages (features,
   help center, blog, community) as of 2026-11-03 show MCP beta and users still requesting description
   search; a logged-in product check or the 2026 app-store changelog (App Store ID not known; Play Store
   URL 404) would settle it.
4. Pricing not public: Axon Evidence, HappyCo, zInspector, Brightwheel, Procare, Lillio, Matterport
   (three URLs failed), ServiceTitan, DermEngine, Net Health, Relativity, OpenSpace, Buildots, Tractable,
   Snapsheet, Inspect Point (429). HOVER and Snapsheet funding history.
5. Whether states other than California have enacted landlord photo mandates like §1950.5(g).
6. Insurer DRP contract photo requirements for body shops; carrier photo-documentation requirements for
   contractor-submitted property claims (only HOVER's marketing is indirect evidence).
7. Agriculture: vendor landscape and the LAM's photo rules.
8. Procore community thread date/content (503 twice).
9. Startups 2024-2026 in every vertical except construction: not searchable this round.
10. Denominators: CA renter-occupied units (Census API key required; QuickFacts 403); count of
    independent adjusters (naiia.com bot-check); CAA membership.
11. Distribution channels for law enforcement, real estate, field service, auto, agriculture, legal,
    childcare beyond "direct/enterprise sales".
12. XactAI launch date (secondary snippet only).

---

## 6. Ranking (Q6) with evidence

Scoring each criterion 0-2 from the evidence above (2 = strong sourced evidence; 1 = partial or
estimated; 0 = absent or contrary; "u" = unknown, scored 0 in the total and flagged). This is a judgment
aggregation, not a measured index. Changes from the first draft: Clinical (b) lowered from 2 to 1 because
HIPAA §164.530(j) is not a photo-retention rule and the state rule found (CA 7 yrs) is narrow; Contractors
(d) kept at 1 but for a new reason (MCP beta exists; NL photo search does not); "?" cells replaced.

| Vertical | (a) corpus in camera roll | (b) legal reason to keep | (c) someone paying | (d) no incumbent AI search | Total | Note |
|---|---|---|---|---|---|---|
| Small landlords / PMs (CA §1950.5) | 1 (phone capture is the natural device; share of landlords on a PM app [unknown]; CA unit count [unknown]) | 2 (statute names photos, capture events and delivery; AB 2801, 2024) | 1 (PM software quote-based; NARPM shows an association channel; small-landlord ARPU [unknown]) | 2 (none found at HappyCo/zInspector/Spectora, 2026-11-03) | 6 | Only explicit photo mandate found; single state; two of four scores rest on unknowns |
| Small contractors / trades | 1 (CompanyCam ≤18% ceiling of establishments [estimated]; vendor blogs describe camera rolls/WhatsApp, no statistic) | 1 (repose 13-15 yrs [estimated], FRE authentication value; no mandate) | 2 ($63-$199/mo norms; 170k customers Feb 2024) | 1 (no NL photo search shipped; MCP beta 2026-09-09 exposes account to Claude/ChatGPT; users requesting search 2026-10/11) | 5 | Biggest paying base; incumbent has already built the BYO-AI bridge |
| Clinical wound/derm | 2 (46-73% smartphone capture; 50% phone-only storage in one survey [sourced: PubMed]) | 1 (state medical-record rules, e.g., CA 7 yrs; HIPAA 6 yrs is documentation only; photos not named) | 2 (enterprise contracts; $10/consult) | 1 (DermEngine visual search) | 6 | PHI/BAA burden high for seed; institutions fix capture, not retrieval |
| Independent/public adjusters | 1 (phones used; deliverable lands in Xactimate; personal copies [unknown]) | 1 (NAIC closure +3 yrs, 5-yr PA rule) | 2 ($29-$39 add-ons, per-job $9-$299) | 0 (XactAI labels shipped; Snapsheet searchable claim files) | 4 | Corpus ends up in Verisk/carrier systems |
| Field service / utilities | 1 (not quantified) | 1 (PHMSA records, photos not named) | 2 (ServiceTitan $961M revenue, per-tech) | 1 (ServiceTitan AI is coaching/recognition, not search) | 5 | Under-researched; electric/water rules unknown |
| Legal e-discovery | 2 (phones collected wholesale) | 1 (per-matter hold; FRE 901/1001) | 2 (Relativity volume pricing) | 1 (no image search evidenced) | 6 | Per-matter, vendor-mediated; no standing corpus |
| Home inspectors | 0 (report software owns the photos) | u (no retention period found; TX rule is content-only) | 2 ($109/mo) | 1 (Spectora AI is voice/text assist) | 3 | |
| Body-worn camera | 0 | 2 (state statutes, 30 days-3 yrs) | 2 (Axon ARR $1.3B) | 0 (Axon auto-tagging/search) | 4 | Closed |
| Auto body / dealers | 0 (CCC; Rapid Recon) | u (DRP/dealer rules unknown) | 2 | 0 (CCC/Tractable) | 2 | Closed on body-shop side |
| Childcare | 0 (apps own the feed; "2.1B moments shared") | 0 (consent rules only) | 2 (quote-based SaaS) | 1 | 3 | No driver |
| Real estate | 1 (listing photos on phones; Matterport is a capture product) | u (USPAP text not retrieved) | 2 (Matterport $147M in CoStar 2025 revenue) | u | 3 | No driver found |
| Agriculture | u | 1 (LASH requires aerial photo/sketch of unit, not damage photos; LAM unknown) | u | u | 1 | Unresearched beyond one handbook |

**Position argued.** The thesis as stated ("corpora already outside the camera roll + forced retention +
unsolved AI search") mostly fails: wherever the corpus is already outside the camera roll, a vendor owns
it and is shipping photo AI or an AI bridge (Verisk, CCC, Axon, Procore, CompanyCam-MCP). The interesting
overlap with the seed is the inverse: corpora that have a legal reason to exist for years but are still
on phones. Three candidates survive, none cleanly:

1. Small trades contractors: best paying norms ($63-$199/mo), long retention horizon (13-15 yrs,
   estimated), and sourced evidence that users want description-level search (community, 2026-10-22). But
   CompanyCam serves up to ~18% of US establishments (ceiling), has unlimited storage, imports camera-roll
   photos with original capture dates, and already lets Claude/ChatGPT read the account via MCP beta. A
   seed company here is betting on the ≥82% of establishments not on CompanyCam, a population that is
   unquantified beyond the ceiling [estimated above].
2. California small landlords under Civ §1950.5 (AB 2801, 2024): the one place a statute names
   photographs, sets capture events, and forces delivery to a counterparty. Weaknesses: single state, ARPU
   [unknown], denominator [unknown], small per-unit corpus, and PM incumbents could add it trivially.
3. Clinical (new entrant to the shortlist on evidence, not on attractiveness): the only vertical with
   peer-reviewed survey data showing the corpus is on personal phones. But the content is PHI, the
   institutional remedy is EHR-integrated capture, and the retention driver is state medical-record law
   that does not name photos. Not a seed-stage fit.

All three candidates are "camera-roll-first" rather than "vendor-corpus-first," which means the seed's
export/ingest machinery (not its storage) is the reusable asset. The compliance driver supplies the
retention argument the consumer seed lacked. The 2026 evidence also sharpens v0 A6: a vertical vendor
(CompanyCam) chose to expose its corpus to assistants itself, which is both proof the MCP route works and
proof the vendor will not leave that layer to a third party.

---

## 7. Full source list (access date 2026-11-03 unless noted)

Primary / near-primary (fetched this round or the prior round and still cited):
1. https://companycam.com/press — press archive, items 2017-03-26 to 2026-03-02 (re-read this round)
2. https://companycam.com/pricing — pricing page (FAQ: "AI features are included in Crew, Scale, and Enterprise"; "your photos stay in your account")
3. https://companycam.com/features — features page ("Unlimited cloud storage"; no "search"; re-read this round)
4. https://help.companycam.com/ — help center (AI Tools section; no release notes)
5. https://companycam.com/resources/blog — blog index (12 posts listed; URLs recorded)
6. https://companycam.com/resources/blog/ways-contractors-use-companycam-mcp-ai-daily-tasks — 2026-09-09 (MCP Server beta)
7. https://companycam.com/resources/blog/find-job-photos — 2026-09-14
8. https://companycam.com/resources/blog/ai-strategy-business-data — 2026-10-01
9. https://companycam.readme.io/llms.txt — API docs index (list-photos endpoints; no MCP)
10. https://community.companycam.com/ ; /forums/product-wishlist.25/ ; /threads/description-search-in-global-search.331/ (2026-10-22) ; /threads/search-by-customer.340/ ; /threads/date-added-camera-roll.345/
11. https://siliconprairienews.com/2025/11/companycam-reaches-unicorn-status-with-2-billion-valuation-a-first-for-a-nebraska-startup/ — 2025-11-22
12. https://www.procore.com/press — press index (2026 items dated to 2026-10-21)
13. https://www.procore.com/press/procore-advances-the-future-of-construction-with-new-ai-innovations — 2025-10-15
14. https://www.procore.com/press/procore-launches-voice-first-ai-mobile-app-built-for-the-jobsite — 2026-10-21
15. https://www.sec.gov/Archives/edgar/data/1611052/000162828026011055/pcor-20251231.htm — Procore 10-K FY2025, filed 2026-02-24
16. https://www.on-sitemag.com/products/procore-introduces-ai-innovations-to-construction-technology-platform/ — 2025-10-20
17. https://www.xactware.com/home/xactai.html — XactAI pricing/features
18. https://buildots.com/blog/buildots-raises-45m-in-series-d-funding/ — 2025-05-29
19. https://www.openspace.ai/news/ — items dated 2026-09-15 to 2026-10-28
20. https://www.openspace.ai/news/openspace-expands-platform-with-ai-agents-and-progress-tracking/ — 2026-09-30
21. https://www.openspace.ai/pricing/ — quote-based by ACV
22. https://www.fieldwire.com/pricing/
23. https://hover.to/pricing ; https://hover.to/insurance ; https://hover.to/press (items 2025-04)
24. https://happy.co/pricing
25. https://www.zinspector.com/pricing
26. https://www.buildium.com/blog/best-property-management-inspection-software/ — 2026-08-18
27. https://www.spectora.com/pricing/ ; https://www.spectora.com/
28. https://www.servicetitan.com/pricing
29. https://www.sec.gov/Archives/edgar/data/1638826/000163882626000028/ttan-20260131.htm — ServiceTitan 10-K FY2026, filed 2026-03-25
30. https://www.cccis.com/
31. https://www.insightpartners.com/ideas/tractable-ai-raises-65m-in-series-e-funding-led-by-softbank-vision-fund-2-investment-to-power-next-generation-ai-for-instant-visual-assessments-within-the-automotive-and-property-ecosystems/ — 2023-07-18
32. https://www.snapsheetclaims.com/ (redirect from snapsheet.me)
33. https://www.cotality.com/insurance (CoreLogic, renamed)
34. https://www.bls.gov/ooh/business-and-financial/claims-adjusters-appraisers-examiners-and-investigators.htm — 2025 employment
35. https://data.bls.gov/cew/data/api/2024/a/industry/23.csv ; .../238.csv — QCEW 2024 annual
36. https://hitconsultant.net/2024/01/29/swift-medical-secures-8m-to-power-ai-driven-wound-care/ — 2024-01-29
37. https://www.nethealth.com/wound-care/tissue-analytics/
38. https://www.dermengine.com/
39. https://miiskin.com/pro/
40. PubMed (via PubMed tool): Milam & Leger 2018 https://doi.org/10.1111/jdv.14839 ; Djian et al. 2018 https://doi.org/10.1016/j.anplas.2018.06.005 ; Janagond & Inamadar 2021 https://doi.org/10.4103/idoj.IDOJ_99_21 ; Yanko et al. 2025 https://doi.org/10.1097/ASW.0000000000000342 ; Wyatt et al. 2020 https://doi.org/10.2196/14412
41. https://mybrightwheel.com/ ; https://www.procaresoftware.com/pricing/ ; https://www.lillio.com/
42. https://www.axon.com/products/axon-evidence ; https://www.axon.com/news
43. https://www.axon.com/resources/body-camera-laws-by-state — 2024-10-16 (no Texas)
44. https://www.sec.gov/Archives/edgar/data/1069183/000162828026011360/axon-20251231.htm — Axon 10-K FY2025, filed 2026-02-25
45. https://www.legislature.mi.gov/Laws/MCL?objectName=mcl-780-316 — MCL 780.316 (Act 85 of 2017)
46. https://content.naic.org/sites/default/files/model-law-910.pdf — NAIC MO-910 (2004), text extracted locally; §6.A re-verified by auditor
47. https://california.public.law/codes/ca_civ_code_section_1950.5 — Civ. Code §1950.5
48. https://calmatters.digitaldemocracy.org/bills/ca_202320240ab2801 — AB 2801, chaptered 2024-09-19 (Ch. 280)
49. https://california.public.law/codes/ca_civ_proc_code_section_337.15 — CCP §337.15
50. https://california.public.law/codes/ca_civ_code_section_8416 — Civ. Code §8416 (mechanics lien contents)
51. https://california.public.law/codes/ca_health_and_safety_code_section_123145 — H&S §123145
52. https://www.law.cornell.edu/rules/fre/rule_901 ; https://www.law.cornell.edu/rules/fre/rule_1001
53. https://www.law.cornell.edu/cfr/text/45/164.530 — 45 CFR §164.530(j)
54. https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-165-1 — repealed eff. 2025-01-09
55. https://www.law.cornell.edu/cfr/text/49/192.491 — 49 CFR §192.491
56. https://www.law.cornell.edu/regulations/texas/22-Tex-Admin-Code-SS-535-222 — 22 TAC §535.222
57. https://www.nspe.org/sites/default/files/resources/pdfs/liability/White%20Paper-060916DocumentRetentionDocument-FINAL.pdf — 2016-06-01, text extracted locally
58. https://www.ftworthconstruction.lawyer/how-long-to-keep-construction-documents/ — 2025-10-23
59. https://www.terial.com/blog-posts/job-site-photo-documentation-workflow — 2026-08-18 (quotes corrected this round)
60. https://www.relativity.com/data-solutions/air/ ; https://www.relativity.com/pricing/
61. https://www.sec.gov/Archives/edgar/data/1057352/000105735226000020/csgp-20251231.htm — CoStar 10-K FY2025, filed 2026-02-26
62. https://www.rapidrecon.com/
63. https://www.narpm.org/ ; https://caanet.org/
64. https://www.rma.usda.gov/policy-procedure/crop-loss-adjustment-standards ; https://www.rma.usda.gov/sites/default/files/2026-09/2027%2025230%20Grape%20Loss%20Adjustment%20Standards%20Handbook.pdf — FCIC-25230, 2026-09-30, text extracted locally
65. https://itbrief.asia/story/onsite-raises-s-1-7-million-to-build-ai-for-construction — 2026-04-09
66. https://www.constructiondive.com/news/construction-tech-funding-Q4-2025/808986/ — 2026-01-07
67. https://www.landbase.com/blog/ai-construction-startups-hiring-fastest — undated list
68. https://www.klutch.ai/ ; https://www.buildpass.ai/
69. https://www.teardown.ai/companies/openspace — secondary aggregator
70. https://support.apple.com/en-us/108047 — iCloud+ US prices
71. https://appraisalfoundation.org/ ; https://appraisalfoundation.org/pages/uspap — no rule text (2024 edition current)

Secondary only (surfaced in prior-round search summaries; page not fetched or blocked):
72. https://www.geekwire.com/2025/seattle-startup-klutch-raises-8m-to-bring-ai-coworkers-to-construction-sites/ — 403 (twice)
73. https://www.businessnewsaustralia.com/articles/-what-a-ride---construction-tech-startup-buildpass-raises--7-5m-from-seed-round.html — 403
74. https://iireporter.com/verisk-launches-xactai-for-property-claims-automation/ — empty body on fetch
75. https://getlatka.com/companies/companycam ; https://getlatka.com/companies/tractable.ai — ARR estimates
76. https://community.procore.com/s/question/0D58V00007oxaEESAY — 503 (twice)
77. https://companycam.com/resources/blog/construction-photo-documentation-a-contractors-guide-to-protecting-your-work — JBKnowledge >90% figure

Blocked / empty / not found this round (not cited for content): api.census.gov (key required, 3 queries);
census.gov/quickfacts (403, 2 URLs); naiia.com (bot-check); statutes.capitol.texas.gov (landing page only,
2 forms); texas.public.law §1701.655 (nav only); codes.findlaw.com §1701-655 (index only, 2 forms);
hhs.gov HIPAA FAQ 580 (403); matterport.com/pricing (nav only), /plans (404), support.matterport.com
(404, 2 articles); inspectpoint.com (429, 3 URLs); buildots.com/pricing (404); companycam.com/product/ai
(404); play.google.com CompanyCam (404); apps.apple.com guessed ID (404); lillio.com/pricing (404);
cotality.com/insurance/claims (404); verisk.com/company/newsroom and /en-us/news (empty); rma.usda.gov
handbooks pages (404, 3 URLs); one.google.com/about/plans (no prices rendered); geekwire (403);
community.procore.com (503). Prior-round blocked list also still applies: leginfo.legislature.ca.gov,
legiscan.com, law.justia.com, ecfr.gov, costargroup.com, miiskin.com/pro/pricing, dermengine.com/pricing,
mybrightwheel.com/pricing, investor.axon.com, forum.nachi.org.

---

## Audit log

Each auditor finding and what was done (all edits in place; nothing that passed verification was removed).

Untagged numbers
1. "14 searches" method count — replaced with the sourced fact that zero searches were available this round [sourced: WebSearch tool response, 2026-11-03]; row added to numbers table.
2. "6-13 years" with an unsupported 6-year input — recomputed as 13-15 years from the inputs actually in the file (CA 10 yrs, TX 10-12 yrs, NSPE +3); the 6-year bound is explicitly withdrawn (sections 2.1 Q2, 4, 6).
3. "~3-year-old Procore community thread" — age removed; thread now described as undated, 503 on two fetches, content unverified.
4. "aggregators disagree by 5x" (Snapsheet revenue) — removed; Snapsheet funding and revenue now [unknown]; replaced with sourced site figures (170+ customers; 16 of top 20 P&C carriers).
5. "$400-$1,200/mo" wound-EMR range with no URL — removed; now [unknown].
6. "12-24 months" shipping estimate — removed; A4 now says timing [unknown] with the roadmap quote and the 2026 MCP-beta fact as the only evidence.
7. "5-20x consumer subscriptions" with unsourced consumer input — recomputed as 6-21x using sourced iCloud+ prices ($9.99/2TB, $2.99/200GB) [sourced: support.apple.com/en-us/108047].
8. Ranking (b)=2 for Clinical resting on HIPAA — lowered to 1; the state medical-record rule (CA H&S §123145, 7 yrs) is now cited and HIPAA §164.530(j) is labelled documentation-only.
9. "$60/mo for 100 units" zInspector — Buildium page re-fetched (dated 2026-08-18): it says only "prices per unit"; the figure is withdrawn and tagged [unknown].

Suspect claims
10. HOVER "$9-$89/job" — corrected to the full per-scan matrix and a $9-$299 overall range; "insurance Pro tier" corrected to the Pro plan on the Insurance tab ("Adjuster Pro"). Fixed in sections 2.1, 2.2 Q5, 4.
11. NAIC MO-910 claim-file rule — corrected to §6.A "calendar year in which the claim is closed plus three (3) years"; noted that "current year plus three" is the §4/5 policy-records rule; clock-at-closure implication added (sections 2.2 Q2, 3, 4).
12. Stale Q3 verdict for CompanyCam — re-researched with 2026 sources: press (latest 2026-03-02), features page, help center, three 2026 blog posts (MCP beta 2026-09-09; find-job-photos 2026-09-14; AI strategy 2026-10-01), API docs, and three community feature requests (2026-10-22 to ~2026-11-01). Verdict rewritten; ranking note updated. Procore 2026 state added (10-K, 2026-10-21 voice app). OpenSpace 2026-09-30 release read.
13. "170,000 contractors" used as current — now labelled "as of 2024-02-28; 2.7 years old, likely understated" everywhere; 2026-03-02 "tens-of-thousands" wording added; current count [unknown].
14. Terial quotes — replaced with the verbatim sentences the auditor supplied ("A photo buried in a text thread or personal gallery..."; "personal camera rolls, text threads, or email attachments"; "may be inaccessible when disputes arise").
15. "Unlimited cloud storage" attribution — now attributed to companycam.com/features only, with the full sentence; pricing-page inconsistency about Core AI credits noted.
16. Procore "Photo AI" — renamed "Photo intelligence"; the sentence is marked as a paraphrase.
17. HOVER tier name — fixed (see 10).
18. "6-13 years" — fixed (see 2).
19. "12-24 months" — fixed (see 6).
20. Clinical (b)=2 — fixed (see 8).
21. Texas 90-day BWC minimum — five statute URLs attempted (statutes.capitol.texas.gov x2, texas.public.law, codes.findlaw.com x2) plus the Axon state-law page (no Texas); none returned section text; figure withdrawn and tagged [unknown].
22. OpenSpace 275,000 / 43B — now reported as the range 275k-350k users and 43-50B sq ft with teardown.ai's own "marketing numbers" disclaimer; openspace.ai/news explicitly noted as not supporting any of these figures.
23. Klutch / BuildPass seed rounds — both company sites fetched (product descriptions added, sourced); funding amounts kept but tagged "[secondary ...; page 403; unverified]"; geekwire 403 again.
24. Snapsheet funding — withdrawn to [unknown] (no URL); site facts added.
25. XactAI launch date — kept as secondary and explicitly "uncorroborated"; Verisk newsroom and xactware news fetched (empty).
26. Spectora Match quote — re-fetched homepage; "Speak your observations, snap photos as you go." now verified verbatim, plus the pairing sentence and the "up to 25%" claim.
27. CA Civ 1950.5 "as amended by AB 2801" — attribution now sourced to calmatters.digitaldemocracy.org (chaptered 2024-09-19, Ch. 280, Stats. 2024).

Broken or misquoted sources
28. hover.to/pricing — misquote fixed (see 10).
29. NAIC PDF — misquote fixed (see 11).
30. terial.com — misquote fixed (see 14).
31. companycam.com/pricing mis-attribution — fixed (see 15).
32. Procore press mis-naming — fixed (see 16).
33. FindLaw §1701.655 — removed as support; listed under blocked/empty.
34. companycam.com/ai and geekwire — remain in blocked list; replaced with working CompanyCam blog/community URLs and klutch.ai.
35. openspace.ai/news — Q1 text now routes every funding/user figure to teardown.ai and says the news page does not support them; news page cited only for dated headlines and the 2026-09-30 release text.
36. Spectora quote — verified (see 26).
37. Verified-verbatim list — all retained unchanged.

Missing vs brief
38. Q1 vendors: added CoreLogic/Cotality (products, no pricing), Procare (quote-based), Lillio/HiMama (site figures; pricing 404), Matterport via CoStar 10-K ($147M 2025 revenue; list pricing unknown after 4 URLs), Procore 10-K (revenue, customers), Axon 10-K (net sales, S&S segment, ARR $1.3B), ServiceTitan 10-K (revenue, customers, Field Pro AI), OpenSpace pricing (quote-based by ACV), Buildots pricing (404 → unknown), Snapsheet (site), Tractable pricing (unknown), Tissue Analytics pricing (unknown), Inspect Point (429 x3 → unknown), Rapid Recon (dealers).
39. Q2 drivers: added mechanics lien law (CA Civ §8416, no photos), FRE 901 and 1001 (authentication; photograph/original definitions), insurer requirements for contractors (unknown; HOVER insurance page as indirect evidence), USPAP (two appraisalfoundation.org pages; rule text not public → unknown), state medical-record retention (CA H&S §123145, 7 yrs; TX 22 TAC §165.1 repealed 2025-01-09), body-shop DRP (unknown, stated), agriculture (RMA listing + Grape LASH FCIC-25230 read; LAM unknown), utilities electric/water (unknown, stated).
40. Q3 demand evidence: added CompanyCam community Product Wishlist threads (3, dated), CompanyCam MCP beta and two further 2026 posts, Procore 2026-10-21 release and 10-K, OpenSpace 2026-09-30 release, Spectora homepage. Reddit was not used (search engine restriction); CompanyCam app-store changelogs could not be reached (Play 404; App Store ID unknown).
41. Q4 denominators: added BLS QCEW 2024 (938,478 / 588,440 establishments) and an [estimated] penetration ceiling (≤18% / ≤29%); BLS OOH adjuster employment (389,700); CA rental units attempted via Census API (key required) and QuickFacts (403) → [unknown]; independent-adjuster count attempted via naiia.com (bot-check) → [unknown]; PubMed surveys added for clinician phone capture.
42. Q5 channels: "app-store self-serve" replaced with sourced "self-serve web signup / free trial" from three pricing pages; NARPM partner/affiliate program added for PM; CAA fetched (no vendor program visible); HOVER insurance channel (adjusting firms, Xactimate/ClaimsConnect/SettleAssist) added; other verticals explicitly [unknown].
43. Startups in non-construction verticals: not searchable this round; stated as "[unknown] — absence of research, not evidence of absence" in 2.12 and section 5.
44. Q6 ranking: "?" cells replaced with scored values or explicit "u" (unknown, counted as 0); the landlord row now states which scores rest on unknowns and its total was recomputed (6, down from 7); clinical row re-scored; a third shortlist candidate (clinical) added on evidence with reasons it is not a seed fit.
45. Automotive dealers (Rapid Recon) and utilities beyond gas (unknown, stated) added.
46. Agriculture vendor (none found), real estate (CoStar/Matterport 10-K), childcare (Procare, Lillio) added.
