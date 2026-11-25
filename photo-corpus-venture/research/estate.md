# Research track: the bereavement / estate event (Gap track R3)

Written 2026-11-03; repaired 2026-11-03 after audit (see "Audit log" at the end). All URLs accessed 2026-11-03 unless noted. Builds on customers.md Q1(b) and Q1(f); does not repeat the Apple/Google policy text already quoted there except where this pass found more precise primary wording.

Variant under test: "recover and consolidate a deceased relative's photos", sold to heirs at the moment of death, when the platform itself hands over a bulk export.

## 1. Questions asked

1. Volume: US deaths/yr by age band; smartphone ownership by age; derived decedents/yr with a smartphone photo library. UK/EU equivalents.
2. Apple Digital Legacy, exactly: what the Legacy Contact receives, format, time limit, no-Legacy-Contact fallback (court order cost/time), self-export by an heir holding the unlocked phone.
3. Google: deceased-user data request outcomes; Inactive Account Manager delivery format.
4. Samsung/Android: locked phone of a decedent; Google account recovery rules.
5. Paid services heirs already use: DriveSavers and other recovery labs; Cellebrite; estate attorneys and "digital executor" services; digital-estate startups (Everplans, GoodTrust, Clocr, Trust & Will, LifeSite, Cake, Empathy, Keeper, Ever Loved); any evidence of heirs paying specifically for photos.
6. Channels to the heir: funeral homes and their software vendors, aftercare programs, Batesville, SCI, estate attorneys (ACTEC), hospice, employers/insurers, obituary platforms.
7. Pre-need: Apple-specific Legacy Contact adoption; whether "set up your legacy contact" content gets traffic.
8. Sensitivity/timing: when families deal with photos; funeral-home tribute-video forcing function, prices, and how photos are collected.

Falsification stance: the variant assumes (a) a large annual cohort of decedents with phone libraries, (b) heirs can get the export, (c) heirs want and will pay for consolidation. Evidence was sought against each.

## 2. Findings per question

### Q1. Volume

