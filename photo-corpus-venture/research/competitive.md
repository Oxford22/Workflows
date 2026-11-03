# Track A — Competitive map

Research date: 2026-11-03 (repair pass same day). All sources accessed 2026-11-03 unless noted. Every
number is tagged `[sourced: url, date]`, `[estimated: method]`, or `[unknown]`. Source dates are the
publication date of the source, not today's date. Where only secondary sources exist, this is said
explicitly. Repair-pass constraint: the per-turn WebSearch budget was exhausted before the repair began,
so every replacement source below was reached by direct WebFetch of a known URL; items that could not be
reached that way are marked `[unknown]` with the URLs tried.

Scope: Apple native, Google native, independents, verticals (brief), the consumer-photo graveyard,
and the "merge relatives' libraries into one family archive" question. Seed assumptions tested:
the founder's "already rejected" voice-app claim and A4 (Apple/Google won't ship cross-account
family merge + open AI access).

---

## 1. Questions asked

1. What do Apple Photos + Siri / Apple Intelligence do today (iOS 26 shipped Sept 2025; iOS 27
   shipped Sept 2026) for natural-language search, voice search, editing by voice, face
   clustering, shared/family libraries, cross-account merging? Is "standalone voice photo
   search/editing is native in iOS 27 Siri AI" true?
2. What is the status of Google Photos "Ask Photos", Gemini integration, partner/family sharing,
   and whether (and since when) the Gemini app can query Google Photos via a connector?
3. Independents: Ente, Immich, PhotoPrism, Mylio, Amazon Photos, Synology/Nextcloud/LibrePhotos/
   Lychee/Photoview, Pixelfed, Forever.com, Permanent.org, Storyworth/Mixbook/Artifact/Remento.
4. Vertical (brief): CompanyCam, HOVER, Spectora, HappyCo.
5. Dead consumer photo startups 2013–2026 and why they died.
6. Has anyone shipped "merge multiple relatives' libraries into one family archive with
   cross-generation face clustering"? Gap or graveyard?

---

## 2. Findings per question

### Q1. Apple native (iOS 26 → iOS 27)

