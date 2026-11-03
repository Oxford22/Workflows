# Track C — Customers (who has the family-archive problem, what they do today, what they pay)

Research date: 2026-11-03 (repair pass same day). All URLs accessed 2026-11-03 unless noted. Source dates are the dates of the source, not today.
Tagging: `[sourced: url, date]`, `[estimated: method]`, `[unknown]`.

Scope note on method: Reddit is blocked to this agent's crawler (WebSearch refused `reddit.com` as an allowed domain; WebFetch refuses `www.reddit.com` and `old.reddit.com`). Forum evidence therefore comes from Apple Community (discussions.apple.com), Apple Developer Forums, MacRumors Forums, Hacker News (threads located via the public HN Algolia API, hn.algolia.com), GitHub Discussions (immich), FamilySearch Community, and the Google Photos Community listing. All quotes are verbatim from public posts, attributed by URL, never by username. No Reddit quote in this file is invented; there are none.
Repair-pass constraint: the shared WebSearch budget for this turn was exhausted before the repair began, so every addition below comes from direct fetches of known or inferable URLs. Where a fetch failed, the attempt is recorded.

---

## 1. Questions asked

1. Which segments have the family-archive problem acutely? (a) genealogists, (b) estates/bereavement, (c) cross-platform households, (d) families with boxes of prints, (e) professional photo organizers, (f) divorce/separation, (g) adult children consolidating parents' libraries, (h) new parents (FamilyAlbum, Tinybeans).
2. What do they do today and what do they pay? (table)
3. Willingness to pay: surveys on photo organization, digital legacy, photo-book spend.
4. Forum evidence of the pain (verbatim, by URL).
5. Search-volume signals.
6. Seed assumption A3: is "merged multi-relative archive" an acute, paid-for pain for some segment? Falsify first.

---

## 2. Findings per question

### Q1(a) Family historians / genealogists