**US deaths, final 2024** [sourced: https://www.cdc.gov/nchs/products/databriefs/db548.htm, NCHS Data Brief 548, Jan 2026]: 3,072,666 resident deaths. By age band: <1: 20,050; 1–4: 3,843; 5–14: 5,940; 15–24: 29,953; 25–34: 57,827; 35–44: 97,430; 45–54: 157,770; 55–64: 358,196; 65–74: 628,416; 75–84: 822,944; 85+: 890,240. So 2,341,600 deaths (76.2%) are at 65+ and 890,240 (29.0%) at 85+ [estimated: sums of the NCHS bands above].

**US smartphone ownership by age** [sourced: https://www.pewresearch.org/internet/fact-sheet/mobile/, "Americans' Use of Mobile Devices in 2026", published 2026-10-19, survey of 5,511 adults Jan 30–Jun 18 2026]: 18–29: 97%; 30–49: 97%; 50–64: 91%; 65+: 79%. Pew publishes no 75+ or 85+ split on this page; the prior-year value for 65+ was 78% [sourced: https://www.pewresearch.org/short-reads/2026/01/08/internet-use-smartphone-ownership-digital-divides-in-u-s/, 2026-01-08].

**Falsification note:** the 65+ band is dominated by 65–74-year-olds, while deaths are dominated by 85+ (29% of all deaths). Decedents are also sicker and more institutionalised than the age-band population. Applying 79% to the 85+ band is therefore an upper bound. No sourced 85+ ownership figure was found [unknown].

**Decedents/yr who owned a smartphone (ages 15+):**
- Scenario A, Pew band rates applied directly: 15–24 29,054; 25–34 56,092; 35–44 94,507; 45–54 143,571 (uses the 50–64 rate, 91%, for the whole NCHS 45–54 band); 55–64 325,958; 65–74 496,449; 75–84 650,126; 85+ 703,290. Total 2,499,047 ≈ **2.50M** [estimated: NCHS 2024 band counts × Pew 2026 band rates; 45–54 uses 91%]. Band-mismatch caveat: Pew's 30–49 band (97%) covers the 45–49 half of the NCHS 45–54 band; if the whole 45–54 band is instead given 97%, the band becomes 153,037 and the total 2,508,513 ≈ **2.51M** [estimated: 157,770 × 0.97]. So the true upper bound is 2.50–2.51M; the difference is immaterial to the funnel.
- Scenario B, sensitivity with 75–84 at 70% and 85+ at 50%: 2,166,812 ≈ **2.17M** [estimated: same inputs with 822,944 × 0.70 = 576,061 and 890,240 × 0.50 = 445,120 replacing the 79% rows; the 70%/50% assumptions are NOT sourced and exist only to show the range; replace when an 85+ figure is found].
- Owning a phone is not the same as having a meaningful photo library on it; the share of owners (especially 85+) with a library worth consolidating is [unknown].

**UK / EU:** England & Wales 2024: 568,613 deaths registered [sourced: https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/bulletins/deathsregistrationsummarytables/2024, released 2025-10-09]. EU 2024: 4.81 million deaths, crude rate 10.7 per 1,000 [sourced: https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Mortality_and_life_expectancy_statistics, data extracted March 2026]. UK 65+ smartphone ownership (Ofcom): [unknown] — in the repair pass three direct Ofcom URLs were tried and all returned HTTP 403 (the Adults' Media Use and Attitudes landing page, the 2024 report page, and the 2025 report PDF path under /siteassets/...); earlier search returned only pre-2020 Ofcom reports and secondary 2026 roundups.

### Q2. Apple Digital Legacy, exactly

Primary (Apple support, four articles):
- **What the Legacy Contact can access** [sourced: https://support.apple.com/en-us/103128, "Data that a Legacy Contact can access", published 2026-04-02]: "iCloud Photos", "Notes", "Mail", "Contacts", "Calendars", "Reminders", "Messages in iCloud", "Call history", "Files stored in iCloud Drive", "Health Data", "Voice Memos", "Safari Bookmarks and Reading List", and "Anything included in an iCloud Backup" (which may include photos and videos stored on the device). Cannot access: "Purchased content, such as movies, music, and books", "Subscriptions and in-app purchases", "Payment information", and iCloud Keychain contents.
- **How access works and the time limit** [sourced: https://support.apple.com/en-us/102678, "Request access to an Apple Account as a Legacy Contact", published 2026-08-10]: access is through a new "legacy contact Apple Account"; after setting a password and two-factor authentication the contact can "sign in to your legacy contact Apple Account on the web at iCloud.com or download the account data at privacy.apple.com". Access lasts "three years from when Apple approves the first Legacy Contact account request", after which the legacy account is permanently deleted. "The account holder's original Apple Account no longer works" and Activation Lock is removed from devices, which must be erased before reuse. If the decedent used Advanced Data Protection, the contact must first sign in on an iPhone/iPad with the legacy account and approve web access there.
- **Mechanism** [sourced: https://support.apple.com/guide/security/legacy-contact-security-secebf027fb8/web, Apple Platform Security, undated]: the access key "doesn't encompass the information necessary to decrypt the decedent's iCloud Keychain"; Apple issues "a user name and password for the new account"; contacts "sign in to the Apple claim website to initiate access".
- **Format / quality of the privacy.apple.com export** [sourced: https://support.apple.com/en-us/102208, "Get a copy of the data associated with your Apple Account", published 2026-09-11; https://support.apple.com/en-us/HT208502 resolves to the same article]: iCloud-stored photos and videos are among the data that can be requested; "Photos, videos, and documents are provided in their original formats" (so originals, i.e. HEIC/H.265 as captured, not transcoded JPEGs); contacts/calendars/bookmarks/mail come as .vcf/.ics/.html/.eml; app-usage data as spreadsheets or .json/.csv/.pdf; the archive stays on the Data & Privacy page for 14 days ("you have 14 days to download your data"), after which it must be requested again; processing time and archive-size options are not stated on the page. The article says its file guides "don't cover content you created or that others shared with you, such as photos and videos stored in iCloud" — so whether albums, People/face names, Memories, or edit history are included in the photo export is still [unknown] from Apple's public documentation.
- **Format / quality of the iCloud.com path** [sourced: https://support.apple.com/en-us/111762, published 2026-04-10]: "You can select up to 1,000 at a time" with options "Unmodified Originals (format as captured or imported)", "Highest Resolution (… typically HEIC or H.265)" and "Most Compatible (JPEG or MP4/H.264)". The page makes no statements about albums or metadata [unknown].
- **No Legacy Contact (US):** a court order that "must name you as the rightful inheritor" and state the decedent's Apple Account, that the requestor is the "legal personal representative, agent, or heir", and that Apple is ordered to assist; "Only one person can request access"; end-to-end encrypted data cannot be decrypted by Apple and may require the device passcode [sourced: https://support.apple.com/digital-legacy, undated]. Time limit on access obtained by court order: not stated [unknown].
- **Court-order cost and time:**
  - Forum, first-hand, 2025 [sourced: https://talk.tidbits.com/t/how-to-access-data-from-deceased-apple-customers-without-a-lawyer/30659 (page 1) and ?page=2, posts dated 2025-04-01 to 2025-06-16; re-verified 2026-11-03 by text search of both pages]: original poster, 2025-04-01: "I was referred me to a lawyer who wants $750 (plus the filing fee) to do this for me"; 2025-04-04: "It's at LEAST $750 that I don't have sitting around". A second poster, 2025-04-05, acting for a parent's estate: "This was in Vermont, which is generally friendly to pro se petitioners"; "It cost the estate (not me) about 30 minutes of his time to learn exactly how to word the initial petitions"; "In all, he billed the estate (again, not me) a total of $1,200 for his advice". Outcome for the original poster on 2025-06-14: "I have the data. Mostly." — roughly 10,000 photos and videos recovered via iCloud.com after the court order, voice memos only visible after signing a device into the account, nothing recoverable from the reset devices: "Court Order or not, Apple will not (apparently cannot) give you access to anything on any of their devices." iCloud storage had dropped to 5 GB after payments stopped but "Apple hasn't deleted any data".
  - Vendor claim, secondary [sourced: https://www.afterlife.ai/what-happens-to-icloud-when-you-die/, "Last reviewed 4 June 2026"]: the court-order route "costs between three and ten thousand dollars in attorney fees depending on jurisdiction" and "typically takes six to twelve months". Unverified; publisher sells a digital-legacy product.
  - Law-firm pages describe the route as opening probate to be appointed personal representative, then a petition/order naming Apple and the Apple ID, with no dollar figures [sourced: https://floridaprobateandfamilylaw.com/blog/how-to-access-an-apple-account-after-someone-passed-away/, 2021-12-08].
  - **Probate-court filing fees (the "plus the filing fee" component), primary statutes:** New York Surrogate's Court, SCPA 2402(7), fee for a petition for probate or administration by estate value: "Less than $10,000 ... $45.00"; "10,000 but under 20,000 ... 75.00"; "20,000 but under 50,000 ... 215.00"; "50,000 but under 100,000 ... 280.00"; "100,000 but under 250,000 ... 420.00"; "250,000 but under 500,000 ... 625.00"; "500,000 and over ... 1,250.00" [sourced: https://www.nysenate.gov/legislation/laws/SCP/2402, current consolidated text]. Florida clerk charges, Fla. Stat. 28.2401(1) (2025): formal administration $395; summary administration $340 (estates ≥ $1,000) or $230 (< $1,000); disposition of personal property without administration $230 [sourced: https://www.flsenate.gov/Laws/Statutes/2025/28.2401]. California statewide fee schedule: not retrievable (courts.ca.gov/documents/filingfees.pdf redirects to www4.courts.ca.gov, which returned HTTP 403) [unknown]. An heir whose only goal is the Apple order must still open an estate, so these are the floor cost even pro se.
  - **Attorney-fee surveys:** [unknown] — lawyers.com "how much does probate cost" returned HTTP 403 in this pass; nolo/legalzoom/findlaw returned 404 in the earlier pass (customers.md); no bar-association fee survey was reachable. Attorney cost for this route therefore rests on the two forum figures ($750 floor quoted; $1,200 billed) and the vendor claim ($3k–10k).
- **Can an heir with the unlocked iPhone + passcode self-export?** Technically yes: Mac Photos "Export Unmodified Originals" or iCloud.com in 1,000-item batches (above). Apple's **Transfer to Google Photos** tool requires signing in at privacy.apple.com with the account and two-factor authentication, Advanced Data Protection off, and a Google account with enough storage; it transfers "only the most recent edit", "duplicates appear as a single photo", "Photos transfer with their albums when possible. Videos transfer separately, without albums"; NOT transferred: "Shared albums, Smart Albums, Live Photos, some metadata"; takes "three to seven days", up to 30 days [sourced: https://support.apple.com/HT208514, published 2026-10-09]. Whether Apple's terms permit an heir to operate the decedent's account this way is a legal question this pass did not resolve [unknown]; the legacy pages say the original account "no longer works" once a legacy request is approved, so self-export must happen *before* filing.
- **Devices:** "Apple can't remove the passcode lock without erasing the device" [sourced (secondary, quoting Apple): https://funeral.com/blogs/the-journal/icloud-inheritance-and-apple-legacy-contact-how-access-works-and-what-families-need, 2026-01-20]; AARP column: "Passcodes are encrypted and Apple can't help with the biometric locks either" [sourced: https://www.aarp.org/personal-technology/tech-guru-unlock-dead-spouses-phone/, 2024-10-22].

### Q3. Google

- Deceased-user request form offers three options: close the account, request funds, "Obtain data from a deceased user's account"; "We cannot provide passwords or other login details"; "Any decision to satisfy a request about a deceased user will be made only after a careful review"; a closed account's contents cannot be released later [sourced: https://support.google.com/accounts/contact/deceased and https://support.google.com/accounts/answer/2842525?hl=en, undated]. Google publishes no document list, timeline, or delivery format on these pages [unknown]. A repair lab's checklist (paraphrased, not Google's wording) says the request involves uploading a death certificate, a government-issued ID for the requester, and proof that the requester is authorised to act on behalf of the estate [sourced (secondary): https://mdrepairs.com/blog/deceased-family-member-data-recovery/, published 2026-07-15, updated 2026-09-09]. No first-hand account of an approved "obtain data" request with the delivered format was found; Q&A-site claims of "5–10 business days" to "2–3 months" are unverified [unknown].
- **Inactive Account Manager** [sourced: https://support.google.com/accounts/answer/3036546, undated]: the trusted contact gets an email "with a link they can follow to download the data"; contact must verify with a mobile number; up to 10 people; "some information can't be shared". The page's example lists Blogger, Drive, Mail, YouTube — Google Photos is not in the example and whether it is selectable was not confirmed on the page [unknown]. Link validity period and format: not stated [unknown].

### Q4. Samsung / Android

- No published Samsung deceased-account process was found; consumer guides say the same [sourced (secondary): https://www.foxnews.com/tech/how-unlock-android-device-windows-pc-when-owner-passes-away, undated]. Samsung Community (Malaysia) thread 2025-05-25: an executor "I have possession of her Samsung tablet and phone but I don't know the unlock patterns for them" asked for a Samsung request link; replies not rendered, no resolution visible [sourced: https://community.samsung.com/my/conversations/tablets/how-to-access-deceased-family-members-samsung-phone-and-tablet/r1_33375046, 2025-05-25]. The UK Samsung Community thread "Accessing deceased relatives S21" could not be rendered.
- Repair-lab view [sourced: mdrepairs.com, 2026-09-09]: the page's table lists recent hardware-encrypted Android as "Usually locked" (paraphrase of a table row; the page adds manufacturer-specific caveats in prose); older Android is described as often recoverable through forensic methods; for a modern iPhone without the passcode the page's verbatim line is "Without the passcode, the data is mathematically unreachable."
- Google: "Google can not help you and your family unlock your late mother's phone" [sourced (secondary column): https://tech.yahoo.com/general/articles/ask-jerry-google-help-access-180005532.html, undated]. Google's own recovery rules for a deceased person's account are the Q3 process; it does not unlock devices.

### Q5. Paid services heirs already use

| Service | Price | Evidence |
|---|---|---|
| DriveSavers Passcode Lockout Data Recovery (launched for consumers incl. "deceased family member" 2018) | "priced around $3,900" at launch (2018); 2026 Trustpilot reviews quote "$900 to $3900", "$3700-3900", "$3.5K and 5-7 business days" for general recovery jobs; list price not published (drivesavers.com 403; businesswire release 403; helpnetsecurity 405) | [sourced (secondary, quoting the 2018 release): https://forums.macrumors.com/threads/drivesavers-lets-consumers-retrieve-data-from-locked-ios-devices-for-3-900-updated.2157359/, 2018-11-27 — "The service is not inexpensive, priced around $3,900"; "DriveSavers says that most people use the service to access the data from the device of a deceased loved one"] [sourced: https://www.trustpilot.com/review/drivesavers.com, TrustScore 2.8/5 on 39 reviews; quotes from reviews dated 2026-02-24, 2026-06-15, 2026-08-11, 2026-10-17] |
| DriveSavers standard phone recovery | "$3000-$4000" (2023) vs "industry average of $300-$1200" | [sourced (competitor page): https://www.ipadrehab.com/article.cfm?ArticleNumber=55, ©2026] |
| MD Repairs (lab, Kansas) | forensic unlock older iPhone/Android $800–$2,000; damaged iPhone with passcode known $500–$1,200; "If we can't recover anything, you don't pay" | [sourced: https://mdrepairs.com/blog/deceased-family-member-data-recovery/, 2026-09-09] |
| Cellebrite (consumer offering?) | none found | [unknown] — cellebrite.com/en/faq (404), /en/about-us (403), investors.cellebrite.com (403) all unreachable in this pass; no consumer or "deceased relative" service page was located; the consumer-facing forensic route in practice is independent labs (MD Repairs, DriveSavers) rather than Cellebrite itself |
| Estate attorney, court order for Apple | $750 quoted (plus filing fee); $1,200 billed for ~30 minutes of petition-wording advice (Vermont estate); vendor claim $3k–10k and 6–12 months; court filing fee NY $45–$1,250 by estate value, FL $395 formal / $340 summary | [sourced: TidBITS Talk 2025-04-01/04-05 (both pages); afterlife.ai 2026-06-04, unverified; nysenate.gov SCPA 2402; flsenate.gov 28.2401 (2025)] |
| "Digital executor" services / estate attorneys' digital-asset fees | [unknown] | no search possible after budget exhaustion; none of the fetched vendor pricing pages (Everplans, GoodTrust, Clocr, Trust & Will) sells a post-death "digital executor" service; the only attorney-priced item seen is Clocr's "Attorney-assisted Revocable Trust $3000" (pre-need, not digital-asset specific) [sourced: https://clocr.com/pricing/] |
| Everplans Premium | $99.99/yr; free tier "Store up to 3 items"; founded 2012; "In October 2024, Everplans was acquired by Precoa"; user/revenue counts [unknown] (about and press pages state none; precoa.com/news is a 404) | [sourced: https://www.everplans.com/pricing; https://www.everplans.com/about; https://www.everplans.com/press] |
| GoodTrust | "One plan. Only $149." (Estate+ bundle: Will, Trust, directives, Digital Vault; 1 year of updates per pricing page); reviewers cite $39/yr after; home page says nothing about recovering a deceased person's photos | [sourced: https://mygoodtrust.com/ and https://mygoodtrust.com/pricing; $39/yr secondary: https://www.ncoa.org/product-resources/estate-planning/goodtrust-willmaker-review/] |
| GoodTrust funding/traction | $2.3M seed Jan 2021 [sourced: https://venturebeat.com/business/goodtrust-raises-2-3-million-for-digital-legacy-platform, 2021-01]; $5M seed Dec 2021 "total $7.5M" [sourced (secondary, page returned 403 at audit, not re-verified): https://www.finsmes.com/2021/12/goodtrust-raises-5m-in-seed-funding.html, 2021-12]; investors named on the about page: Moxxie Ventures, Khosla Ventures, Concrete Rose Capital, Bling Capital, Synetro Ventures, Azure Capital Partners, Alumni Ventures, Primer Holdings, Gaingels Network, Lane VC [sourced: https://mygoodtrust.com/about, ©2026]; total raised since 2021 and customer count: [unknown] (the earlier draft's Tracxn/PitchBook totals and "200,000 registered customers" had no fetched URL and are withdrawn) | see tags inline |
| Clocr Platinum | $30/mo; $141/yr; lifetime shown as two figures on the same page, "$1500" and "$475/Onetime *" (ambiguous; the asterisk is not explained in the rendered page); "+$19 Yearly Maintenance" appears under the Platinum feature list without stating which billing option it attaches to; Social Media Will $5; attorney-assisted revocable trust $3,000 | [sourced: https://clocr.com/pricing/] |
| Trust & Will | Will "starting at $199"; Trust "starting at $499"; attorney match "starting at $1,499"; Membership $49/year includes "a secure Digital Vault for important documents"; Attorney Support add-on +$299; no mention of digital assets/online accounts | [sourced: https://www.trustandwill.com/pricing] |
| Empathy | B2B2C only: homepage targets life insurers, financial-services firms and employers, sole call to action "Book a demo"; empathy.com/pricing is a 404; consumer price [unknown] (the earlier draft's "$65 after free month" had no source and is withdrawn); homepage stats strip reads "500M+ Individuals covered", "2120 hrs Saved per user", "4.80.0/5 User satisfaction rating" as displayed — the "500M+" is inconsistent with the company's own 2025 blog ("over 45 million lives") and Calcalist ("over 50 million covered lives"); treat all three as unreconciled company claims; no photo/memorial feature mentioned | [sourced: https://www.empathy.com/, ©2026; conflict sources in Q6] |
| Keeper (mykeeper.com) | Keeper Basic "$0 USD - Limited Features": "1 Memorial Page", "Up to 5 Photos and Videos" (the same page's FAQ says the free account lets you "build up to two Memorial pages" — internal inconsistency); Keeper Plus "$99.00 USD - One Time Payment", "Unlimited Memorial Pages", "Unlimited Photos and Videos"; Keeper Concierge "$350.00 USD - One Time Payment"; "KeeperQR Plaques" sold as sympathy gifts | [sourced: https://www.mykeeper.com/pricing]; QR-on-headstone description secondary [sourced: https://www.everplans.com/articles/the-top-10-online-memorial-websites] |
| Ever Loved | everloved.com root and /pricing returned 403 | [unknown] |
| LifeSite | lifesite.co returned HTTP 525 | [unknown] |
| Cake (joincake.com) | now redirects to altogetherfuneral.com, a funeral-home network "of more than 1,700 compassionate professionals" in 21 states; no Cake product visible | [sourced: https://www.altogetherfuneral.com/, ©2026] |
| Tribute video, DIY vendor | Eulogize $69 first tribute, $20 each after; "our services may already be included in what they've arranged" | [sourced: https://www.eulogizememorials.com/pricing] |
| Tribute video, price survey (secondary) | funeral-home slideshow often included in the package at no extra charge; "As a paid add-on, it usually runs somewhere around $75 to $300, with a bit more for extra copies on USB or DVD"; freelance/videographer simple montage "somewhere around $150 to $600"; with interviews/restoration "$800 to $2,000 range and occasionally beyond"; editors "$50 to $150 an hour"; rush surcharge "25% to 50%"; DIY "anywhere from nothing to about $50" | [sourced (secondary, vendor blog): https://www.talkpix.ai/blog/memorial-tribute-video-cost, byline 2026-07-20, "verified" 2026-10-13] |
| Funeral-home aftercare vendor (Aftercare.com / Directors Advantage LLC) | "Aftercare Card Program" $25/family ("personalized cards mailed on meaningful days during the first year following a loss"); "Aftercare-By-Text" $150/month; "Trusted by thousands of funeral homes & cemeteries"; no photos/digital-asset content | [sourced: https://www.aftercare.com/, accessed 2026-11-03] |

**Evidence of heirs paying specifically to recover photos:** one first-hand account (TidBITS, above) of paying legal fees to get ~10,000 photos/videos out of iCloud; one AARP reader question about a late wife's locked iPhone photos (2024-10-22); DriveSavers' 2018 statement, as reported, that most passcode-lockout customers were accessing a deceased loved one's device [sourced (secondary): MacRumors thread above, 2018-11-27]. Review-site check: none of the 39 DriveSavers Trustpilot reviews mentions a deceased person or a late relative's phone [sourced: https://www.trustpilot.com/review/drivesavers.com]; Reddit and Google-reviews checks were not possible after the search budget was exhausted. No review corpus or volume figure for paid photo recovery after death was found [unknown].

### Q6. Channels to the heir

| Channel | Scale | Evidence |
|---|---|---|
| Funeral homes (US) | 15,401 funeral homes; ~75% family/privately owned; 105,300 employees; $16.3B revenue | [sourced: https://www.nfda.org/media-center/, data last updated 2025-09-29] |
| FTC Funeral Rule (how price data reaches families) | "The funeral home must give you a General Price List (GPL) that is yours to keep"; "Although they are not required to do so, many funeral homes mail their price lists, and some post them online" | [sourced: https://consumer.ftc.gov/articles/ftc-funeral-rule, page dated July 2012] |
| Tukios (tribute video + websites) | "Trusted by 10,000+ funeral homes since 2010"; "2.5M+ tribute videos created"; no public pricing; photo collection: funeral home gets "a shareable link to send via email or text, allowing families to upload their photos and videos directly"; "5 min" average build time; finished video "automatically publishes to the TV display and online obituary"; "Make your first video free" | [sourced: https://www.tukios.com/, ©2026; https://www.tukios.com/tribute-videos] |
| Tribute Technology | "Serving more than 9,000 providers worldwide" [sourced: https://www.tributetech.com/tribute-technology-the-most-comprehensive-technology-platform-provider-in-funeral-service-advances-its-customer-first-approach, 2025-12-16]. Brand ownership verified brand-by-brand in this pass: srscomputing.com 301-redirects to https://www.tributetech.com/srs ("8 years with Tribute Technology — same team, same commitment"; SRS Procession/InStone/Pet Phoenix); frontrunnerpro.com: "FrontRunner is now part of Tribute Technology" (websites, Pulse business system; footer ©2021); frazerconsultants.com: "Frazer Consultants is now part of Tribute Technology"; crakn.net 301-redirects to https://www.tributetech.com/crakn/ ("CRäKN is now Tribute Management Software"); funeraltech.com 301-redirects to https://www.tributetech.com/funeral-tech ("Funeral Tech Professional is Now Part of Tribute Technology"); runcfs.com: "CFS is now part of Tribute Technology", "Over 6,400 funeral homes trust CFS", "No contracts - No fees" (revenue from a share of sympathy-flower sales; footer ©2008–2025). Tribute's own homepage lists products (Tribute Websites, Tribute Video, Tribute Management Software, Tribute Pay, Parting Pro, etc.) but names none of the acquired brands; tributetech.com/brands is a 404 | [sourced: each brand URL above, accessed 2026-11-03] |
| Passare (case mgmt) | "1,000+ funeral homes"; "Starting at $199" | [sourced: https://www.tukiospartners.com/case-management-partners/passare] |
| Batesville | caskets, urns, memorial jewellery; "Family Choices® Digital Showroom" (online casket/cremation selection tool); "Halcyon Deathcare Management Solutions" (web-based management software); no tribute-video or website product; no funeral-home count; footer "© 2026 Batesville Services, LLC" | [sourced: https://www.batesville.com/] |
| Service Corporation International | "At September 30, 2026, we owned and operated 1,491 funeral service locations and 506 cemeteries" (prior: 1,495 / 494 at 2024-09-30) | [sourced: https://www.sec.gov/Archives/edgar/data/89089/000008908926000094/exhibit991q326earningsrele.htm, 8-K filed 2026-10-28; prior figure https://www.sec.gov/Archives/edgar/data/89089/000008908924000168/exhibit991q324earningsrele.pdf, Q3 2024 8-K] |
| Funeral-home aftercare programs | Aftercare.com: $25/family card programme, $150/month text programme, "Trusted by thousands of funeral homes & cemeteries"; NFDA's consumer site Remembering A Life (©2026 NFDA) offers planning/grief content, a funeral-home finder and a store, with no mention of photos, memorial videos or digital assets | [sourced: https://www.aftercare.com/; https://www.rememberingalife.com/] |
| Hospice | 1.91M Medicare hospice enrollees 2024; 1.3M died in hospice; 53.1% of Medicare decedents used hospice; bereavement services required "up to 1 year following the death of the patient" to "the family and other individuals in the bereavement plan of care" | [sourced: https://allianceforcareathome.org/wp-content/uploads/Facts-and-Figures-2025-Executive-Summary.pdf, 2025 edition; 42 CFR 418.64(d) via https://www.law.cornell.edu/cfr/text/42/418.64] |
| Employers / insurers (Empathy) | $72M Series C 2025-05-29, $162M total; "1 in 5 insurance claimants"; two million families under Loss Support; product = logistics, documents, LifeVault; **no photo or memorial-photo feature found**. Carrier/lives figures CONFLICT by source: Empathy's blog says "8 of the 10 top life insurance carriers" and "over 45 million lives"; Calcalist (same day) says "seven of the ten largest" and "over 50 million covered lives"; Empathy's 2026 homepage strip says "500M+ Individuals covered". Employer count: "Over 1,000 employers" appears only in Calcalist, not in Empathy's blog | [sourced: https://www.empathy.com/blog/empathy-series-c-announcement, 2025-05-29 (8/10; 45M; 1 in 5; 2M families); https://www.calcalistech.com/ctechnews/article/42w333g67, 2025-05-29 (7/10; 50M; 1,000+ employers); https://hospicenews.com/2025/05/30/bereavement-care-company-empathy-raises-72m-in-series-c-round/ ($72M; $162M); https://www.empathy.com/ (500M+, as displayed)] |
| Obituary platforms (Legacy.com) | "more than 30 million unique visitors per month" (company claim, May 2025 ad page per search snippet; page itself 403); Wikipedia repeats 30M and "more than 70 percent of all U.S. deaths" but cites 2009 sources | [sourced (secondary): https://en.wikipedia.org/wiki/Legacy.com; Passare page cites "over 40 million": https://support.passare.com/getting-started-with-legacy] |
| Estate attorneys (RUFADAA, ACTEC) | RUFADAA/digital-asset law: Everplans' state-by-state page (undated, ©2026) says "Almost all 50 states have passed laws"; its entries show Louisiana "No legislation" and Massachusetts "introduced ... but hasn't been approved yet", implying 48 states enacted if Oregon and Virginia (labelled "Proposed law" but with effective dates) are counted, 46 if not [estimated: count of entries on that page, not a figure the page states]. The 2019 count of "41 states" is retained only as a dated prior [sourced (secondary, archived): https://www.journalofaccountancy.com/issues/2019/aug/estate-planning-for-digital-assets.html, 2019-08]. ULC committee page for the act was fetched but its "Legislative Bill Tracking" section rendered empty; Wikipedia's UFADAA page returned 404. California SB 1458 effective 2025-01-01 updates it [sourced: https://dailyjournal.com/articles/388041-california-fixes-its-digital-asset-blind-spot]. ACTEC: the resource-center index (https://www.actec.org/resource-center/, ©2026) lists no digital-assets or RUFADAA resource; ACTEC position [unknown] | [sourced: https://www.everplans.com/articles/state-by-state-digital-estate-planning-laws; https://www.uniformlaws.org/committees/community-home?CommunityKey=f7237fc4-74c2-4728-81c6-b39a91ecdf22; actec.org as above] |

Observation against the variant: the two channels with real scale and a photo moment (funeral homes via Tukios/Tribute; Empathy via insurers) already own the photo touchpoint (tribute video, now with a family upload link that collects phone photos directly) or have chosen not to build one (Empathy). Aftercare programmes are cards and texts, not data services. A new entrant would be a feature inside Tukios/Tribute, not a channel partner.

### Q7. Pre-need adoption and content traffic

- Apple-specific Legacy Contact adoption: [unknown]. Searched Apple statements, surveys, and news (three searches in the first pass); nothing beyond the T&W 2026 12% (Facebook/Google) proxy already in customers.md, with Boomers at 4% — the relevant cohort for decedents.
- "Set up your legacy contact" content: dozens of how-to pages exist (Apple Support 102631, PopSci, Tom's Guide, iMore, How-To Geek, AppleInsider, MacSparky screencast 2021-12, law-firm blogs). View/traffic counts: [unknown] — Apple does not publish article popularity; YouTube view counts require either a YouTube results query (a search-engine query, not permitted once the search budget is exhausted) or known video IDs, which this pass does not have. Not attempted; flagged for a later pass with search budget.

### Q8. Sensitivity and timing

- Forcing function: funeral homes need slideshow photos "A day or two before the service", "Typically 30 to 100 photos", collected as "Scans or phone pictures of the prints" [sourced (vendor): https://timelinescan.com/funeral-photo-slideshow/, undated]. How funeral homes collect them today: Tukios gives the funeral home "a shareable link to send via email or text, allowing families to upload their photos and videos directly" [sourced: https://www.tukios.com/tribute-videos]. What funeral homes charge: slideshows are often included in the package; "As a paid add-on, it usually runs somewhere around $75 to $300" [sourced (secondary): talkpix.ai, 2026-07-20]; "our services may already be included in what they've arranged" [sourced: https://www.eulogizememorials.com/pricing]. No funeral-home General Price List was sampled: the FTC does not require GPLs to be posted online [sourced: consumer.ftc.gov, 2012] and no GPL URL could be located without search [unknown]. Tukios' 2.5M+ videos (above) show the photo-gathering moment is already served at the funeral home.
- Grief guidance on the full archive: no fixed timeline; "You are not procrastinating, you are grieving"; "When the time is right, it will be easier, but not easy" [sourced: https://thephotomanagers.com/after-death-parents-photos/, 2017-08-07]. Hospice bereavement support window is up to one year (42 CFR 418.64(d)). Apple's window is three years from approval; Google may delete accounts inactive for two years (customers.md).
- Interpretation: there are two distinct moments — a scramble, "a day or two before the service", for 30–100 photos (served by funeral homes, increasingly via a phone upload link) and a months-to-years archive job with a three-year Apple deadline and a 14-day download window per Apple data request. The variant's premise ("at the moment of death, when the platform hands over a bulk export") describes the second, which has no forcing function except the deletion clocks.

## Funnel table (per year, US)

| Step | Value | Tag |
|---|---|---|
| Deaths | 3,072,666 (2024) | [sourced: NCHS db548] |
| Deaths age 15+ | 3,042,833 | [estimated: total minus <15 bands] |
| Decedents who owned a smartphone | 2.17M–2.51M | [estimated: Scenario B–A above; 85+ ownership unsourced; upper end uses 97% for 45–54] |
| ...with a photo library worth consolidating | [unknown] | no survey of library size by age |
| Heir with access (Legacy Contact / IAM set, or passcode known) | [unknown]; proxy ceiling 4–12% have FB/Google controls (Boomers 4%) | [sourced: T&W 2026 via customers.md]; Apple-specific [unknown]; passcode-known share [unknown] |
| Heir without access who obtains a court order | [unknown]; cost: court filing $45–$1,250 (NY, by estate value) or $230–$395 (FL) plus attorney $750 (quoted)–$1,200 (billed) (forum) to $3k–10k (vendor claim); months | [sourced: nysenate.gov SCPA 2402; flsenate.gov 28.2401; TidBITS 2025; afterlife.ai 2026] |
| Heir who wants consolidation (beyond 30–100 slideshow photos) | [unknown] | no survey found |
| Heir who pays | [unknown]; price anchors: $0–$300 funeral-home slideshow add-on, $69 Eulogize, $99 Keeper Plus one-time, $99.99/yr Everplans, $149 GoodTrust, $800–$3,900 forensic recovery | [sourced: vendor pages above] |

## 3. Numbers table

| Number | Tag |
|---|---|
| US deaths 2024: 3,072,666; bands as listed in Q1 | [sourced: cdc.gov db548, Jan 2026] |
| 76.2% of deaths at 65+; 29.0% at 85+ | [estimated: band sums / total] |
| Pew 2026 smartphone: 97/97/91/79% (18–29/30–49/50–64/65+); n=5,511 | [sourced: pewresearch.org mobile fact sheet, 2026-10-19] |
| Pew 2025: 65+ 78% | [sourced: pewresearch.org short read 2026-01-08] |
| Decedents with smartphone: 2.50M (A, 91% for 45–54) / 2.51M (A, 97% for 45–54) / 2.17M (B) | [estimated: see Q1] |
| England & Wales 2024 deaths: 568,613 | [sourced: ons.gov.uk, 2025-10-09] |
| EU 2024 deaths: 4.81M; crude rate 10.7/1,000 | [sourced: eurostat, Mar 2026] |
| Apple legacy access: 3 years from first approval | [sourced: support.apple.com/102678, 2026-08-10] |
| Apple Data & Privacy export: originals; 14 days to download | [sourced: support.apple.com/102208, 2026-09-11] |
| iCloud.com: 1,000 items per download batch | [sourced: support.apple.com/111762, 2026-04-10] |
| Apple→Google transfer: 3–7 days, up to 30; 20,000 photos/album cap at Google | [sourced: support.apple.com/HT208514, 2026-10-09] |
| Court-order attorney cost: $750 quoted (plus filing fee); $1,200 billed (~30 min advice, Vermont) | [sourced: talk.tidbits.com 30659 pp. 1–2, 2025-04-01 and 2025-04-05] |
| Court-order cost $3k–10k, 6–12 months | [sourced: afterlife.ai, 2026-06-04; vendor, unverified] |
| Photos recovered in one court-order case: ~10,000 | [sourced: talk.tidbits.com, 2025-06-14] |
| NY Surrogate's Court probate/administration filing fee: $45–$1,250 by estate value | [sourced: nysenate.gov SCPA 2402(7)] |
| FL probate clerk fee: $395 formal; $340 / $230 summary; $230 disposition without administration | [sourced: flsenate.gov 28.2401 (2025)] |
| Google IAM: up to 10 contacts; download link by email | [sourced: support.google.com/3036546] |
| DriveSavers passcode lockout: "around $3,900" (2018) | [sourced (secondary): forums.macrumors.com thread 2157359, 2018-11-27] |
| DriveSavers 2026 quotes in reviews: $900–$3,900; $3,700–3,900; $3.5K; Trustpilot 2.8/5, 39 reviews | [sourced: trustpilot.com/review/drivesavers.com, reviews 2026-02 to 2026-10] |
| DriveSavers standard: $3,000–4,000 vs $300–1,200 industry (competitor) | [sourced: ipadrehab.com article 55] |
| MD Repairs: $800–2,000 forensic unlock; $500–1,200 damaged iPhone | [sourced: mdrepairs.com, 2026-09-09] |
| Everplans $99.99/yr; free = 3 items; founded 2012; acquired by Precoa Oct 2024 | [sourced: everplans.com/pricing; everplans.com/about] |
| GoodTrust $149; $39/yr after (secondary); seed $2.3M (2021-01) + $5M (2021-12, "total $7.5M", secondary unverified); later totals and customer count | [sourced: mygoodtrust.com; venturebeat 2021; finsmes 2021-12 (403)]; later totals/customers [unknown] |
| Clocr $30/mo, $141/yr; lifetime "$1500" and "$475/Onetime *" (both shown); "+$19 Yearly Maintenance" (attachment unclear); attorney-assisted trust $3,000 | [sourced: clocr.com/pricing] |
| Trust & Will $199 Will / $499 Trust / $1,499 attorney; $49/yr membership incl. Digital Vault; +$299 attorney support | [sourced: trustandwill.com/pricing] |
| Keeper: $0 Basic (1 page, 5 photos; FAQ says 2 pages); $99 Plus one-time; $350 Concierge | [sourced: mykeeper.com/pricing] |
| Eulogize $69 / $20 | [sourced: eulogizememorials.com/pricing] |
| Tribute video survey: funeral-home add-on $75–$300 (often included); pro $150–$600; complex $800–$2,000; $50–$150/hr; rush +25–50%; DIY $0–~$50 | [sourced (secondary): talkpix.ai, 2026-07-20] |
| Aftercare.com: $25/family cards; $150/month texts | [sourced: aftercare.com] |
| Funeral homes 15,401; 105,300 staff; $16.3B | [sourced: nfda.org media center, 2025-09-29] |
| Tukios 10,000+ funeral homes; 2.5M+ tribute videos; 5-min average build | [sourced: tukios.com, vendor claim] |
| Tribute Technology 9,000+ providers; CFS "Over 6,400 funeral homes" | [sourced: tributetech.com, 2025-12-16; runcfs.com ©2025] |
| Passare 1,000+ funeral homes; from $199 | [sourced: tukiospartners.com] |
| SCI 1,491 funeral locations, 506 cemeteries (2026-09-30); 1,495 / 494 (2024-09-30) | [sourced: SEC 8-K 2026-10-28; SEC 8-K Q3 2024] |
| Hospice 2024: 1.91M enrollees; 1.3M died in hospice; 53.1% of Medicare decedents | [sourced: Alliance 2025 Facts & Figures exec summary] |
| Hospice bereavement services up to 1 year | [sourced: 42 CFR 418.64(d)] |
| Empathy $72M Series C, $162M total; 2M families; 1 in 5 claimants | [sourced: empathy.com blog 2025-05-29; hospicenews 2025-05-30] |
| Empathy carriers/lives: 8/10 and 45M (Empathy blog) vs 7/10 and 50M (Calcalist) vs "500M+" (empathy.com 2026 homepage) — conflicting | [sourced: as listed in Q6] |
| Empathy employers: 1,000+ | [sourced (secondary): calcalistech 2025-05-29 only] |
| Legacy.com 30M+ monthly uniques (company); 70% of US deaths (2009) | [sourced (secondary): Wikipedia; legacy.com ad page 403] |
| Funeral slideshow: 30–100 photos, due "a day or two before the service" | [sourced (vendor): timelinescan.com] |
| RUFADAA: 46–48 states (count of Everplans state entries, ©2026, undated); 41 states (2019) | [estimated: from everplans.com state list]; [sourced (secondary, archived): journalofaccountancy 2019-08] |
| Apple Legacy Contact adoption; Google IAM adoption | [unknown] |
| Share of decedents whose heir knows the passcode | [unknown] |
| Google deceased-data delivery format and time | [unknown] |
| Cellebrite consumer pricing; digital-executor service pricing; attorney digital-asset fee surveys | [unknown] |

## 4. Unknowns and what was tried

1. **Apple Legacy Contact adoption rate** — three extended searches (Apple statements, surveys, "percent"); nothing. Only T&W 2026 FB/Google proxy exists.
2. **Album / People-name structure of the legacy or court-order export** — Apple's public Data & Privacy article (102208, 2026-09-11) confirms originals and a 14-day download window but says its file guides do not cover photos; the three legacy articles and the iCloud.com download article say nothing about albums or metadata. Only the Transfer-to-Google tool documents album handling.
3. **Google "obtain data" outcomes** — Google's pages give no document list, timeline, or format; no first-hand forum account found (one extended search); Q&A-site timing claims are unverified.
4. **Smartphone ownership at 75–84 and 85+** — Pew publishes 65+ only; Ofcom pages (landing, 2024 report, 2025 PDF path) all returned 403. The funnel's top step is therefore a range.
5. **Court-order cost/time distribution** — statutory filing fees found for NY and FL; CA fee PDF 403; no attorney fee survey reachable (lawyers.com 403; nolo/legalzoom/findlaw 404 earlier); one forum case ($750 quoted, $1,200 billed) and one vendor claim ($3k–10k).
6. **Share of heirs who know the passcode** — no survey found.
7. **Heir willingness to pay for consolidation (vs a 30–100-photo slideshow)** — no survey; DriveSavers' 39 Trustpilot reviews contain no bereavement cases; Reddit/Google-reviews not checkable after search budget exhaustion.
8. **Ever Loved, LifeSite pricing/traction; Everplans and GoodTrust traction** — Ever Loved 403, LifeSite 525; Everplans about/press pages give founding year and Precoa acquisition but no counts, precoa.com/news 404; GoodTrust home/about pages give investors but no customer count; Cake now redirects to a funeral network. Keeper pricing now sourced from mykeeper.com.
9. **Tribute video price inside funeral-home GPLs** — FTC does not require online GPLs; no GPL URL could be located without search; only the talkpix secondary range ($75–$300 add-on, often included) and DIY vendor prices.
10. **Legacy.com current traffic** — company ad page 403; only Wikipedia (2009 citations) and partner pages.
11. **YouTube/Apple article traffic for "set up legacy contact"** — not attempted: requires a YouTube query (search) or known video IDs.
12. **Samsung deceased process** — no Samsung policy page; UK community thread did not render.
13. **Cellebrite consumer offering** — cellebrite.com FAQ 404, about-us 403, investors site 403; no consumer page located.
14. **"Digital executor" services and attorney digital-asset fees** — no search possible in the repair pass; none of the fetched estate-planning vendors sells one.
15. **ACTEC position on digital assets** — actec.org resource-center index lists nothing on the topic; its internal search was not used.
16. **Current RUFADAA count from the ULC itself** — the ULC committee page rendered without enactment data; Wikipedia 404; Everplans' state list used as a secondary proxy (46–48).

## 5. Source list (all accessed 2026-11-03)

Primary
1. https://www.cdc.gov/nchs/products/databriefs/db548.htm — NCHS Data Brief 548, Mortality in the US 2024 (Jan 2026)
2. https://www.pewresearch.org/internet/fact-sheet/mobile/ — Pew mobile fact sheet (2026-10-19)
3. https://www.pewresearch.org/short-reads/2026/01/08/internet-use-smartphone-ownership-digital-divides-in-u-s/ — Pew (2026-01-08)
4. https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/bulletins/deathsregistrationsummarytables/2024 — ONS (2025-10-09)
5. https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Mortality_and_life_expectancy_statistics — Eurostat (Mar 2026)
6. https://support.apple.com/en-us/103128 — Data a Legacy Contact can access (2026-04-02)
7. https://support.apple.com/en-us/102678 — Request access as a Legacy Contact (2026-08-10)
8. https://support.apple.com/en-us/102631 — Add a Legacy Contact (undated)
9. https://support.apple.com/digital-legacy — Request access to a deceased family member's Apple Account (undated)
10. https://support.apple.com/guide/security/legacy-contact-security-secebf027fb8/web — Platform Security: Legacy Contact
11. https://support.apple.com/en-us/111762 — Download iCloud photos and videos (2026-04-10)
12. https://support.apple.com/HT208514 — Transfer a copy of iCloud Photos to another service (2026-10-09)
13. https://support.apple.com/en-us/102208 — Get a copy of the data associated with your Apple Account (2026-09-11); HT208502 resolves here
14. https://support.google.com/accounts/contact/deceased — Google deceased-user request form
15. https://support.google.com/accounts/answer/2842525?hl=en — Google deceased-user help
16. https://support.google.com/accounts/answer/3036546 — Inactive Account Manager
17. https://talk.tidbits.com/t/how-to-access-data-from-deceased-apple-customers-without-a-lawyer/30659 and ?page=2 — forum, 2025-04 to 2025-06 (both pages text-searched 2026-11-03)
18. https://community.samsung.com/my/conversations/tablets/how-to-access-deceased-family-members-samsung-phone-and-tablet/r1_33375046 — Samsung Community, 2025-05-25
19. https://www.nysenate.gov/legislation/laws/SCP/2402 — NY SCPA 2402 fee schedule
20. https://www.flsenate.gov/Laws/Statutes/2025/28.2401 — Florida clerk charges (2025)
21. https://www.nfda.org/media-center/ — NFDA statistics (2025-09-29)
22. https://consumer.ftc.gov/articles/ftc-funeral-rule — FTC Funeral Rule (July 2012)
23. https://www.tukios.com/ and https://www.tukios.com/tribute-videos — Tukios (©2026)
24. https://www.tukiospartners.com/case-management-partners/passare — Passare count/price
25. https://www.tributetech.com/tribute-technology-the-most-comprehensive-technology-platform-provider-in-funeral-service-advances-its-customer-first-approach — Tribute Technology (2025-12-16); https://www.tributetech.com/ ; https://www.tributetech.com/srs ; https://www.tributetech.com/crakn/ ; https://www.tributetech.com/funeral-tech ; https://www.tributetech.com/about
26. https://www.frontrunnerpro.com/ ; https://www.frazerconsultants.com/ ; https://www.runcfs.com/ — brand pages stating "now part of Tribute Technology"
27. https://www.batesville.com/ — Batesville (©2026)
28. https://www.aftercare.com/ — Aftercare.com pricing
29. https://www.rememberingalife.com/ — NFDA consumer site (©2026)
30. https://www.sec.gov/Archives/edgar/data/89089/000008908926000094/exhibit991q326earningsrele.htm — SCI Q3 2026 8-K exhibit (2026-10-28); https://www.sec.gov/Archives/edgar/data/89089/000008908924000168/exhibit991q324earningsrele.pdf — SCI Q3 2024 8-K
31. https://allianceforcareathome.org/wp-content/uploads/Facts-and-Figures-2025-Executive-Summary.pdf — 2025 Facts & Figures (text extracted locally with pdftotext)
32. https://allianceforcareathome.org/2025-facts-and-figures-report-now-available-to-alliance-members/ — (2026-03-03)
33. https://www.law.cornell.edu/cfr/text/42/418.64 — 42 CFR 418.64(d)
34. https://www.empathy.com/blog/empathy-series-c-announcement — Empathy (2025-05-29); https://www.empathy.com/ (©2026)
35. https://www.everplans.com/pricing ; https://www.everplans.com/about ; https://www.everplans.com/press — Everplans
36. https://mygoodtrust.com/ ; https://mygoodtrust.com/pricing ; https://mygoodtrust.com/about — GoodTrust
37. https://clocr.com/pricing/ — Clocr
38. https://www.trustandwill.com/pricing — Trust & Will
39. https://www.mykeeper.com/pricing — Keeper
40. https://www.eulogizememorials.com/pricing — Eulogize
41. https://mdrepairs.com/blog/deceased-family-member-data-recovery/ — MD Repairs (2026-09-09)
42. https://www.ipadrehab.com/article.cfm?ArticleNumber=55 — iPad Rehab vs DriveSavers (©2026)
43. https://www.trustpilot.com/review/drivesavers.com — DriveSavers reviews (2.8/5, 39 reviews)
44. https://www.altogetherfuneral.com/ — Cake redirect target
45. https://thephotomanagers.com/after-death-parents-photos/ — (2017-08-07)
46. https://timelinescan.com/funeral-photo-slideshow/ — vendor guidance
47. https://www.uniformlaws.org/committees/community-home?CommunityKey=f7237fc4-74c2-4728-81c6-b39a91ecdf22 — ULC RUFADAA committee page (no enactment data rendered)
48. https://www.actec.org/resource-center/ — ACTEC resource index (©2026)

Secondary
49. https://www.calcalistech.com/ctechnews/article/42w333g67 — Empathy employers/insurers (2025-05-29)
50. https://hospicenews.com/2025/05/30/bereavement-care-company-empathy-raises-72m-in-series-c-round/
51. https://www.aarp.org/personal-technology/tech-guru-unlock-dead-spouses-phone/ — AARP (2024-10-22)
52. https://funeral.com/blogs/the-journal/icloud-inheritance-and-apple-legacy-contact-how-access-works-and-what-families-need — (2026-01-20)
53. https://www.afterlife.ai/what-happens-to-icloud-when-you-die/ — vendor claim (2026-06-04)
54. https://floridaprobateandfamilylaw.com/blog/how-to-access-an-apple-account-after-someone-passed-away/ — (2021-12-08)
55. https://forums.macrumors.com/threads/drivesavers-lets-consumers-retrieve-data-from-locked-ios-devices-for-3-900-updated.2157359/ — (2018-11-27); the businesswire (403) and helpnetsecurity (405) originals were not retrievable
56. https://venturebeat.com/business/goodtrust-raises-2-3-million-for-digital-legacy-platform — (2021-01); https://www.finsmes.com/2021/12/goodtrust-raises-5m-in-seed-funding.html — (2021-12; 403 at audit, unverified)
57. https://www.ncoa.org/product-resources/estate-planning/goodtrust-willmaker-review/ — GoodTrust $39/yr
58. https://en.wikipedia.org/wiki/Legacy.com — traffic claims (2009 citations); https://support.passare.com/getting-started-with-legacy
59. https://www.everplans.com/articles/the-top-10-online-memorial-websites — Keeper QR description
60. https://www.everplans.com/articles/state-by-state-digital-estate-planning-laws — RUFADAA state list (©2026, undated)
61. https://www.journalofaccountancy.com/issues/2019/aug/estate-planning-for-digital-assets.html — RUFADAA 41 states (2019, archived); https://dailyjournal.com/articles/388041-california-fixes-its-digital-asset-blind-spot
62. https://www.talkpix.ai/blog/memorial-tribute-video-cost — tribute-video price survey (2026-07-20)
63. https://www.foxnews.com/tech/how-unlock-android-device-windows-pc-when-owner-passes-away; https://tech.yahoo.com/general/articles/ask-jerry-google-help-access-180005532.html — Android/Google guidance

Not retrievable in the repair pass (recorded so the next pass does not repeat them): businesswire.com DriveSavers release (403); drivesavers.com (403); www4.courts.ca.gov filing-fee PDF (403); lawyers.com probate-cost page (403); ofcom.org.uk media-use pages and 2025 PDF (403); cellebrite.com FAQ (404) / about-us (403) / investors (403); empathy.com/pricing (404); tributetech.com/brands (404); en.wikipedia.org UFADAA article (404); precoa.com/news (404).

## Audit log

Each auditor finding and what was done (2026-11-03 repair pass; WebSearch budget was exhausted at the start of the pass, so every fix below rests on direct fetches of known URLs, and gaps that needed search are marked as such).

Untagged numbers
1. GoodTrust Tracxn/PitchBook/"200,000 customers" — no URL could be fetched for any of the three; all three withdrawn from the row and the numbers table; replaced with the investor list from mygoodtrust.com/about and [unknown] for post-2021 totals and customer count.
2. Empathy "$65 after free month" — no source; withdrawn. empathy.com/pricing is a 404 and the homepage is demo-only B2B, recorded in the row.
3. "Funeral Video Maker $39/$99/$249; pro $299–$850" — never fetched; removed from Q5, Q8, funnel and numbers tables. Replaced with the talkpix page's actual figures ($75–$300 add-on, often included; $150–$600; $800–$2,000; $50–$150/hr; rush 25–50%; DIY $0–~$50), correctly attributed and dated.
4. Keeper "two memorials / Keeper Plus" — now sourced from mykeeper.com/pricing ($0 Basic with "1 Memorial Page" and "Up to 5 Photos and Videos", FAQ says two pages — inconsistency noted; Plus $99 one-time; Concierge $350). Everplans top-10 page kept only for the QR-on-headstone description.
5. "1–3 day scramble" — changed to the source's wording, "a day or two before the service", in Q8 and the numbers table.
6. TidBITS "30 minutes" — re-verified by text search of page 2: "It cost the estate (not me) about 30 minutes of his time to learn exactly how to word the initial petitions" (2025-04-05); "Vermont" also verified on the same post. Both retained, now quoted verbatim with the page URL; poster usernames not reproduced per project rules.

Suspect claims
7. talkpix misattribution (major) — fixed as in item 3; the funeral-home add-on range the brief asked for is now used in Q5, Q6/Q8 and the funnel.
8. Tribute Technology brand ownership (major) — verified brand by brand: srscomputing.com, crakn.net and funeraltech.com 301-redirect to tributetech.com sub-pages; frontrunnerpro.com, frazerconsultants.com and runcfs.com each carry a "now part of Tribute Technology" statement; CFS adds "Over 6,400 funeral homes". The 9,000-provider press release is now cited only for the count.
9. Keeper (minor) — fixed as in item 4.
10. mdrepairs paraphrases dressed as quotes (minor) — rewritten as explicit paraphrases in Q3 and Q4; only "Without the passcode, the data is mathematically unreachable." remains in quotation marks.
11. Clocr lifetime ambiguity (minor) — row now shows both "$1500" and "$475/Onetime *" and states that the "+$19 Yearly Maintenance" line does not say which option it attaches to.
12. Empathy source conflict (minor) — Q6 row and numbers table now state the 8/10-vs-7/10 and 45M-vs-50M conflict explicitly, attribute "1,000+ employers" to Calcalist only, and add the homepage's "500M+" as a third unreconciled figure.
13. RUFADAA 41 states (minor) — ULC committee page fetched (no enactment data rendered); Wikipedia 404; Everplans state-by-state page used as a dated secondary proxy giving 46–48 states by count of entries [estimated]; 2019 figure retained only as a prior.
14. SCI two-year-old filing (minor) — EDGAR index fetched; Q3 2026 8-K (filed 2026-10-28) exhibit 99.1 quoted: 1,491 funeral service locations and 506 cemeteries at 2026-09-30; prior 1,495/494 kept for comparison.
15. DriveSavers $3,900 (minor) — businesswire 403 and helpnetsecurity 405 again; MacRumors thread (2018-11-27) fetched and quotes "priced around $3,900" and the deceased-loved-one statement; Trustpilot adds 2026 quotes of $900–$3,900. Row retagged accordingly.
16. TidBITS "30 minutes"/"Vermont" (minor) — verified, see item 6.
17. Scenario A 45–54 at 91% (minor) — added the 97% alternative (153,037; total 2,508,513 ≈ 2.51M) and widened the funnel range to 2.17–2.51M.

Broken/misquoted sources
18. talkpix — fixed (items 3, 7). tributetech press release — fixed (item 8). everplans top-10 — fixed (item 4). mdrepairs — fixed (item 10). helpnetsecurity/businesswire — replaced by MacRumors (item 15). finsmes — still 403; kept as secondary, marked unverified. calcalistech conflict — flagged (item 12). Sources marked "VERIFIED AS STATED" were left unchanged.

Missing vs brief
19. Q2 export format — Apple 102208 (2026-09-11) fetched: originals, 14-day download window, file guides exclude photos; HT208502 resolves to the same article; album/People structure still [unknown] and stated as such.
20. Q2 court fee pages — NY SCPA 2402(7) and Fla. Stat. 28.2401 fee schedules added from statute text; CA PDF 403; attorney-fee surveys unreachable (lawyers.com 403) and marked [unknown] with attempts listed.
21. Q5 Cellebrite — attempted three Cellebrite URLs (404/403/403); row added as [unknown] with the attempts.
22. Q5 digital executor / attorney digital-asset fees — row added as [unknown]; notes that none of the fetched vendors sells one and that Clocr's attorney-assisted trust is $3,000.
23. Q5 Everplans/GoodTrust traction; Trust & Will from vendor — Everplans about/press fetched (founded 2012; Precoa acquisition Oct 2024; no counts); GoodTrust home/about fetched (investors; no counts); Trust & Will pricing now from trustandwill.com ($199/$499/$1,499; $49/yr membership with Digital Vault; +$299).
24. Q5 review evidence — Trustpilot DriveSavers fetched (39 reviews, none bereavement-related); Reddit/Google reviews not possible without search; stated.
25. Q6 aftercare, Batesville, ACTEC — aftercare.com ($25/family; $150/month) and NFDA Remembering A Life added; batesville.com fetched (Family Choices Digital Showroom; Halcyon software; no tribute/website product); actec.org resource index fetched, nothing on digital assets, marked [unknown].
26. Q6 SRS/FrontRunner direct pages — fetched (item 8).
27. Q7 YouTube views — explicitly recorded as not attempted and why (requires a search query or known video IDs).
28. Q8 funeral-home tribute price — talkpix add-on range now used; FTC page cited for why GPLs are not reliably online; no GPL sampled, stated as [unknown] with reason.
29. Q8 photo collection — Tukios tribute-video page fetched: shareable upload link by email/text, 5-minute average build, auto-publish to TV display and obituary.
30. Q1 Ofcom — three direct URLs tried, all 403; recorded.
31. Funnel and channel tables — retained; funnel price anchors and court-cost row updated to the sourced figures above.