**Version numbers verified.** iOS 26 released 2025-09-15 [sourced: https://www.macrumors.com/2025/09/15/apple-releases-ios-26/, 2025-09-15]. iOS 27 announced at WWDC 2026-06-08 with developer beta the same day, public release "this fall" [sourced: https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/, 2026-06-08]; the "2027 software releases" (iOS 27 etc.) shipped 2026-09-14 [sourced: https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/, 2026-09-14].

**Natural-language photo search: native since iOS 18.1 (Oct 2024), not new in iOS 27.** Apple, Oct 2024: "Natural language search gives users the ability to search for just about anything by simply describing what they are looking for," example "Maya skateboarding in a tie-dye shirt"; it "also works across videos" [sourced: https://www.apple.com/newsroom/2024/10/apple-intelligence-is-available-today-on-iphone-ipad-and-mac/, 2024-10-28]. Re-stated at WWDC25: "Natural language search in Photos makes it easier for users to find a photo or video by simply describing it" and "Users can create a memory movie in Photos by typing a description" [sourced: https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/, 2025-06-09].

**iOS 26 Photos changes were cosmetic/organizational, not AI.** 9to5Mac's iOS 26 Photos roundup (URL slug dated 2025-08-13; page shows "Oct 23 2025") names six things: Liquid Glass design, return of the tab bar (Library / Collections / Search), Spatial Scenes (including as Lock Screen wallpaper), Collections view options, and event-details screens for concerts/sports. The article does not mention Apple Intelligence or natural-language search at all; its only search reference is the Search tab [sourced: https://9to5mac.com/2025/08/13/heres-everything-new-for-apple-photos-in-ios-26/, 2025-10-23 — paraphrase, not a quotation]. WWDC25 also opened the on-device Foundation Model to third-party apps ("Apple is opening up access for any app to tap directly into the on-device foundation model"; "Guided generation, tool calling, and more are all built into the framework") [sourced: https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/, 2025-06-09].

**iOS 27 / Siri AI (shipped 2026-09-14): voice *search* of photos is native; voice *editing* of photos is NOT clearly native.**
- Apple, June 2026: Siri AI "can search across messages, emails, photos, and more"; the Photos/Spotlight/Mail "search experience has been rebuilt to make it more stable and efficient"; "iCloud Shared Albums introduce cross-platform photo sharing with full-resolution support"; photos load "up to 70 percent faster" [sourced: https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/, 2026-06-08].
- Apple, Sept 2026: Siri AI "draws on personal context understanding to help users find what they need in the moment across messages, emails, photos"; Siri AI can handle "editing and sharing a set of photos" (listed as an action, no detail on what "editing" means); Photos "taps into more powerful image models to provide new ways to edit photos": Spatial Reframing, Extend, Clean Up. Apple Foundation Models were "custom-built in collaboration with Google and its Gemini models." Siri AI is beta, English only at launch; "will not be available initially in the EU on iOS, iPadOS, and watchOS"; not in China [sourced: https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/, 2026-09-14].
- Apple, June 2026 (Photos-specific release): AI edits "will automatically include a hidden SynthID watermark"; photo editing tools are "subject to daily usage limits"; "Increased access is available with most iCloud+ subscription plans" [sourced: https://www.apple.com/newsroom/2026/06/apple-intelligence-brings-powerful-ai-capabilities-into-everyday-experiences/, 2026-06-08].
- WWDC26 session 121: the session *description* says Siri AI uses "natural language abilities to edit and write emails, texts, and documents" — the natural-language-editing claim is about text, not photos. The *video transcript* (not the description) contains the photo line "See next-generation Apple Intelligence extend, reframe, and clean up your photos", attributed to Apple Intelligence rather than to Siri [sourced: https://developer.apple.com/videos/play/wwdc2026/121/, 2026-06-08].
- MacRumors iOS 27 roundup: Siri example queries "Find images with pancakes from 2024", "Show me my photos from the music festival last weekend", actions "Add these photos to the cat album", "Send all the photos from today to Eric". Re-fetched 2026-11-03: the roundup "has no sentence saying Siri edits photos"; photo editing is described as the Photos app's own Clean Up / Extend / Reframe tools, and Image Playground modifies images separately [sourced: https://www.macrumors.com/roundup/ios-27/, accessed 2026-11-03].
- Secondary press disagrees: RedShark says "users can describe a desired edit in plain text" and Photos carries it out [sourced: https://www.redsharknews.com/apple-wwdc-2026-siri-ai-ios-27-photo-editing, 2026-06-09]. A Yahoo WWDC recap reportedly said Siri can change an image when asked by typing or speaking, but the fetch was blocked (403) and the claim is seen only in a search snippet [unknown — unverified secondary]. MacRumors pre-WWDC reported Apple was testing natural-language photo editing and it "may not ship in the first iOS 27 release" [sourced: https://www.macrumors.com/guide/wwdc-2026-what-to-expect/, 2026-06].

**Face clustering**: Apple People & Pets is longstanding; iOS 27 newsroom text does not describe changes. On-device only; no API exposes Apple's face clusters to third parties [unknown — no primary source found stating otherwise].

**Shared/family libraries** (Apple support, re-fetched 2026-11-03): iCloud Shared Photo Library lets you share with "up to five other people" (creator + 5 = 6 people); "You can join one Shared Library"; setting up or joining requires "iOS 16.1, iPadOS 16.1, or macOS Ventura or later" with iCloud Photos on. The creator "can remove a participant or delete the Shared Library at any time." The 7-day rule applies when the *creator deletes* the library: participants who were members for more than a week automatically receive everything in their Personal Library, those in it for less than a week receive only what they contributed. Participants who *leave* choose between keeping a copy of the whole library or only their own contributions [sourced: https://support.apple.com/HT213248 and https://support.apple.com/guide/photos/pht4dd77b3aa, accessed 2026-11-03]. Cap is 6 people [sourced: same]. Note the community caveat that a Shared Library "is only sharing the media, but not the structure of the library" [sourced: https://discussions.apple.com/thread/256192786, community, accessed 2026-11-03].

**Cross-account merging**: No Apple mechanism merges two Apple Accounts' iCloud Photos libraries. What Apple documents is single-account: on a Mac, "only the photos and videos in your System Photo Library are uploaded to iCloud"; when you designate a new System Photo Library and turn on iCloud Photos, "the photos stored in iCloud are merged" into it and "the libraries can't be unmerged" [sourced: https://support.apple.com/guide/photos/use-multiple-libraries-pht6d60b524/mac, accessed 2026-11-03]. Apple Community guidance (secondary): "Merging in iCloud is the only way to preserve the master-version pairs"; export/re-import is "the most tedious method"; PowerPhotos is "second best" [sourced: https://discussions.apple.com/docs/DOC-10211, last modified 2019-03-03, community doc]. A 2025 thread on merging two people's iCloud libraries recommends logging in with the other person's Apple ID on a Mac and importing, or "PowerPhotos ($40) to merge the Libraries" — "Outside of using iCloud, this is the only way of merging two Libraries without losing album and folder organization" [sourced: https://discussions.apple.com/thread/256192786, community, accessed 2026-11-03]. PowerPhotos' own page says it "lets you merge your libraries together while weeding out duplicate photos" and does not mention any limitation on iCloud/optimised libraries (the earlier draft's "cannot merge optimised iCloud Photos Libraries" quote was not in any cited source and is withdrawn) [sourced: https://www.fatcatsoftware.com/powerphotos/, accessed 2026-11-03]. No Apple support article describing Apple-Account-to-Apple-Account photo merge was found; URLs tried: support.apple.com/HT213248, /guide/photos/pht4dd77b3aa, /guide/photos/use-multiple-libraries-pht6d60b524/mac [unknown whether one exists].

**Verdict on the "already rejected" claim**: *Voice photo search* is native (Siri AI, iOS 27, Sept 2026, US/English, not EU-iOS at launch). *Voice photo editing* is at best "editing a set of photos" as a Siri action with no public detail, plus Apple-defined AI edit tools (Extend/Reframe/Clean Up) with daily usage limits. The claim is partially true: search yes, editing unproven.

### Q2. Google native

**Ask Photos timeline**: announced I/O May 2024; US early access 2024-09-05 [sourced: https://blog.google/products-and-platforms/products/photos/google-ask-photos-early-access/, 2024-09-05]. Paused June 2025: Android Police (2025-06-04) reports PM Jamie Aspinall saying the rollout "has been paused at very small numbers" because the feature was not there "in terms of latency, quality and ux", and that an "improved version" with the speed of the original search would ship in about two weeks [sourced: https://www.androidpolice.com/google-photos-hits-pause-gemini-powered-ask-photos-search/, 2025-06-04]. Resumption date: a PetaPixel report dated 2025-06-27 was cited in the earlier draft but returns 403 on fetch; the resumption is consistent with Aspinall's "about two weeks" but the exact date is [unknown — PetaPixel unreachable]. Nov 2025: expanded to "more than 100 new countries and regions, and 17 new languages"; "Help me edit" lets users type or speak "Remove Riley's sunglasses, open my eyes, make Engel smile"; "Photos uses images from your private face groups to generate personalized, accurate edits" [sourced: https://blog.google/products-and-platforms/products/photos/nano-banana-ai-templates-ask-photos/, 2025-11-11].

**What Ask Photos can and cannot do (Google help, re-fetched 2026-11-03)**: example prompts "Photos that'd make great phone backgrounds" and "What did I eat on my trip to Barcelona?"; it can also edit photos from plain-language instructions. Requirements: "To use Ask Photos, you need to confirm your 'me' face group" and you must meet the "Gemini features in Photos requirements" (linked separately). Limitations: "You can only use Ask Photos with images that are backed up"; "This feature is still experimental, so it may give unexpected or inaccurate results"; "This experimental feature from Google Labs won't always get it right". Availability: "Currently, Ask Photos is rolling out to a select number of countries and regions, and is available in several languages." Off switch: Photos settings > Preferences > Gemini features in Photos > "Search with Ask Photos" (or "Use Gemini in Photos" for all) [sourced: https://support.google.com/photos/answer/15318661, accessed 2026-11-03]. 2026 user complaints ("Did Gemini ruin search in Photos?") were reported by PhoneArena, but the page returned 403 on fetch and is seen only via a search snippet [unknown — unverified secondary; https://www.phonearena.com/news/Gemini-broke-Google-Photos-search-and-users-arent-happy_id180791].

**Gemini app ↔ Google Photos connector: exists since March 2025, read-only-ish.** Dating: the Gemini app release notes entry dated 2025.03.13 says Gemini can now "connect to more of your apps like Calendar, Notes, Tasks, Google Photos, Youtube, and Google Maps"; a 2026.01.20 entry again lists "Gmail, Photos, YouTube, and Search" among connected apps [sourced: https://gemini.google/release-notes/, entries 2025-03-13 and 2026-01-20, accessed 2026-11-03]. Requirements: personal account (no work/school/supervised), 18+, Keep Activity on, Face Groups on with "me" selected, Estimate missing locations on; "This feature isn't available in some United States regions." Can: find photos by face groups, saved relationships, date/location, description; answer questions about photo contents; open in Photos. Cannot: "Use the editing features within Google Photos", add face groups/names/locations, "create, edit, or move albums"; "the search results are provided directly by Google Photos, not Gemini"; export covers text only [sourced: https://support.google.com/photos/answer/17597604, accessed 2026-11-03; https://support.google.com/gemini/answer/15734842, accessed 2026-11-03].

**April 2026 — "Personal Intelligence"**: Gemini "can use actual images of you and your loved ones to guide the image generation process" using Photos people/pet labels; rolling out to "eligible Google AI Plus, Pro and Ultra subscribers in the U.S."; opt-in; "The Gemini app does not directly train its models on your private Google Photos library" [sourced: https://blog.google/innovation-and-ai/products/gemini-app/personal-intelligence-nano-banana/, 2026-04-16].

**Sept 2026 — Gemini Spark agent manages Google Photos**: can edit images, curate albums, auto-build shared albums, turn a flyer photo into a calendar event, run workflows; rolling out "to eligible Gemini AI Pro and Ultra subscribers in the U.S. in English"; "The company didn't say if or when it would roll out more broadly to international markets" [sourced: https://techcrunch.com/2026/09/04/googles-gemini-spark-can-now-manage-your-google-photos-library/, 2026-09-04].

**Partner sharing**: "You can use partner sharing with one person at a time"; "Face Groups isn't perfect"; "Sharing photos of specific people isn't available in all geographic regions"; "You can only invite someone with a Google Account" [sourced: https://support.google.com/photos/answer/7378858, accessed 2026-11-03]. Cap is 1 partner [sourced: same]. **Face identities do not cross accounts** — this is stated on Google's face-groups help page, not the partner-sharing page: "By default, your face groups and labels are only visible to you."; "Face groups aren't shared when you share photos."; "Face labels are private to each account and aren't shared across accounts." [sourced: https://support.google.com/photos/answer/6128838, accessed 2026-11-03]. No Google account-merge feature was found [unknown].

**Open AI access to Photos**: Google's own Gemini can read Photos (connector since 2025-03-13, above). Third-party apps lost library read access: Google's Library API updates page says "These changes will take effect March 31, 2025"; the `photoslibrary.readonly`, `photoslibrary.sharing` and `photoslibrary` scopes "will be removed from the Library API after March 31, 2025"; "You can now only list, search, and retrieve albums and media items that were created by your app"; calls relying on the removed scopes "will return a 403 PERMISSION_DENIED after March 31, 2025" [sourced: https://developers.google.com/photos/support/updates, accessed 2026-11-03]. The Gemini connector is Google-to-Google only; no MCP or third-party equivalent was found [unknown — none found].

### Q3. Independents

**Ente** (ente.com). Pricing (USD): Free 10 GB; 50 GB $2.49/mo or $29.88/yr; 200 GB $4.99/mo or $59.88/yr; 1 TB $9.99/mo or $119.88/yr; 2 TB $19.99/mo or $239.88/yr. Family: "You can add up to 5 family members and share your available storage space with them at no extra cost. Each member will get their own private space, and can only access their own photos." ML: "On-device face detection and grouping", magic search "in natural language", "Zero knowledge AI". Import: "simple migration process from both Google and Apple" (export → drop into desktop app). GitHub badge 29k stars; Discord 5k [sourced: https://ente.com/pricing, accessed 2026-11-03]. Open-source status: repository ente-io/ente is "AGPL-3.0 license", 29.9k stars, "End-to-end encrypted cloud for everything" [sourced: https://github.com/ente-io/ente, accessed 2026-11-03]. Scale: "over 150,000 registered customers", "over 165 million photos", 12 employees, bootstrapped ("We don't want to take venture money at the moment") [sourced: https://techcrunch.com/2025/04/01/ente-wants-to-take-on-google-photos-with-its-privacy-first-photo-storage-service/, 2025-04-01]. ARR: a founder LinkedIn post reportedly claims >$1M ARR; seen only in a search snippet of a profile page, not the post itself [unknown — unverified secondary]. Paying-user count [unknown]. Note: family plan is shared *storage*, not a merged library — each member's photos stay private to them.

**Immich** (immich-app/immich). 118.0k stars, 7.5k forks, AGPL-3.0 [sourced: https://github.com/immich-app/immich, accessed 2026-11-03]. Features table: "Facial recognition and clustering" (mobile+web), "Search by metadata, objects, faces, and CLIP", "Background backup" (mobile), "Partner Sharing" [sourced: same]. FUTO: the core team went full-time on 2024-05-01; FUTO provides compensation for the core team plus financial, technical, legal and administrative support; no dollar amount is stated; "Immich will continue to be licensed under AGPL without a CLA"; "no paywalled features" [sourced: https://immich.app/blog/2024/immich-core-team-goes-fulltime, 2024-05-01]. FUTO funding amount [unknown — not disclosed in the blog]. v2.0.0 "Stable" 2025-10-01: 78,000 stars then, 1,558 contributors, 31,500 Discord, 36,000 Reddit; "Surviving the controversial announcement about joining FUTO"; "we will never implement paywalled features"; plans "additional paid services" [sourced: https://immich.app/blog/v2.0.0-release, 2025-10-01]. v3.0.0 2026-07-01: Android background backup previously "limited to newly taken photos", now periodic full-library upload; iOS background refresh "now runs sync and upload work in parallel" but must start "within the short time window iOS allows" [sourced: https://immich.app/blog/v3.0.0-release, 2026-07-01]. Hosting model: self-hosted only; no first-party cloud. User count [unknown — only community sizes above]. MCP: no official server; at least 4 community servers verified (homeserverhq/immich-mcp "135 tools", okopok/immich-mcp "276 tools" generated from OpenAPI, JoeRu/mcp4immich v1.0.0 for Immich 2.x/3.x, barryw/ImmichMCP with CLIP search) [sourced: https://github.com/homeserverhq/immich-mcp, https://github.com/okopok/immich-mcp, https://github.com/JoeRu/mcp4immich, https://github.com/barryw/ImmichMCP, accessed 2026-11-03]. Partner sharing exists but each user keeps their own library; cross-user face identity merge [unknown — not documented].

**PhotoPrism**. Community edition free/open source; Essentials €2.00/mo, Plus from €6.00/mo, "billed annually" [sourced: https://www.photoprism.app/editions/, accessed 2026-11-03]. "People & Faces" is listed on the features page as a label without a per-edition value; whether face recognition is in the free tier is an inference, not stated [sourced: https://www.photoprism.app/features/, accessed 2026-11-03 — inference flagged]. Managed hosting via PikaPods from $6.50/mo [sourced: editions page]. Note: the editions page's price cards render "€ 200 / mo" / "€ 600 / mo" (dropped decimals); the table values €2.00 / €6.00 are used here.

**Mylio Photos**. Plans page shows "Mylio Personal" (Individual and Family), "Mylio Business", "NEW. Mylio Family." and optional "Mylio SecureCloud"; buttons read "Get Special Offer" and no price is printed [sourced: https://mylio.com/plans/ and https://mylio.com/pricing/, accessed 2026-11-03]. List prices [unknown — also tried apps.apple.com/us/app/mylio-photos/id908257220 (404), en.wikipedia.org/wiki/Mylio (404), mylio.com/about/ (no pricing)]. Concierge page (fetched fine 2026-11-03; the earlier "404" note was wrong): "Three sessions with a professional photo manager (1 hour each session)"; the page shows "$299" and "$450" without labelling $450 as a former price; the FAQ describes "a $299 plan for photo management services" and "a $379 plan that includes the same photo management services plus a 1-year subscription to Mylio Photos+", with "the Mylio Photos+ subscription renews annually at $99"; "up to 50% discount on premium photo scanning services" [sourced: https://mylio.com/concierge/, accessed 2026-11-03 — page is internally inconsistent on $379 vs $450]. The Photo Managers: "over 700 members worldwide", certification program; joint RootsTech 2024 booth [sourced: https://www.einpresswire.com/article/689981890/mylio-and-the-photo-managers-join-forces-at-rootstech-2024, 2024-02]. Face recognition "fully offline"; SpaceSaver keeps device storage small; "no internet needed" AI [sourced: mylio.com/pricing, accessed 2026-11-03]. Model: local-first, device sync, optional SecureCloud. Mylio's earlier incarnation / founding history [unknown — about page carries only "©2025 MYLIO, LLC"; Wikipedia page 404].

**Amazon Photos**. Amazon's explainer (undated; "Written by Amazon Staff"; says "more updates to the Amazon Photos experience coming later in 2026" and describes "a redesigned mobile app experience") states Prime members get "unlimited photo storage and 5 GB of video storage included"; extra video "50 GB for $0.99/month"; natural-language search examples "beach sunset last summer" / "kids playing in the snow"; Alexa can show "your trip to Hawaii or a photo of your dog at the beach"; groups share with "up to 50 others at once" [sourced: https://www.aboutamazon.com/news/amazon-prime/how-to-use-amazon-photos-storage, undated, accessed 2026-11-03]. Alexa Photo Frame (Oct 2026) was reported by PetaPixel but the page returns 403; price [unknown — unverified]. Prime scale: "We have more than 200 million Prime members worldwide" [sourced: https://www.aboutamazon.com/news/company-news/2020-letter-to-shareholders, 2020 letter published April 2021]. Implication: the price floor for consumer photo storage for Prime households is $0 [estimated: Prime bundle includes unlimited photos at no extra charge, per the Amazon page above].

**Synology Photos / Nextcloud Memories / LibrePhotos / Lychee / Photoview** (primary docs, re-sourced). Synology Photos: automatic albums by "facial and object recognition"; "Shared Space" to "collaborate with selected users on a complete, folder-based media library"; background mobile backup; FAQ: "No, Synology Photos requires a Synology NAS to privately store your photos." [sourced: https://www.synology.com/en-us/dsm/feature/photos, accessed 2026-11-03]. Nextcloud Memories: "Fast, modern and advanced photo management suite. Runs as a Nextcloud app."; AGPLv3; 3.9k stars; "Group photos by people and objects, powered by recognize and facerecognition" (i.e., face grouping depends on the separate Recognize / Face Recognition Nextcloud apps); albums can be shared [sourced: https://github.com/pulsejet/memories, accessed 2026-11-03]. Photoview: "Photo gallery for self-hosted personal servers"; AGPL-3.0; 6.6k stars; "Faces will automatically be detected in photos, and photos of the same person will be grouped together."; "Each user is created along with a path on the local filesystem" [sourced: https://github.com/photoview/photoview, accessed 2026-11-03]. Lychee: MIT; 4.3k stars; README has no face-recognition or AI feature line [sourced: https://github.com/LycheeOrg/Lychee, accessed 2026-11-03]. LibrePhotos: MIT; 8.1k stars; "Face detection and clustering: name a person once and the rest is suggested"; "Tags and generated captions for every photo"; "Multiple users, shared albums and public links"; "8 GB+ RAM is strongly recommended" [sourced: https://github.com/LibrePhotos/librephotos, accessed 2026-11-03]. None documents cross-account identity merge [unknown; none claimed]. (The earlier draft attributed three of these claims to a ZimaSpace vendor blog that does not contain them; that citation is dropped.)

**Pixelfed** (in the brief's list). "Photo Sharing. For Everyone."; "open-sourced software licensed under the AGPL license"; 7.1k stars; repository topics "activitypub", "federation", "fediverse" [sourced: https://github.com/pixelfed/pixelfed, accessed 2026-11-03; https://pixelfed.org/ says only "Decentralized social media"]. It is a federated *social* photo network (Instagram-like), not a private library/archive; no face recognition or private-archive feature is documented [sourced: same — absence]. Not a competitor to this seed except as a publishing surface.

**Permanent.org** (nonprofit). "$10 per gigabyte of storage", one-time, "no recurring fees"; 1 GB free [sourced: https://www.permanent.org/, accessed 2026-11-03]. Archive/user counts [unknown].

**Forever.com**. One-time "permanent" storage: 10 GB $179.99; 25 GB $349.99; 50 GB $529.99; 100 GB $899.99; 250 GB $1,999.99; 500 GB $3,499.99; 1 TB $5,999.99; 2 TB $10,999.99; "guaranteed for your lifetime plus 100 years"; portion goes to "FOREVER Guarantee Fund"; 24-month installments; succession/account-manager features [sourced: https://www.forever.com/pricing, accessed 2026-11-03]. Per-GB: $18.00 at 10 GB down to $5.50 at 2 TB [estimated: $179.99 ÷ 10 GB; $10,999.99 ÷ 2,000 GB, from the sourced table]. User count [unknown].

**Storyworth / Remento / Mixbook / Artifact** (adjacent memory products). Storyworth tiers reported at $59 / $109 / $199 first year, renewal $99/yr [sourced: https://memoirji.com/blog/storyworth-pricing-2026-buyer-guide/, page marked updated 2026-05-15 — secondary affiliate; storyworth.com not fetched]. Remento (primary): "A book of your loved one's life stories, told in their voice"; $99 initial purchase including one year of prompts and one hardcover book; renewal "$99/year" or "$12/month"; additional copies "$69 each" [sourced: https://www.remento.co/, accessed 2026-11-03]. Mixbook (primary): softcover photo books "Starting at $14.99"; site banner "45-55% off almost everything" on the day of access [sourced: https://www.mixbook.com/photo-books, accessed 2026-11-03]. Artifact (heyartifact.com; the brief's "Artifact"): recorded ~30-minute family-story interviews by professional interviewers, "$149" per interview, 10% off for two or more, "$35" per extra guest — and the homepage now says "Artifact is shutting down", no new Artifacts sold, completed interviews hosted "through 2024" [sourced: https://www.heyartifact.com/, accessed 2026-11-03, page undated]. Relevance: these monetize *curation output* (books, recorded stories), not storage — and one of them (Artifact) has already died at that price point.

### Q4. Vertical (brief; Track F covers depth)

**CompanyCam**. Pricing: Core $63/mo (1 user incl.), Crew $129/mo (3 users), Scale $199/mo (3 users), +$29/user billed annually; AI credits 10/100/unlimited; Enterprise "50+ users" [sourced: https://companycam.com/pricing, accessed 2026-11-03]. Valuation $2B as of Aug 2025, Series C led by B Capital, amount undisclosed by company [sourced: https://siliconprairienews.com/2025/11/companycam-reaches-unicorn-status-with-2-billion-valuation-a-first-for-a-nebraska-startup/, 2025-11-22]. Series C size [unknown — a $415M figure circulates on PitchBook, which returned 403 on fetch; company declined to disclose]. 2024 ARR $68M (up from $32M 2023) [sourced: https://getlatka.com/companies/companycam, 2024 — Latka estimate, secondary]. Scale: "over 140,000 contractors", ">1 billion photos" [sourced: https://jobs.insightpartners.com/companies/companycam, undated — secondary]. Why photos are a business here: timestamped/geotagged evidence → reports, invoicing, disputes; photos are a liability/record artifact, not a memory.

**HOVER**: total raised "$136.71M"; latest round "Series D", "$60M", "6 yrs ago" (no month given); no debt rounds listed [sourced: https://www.cbinsights.com/company/hover-inc, accessed 2026-11-03 — aggregator; PitchBook returned 403]. Pricing (primary): Starter "Get your first 3 projects for free"; Pro "$999/year"; Business "$2,999/year"; Enterprise custom; per-scan fees e.g. exterior simple structure $59 Starter / $39 Pro / $79 Business, roof simple $29 / $9 / $39 [sourced: https://hover.to/pricing, accessed 2026-11-03]. **Spectora** (primary): "$109 /month" or "$1090 /year"; additional inspectors "$99/month" or "$999/year"; websites $699–$1,599/yr plus setup fees [sourced: https://www.spectora.com/pricing/, accessed 2026-11-03]; ~$5.9M 2025 revenue [sourced: https://getlatka.com/companies/spectora.com, 2025 — Latka estimate, secondary]. **HappyCo**: "$52 million in funding" led by Camber Creek, Jan 2022 (the article does not label the round) [sourced: https://www.connectcre.com/stories/happyco-expands-platform-with-52m-in-funding/, 2022-01-20]; cumulative total [unknown — PitchBook 403]; pricing is quote-only ("Only pay for what you need", "Book a Demo") [sourced: https://www.happy.co/pricing, accessed 2026-11-03].

### Q5. The graveyard (2010–2026)

| Company | Years | What it charged | Why it died | Lesson for this seed |
|---|---|---|---|---|
| Everpix | 2011–2013 [sourced: "Everpix was started in 2011"; shutdown announced 2013-11-05, https://github.com/everpix/Everpix-Intelligence, accessed 2026-11-03] | $5/mo or $49/yr unlimited [sourced: https://venturebeat.com/business/goodbye-everpix-photo-storage-startup-shuts-down-as-bills-pile-up, 2013-11-05] | "unable to secure sufficient funding in order to properly scale"; an "impending bill from Amazon Web Services, estimated at $35,000, precipitated the decision"; 55,000 users; $2.3M raised [sourced: VentureBeat, 2013-11-05]. Company's own post-mortem: "50,000 signed up users (including 7,000 subscribers)", "subscription sales of $40,000 / month during the last 3 months", "400 millions photos imported", "$2.3M raised over its lifetime" [sourced: https://github.com/everpix/Everpix-Intelligence, accessed 2026-11-03] | Storage COGS + ~14% paying base [estimated: 7,000 ÷ 50,000, company README] + free iCloud/Google = no runway. Product love ≠ business. |
| Picturelife | 2012–2016 [sourced: $4M raise 2012-11-02 (TechCrunch); shutdown 2016-08 (DPReview), below] | Paid tiers (prices not sourced) [unknown] | $4M raised 2012 [sourced: https://techcrunch.com/2012/11/02/charles-forman-4m-picturelife/, 2012-11-02]; acquired by StreamNation Jan 2015 [sourced: https://tech.co/news/streamnation-acquires-picturelife-cloud-photo-service-2015-01, 2015-01]; shut Aug 2016 citing "a challenging economic environment"; SmugMug rescued photos but "weren't interested in acquiring Picturelife's business" [sourced: https://www.dpreview.com/news/5910446180/picturelife-shutters-service-user-content-migrates-to-smugmug, 2016-08-23]. Hosting cost: a figure of ~$1M/yr AWS attributed to the ex-CEO circulated in the earlier draft without a URL; no primary could be fetched [unknown] | Acquirer couldn't carry the hosting bill either. Nobody wants to buy a storage liability. |
| Loom (photo) | –2014 [sourced: "In April 2014, Dropbox acquired photo-sharing company Loom", https://en.wikipedia.org/wiki/Dropbox, accessed 2026-11-03 — secondary] | — [unknown] | "would be shut down and integrated with the then-recently announced Carousel" [sourced: same] | Acqui-hire exit, product killed. |
| Dropbox Carousel | 2014–2016 [sourced: introduced April 2014, https://en.wikipedia.org/wiki/Dropbox; shut 2016-03-31, Dropbox blog below] | Free (Dropbox storage) [sourced: Wikipedia Dropbox, "combines the photos in your Dropbox with the photos on your phone"] | Dropbox: "Over the past few months, we've increased our team's focus on collaboration and simplifying the way people work together." … "we've made the difficult decision to shut down Carousel and Mailbox"; Carousel shut March 31, 2016; key photo features moved into the Dropbox app [sourced: https://blog.dropbox.com/topics/company/saying-goodbye-to-carousel-and-mailbox, 2015-12-07; https://techcrunch.com/2015/12/07/failing-to-find-users-dropbox-will-shut-down-mailbox-in-february-2016-and-carousel-in-march/, 2015-12-07]. (The earlier draft's "vast majority of our users prefer…" quote is not in either source and is withdrawn.) | Even Dropbox couldn't make a standalone photo app stick next to its own storage product. |
| Ever / Everalbum | 2013–2020 [unknown — founding year and Aug-2020 shutdown widely reported but not in any reachable primary; FTC complaint dates the "Friends" face feature to February 2017] | Freemium [unknown — prices not sourced] | FTC complaint: when the Friends feature launched (Feb 2017) Everalbum "enabled face recognition by default for all users of the Ever mobile app" and "did not provide users … an option to turn off or disable" it; outside Texas, Illinois, Washington and the EU, "face recognition was enabled by default" until April 2019 [sourced: https://www.ftc.gov/system/files/documents/cases/1923172_-_everalbum_complaint_final.pdf, accessed 2026-11-03]. FTC press release 2021-01-11: settlement requires deleting "any facial recognition models or algorithms developed with Ever users' photos or videos" [sourced: https://www.ftc.gov/news-events/news/press-releases/2021/01/california-company-settles-ftc-allegations-it-deceived-consumers-about-use-facial-recognition-photo, 2021-01-11]. Final order issued 2021-05-06 defines "Affected Work Product" as "any models or algorithms developed in whole or in part using Biometric Information" and orders it deleted within 90 days [sourced: https://www.ftc.gov/system/files/documents/cases/1923172_-_everalbum_decision_final.pdf, 2021-05-06] | Consumer face data is a regulatory landmine; consent must be explicit; pivoting consumer face data to B2B (Paravision) drew the FTC and an algorithm-disgorgement order. |
| Lifecake (Canon) | –2020 [sourced: closure 2020-06-30, https://news.ycombinator.com/item?id=23033676, 2020-04; launch year unknown] | Subscription [unknown — price not sourced] | "Lifecake will be closing on 30th June, 2020"; users pointed to rebranded app "BackThen"; a commenter: the new pricing "is considerably more expensive" (no multiplier given) [sourced: same HN thread — secondary] | Corporate-owned family apps get shut when strategy shifts. |
| Picasa | 2002–2016 [sourced: released 2002-10-15; desktop app discontinued 2016-03-15; Picasa Web Albums closed 2016-05-01, https://en.wikipedia.org/wiki/Picasa, accessed 2026-11-03 — secondary; TidBITS and Google's blog post were unreachable (bot check / 404)] | Free | Google retired it in favour of Google Photos: desktop support ended 2016-03-15, web service 2016-05-01 [sourced: same] | Platform consolidates its own products too. |
| Google+ Photos | –2015 [sourced: Google Photos introduced "a new, standalone product" on 2015-05-28, https://blog.google/products/photos/picture-this-fresh-approach-to-photos/, 2015-05-28; Google+ Photos start year unknown] | Free; Google Photos launched with "unlimited, high-quality photos and videos, for free" up to 16 MP / 1080p [sourced: same] | Superseded by standalone Google Photos [sourced: same — the post does not itself name Google+] | Same. |
| Photobucket | 2003– [sourced: founded 2003, https://en.wikipedia.org/wiki/Photobucket, accessed 2026-11-03 — secondary] | Free → paid hosting (2017): only the "US$399.99 per year" plan "permitted third party hosting and linking to forums"; a US$99/yr plan for external linking [sourced: Wikipedia Photobucket, 2017-06-28 entry — secondary; PetaPixel 2017 unreachable (403)] | Broke embedded images across the web in June 2017 [sourced: same]. 2023 deletion of inactive free-account images: cited to alternativeto.net in the earlier draft; page 403 and not on Wikipedia [unknown — unverified] | Hostage pricing destroys trust; free-tier liabilities get purged eventually. |
| Flickr | 2004– [sourced: launched 2004-02-10, https://en.wikipedia.org/wiki/Flickr, accessed 2026-11-03] | 1 TB free from 2013-05-20 → free accounts "limited to 1,000 photos or videos" announced 2018-11-01, deletion first set for 2019-02-05 then 2019-03-12 [sourced: Wikipedia Flickr — secondary]; Pro "$5.99 per month" or "pay $50 per year" [sourced: https://techcrunch.com/2018/11/01/flickr-revamps-under-smugmug-with-new-limits-on-free-accounts-unlimited-storage-for-pros/, 2018-11-01] (Wikipedia gives "US$60 per year" — sources conflict) | Yahoo → Verizon/Oath → SmugMug (2018-04-20) [sourced: Wikipedia Flickr]; cap justified because "The vast majority of free users have fewer than 1,000 photos uploaded" [sourced: TechCrunch 2018-11-01 — no percentage given; the earlier "97%" figure is withdrawn]. Wikipedia adds that in March 2022 Flickr said it had not deleted any photos for exceeding limits [sourced: Wikipedia Flickr — secondary] | "Free unlimited" is a subsidy that ends when the subsidizer changes. |
| Keepy | 2013– [unknown — launch year unsourced] | Freemium [unknown] | Status [unknown — keepy.me and www.keepy.me both returned 503 on 2026-11-03] | Niche (kids' artwork) may survive small; could not verify it is alive. |
| ThisLife (Shutterfly) | 2010–2016 [sourced: "ThisLife initially launched in 2010"; "acquired by Shutterfly in January 2013 … reported to cost $25 million"; "transitioned This Life into the all-new Shutterfly Photos platform in 2016", https://en.wikipedia.org/wiki/Shutterfly, accessed 2026-11-03 — secondary] | — [unknown] | Aggregator of "photos from social networks, mobile devices, personal computers, and cloud storage"; $2.75M seed (Madrona); absorbed into Shutterfly Photos [sourced: same] | The "aggregate all your sources" pitch was bought for $25M and folded into a print funnel. |
| Lifetouch (Shutterfly) | –2018 (acquired) [sourced: "In 2018, Shutterfly acquired Lifetouch for $825 million", Wikipedia Shutterfly — secondary] | School/portrait photography (not a consumer storage app) | Not dead — acquired; a photography *services* business, not a library product [sourced: same] | Photos as a services/print business command real M&A value; storage does not. |
| Mosaic (Mixbook) | ~2012– [sourced: Mixbook "released a photo book app called Mosaic" (implied 2012), https://en.wikipedia.org/wiki/Mixbook, accessed 2026-11-03 — secondary] | Photo books (price not sourced) [unknown] | Discontinuation [unknown — not stated in the fetched source] | Output product; no storage liability. |
| Lyve (Seagate) | [unknown] | [unknown] | [unknown — en.wikipedia.org/wiki/Lyve_Minds returned 404; Seagate's Wikipedia page mentions only Lyve Rack (2020) and Lyve Cloud (Feb 2021), not Lyve Minds/Lyve Home; WebSearch unavailable] | — |
| Pixieset (consumer?) | n/a | Client Gallery plans $0 / $8 / $16 / $24 / $40 per mo billed annually [sourced: https://pixieset.com/pricing/, accessed 2026-11-03] | Not dead and not consumer: "An all-in-one platform for modern photographers"; no family/consumer product listed [sourced: same] | Pro-photographer delivery is a separate market. |
| "Memories" features | n/a | n/a | Apple Memories, Google Photos Memories and Facebook "On This Day"-style features are platform features, not startups; none was researched as a standalone company here [unknown — no primary fetched] | The platforms own "resurfacing". |
| Tinybeans (ASX:TNY) | 2012– [sourced: "Founded in Sydney, Australia in 2012"; ASX listing April 2017 with "1.6 million parents and family members", https://en.wikipedia.org/wiki/Tinybeans, accessed 2026-11-03 — secondary] | Tinybeans+ subscription; price [unknown — tinybeans.com, /pricing (404), /plus (404), /tinybeans-plus (404), /gift/purchase (no prices rendered) tried; help.tinybeans.com not resolvable from this session] | NOT dead: FY25 revenue US$4.82M (-11%), sub revenue US$3.32M (+12%) [sourced: https://announcements.asx.com.au/asxpdf/20250821/pdf/06n4h84f2x4yl9.pdf, 2025-08-21]; FY26 revenue US$6.49M (+35%), sub revenue US$4.82M (+45%), first Adjusted EBITDA profit US$427k, ~95k paid subs post-Qeepsake, 96% annual retention, cash US$1.64M, costs cut ~33% [sourced: https://newshub.medianet.com.au/2026/08/tinybeans-asxtny-posts-maiden-adjusted-ebitda-profit-in-fy26/168355/, 2026-08-27] | A family-sharing app can reach break-even at ~95k subs by consolidating (Qeepsake) and cutting ~33% costs [sourced: medianet 2026-08-27]; it's a small business, not a venture outcome (micro-cap). |
| FamilyAlbum (Mixi) | –present [launch year unknown — not in fetched sources] | Free: "Free Unlimited Storage", "no fees or storage limits", "Only family members you invite can see your album" [sourced: https://family-album.com/en, accessed 2026-11-03]. Premium: One "$2.99 USD/month"; Family "$5.99 USD/month" or "$59 USD/year"; Family Pro "$10.99 USD/month" or "$109 USD/year"; first month free [sourced: https://family-album.com/en/premium, accessed 2026-11-03] | NOT dead, growing: 30M registered users 2026-05-07; ~65% of Japanese parents (Dec 2024); ">40% of users outside Japan, North America 20%" [sourced: https://pdf.irpocket.com/C2121/Kdx3/R43P/MfKg.pdf, 2026-05-07]. Premium subscriber count [unknown] | Child-centric, invite-only sharing with free unlimited storage subsidised by a large parent (Mixi) + print/commerce upsell works; the wedge is a newborn, not an archive. |

Pattern: the independents that died sold *storage of the whole library* to consumers against a $0 platform price; the survivors sell a *narrow social object* (a baby's album) or *output* (books, prints) or run on a subsidy (Prime, Mixi). Even output-only players can die (Artifact, Q3).

### Q6. Who has shipped cross-relative library merge + cross-generation face clustering?

- **Apple**: Shared Library caps at 6 people, "You can join one Shared Library", no account merge [sourced: Q1, support.apple.com/HT213248]. Does not merge existing libraries across generations; it forward-shares media without library structure.
- **Google**: Partner sharing is 1 partner [sourced: support.google.com/photos/answer/7378858]; "Face labels are private to each account and aren't shared across accounts" [sourced: https://support.google.com/photos/answer/6128838]; no merge.
- **Ente**: family plan shares storage, "each member … can only access their own photos" [sourced: ente.com/pricing]. Not a merge.
- **Immich**: partner sharing per user; no cross-user face identity merge documented [unknown].
- **MyHeritage**: photo tools named on its knowledge-base page: LiveMemory, Deep Nostalgia, In Color, Photo Enhancer, Photo Repair, PhotoDater, Reimagine, Photo Storyteller; the page describes face *detection* for animation ("identifies the faces in your photos") and references a webinar on "Organizing and Tagging Photos with the MyHeritage Mobile App", but contains no statement on whether face tagging is restricted to deceased people [sourced: https://education.myheritage.com/article/myheritage-photo-features/, accessed 2026-11-03]. The earlier "deceased individuals only" claim came from an affiliate blog that returns a bot-challenge page and is withdrawn [unknown — myheritage.com/photos redirects to /incolor; /photo-tagger is 404]. Scope is historical/ancestor photos attached to a tree, not merging living relatives' phone libraries.
- **Ancestry** (primary, re-sourced): "Face Match uses AI technology to compare faces in your photos with photos of deceased people available on Ancestry."; "To protect the privacy of living people, Face Match is only designed to help identify deceased people."; "Face Match is available with an active Ancestry family history membership."; it runs only when the user chooses [sourced: https://help.ancestry.com/hc/en-us/articles/53933332427283, accessed 2026-11-03; launch date not stated — the earlier dnyuz.com citation 404s and is dropped]. Photo Insights: "AI-powered feature that helps you uncover unexpected details about your historical family photos" (suggested dates, locations, historical details); Ancestry "does not use your private family photos to train AI models" [sourced: https://help.ancestry.com/hc/en-us/articles/53933301940627, accessed 2026-11-03].
- **FamilySearch Memories**: free storage for "your most cherished family photographs, historical records, and other heirloom family documents" [sourced: https://www.familysearch.org/en/blog/free-cloud-storage-familysearch-memories, 2021-02-11]. File-size and per-person count limits [unknown — the blog states none; developer docs returned 403; church news page 503; the help-center URL tried redirects to a site search that was not followed]. Tree-centric, not library-centric.
- **Vivid-Pix Memory Station**: scanning/restore software; "Memory Station Home and pRT Family Edition Bundle" $228.99, includes "Memory Station Home Edition Software for Windows" [sourced: https://www.vivid-pix.com/product/memory-station-home, accessed 2026-11-03]. Standalone V5 price [unknown — the RootsTech 2026 blog URL cited earlier 404s; /software page lists no prices]. Digitisation, not merge.
- **Mylio + The Photo Managers**: the closest thing to "merge the family's libraries" is a *human service* — a certified photo organizer consolidating into one Mylio catalog ($299 concierge plan; $379 with a Photos+ year) [sourced: Q3, mylio.com/concierge]. This is evidence the job exists and is currently done by hand.

**Verdict: gap, not graveyard — but a thin one, and now resting on fewer verified legs.** Nobody has shipped the merged multi-account family archive with cross-generation face identity as a product. The platforms cap sharing at 1–6 people and never merge accounts or face labels (verified, primary). Ancestry restricts face matching to deceased people by design (verified, primary); MyHeritage's restriction is unverified; FamilySearch is tree-centric. The open-source tools merge storage, not identity. The absence could be a gap or could reflect that the job is low-frequency (done once, by a human organizer) — Track F/customer research must decide.

---

## 3. Seed assumptions tested

**"Standalone voice photo search/editing app is already native in iOS 27 Siri AI and Google Ask Photos" (founder's prior rejection)** — **PARTIAL (search: holds; editing: unproven).**
- For: Siri AI (iOS 27, 2026-09-14) searches photos by natural language with personal context [sourced: Apple 2026-09-14]; Google "Help me edit" takes voice/text edit prompts (Nov 2025) and Gemini Spark edits/curates (Sept 2026, US, paid tiers) [sourced: Google 2025-11-11; TechCrunch 2026-09-04].
- Against: Apple's primary text never says Siri edits photos by voice; WWDC26 session 121's description says "natural language abilities to edit and write emails, texts, and documents" [sourced: developer.apple.com/videos/play/wwdc2026/121/]; MacRumors' roundup has no sentence saying Siri edits photos [sourced: macrumors.com/roundup/ios-27/]. Siri AI unavailable on EU iOS and in China at launch; English-only beta [sourced: Apple 2026-09-14]. Ask Photos is "still experimental", limited to backed-up images, with a documented 2025 pause [sourced: Google help 15318661; Android Police 2025-06-04].
- Net: rejecting the *standalone* app is still right (platform search is good enough and free), but the rejection reason is only half-true. The real reason is distribution, not feature parity.

**A4 — "Apple and Google will not ship cross-account family merge + open AI access themselves"** — **PARTIAL: merge half holds; open-AI-access half is being eroded by Google, not by Apple.**
- Merge: neither has shipped account-to-account merge; Apple caps at 6 and one Shared Library per person [sourced: Apple HT213248]; Google at 1 partner [sourced: Google 7378858]; "Face labels are private to each account and aren't shared across accounts" [sourced: Google 6128838]. Holds as of 2026-11-03.
- AI access: Google's *own* Gemini reads Photos (connector dated 2025-03-13 in Gemini release notes), personalises generation from face groups (Apr 2026), and acts on the library via Spark (Sept 2026) — but only Google→Google, US, paid tiers, with no third-party/MCP path; third-party API read access to the whole library ended 2025-03-31 [sourced: Q2, developers.google.com/photos/support/updates]. Apple: Siri AI "already works seamlessly with apps from Apple's vast ecosystem of developers" and acts in third-party apps via App Actions / App Intents, but Apple's text describes Siri reaching *into* apps, not third-party models reaching into Photos; nothing says ChatGPT, Gemini or any external model can read the user's library [sourced: Apple 2026-09-14; macrumors.com/roundup/ios-27/]. Whether Apple's Foundation Models tool-calling or PhotoKit lets an app expose the library to a *third-party* model is not settled here (Apple developer doc pages did not render body text on fetch) [unknown]. So "open" (any model) access remains unshipped; "AI access" per se is shipped by Google. The seed's BYO-AI wedge must be defined as *model-agnostic* access, or Google has already shipped it for the Gemini-only case.

Other assumptions touched incidentally: A5 (unit economics) — graveyard evidence (Everpix: $35k AWS bill as tipping point [sourced: VentureBeat 2013-11-05], 7,000 subscribers at ~$40k/mo [sourced: Everpix README]) and Amazon's $0 Prime-bundled price [sourced: aboutamazon.com explainer] are negative evidence. Ente's reported >$1M ARR on 150k registered users would imply ≈$6.7/registered user/yr [estimated: $1M ÷ 150,000; ARR input is an unverified secondary claim, registered-user input is TechCrunch 2025-04-01]; *illustratively*, if ARPU were $60/yr (Ente's 200 GB annual price is $59.88 [sourced: ente.com/pricing]) that would be ≈11% paying [estimated: $6.7 ÷ $60 — illustrative only; ARPU is an assumption, not a measurement].

---

## 4. Numbers table

| Number | Value | Tag |
|---|---|---|
| iOS 26 release | 2025-09-15 | [sourced: macrumors.com/2025/09/15/apple-releases-ios-26/, 2025-09-15] |
| WWDC26 / iOS 27 dev beta | 2026-06-08 | [sourced: apple.com newsroom 2026-06-08] |
| iOS 27 / Siri AI public release | 2026-09-14 | [sourced: apple.com newsroom 2026-09-14] |
| Photos load speedup iOS 27 | up to 70% | [sourced: apple.com newsroom 2026-06-08] |
| iCloud Shared Photo Library participants | creator + 5 (6) | [sourced: support.apple.com/HT213248] |
| Shared Library OS requirement | iOS 16.1 / iPadOS 16.1 / macOS Ventura | [sourced: support.apple.com/HT213248] |
| Shared Library 7-day rule | <1 week members keep only own items when creator deletes | [sourced: support.apple.com/HT213248] |
| PowerPhotos price | $40 | [sourced: discussions.apple.com/thread/256192786, community; fatcatsoftware.com shows no price] |
| Google partner sharing partners | 1 | [sourced: support.google.com/photos/answer/7378858] |
| Gemini↔Photos connector date | 2025-03-13 | [sourced: gemini.google/release-notes, entry 2025.03.13] |
| Google Library API scope removal | 2025-03-31 | [sourced: developers.google.com/photos/support/updates] |
| Ask Photos pause report | 2025-06-04 | [sourced: androidpolice.com, 2025-06-04] |
| Ask Photos resume date | — | [unknown — PetaPixel 2025-06-27 unreachable (403)] |
| Ask Photos expansion | 100+ countries, 17 languages | [sourced: blog.google, 2025-11-11] |
| Gemini–Photos connector age req | 18+ | [sourced: support.google.com/gemini/answer/15734842] |
| Gemini Spark Photos rollout | US, English, AI Pro/Ultra | [sourced: techcrunch.com, 2026-09-04] |
| Ente free tier | 10 GB | [sourced: ente.com/pricing] |
| Ente 200 GB annual | $59.88/yr | [sourced: ente.com/pricing] |
| Ente 1 TB | $9.99/mo, $119.88/yr | [sourced: ente.com/pricing] |
| Ente 2 TB | $19.99/mo, $239.88/yr | [sourced: ente.com/pricing] |
| Ente family members | up to 5 | [sourced: ente.com/pricing] |
| Ente registered customers | >150,000 | [sourced: techcrunch.com, 2025-04-01] |
| Ente photos stored | >165M | [sourced: techcrunch.com, 2025-04-01] |
| Ente employees | 12 | [sourced: techcrunch.com, 2025-04-01] |
| Ente ARR | >$1M | [unknown — founder LinkedIn claim seen only in a search snippet; unverified] |
| Ente GitHub stars | 29.9k | [sourced: github.com/ente-io/ente, 2026-11-03] |
| Immich stars / forks | 118.0k / 7.5k | [sourced: github.com/immich-app/immich, 2026-11-03] |
| Immich FUTO full-time date | 2024-05-01 | [sourced: immich.app/blog/2024/immich-core-team-goes-fulltime] |
| Immich FUTO funding amount | — | [unknown — not disclosed] |
| Immich stars at v2.0.0 | 78,000 | [sourced: immich.app/blog/v2.0.0-release, 2025-10-01] |
| Immich contributors | 1,558 | [sourced: same] |
| Immich Discord / Reddit | 31,500 / 36,000 | [sourced: same] |
| Immich v3.0.0 date | 2026-07-01 | [sourced: immich.app/blog/v3.0.0-release] |
| Community Immich MCP servers verified | 4 | [sourced: the 4 GitHub repos listed in Q3] |
| PhotoPrism Essentials / Plus | €2.00/mo / from €6.00/mo (annual) | [sourced: photoprism.app/editions] |
| PikaPods hosted PhotoPrism | from $6.50/mo | [sourced: photoprism.app/editions] |
| Nextcloud Memories stars | 3.9k | [sourced: github.com/pulsejet/memories, 2026-11-03] |
| Photoview stars | 6.6k | [sourced: github.com/photoview/photoview, 2026-11-03] |
| Lychee stars | 4.3k | [sourced: github.com/LycheeOrg/Lychee, 2026-11-03] |
| LibrePhotos stars / RAM | 8.1k / 8 GB+ recommended | [sourced: github.com/LibrePhotos/librephotos, 2026-11-03] |
| Pixelfed stars | 7.1k | [sourced: github.com/pixelfed/pixelfed, 2026-11-03] |
| Mylio Photos+ renewal | $99/yr | [sourced: mylio.com/concierge FAQ, 2026-11-03] |
| Mylio Concierge plans | $299 (services) / $379 (with Photos+); $450 shown unlabelled | [sourced: mylio.com/concierge, 2026-11-03 — page inconsistent] |
| Mylio list prices | — | [unknown — hidden behind "Get Special Offer"] |
| The Photo Managers members | >700 | [sourced: einpresswire.com, 2024-02] |
| Amazon Photos Prime video storage | 5 GB | [sourced: aboutamazon.com explainer, undated] |
| Amazon extra video storage | 50 GB for $0.99/mo | [sourced: same] |
| Amazon group sharing | up to 50 | [sourced: same] |
| Prime members | >200M worldwide | [sourced: aboutamazon.com 2020 letter to shareholders, Apr 2021] |
| Alexa Photo Frame price | — | [unknown — PetaPixel 2026-10-28 unreachable (403)] |
| Permanent.org price | $10/GB one-time; 1 GB free | [sourced: permanent.org] |
| Forever.com 10 GB … 2 TB | $179.99 … $10,999.99 | [sourced: forever.com/pricing] |
| Forever.com $/GB range | $18.00 → $5.50 | [estimated: $179.99 ÷ 10; $10,999.99 ÷ 2,000] |
| Forever guarantee | lifetime + 100 years | [sourced: forever.com/pricing] |
| Remento | $99 incl. book; renew $99/yr or $12/mo; extra copies $69 | [sourced: remento.co, 2026-11-03] |
| Mixbook softcover | from $14.99; "45-55% off" banner | [sourced: mixbook.com/photo-books, 2026-11-03] |
| Artifact interview | $149; +$35 per extra guest; 10% off for 2+ | [sourced: heyartifact.com, undated — shutting down] |
| Storyworth tiers | $59 / $109 / $199; renew $99 | [sourced: memoirji.com, updated 2026-05-15 — secondary affiliate] |
| CompanyCam Core/Crew/Scale | $63 / $129 / $199 per mo | [sourced: companycam.com/pricing] |
| CompanyCam extra user | $29/user, annual | [sourced: same] |
| CompanyCam valuation | $2B (Aug 2025) | [sourced: siliconprairienews.com, 2025-11-22] |
| CompanyCam Series C size | — | [unknown — $415M aggregator figure; PitchBook 403; company declined] |
| CompanyCam ARR 2024 / 2023 | $68M / $32M | [sourced: getlatka.com estimate — secondary] |
| CompanyCam contractors / photos | >140,000 / >1B | [sourced: jobs.insightpartners.com, undated — secondary] |
| HOVER total raised | $136.71M | [sourced: cbinsights.com/company/hover-inc, 2026-11-03 — aggregator] |
| HOVER last round | Series D $60M, "6 yrs ago" | [sourced: same] |
| HOVER Pro / Business | $999/yr / $2,999/yr | [sourced: hover.to/pricing, 2026-11-03] |
| Spectora base | $109/mo or $1,090/yr; +$99/mo or $999/yr per inspector | [sourced: spectora.com/pricing, 2026-11-03] |
| Spectora 2025 revenue | ~$5.9M | [sourced: getlatka.com estimate — secondary] |
| HappyCo funding Jan 2022 | $52M (round unlabelled) | [sourced: connectcre.com, 2022-01-20] |
| Everpix price | $5/mo or $49/yr | [sourced: venturebeat.com, 2013-11-05] |
| Everpix users / raised / AWS bill | 55,000 / $2.3M / ~$35,000 | [sourced: venturebeat.com, 2013-11-05] |
| Everpix signed-up / subscribers / MRR / photos | 50,000 / 7,000 / $40,000 / 400M | [sourced: github.com/everpix/Everpix-Intelligence] |
| Everpix paying share | ≈14% | [estimated: 7,000 ÷ 50,000] |
| Picturelife raised 2012 | $4M | [sourced: techcrunch.com, 2012-11-02] |
| Picturelife shutdown | Aug 2016 | [sourced: dpreview.com, 2016-08-23] |
| Picturelife AWS cost | — | [unknown — no primary reachable] |
| Loom acquired | Apr 2014 | [sourced: en.wikipedia.org/wiki/Dropbox — secondary] |
| Carousel launch / shutdown | Apr 2014 / 2016-03-31 | [sourced: Wikipedia Dropbox; blog.dropbox.com 2015-12-07] |
| Everalbum Friends launch / default-on until | Feb 2017 / Apr 2019 | [sourced: FTC complaint PDF] |
| Everalbum FTC announcement / order issued | 2021-01-11 / 2021-05-06 | [sourced: ftc.gov press release; ftc.gov decision PDF] |
| Ever app shutdown date | — | [unknown — not stated in FTC documents; Perkins Coie page 404] |
| Lifecake closure | 2020-06-30 | [sourced: news.ycombinator.com/item?id=23033676 — secondary] |
| Picasa release / desktop end / web end | 2002-10-15 / 2016-03-15 / 2016-05-01 | [sourced: en.wikipedia.org/wiki/Picasa — secondary] |
| Google Photos launch | 2015-05-28 | [sourced: blog.google picture-this post] |
| Photobucket founded / 2017 hosting plan | 2003 / US$399.99/yr (US$99/yr linking tier) | [sourced: en.wikipedia.org/wiki/Photobucket — secondary] |
| Photobucket 2023 free-account purge | — | [unknown — alternativeto.net 403; not on Wikipedia] |
| Flickr launch / 1 TB free / SmugMug | 2004-02-10 / 2013-05-20 / 2018-04-20 | [sourced: en.wikipedia.org/wiki/Flickr — secondary] |
| Flickr free cap / deletion dates | 1,000 items; 2019-02-05 → 2019-03-12 | [sourced: Wikipedia Flickr; cap announced 2018-11-01 per TechCrunch] |
| Flickr Pro | $5.99/mo or $50/yr (TechCrunch) vs US$60/yr (Wikipedia) | [sourced: techcrunch.com 2018-11-01; Wikipedia — conflict noted] |
| Flickr free users under cap | "vast majority" (no %) | [sourced: techcrunch.com, 2018-11-01] |
| ThisLife launch / acquired / absorbed | 2010 / Jan 2013 for $25M / 2016 | [sourced: en.wikipedia.org/wiki/Shutterfly — secondary] |
| ThisLife seed | $2.75M | [sourced: same] |
| Lifetouch acquisition | 2018, $825M | [sourced: same] |
| Pixieset plans | $0 / $8 / $16 / $24 / $40 per mo (annual) | [sourced: pixieset.com/pricing, 2026-11-03] |
| Tinybeans founded / listed / users at listing | 2012 / Apr 2017 / 1.6M | [sourced: en.wikipedia.org/wiki/Tinybeans — secondary] |
| Tinybeans+ price | — | [unknown — see Q5 row for URLs tried] |
| Tinybeans FY25 revenue / sub revenue | US$4.82M / US$3.32M | [sourced: ASX Appendix 4E, 2025-08-21] |
| Tinybeans FY26 revenue / sub rev / adj. EBITDA | US$6.49M / US$4.82M / US$427k | [sourced: medianet.com.au, 2026-08-27] |
| Tinybeans paid subs / retention / cash / cost cut | ~95k / 96% / US$1.64M / ~33% | [sourced: same] |
| FamilyAlbum Premium | One $2.99/mo; Family $5.99/mo or $59/yr; Family Pro $10.99/mo or $109/yr | [sourced: family-album.com/en/premium, 2026-11-03] |
| FamilyAlbum registered users | 30M (2026-05-07) | [sourced: Mixi PDF, 2026-05-07] |
| FamilyAlbum JP parent penetration | ~65% (Dec 2024) | [sourced: same] |
| FamilyAlbum non-JP / NA share | >40% / 20% | [sourced: same] |
| FamilySearch photo size / per-person caps | — | [unknown — no reachable primary states them] |
| Vivid-Pix Memory Station Home + pRT bundle | $228.99 (Windows) | [sourced: vivid-pix.com/product/memory-station-home, 2026-11-03] |
| Ente implied ARR per registered user | ≈$6.7/yr | [estimated: $1M ÷ 150,000; ARR input unverified] |
| Ente illustrative paying share | ≈11% | [estimated: $6.7 ÷ $60 assumed ARPU — illustrative only] |

---

## 5. Unknowns we could not resolve

- Whether Siri AI (iOS 27.0) can execute a *photo edit* (e.g., "remove the trash can") by voice. Apple's text says only "editing and sharing a set of photos"; press is split. Needs hands-on test or Apple feature-page confirmation.
- Whether Apple exposes any third-party-model access to the Photos library (App Intents / Foundation Models tool-calling over the user's photos). Apple developer documentation pages did not render on fetch; newsroom text describes Siri acting in third-party apps, not the reverse.
- Whether an Apple support article exists on merging two Apple Accounts' photo libraries (three support URLs checked; none describes it).
- Exact Ask Photos resumption date in June 2025 (PetaPixel 403).
- Ente paying-subscriber count and verified ARR; Immich user count and FUTO funding amount.
- Immich cross-user face identity merge (does Immich unify "Grandma" across two users' libraries?). Not documented.
- Mylio current list prices (hidden behind "Get Special Offer"; App Store and Wikipedia pages 404); Mylio user count; Mylio's founding/earlier incarnation.
- CompanyCam Series C amount and 2025–2026 ARR; HOVER's round dates and any debt; HappyCo cumulative funding.
- Picturelife's AWS cost and user count; Ever app shutdown month; Lifecake launch year and BackThen price; Keepy's status (503); Google+ Photos start year; Photobucket's 2023 purge; Mosaic's discontinuation; Seagate Lyve Minds/Lyve Home entirely.
- Tinybeans+ price; FamilyAlbum Premium subscriber count and launch year.
- Whether MyHeritage's face tagging excludes living people (only an unreachable affiliate blog claimed it); FamilySearch Memories size/count limits; Vivid-Pix standalone V5 price; Alexa Photo Frame price.
- PhoneArena 2026 "Gemini broke search" complaints and the Yahoo WWDC recap — both 403; unverified.

---

## 6. Full source list (accessed 2026-11-03)

Apple (primary)
1. https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/ (2026-06-08)
2. https://www.apple.com/newsroom/2026/09/siri-ai-a-profoundly-more-capable-and-personal-assistant-is-here/ (2026-09-14) — re-fetched for third-party/App Intents language
3. https://www.apple.com/newsroom/2026/06/apple-intelligence-brings-powerful-ai-capabilities-into-everyday-experiences/ (2026-06-08)
4. https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/ (2025-06-09)
5. https://www.apple.com/newsroom/2024/10/apple-intelligence-is-available-today-on-iphone-ipad-and-mac/ (2024-10-28)
6. https://developer.apple.com/videos/play/wwdc2026/121/ (2026-06-08) — description vs transcript distinguished
7. https://support.apple.com/HT213248 and https://support.apple.com/guide/photos/pht4dd77b3aa (iCloud Shared Photo Library) — re-fetched
8. https://support.apple.com/guide/photos/use-multiple-libraries-pht6d60b524/mac (System Photo Library / iCloud merge)
9. https://discussions.apple.com/thread/256192786 ; https://discussions.apple.com/docs/DOC-10211 (community, secondary; 2019-03-03) — re-fetched and re-quoted
10. https://www.fatcatsoftware.com/powerphotos/ (PowerPhotos vendor page)
Apple (secondary)
11. https://www.macrumors.com/roundup/ios-27/ — re-fetched
12. https://www.macrumors.com/guide/wwdc-2026-what-to-expect/ (2026-06)
13. https://www.macrumors.com/2025/09/15/apple-releases-ios-26/ (2025-09-15)
14. https://9to5mac.com/2025/08/13/heres-everything-new-for-apple-photos-in-ios-26/ (page dated 2025-10-23; slug 2025-08-13) — re-fetched
15. https://www.redsharknews.com/apple-wwdc-2026-siri-ai-ios-27-photo-editing (2026-06-09)
Google (primary)
16. https://support.google.com/photos/answer/17597604 (Gemini + Photos, desktop)
17. https://support.google.com/gemini/answer/15734842 (Gemini + gallery apps, Android)
18. https://support.google.com/photos/answer/15318661 (Ask Photos) — re-fetched for capabilities/limits
19. https://support.google.com/photos/answer/7378858 (partner sharing) — re-fetched; face-label sentences are NOT here
20. https://support.google.com/photos/answer/6128838 (face groups: "Face labels are private to each account and aren't shared across accounts")
21. https://gemini.google/release-notes/ (entries 2025.03.13, 2026.01.20)
22. https://developers.google.com/photos/support/updates (Library API scope removal 2025-03-31)
23. https://blog.google/products-and-platforms/products/photos/nano-banana-ai-templates-ask-photos/ (2025-11-11)
24. https://blog.google/innovation-and-ai/products/gemini-app/personal-intelligence-nano-banana/ (2026-04-16)
25. https://blog.google/products-and-platforms/products/photos/google-ask-photos-early-access/ (2024-09-05)
26. https://blog.google/products/photos/picture-this-fresh-approach-to-photos/ (2015-05-28)
Google (secondary)
27. https://techcrunch.com/2026/09/04/googles-gemini-spark-can-now-manage-your-google-photos-library/ (2026-09-04)
28. https://www.androidpolice.com/google-photos-hits-pause-gemini-powered-ask-photos-search/ (2025-06-04) — re-fetched
29. https://petapixel.com/2025/06/27/google-resumes-rollout-of-ai-based-ask-photos-image-search/ (403 — unverified)
30. https://www.phonearena.com/news/Gemini-broke-Google-Photos-search-and-users-arent-happy_id180791 (403 — unverified)
Independents (primary)
31. https://ente.com/pricing ; https://github.com/ente-io/ente
32. https://github.com/immich-app/immich ; https://immich.app/blog/2024/immich-core-team-goes-fulltime (2024-05-01) ; https://immich.app/blog/v2.0.0-release (2025-10-01) ; https://immich.app/blog/v3.0.0-release (2026-07-01)
33. https://github.com/homeserverhq/immich-mcp ; https://github.com/okopok/immich-mcp ; https://github.com/JoeRu/mcp4immich ; https://github.com/barryw/ImmichMCP
34. https://www.photoprism.app/editions/ ; https://www.photoprism.app/features/
35. https://mylio.com/pricing/ ; https://mylio.com/plans/ ; https://mylio.com/concierge/ (fetched OK) ; https://mylio.com/about/
36. https://www.einpresswire.com/article/689981890/mylio-and-the-photo-managers-join-forces-at-rootstech-2024 (2024-02)
37. https://www.aboutamazon.com/news/amazon-prime/how-to-use-amazon-photos-storage (undated) ; https://www.aboutamazon.com/news/company-news/2020-letter-to-shareholders (Apr 2021)
38. https://www.synology.com/en-us/dsm/feature/photos ; https://github.com/pulsejet/memories ; https://github.com/photoview/photoview ; https://github.com/LycheeOrg/Lychee ; https://github.com/LibrePhotos/librephotos
39. https://github.com/pixelfed/pixelfed ; https://pixelfed.org/
40. https://www.permanent.org/ ; https://www.forever.com/pricing
41. https://www.remento.co/ ; https://www.mixbook.com/photo-books ; https://www.heyartifact.com/
42. https://keepy.me/ and https://www.keepy.me/ (503 both)
Independents (secondary)
43. https://techcrunch.com/2025/04/01/ente-wants-to-take-on-google-photos-with-its-privacy-first-photo-storage-service/ (2025-04-01)
44. https://petapixel.com/2026/10/28/amazons-photo-frame-has-alexa-ai-to-show-only-your-best-pics/ (403 — unverified)
45. https://memoirji.com/blog/storyworth-pricing-2026-buyer-guide/ (affiliate; updated 2026-05-15)
Vertical
46. https://companycam.com/pricing (primary)
47. https://siliconprairienews.com/2025/11/companycam-reaches-unicorn-status-with-2-billion-valuation-a-first-for-a-nebraska-startup/ (2025-11-22)
48. https://getlatka.com/companies/companycam ; https://jobs.insightpartners.com/companies/companycam (aggregators) ; https://pitchbook.com/profiles/company/223056-55 (403)
49. https://www.cbinsights.com/company/hover-inc (aggregator) ; https://hover.to/pricing (primary)
50. https://www.spectora.com/pricing/ (primary) ; https://getlatka.com/companies/spectora.com (estimate)
51. https://www.connectcre.com/stories/happyco-expands-platform-with-52m-in-funding/ (2022-01-20) ; https://www.happy.co/pricing (primary)
Graveyard
52. https://venturebeat.com/business/goodbye-everpix-photo-storage-startup-shuts-down-as-bills-pile-up (2013-11-05)
53. https://github.com/everpix/Everpix-Intelligence (company post-mortem data)
54. https://techcrunch.com/2012/11/02/charles-forman-4m-picturelife/ (2012-11-02)
55. https://tech.co/news/streamnation-acquires-picturelife-cloud-photo-service-2015-01 (2015-01)
56. https://www.dpreview.com/news/5910446180/picturelife-shutters-service-user-content-migrates-to-smugmug (2016-08-23)
57. https://blog.dropbox.com/topics/company/saying-goodbye-to-carousel-and-mailbox (2015-12-07) — re-fetched
58. https://techcrunch.com/2015/12/07/failing-to-find-users-dropbox-will-shut-down-mailbox-in-february-2016-and-carousel-in-march/ (2015-12-07)
59. https://en.wikipedia.org/wiki/Dropbox ; https://en.wikipedia.org/wiki/Picasa ; https://en.wikipedia.org/wiki/Photobucket ; https://en.wikipedia.org/wiki/Flickr ; https://en.wikipedia.org/wiki/Shutterfly ; https://en.wikipedia.org/wiki/Tinybeans ; https://en.wikipedia.org/wiki/Mixbook (secondary; used for dates)
60. https://www.ftc.gov/news-events/news/press-releases/2021/01/california-company-settles-ftc-allegations-it-deceived-consumers-about-use-facial-recognition-photo (2021-01-11)
61. https://www.ftc.gov/system/files/documents/cases/1923172_-_everalbum_complaint_final.pdf ; https://www.ftc.gov/system/files/documents/cases/1923172_-_everalbum_decision_final.pdf (issued 2021-05-06) ; https://www.ftc.gov/legal-library/browse/cases-proceedings/192-3172-everalbum-inc-matter
62. https://news.ycombinator.com/item?id=23033676 (Lifecake, 2020-04)
63. https://techcrunch.com/2018/11/01/flickr-revamps-under-smugmug-with-new-limits-on-free-accounts-unlimited-storage-for-pros/ (2018-11-01) — re-fetched
64. https://pixieset.com/pricing/
65. https://announcements.asx.com.au/asxpdf/20250821/pdf/06n4h84f2x4yl9.pdf (Tinybeans FY25, 2025-08-21)
66. https://newshub.medianet.com.au/2026/08/tinybeans-asxtny-posts-maiden-adjusted-ebitda-profit-in-fy26/168355/ (2026-08-27)
67. https://pdf.irpocket.com/C2121/Kdx3/R43P/MfKg.pdf (Mixi FamilyAlbum 30M, 2026-05-07) ; https://family-album.com/en ; https://family-album.com/en/premium
Family-merge / genealogy
68. https://education.myheritage.com/article/myheritage-photo-features/ — re-fetched
69. https://help.ancestry.com/hc/en-us/articles/53933332427283 (Face Match) ; https://help.ancestry.com/hc/en-us/articles/53933301940627 (Photo Insights)
70. https://www.familysearch.org/en/blog/free-cloud-storage-familysearch-memories (2021-02-11)
71. https://www.vivid-pix.com/ ; https://www.vivid-pix.com/software ; https://www.vivid-pix.com/product/memory-station-home
Dropped (unreachable or misattributed; listed for the record): perkinscoie.com Everalbum article (308→404); dnyuz.com/?p=210096 (404); vivid-pix.com RootsTech 2026 blog (404); checkout.memorygram.com (truncated URL); churchofjesuschrist.org FamilySearch news (503); familysearch.org developer docs (403); genealogyexplained.com (bot challenge); shop.zimaspace.com NAS blog (does not contain the claims attributed to it); tidbits.com Picasa (bot check); petapixel.com Photobucket 2017 (403); alternativeto.net Photobucket 2023 (403); capterra.com Spectora (403); pitchbook.com (403 ×3); theverge.com Everpix (fetch not permitted); help-redir.ancestry.com (replaced by help.ancestry.com); linkedin.com Ente founder profile (not the post).

---

## Audit log

Each auditor finding, and what was done (repair pass 2026-11-03; WebSearch unavailable, WebFetch only).

**Untagged numbers**
1. Prime "hundreds of millions" — replaced with "more than 200 million Prime members worldwide" [sourced: Amazon 2020 shareholder letter, Apr 2021]; the $0 price-floor line is now an [estimated] with its input named.
2. Remento truncated URL — replaced with primary https://www.remento.co/ ($99 incl. book; $99/yr or $12/mo renewal; $69 extra copies). Note: /pricing returned 404; the homepage carries the prices.
3. Mixbook "[secondary]" — replaced with primary mixbook.com/photo-books ("Starting at $14.99"; "45-55% off almost everything" banner on access date).
4. 'Years' column — every row now carries a tag; years derived from Everpix README, TechCrunch/DPReview, Wikipedia (Dropbox, Picasa, Photobucket, Flickr, Shutterfly, Tinybeans, Mixbook), blog.google, HN; unsourced years marked [unknown].
5. Picturelife ~$1M/yr AWS — no primary reachable; removed as a figure, marked [unknown] in the row, A5 note and unknowns.
6. Ever app shutdown Aug 2020 — FTC press release and complaint do not state it; marked [unknown]; FTC complaint dates (Feb 2017 Friends launch, Apr 2019 opt-in) added from the PDF.
7. Google+ Photos — now sourced to blog.google 2015-05-28 (Google Photos launch as "a new, standalone product"); Google+ Photos start year marked [unknown].
8. Photobucket "Free → $399/yr (2017)" — now [sourced: Wikipedia Photobucket, 2017-06-28 entry: US$399.99/yr plan; US$99/yr linking tier] (secondary; PetaPixel 403).
9. Flickr "1 TB free (2013)" and 2019 enforcement — now [sourced: Wikipedia Flickr: 2013-05-20; deletion set 2019-02-05 then 2019-03-12; never implemented per Mar 2022 statement].
10. Tinybeans "~33% costs" — tagged [sourced: medianet 2026-08-27] in both the Why and Lesson cells.
11. Ente "$60 ARPU" — relabelled as an illustrative assumption, anchored to Ente's $59.88 200 GB annual price; the 11% is marked illustrative only.
12. Storyworth date — tag now reads "updated 2026-05-15".

**Suspect claims**
- Google face labels (major) — sentences located verbatim at support.google.com/photos/answer/6128838 and re-cited there in Q2, Q6, A4; answer/7378858 is now cited only for what it contains.
- Apple 7-day rule / iOS 16+ (minor) — rewritten: rule applies when the creator deletes the library; requirement is iOS 16.1 / iPadOS 16.1 / macOS Ventura; "You can join one Shared Library" quoted.
- PowerPhotos "cannot merge optimised" (major) — withdrawn; both community pages re-quoted accurately ($40; "only way of merging two Libraries without losing album and folder organization"); PowerPhotos vendor page added; Apple's own multiple-libraries guide added as the single-account primary.
- Carousel quote (major) — withdrawn; replaced with the verbatim Houston/Ferdowsi "increased our team's focus on collaboration" wording from the Dropbox post and TechCrunch; shutdown date retained.
- Flickr $49.99 / 97% (major) — corrected to "$5.99 per month" / "$50 per year" and "vast majority"; Wikipedia's US$60/yr noted as conflicting.
- HOVER ~$142M + debt (minor) — corrected to $136.71M, Series D $60M "6 yrs ago", no debt listed; pricing added from hover.to.
- Amazon "May 2026 redesign" (minor) — date removed (page undated); "redesigned mobile app experience" and "later in 2026" quoted as the page has them.
- 9to5Mac quote (minor) — converted to an explicit paraphrase; dates corrected (slug 2025-08-13, page 2025-10-23).
- Picasa "shut Mar 2016" (minor) — split into desktop end 2016-03-15 and Web Albums close 2016-05-01 (Wikipedia; TidBITS bot-blocked).
- Lifecake "2x" (minor) — replaced with the commenter's "considerably more expensive"; Trustpilot reference dropped; BackThen named.
- ZimaSpace misattributions (minor) — citation dropped; each of Synology/Memories/Photoview/Lychee/LibrePhotos now cited to its own primary (vendor page or GitHub README).
- Ask Photos "isn't where it needs to be" (minor) — quote trimmed to the body text ("has been paused at very small numbers"; "in terms of latency, quality and ux"); date fixed to 2025-06-04.
- HappyCo "Series B" (minor) — label removed; "$52 million in funding" led by Camber Creek, 2022-01-20.
- Mylio Concierge "$299 (was $450)" (minor) — rewritten to what the page shows ($299 services plan; $379 with Photos+; $450 unlabelled; $99 renewal); "404" note corrected.
- MyHeritage "deceased only" (minor) — withdrawn; knowledge-base page re-quoted (no tagging statement); marked [unknown]. Ancestry's primary now carries the deceased-only restriction, and the Q6 verdict is rewritten to rest on Ancestry (verified) rather than MyHeritage.
- FamilySearch 15 MB / 5,000 (minor) — both removed; marked [unknown] with URLs tried.
- Ente 11% (minor) — labelled illustrative.
- WWDC26 session 121 (minor) — description vs transcript distinguished; attribution to Apple Intelligence, not Siri.
- PhotoPrism free-tier faces (minor) — flagged as inference, not stated.
- Photobucket 2017/2023 (minor) — 2017 re-sourced to Wikipedia; 2023 marked [unknown].

**Broken or misquoted sources** — all addressed as above; the "Dropped" line in §6 lists every URL removed and why. perkinscoie → replaced by FTC press release, complaint PDF and decision PDF; dnyuz → help.ancestry.com; vivid-pix blog → vivid-pix.com/product/memory-station-home; memorygram → remento.co; churchofjesuschrist/familysearch dev docs → [unknown]; petapixel ×3, phonearena, capterra, pitchbook, alternativeto → replaced by primaries where one existed (spectora.com, hover.to, Wikipedia) or marked unverified; mylio.com/concierge "404" note corrected; Verge Everpix → Everpix's own README (7,000 subscribers); Wikipedia Dropbox fetched for Loom; Ente LinkedIn marked unverified.

**Missing vs brief**
- Q1 cross-account merging — Apple's multiple-libraries guide added; URLs tried listed; still no Apple account-to-account merge article [unknown].
- Q2 connector date — 2025-03-13 from Gemini release notes.
- Q2 Ask Photos capabilities/limits — added from Google help (examples, backed-up-only, Labs/experimental, availability, off switch).
- Q3 Ente license — AGPL-3.0 from GitHub. Immich FUTO — 2024-05-01 blog; amount not disclosed.
- Q3 Mylio pricing — plans page, App Store and Wikipedia tried; still hidden [unknown].
- Q3 Pixelfed — added (federated social, AGPL, 7.1k stars; not an archive).
- Q3 Artifact — added (heyartifact.com: $149/interview; shutting down).
- Q3 self-hosted tools — all five now on primary docs.
- Q4 HOVER and Spectora pricing — added from primaries; HappyCo pricing is quote-only (primary).
- Q5 Lyve/ThisLife/Mosaic/Lifetouch — ThisLife (2010; Jan 2013 $25M; absorbed 2016), Lifetouch (2018, $825M) and Mosaic (~2012) sourced to Wikipedia; Lyve still [unknown] with the pages tried.
- Q5 "Memories" apps and Mylio's earlier incarnation — addressed as rows/notes; Mylio history [unknown].
- Q5 Pixieset consumer — added (photographer-only; no consumer product).
- Q5 Tinybeans pricing — five URLs tried; still [unknown]. FamilyAlbum Premium — added from primary ($2.99 / $5.99 or $59 / $10.99 or $109).
- Q5 Google+ Photos / Loom — primaries/Wikipedia added.
- Q6 Vivid-Pix / FamilySearch / Ancestry — Ancestry now primary; Vivid-Pix bundle price primary; FamilySearch limits [unknown].
- A4 Apple open AI access — Apple newsroom and MacRumors re-read for App Actions/App Intents language; Google Library API change now verified directly (developers.google.com, effective 2025-03-31); Apple developer docs did not render, so third-party-model access remains [unknown].