**Scale (primary sources):**
- Ancestry: "3.8M+ subscribers", "29M+ DNA customers", "71B+ records available", "145M+ family trees" (2025 Impact Report, published 2026) [sourced: https://cmsasset.ancestrycdn.com/content/dam/Impact-Report-2026/Ancestry_IR_2026_FullReport.pdf, 2026]. SASB table in the same report: "TC-IM-000.A Entity-defined measure of user activity — 3.8M subscribers" and data storage "42 PB" (2025 result) vs "24 PB" baseline [sourced: same, 2026]. Caveat: the SASB table shows "3.8M subscribers" in both the baseline column (2022 report) and the 2025 column, i.e. unchanged over ~3 years, which reads as a rounded marketing figure rather than a measured year-end count.
- Ancestry company-facts page (live, undated): "More than 3 million paying subscribers", "over 30 million" DNA customers, "150 million" family trees, "Over 1 billion user generated photos, scanned documents and written stories" [sourced: https://www.ancestry.com/corporate/about-ancestry/company-facts, ©2026, undated]. The 3M / 30M / 150M figures conflict with the Impact Report's 3.8M+ / 29M+ / 145M+; the two pages are of different vintages and neither is dated. The "1 billion" figure is the only public number on user-photo volume at a genealogy vendor, and it bundles photos with documents and stories.
- MyHeritage: "MyHeritage celebrates an extraordinary milestone, and surpasses one million annual subscribers!" (milestone carries **no year** on the page), "58 MILLION family trees", "9.6 MILLION DNA database", "520 employees" (all undated) [sourced: https://www.myheritage.com/about-myheritage, ©2026, undated]. Registered-user count 2025–26: [unknown] — attempts: about page (no user count), blog index (only record-count posts, e.g. "MyHeritage Adds 450 Million Historical Records in September 2026", 2026-10-06 [sourced: https://blog.myheritage.com/2026/10/myheritage-adds-450-million-historical-records-in-september-2026/, 2026-10-06]). Older secondary: "75 million registered users" (2013, TechCrunch as cited by Wikipedia) and "80 million registered users" (2015, Jewish News as cited by Wikipedia); Francisco Partners acquired MyHeritage in early 2021 for a reported $600M [sourced: https://en.wikipedia.org/wiki/MyHeritage, accessed 2026-11-03; secondary, citing TechCrunch 2013-10-15, 2015-04-29, 2021-02-24].
- FamilySearch (free, LDS-funded): "more than 297 million visits in 2025"; Family Tree "grew by more than 163 million people"; "467 million sources" added [sourced: https://www.familysearch.org/en/blog/familysearch-year-in-review-2025, 2026-01-07]. Count of Memories (photos) uploaded: [unknown] — not published. Help center: no hard cap on Memories, but "accounts with more than 5,000 items may load slowly" [sourced: https://www.familysearch.org/en/help/helpcenter/article/how-many-memories-photos-stories-documents-and-audio-files-can-i-upload, undated].

**Pricing:**
- Ancestry: web plan page unreachable (ancestry.com/offers → HTTP 400; /cs/offers/subscribe returns navigation only; help-center search "subscription price" lists 10 articles, none with a dollar figure). App Store listing (primary, but billing period not labelled per line): in-app purchases "U.S. Discovery $19.99", "U.S. Discovery $24.99", "World Explorer $34.99", "World Explorer $39.99", "Just this record $1.99"; 659K ratings, 4.8 average [sourced: https://apps.apple.com/us/app/ancestry-family-history-dna/id349554263, accessed 2026-11-03]. Read as: U.S. Discovery ≈ $20–25/month, World Explorer ≈ $35–40/month [estimated: App Store IAP lines; the two price points per plan are consistent with monthly vs promotional/first-period pricing, but the listing does not say]. Six-month / annual web prices: [unknown].
- MyHeritage: plan structure is public but prices are not on any fetched page. Plans: Basic (free; "family tree of up to 250 people and 500 MB"), Premium ("up to 2,500 people, 1,000 MB"), PremiumPlus (unlimited), Data (annual; "more than 40 billion historical records"), Photo subscription ("Unlimited photo scanning and storage, plus AI tools ... and 20 LiveMemory videos per year"), Complete ("does not include the Photo Scanner"), Omni (adds OldNews, Geni Pro, "unlimited photo scanning and 30 LiveMemory videos per year") [sourced: https://www.myheritage.com/help/en/articles/13130253-what-types-of-subscriptions-does-myheritage-offer, undated]. The two price articles say the Data plan is "offered on a yearly basis" and that the upgrade price "depends on the subscription type and number of years you choose" and is computed inside the account [sourced: https://www.myheritage.com/help/en/articles/12852235-how-much-does-a-data-subscription-cost and .../12852240-how-much-does-a-family-site-upgrade-cost, undated]. myheritage.com/plans → 404; App Store listing id417558742 → 404. MyHeritage USD prices: [unknown] after five attempts. Notable for this track: MyHeritage sells a **standalone Photo subscription** (scanning + AI tools) — a genealogy vendor already monetizes the photo side separately.

**Do they handle photos?** Yes, but as attachments to tree persons, not as a library manager. MyHeritage discontinued DeepStory in Aug 2025 and replaced it with LiveMemory (animation), and still offers colorization ("MyHeritage In Color") [sourced: https://education.myheritage.com/article/myheritage-photo-features/, 2025]. FamilySearch Memories supports albums and archiving when a gallery "can become so full that it is difficult to manage" [sourced: https://www.familysearch.org/en/help/helpcenter/article/my-gallery-in-memories-is-too-full, undated].

**Pain evidence (forums):**
- FamilySearch Community, Jan 2021: a user said a second cousin "just texted me quite a few photos of family documents and I'd love to add them to the LDS database but feel overwhelmed"; a reply warned the forum "is not a service for sorting photos" and "you will NEED to know the People in the Photographs; BEFORE, they can even be 'Uploaded'" [sourced: https://community.familysearch.org/en/discussion/comment/215626, 2021-01].
- FamilySearch Community, Memories category (thread dated Sep 26–Oct 12; page shows month/day only, year 2026 inferred from the category listing's "last activity October 27" ordering): "I selected all my gallery images (~1700) and tried to copy them all to one folder." "Failed with no error message. So I tried copying a couple hundred at a time. Worked." Replies: albums have "a number limit of 1000 memories"; "so don't add more than 1,000 items to an album - or you will just get frustrated"; batch operations "you dont get an error - it simply doesnt work" at roughly 400–500 items [sourced: https://community.familysearch.org/en/discussion/192372/what-are-the-limits-on-folders-of-images-and-or-total-size-mbytes, 2026 (inferred)]. Same category listing also shows "BUG in latest Memories UI" ("It used to be that we could see the DATE a memories item was uploaded") and "Change in upload to Memories" [sourced: https://community.familysearch.org/en/categories/memories, accessed 2026-11-03].
- Adobe Community (Lightroom Classic): a user with "about 10,000 scanned family photos" wanted metadata "saved in the files and not be dependent on a catalog that would force family to purchase software" [sourced: https://community.adobe.com/t5/lightroom-classic-discussions/beginner-workflow-for-scanned-photos/m-p/10435335, undated].
- r/Genealogy: not reachable (Reddit blocked); FamilySearch Community search endpoint returns 403, so evidence is limited to the category listing above.

**Interpretation:** Genealogists are a large, already-paying population (3.8M Ancestry subs alone, at roughly $20–40/month per the App Store) with an explicit "identify people across generations, preserve metadata portably" need, and MyHeritage already sells a separate Photo subscription. But their tools organize *ancestors*, not *libraries*; FamilySearch's own Memories tooling breaks at ~1,000-item albums. Evidence that they would pay separately for a *library* product is still indirect.

### Q1(b) Estates and bereavement

**What happens at death (primary):**
- Apple Legacy Contact: data "might include photos, messages, notes, files, device backups, and more"; requires access key plus death certificate; the legacy contact must be 13 or older; requires iOS 15.2 / macOS 12.1 or later; excludes purchased media and iCloud Keychain [sourced: https://support.apple.com/en-us/102631, undated]. Without a Legacy Contact, Apple "generally includes a death certificate, and might also require a court order"; in the U.S. a court order naming the heir is required; "Only one person can request access to a deceased person's Apple Account"; Apple "isn't able to decrypt" end-to-end encrypted data [sourced: https://support.apple.com/digital-legacy, undated].
- Google: three options for a deceased user ("Close the account", "request for funds", "Obtain data"); Google "cannot provide passwords or other login details"; content may be provided "in certain circumstances" and "only after a careful review"; closure is permanent and Google "is unable to process any request to turn over the contents of the account at a later date" [sourced: https://support.google.com/accounts/troubleshooter/6357590, undated]. Inactive Account Manager: up to 10 trusted contacts; without a plan Google may delete accounts "inactive across Google for at least two years"; the help page's example data list does not mention Photos [sourced: https://support.google.com/accounts/answer/3036546, undated].

**Adoption (surveys, secondary but named):**
- Trust & Will 2026 Estate Planning Report (n=5,000 US adults, fielded Jan 28–Feb 5 2026, MoE ±1.4pp): "48% of Americans have no instructions in place for what should happen to their digital accounts and files when they die"; 21% have formal written instructions; **12% have account-level controls** ("Facebook's Legacy Contact or Google's Inactive Account Manager"); Gen Z 23% vs Boomers 4%; "12% of Americans say their digital life will be among the most meaningful things they leave behind" [sourced: https://trustandwill.com/learn/estate-planning-report-2026, page "Last updated June 29, 2026"]. No photo-specific statistic; Apple Legacy Contact is not named in the question wording.
- Bryn Mawr Trust / Opinium (n=1,500: 750 nat-rep + 750 HNW; fielded Sep 25–Oct 2 2024; MoE ±4%): 76% "little or no knowledge of digital estate planning"; 39% never heard of the term; 79% say protecting digital assets is important; "30% have more than 30,000 digital files"; only 53% of will-holders specify digital-asset wishes [sourced: https://www.bmt.com/news-insights-events/bryn-mawr-trust-survey/, 2024-12]. Definition of digital assets names "personal records, videos, social media content, passwords, biometric data, and financial information" — photos not named explicitly.
- Apple's count of users with a Legacy Contact set: [unknown] (not disclosed; no Apple statement found). Google IAM adoption: [unknown]. Repair-pass note: no Pew / Morning Consult / vendor survey on this specific question could be located without web search; the T&W 12% remains the only proxy and it covers Facebook + Google only.

**Pain evidence (forums):**
- Apple Community, 2024-01-15: "My husband sadly passed away in May of 2021." ... "I would like to access the many photos he took of himself and our family" ... "authentication is not possible because we no longer have his old phone number active." ... "I would be devastated if the hundreds of memories stored on his cloud are lost". Only reply: a link to Apple's deceased-account article; thread closed with no resolution [sourced: https://discussions.apple.com/thread/255414530, 2024-01-15].
- The previous version of this file cited "multiple" similar Apple Community threads from a search-result listing without opening them; that claim is withdrawn. Apple Community's own search page (discussions.apple.com/search) renders no results to the crawler, so no further threads could be opened this pass.

**Estate-attorney guidance (secondary, law-firm blogs):** RUFADAA hierarchy — platform tools (Legacy Contact / IAM) override will language; "a generic grant of authority to an executor is not sufficient"; without explicit language executors may get "catalog" metadata but not content [sourced: https://www.ament.law/blog/digital-assets-estate-planning-pennsylvania/ and https://www.hellosunset.com/blog/rufadaa-digital-assets-executor-guide, 2025-2026]. Since only 12% of US adults report Facebook/Google account-level controls (T&W 2026), the large majority of accounts have no platform-level designee; for Apple accounts the published fallback in the U.S. is a court order [sourced: support.apple.com/digital-legacy]. The share of *decedents* (as opposed to adults) with a designee set, and the share of those with written instructions that are honoured, are [unknown]. Legal fees for obtaining such an order: [unknown] — attempts at nolo.com (403), legalzoom.com (404), findlaw.com (404), trustandwill.com probate-cost pages (404 ×3).

**Interpretation:** Bereavement is the most acute version of the problem (irreversible loss, legal friction, single-heir rule at Apple), but it is *episodic* and the buyer is the heir, after the fact. A product that only helps after death faces the same problem Apple does: the account owner has to set it up beforehand, and most don't.

### Q1(c) Cross-platform households (iPhone + Android)

- Google Photos Partner Sharing: "You can use partner sharing with one person at a time"; sharing is "All photos" or "Only photos containing selected people"; the help page now documents a toggle "Include content from other Android apps" ("Photos and videos backed up from other Android apps to Google Photos are also shared") [sourced: https://support.google.com/photos/answer/7378858, undated, fetched 2026-11-03]. Background: a Nov 2024 change had restricted partner sharing to camera captures, and the toggle was reported "in development" in Jan 2025 [sourced: https://www.androidpolice.com/google-photos-might-fix-this-frustrating-partner-sharing-restriction/, 2025-01-08]. The toggle's presence in Google's current help page indicates it shipped; ship date [unknown].
- Apple iCloud Shared Photo Library: creator "provides iCloud storage for all of the content"; up to five invited participants; "All participants have equal permissions to add, edit, and delete content"; "You can belong to one shared library at a time" [sourced: https://support.apple.com/HT213248 (en-ae/118229 mirror), undated, via search snippets]. Apple-only.
- **Falsification evidence (platforms closing the gap):** On 2026-06-08 Apple announced iCloud Shared Albums updates to "allow friends and family on Android and Windows to join and contribute photos more conveniently" and "add photos at full-resolution with no compression for the first time" (via iCloud.com) [sourced: https://www.macrumors.com/2026/06/08/apple-brings-icloud-shared-albums-to-android/, 2026-06-08]. Pre-update, Android recipients saw "Shared albums are not available for this device" [sourced: https://geeksontour.com/2023/02/how-to-share-an-iphones-photo-album-with-a-non-iphone-user/, 2023-02]. Shared Album cap: 5,000 items; "Shared Album content isn't automatically backed up" [sourced: https://support.apple.com/en-is/108314, undated].
- **User-satisfaction evidence for Partner Sharing (sought as A3 counter-evidence):** HN comments: "Partner sharing, Face tagging, adding photos to albums based on faces.. these things are great." [sourced: https://news.ycombinator.com/item?id=36351864, 2023-06-16]; "For me the key feature is partner sharing." [sourced: https://news.ycombinator.com/item?id=27339588, 2021-05-31]; the limit is the recurring complaint: "You can only have one account configured this way though, so choose your real partner or a backup account." [sourced: https://news.ycombinator.com/item?id=24970052, 2020-11-02]; "its "partner" sharing feature (limited to just 1 partner)" [sourced: https://news.ycombinator.com/item?id=25061192, 2020-11-11]. Google Photos App Store rating: 1.6M ratings, 4.8/5 (not feature-specific) [sourced: https://apps.apple.com/us/app/google-photos-backup-edit/id962194608, accessed 2026-11-03].
- Pain evidence: Apple Community 2022-05-14 asked to "Make photo library available to all family members, e.g. have a single unified family album"; replies: Photos Library "is a single-user database that can't be shared over a network"; workarounds (external drive passed around, or a dedicated Apple ID); third-party options "about $150 per month for up to 10 users"; no solution, poster filed it as Apple feedback [sourced: https://discussions.apple.com/thread/253896284, 2022-05-14].

**Interpretation:** Share-with-partner is solved on each platform in a one-to-one way and users like it; *cross-platform merged library* is not solved, but Apple's June 2026 move and Google's restored app-content toggle show the gap narrowing at the album/partner level. A3 is weakened, not refuted, here.

### Q1(d) Families with boxes of prints (scanning services)

Prices (primary vendor pages unless noted):
- Legacybox kits: Starter $69.98 (up to 2 items), Family $319.98 (10), Closet $639.98 (20), Trunk $1,249.98 (40), Vault $2,499.98 (80); an "item" is a tape, reel, or set of 25 photos; "Over 2 million families have trusted Legacybox with their memories" [sourced: https://legacybox.com/, fetched 2026-11-03]. The page carried a "BLACK FRIDAY STARTS NOW: Every tape, $8" banner ("Was $27.50. Now $8."), but **no kit shows a crossed-out or regular price**, so whether the kit prices are list or sale is [unknown]; the /products/family-kit page returns 404. Implied per-photo at Family kit: $319.98 / (10×25) = $1.28/photo [estimated: displayed kit price ÷ (items × 25 photos); understated if the displayed price is promotional].
- EverPresent: prints "$0.68 for scans 200+", first 200 at "$0.98", delicate "$1.99 per scan", album pages "$2.99 per page", "A one-time $50 service fee applies to all orders"; organizing services are quote-only [sourced: https://everpresent.com/pricing/, undated].
- Memories Renewed: photos "85¢ each", album photos $1.25–$2.50, 35mm negatives "$1.00 each frame", slides "$1.00 each", VHS "$30 each", "$50 Complex Check-In Fee for Large Unorganized Collections" [sourced: https://www.memoriesrenewed.com/pricing, undated].
- iMemories: photo scanning "$ .99 per photo After savings: 49¢" (code SAVE50), videotapes "$29.99 per tape After savings: $14.99" [sourced: https://www.imemories.com/pricing, fetched 2026-11-03].
- Walgreens Photo ("Home Movies + Prints Digitization"): Photos "Starting at $29.99", Videotapes "Starting at $34.99", Film Reels "Starting at $29.99", HD Videos "Starting at $29.99"; per-item rates not shown; fulfilment partner not named [sourced: https://photo.walgreens.com/store/transfer-vhs-to-dvd, fetched 2026-11-03]. Walgreens' detailed "Photo Products Pricing" article sits behind a login (wagcco.my.site.com). CVS: not attempted (search budget exhausted) — [unknown].
- ScanCafe and ScanMyPhotos pricing pages returned HTTP 403 to the crawler (scanmyphotos.com and blog.scanmyphotos.com both 403 on the repair pass). Secondary roundups put ScanCafe at ~$0.48/image and ScanMyPhotos at ~$0.09–0.19/photo in prepaid boxes (e.g., ~1,800 photos for $169 on sale) [sourced: https://kinphotos.com/blog/scanning-services-comparison and https://pixoneye.com/best-photo-scanning-service/, 2026; secondary only].
- Costco: in-store photo centers closed 2021; online photo service later discontinued [sourced: https://heirloom.cloud/blogs/blog/costco-photo-is-gone-here-s-the-better-way-to-digitize-your-memories, undated; secondary]. costcophotocenter.com does not resolve from this session (host not in network allowlist), so closure could not be confirmed from a Costco page.
- Photomyne (TASE: PHTM, scanning app): revenue 2021 $12.32M, 2022 $16.16M, 2023 $13.33M, 2024 $13.05M, **2025 $17.01M (+30.39%)** [sourced: https://stockanalysis.com/quote/tlv/PHTM/revenue/, 2026; aggregator of TASE filings]. Photomyne's site claims only "Millions of stories scanned and saved" with no figure; its investor page lists Hebrew-language reports (H1 2026, 2025, H1 2025 ...) whose PDFs did not yield extractable text [sourced: https://photomyne.com/ and https://photomyne.com/investors, accessed 2026-11-03]. Photos-scanned count: [unknown].
- Legacybox revenue: [unknown] (private; no filing; third-party revenue guesses exist but none is sourced and none is reproduced here).
- Volumes: Legacybox "2 million families" is the only public cumulative volume figure; ScanMyPhotos' advertised totals could not be read (403); no vendor publishes photos-scanned counts for 2025.

**Interpretation:** This is the one segment with clear, recurring, out-of-pocket spend: hundreds to low thousands of dollars per family, one-time, with prices from ~$0.49 (iMemories promo) to ~$1.28 (Legacybox kit) per print. But the product bought is *digitization*, and the output is a USB/ZIP that then gets dumped into Google/Apple Photos — the "merge" step after scanning is unpriced and unserved by scanners.

### Q1(e) Professional photo organizers

- The Photo Managers: "Founded in 2009", "Formerly known as the Association of Personal Photo Organizers (APPO)"; contact address "7901 4th Street N, Suite 300, St Petersburg, FL 33702, US"; links to five national sites (Canada, Australia, UK, Brazil, Netherlands); no member count or rename date on the About page [sourced: https://thephotomanagers.com/about/, accessed 2026-11-03]. Professional membership "$599 / year" or "$175 / quarter" (compare page) and "$649 RENEWS ANNUALLY" / Plus "$799 INITIAL PAYMENT" (membership page — two prices live on site simultaneously); in-training "$299"; certification $399 list / $199 first-year [sourced: https://thephotomanagers.com/compare-memberships/, https://thephotomanagers.com/membership/, https://thephotomanagers.com/certification/, 2026]. Member count: [unknown] — the site says "a community of professionals"; the only secondary figure found is "hundreds" in a Gaylord profile [sourced: https://info.gaylord.com/resources/meet-the-org-the-photo-managers, undated; secondary]; the member directory pages (/find-a-photo-manager/, /directory/) return 404 and directory.thephotomanagers.com does not resolve, so the listed-member count could not be counted.
- Rates: "Typical rates range from $50 to $100 per hour, with low overhead costs" (association article, "attributed to survey data from members") [sourced: https://thephotomanagers.com/turning-picture-keeper-skills-into-a-professional-photo-management-business, 2026-04-14]. Individual pricing pages: $85/hr or $75/hr prepaid [sourced: https://www.organizedimages.com/pricing/, undated]; $140/hr sliding to $110/hr with $280 two-hour minimum [sourced: https://www.tidy.haus/digital-photo-organizing, undated]; $785 package for 5 hours plus kit [sourced: https://www.decluttereddigital.com/photo-organizing-pricing, undated]; scan-only $0.75/item, scan+organize $1.50/item [sourced: organizedimages.com, undated]. One certified organizer: "photo organizing projects for families typically start around $1500" [sourced: https://signaturephotoorganizing.com/, undated].
- Software they use: association article names "Adobe Lightroom" and "SmugMug" [sourced: thephotomanagers.com article above, 2026-04-14]. Association blog, 2026-10-13, names "Apple Photos, Mylio Photos, Lightroom, and Google Photos" as the AI-organizing tools [sourced: https://thephotomanagers.com/how-to-organize-photos-with-ai-and-find-your-favourite-memories/, 2026-10-13]. An organizer's blog says FOREVER "is often the solution clients choose", best for "25 to 100 GB", drawback "no AI search beyond facial recognition" [sourced: https://www.arrangewanderfocus.com/blog/photo-organizing-software-spotlight-forever, undated]. Mylio exhibits at RootsTech and markets "consolidates your scattered family photos, videos, and documents into one stunning, cloud-independent library" [sourced: https://www.familysearch.org/to/rootstech/expohall/mylio, undated]. Mylio pricing page shows no prices (offer buttons only) [sourced: https://mylio.com/pricing/, 2026-11-03].
- FOREVER permanent storage (one-time): 10GB $179.99, 100GB $899.99, 1TB $5,999.99, 2TB $10,999.99; "guaranteed for your lifetime plus 100 years" backed by a "FOREVER Guarantee Fund" (percentage undisclosed) [sourced: https://www.forever.com/storage, 2026-11-03].
- Client mix (organizers' own descriptions, secondary): "people who've inherited decades of photos from their parents" and "helping a family member downsize" [sourced: https://photoarchivers.com/, undated]; "middle-aged women and downsizing seniors make up the majority of clients" [sourced: https://www.cbc.ca/news/canada/edmonton/professional-photo-managers-edmonton-share-tips-1.6284573, 2021-12; page returns 403, quote from search snippet only — treat as unverified].
- What they say they lack (association's own words, 2026): "Learning how to organize digital photos can feel impossible when your collection is scattered everywhere." "You may have pictures on phones, computers, memory cards, old drives, and cloud services." — recommended fix is Apple Photos (Mac) or Google Photos + separate duplicate software (PC) [sourced: https://thephotomanagers.com/how-to-organize-digital-photos-when-theyre-everywhere/, 2026-09-08]. On AI: "Facial recognition groups photos of people who appear throughout your collection." "However, you still need to review those suggestions and identify unfamiliar relatives." "Similar-looking relatives may be confused, and automatic groupings still need checking." [sourced: thephotomanagers.com AI post, 2026-10-13]. Other 2026 blog titles: "How to Save Money on Photo Cloud Storage Without Losing Your Photos" ("Cloud storage fees can add up, especially when your photos are spread across several services", 2026-09-29) [sourced: https://thephotomanagers.com/blog/, accessed 2026-11-03]. No member survey of software gaps was found; podcast page returns 404: [unknown].

**Interpretation:** This is a real channel of unknown size (the only count is a secondary "hundreds"), charging $50–140/hr to do by hand exactly the merge/dedupe/face-tag job the seed idea automates. The association's own 2026 content frames the client problem as "scattered everywhere" across devices and clouds and recommends single-vendor consumer tools plus manual review — i.e., no tool they recommend does cross-account merge with cross-generation face identification. They are both a potential customer (tooling) and a distribution channel.

### Q1(f) Divorce / separation

- A specialist service exists ("Divorce Photo Help — Everyone Keeps Every Memory"; neutral third party does "the exports, the scanning, the organizing, and the delivery"; both spouses get identical copies; quote after discovery call, no prices listed) [sourced: https://photopossible.com/blog/how-to-divide-photos-in-divorce.html, 2026-03-22]. Its stated failure modes: "Turning off sharing without a plan can mean photos disappear from one person's device"; on Google, "Disconnect the account and you might lose access to years of images you assumed were 'yours.'"; "pictures of your kid's first steps" "might only exist on your ex's old iPhone".
- Apple: creator alone can remove participants or delete the Shared Library; the person who created it supplies all storage [sourced: https://support.apple.com/en-lk/123926, undated].
- Apple Developer Forums, Oct 2022: a couple with "41,160 photos & 4,354 videos" stuck on "Deleting Shared Library" / "Leaving Shared Library"; "Please tell me my photos are not lost nor unrecoverable"; 13 other participants reported the same, durations "4 months", "exactly 6 months"; Apple support "advised to archive their photos and videos offline as a precaution"; last activity May 2024, "no confirmed, broadly applicable fix" [sourced: https://developer.apple.com/forums/thread/716724, 2022-10 to 2024-05]. MacRumors forum: "roughly 20,000 of 50,000 copied images moved back to the private library, and the rest were stuck"; "Apple support had 8 or 9 similar cases documented" [sourced: https://forums.macrumors.com/threads/shared-photo-library-risky.2359656/, 2022-09 to 2023-01].
- Divorce volume × photo-split incidence: [unknown]. No survey found.

**Interpretation:** Acute, legally motivated, and currently served by one-off human services at quote-only prices. Small but high-intent; also a strong argument that *shared* libraries (Apple's answer) are not a *merged, owned* archive — they create a new single point of failure.

### Q1(g) Adult children consolidating parents' libraries

- Apple Community, 2025-11-19: "I have one photo library A in an external drive connected to my iCloud account." "I have another photo library B on the external drive that used to be connected to my husband's iCloud account" "How can I get the rest of his photos from iCloud onto library B and then merge the two A & B so it's one library?" Replies: back up first; export/re-import "loses metadata such as albums and keywords"; PowerPhotos (~$40) to merge; Photos duplicate finder "a little flaky"; Shared Library objections: "Album and folder structure is not shared", "Any participant can edit metadata or delete", and the poster "doesn't want to pay for rarely viewed archives" in iCloud [sourced: https://discussions.apple.com/thread/256192786, 2025-11-19].
- Apple Community, 2021-03-22: user wants to "take all her photos and move it to MY account"; prescribed path: download originals on Mac, keyword-tag, copy library to external drive, set as System Library, merge via iCloud; "the merge can take days"; poster: stuck, "didn't want to damage his photos"; thread closed [sourced: https://discussions.apple.com/thread/252584800, 2021-03-22].
- Apple Community, 2019-05-13: "Data from one account can not be 'merged' into another account." [sourced: https://discussions.apple.com/thread/250361584, 2019-05-13].
- Hacker News, "Ask HN: What is your system for backing up family photos and video?", 2022-01-18: "Because Apple has't solved what everyone ask — a way for two or more users to merge Photos" [sourced: https://news.ycombinator.com/item?id=29981774, 2022-01-18]; same thread: "How to access/merge other apple photo accounts?" (reply from a startup founder: what is "missing in most photo backup tools" is that "they're primarily archival and aren't designed to tie ephemera together into a permanent catalog") [sourced: https://news.ycombinator.com/item?id=29979071, 2022-01-18]. HN 2024-09-26: "I see that there are some guides on how to use Photos Takeout data and merge it back into something useful," [sourced: https://news.ycombinator.com/item?id=41653754, 2024-09-26].
- Google side: no account merge exists; Partner Sharing is "one person at a time" [sourced: https://support.google.com/photos/answer/7378858]. Takeout omits other contributors' photos in shared albums: "given the shared albums have photos contributed by other people, those aren't in the Takeout archive" (immich discussion OP, 2024-12-04); workaround posted 2025-10-12 requires each contributor to export separately; 2026-09-12 report that partner-shared photos still fail [sourced: https://github.com/immich-app/immich/discussions/14477, 2024-12 to 2026-09]. Hacker News 2023-10-30: "your Shared albums will only contain pictures that you yourself added!"; "Google Takeout just flat out fails every time I try it."; "Some files will only be available at reduced quality and have all metadata stripped" [sourced: https://news.ycombinator.com/item?id=38065002, 2023-10-30].
- Google Photos Community (support.google.com/photos/community): two listing queries ("merge accounts", "transfer all photos to another account") surfaced only device-migration and export-loss threads (e.g. "Exported my account. Saved everything to my device and now it's gone." [sourced: https://support.google.com/photos/thread/475876404, "Updated: Today" per listing, accessed 2026-11-03]); the listing shows recent threads only and does not expose a true search, so absence here is not evidence of absence.
- Size of this segment: [unknown]. Proxy: 48% of US adults have >1,000 phone photos; 1 in 5 feel overwhelmed (Mixbook, n>2,400, as cited by CNBC) [sourced: https://www.cnbc.com/2026/02/28/cloud-storage-prices-apple-icloud-google-snap-shutterfly.html, 2026-02-28].

**Interpretation:** This is where the technical pain is most concrete and most repeated across years (2019, 2021, 2022, 2025 Apple threads and 2022–2024 HN comments say the same thing). It is not yet evidence of *payment*: the only money changing hands in these threads is ~$40 for PowerPhotos.

### Q1(h) New parents — FamilyAlbum (MIXI) and Tinybeans (ASX: TNY)

**FamilyAlbum / Mitene (MIXI, TSE 2121):**
- Lifestyle segment FY2026 (year to March 2026): "net sales increased by 16.0% to 17.1 billion yen"; "achieved full-year positive EBITDA"; "FamilyAlbum now has around 30 million users", "with an MAU of 12 million as of May 2026" [sourced: https://mixi.co.jp/en/ir/message/, 2026]. Growth credited to "FamilyAlbum Premium, photo prints, GPS Guardian, and advertising". Premium subscriber count: [unknown] (not disclosed on the fetched page; MIXI's IR library pages — /ir/docs/results/, /ir/docs/data/, /ir/docs/earnings/, /ir/finance/highlight/ — load their document lists dynamically and returned no links to the crawler; the Integrated Report 2025 PDF exceeds the 10 MB fetch limit and was **not read**).
- FY2025 (year to March 2025) Lifestyle net sales ≈ ¥14.7B [estimated: ¥17.1B ÷ 1.160, from the FY2026 figure and its stated +16.0% growth]. The earlier draft's "Lifestyle = 26.0% of ¥154,847M → ¥40.3B" came from a search excerpt of the unread Integrated Report and is withdrawn: it is irreconcilable with the verified ¥17.1B (+16%), so the 26% must refer to a differently defined metric or segment, or was mis-excerpted.
- Users: "surpassed 30 million" on 2026-05-07; "overseas users account for more than 40%"; North America ~20%; used by "65% as of December 2024" of new parents in Japan (vs MHLW births); "175 countries and regions" [sourced: https://babytech.jp/en/2026/05/mixi-2/, 2026-05-14; press-release relay].
- Pricing (verified on FamilyAlbum's own site): Premium One "$2.99 USD/month" (subscriber only); Premium Family "$5.99 USD/month" or "$59 USD/year"; Premium Family Pro "$10.99 USD/month" or "$109 USD/year"; first month free for first-time subscribers. Family Pro is the tier that adds "Organize Photos/Videos With Tags (Admins Only)", "Search Features" and "Bulk Downloading" [sourced: https://family-album.com/en/premium, fetched 2026-11-03]. (The help-center article cited earlier returns 403; the memorymurals.com secondary for the $2.99 tier is no longer needed.)
- ARPU: ¥17.1B / 12M MAU = ¥1,425/MAU/yr [estimated: FY2026 segment sales ÷ May-2026 MAU]; ≈ US$9.5/MAU/yr [estimated: ¥1,425 ÷ assumed ¥150/USD; the exchange rate is an assumption, not sourced this round — at ¥140 it is $10.2, at ¥160 it is $8.9]. The segment includes GPS Guardian and prints, so this overstates FamilyAlbum-only ARPU.

**Tinybeans (ASX: TNY), all USD:**
- FY25 (to 30 Jun 2025): revenue $4.820M (−11%); subscription revenue/ARR $3.323M (+12%); advertising $1.264M; photobook $103K; GP margin 87%; opex $6.626M (−33%); adjusted EBITDA −$1.443M [sourced: https://announcements.asx.com.au/asxpdf/20250821/pdf/06n4m9jjp1zr87.pdf, 2025-08-21]. KPI slide: "51K" paid subscribers, "$355" LTV, "$75" ARPU, "0.86M" MAU, "93%" retention rate, "61%" DAU/WAU, "93% Recommend TB"; "Churn reduced by 33% since FY24"; "ARPU up +40% since FY23" [sourced: same]. Definitions: ARPU = "Average monthly subscription revenue / number of Tinybeans+ subscribers"; retention = "% of Tinybeans+ subscribers with a paid subscription from start to end of month" [sourced: same, glossary].
- **KPI reconciliation warning (these vendor KPIs do not reconcile):** (i) ARPU is defined as *monthly* revenue per subscriber, yet "$75" equals the $74.99 *annual* plan price, so it is evidently annual ARPU despite the glossary; (ii) 93% monthly retention implies ~7% monthly churn [estimated: 100% − 93%] and an expected paid life of ~14 months [estimated: 1 ÷ 0.07], whereas LTV $355 ÷ annual ARPU $75 ≈ 4.7 years [estimated]; the two cannot both hold unless "retention" is measured on a different base (e.g. annual-plan renewals) than the glossary states. The previously cited "7% monthly churn per management on earnings call" rested on a search snippet of a 404 page and is withdrawn; 7% is retained only as the arithmetic complement of the 93% KPI.
- Plans: Tinybeans free (5GB, ad-supported); Tinybeans+ $74.99/yr (2 accounts, 200GB); Tinybeans+ Family $119.99/yr (6 accounts, 1TB, launching FY26); Tinybeans+ Legacy $39.99/yr (2 accounts, 200GB, "Reminiscing child 5+ years") [sourced: FY25 results PDF above, 2025-08-21]. Strategy slide positions a move from "Niche photo sharing" to "Multigenerational memory preservation" with "Cross-generational access" and "AI-powered photo management" [sourced: same].
- Tinybeans' own survey ("How Moms share & save memories", April 2025, n=600): "67% of US moms plan to buy a physical photo product in the next 12 months" [sourced: same PDF, citing internal survey; survey itself not published].
- Q3 FY26 (to 31 Mar 2026): revenue $1.79M (+86%); subscription $1.45M (+87%, 81% of revenue); first EBITDA-positive quarter ($8K); "~95k paid subscribers across both platforms" after Qeepsake acquisition (Nov 2025); Tinybeans ARPU $75, retention 95%; Qeepsake ARPU $64, retention 79%; Qeepsake CAC $35; "~1 million active families worldwide" [sourced: https://investorpa.com/announcement-pdf/20260428/285467.pdf, 2026-04-28].
- Q4 FY26 and FY26 full year: the primary documents exist — ASX announcements list "Quarterly Activities/Appendix 4C Cash Flow Report" released 28/07/2026 (13 pages, price sensitive), "Appendix 4E and Annual Report" and "FY26 Results Presentation" released 27/08/2026, a further "Quarterly Activities/Appendix 4C Cash Flow Report" (Sept 2026 quarter) released 28/10/2026, and "Appointment of Tracy Cho as Chief Executive Officer" 14/07/2026 [sourced: https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=TNY&timeframe=D&period=M6, accessed 2026-11-03]. Their PDFs sit behind ASX's access-terms gate (displayAnnouncement.do returns the terms page to the crawler; investors.tinybeans.com renders no listing; marketindex/listcorp 403), so the figures remain secondary: Q4 FY26 revenue $1.81M, "approximately 93,000 paid subscribers", subscription revenue +45% YoY [sourced: https://kalkine.com.au/news/announcements/tinybeans-reports-record-e-commerce-growth-and-third-consecutive-quarter-of-operating-cash-inflows, 2026-07; secondary; page now 403 — unverified]. If the secondary figure is right, paid subscribers fell from ~95k (Q3) to ~93k (Q4), a −2% quarter [estimated: 93 ÷ 95 − 1], which would be the first sequential decline since the Qeepsake acquisition and is worth checking against the primary 4C.
- **Directly relevant quote:** "Tinybeans has commenced development work for its AI-driven photo organisation tools, including automated content tagging and the creation of smart albums. These features target the number-one job that parents told us they would pay for: photos that are organised and findable without difficulty." [sourced: Q3 FY26 report above, 2026-04-28].

**Interpretation:** New-parent apps prove consumers pay ~$36–120/yr for private family photo sharing at scale (FamilyAlbum ¥17.1B segment with ~12M MAU; Tinybeans ~$75 annual ARPU on ~95k subs). Retention is *claimed* high (93–95% monthly) but the KPIs do not reconcile with the stated LTV, so this file does not treat them as proof of durable WTP. Both companies are explicitly moving toward "multigenerational" and "AI organisation", which is both validation of demand and evidence for A4-style incumbent risk. Neither offers cross-account *merge* of existing Apple/Google libraries; they are forward-looking capture apps.

### Q2. What they do today and what they pay (table)

| Segment | Current solution | Price paid | Frequency | Evidence |
|---|---|---|---|---|
| Genealogists | Ancestry / MyHeritage subscription; photos attached to tree persons; MyHeritage standalone Photo subscription; FamilySearch Memories (free) | Ancestry ≈ $20–25/mo (U.S. Discovery) or $35–40/mo (World Explorer) per App Store IAP [estimated from IAP lines]; MyHeritage: [unknown] (prices computed in-account; 5 pages tried); FamilySearch $0 | Monthly/6-month/annual subs | apps.apple.com id349554263; myheritage.com/help articles 13130253/12852235/12852240; familysearch.org help |
| Bereaved heirs | Apple Digital Legacy request (court order in US) / Google deceased-user request; or nothing | $0 to platform; legal fees [unknown] (nolo/legalzoom/findlaw/T&W pages unreachable) | Once | support.apple.com/digital-legacy; support.google.com/accounts/troubleshooter/6357590 |
| Cross-platform couples | Google Partner Sharing (one partner; app-content toggle now documented), iCloud Shared Albums (Android-joinable via iCloud.com, Jun 2026), WhatsApp/text | $0 (plus storage plans: Google 200GB $4.99/mo since Feb 2025) | Continuous | support.google.com/photos/answer/7378858; macrumors.com 2026-06-08; cnbc.com 2026-02-28 |
| Boxes of prints | Mail-in scanning: Legacybox kits $69.98–$2,499.98; EverPresent $0.68–0.98/print + $50 fee; Memories Renewed $0.85/print; iMemories $0.99 ($0.49 promo)/print; Walgreens "starting at $29.99"; Photomyne app | ~$0.09 (secondary, ScanMyPhotos) to $1.28/photo; typical family order $300–$1,250 [estimated: Legacybox Family–Trunk displayed kit prices; may be promotional] | Once (sometimes repeated per batch) | legacybox.com; everpresent.com/pricing; memoriesrenewed.com/pricing; imemories.com/pricing; photo.walgreens.com; stockanalysis.com PHTM |
| Pro photo organizers | Lightroom, SmugMug, FOREVER, Mylio, Apple/Google Photos; hands-on hourly | $50–$140/hr; projects "start around $1500"; FOREVER storage $179.99 (10GB) to $10,999.99 (2TB) one-time | Per project | thephotomanagers.com; organizedimages.com; tidy.haus; forever.com/storage |
| Divorcing couples | Export everything before leaving shared library; neutral third-party service | Quote-only | Once | photopossible.com 2026-03-22; support.apple.com 123926 |
| Adult children consolidating | Mac Photos import/merge, PowerPhotos (~$40), Google Takeout + immich-go / scripts | ~$0–$40 software; many hours | Once, often abandoned | discussions.apple.com/thread/256192786; github immich #14477; HN 29981774 |
| New parents | FamilyAlbum Premium One $2.99/mo, Family $5.99/mo ($59/yr), Family Pro $10.99/mo ($109/yr); Tinybeans+ $74.99/yr, Family $119.99/yr, Legacy $39.99/yr | $36–$132/yr | Annual; claimed 93–95% monthly retention (Tinybeans; see reconciliation warning) | family-album.com/en/premium; Tinybeans FY25 & Q3 FY26 ASX filings |
| Pre-need digital legacy (reference point) | Everplans Premium | $99.99/yr | Annual | everplans.com/pricing |

### Q3. Willingness to pay

- **Direct proof of consumer spend on family-memory software:** FamilyAlbum Lifestyle segment ¥17.1B (FY2026) [sourced: mixi.co.jp IR message, 2026]; Tinybeans subscription revenue US$3.32M FY25 with ARPU $75 and LTV $355 (KPIs do not reconcile; see Q1(h)) [sourced: TNY FY25 ASX, 2025-08-21]; Photomyne revenue $17.01M 2025 [sourced: stockanalysis.com PHTM, 2026].
- **Photo books / physical products as proxy:** Shutterfly is private (Apollo); Snapfish has been part of the same private entity since the Shutterfly–Snapfish merger "completed" 2020-01-08 (Apollo's 2019 deals for both were "valued at about $3 billion combined"); Snapfish revenue was "less than $100 million" when HP bought it for $300M in 2005 (uncited clause in Wikipedia) and no later Snapfish revenue is public [sourced: https://en.wikipedia.org/wiki/Snapfish, accessed 2026-11-03; secondary]. Snapfish 2024–25 revenue: [unknown]. Shutterfly Inc.'s corporate site states no revenue, customer or order counts [sourced: https://www.shutterflyinc.com/, ©2026]. A third-party *modeled* estimate puts shutterfly.com online sales at "$936.8M in 2025, down 5-10%" [sourced: https://gripsintelligence.com/insights/retailers/shutterfly.com, 2026; modeled estimate, not a filing — the precision is spurious; use only as "order of magnitude: high hundreds of $M"]. Shutterfly offers "unlimited free photo storage, sharing, and downloading" to accounts with an order every 18 months; inactive accounts' photos "will be archived, not deleted" [sourced: cnbc.com 2026-02-28]. Tinybeans cites a "$3.8B" US physical-photo-products market "growing 4.6% annually" from Verified Market Research (Mar 2025) [sourced: TNY FY25 PDF; third-party market report, not verifiable here]. Mixbook's own claims: "6 million+ happy Mixbookers", "20 million+ projects printed" [sourced: https://www.mixbook.com/inspiration/states-that-phlush-away-memories, 2023-05-16; vendor claim]. Photo-book market sizes from research-report vendors range $3.6B–$5.1B for 2025 and are not reliable [sourced: growthmarketreports.com, dataintelo.com, 2025; low quality].
- **Storage spend:** ~70% of Apple customers use iCloud storage (CIRP via CNBC) [sourced: cnbc.com 2026-02-28]; Google 200GB rose from $2.99 to $4.99/mo in Feb 2025 [sourced: same].
- **Digital legacy WTP:** No survey found that prices a digital-legacy service (goodtrust.com returns a bot-verification page; Pew/Statista/Morning Consult could not be searched this pass). Price reference point: Everplans Premium "$99.99/year" (free tier "Stores up to three items") [sourced: https://www.everplans.com/pricing, accessed 2026-11-03]. Attitude signals: 79% say protecting digital assets is important (BMT 2024); 12% have account-level controls (T&W 2026). WTP for legacy specifically: [unknown].
- **Photo-organization WTP survey:** Tinybeans states organised/findable photos is "the number-one job that parents told us they would pay for" (Q3 FY26) but publishes no numbers. Mixbook 2023 (n=1,967 smartphone owners, fielded May 2–8 2023): average "3,139 pictures and videos"; "55% have felt overwhelmed"; "63% of people say they take multiple pictures of the same thing"; "Half of the respondents say they do nothing with the photos and videos they take"; "80% of people have pictures or videos on their phones that they haven't looked at since the day they took them"; "58% say that only 50% or less of the pictures and videos in their camera roll are so important" [sourced: mixbook.com, 2023-05-16; vendor survey]. No independent survey of dollars spent on photo organization was found: [unknown].

### Q4. Forum evidence (verbatim, by URL — see Q1 sections for full context)

| Date | Source | Quote (verbatim) |
|---|---|---|
| 2025-11-19 | https://discussions.apple.com/thread/256192786 | "How can I get the rest of his photos from iCloud onto library B and then merge the two A & B so it's one library?" |
| 2024-01-15 | https://discussions.apple.com/thread/255414530 | "I would be devastated if the hundreds of memories stored on his cloud are lost" |
| 2022-10 | https://developer.apple.com/forums/thread/716724 | "Please tell me my photos are not lost nor unrecoverable." (41,160 photos stuck between personal and Shared Library) |
| 2022-05-14 | https://discussions.apple.com/thread/253896284 | "Make photo library available to all family members, e.g. have a single unified family album" |
| 2022-01-18 | https://news.ycombinator.com/item?id=29981774 | "Because Apple has't solved what everyone ask — a way for two or more users to merge Photos" |
| 2022-01-18 | https://news.ycombinator.com/item?id=29979071 | "How to access/merge other apple photo accounts?" |
| 2021-03-22 | https://discussions.apple.com/thread/252584800 | wants to "take all her photos and move it to MY account" — stuck, closed unresolved |
| 2019-05-13 | https://discussions.apple.com/thread/250361584 | reply: "Data from one account can not be 'merged' into another account." |
| 2024-12-04 | https://github.com/immich-app/immich/discussions/14477 | "given the shared albums have photos contributed by other people, those aren't in the Takeout archive" |
| 2024-09-26 | https://news.ycombinator.com/item?id=41653754 | "I see that there are some guides on how to use Photos Takeout data and merge it back into something useful," |
| 2023-10-30 | https://news.ycombinator.com/item?id=38065002 | "your Shared albums will only contain pictures that you yourself added!"; "Google Takeout just flat out fails every time I try it." |
| 2022-09/2023-01 | https://forums.macrumors.com/threads/shared-photo-library-risky.2359656/ | ~20,000 of 50,000 images moved back, rest stuck; "Apple support had 8 or 9 similar cases documented" (paraphrase) |
| 2026 (inferred) | https://community.familysearch.org/en/discussion/192372/... | "I selected all my gallery images (~1700) and tried to copy them all to one folder." "Failed with no error message." |
| 2021-01 | https://community.familysearch.org/en/discussion/comment/215626 | "feel overwhelmed" / "you will NEED to know the People in the Photographs; BEFORE, they can even be 'Uploaded'" |

Counter-evidence of *no* pain (searched for, as required): Apple Community threads also include a Community Specialist steering users to Shared Library as "the easiest way"; MacRumors posters say "creating the library and day-to-day use worked well" and problems "mainly arose when leaving or deleting". HN users call Partner Sharing "great" and "the key feature" (2021, 2023, URLs in Q1(c)); the only recurring complaint is the one-partner limit. So for *two-person, same-platform, ongoing* sharing, the platforms are adequate and liked; the pain concentrates on (i) historical merge, (ii) >2 people / >1 platform, (iii) exit/death/divorce.

Reddit (r/DataHoarder, r/selfhosted, r/Genealogy, r/photography) and Google Photos Community: Reddit is unreachable from this session (both reddit.com hosts refused; search-engine snippet route unavailable because the search budget was exhausted); Google Photos Community listings were queried twice and show only recent device/export threads (see Q1(g)).

### Q5. Search-volume signals

- Google Trends and keyword-tool volumes for "merge google photos accounts", "transfer photos from google to icloud", "scan old photos", "family photo archive": [unknown]. Attempts this pass: Google Trends explore page → HTTP 429; Ahrefs free Keyword Generator page is a client-side app that shows no volumes without interaction/login (page text contains no keyword figures) [sourced: https://ahrefs.com/keyword-generator/, accessed 2026-11-03]; Semrush, Keywords Everywhere and Google Ads Keyword Planner require accounts; no page publishing these volumes was found.
- Indirect signal (qualitative only): the query "merge google photos accounts" is served by multiple commercial how-to pages from cloud-transfer vendors (MultCloud, Wondershare InClowdz) and tech sites (ScreenRant, Zapier, TechPP, cbackup, PicBackMan) that monetize exactly this query — a prior-round search listing; URLs were not retained, so no count is asserted.

---

## 3. Seed assumptions tested

### A3 — "There exists a customer segment for whom merged multi-relative archive is an acute, paid-for pain."

**Status: PARTIAL.**

Evidence FOR:
- Pain is acute and durable: the same unresolved "merge two accounts / unify family library" threads recur on Apple Community in 2019, 2021, 2022, 2025, on HN in 2022–2024, and on GitHub 2024–2026; Apple's and Google's own docs confirm no account merge exists and Takeout drops other contributors' photos.
- Adjacent paid behaviors exist: scanning ($300–$1,250 per family order at displayed prices), pro organizers ($50–140/hr, projects from ~$1,500), FOREVER permanent storage ($900 for 100GB), new-parent subscriptions ($36–$132/yr), MyHeritage's standalone Photo subscription, genealogy subs at ~$20–40/month.
- A listed company (Tinybeans) says organised/findable photos is "the number-one job that parents told us they would pay for" and is repositioning to "multigenerational memory preservation" with "cross-generational access"; the professional organizers' association frames the client problem in 2026 as photos "scattered everywhere" across devices and clouds.

Evidence AGAINST (falsification attempts):
- No one has been found paying specifically for *merge*. The money in the merge threads is ~$40 (PowerPhotos). Scanners sell digitization, organizers sell labor, FamilyAlbum/Tinybeans sell forward capture; none sells cross-account consolidation as a product with a known price.
- Platforms are closing the sharing gap and users like what exists: Apple extended iCloud Shared Albums to Android/Windows with full-resolution contributions (2026-06-08); Google restored app-content partner sharing via a documented toggle; iCloud Shared Photo Library handles up to 6 people on-platform; HN users call Partner Sharing "great" / "the key feature". For the modal nuclear family on one platform, "shared albums are fine" is a defensible position.
- Bereavement/divorce pain is real but episodic, and only ~12% set up (Facebook/Google) account-level legacy controls, which suggests low *pre-need* willingness to act even when the cost is zero.
- The strongest "consumers pay for family photos" datapoints (Tinybeans retention/LTV) are internally inconsistent vendor KPIs; the secondary Q4 FY26 figure, if correct, shows paid subscribers slipping ~2% quarter-on-quarter.
- Segment sizes for (e), (f), (g) are unknown; no survey quantifies them.

Net: a segment exists (inherited collections, multi-household families, pro organizers' clients), the pain is acute at specific life events, and adjacent spend is proven, but "paid-for" is not yet demonstrated for the merge itself. The strongest testable wedge from this track is **pro photo organizers and their downsizing / inherited-box clients**, because money already flows there and the manual job is the automation target.

No other seed assumptions were in this track's brief (A1, A2, A4, A5, A6 belong to other tracks); A4 is touched indirectly: Tinybeans' and MIXI's roadmaps (AI organisation, multigenerational), Apple's June 2026 Shared Albums change and Google's partner-sharing toggle are incumbent-motion evidence.

---

## 4. Numbers table

| Number | Tag |
|---|---|
| Ancestry 3.8M+ subscribers (same figure in 2022-baseline and 2025 columns) | [sourced: ancestrycdn Impact Report 2026] |
| Ancestry 29M+ DNA customers; 71B+ records; 145M+ trees | [sourced: same] |
| Ancestry 42 PB data storage (2025), 24 PB baseline | [sourced: same, SASB table] |
| Ancestry company-facts: "more than 3 million paying subscribers", "over 30 million" DNA, "150 million" trees, "over 1 billion user generated photos, scanned documents and written stories" | [sourced: ancestry.com company-facts, ©2026, undated; conflicts with IR figures] |
| Ancestry IAP: U.S. Discovery $19.99 / $24.99; World Explorer $34.99 / $39.99; single record $1.99; 659K ratings, 4.8★ | [sourced: apps.apple.com id349554263, accessed 2026-11-03; billing period not labelled] |
| Ancestry ≈ $20–25/mo and $35–40/mo | [estimated: reading of the IAP lines above] |
| MyHeritage 1M annual subscribers (milestone undated), 58M trees, 9.6M DNA, 520 employees | [sourced: myheritage.com/about-myheritage, undated] |
| MyHeritage 75M registered users (2013); 80M (2015); Francisco Partners ~$600M (early 2021, reported) | [sourced: en.wikipedia.org/wiki/MyHeritage, secondary citing TechCrunch / Jewish News] |
| MyHeritage Basic 250 people / 500 MB; Premium 2,500 people / 1,000 MB; Data "40 billion" records; Photo plan 20 LiveMemory videos/yr; Omni 30/yr | [sourced: myheritage.com/help article 13130253] |
| MyHeritage USD prices | [unknown] |
| MyHeritage +450M records Sep 2026; +530M Oct 2025 | [sourced: blog.myheritage.com 2026-10-06, 2025-11] |
| FamilySearch 297M visits 2025; +163M tree persons; 467M sources | [sourced: familysearch.org year-in-review-2025, 2026-01-07] |
| FamilySearch Memories >5,000 items may load slowly; album display limit 1,000; batch failures ~400–500 | [sourced: familysearch.org help; community thread 192372] |
| Apple Legacy Contact: age 13 or older; iOS 15.2+ | [sourced: support.apple.com/102631] |
| Apple: only one person may request a deceased account; US requires court order | [sourced: support.apple.com/digital-legacy] |
| Google IAM: up to 10 contacts; deletion after ≥2 years inactivity | [sourced: support.google.com/accounts/answer/3036546] |
| T&W 2026: n=5,000; ±1.4pp; 48% no digital instructions; 21% formal; 12% account-level controls (Facebook/Google); Gen Z 23% / Boomers 4%; 12% "digital life among most meaningful" | [sourced: trustandwill.com 2026 report, updated 2026-06-29] |
| BMT 2024: n=1,500; 76% little/no knowledge; 39% never heard; 79% important; 30% >30,000 files; 53% of will-holders specify digital assets; MoE ±4% | [sourced: bmt.com survey, 2024-12] |
| Probate / court-order legal fees | [unknown] |
| Google Partner Sharing: one partner at a time; app-content toggle documented | [sourced: support.google.com/photos/answer/7378858, fetched 2026-11-03] |
| iCloud Shared Photo Library: up to 5 invitees (6 total); creator pays storage | [sourced: support.apple.com HT213248 / 123926] |
| iCloud Shared Album cap 5,000 items | [sourced: support.apple.com/108314] |
| Google 200GB $2.99 → $4.99/mo (Feb 2025) | [sourced: cnbc.com 2026-02-28] |
| ~70% of Apple customers use iCloud storage (CIRP) | [sourced: cnbc.com 2026-02-28, secondary] |
| Google Photos iOS: 1.6M ratings, 4.8★ | [sourced: apps.apple.com id962194608, accessed 2026-11-03] |
| Legacybox kits $69.98 / $319.98 / $639.98 / $1,249.98 / $2,499.98 (displayed; no compare-at price shown); tapes "Was $27.50. Now $8."; 25 photos per item; "over 2 million families" | [sourced: legacybox.com, fetched 2026-11-03] |
| Legacybox ~$1.28/photo at Family kit | [estimated: $319.98 ÷ 250; understated if displayed price is promotional] |
| EverPresent $0.68 (200+), $0.98 first 200, $1.99 delicate, $2.99 album page, $50 service fee | [sourced: everpresent.com/pricing] |
| Memories Renewed $0.85/photo, $1.00 slide/negative, $30 VHS, $50 complex check-in | [sourced: memoriesrenewed.com/pricing] |
| iMemories $0.99/photo (49¢ with SAVE50); tapes $29.99 ($14.99) | [sourced: imemories.com/pricing, fetched 2026-11-03] |
| Walgreens: photos "Starting at $29.99"; videotapes $34.99; film reels $29.99; HD videos $29.99 | [sourced: photo.walgreens.com/store/transfer-vhs-to-dvd, fetched 2026-11-03] |
| CVS scanning prices | [unknown] |
| ScanCafe ~$0.48/image; ScanMyPhotos ~$0.09–0.19/photo | [sourced: kinphotos.com, pixoneye.com 2026; secondary — vendor pages 403] |
| Photomyne revenue 2021 $12.32M; 2022 $16.16M; 2023 $13.33M; 2024 $13.05M; 2025 $17.01M (+30.39%) | [sourced: stockanalysis.com PHTM] |
| Photomyne photos scanned; Legacybox revenue; ScanMyPhotos volume | [unknown] |
| Photo Managers: founded 2009; formerly APPO; St Petersburg FL address; 5 international sites | [sourced: thephotomanagers.com/about/] |
| Photo Managers: $599/yr or $175/qtr; $649 renew; $799 Plus; $299 training; cert $399/$199 | [sourced: thephotomanagers.com pages] |
| Photo Managers member count | [unknown] (secondary "hundreds": info.gaylord.com) |
| Organizer rates $50–$100/hr (association); $85/$75; $140→$110 + $280 min; $785/5hr package; projects "start around $1500"; $0.75 scan / $1.50 scan+organize | [sourced: thephotomanagers.com 2026-04-14; organizedimages.com; tidy.haus; decluttereddigital.com; signaturephotoorganizing.com] |
| FOREVER storage: 10GB $179.99 … 100GB $899.99 … 1TB $5,999.99 … 2TB $10,999.99 | [sourced: forever.com/storage] |
| Third-party family-library apps "about $150 per month for up to 10 users" (forum claim) | [sourced: discussions.apple.com/thread/253896284, 2022; unverified claim in a reply] |
| PowerPhotos ~$40 | [sourced: discussions.apple.com/thread/256192786, 2025 reply; approximate] |
| Shared-library stuck case: 41,160 photos + 4,354 videos; 13 others; durations up to 6 months | [sourced: developer.apple.com/forums/thread/716724] |
| MacRumors: ~20,000 of 50,000 moved back; Apple support "8 or 9 similar cases" | [sourced: forums.macrumors.com thread 2359656] |
| MIXI Lifestyle FY2026 net sales ¥17.1B (+16.0%); FamilyAlbum ~30M users; 12M MAU (May 2026) | [sourced: mixi.co.jp/en/ir/message/] |
| MIXI Lifestyle FY2025 ≈ ¥14.7B | [estimated: ¥17.1B ÷ 1.16] |
| FamilyAlbum >30M users 2026-05-07; >40% overseas; N. America ~20%; 65% of Japanese new parents; 175 countries | [sourced: babytech.jp 2026-05-14] |
| FamilyAlbum ARPU ≈ ¥1,425/MAU/yr ≈ US$9.5 | [estimated: ¥17.1B ÷ 12M MAU; ÷ assumed ¥150/USD] |
| FamilyAlbum Premium One $2.99/mo; Family $5.99/mo or $59/yr; Family Pro $10.99/mo or $109/yr | [sourced: family-album.com/en/premium, fetched 2026-11-03] |
| Tinybeans FY25: revenue $4.820M; subs $3.323M; ads $1.264M; photobook $103K; GM 87%; opex $6.626M; adj. EBITDA −$1.443M | [sourced: ASX 2025-08-21 PDF] |
| Tinybeans FY25 KPIs: 51K paid subs; $75 ARPU; $355 LTV; 0.86M MAU; 93% retention; 61% DAU/WAU; 93% recommend | [sourced: same; KPIs do not reconcile — see Q1(h)] |
| Tinybeans implied monthly churn ~7%; implied paid life ~14 months; LTV/ARPU ≈ 4.7 years | [estimated: 100% − 93%; 1 ÷ 0.07; $355 ÷ $75] |
| Tinybeans plans: $0 / $74.99 / $119.99 / $39.99 per year | [sourced: same PDF] |
| Tinybeans survey Apr 2025 n=600: 67% of US moms plan physical photo purchase | [sourced: same PDF, internal survey] |
| US physical photo products $3.8B, +4.6%/yr | [sourced: Verified Market Research via Tinybeans PDF; third-party report, unverified] |
| Tinybeans Q3 FY26: revenue $1.79M (+86%); subs $1.45M (81%); EBITDA +$8K; ~95K paid subs; TB ARPU $75 / retention 95%; Qeepsake ARPU $64 / retention 79% / CAC $35; ~1M active families | [sourced: investorpa.com Q3 FY26 PDF, 2026-04-28] |
| Tinybeans ASX filings: 4C 28/07/2026 (13 pp); 4E + Annual Report and FY26 Results Presentation 27/08/2026; 4C 28/10/2026; CEO appointment 14/07/2026 | [sourced: asx.com.au announcements listing, accessed 2026-11-03; PDFs not readable] |
| Tinybeans Q4 FY26: revenue $1.81M; ~93,000 paid subs; subs rev +45% | [sourced: kalkine.com.au 2026-07; secondary; now 403 — unverified] |
| Tinybeans paid subs ~−2% Q3→Q4 FY26 | [estimated: 93k ÷ 95k − 1; depends on unverified secondary] |
| Everplans Premium $99.99/yr | [sourced: everplans.com/pricing, accessed 2026-11-03] |
| Snapfish: HP paid $300M (2005), revenue then "<$100M" (uncited); Apollo deals ~$3B combined (2019); merger completed 2020-01-08 | [sourced: en.wikipedia.org/wiki/Snapfish; secondary] |
| Snapfish revenue 2024–25 | [unknown] |
| Shutterfly.com 2025 online sales ~$936.8M (−5–10%) | [sourced: gripsintelligence.com; modeled estimate — order of magnitude only] |
| Mixbook: "6 million+ happy Mixbookers", "20 million+ projects printed" | [sourced: mixbook.com 2023-05-16; vendor claim] |
| Photo-book market $3.6B–$5.1B (2025) | [sourced: growthmarketreports.com / dataintelo.com; low-quality research-report vendors] |
| Mixbook 2023: n=1,967; fielded May 2–8 2023; 3,139 photos avg; 55% overwhelmed; 63% multiple shots; 50% do nothing; 80% have never re-viewed some; 58% say ≤half matter | [sourced: mixbook.com 2023-05-16] |
| Mixbook (CNBC-cited): n>2,400; 48% >1,000 photos; 1 in 5 overwhelmed | [sourced: cnbc.com 2026-02-28] |
| Search volumes for the four target queries | [unknown] |
| Apple Legacy Contact adoption; Google IAM adoption | [unknown] |
| Divorce photo-split incidence | [unknown] |

---

## 5. Unknowns we could not resolve

1. Monthly search volumes for "merge google photos accounts", "transfer photos from google to icloud", "scan old photos", "family photo archive" — Trends 429; Ahrefs free tool is client-side; paid tools require login; no published figures.
2. Number of Apple users with a Legacy Contact set, and Google users with Inactive Account Manager configured — not disclosed; only the T&W 12% proxy (Facebook/Google, all adults).
3. The Photo Managers' membership count (directory pages 404) and any member survey of software gaps (podcast page 404).
4. Ancestry web plan prices by term (only App Store IAP lines); MyHeritage USD prices (computed in-account; five pages tried); MyHeritage 2025–26 registered-user count.
5. FamilySearch Memories upload counts; share of genealogists who manage photos outside the tree; r/Genealogy evidence (Reddit blocked).
6. Legacybox revenue, whether displayed kit prices are list or promotional, and annual order volume; ScanCafe / ScanMyPhotos primary pricing and volume claims (403); Photomyne photos-scanned count (Hebrew PDFs not extractable).
7. CVS print-scanning prices; Walgreens per-photo rate (pricing article behind login); Costco closure from a Costco page (host not resolvable).
8. FamilyAlbum Premium subscriber count and premium revenue split (MIXI IR document lists load dynamically; Integrated Report >10 MB, unread).
9. Tinybeans Q4 FY26 and FY26 full-year primary figures (ASX PDFs gated); whether the ~93k subscriber figure and the implied −2% quarter are right.
10. Any survey quantifying dollars households spend on photo organization, or WTP for a digital-legacy service; Snapfish revenue.
11. Size of the divorce/separation and adult-child-consolidation segments; no incidence data.
12. Estate-attorney fees for a court order to access a decedent's Apple/Google account (four legal-fee sources unreachable).
13. Reddit threads (r/DataHoarder, r/selfhosted, r/Genealogy, r/photography) — crawler blocked and search budget exhausted; equivalent evidence substituted from Apple/HN/GitHub/FamilySearch forums.

---

## 6. Full source list (accessed 2026-11-03)

Primary / near-primary:
1. https://cmsasset.ancestrycdn.com/content/dam/Impact-Report-2026/Ancestry_IR_2026_FullReport.pdf — Ancestry 2025 Impact Report (2026)
2. https://www.ancestry.com/corporate/about-ancestry/company-facts — Ancestry company facts (©2026, undated)
3. https://apps.apple.com/us/app/ancestry-family-history-dna/id349554263 — Ancestry App Store listing (IAP prices)
4. https://www.myheritage.com/about-myheritage — MyHeritage about page (©2026; counts undated)
5. https://www.myheritage.com/help/en/articles/13130253-what-types-of-subscriptions-does-myheritage-offer — MyHeritage plan types
6. https://www.myheritage.com/help/en/articles/12852235-how-much-does-a-data-subscription-cost and https://www.myheritage.com/help/en/articles/12852240-how-much-does-a-family-site-upgrade-cost — MyHeritage price articles (no prices)
7. https://blog.myheritage.com/ — MyHeritage blog index (record-count posts 2025-11, 2026-10)
8. https://www.familysearch.org/en/blog/familysearch-year-in-review-2025 — FamilySearch 2025 year in review (2026-01-07)
9. https://www.familysearch.org/en/help/helpcenter/article/how-many-memories-photos-stories-documents-and-audio-files-can-i-upload — FamilySearch help
10. https://www.familysearch.org/en/help/helpcenter/article/my-gallery-in-memories-is-too-full — FamilySearch help
11. https://education.myheritage.com/article/myheritage-photo-features/ — MyHeritage photo features (2025)
12. https://support.apple.com/en-us/102631 — Apple Legacy Contact
13. https://support.apple.com/digital-legacy — Apple: request access to a deceased family member's account
14. https://support.google.com/accounts/answer/3036546 — Google Inactive Account Manager
15. https://support.google.com/accounts/troubleshooter/6357590 — Google: deceased user's account
16. https://support.google.com/photos/answer/7378858 — Google Photos Partner Sharing (fetched 2026-11-03; documents app-content toggle)
17. https://support.apple.com/HT213248 (and https://support.apple.com/en-lk/123926) — iCloud Shared Photo Library
18. https://support.apple.com/en-is/108314 — Apple Shared Albums
19. https://trustandwill.com/learn/estate-planning-report-2026 — Trust & Will 2026 Estate Planning Report (fielded Jan–Feb 2026; updated 2026-06-29)
20. https://www.bmt.com/news-insights-events/bryn-mawr-trust-survey/ — Bryn Mawr Trust / Opinium survey (Dec 2024)
21. https://legacybox.com/ — Legacybox pricing (fetched 2026-11-03)
22. https://everpresent.com/pricing/ — EverPresent pricing
23. https://www.memoriesrenewed.com/pricing — Memories Renewed pricing
24. https://www.imemories.com/pricing — iMemories pricing (fetched 2026-11-03)
25. https://photo.walgreens.com/store/transfer-vhs-to-dvd — Walgreens Home Movies + Prints Digitization (fetched 2026-11-03)
26. https://stockanalysis.com/quote/tlv/PHTM/revenue/ — Photomyne (TASE) revenue 2021–2025
27. https://photomyne.com/ and https://photomyne.com/investors — Photomyne site / investor report list
28. https://thephotomanagers.com/about/ — The Photo Managers about page
29. https://thephotomanagers.com/membership/ ; https://thephotomanagers.com/compare-memberships/ ; https://thephotomanagers.com/certification/ — membership and certification pricing
30. https://thephotomanagers.com/turning-picture-keeper-skills-into-a-professional-photo-management-business — rates $50–100/hr (2026-04-14)
31. https://thephotomanagers.com/how-to-organize-digital-photos-when-theyre-everywhere/ — association blog (2026-09-08)
32. https://thephotomanagers.com/how-to-organize-photos-with-ai-and-find-your-favourite-memories/ — association blog (2026-10-13)
33. https://thephotomanagers.com/blog/ — association blog index
34. https://www.organizedimages.com/pricing/ ; https://www.tidy.haus/digital-photo-organizing ; https://www.decluttereddigital.com/photo-organizing-pricing ; https://signaturephotoorganizing.com/ — organizer pricing pages
35. https://www.forever.com/storage — FOREVER permanent storage pricing
36. https://mylio.com/pricing/ — Mylio pricing page (no prices shown)
37. https://www.familysearch.org/to/rootstech/expohall/mylio — Mylio RootsTech exhibitor page
38. https://photopossible.com/blog/how-to-divide-photos-in-divorce.html — divorce photo-division service (2026-03-22)
39. https://announcements.asx.com.au/asxpdf/20250821/pdf/06n4m9jjp1zr87.pdf — Tinybeans FY25 results presentation (2025-08-21)
40. https://investorpa.com/announcement-pdf/20260428/285467.pdf — Tinybeans Q3 FY26 quarterly report (2026-04-28)
41. https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=TNY&timeframe=D&period=M6 — ASX announcements listing for TNY (titles/dates only; PDFs gated)
42. https://mixi.co.jp/en/ir/message/ — MIXI president's message, FY2026 Lifestyle segment
43. https://babytech.jp/en/2026/05/mixi-2/ — FamilyAlbum 30M users (2026-05-14; press-release relay)
44. https://family-album.com/en/premium — FamilyAlbum Premium pricing (fetched 2026-11-03)
45. https://www.everplans.com/pricing — Everplans pricing
46. https://www.mixbook.com/inspiration/states-that-phlush-away-memories — Mixbook survey (2023-05-16)
47. https://www.cnbc.com/2026/02/28/cloud-storage-prices-apple-icloud-google-snap-shutterfly.html — CNBC (2026-02-28)
48. https://www.macrumors.com/2026/06/08/apple-brings-icloud-shared-albums-to-android/ — MacRumors (2026-06-08)
49. https://www.androidpolice.com/google-photos-might-fix-this-frustrating-partner-sharing-restriction/ — Android Police (2025-01-08)
50. https://www.shutterflyinc.com/ — Shutterfly Inc. corporate site (no figures)
51. https://apps.apple.com/us/app/google-photos-backup-edit/id962194608 — Google Photos App Store listing

Forum / public-post evidence:
52. https://discussions.apple.com/thread/256192786 — Apple Community (2025-11-19)
53. https://discussions.apple.com/thread/252584800 — Apple Community (2021-03-22)
54. https://discussions.apple.com/thread/250361584 — Apple Community (2019-05-13)
55. https://discussions.apple.com/thread/253896284 — Apple Community (2022-05-14)
56. https://discussions.apple.com/thread/255414530 — Apple Community (2024-01-15)
57. https://developer.apple.com/forums/thread/716724 — Apple Developer Forums (2022-10 to 2024-05)
58. https://forums.macrumors.com/threads/shared-photo-library-risky.2359656/ — MacRumors Forums (2022-09 to 2023-01)
59. https://github.com/immich-app/immich/discussions/14477 — immich discussion (2024-12 to 2026-09)
60. https://news.ycombinator.com/item?id=38065002 — Hacker News (2023-10-30)
61. https://news.ycombinator.com/item?id=29981774 and https://news.ycombinator.com/item?id=29979071 — Hacker News, "Ask HN: What is your system for backing up family photos and video?" (2022-01-18)
62. https://news.ycombinator.com/item?id=41653754 — Hacker News (2024-09-26)
63. https://news.ycombinator.com/item?id=36351864 ; https://news.ycombinator.com/item?id=27339588 ; https://news.ycombinator.com/item?id=24970052 ; https://news.ycombinator.com/item?id=25061192 — Hacker News comments on Partner Sharing (2020–2023), located via https://hn.algolia.com/api/v1/search
64. https://community.familysearch.org/en/discussion/comment/215626 — FamilySearch Community (2021-01)
65. https://community.familysearch.org/en/discussion/192372/what-are-the-limits-on-folders-of-images-and-or-total-size-mbytes — FamilySearch Community (2026, year inferred)
66. https://community.familysearch.org/en/categories/memories — FamilySearch Community Memories category listing
67. https://support.google.com/photos/thread/475876404 — Google Photos Community (listing, accessed 2026-11-03)
68. https://community.adobe.com/t5/lightroom-classic-discussions/beginner-workflow-for-scanned-photos/m-p/10435335 — Adobe Community (undated)

Secondary (used only where primary unavailable, flagged inline):
69. https://en.wikipedia.org/wiki/MyHeritage — MyHeritage user counts 2007–2015, 2021 acquisition (citing TechCrunch etc.)
70. https://en.wikipedia.org/wiki/Snapfish — Snapfish ownership history
71. https://kalkine.com.au/news/announcements/tinybeans-reports-record-e-commerce-growth-and-third-consecutive-quarter-of-operating-cash-inflows — Tinybeans Q4 FY26 summary (2026-07; now 403; unverified)
72. https://kinphotos.com/blog/scanning-services-comparison — scanning price comparison (2026)
73. https://pixoneye.com/best-photo-scanning-service/ — scanning price comparison (2026)
74. https://heirloom.cloud/blogs/blog/costco-photo-is-gone-here-s-the-better-way-to-digitize-your-memories — Costco closure (undated)
75. https://gripsintelligence.com/insights/retailers/shutterfly.com — Shutterfly sales estimate (2026; modeled)
76. https://www.arrangewanderfocus.com/blog/photo-organizing-software-spotlight-forever — organizer on FOREVER
77. https://photoarchivers.com/ — organizer client description
78. https://www.cbc.ca/news/canada/edmonton/professional-photo-managers-edmonton-share-tips-1.6284573 — CBC (2021-12; 403 on fetch, snippet only — unverified)
79. https://info.gaylord.com/resources/meet-the-org-the-photo-managers — Gaylord profile of TPM ("hundreds")
80. https://geeksontour.com/2023/02/how-to-share-an-iphones-photo-album-with-a-non-iphone-user/ — pre-2026 Android limitation (2023-02)
81. https://www.ament.law/blog/digital-assets-estate-planning-pennsylvania/ — RUFADAA guidance (law-firm blog)
82. https://www.hellosunset.com/blog/rufadaa-digital-assets-executor-guide — RUFADAA guidance (2026)

Removed from the source list this pass (not read, or no longer relied on): help.family-album.com article (403; replaced by family-album.com/en/premium); finance.yahoo.com TNY earnings-call page (404; churn claim withdrawn); pdf.irpocket.com MIXI Integrated Report 2025 (never read; derived figure withdrawn); memorymurals.com (superseded by primary).

Fetch failures logged this pass (for reproducibility): ancestry.com/offers (400); ancestry.com/cs/offers/subscribe (nav only); help.ancestry.com search (no prices); myheritage.com/plans (404); App Store MyHeritage id417558742 (404); Google Play listings (truncated/404); scanmyphotos.com and blog (403); scancafe.com (403, prior round); legacybox.com/products/family-kit (404); costcophotocenter.com (DNS not allowed); wagcco.my.site.com pricing article (login); photomyne H1-2025 PDF (no extractable text); mixi.co.jp IR library pages (dynamic, no links); pdf.irpocket.com (>10 MB); ASX displayAnnouncement.do (terms gate); investors.tinybeans.com (empty); marketindex.com.au / listcorp.com (403); thephotomanagers.com/podcast/, /find-a-photo-manager/, /directory/ (404); directory.thephotomanagers.com (DNS); community.familysearch.org/en/search (403); discussions.apple.com/search (no results rendered); reddit.com (blocked); trends.google.com (429); nolo.com (403); legalzoom.com, findlaw.com, trustandwill.com probate pages (404); goodtrust.com (bot check).

---

## Audit log

Each auditor finding and what was done (file edited in place; structure kept; sourced material that passed was retained).

**Untagged numbers**
1. L28 Wikipedia "75M at 2021 acquisition" — Fetched en.wikipedia.org/wiki/MyHeritage: 75M is a 2013 figure (TechCrunch), 80M in 2015; the 2021 event is the Francisco Partners acquisition (reported $600M). Rewritten with URL, dates and [sourced: … secondary] tag.
2. L75 Legacybox "$16M–$100M" — Range deleted; revenue now [unknown] with a note that unsourced third-party guesses are not reproduced.
3. L82 "founder interviews say thousands" — Removed (no URL). Member count is [unknown]; only the Gaylord "hundreds" (secondary, URL) remains.
4. L82 founding/renaming/HQ/sites bundled under pricing sources — Fetched thephotomanagers.com/about/: "Founded in 2009", "Formerly known as … (APPO)", St Petersburg FL address, five international sites confirmed; rename year not on the page → stated as not given. Re-tagged to the About URL.
5. L117 yen→USD rate unstated — Now "[estimated: ¥1,425 ÷ assumed ¥150/USD]" with sensitivity at ¥140 and ¥160; rate flagged as an assumption.
6. L120 "7% churn per earnings call" — Withdrawn as a sourced claim; retained only as [estimated: 100% − 93%] with the implied ~14-month life and the LTV/ARPU contradiction spelled out.
7. L52 "multiple threads … mostly unresolved" from a search-result set — Claim withdrawn and replaced with an explicit note; Apple Community search page rendered no results.
8. L250 Mixbook 80% not in body — Re-fetched mixbook.com: "80% of people have pictures or videos on their phones that they haven't looked at since the day they took them" confirmed; now quoted in the Q3 body and the table (plus the 63% duplicate-shot figure and fielding dates).
9. L89 "a few hundred to a few thousand practitioners" — Rewritten as "a channel of unknown size (the only count is a secondary 'hundreds')".

**Suspect claims**
1. MIXI ¥40.3B (major) — Deleted. Replaced with FY2025 Lifestyle ≈ ¥14.7B [estimated: ¥17.1B ÷ 1.16]; the Integrated Report is now stated as unread and the 26% excerpt as irreconcilable/withdrawn. MIXI IR library pages were re-tried (results, data, earnings, highlight) and return no document links to the crawler.
2. Tinybeans 7% churn / 93–95% retention as WTP proof (major) — Added a "KPI reconciliation warning" paragraph (monthly-ARPU definition vs $74.99 annual price; 93% monthly retention ⇒ ~14-month life vs LTV/ARPU ≈ 4.7 years). Interpretation and A3 sections now say retention is "claimed" and not treated as proof of durable WTP.
3. MyHeritage "1M subscribers (2021)" — Re-fetched about page: milestone carries no year. Body and table now say "milestone undated".
4. Ancestry 3.8M in both SASB columns; company-facts 3M/30M/150M — Both caveats added to Q1(a) and the numbers table.
5. Partner Sharing toggle "in development" (stale) — Re-fetched Google's help page: the "Include content from other Android apps" toggle is now documented ("Photos and videos backed up from other Android apps to Google Photos are also shared"); file says it shipped, ship date unknown.
6. Legacybox "Black Friday pricing" — Re-fetched: kits show no compare-at/was price (only tapes do: "Was $27.50. Now $8."); list-vs-sale status now [unknown] and the per-photo and typical-order estimates are flagged "understated if promotional". /products/family-kit → 404.
7. FamilyAlbum prices (403 help article) — Verified on family-album.com/en/premium: Premium One $2.99/mo; Family $5.99/mo or $59/yr; Family Pro $10.99/mo or $109/yr; first month free. Secondary memorymurals.com dropped. Q2 range updated to $36–$132/yr.
8. Tinybeans Q4 FY26 via kalkine (403) — Primary ASX listing fetched: confirms the 28/07/2026 Appendix 4C, 27/08/2026 4E/Annual Report/FY26 presentation, 28/10/2026 4C and 14/07/2026 CEO appointment; the PDFs are gated (ASX terms page; markitdigital CDN ids did not map to TNY), so the Q4 figures stay secondary and are labelled unverified. The ~95k → ~93k (−2%) decline is now stated and flagged.
9. Shutterfly $936.8M; Snapfish missing — Estimate kept but demoted to "order of magnitude only, precision spurious"; Snapfish added (Wikipedia ownership history, 2005 "<$100M" uncited clause, 2019 Apollo ~$3B combined, 2020-01-08 merger; 2024–25 revenue [unknown]); shutterflyinc.com fetched (no figures).
10. Apple Legacy Contact "over 13" — Corrected to "13 or older".
11. "88% of estates" — Removed both occurrences and the numbers-table row; replaced with wording limited to what T&W measures (12% of US adults, Facebook/Google) plus [unknown] for decedents and for honoured written instructions.

**Broken or misquoted sources**
- help.family-album.com (403) → replaced by family-album.com/en/premium (verified).
- kalkine.com.au (403) → kept as secondary/unverified; primary ASX listing added; PDFs gated.
- finance.yahoo.com TNY call (404) → removed; churn claim withdrawn.
- pdf.irpocket.com MIXI Integrated Report → removed from sources; marked unread; derived figure withdrawn.
- myheritage.com/about-myheritage "2021" → corrected to undated.
- cbc.ca (403) → kept but labelled "snippet only — unverified".
- Wikipedia 75M and "founder thousands" → the former now has a URL and dates; the latter removed.
- Sources the auditor verified as stated were left untouched.

**Missing vs brief**
- Q1(a) prices: Ancestry App Store IAP lines obtained (U.S. Discovery $19.99/$24.99; World Explorer $34.99/$39.99); web plan page 400 / nav-only / help search no prices → term prices [unknown]. MyHeritage: plan structure and three help articles fetched; prices are computed in-account → [unknown], five attempts logged. MyHeritage sells a standalone Photo subscription (new finding).
- Q1(a) forum pain: added FamilySearch Memories category listing and thread 192372 (1,000-item album limit, silent batch failures); search endpoints (FamilySearch search, Reddit) blocked — stated.
- Q1(a) MyHeritage user count: about page, blog index and Wikipedia tried; current count still [unknown]; 2013/2015 counts given with URL.
- Q1(b) Legacy Contact / IAM adoption: no fetchable primary; stated [unknown] with attempts (search budget exhausted).
- Q1(d) Walgreens: primary page fetched ("Photos starting at $29.99"); detailed pricing behind login; CVS not attempted → [unknown]; iMemories primary prices added; Costco host not resolvable.
- Q1(d) volumes: ScanMyPhotos site/blog 403; Photomyne site ("Millions of stories") and investor PDFs tried (no extractable text) → [unknown].
- Q1(e) what they lack: association blog posts 2026-09-08 and 2026-10-13 quoted (scattered-everywhere framing; AI face grouping "still need checking"); podcast 404; no member survey → [unknown].
- Q1(e) membership size: About page and three directory URLs tried → [unknown].
- Q1(h) FamilyAlbum churn/Premium subs: MIXI IR pages re-tried (dynamic) → [unknown], stated.
- Q3 Snapfish: added (see above). Shutterfly: corporate site fetched; estimate demoted.
- Q3 surveys: goodtrust blocked; Everplans $99.99/yr price point added; surveys still [unknown] with attempts listed.
- Q4 Reddit / Google Photos Community: Reddit unreachable; Google Photos Community listing queried twice (only device/export threads, URL cited); HN Algolia API used to add four new HN posts (2022–2024) with verbatim quotes.
- Q5 search volumes: Trends (429) and Ahrefs free tool (client-side, no figures) tried → [unknown]; the "nine SEO pages" count removed (URLs not retained).
- Q2 table: genealogist price row now carries Ancestry IAP-derived ranges and the MyHeritage attempts; legal-fee cell records four failed sources; Everplans reference row added.
- A3 falsification: added Partner Sharing satisfaction evidence (HN 2021/2023 "great" / "key feature"; one-partner limit as the complaint) and Google Photos 1.6M-rating/4.8 context; A3 remains PARTIAL.
