# Gap track R8 — Family historians as the paying segment

Written 2026-11-03; repaired 2026-11-03 after audit (see "Audit log" at the end). All URLs accessed 2026-11-03 unless a page date is given. Builds on `customers.md` Q1(a), `competitive.md` Q6 and `pro-channel.md` (APG); where a number was first sourced there, the originating URL is repeated inline. Reddit evidence comes from the arctic-shift archive of r/Genealogy (posts quoted by URL, date and score only; no usernames). Archive behaviour this session: 11 queries were sent in the first pass and 6 returned `{"error":"Timeout. Maybe slow down a bit"}` [sourced: https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=Genealogy, responses captured 2026-11-03]; on retry with 20-second and then 60-second pauses, "photo restoration", "Photo Tagger" and "photo detective" returned results and are now used in §Q6; "organize photos", "facial recognition" and "unknown relatives photos" timed out on all three attempts [sourced: same endpoint, three attempts 2026-11-03]. The web-search budget for this session was exhausted before the repair pass began, so every repair below rests on direct fetches of known URLs; items that needed discovery rather than verification are marked [unknown] with the attempt recorded.

## 1. Questions asked

1. How big is the paying genealogy population, with provenance (Ancestry, MyHeritage, FamilySearch, Findmypast, Geneanet)?
2. What do family historians already pay, and for what (platform tiers, software, photo tools, societies, DNA, consulting)?
3. What photo features do the platforms ship, and where do they stop (living-people policy, limits, API)?
4. Can a third party read/write photos into a user's tree today (FamilySearch, Ancestry, MyHeritage, Gramps Web)?
5. Where do family historians gather and how do small vendors reach them?
6. What photo-specific pain is visible in forums, and is anyone paying for photo identification?
7. Falsify: are they already satisfied; is the hobby shrinking; is living-relative tagging unwanted?

## 2. Findings per question

### Q1. Market size with provenance

**Ancestry (Blackstone-owned since Dec 2020).** The disclosed figures, in date order:
- Moody's via The Globe and Mail, 2020-08-11 (pre-close): "Ancestry's total revenue declined 1.2 per cent in 2019", partly because of "a 48-per-cent dip in DNA unit sales compared with 2018"; adjusted debt to EBITDA "6.7 times at the end of 2019" [sourced: https://www.theglobeandmail.com/investing/investment-ideas/article-investors-ready-for-up-to-us25-billion-in-debt-for-blackstones/, 2020-08-11]. The article carries no subscriber count.
- Blackstone's 2020 acquisition releases (announcement and completion) could not be read: both blackstone.com URLs return 403 (reproduced 2026-11-03: https://www.blackstone.com/news/press/blackstone-to-acquire-ancestry-leading-online-family-history-business-for-4-7-billion/ and the "completes" release); Ancestry's corporate newsroom index renders no release bodies (https://www.ancestry.com/corporate/newsroom/press-releases) and a guessed Ancestry press URL returned 404. The "3.6 million subscribers" figure that an earlier draft attributed to the 2020 close is therefore **withdrawn**: it rested on a search snippet, and the two primary pages are unreachable. 2020 subscriber count at close: [unknown — attempts above].
- Moody's, 2021-12-13: "Ancestry generated approximately $1.2 billion in revenue" (TTM to 2021-09-30); "a large customer base of approximately 3.8 million subscribers"; family history "approximately 84%" of FY2021 revenue; pro-forma debt/EBITDA "about 6.5x from 6.0x"; free cash flow expected "more than $300 million" over 12–15 months [sourced: https://finance.yahoo.com/news/arches-holdings-inc-moodys-assigns-005705240.html, 2021-12-13 (Moody's rating action reproduced on Yahoo Finance)].
- 2025 Impact Report: "3.8M+ subscribers", same figure in the 2022 baseline column [sourced: https://cmsasset.ancestrycdn.com/content/dam/Impact-Report-2026/Ancestry_IR_2026_FullReport.pdf, via customers.md Q1(a)].
- Reuters, 2025-09-25 (via Private Equity Wire): "Ancestry, which generates more than $1bn in annual revenue and counts over three million paying subscribers"; "A public listing could value Ancestry at around $10bn" [sourced-secondary: https://www.privateequitywire.co.uk/blackstone-explores-sale-or-ipo-of-ancestry-com/, 2025-09-26, "according to a report by Reuters"]. Whether a sale or IPO has since happened: [unknown — no search budget remained in the repair pass; the original pass found nothing in 2026 coverage].
- Company-facts page (live, undated): "More than 3 million paying subscribers" and "Over 1 billion user generated photos, scanned documents and written stories" [sourced: https://www.ancestry.com/corporate/about-ancestry/company-facts, via customers.md].
- Moody's/S&P 2024–2026 rating reports: [unknown — not found in the original pass; no search budget in the repair pass].
- **Reading.** The only point estimates are 3.8M (Moody's, 2021) and "3.8M+" (Ancestry's own 2025 Impact Report, which also shows 3.8M+ for 2022). "Over three million" (Reuters 2025) and "more than 3 million" (company facts) are floors, consistent with 3.8M. Revenue: ~$1.2B TTM 2021 [sourced: Moody's above]; "more than $1bn" 2025 [sourced-secondary: Reuters via PEW above]. Correct statement: **no disclosed growth in subscribers or revenue between 2021 and 2025**, with 2019 revenue down 1.2% on 2018. It is not evidence of decline; it is evidence of a sponsor not disclosing growth.

**MyHeritage (Francisco Partners since Feb 2021).** "serves more than 104 million registered users worldwide"; Jefferies hired for a sale "valuing the company at around $1 billion"; 2021 acquisition "at an estimated valuation of about $600 million" [sourced: https://www.calcalistech.com/ctechnews/article/syr4gmfmzl, 2025-12-24]. Paying subscribers: "surpasses one million annual subscribers" — the milestone is **undated** on the page (it sits after 2021 timeline entries with no year) and "annual subscribers" may mean annual-plan holders rather than all paying users [sourced: https://www.myheritage.com/about-myheritage, via customers.md]. Marketing-page counts (© 2026, undated): "Over 119 million animations and counting!", "7.1 Billion" profiles, "63 Million" family trees, "4.4/5 on Trustpilot (107k reviews)" [sourced: http://www.myheritage.com/deepstory (the /livestory URL 301-redirects here)]. Revenue: [unknown — Calcalist, Globes, ynet and the about page carry no revenue figure]. Headcount: "MyHeritage currently has 500 employees in Israel, the US and Europe"; "about 15% of the company's workforce will be dismissed" [sourced: https://en.globes.co.il/en/article-myheritage-to-lay-off-15-of-workforce-1001548761, 2026-07-08]. The "75 jobs" figure on layoff trackers is 15% × 500, not a company statement [estimated: 0.15 × 500 = 75].

**FamilySearch (free, LDS-funded).** Year in Review 2025 (posted 2026-01-07): "more than 297 million visits in 2025"; "More than 2.2 billion new searchable names and images" added in 2025; total "more than 22.7 billion" names and images; records from "more than 170 countries and principalities"; Family Tree grew by "more than 163 million people" to "1.8 billion searchable people"; "467 million sources" added, "3.9 billion sources in Family Tree"; "more than 6,447 locations worldwide" (FamilySearch centers); Labs testers "tens of thousands of users" [sourced: https://www.familysearch.org/en/blog/familysearch-year-in-review-2025, 2026-01-07]. Registered users and Memories upload count: [unknown — the year-in-review, the about page (https://www.familysearch.org/en/about/, © 2026: "238 countries", "over 5,000 local family history centers", 2020 "average visitors per day is 400,000") and the newsroom publish neither]. RootsTech 2026: "drew millions of people in person and online from 235 countries and territories"; "offered new content in 23 languages"; "an expo hall with more than 200 exhibitors"; "more than 500 sessions and 200 expert-led classes" [sourced: https://www.familysearch.org/en/newsroom/rootstech-2026-highlights, 2026-04-13]. RootsTech 2025: "millions of participants from 235 countries and all 50 states"; "Relatives at RootsTech, had more than 660,000 participants who viewed 6.6 million ancestral relationships" [sourced: https://www.familysearch.org/en/newsroom/rootstech-2025-recap, 2025-04-14]. In-person headcount for either year: [unknown — every official page says "thousands" or "millions" without a number].

**Findmypast (DC Thomson).** Subscribers, revenue and prices: [unknown]. Attempted 2026-11-03: https://www.dcthomson.co.uk/news/ (press items only, no financials; links a brand page for Findmypast); https://www.findmypast.co.uk/subscribe (renders "Choose your subscription" with no plans or prices in the fetched text); https://www.findmypast.com/ (no prices, no subscriber count, no photo features; "Save up to 50%" offer and free trial only). The "about £134m" group-revenue figure in an earlier draft had no URL and is **withdrawn**.

**Geneanet (Ancestry-owned, EU).** "more than 5 million members" per a search snippet of its own site [sourced-secondary: https://en.geneanet.org/, undated, unverified — en.geneanet.org, www.geneanet.org and en.geneanet.org/legal/about/ all returned 403 on 2026-11-03]. Paying share and photo features: [unknown].

**23andMe (adjacent, not photos).** Filed for Chapter 11 in 2025 and has since been sold; this session could not reach a primary (https://investors.23andme.com/ and /news-releases both 403; the guessed release URL 404) [sourced-secondary: review-site mentions only; no URL retrievable this session; background only, not load-bearing].

**Sum of paying platform subscribers.** Ancestry 3.8M [sourced: Moody's 2021 / Impact Report 2025] (floor >3M [Reuters 2025]) + MyHeritage >1M [sourced: about page, undated] + Findmypast [unknown] + Storied [unknown] ≈ **4–5M paying genealogy subscribers worldwide** [estimated: 3.0M floor + 1.0M floor = 4.0M low; 3.8M + 1.0M = 4.8M mid; overlap between the two bases unknown; MyHeritage input is an undated marketing milestone].

### Q2. What family historians already pay

**Platform tiers (primary, fetched 2026-11-03).** Ancestry: U.S. Discovery "$24.99/mo." or "$119.00/6 mo."; World Explorer "$39.99/mo." or "$179.00/6 mo."; All Access "$59.99/mo." or "$269.00/6 mo."; AncestryDNA "$99*", + Traits "$119*" [sourced: https://www.ancestry.com/c/allproducts]. MyHeritage: Photo plan "currently costs only $49.90 per year and is available exclusively on the MyHeritage app"; "Complete subscribers are eligible for a 25% discount on the Photo plan"; "Users with a Photo plan can create 20 LiveMemory™ videos annually" [sourced: https://blog.myheritage.com/2024/11/introducing-livememory-bring-your-photos-to-life-in-video/, 2024-11-21]. Complete "$299/year, with a discount for your first year" [sourced-secondary: https://familytreemagazine.com/websites/myheritage/myheritage-photo-tools/, print version Nov/Dec 2023]. MyHeritage DNA kit: "Only $19.90 was $89 + shipping", bundled with a "30-day Complete free trial" [sourced: https://www.myheritage.com/dna, fetched 2026-11-03; sale price]. MyHeritage Data / Premium / PremiumPlus / Omni current US prices: [unknown — https://www.myheritage.com/subscriptions shows only a "Price list" link to /pricing, which returns 404; /plans and /upgrade 404; /site-upgrade renders empty; all 2026-11-03]. Storied: Essential $19.99/yr, Plus $49.99/yr, Ultimate $99.99/yr; "The free account covers the tree, your stories, photos, and sharing with family, and records are the paid part" [sourced-secondary: https://ancestoriq.com/blog/storied-review/, 2026-08-14; Storied's own pricing page redirects to login (https://storied.com/pricing → auth.storied.com, 307, 2026-11-03); its trial page shows features but no prices: https://storied.com/trial-offers]. Findmypast prices: [unknown — see Q1].

**Desktop software.** RootsMagic 12 "Buy · $39.95", "Upgrade for $29.95", free edition available; "Download your Ancestry tree, photos included" [sourced: https://www.rootsmagic.com/]. Family Tree Maker 2024 (MacKiev): "Single click synchronization with Ancestry.com®"; price [unknown — not on https://www.mackiev.com/ftm/; /ftm/buy.html 404; store.mackiev.com does not resolve from this session; the earlier "~$79.95" had no URL and is withdrawn]. Legacy Family Tree 10: "Download Now (It's Free!)" [sourced: https://legacyfamilytree.com/, fetched 2026-11-03].

**Photo-specific tools.** Vivid-Pix Memory Station: "Home Edition: $249.99", "Pro Edition: $499.99"; transcription "8 cents per minute"; voice text "is automatically placed into the image metadata" [sourced: https://www.vivid-pix.com/memorystationsoftware/]. FOREVER Historian 6: "$159.99 USD"; "will identify 'who's who' in your photos" via Face Tags [sourced: https://www.forever.com/historian]. Epson FastFoto FF-680W: "Our Price: $629.99", "After 16% savings: $529.99" [sourced: https://epson.com/For-Home/Scanners/Photo-Scanners/FastFoto-FF-680W-Wireless-High-speed-Photo-Scanning-System/p/B11B237201]. Photomyne: App Store lines $6.99–$59.99 with only one labelled "(yearly) $59.99" [sourced-secondary: https://photoscanrestore.com/guides/photomyne-cost, updated 2026-09-30]. Related Faces (face-matching for genealogists, listed in FamilySearch's Solutions Gallery): "Six Month $64.99", "Annual $99.00", 14-day trial [sourced: https://relatedfaces.com/]. iMemories (now Ancestry): kit "Only $20*", photos "$0.49 each", "Most orders average $300", "tag family members to your tree" [sourced: https://www.ancestry.com/c/imemories/offer]. Permanent.org (nonprofit archive): "Storage fees are only charged once: $10 per gigabyte of storage"; "Get Started with a FREE GB"; "Original files are never modified and all file metadata is preserved"; Archive Steward and Legacy Contact roles; "Preserve any format"; no tagging feature mentioned on the homepage [sourced: https://www.permanent.org/, fetched 2026-11-03; the /pricing/ path 404s].

**Restoration services (paid, per photo).** MemoryCherish: "starts at $38"; tiers "Experienced Artist: $38", "Head Artist: $58", "Senior Artist: $148" per photo; vendor claim "Trusted by 400,000+ families"; "2,185+ verified reviews"; notes Walgreens discontinued photo restoration in 2024; most recent review dated 2026-10-08 [sourced: https://www.memorycherish.com/, fetched 2026-11-03; customer count is a vendor claim]. Phojoe pricing page 404. This is the second line of evidence (after Maureen Taylor, below) that family historians pay per-photo cash.

**Societies and education.** NGS: Individual "$85" / yr, Family "$105", Youth "$35" [sourced: https://www.ngsgenealogy.org/join-renew-membership/]; member count [unknown — not on the join page, the homepage, or https://www.ngsgenealogy.org/about-ngs/ (404); the "nearly 10,000 (2018)" figure in an earlier draft had no URL and is withdrawn]. Legacy Family Tree Webinars (MyHeritage-owned): membership "$59.95 per year"; library "2,860" webinars; "502" speakers; "Upcoming Live Webinars … View all (23)" [sourced: https://familytreewebinars.com/, © 2026, fetched 2026-11-03]; the library page separately shows "2,553 of 2860 webinars" [sourced: https://familytreewebinars.com/webinar-library]. APG: "more than 2,000 members in forty countries" [sourced: https://www.apgen.org/about_us.php, via pro-channel.md].

**Photo-identification consulting.** The Photo Detective (Maureen Taylor): "One image: $45 (Wednesday mornings)", "Up to Three images: (Save $26) $99 (Friday mornings)", recorded Zoom consultations (the page says "Those fifteen minutes can change your research"; no session length is stated as such); © 2026 [sourced: https://maureentaylor.com/photo-consultation-options/]. Event add-on rate "$25 per photo (usual fee is $45)" [sourced: https://maureentaylor.com/speaking-page/]. Volume [unknown].

**Spend-per-hobbyist surveys.** The widely quoted "$1,000–$18,000 per year" range comes from a ~2012 Global Industry Analysts report whose full text is paywalled and whose top end is unsupported; a photo-restoration company's survey put spend at "about $43 a month" (non-representative) [sourced-secondary: https://www.familytree.com/blog/how-much-does-your-genealogy-hobby-cost/ and https://www.instarestoration.com/blog/the-genealogist-a-unique-survey, undated]. **Both are low quality; do not use for sizing.** No NGS or industry spend survey from 2024–2026 was found [unknown]. One forum data point: a user weighing "the 39$ to unlock the DNA or the 200 for a year of records and photo restoration" on MyHeritage [sourced: https://reddit.com/r/Genealogy/comments/wv7bot/, 2022-08-22, score 6, 12 comments].

### Q3. Platform photo features and their limits

| Platform | Feature | What it does | Limit | Source |
|---|---|---|---|---|
| Ancestry | Face Match | compares faces "with photos of deceased people available on Ancestry" | "only designed to help identify deceased people"; needs active membership | help.ancestry.com/hc/en-us/articles/53933332427283 (via competitive.md) |
| Ancestry | Photo Insights | AI suggests "likely time periods, possible locations, and short descriptions"; "Insights typically load in under 15 seconds" | "available to all Ancestry subscribers" (paid) | https://www.ancestry.com/c/ancestry-blog/ancestry-news/unearth-family-stories-with-photo-insights, 2026-08-25 |
| Ancestry | iMemories | mail-in digitisation; "added to your Ancestry gallery where you can tag family members to your tree"; TV streaming "Coming Late 2026" | $0.49/photo, ~$300 avg order; AI enhancements extra, price unlisted | https://www.ancestry.com/c/imemories/offer |
| Ancestry | app scanning | "Scan, upload, and enhance old photos and give them context" | no living-people statement on the page | https://help.ancestry.com/hc/en-us/articles/53933306174355 |
| MyHeritage | Photo Tagger | bulk face tagging; "available for free to all MyHeritage users" | "Tagging suggestions identified by name are provided only for individuals marked as deceased in your family tree"; "Living individuals from the family tree will remain unidentified"; consent required; unreviewed suggestions deleted after "3 months" | https://blog.myheritage.com/2022/08/introducing-photo-tagger-tag-multiple-photos-instantly/, 2022-08-01 |
| MyHeritage | Deep Nostalgia | animation | "As of May 2024, over 112 million animations were created"; "Over 1 million photos were animated in the first 48 hours" [sourced: wiki]; "Over 119 million animations and counting!" [sourced: myheritage.com/deepstory, © 2026] | https://www.myheritage.com/wiki/What_is_the_Deep_Nostagia_photo_feature_by_MyHeritage |
| MyHeritage | PhotoDater | date estimates for "undated photos taken between 1860 and 1990"; free | — | familytreemagazine.com MyHeritage photo tools (secondary) |
| MyHeritage | AI Time Machine | launched 2022-11-17: "hyper-realistic images of yourself as a historical figure"; needed 10–25 photos of one person (upload limit 35); 8 images per theme, introductory "one model and 20 themes per user, for a total of 160 images"; "free at launch for a limited introductory period", then paid | **sunset**: a January 2026 note at the top of the post says "AI Time Machine™ was sunset and is no longer available" | https://blog.myheritage.com/2022/11/introducing-ai-time-machine/, 2022-11-17 (updated Jan 2026) |
| MyHeritage | LiveStory → DeepStory | https://www.myheritage.com/livestory 301-redirects to /deepstory; that page describes it only via a testimonial ("DeepStory allows ancestors to tell their own life stories") | pricing, living-people policy, usage: [unknown — the page carries none; the 2022 launch post URL guessed returned 404] | http://www.myheritage.com/deepstory, © 2026 |
| MyHeritage | Photo plan | $49.90/yr, app-only, unlimited enhance/colorise/repair/scan, 20 LiveMemory videos/yr | "do not upload photos of living people unless you receive their prior permission" | MyHeritage blog 2024-11-21 |
| FamilySearch | Memories | free upload, albums, tags to tree persons | albums "a number limit of 1000 memories"; a bulk copy of "~1700" gallery images "Failed with no…" (thread 192372, 99 views / 8 replies as of 2026-11-03) [sourced: https://community.familysearch.org/en/discussion/192372/what-are-the-limits-on-folders-of-images-and-or-total-size-mbytes, via customers.md and category listing]; "accounts with more than 5,000 items may load slowly" [sourced: help article via customers.md]; default visibility public for deceased, private for living; "do not submit photographs of living people, except your own minor children, without their consent" [sourced-secondary: help-center articles as summarised in search in the original pass; on 2026-11-03 four familysearch.org/en/help/helpcenter/article/... URLs redirected to articles.familysearch.org, which returns 403 — still unverified against the page text] |
| FamilySearch | Full-Text Search / Labs | Full-Text Search: "search almost 2 billion historical records that haven't been indexed yet", AI reads text from images; Simple and Advanced modes [sourced: https://www.familysearch.org/en/search/full-text, fetched 2026-11-03]. Labs "Available Experiments" (2026-11-03): person/sources review, new Discovery Activities, "MyHeritage Matches", "Search All Family Trees on FamilySearch" [sourced: https://www.familysearch.org/en/labs/, © 2026] | no AI photo feature listed in Labs or announced at RootsTech 2026 [sourced: labs page; rootstech-2026-highlights] |
| FamilySearch | Compare-a-Face | face-similarity activity | menu item only; not a gallery listing [sourced: solutions-gallery page] |
| Storied | photos free; records paid | "Capture stories, memories, and photos"; StoriedBook print; "Import your FamilySearch tree and memories" [sourced: solutions-gallery entry] | pricing per Q2; funding [unknown — https://storied.com/about names five executives (CEO Kendall Hulet) and no investors, founding year or HQ; © "2022-2026"; no search budget to go further] | https://storied.com/trial-offers; https://storied.com/about |
| Permanent.org | nonprofit archive | one-time $10/GB; metadata preserved; steward/legacy-contact roles; sharing | no tagging/face feature on the homepage | https://www.permanent.org/ |
| Related Faces | face matching across users' uploads and archives | "isolates and maps faces and then compares them to reveal previously unknown connections" | $99/yr | https://relatedfaces.com/ |
| "Kinship" / "Kindred" apps | [unknown] | the FamilySearch gallery's only "Kin-" entries are Kin2me (famous-relative charts) and Kindex (letters/journals), neither a photo app [sourced: https://www.familysearch.org/en/innovate/solutions-gallery, 2026-11-03] | no search budget to locate apps by these names elsewhere | — |

Net: every incumbent has made the same design choice — AI face identification for the dead, manual-only for the living — and none manages a *library* (no dedup, no camera-roll ingestion, no cross-account merge). MyHeritage is the only one selling a standalone photo subscription, and it has already retired one paid AI photo product (AI Time Machine).

### Q4. APIs and app ecosystems

**FamilySearch.** Access is by application: "Apply to collaborate with us"; "We're seeking applicants with demonstrated technical skills and a strong business track record" [sourced: https://www.familysearch.org/innovate/]. Certification checklist (updated 2026-10-09): every app must "Apply to become a Solutions Provider" and "Obtain acceptance in the Solutions Program"; "Each user must obtain a FamilySearch access token in order to read or write to the Family Tree"; the Memories Write compatibility section lists (paraphrased from its bullets) uploading/editing/deleting memories, creating personas and comments, and detaching memories; an "AI Utilization Disclosure Addendum" is required for AI apps [sourced: https://developers.familysearch.org/main/docs/compatibility-checklist]. Whether an end-user upload agreement is required was not confirmed in the fetch and is dropped. **Answer to "can a third-party app push named photos into a user's FamilySearch tree today?": yes, with Memories-Write certification — upload, attach to a person, create personas (face tags) — but only after acceptance into a vetted partner program, not via self-serve keys.** Solutions Gallery (live count 2026-11-03): **90 listings** — "Access to Top Genealogical Resources: 7", "Family Tree Management Apps: 15", "Connection Solutions: 7", "Other Solutions: 61"; 17 entries mention photos, faces or memories, including Family Historian ("Link people to faces in photos"), Related Faces ("load photos from your memories gallery"), Tree-Me ("Link faces to names with drag an drop"), MemoryWeb, Mylio ("Store photos, videos, documents, and scanned sources"), Roots and Reels ("Sync your video to FamilySearch through Memories"), Storied [sourced: https://www.familysearch.org/en/innovate/solutions-gallery].

**Ancestry.** No public API. The partner API used by RootsMagic was replaced: "As of today" (2026-05-05) "the previous API has been turned off"; RootsMagic 11.2.0+ required; media over 20 MB not supported [sourced: https://blog.rootsmagic.com/?p=4065, 2026-05-05]. Ancestry had earlier "shut off external sign-in access to their API as of December 11, 2023" [sourced-secondary: RootsMagic blog ?p=3703 via search]. The "closed since 2017" premise in the brief is not supported; the partner API has existed continuously for FTM/RootsMagic and was *re-platformed* in 2026. Third-party write of photos: only via FTM/RootsMagic tree sync [unknown whether photo upload survives the new API — a user comment on the RootsMagic post reports images not updating].

**MyHeritage.** No public API found; the Family Tree Builder API was described as private in 2010 [sourced-secondary: https://www.tamurajones.net/GenealogyAPIs.xhtml]. MyHeritage's developer programme historically lived at FamilyGraph; on 2026-11-03 https://www.familygraph.com/ and https://familygraph.com/ returned 503 and /developer returned 403, so current status, scope and photo read/write are [unknown — three attempts recorded].

**Gramps Web (open source).** Main repo "1.8k" stars, "289" forks, "Open Source Online Genealogy System" [sourced: https://github.com/gramps-project/gramps-web, page fetched 2026-11-03]. The earlier "passing 1000 GitHub stars in 2025" line had no URL and is withdrawn; https://grampshub.com/ rendered only its title. Adoption in users: [unknown].

### Q5. Where they gather; how vendors reach them

- **RootsTech**: next event "March 4–6, 2027"; online "FREE"; in-person early-bird "$99 US 3-Day Pass ($129 US Standard Price)" and "$69 1-Day Pass ($79 US Standard Price)"; "200+ exhibitors/sponsors in the Expo Hall" [sourced: https://www.familysearch.org/en/rootstech/, fetched 2026-11-03]. Exhibitor booth cost: [unknown — /rootstech/exhibit, /rootstech/exhibitors and /rootstech/sponsor all 404 on 2026-11-03; no prospectus located]. Booth growth anecdote: The Family History Guide Association (a nonprofit, not a vendor) "started with a simple 10×10′ booth in 2016, and we are now enjoying a more spacious 30×40′ location" [sourced: https://www.thefhguide.com/blog/get-ready-for-rootstech-2026/, 2026-03-01]. RootsMagic says it has "been part of this event from the very beginning" [sourced: https://blog.rootsmagic.com/?p=4048, "RootsTech 2026: See Us at the Front Door!", 2026-03-03] — no booth size or year count given.
- **NGS conference**: "The National Genealogical Society 2027 Family History Conference", "19-22 May 2027", Madison, Wisconsin, Monona Terrace; "Registration will open December 2026"; no prices or attendance listed [sourced: https://conference.ngsgenealogy.org/, fetched 2026-11-03]. NGS 2026 "America at 250" in Fort Wayne, IN [sourced: https://www.ngsgenealogy.org/conference/]. FGS no longer runs a separate conference: the NGS site carries "Merger with FGS", "Welcome to the New NGS" and "Forum Magazine (FGS) Archives" pages [sourced: https://www.ngsgenealogy.org/, fetched 2026-11-03]; merger year and FGS's member-society count: [unknown — the merger page URL guessed returned 404].
- **Legacy Family Tree Webinars** (MyHeritage-owned): 2,860-webinar library; 502 speakers; 23 live webinars listed as upcoming at fetch; $59.95/yr [sourced: https://familytreewebinars.com/, 2026-11-03]. Vendors (Vivid-Pix, Photomyne) present here; handouts are hosted on the site. The earlier "220+ live classes, 117 expert presenters" line had no URL and is withdrawn.
- **YouTube**: Genealogy TV "reached the milestone of 100,000 subscribers in 2024" [sourced: https://genealogytv.org/about-gtv/]. Other channels' counts: [unknown — no search budget; youtube.com not fetchable from this session per pro-channel.md].
- **Podcasts**: a 2025 r/Genealogy thread from a university instructor asks for "the best podcasts related to genealogy" to update a 2023 course list [sourced: https://reddit.com/r/Genealogy/comments/1mf76lb/, 2025-08-01, score 7]. Audience numbers: [unknown — https://lisalouisecooke.com/ (Genealogy Gems) shows "Million free episode downloads" and "Free Podcast Episodes" labels whose figures are in graphics the fetch did not carry; https://www.genealogyguys.com/ 503; https://extremegenes.com/ now 301-redirects to an unrelated domain (m77go.com), not followed].
- **Facebook**: ">16,000 genealogy-based groups" (2021 count) [sourced-secondary: https://vitabrevis.americanancestors.org/2023/04/facebooks-locational-genealogy-groups, 2023-04]; current sizes of the largest groups [unknown — facebook.com is not fetchable from this session and no search budget remained].
- **Societies**: NGS member count [unknown — see Q2]; APG 2,000+ [sourced: apgen.org/about_us.php via pro-channel.md]; local society count [unknown — the NGS homepage links a "Find a Society, Library, Museum, Archive, or College Program" directory, but /society-directory/ and /societies-organizations/ both 404]. Local society newsletters as a channel: [unknown — one r/Genealogy post describes a monthly local group whose programme was "photo identification and restoration" [sourced: https://reddit.com/r/Genealogy/comments/tag2g2/, 2022-03-09, score 8]].
- **Small vendors that sell here**: RootsMagic (one-time $39.95; exhibits at RootsTech "from the very beginning" [sourced: ?p=4048]), Vivid-Pix ($249.99 software, bundles with ScanSnap), Related Faces ($99/yr), Photomyne (now bundled into Ancestry's app), MemoryCherish ($38–$148/photo). Revenue for any of them: [unknown — all private].

### Q6. Photo pain evidence (r/Genealogy via arctic-shift; URL, date, score, comments)

Original pass (12 threads, IDs re-verified by the auditor via the archive's /posts/ids endpoint):
- "1000's of photos in boxes. Need guidance on what to do with them" — "I want to cull my photos by about 80% or more… would you upload them to Ancestry, Family Search, Find A Grave, or other?" [sourced: https://reddit.com/r/Genealogy/comments/1vxjbjs/, 2026-08-24, score 46, 43 comments].
- "Mass transcribing photos and documents" — "I have scanned a little over 10,000 family photos and documents (fronts and backs)… the reason I was transcribing wasn't strictly for the transcription itself. It was so I could search the photos quickly" [sourced: https://reddit.com/r/Genealogy/comments/1w8eoxr/, 2026-09-05, score 8, 6 comments].
- "Help finding a person/service to digitize photos and letters while capturing names" — "those photo scanning services… wouldn't capture the 'who's who' side of things"; "keeping names with faces" [sourced: https://reddit.com/r/Genealogy/comments/1xemakt/, 2026-10-24, score 4, 7 comments].
- "How do you keep the story attached to scanned family photos?" — "who's in it, where it was taken, who identified the people, and whether the date is certain or just a guess" [sourced: https://reddit.com/r/Genealogy/comments/1ubnb7n/, 2026-06-21, score 5].
- "Inherited family photos back to 1800s" — plans to "manually update EXIF data"; "not sure how much I want to be publicly available (or Ancestry to have access to)"; "I have one living uncle that is my hope of naming some of the relatives" [sourced: https://reddit.com/r/Genealogy/comments/1s7dqoi/, 2026-03-30, score 1].
- "App to scan and store metadata to iCloud?" — "I thought Photomyne might be it, but you can't move the scans and metadata into iCloud… the metadata is then lost" [sourced: https://reddit.com/r/Genealogy/comments/1rybxkf/, 2026-03-19, score 0].
- "Best way to scan both sides of old family photos" — wants backs kept with fronts "in one file" [sourced: https://reddit.com/r/Genealogy/comments/1sb15nb/, 2026-04-03, score 6].
- "Have you ever found some really old family pictures…" — "I was only able to use less than a half of the pictures… the rest of them are a complete mystery" [sourced: https://reddit.com/r/Genealogy/comments/1mhi62p/, 2025-08-04, score 74, 44 comments].
- "Ever tried FaceSeek to place that random old family photo on your family tree?" [sourced: https://reddit.com/r/Genealogy/comments/1mobe66/, 2025-08-12, score 118, 22 comments] — demand for face search outside the platforms.
- "Photo Organizing Software. Any out there with the ability to save facial recognition name and location within the photo's metadata?" — Picasa nostalgia; "allowed me to share these 'digitally labelled' photos with others that could use any number of photo viewers" [sourced: https://reddit.com/r/Genealogy/comments/l1m646/, 2021-01-21, score 7, 20 comments].
- "For those with large digital photo collections" — Tropy recommended; "it doesn't have the AI that Google Photos does" [sourced: https://reddit.com/r/Genealogy/comments/rhwy7m/, 2021-12-16, score 100, 30 comments].
- "Compare-a-face accuracy?" [sourced: https://reddit.com/r/Genealogy/comments/16b5xbc/, 2023-09-06, score 6].

Repair-pass retries (queries "photo restoration", "Photo Tagger", "photo detective"; archive responses 2026-11-03):
- "I built a tool that helps analyze old genealogy photos — Photo Whisperer!" — a free custom GPT that reads clues in old photos [sourced: https://reddit.com/r/Genealogy/comments/1oqh7la/, 2025-11-07, score 44, 31 comments] — appetite for AI photo analysis outside the platforms.
- "I found a stack of old family photos - which photo restoration app do you use that actually…" — "tested a few tools that needed tons of manual adjustments" [sourced: https://reddit.com/r/Genealogy/comments/1rku7v4/, 2026-03-04, score 23, 6 comments].
- "How to people feel about photo restoration with AI?" [sourced: https://reddit.com/r/Genealogy/comments/1hjt2ib/, 2024-12-22, score 18, 22 comments].
- "What would make you trust someone to restore an irreplaceable family photo?" — market-research post from someone "looking into the photo restoration industry" [sourced: https://reddit.com/r/Genealogy/comments/1xg7ado/, 2026-10-26, score 0, 10 comments].
- "Photo tagger app: android." — wants to show scans to "nonaganrian relatives" on a tablet "so they can point to people and give me their name and backstory" [sourced: https://reddit.com/r/Genealogy/comments/ctrgo0/, 2019-08-22, score 3].
- "Anyone good at vintage photo detective work?" — "many without names or identifying details (put names on your photos, people!)" [sourced: https://reddit.com/r/Genealogy/comments/8od465/, 2018-06-04, score 6, 14 comments].
- "Is the one year Complete package from MyHeritage worth it?" — "$39 to unlock the DNA or the 200 for a year of records and photo restoration" [sourced: https://reddit.com/r/Genealogy/comments/wv7bot/, 2022-08-22, score 6, 12 comments].

FamilySearch Community, Memories category (page 1 of 122 pages, fetched 2026-11-03; dates shown without year on the listing) [sourced: https://community.familysearch.org/en/categories/memories]:
- "What are the limits on folders (# of images and/or total size (mbytes?)" — "I selected all my gallery images (~1700) and tried to copy them all to one folder. Failed with no…"; 99 views, 8 replies [sourced: https://community.familysearch.org/en/discussion/192372/what-are-the-limits-on-folders-of-images-and-or-total-size-mbytes].
- "Change in upload to Memories" (drag-and-drop change), "BUG in latest Memories UI", "Long TIme BUG" — three new reports posted the morning of the fetch [sourced: https://community.familysearch.org/en/discussion/193510/change-in-upload-to-memories; /193509/bug-in-latest-memories-ui; /193511/long-time-bug].
- "I need help correcting a person-tag display problem." — 34 views, 1 reply [sourced: https://community.familysearch.org/en/discussion/192996/i-need-help-correcting-a-person-tag-display-problem].
- "AI find a memory" — 55 views, 1 reply [sourced: https://community.familysearch.org/en/discussion/193207/ai-find-a-memory].
- "'Memories Feedback' & 'Memories (People and Find Pages)' groups are no longer available" — 757 views, 5 replies [sourced: https://community.familysearch.org/en/discussion/184843/memories-feedback-memories-people-and-find-pages-groups-are-no-longer-available].

Pattern: the recurring asks are (1) keep names/faces/backs/provenance *with the file* in portable metadata, (2) search by person, (3) control who sees it, (4) capture an elderly relative's identifications before they die, (5) restoration that does not need manual tuning. Paid identification exists ($45/photo consulting; $38–$148/photo restoration) at consultant/boutique scale.

### Q7. Falsification

**Are they satisfied with incumbent photo tools?** Weak evidence either way. The only hands-on independent account found says of Ancestry's face tool: "I got a great match, and I got 21 trees", and "You're not always going to be lucky enough to get a good facial recognition match." [sourced-secondary: https://blog.familyhistoryhound.com/2025/05/the-hidden-tool-on-ancestry-you-should-be-using-recognize-ancestors/, 2025-05-29]. Deep Nostalgia's 112M→119M animations show enormous *engagement* with photo features — but it is free and viral, not paid — and MyHeritage retired its paid AI Time Machine by January 2026 [sourced: blog.myheritage.com 2022-11-17 post, Jan 2026 note]. Against satisfaction: the forum asks above are from 2025–2026 and none is answered by an incumbent feature; FamilySearch's own community documents 1,000-item album limits, a failed ~1,700-item copy, and three fresh Memories bug reports on the day of fetch. Verdict: not falsified, but not proven — nobody has surveyed this.

**Is the hobby aging/shrinking?** Not supported as "shrinking"; supported as "no disclosed growth". Ancestry subscribers: 3.8M (Moody's, 2021) and "3.8M+" (Impact Report, 2022 column and 2025) with floors of "over three million" (Reuters 2025) and "more than 3 million" (company facts); revenue "$1.2 billion" (2021) and "more than $1bn" (2025); 2019 revenue down 1.2% on 2018 [sources as in Q1]. A floor of ">3M" is consistent with 3.8M, so the series does not show decline; it shows a sponsor that has disclosed no growth in four years while seeking an exit at ~$10bn after paying $4.7B. MyHeritage cut 15% of 500 staff in July 2026 while on the block at ~$1B [Globes 2026-07-08; Calcalist 2025-12-24]. 23andMe's 2025 Chapter 11 is adjacent (DNA, not subscriptions) and could not be primary-sourced this session [see Q1]. Counter-evidence: RootsTech online reach "millions" (2025, 2026); FamilySearch 297M visits in 2025 and 22.7B names/images; Genealogy TV crossed 100k subscribers in 2024; Storied (launched January 2023 per ancestoriq) sells an entry tier at $19.99/yr [sourced-secondary: ancestoriq 2026-08-14; when that price was introduced is [unknown]]. Verdict: the *paid-subscription* core shows no disclosed growth; the *free/online* audience is large and still growing. A photo-layer product would be selling into a paying base that is, on the evidence, flat rather than shrinking.

**Is living-relative tagging unwanted for privacy reasons?** All three platforms restrict it by design (Ancestry: "To protect the privacy of living people, Face Match is only designed to help identify deceased people"; MyHeritage: name suggestions "only for individuals marked as deceased"; FamilySearch: living-person memories private by default, consent rule [still secondary — see Q3 table note]). But these are *vendor* choices under biometric-law exposure (see `face-regulation.md`), not evidence of user preference. User evidence cuts the other way: the 2026-03-30, 2021-01-21 and 2019-08-22 threads want faces identified (including living relatives) but kept *private and portable*; a FamilySearch community thread titled "Memories searchtool is finding photos with living people tagged" shows the complaint is about *public exposure*, not tagging itself [sourced-secondary: https://community.familysearch.org/en/discussion/62998/, fetch redirected to login]. Verdict: not falsified; the demand is for private, user-controlled tagging, which is exactly what the incumbents will not ship.

## 3. Segment table and ceiling

| Platform | Paying users | Price | Photo features | API access |
|---|---|---|---|---|
| Ancestry | 3.8M [sourced: Moody's 2021-12-13]; "3.8M+" [sourced: Impact Report 2025]; floor "over three million" [sourced-secondary: Reuters via PEW 2025-09-26] | $24.99–$59.99/mo; $119–$269/6 mo [sourced: ancestry.com/c/allproducts] | Face Match (deceased only), Photo Insights, iMemories ($0.49/photo), app scan | none public; partner API re-platformed 2026-05-05 [sourced: RootsMagic ?p=4065] |
| MyHeritage | "one million annual subscribers" [sourced: about page, undated milestone]; 104M registered [sourced: Calcalist 2025-12-24] | Photo plan $49.90/yr [sourced: blog 2024-11-21]; Complete $299/yr [sourced-secondary: familytreemagazine 2023]; other tiers [unknown — /pricing 404] | Photo Tagger (deceased suggestions, free), Deep Nostalgia (119M), PhotoDater, LiveMemory, DeepStory; AI Time Machine sunset Jan 2026 | none public; FamilyGraph site 503/403 [unknown] |
| FamilySearch | 0 (free) | $0 | Memories (1,000/album limit; ~1,700-item copy failed), tags, Compare-a-Face; Full-Text Search ~2B records (not photos) | partner-only; Memories Write certifiable; 90 apps in gallery, 17 photo/memory-related [sourced: solutions-gallery] |
| Storied | [unknown] | $19.99–$99.99/yr [sourced-secondary: ancestoriq 2026-08-14; own pricing page login-walled] | photos free, StoriedBook print, FamilySearch memories import | listed in FamilySearch gallery; funding [unknown] |
| Findmypast | [unknown — findmypast.com and /subscribe show no counts] | [unknown — subscribe page renders no plans in fetched text] | none mentioned on homepage [sourced: https://www.findmypast.com/, 2026-11-03] | [unknown] |
| Geneanet | "more than 5 million members" [sourced-secondary: en.geneanet.org snippet, undated; site 403 ×3]; paying [unknown] | [unknown — 403] | [unknown — 403] | [unknown] |
| Permanent.org | [unknown] | $10/GB one-time [sourced: permanent.org] | archive, metadata preserved, no tagging shown | [unknown] |
| Related Faces | [unknown] | $99/yr [sourced] | face matching across users | reads FamilySearch Memories |

**Ceiling arithmetic (attach rate × price).**
- Paying base, two cases: **A. Ancestry-only, floor 3.0M** [sourced-secondary: Reuters 2025; company facts]; **B. Ancestry 3.8M + MyHeritage 1.0M = 4.8M** [estimated: Moody's 2021 point estimate + undated MyHeritage milestone; overlap unknown; the MyHeritage input is the weakest number in this file]. The earlier draft's "4M" was the sum of two floors and sits between these cases.
- Price anchor: $49.90/yr — the one genealogy-vendor photo subscription that exists [sourced: MyHeritage blog 2024-11-21]; cross-checks $59.99 (Photomyne yearly, secondary), $99 (Related Faces), $59.95 (Legacy webinars, primary 2026-11-03).
- Attach rate: [unknown — MyHeritage does not disclose Photo-plan take-up]. Illustrative range:
  - 1%: A. 3.0M × 0.01 × $49.90 = **$1.5M/yr**; B. 4.8M × 0.01 × $49.90 = **$2.4M/yr** [estimated]
  - 3%: A. 3.0M × 0.03 × $49.90 = **$4.5M/yr**; B. 4.8M × 0.03 × $49.90 = **$7.2M/yr** [estimated]
  - 10%: A. 3.0M × 0.10 × $49.90 = **$15.0M/yr**; B. 4.8M × 0.10 × $49.90 = **$24.0M/yr** [estimated]
- Upper bound if priced like a full tier ($119/6 mo ≈ $238/yr) at 3%: B. 4.8M × 0.03 × $238 = $34.3M/yr; A. 3.0M × 0.03 × $238 = $21.4M/yr [estimated]; nobody has demonstrated a $238/yr photo-only willingness to pay, and MyHeritage's one paid AI photo add-on (AI Time Machine) was withdrawn.
- Reality check: the entire paid genealogy-subscription market is ≈$1.0–1.2B (Ancestry) [sourced: Moody's 2021; Reuters 2025] + MyHeritage [unknown revenue; a ~$1B asking valuation at a 3–5× revenue multiple implies $200M–$333M revenue — [estimated: $1B ÷ 5 = $200M; $1B ÷ 3 = $333M; the multiple is an assumption, not sourced]]. A photo layer at 3% attach is a $4.5–7.2M business; at 10% it is $15–24M. That is a bootstrappable niche or a feature, not a venture-scale market on its own — unless the product reaches the much larger *non-subscriber* family-historian population (FamilySearch's 297M visits; Deep Nostalgia's 119M animations) for whom no paying-user count exists [unknown].

## 4. Unknowns and what was tried

- Ancestry 2020 subscriber count at the Blackstone close: both blackstone.com releases 403 (reproduced); Ancestry newsroom index renders no bodies; guessed Ancestry press URL 404. The 3.6M snippet figure is withdrawn.
- Ancestry 2024–2026 subscriber and revenue figures from a primary: Moody's/S&P 2025–26 reports not found in the original pass; no search budget in the repair pass; Reuters original not retrieved (PEW secondary used). "$1.3B 2024 revenue" appears only on revenuememo.com — not used.
- MyHeritage revenue, Photo-plan subscriber count, tier ladder (Data/Premium/PremiumPlus/Omni): /pricing 404, /plans 404, /upgrade 404, /site-upgrade empty, /subscriptions shows no prices. FamilyGraph (API) 503 ×2, /developer 403.
- FamilySearch registered users, Memories count, in-person RootsTech headcount: not published; year-in-review, about page and newsroom pages fetched. Help-center articles on Memories visibility/living people: four /help/helpcenter/article/ URLs redirect to articles.familysearch.org (403) or to its site search; still secondary.
- RootsTech exhibitor pricing: /rootstech/exhibit, /exhibitors, /sponsor all 404; no prospectus online.
- Findmypast: dcthomson.co.uk/news has no financials; findmypast.com and /subscribe render no prices or counts. The earlier "£134m" had no URL and is withdrawn.
- Geneanet: en.geneanet.org, www.geneanet.org, en.geneanet.org/legal/about/ all 403.
- Storied funding: about page has none; pricing page login-walled. 23andMe primary: investors.23andme.com 403 ×2, guessed release URL 404.
- NGS member count: join page, homepage and /about-ngs/ (404) carry none; society directory /society-directory/ and /societies-organizations/ 404; merger page URL guessed 404.
- Family Tree Maker price: mackiev.com/ftm/ has none; /ftm/buy.html 404; store.mackiev.com does not resolve from this session (would need to be allowed in network settings).
- Podcast audiences: lisalouisecooke.com figures are in graphics; genealogyguys.com 503; extremegenes.com redirects to an unrelated domain.
- Legacy webinars post-June-2026 price: now primary ($59.95/yr on the homepage); the earlier genealogyalacarte page remains 403.
- Reddit queries that still time out at the archive after three attempts: "organize photos", "facial recognition", "unknown relatives photos".
- Facebook group sizes 2025–26, Findmypast/Geneanet paid counts, Gramps Web user counts, "Kinship"/"Kindred" app identities: not found; no search budget in the repair pass.
- Any representative survey of genealogist spend 2020–2026: none found; the two circulating figures are flagged low-quality above.

## 5. Source list (distinct, accessed 2026-11-03 unless dated)

Primary (fetched and quoted):
1. https://finance.yahoo.com/news/arches-holdings-inc-moodys-assigns-005705240.html (Moody's, 2021-12-13)
2. https://www.theglobeandmail.com/investing/investment-ideas/article-investors-ready-for-up-to-us25-billion-in-debt-for-blackstones/ (2020-08-11; Moody's 2019 data)
3. https://www.calcalistech.com/ctechnews/article/syr4gmfmzl (2025-12-24)
4. https://en.globes.co.il/en/article-myheritage-to-lay-off-15-of-workforce-1001548761 (2026-07-08)
5. https://www.familysearch.org/en/newsroom/rootstech-2026-highlights (2026-04-13)
6. https://www.familysearch.org/en/newsroom/rootstech-2025-recap (2025-04-14)
7. https://www.familysearch.org/en/blog/familysearch-year-in-review-2025 (2026-01-07)
8. https://www.familysearch.org/en/about/ (© 2026)
9. https://www.familysearch.org/en/search/full-text
10. https://www.familysearch.org/en/labs/
11. https://www.familysearch.org/en/rootstech/ (2027 pricing)
12. https://www.ancestry.com/c/ancestry-blog/ancestry-news/ancestry-acquires-imemories (2025-07-30)
13. https://www.ancestry.com/c/imemories/offer
14. https://www.ancestry.com/c/allproducts
15. https://www.ancestry.com/c/ancestry-blog/ancestry-news/unearth-family-stories-with-photo-insights (2026-08-25)
16. https://help.ancestry.com/hc/en-us/articles/53933306174355-Creating-and-Preserving-Memories-on-Ancestry
17. https://blog.myheritage.com/2022/08/introducing-photo-tagger-tag-multiple-photos-instantly/ (2022-08-01)
18. https://blog.myheritage.com/2024/11/introducing-livememory-bring-your-photos-to-life-in-video/ (2024-11-21)
19. https://blog.myheritage.com/2022/11/introducing-ai-time-machine/ (2022-11-17; Jan 2026 sunset note)
20. https://www.myheritage.com/wiki/What_is_the_Deep_Nostagia_photo_feature_by_MyHeritage
21. http://www.myheritage.com/deepstory (© 2026; /livestory redirects here)
22. https://www.myheritage.com/dna
23. https://developers.familysearch.org/main/docs/compatibility-checklist (updated 2026-10-09)
24. https://www.familysearch.org/innovate/
25. https://www.familysearch.org/en/innovate/solutions-gallery
26. https://www.familysearch.org/en/blog/the-familysearch-app-gallery-connects-you-with-the-latest-family-history-apps (2015-01-13)
27. https://blog.rootsmagic.com/?p=4065 (2026-05-05)
28. https://blog.rootsmagic.com/?p=4048 (2026-03-03)
29. https://www.rootsmagic.com/
30. https://www.mackiev.com/ftm/
31. https://legacyfamilytree.com/
32. https://maureentaylor.com/photo-consultation-options/ (© 2026); https://maureentaylor.com/speaking-page/
33. https://www.vivid-pix.com/memorystationsoftware/
34. https://www.forever.com/historian
35. https://epson.com/For-Home/Scanners/Photo-Scanners/FastFoto-FF-680W-Wireless-High-speed-Photo-Scanning-System/p/B11B237201
36. https://relatedfaces.com/
37. https://www.permanent.org/
38. https://www.memorycherish.com/
39. https://www.ngsgenealogy.org/join-renew-membership/; https://www.ngsgenealogy.org/; https://www.ngsgenealogy.org/conference/; https://conference.ngsgenealogy.org/
40. https://familytreewebinars.com/ ; https://familytreewebinars.com/webinar-library
41. https://genealogytv.org/about-gtv/
42. https://storied.com/trial-offers ; https://storied.com/about
43. https://github.com/gramps-project/gramps-web
44. https://www.thefhguide.com/blog/get-ready-for-rootstech-2026/ (2026-03-01; booth anecdote, The Family History Guide Association)
45. https://www.findmypast.com/ ; https://www.findmypast.co.uk/subscribe (no prices in fetched text)
46. https://community.familysearch.org/en/categories/memories (page 1 of 122) and the discussion URLs listed in Q6
47. arctic-shift r/Genealogy archive, 19 threads listed in Q6 (https://arctic-shift.photon-reddit.com/api/posts/search?subreddit=Genealogy)
48. https://www.apgen.org/about_us.php (via pro-channel.md)

Secondary (quoted via search or a page that would not fetch):
49. https://www.privateequitywire.co.uk/blackstone-explores-sale-or-ipo-of-ancestry-com/ (2025-09-26, citing Reuters)
50. https://ancestoriq.com/blog/storied-review/ (2026-08-14)
51. https://familytreemagazine.com/websites/myheritage/myheritage-photo-tools/ (Nov/Dec 2023)
52. https://photoscanrestore.com/guides/photomyne-cost (2026-09-30)
53. https://blog.familyhistoryhound.com/2025/05/the-hidden-tool-on-ancestry-you-should-be-using-recognize-ancestors/ (2025-05-29)
54. https://vitabrevis.americanancestors.org/2023/04/facebooks-locational-genealogy-groups
55. https://www.tamurajones.net/GenealogyAPIs.xhtml
56. https://community.familysearch.org/en/discussion/62998/memories-searchtool-is-finding-photos-with-living-people-tagged (login redirect)
57. https://en.geneanet.org/ (snippet; 403)
58. https://www.familytree.com/blog/how-much-does-your-genealogy-hobby-cost/ and https://www.instarestoration.com/blog/the-genealogist-a-unique-survey (low-quality spend figures)
59. Prior-round files: customers.md Q1(a), competitive.md Q6, pro-channel.md (for Ancestry Impact Report, company-facts, Face Match help article, Memories help article, thread 192372, APG).

Blocked / empty this session (not cited for numbers): blackstone.com Ancestry releases (403 ×2); ancestry.com/corporate/newsroom/press-releases (no bodies); myheritage.com /pricing, /plans, /upgrade (404), /site-upgrade (empty), /subscriptions (no prices); familygraph.com (503 ×2, /developer 403); articles.familysearch.org (403); familysearch.org/en/rootstech/exhibit, /exhibitors, /sponsor (404); ngsgenealogy.org/about-ngs/, /society-directory/, /societies-organizations/, /merger-with-fgs/ (404); investors.23andme.com (403 ×2) and guessed release (404); storied.com/pricing (login); mackiev /ftm/buy.html (404), store.mackiev.com (unresolvable); grampshub.com (title only); geneanet.org (403 ×3); dcthomson.co.uk/news (no financials); phojoe.com restoration page (404); genealogyguys.com (503); extremegenes.com (301 to unrelated domain); lisalouisecooke.com (figures in graphics); genealogyalacarte.ca ?p=47592 (403).

## Audit log

Repair pass 2026-11-03. Web-search budget was exhausted at the start of the pass; every fix below used direct fetches of known URLs or the arctic-shift archive.

Untagged numbers:
1. L3 "6 of 11 queries returned Timeout" — tagged to the archive endpoint; added the retry record (3 of the 6 now returned, 3 still time out after three attempts).
2. L31 Findmypast "£134m" — withdrawn (no URL); Findmypast now [unknown] with three attempted URLs listed.
3. L41 FTM "~$79.95" and Legacy "free" — FTM price withdrawn and set [unknown] with attempts; Legacy 10 free now primary-sourced to legacyfamilytree.com.
4. L45 NGS "nearly 10,000" — withdrawn; [unknown] with the three NGS pages checked.
5. L45 APG "~2,000" — citation corrected to apgen.org/about_us.php via pro-channel.md.
6. L64 Full-Text Search "2.3 billion" — replaced with the primary landing page's "almost 2 billion historical records" (URL given); Labs experiments listed from the Labs page.
7. L78 Gramps Web stars — "1.8k" and "289 forks" now sourced to the GitHub page fetched 2026-11-03; the "passing 1000 stars in 2025" line withdrawn (grampshub.com rendered empty).
8. L82 "2013 kit $295" — removed; exhibitor cost [unknown] with three 404 URLs listed.
9. L83 Legacy webinars "220+ classes, 117 presenters" — replaced with primary homepage figures (2,860 library, 502 speakers, 23 upcoming, $59.95/yr).
10. L87 RootsMagic "10+ years exhibiting" — replaced with the RootsMagic post's own words ("from the very beginning", no number).
11. L110 "Storied launched sub-$20 pricing in 2025" — rewritten: launched January 2023 per ancestoriq; $19.99 tier exists; introduction date [unknown].
12. L110 23andMe Chapter 11 — retained as background only, explicitly flagged no-URL after investors.23andme.com 403 ×2 and a 404 guess; not load-bearing.
13. L134 MyHeritage revenue "well under $300M" — corrected to the arithmetic the method gives ($200M–$333M) and the multiple flagged as an assumption.
14. L25 "Revenue ≈ $1.0–1.2B throughout" — rewritten with per-year sourced figures and the withdrawn 2020 number removed.

Suspect claims:
1. Blackstone 2020 "3.6 million" — withdrawn; both primary pages 403 (reproduced), Ancestry newsroom empty; the Globe and Mail Moody's 2019 data (revenue −1.2%, DNA units −48%, 6.7× leverage) now used and cited inline.
2. "Flat/shrinking" overread of "over three million" — Q1 reading and Q7 verdict rewritten to "no disclosed growth"; floors stated as floors, consistent with 3.8M.
3. RootsTech "$79 / $129" attributed to thefhguide — replaced with FamilySearch's own RootsTech page (2027: $69/$79 one-day, $99/$129 three-day, online free).
4. Booth-growth sentence misattributed to RootsMagic — reattributed to The Family History Guide Association with the exact quote and the 2026-03-01 date; RootsMagic's post quoted correctly.
5. familyhistoryhound quotations — replaced with the page's actual sentences ("I got a great match, and I got 21 trees"; "You're not always going to be lucky enough to get a good facial recognition match"); date 2025-05-29.
6. MyHeritage "one million annual subscribers" as a 2026 input — flagged undated and possibly annual-plan-only; the ceiling now shows case A (Ancestry-only 3.0M floor) and case B (3.8M + 1.0M = 4.8M) with the MyHeritage input named as the weakest number.
7. "Blackstone's 2026 8-Ks do not mention Ancestry" — dropped; replaced with what was actually tried.
8. Findmypast "£134m" — withdrawn (see above).
9. Geneanet "5 million" — kept as sourced-secondary, marked undated and unverified, with three 403 attempts recorded.
10. Memories Write "quoted" paraphrase and upload-agreement claim — rewritten as an explicit paraphrase of the checklist bullets; the upload-agreement sentence dropped as unconfirmed.
11. Maureen Taylor "15-minute" — replaced with the page's actual wording; no session length asserted.

Broken/misquoted sources:
- thefhguide.com: now cited only for the booth anecdote (verified quote), not for prices.
- blog.rootsmagic.com/?p=4048: now cited only for "from the very beginning" (verified), with title and date.
- familyhistoryhound: quotes corrected (verified).
- Globe and Mail: now cited inline for the Moody's 2019 figures it actually contains.
- Blackstone release: no longer the basis for any number.
- APG: internal citation corrected to pro-channel.md / apgen.org.

Missing vs brief:
- Q1: FamilySearch totals added (22.7B names/images, 1.8B tree people, 3.9B sources, 6,447 centers); Moody's 2019 data used; 23andMe flagged as no-URL background; Ancestry 2024–26 rating reports still [unknown].
- Q2: MyHeritage DNA kit price added ($19.90 sale, was $89); tier ladder [unknown] with five attempted URLs; Permanent.org pricing and features added from the root page; restoration-service pricing added (MemoryCherish); local society counts [unknown] with two 404 directory URLs recorded.
- Q3: AI Time Machine (launch and Jan 2026 sunset) and LiveStory→DeepStory redirect added; Storied funding [unknown] with the about page's contents; Permanent.org row added; Kinship/Kindred row added as [unknown] with the gallery check; FamilySearch Memories visibility still secondary, with the four redirect/403 URLs recorded.
- Q4: MyHeritage API — FamilyGraph attempted three ways (503/503/403) and recorded; Gramps Web primary-sourced, user count still [unknown].
- Q5: NGS 2027 conference (dates, venue, registration timing) and the NGS–FGS merger pages added; podcasts section added (three attempts, one Reddit thread); Facebook and other YouTube counts [unknown] with reasons; RootsTech pass prices now primary; exhibitor cost [unknown] with attempts.
- Q6: three archive queries recovered (seven new threads added with URL/date/score); FamilySearch Community Memories category page listed with six thread URLs; restoration pricing and demand evidence added.
- Q7: shrinking verdict rewritten without the withdrawn 3.6M figure and without overreading floors.
- Output: Findmypast and Geneanet rows now carry [unknown] with what was fetched; ceiling arithmetic split into two bases and the MyHeritage revenue aside corrected.
