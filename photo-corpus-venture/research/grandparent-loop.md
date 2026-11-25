# Track R9 — The grandparent invite loop (FamilyAlbum / Tinybeans) as a proven $100M consumer mechanism

Date of research: 2026-11-03 (repaired same day after audit; see §8). All URLs accessed 2026-11-03 unless stated. Currency: ¥ = JPY, $ = USD, A$ = AUD.
Inputs read first: `research/customers.md` Q1(h) (FamilyAlbum ¥17.1B Lifestyle FY2026; Tinybeans ~95k paid) and `research/sizing.md` Q4 (CAC: Qeepsake $35; FamilyAlbum CAC [unknown]).

Bottom line up front: the mechanism is real and one company has scaled it to ~¥17B (~$114M at ¥150/$ [estimated: ¥17,159M ÷ 150; FX assumed]) — but only after 11 years [estimated: launched April 2015 per S2 → 2026], 30M registrations [sourced: S2, 2026-05-07], free unlimited storage subsidised by a games business [sourced: S6 CFO section], a segment margin of ~5% [estimated: ¥876M ÷ ¥17,159M, S5], and segment ad spend of ~¥1.9–2.0B/yr (≈13–15% of segment sales) [sourced: S3 p.30; estimated: sums below]. The second-best operator (Tinybeans) is a A$7.33M micro-cap [sourced-secondary: S32, 2026-11-03] with ~95k paid subs [sourced-secondary: S29, 2026-08-27]. No operator discloses relatives-per-family, invite acceptance, or grandparent engagement. The loop is proven for *acquisition*; it is not proven as a path to a paid multigenerational *archive*.

---

## 1. Questions asked

1. MIXI FamilyAlbum from filings/IR: users, paying subs, prices by country, revenue split, overseas share, marketing spend, retention, invite mechanics, multigenerational roadmap, AI.
2. Tinybeans (ASX: TNY): FY25/FY26 KPIs, pivot statements, Qeepsake deal and CAC, share price, cash; what has not worked.
3. Other newborn-wedge apps: Lifecake→BackThen, 23snaps, Keepy, Peekaboo Moments, Baby Pics, Kinzoo; App Store rating counts.
4. The invite mechanic quantified; Pew/AARP grandparent tech data.
5. Distribution channels and CAC evidence; FamilyAlbum US marketing.
6. Economics of free unlimited storage; gross margins; implication for an entrant.
7. Falsification: wedge not extending to archives; grandparents refusing apps.

---

## 2. Findings per question

### Q1. MIXI / FamilyAlbum (みてね) — from IR documents

**Documents actually read (text-extracted locally with pdftotext/pypdf; WebFetch cannot read irpocket/ASX PDFs):** FY2026 earnings summary (決算短信, 2026-05-15) [S5]; Q1 FY2026 results deck (2025-07-31) [S3]; Introductory Materials for Investors (2026-06-26) [S4]; Integrated Report 2026 (11.5 MB) [S6]; 30M-user release, JP and EN (2026-05-07) [S1][S2]; 15M-user release (2022-08-26) [S10]; Q2 and Q4 FY2026 call transcripts (Investing.com, secondary) [S8][S7]. The FY2026 Q4 and Q3 results decks could not be located (MIXI's IR document lists render dynamically; irpocket URLs are unguessable). S4 reposts Q4 FY2026 slides, but only the capital-allocation, portfolio-management and shareholder-return pages (S4 pp.23–25, each marked "Repost From FY2026 Q4"); a full-text scan of S4 for "comment", "sticker", "posts", "MAU", "paying" finds only the product description "family members can communicate with comments and other features" (p.14) — the Q4 deck's "comments and stickers posted" chart and any premium-subscriber chart are **not** in S4 and remain unread.

- **Registered users:** "surpassed 30 million users worldwide on May 7, 2026", defined as "Total number of registered users using the iOS/Android app and browser version" — i.e. individuals (parents + invited relatives), not families; the app "launched in April 2015" [sourced: S2, 2026-05-07]. Milestones: 15M (2022-08-14) [S10]; 25M (Jan 2025) [S3 slide 37]; 27M (Jul 2025) [S1]; 30M (May 2026). Registration run-rate: 3M in the 10 months Jul 2025→May 2026 ≈ **3.6M/yr** [estimated: 3M ÷ 10 × 12]; 2M in the 6 months Jan→Jul 2025 ≈ 4.0M/yr [estimated]. MAU 12M (May 2026) [sourced-secondary: S7 "The number of users has reached 30 million, and MAU has reached 12 million"; also mixi.co.jp/en/ir/message/ per customers.md]. MAU/registered = 40% [estimated: 12M ÷ 30M].
- **Japan penetration:** "used by approximately 65% of parents in Japan as the app they use when their children are born" (65% as of Dec 2024; computed from child birthdates entered at sign-up vs MHLW vital statistics) [sourced: S2]. Was 47.1% in Aug 2022 [sourced: S10].
- **Overseas share:** "Over 40% of our users are outside Japan, with North America alone making up 20%" [sourced: S2]. Q1 FY2026 deck: overseas 41.5% at end-June 2025, "全体の2割程度が北米" [sourced: S3 p.37]. In 2022 North America was "about half of overseas users" [sourced: S10]. "new overseas family registrations keep exceeding Japanese new registrations" [sourced: S1]. Per-country (UK/DE/FR) user splits: [unknown — not disclosed in any document read].
- **Paying subscribers (Premium):** [unknown]. No document read gives a count. The Q1 FY2026 deck shows a stacked revenue-mix bar (GPS / プレミアム / 写真プリント / その他) without values, and states "注力商材のうちプレミアムプランとGPSが前年同期比1.5倍成長" and FamilyAlbum sales +37.1% YoY [sourced: S3 p.12]. FY2026 earnings summary: ライフスタイル segment sales ¥17,159M (+16.0% from ¥14,795M), segment profit ¥876M (vs loss ¥128M) [sourced: S5 p.2]. FamilyAlbum-only revenue: [unknown] (segment also includes minimo, mixi, mixi2). Quarterly Lifestyle sales / segment profit (labelled セグメント利益（EBITDA） in S3, ¥M): FY2024 Q1–Q4 2,421/2,129/6,131/2,736 and −374/−308/+747/−747; FY2025 2,736/2,719/5,942/3,397 and −301/−211/+1,008/−623; FY2026 Q1 3,505 and −69 [sourced: S3 p.11]. Q2 FY2026 ≈ ¥3.5B (+32%), "EBITDA turned profitable for the first time in Q2", FamilyAlbum +36.9% [sourced-secondary: S8]; Q3 ¥5,598M (−5.8%, New Year cards shrinking), EBITDA ¥1,079M [sourced-secondary: S9]; Q4 ¥4.4B (+31.4%), "focus areas" +37.5%; Lifestyle "Net sales has grown steadily with a 5-year CAGR of 20%" [sourced-secondary: S7, 2026-05-18, verbatim].
- **Price points by country (App Store IAP lists, fetched 2026-11-03):** US: Premium One $2.99/mo; Premium Family $5.99/mo or $59.00/yr; Premium Family Pro $10.99/mo or $109.00/yr; Sticker Subscription $3.99 [sourced: S15]. UK: Premium One £2.99; Premium Family £5.49/mo or £54.99/yr; Premium Family Pro £10.49/mo or £104.99/yr [sourced: S15-GB]. Germany: Premium One €2,99; Premium Family €5,49/mo or €54,99/yr; Premium Family Pro €10,49/mo or €104,99/yr [sourced: S15-DE]. France: Premium Individuel €2,99; Premium Famille €5,49/mo or €54,99/yr; Premium Famille Pro €10,49/mo or €104,99/yr [sourced: S15-FR]. No sticker subscription is listed on the GB/DE/FR storefronts. Japan: プレミアム 590円/月, Pro 1,090円/月 [sourced-secondary: S47 pricey.jp, 2026; an older article quotes 480円 — price has moved]. Rating counts by storefront: US 380K/4.9; GB 59k/4.8; DE 22,175/4.7; FR 51k/4.8 [sourced: S15, S15-GB, S15-DE, S15-FR].
- **Revenue split premium vs physical:** [unknown]. Direction only: "increasing the proportion of net sales from digital products such as subscriptions and advertising" [sourced-secondary: S7]; New Year cards declining "due to market shrinkage" while "注力領域（みてねプレミアム、写真プリント、みてねみまもりGPS、広告）の売上は伸長" [sourced: S5 p.2].
- **Marketing spend (Lifestyle segment, disclosed quarterly):** S3 p.30 "セグメント別 売上原価・販管費内訳" prints 広告宣伝費（販管費） for ライフスタイル (¥M): FY2024 Q1–Q4 = 358 / 279 / 940 / 462; FY2025 = 445 / 378 / 533 / 582; FY2026 Q1 = 485 [sourced: S3 p.30, 2025-07-31]. Annual sums: FY2024 ¥2,039M = 15.2% of FY2024 Lifestyle sales ¥13,417M; FY2025 ¥1,938M = 13.1% of ¥14,795M; Q1 FY2026 ¥485M = 13.8% of ¥3,505M [estimated: sums of the quarterly rows ÷ S3 p.11 / S5 sales]. Caveats: the segment also carries minimo and mixi2 marketing (mixi2 launched in the segment during FY2025), so this is an **upper bound** for FamilyAlbum ad spend; it is the advertising line only (no staff or agency costs). Lifestyle headcount 207 (Q1 FY2024) → 279 (Q1 FY2026) [sourced: S3 p.33]. **Ad spend per net new registered individual:** ¥1,938M FY2025 spend ÷ ~3.6–4.0M registrations/yr ≈ **¥480–540 ≈ $3.2–3.6** [estimated: FY2025 ad spend ÷ 2025–26 registration run-rate; mismatched periods; registrations include invited relatives, so cost per *family* is k× higher where k = members per family, [unknown]]. Statements: Q1 FY2026 EBITDA "海外ユーザー獲得に向けた投資を継続しているため引き続き赤字" [sourced: S3 p.11]; MIXI's model is "過度なマーケティングコストに頼らず…ソーシャル性を通じて長期的な利益を創出" [sourced: S6 CFO section]; "2027年3月期以降は、ユーザー獲得だけでなく投資効率の向上に重点" [sourced: S6, FamilyAlbum GM section]. Consolidated 広告宣伝費 FY2026 ¥27,387M (+54.5%) [sourced-secondary: S46 irbank.net; company-wide]; S3 p.30 shows consolidated quarterly ad spend FY2025 3,325/4,831/4,892/4,679 and Q1 FY2026 4,181, of which Digital Entertainment is 1,649/3,287/2,819/2,285 and 1,802 [sourced: S3 p.30].
- **Retention:** no churn figure disclosed. KPIs MIXI says it monitors: MAU, WAF (週間アクティブ家族数, weekly active families) growth rate for global expansion, and "写真へのリアクション件数" (reactions on photos) as the inter-user-communication KPI that gates investment acceleration [sourced: S6]. Values: [unknown]. Guidance language for FY2027: "みてね経済圏のユーザー拡大及び課金率の維持" (expand users, *maintain* paying rate) [sourced: S5 p.3]; the English call says "stable monetization rate" [sourced-secondary: S7] — i.e. management guides to flat conversion, not rising.
- **Invite mechanics:** albums are invite-only; "100 members, including Album Admins" per album [sourced-secondary: S48 help.family-album.com via search snippet; page returns 403]. Relatives per family: [unknown — never disclosed]. The one quantified loop datapoint: **"フォロワー課金" (follower billing) launched April 2025: "6月新規会員数のうち4.3%がフォロワーが課金"** — 4.3% of June-2025 new members were followers (non-admin family members in a premium subscriber's album) who paid; one subscription covers the whole album [sourced: S3 p.12]. FamilyAlbum's own FAQ: "Everyone invited views for free, and one person's Premium Family or Premium Family Pro subscription extends its benefits to the whole album" [sourced: S12]. This is the only hard number on relatives converting.
- **Multigenerational roadmap:** no "multigenerational" language. Strategy is life-stage extension via adjacent services: "GPSなどライフステージに連動したサービス拡張も重要な成長ドライバー" and "アルバム体験の深化と継続利用の促進" [sourced: S6]; target "グローバル売上高400億円、EBITDAマージン20%超" for みてね [sourced: S6 CFO section; S4 p.36 "Target scale: 40+ billion yen"]; "家族の『こころのインフラ』" [sourced: S6]. Q4 call: "we have started to disclose the number of comments and stickers posted in FamilyAlbum… The number of posts is increasing… steadily growing as a platform of communication among family members" — values not in the transcript [sourced-secondary: S7].
- **AI 2025–2026:** [unknown — no FamilyAlbum-specific AI feature release located]. Tried: (a) US App Store version history S15 — 12 releases Jun 8 → "1d ago" (v22.46.0 → v23.2.0); the only release note naming a feature is v23.0.0 (Oct 5, 2026) "New features/services: • Memories screen"; no note mentions AI or search; (b) blog.family-album.com/announcements index — 2025–2026 posts are only the 25M (2025-03-04), 10th-anniversary campaign (2025-08-01), 30M (2026-05-13) and 30M appreciation campaign (2026-07-31) posts [sourced: S49]; (c) S12 contains no AI sentence; (d) S6 says "1秒動画" and per-person albums use image analysis/face recognition since before generative AI, and AI is applied to dev, analytics and support [sourced: S6]; (e) a web search for FamilyAlbum AI features could not be run (per-turn search budget exhausted). A US Google Play review (Oct 2026) complaining an update "added AI photo search" was found in the prior round via a search snippet — single anonymous review, unverified, not treated as evidence. Company-wide: "AI utilization rate exceeded 99%, reducing monthly workloads by ~17,600 hours" [sourced-secondary: S7].
- **Ads:** introduced after ~10 years ad-free because "世界累計利用者数3,000万人超のユーザーに無料でサービスを提供し続けるためには、収益基盤の強化が不可欠" [sourced: S6 ad-business interview]; "We have included advertisements in our focus areas for FamilyAlbum this time" [sourced-secondary: S7].

### Q2. Tinybeans (ASX: TNY)

- **FY25 (to 30 Jun 2025):** revenue $4.82M (−11%); subscription $3.32M (+12%, 69%); gross margin 87% (89% FY24); opex $6.63M (−33%); adj. EBITDA −$1.44M; operating cash flow −$1.07M [sourced: S23 FY25 results ASX release, 2025-08-21, text-extracted]. Partnerships "raising brand awareness with high-value, target pre-natal audience by 25%" citing "Hello Baby List Receivers Survey, H2 FY25, sample size 247,500 expecting mothers" [sourced: S23 footnote 1]. "featured as Apple App Store 'App of the Day' in over 100+ countries" [sourced: S23].
- **Q3 FY26 (to 31 Mar 2026):** ~95k paid subs; Tinybeans 49,793 (Q2: 49,796 — flat) and Qeepsake 45,525 (Q2: 47,155) [sourced-secondary: Q3 FY26 investor presentation via search snippet; marketindex PDF returned 403]; Tinybeans ARPU $75 (Q2 $78), retention 95% (Q2 93%), CAC $19 (Q2 $100); **Qeepsake ARPU $64 (Q2 $77, −17% QoQ)**, retention 79% (Q2 77%), CAC $35 (Q2 $8); the company attributes the ARPU fall to "a spike in the prior quarter in e-commerce revenue" and says retention "improved by 2% for both platforms" [sourced: S25 investorpa Q3 FY26 PDF, 2026-04-28, text-extracted]. Cash $1.95M (A$2.81M), no debt, Q3 operating inflow $324k (vs $76k pcp), EBITDA +$8k [sourced: S25].
- **FY26 (to 30 Jun 2026):** revenue $6.49M (+35%); subscription $4.82M (+45%, ~74%); adj. EBITDA +$427k (vs −$1.44M); e-commerce $767k (+646%, iOS in-app photo store); cash $1.64M, no debt; "96% annual retention on Tinybeans+"; Q4 revenue ~$1.9M (+57%); Qeepsake "approximate 80% subscriber uplift on day one"; "serving ~95k paid subscribers and ~1 million active families worldwide" [sourced-secondary: S29 Medianet release relay 2026-08-27, re-verified; S30]. The prior draft's "~93,000 year-end subs" came from a kalkine.com.au summary that returns 403 (re-tried today) — **superseded by S29's ~95k**, the only readable FY26 figure; the two are consistent with a flat-to-slightly-down base vs Q3's ~95.3k [estimated: 49,793 + 45,525], and both are rounded vendor figures.
- **Churn derivation:** Tinybeans+ annual churn ≈ 4% [estimated: 1 − 0.96, S29]; Qeepsake ≈ 21% [estimated: 1 − 0.79, S25]. The 95%/79% quarterly "retention rate" in S25 and the 96% "annual retention" in S29 are not reconciled by the company (customers.md flag stands).
- **Cash runway:** not binding on current numbers: cash $1.64M (30 Jun 2026) with operating cash inflow in Q3 FY26 (+$324k) and the Q4 FY26 4C headline "third consecutive quarter of operating cash inflows" [sourced-secondary: S31 kalkine title, page 403]; at the FY25 burn rate (OCF −$1.07M/yr) runway would be ~18 months [estimated: 1.64 ÷ 1.07]. **New since the prior draft:** the ASX announcement list shows "Proposed issue of securities – TNY" dated 03/11/2026 (today), a "Quarterly Activities/Appendix 4C Cash Flow Report" dated 28/10/2026 (price-sensitive), "Appointment of Tracy Cho as Chief Executive Officer" 14/07/2026 (price-sensitive), "Head of Product Appointed to Drive Next Phase of Growth" 12/10/2026, and "Appendix 4E and Annual Report" 27/08/2026 [sourced: S50 ASX announcements list, 2026-11-03]. None of these PDFs is readable: the ASX links (idsId 03161443, 03158464, 03130887, 03114612) return the ASX terms-acceptance page; investors.tinybeans.com/announcements returns 404; tinybeans.com/investors lists no documents; the OTC Markets news API returned no JSON. So the **Q1 FY27 subscriber count, the purpose/size of the 3 Nov securities issue (it could be a placement or merely performance-rights issuance under the Qeepsake deal), and the FY26 annual-report cost lines are [unknown]**; today's −12.5% share move coincides with the 3 Nov notice [sourced-secondary: S32].
- **Qeepsake acquisition:** announced 2025-11-03, completed 2025-11-14; US$2.7M all-stock (20.2M shares ≈ $1.2M upfront + up to $1.5M performance rights); 0.66× Qeepsake FY25 revenue; ~49,000 paid subs added, Tinybeans "expects to retain about 40,000"; "effective cost per subscriber ~US$67" [sourced-secondary: S28 channellife / dealroom / marketscreener, Nov 2025; nasdaq.com primary release returned 503]. $2.7M ÷ 40,000 = $67.5 [estimated]. Qeepsake subs fell 49,000 → 45,525 by Mar 2026, −7% in ~4 months [estimated: 45,525 ÷ 49,000 − 1].
- **CEO on why Qeepsake churns:** "As you complete your baby book in the first or second year, you're more likely to churn"; Tinybeans is "harder to leave, as you have a built-in community" [sourced-secondary: S26 transcript, 2026-04-29].
- **Pivot statements:** FY25 deck: "Niche photo sharing" → "Multigenerational memory preservation", "Cross-generational access", "AI-powered photo management" [sourced: S24 FY25 results presentation, 2025-08-21, per customers.md]. Q3 FY26 call: "Tinybeans users want a collective family archive, a shared space where the whole family contributes"; "They need us through the broader parenting years and ultimately as a permanent family archive"; AI organisation "the number one feature parents tell us that they would pay for… Development has started" — no launch date [sourced-secondary: S26]. S25: Qeepsake extends engagement "beyond the 0–2 age range, directly improving subscriber retention and book creation rates" [sourced: S25].
- **Share price:** A$0.035 on 2026-11-03 (−12.5% on the day); 52-week range A$0.035–0.160; market cap A$7.33M; 1-year −69.57% [sourced-secondary: S32 investing.com, re-verified]. Longer-run decline: Simply Wall St snippet says 5-year ≈ −94% [sourced-secondary: S33 snippet, page 403, unverified]; the prior draft's "30 June 2021 close A$1.09 / −97%" was an unverified marketindex snippet with no check for consolidations or placements and is withdrawn — long-run drawdown is **[unknown beyond the −69.6% one-year figure]**.
- **What has not worked (in the company's own words or numbers):** "Our organic growth has stalled, and we're being honest about that" [sourced-secondary: S26]; Tinybeans core paid subs flat at ~49.8k Q2→Q3 FY26 [sourced-secondary: deck snippet]; FY25 total revenue fell 11% as ads collapsed [sourced: S23]; Qeepsake ARPU fell $77→$64 in the first full post-acquisition quarter and its subs fell ~7% [sourced: S25; estimated]; Qeepsake retention 79% vs Tinybeans 95% [sourced: S25]; 2024 price rise of ~87% to $74.99 [sourced-secondary: S13 FamilyAlbum blog citing Mi-3, 2026-07-26 — competitor source]; the Babylist affiliate partnership had an "initial term to December 2024… terminated by either party with 10 days notice" [sourced: S27 ASX release 2024-06-18, text-extracted] and is not mentioned in FY26 releases; a Tinybeans+ Legacy plan at $39.99/yr for "Reminiscing child 5+ years" [sourced: S24] is a 47% price cut for aged-out families [estimated: 1 − 39.99 ÷ 74.99]; a CEO change (July 2026) and a securities-issue notice (Nov 2026) within four months of the "maiden adjusted EBITDA profit" release [sourced: S50 titles only; contents unread].

### Q3. Other newborn-wedge apps

| App | Outcome | Evidence |
|---|---|---|
| Lifecake (Canon) | Closed 30 June 2020; two months' notice; zip export; one-tap migration to BackThen; pro-rata refunds | [sourced-secondary: S35 trove.photo 2026-08-14; S36 x.com/Lifecake status 2020-05-01 (closure announced "yesterday")]. Reason: not stated by Canon in sources read. |
| BackThen | Alive (built by Lifecake founders; US App Store id1505173822) | [sourced-secondary: S35; App Store listing exists] |
| 23snaps (UK, 2012, self-funded) | Alive but small; Google Play "Updated on Oct 23, 2026"; last reported users 500k (Nov 2013) | [sourced-secondary: S37 Wikipedia; S38 Google Play snippet] |
| Keepy (kids' artwork, 2014) | Status [unknown] — only 2014–2017 reviews found; no App Store page located | tried 2 searches + 1 URL guess (404) |
| Peekaboo Moments (Bithouse, China) | Jan 2020 breach exposed ~100GB incl. ~800,000 user emails, baby photos/videos; CEO unresponsive; current status [unknown] | [sourced-secondary: S40 bitdefender 2020-01] |
| Baby Pics (babypicsapp.com) | Alive; a pregnancy/baby-milestone **photo editor** (overlays, templates, collages), not a sharing/archive app; vendor claims "Loved by 5 million+ families", "#1 Photo app in 90+ countries", "30,000+" 5-star ratings; footer names Burleigh Creative (Turkish-registered entity; Play package "burleighlabs"); © 2026; pricing not on page | [sourced: S51 babypicsapp.com, 2026-11-03; vendor claims, unverified]. Not a competitor to the loop — it has no invite mechanic. |
| Kinzoo | Alive; pivoted to kids' messenger (Kinzoo Adventures retired 2023 → Kinzoo Studio) | [sourced-secondary: S41 kinzoo.com blog] |
| KinKeeper (family records/photos) | Discontinuing 1 May 2026, citing healthcare and economic environment | [sourced: S39 kinkeeper.app] |

Pattern: the newborn-wedge graveyard is mostly *corporate-owned* or *unfunded* apps; nothing in the sources explains Lifecake's closure beyond Canon's discretion. The apps that survived are the two with a subscription (Tinybeans) or a parent subsidy (MIXI), plus a one-off-purchase photo editor (Baby Pics) that never tried to be a system of record.

**Store metrics (fetched 2026-11-03):**

| App | US App Store ratings / avg | Google Play (US) installs / reviews / avg | US App Store latest version (date label on page) |
|---|---|---|---|
| FamilyAlbum | 380K / 4.9 [sourced: S15] | 10M+ / 367K / 4.8 [sourced: S18] | v23.2.0 "1d ago"; prior v23.1.0 Oct 19, v23.0.0 Oct 5 [sourced: S15] |
| Tinybeans | 104K / 4.9 [sourced: S16] | 500K+ / 4.99K / 3.7 [sourced: S19] | v5.93.0 "1d ago"; prior v5.92.1 Oct 15 [sourced: S16] |
| Qeepsake | 15K / 4.9 [sourced: S17] | 100K+ / 4.95K / 4.5 [sourced: S20] | v4.9.21 Sep 8; prior v4.9.20 Aug 4 [sourced: S17] |

(The prior draft's "Last update" column carried untagged dates of unknown origin; replaced with the App Store version labels above. FamilyAlbum ships roughly fortnightly — 12 releases Jun 8 → Nov 2 [sourced: S15]; Qeepsake has not shipped since Sep 8.)

FamilyAlbum has 3.7× Tinybeans' iOS rating count and ~20× its Android install band [estimated: 380K ÷ 104K; band ratio only].

### Q4. The invite mechanic, quantified (mostly it is not)

- Relatives invited per family, invite acceptance, time-to-second-member, grandparent DAU: **[unknown] for all three apps.** Searched MIXI JP/EN IR, press releases 2022–2026, Integrated Report, Tinybeans ASX releases and transcripts. MIXI names WAF (weekly active families) and photo-reaction counts as KPIs but publishes no values [sourced: S6].
- Only hard loop numbers: 4.3% of new members in June 2025 were paying followers [sourced: S3 p.12]; album cap 100 members [sourced-secondary: S48 snippet]; Tinybeans "acquires over 70% of its new subscribers in the third and 'fourth' trimesters of pregnancy" [sourced: S27, 2024-06-18]; Tinybeans "~1 million active families" vs ~95k paid → ~9.5% paid-per-active-family [estimated: 95k ÷ 1M; both vendor-claimed, S29].
- FamilyAlbum's own blog (2026-07-26), "drawn from more than 160 interviews conducted between 2024 and 2026", says of grandparents only that "Plenty of the grandparents we interviewed have signed up for and cancelled more subscriptions than most of us" — a remark that grandparents are experienced, subscription-savvy consumers, used to motivate a "no concrete value, no payment" product rule; it does **not** say grandparents cancel FamilyAlbum, nor how often [sourced: S12, re-read verbatim]. (The prior draft misrendered this; corrected here and in Q7.)
- **AARP "Powering Families: The Essential Role of Grandparents" (published 2026-06-16; n=3,283 grandparents, 2,962 online + 321 phone, fielded 2025-11-18 to 2025-12-22; 15 follow-up interviews Feb 2026):** "Three-quarters of grandparents (76%) say electronic technology" is a primary way they stay connected; "half (50%) of grandparents 80-plus text with their grandkids"; "about 65 million grandparents in America today… a decline from the roughly 70 million reported in AARP's 2018 Grandparents Survey"; average spend $2,654/yr on all grandchildren (vs $2,562 in 2018); 28% have lived with a grandchild, 11% currently do [sourced: S42, re-verified verbatim]. No photo-app-specific share.
- **AARP 2026 Tech Trends (50+; n=3,838, fielded 2025-09-09 to 2025-10-06):** smartphone ownership "55% in 2016 to 90% in 2025"; "Nine in 10 use social media"; average "10 different apps in a three-month period"; "top barrier to tech adoption overall remains data privacy" [sourced: S43]. No photo-sharing share.
- **Pew Mobile Fact Sheet (survey Jan 30–Jun 18, 2026; n=5,511):** smartphone ownership 65+: 79%; 14% of 65+ own a non-smartphone cellphone; 50–64: 91% [sourced: S44].

### Q5. Distribution and CAC

- **Tinybeans:** Babylist affiliate + sales partnership (2024-06-18): Babylist "helps over 9 million people" per year, "over 650,000 families registered… in 2023; 81% first-time parents"; promotion "across its large and engaged email database and registry feed, reaching hundreds of thousands of expecting and new parents per month"; revenue share on media; term to Dec 2024, 10-day termination [sourced: S27]. Bounty Bags (Australia) distribution [sourced: S23]. Apple App of the Day in 100+ countries [sourced: S23]. New channels Q3 FY26: "channels where Gen Z lives, TikTok, Reddit"; Peanut app collaboration [sourced-secondary: S26; S25]. Disclosed CAC: Tinybeans $100 (Q2 FY26) → $19 (Q3, "as marketing efficiency improved"); Qeepsake $8 → $35 "as marketing spend commenced post-Acquisition" [sourced: S25]. Hospital / pediatrician / What to Expect / The Bump / Pampers deals: none found [unknown after 2 searches in the prior round; no further search possible this round].
- **FamilyAlbum US:** first major US campaign, agency Familiar Creatures, 30-second hero spot "Running on socials now", published Jan 2025, describes the app as having "23 million subscribers" [sic — registrations] [sourced-secondary: S21 adsoftheworld]. No TV placement found. Instagram/TikTok parenting-creator programmes: [unknown — the blog announcements index (S49) lists no partnership or creator posts; S6 and S7 mention none; a dedicated search could not be run this round (budget exhausted)]. US PR: LA-wildfire free-reshipment offer, "Free Delivery Period: January 7, 2025 – January 6, 2026" [sourced: S52 FamilyAlbum blog post, 2025-01-16]; the BusinessWire version (S22, 2025-01-17) returns HTTP 403 on fetch and on direct retrieval, so its "over 25 million users" and "11 free photo prints up to 3 times per month" phrasing are **unverified this round** [sourced-secondary: S22, not re-readable]; the blog's own 25M milestone post is dated 2025-03-04 [sourced: S49]. Free-print hook, verified from the vendor: "you can get 8 free prints every month… any member of the album can get up to 8 free prints a month" (2022-06-27) [sourced: S53]; current US prints promotions: "up to 50% off photo prints" (30M campaign, 2026-07-31) [sourced: S49]. Japan Expo Paris exhibit (2026-06) [sourced: https://mixi.co.jp/en/news/2026/0609/52979/]. Babylist/hospital partnerships: none found. **CAC proxy:** Lifestyle ad spend ≈ ¥480–540 ($3.2–3.6) per net new registered individual [estimated above, Q1]; per paying subscriber [unknown] (subscriber count undisclosed). MIXI's stated doctrine is social spread over paid marketing [sourced: S6], and overseas acquisition investment is the stated reason Lifestyle EBITDA was negative through Q1 FY2026 [sourced: S3].

### Q6. Economics of free unlimited storage

- FamilyAlbum stores original + smartphone-optimised + S/M/L thumbnails; originals moved to S3 Standard-IA (Feb 2018) then "全面的に" to S3 Glacier Instant Retrieval (Mar 2022); smartphone-size video is no longer stored but generated on demand via HLS (Mar 2022), which "数PB削減" (cut several PB); Glacier IR savings made the HLS savings look small by comparison; no percentages or $ disclosed [sourced: S11 MIXI SRE talk 2023-06-07]. The company's phrase for the policy: "「無料・容量無制限でアップロード」を支える みてねのコスト削減術".
- Quality policy: free and Family tiers "re-encode your uploads at lower quality"; Family Pro caps at 1920×1080 [sourced-secondary: S45 memorymurals 2026-04-01; competitor-affiliated blog]. FamilyAlbum's own blog: "individual videos cap at two minutes on the free plan"; comparison table "Max video length 10 min" for Premium Family and Pro; "higher-quality video" is a Pro feature [sourced: S12, re-verified]. Free plan compresses: consistent across S45 and a keeprcircle review [sourced-secondary: search snippet].
- **Segment cost structure (partial):** S3 p.30 discloses Lifestyle 外注費（原価） (outsourcing cost within cost of sales, ¥M): FY2024 598/595/2,674/1,051 (sum ¥4,918M = 36.7% of sales); FY2025 538/633/2,113/958 (sum ¥4,242M = 28.7%); FY2026 Q1 569 (16.2% of Q1 sales) [sourced: S3 p.30; estimated: sums ÷ S3 p.11 sales]. The Q3 spike each year is New Year-card/print fulfilment. Because outsourcing is only one COGS component (hosting is not broken out), this gives a **ceiling, not a value**: Lifestyle gross margin ≤ ~71% in FY2025 and ≤ ~84% in Q1 FY2026 [estimated: 1 − 外注費 ÷ sales]; the true figure, and FamilyAlbum's storage cost, are [unknown — not disclosed in S3, S4, S5, S6]. For comparison Tinybeans, which caps free storage, reports 87% [sourced: S23].
- Who pays for it: Lifestyle segment profit (EBITDA) was negative in FY2024 (−¥682M [estimated: −374−308+747−747, S3 p.11]) and FY2025 (−¥128M [sourced: S5]; quarterly −301/−211/+1,008/−623 [sourced: S3 p.11]) and turned positive only in FY2026 (+¥876M) [sourced: S5]; years before FY2024 are not shown in any document read. MIXI "has redistributed profits generated by Digital Entertainment to next growth areas such as Sports and Lifestyle" [sourced: S6 CFO]. Ads were added explicitly to fund free users [sourced: S6]. Segment profit margin FY2026 5.1% [estimated: 876 ÷ 17,159]; target >20% at ¥40B [sourced: S6].
- Tinybeans: gross margin 87% (FY25), 89% (FY24) [sourced: S23]; hosting cost line [unknown — not in the FY25 results release S23 (the only FY25 document cached; the file named "annual report" locally is S23); the FY26 Appendix 4E/Annual Report (ASX, 27/08/2026, idsId 03130887) is gated behind the ASX terms page]; free tier is 5GB (~1,200 photos) vs 200GB–1TB paid [sourced: S24 FY25 deck p.(plans slide)] and "20 uploads per month" [sourced-secondary: S45] — storage is capped, not subsidised.
- **Implication for an entrant with index-only economics:** it cannot match "free, unlimited, originals kept" without a subsidising parent; MIXI needed two storage-class migrations over the 7 years from the 2015 launch to the 2022 Glacier/HLS move [estimated: 2022 − 2015; S2, S11] and still needed ads. An index-only product stores embeddings/thumbnails, not originals, so its unit COGS is inference + metadata — structurally cheaper per family but it *cannot be the system of record*, which is exactly the thing grandparents are invited into. The loop therefore has to be bought with a different hook (search/consolidation across the parents' existing libraries) rather than with storage.

### Q7. Falsification

**Evidence the newborn wedge does NOT extend to an archive:**
- Qeepsake retention 79% vs Tinybeans 95%, with the CEO's causal statement that finishing the baby book triggers churn [sourced: S25; sourced-secondary: S26]. Qeepsake lost ~7% of subs and 17% of ARPU in the first four months post-acquisition [estimated above; S25].
- Tinybeans built a cheaper "Legacy" tier for child 5+ [sourced: S24] — a price signal that willingness to pay falls as children age; Tinybeans core paid subs flat at ~49.8k across Q2–Q3 FY26 [sourced-secondary: deck snippet]; "organic growth has stalled" [sourced-secondary: S26]; TNY −69.6% over one year [sourced-secondary: S32]; CEO change and securities-issue notice within four months of the maiden-profit release [sourced: S50 titles].
- FamilyAlbum's MAU/registered ratio is 40% [estimated]; its positioning is explicitly "the app they use when their children are born" [sourced: S2]; growth of the economic sphere comes from GPS trackers, prints, stickers and ads — life-stage adjacency, not archive [sourced: S4 p.16; S6]. Management guides FY2027 to "maintain" paying rate [sourced: S5]. Competitor blog argues daily-feed cadence "starts to feel like a chore" after school age and older kids object to being posted — opinion, no data [sourced-secondary: S45].
- MIXI uses "multigenerational" nowhere; its archive language is "look back on their albums" [sourced: S2] and "家族の『こころのインフラ』" [sourced: S6] — retention through emotion, not through consolidation of legacy photos.
- Counter-evidence (for the wedge extending): Tinybeans+ "96% annual retention" FY26 [sourced-secondary: S29] and a user email on the Q3 call about an 11-year-old adding her own photos [sourced-secondary: S26]; FamilyAlbum, 11 years after launch [estimated: 2026 − 2015, S2], is still adding registrations at ~3.6M/yr [estimated: 27M Jul 2025 → 30M May 2026 = 3M in 10 months, annualised]. Note the retention KPI reconciliation problem flagged in customers.md still stands (quarterly vs annual definitions).

**Evidence grandparents refuse apps:** weak. Pew: 79% of 65+ own smartphones (2026) [sourced: S44]; AARP: 90% of 50+ (2025), 10 apps used per quarter, social media 90% [sourced: S43]; AARP grandparents: 76% use electronic technology as a primary connection channel, 50% of 80+ text [sourced: S42]. Residual friction is real but narrow: 14% of 65+ are on basic phones [sourced: S44]; privacy is the top adoption barrier [sourced: S43]; FamilyAlbum's own user research characterises grandparents as experienced subscription cancellers *in general* ("signed up for and cancelled more subscriptions than most of us") — i.e. price-sensitive and willing to churn, not app-averse — and the product answer was to never charge them [sourced: S12]; one review claims relatives must install the app [sourced-secondary: S45] while FamilyAlbum's own comparison page says grandparents can "view through a browser without an account" [sourced: S13] — conflict; FamilyAlbum's statement is from the vendor and more recent. **Net: no evidence that grandparents refuse apps; the evidence is that they refuse to *pay* for them, which is why both incumbents make the parent the single payer.**

---

## 3. Mechanism table

| App | Users | Paid | Price | Invite-loop metrics | Storage policy | Revenue |
|---|---|---|---|---|---|---|
| FamilyAlbum (MIXI) | 30M registered individuals (2026-05-07); 12M MAU (May 2026); >40% overseas, 20% N. America; 65% of Japanese new parents [sourced: S1/S2; S7] | [unknown]; Premium+GPS sales ×1.5 YoY Q1 FY2026 [sourced: S3]; 4.3% of Jun-2025 new members paid as followers [sourced: S3 p.12] | US $2.99 / $5.99 ($59/yr) / $10.99 ($109/yr) / stickers $3.99; UK £2.99 / £5.49 (£54.99) / £10.49 (£104.99); DE & FR €2,99 / €5,49 (€54,99) / €10,49 (€104,99); JP ¥590 / ¥1,090 [sourced: S15, S15-GB/DE/FR; sourced-secondary: S47] | 100 members/album [sourced-secondary: S48]; relatives/family, acceptance, grandparent DAU [unknown]; KPIs tracked: WAF, photo reactions, comments & stickers posted (values undisclosed) [sourced: S6; S7] | Free unlimited uploads; free re-encoded, 2-min video cap; originals in S3 Glacier IR; HLS on-demand video [sourced: S2; S12; S11] | Lifestyle ¥17,159M FY2026 (+16%), profit ¥876M [sourced: S5]; ad spend ¥1,938M FY2025 (13.1% of sales) [sourced: S3 p.30]; FamilyAlbum share [unknown]; target ¥40B, >20% EBITDA [sourced: S6] |
| Tinybeans | "~1M active families" (claimed) [sourced-secondary: S29]; 0.86M MAU FY25 [sourced: S24] | ~95k (Q3 FY26: 49,793 TB + 45,525 QS; FY26 release "~95k") [sourced-secondary: deck snippet; S29] | Tinybeans+ $7.99/mo or $74.99/yr; Legacy $4.49/mo or $39.99/yr [sourced: S16 US App Store IAP list]; a $119.99 Family tier appears only in the FY25 deck [sourced: S24], not on the current US storefront | >70% of new subs acquired in 3rd/"4th" trimester [sourced: S27]; relatives/family [unknown]; email digest for non-installing relatives [sourced-secondary: S45] | Free 5GB / 20 uploads per month; 200GB–1TB paid [sourced: S24; S45] | FY26 $6.49M; subs $4.82M; adj. EBITDA +$427k; cash $1.64M [sourced-secondary: S29]; GM 87% FY25 [sourced: S23] |
| Qeepsake (Tinybeans since Nov 2025) | 100K+ Android installs [sourced: S20] | 45,525 (Mar 2026) from ~49,000 at deal [sourced-secondary: deck snippet; S28] | $4.99/mo Essential, $9.99/mo Premium; $47.99 / $95.99 per year; Plus $35.99 [sourced: S17] | SMS-prompt journal; spouse/contributors sharing; churn after baby book done [sourced: S17; S26] | journal + photos; book printing | ARPU $64 (Q2 $77); retention 79%; CAC $35 [sourced: S25]; bought at 0.66× revenue → FY25 revenue ≈ $4.1M [estimated: 2.7 ÷ 0.66] |
| Lifecake / 23snaps / Keepy / Peekaboo / Baby Pics | see Q3 | — | — | — | — | Lifecake closed 2020; 23snaps alive, tiny; Baby Pics alive (editor, vendor-claimed 5M+ families); others [unknown] |

## 4. Scenario — entrant with index-only economics reaching $100M ARR via the loop

Assumptions are labelled; vary them in a spreadsheet, not in prose.

1. Price: $60/yr per paying family [estimated: assumption anchored on FamilyAlbum Premium Family $59/yr (S15) and Tinybeans+ $74.99 (S16)]. Paying families needed = $100M ÷ $60 = **1.67M** [estimated]; at $75: 1.33M; at $109: 0.92M.
2. Paid conversion of active families: Tinybeans ≈ 9.5% [estimated above, vendor inputs]; FamilyAlbum [unknown]. At 10%, active families needed = **16.7M** [estimated: 1.67M ÷ 0.10] — more than FamilyAlbum's entire 12M MAU (individuals, not families) after 11 years [estimated: 2026 − 2015]. At 25% (no operator has disclosed this), 6.7M.
3. Cohort arithmetic: US births 2024 = 3,628,934 [sourced: S54 CDC NCHS "Births: Final Data for 2024", 2026-06-09; the same count appears as the 2024 provisional denominator in NCHS VSRR No. 41, Dec 2025]. If the entrant matched FamilyAlbum's Japan penetration (65% of births [sourced: S2]) in the US, it would add ≈2.36M families/yr [estimated: 3.629M × 0.65]; five cohorts ≈ 11.8M families → at 10% paid ≈ 1.18M paying ≈ $71M [estimated: × $60]. **$100M therefore requires at least two of: >10% paid conversion, >$60 price, multi-country rollout, or paid relatives (follower billing).** MIXI's own route to ¥40B (~$267M [estimated: ÷150]) is an "economic sphere" (GPS, prints, ads), not subscriptions alone.
4. Invite loop contribution: with k accepted relatives per family and FamilyAlbum's 4.3% follower-pay rate [sourced: S3], paying relatives per family = 0.043·k. At k=3 [estimated: assumption; no disclosure exists], that is +0.13 paying units per family, i.e. ~+13% revenue uplift at equal price — helpful, not decisive. At Tinybeans-style single-payer albums, k affects retention (the "built-in community" that makes it "harder to leave" [S26]) rather than revenue.
5. Retention/acquisition: steady-state paying base S = gross paid adds G ÷ annual churn c. For S=1.67M: c=4% (Tinybeans+ 96% annual retention [sourced-secondary: S29]) → G=67k/yr; c=21% (Qeepsake 79% [sourced: S25]) → G=350k/yr; c=40% [estimated: **assumption** for an age-out cohort — no operator discloses churn at child age 5+; the only signals are Tinybeans' 47% Legacy price cut and Qeepsake's baby-book churn] → G=667k/yr [estimated: S × c]. At CAC $35–$100 per paid sub [sourced: S25 range] that is $2.3M–$67M/yr of acquisition spend [estimated: G × CAC]; at FamilyAlbum-style social spread the disclosed cost is ~$3.2–3.6 of ad spend per registered individual [estimated above] but the segment ran at a loss in FY2024–FY2025 [sourced: S3; S5].
6. Unit COGS: index-only avoids the Glacier/HLS problem (no originals), so gross margin should sit at or above Tinybeans' 87% [sourced: S23] — but the entrant then cannot offer the "we keep everything forever for free" promise that drives FamilyAlbum's 65% penetration. The wedge must instead be the parents' *existing* iCloud/Google libraries (the consolidation problem in customers.md), with the grandparent invite as a retention and secondary-payer mechanic.

Verdict for the round-2 variant: the loop is a credible acquisition engine (FamilyAlbum proves nationwide penetration is achievable; Tinybeans proves >70% of signups come pre-birth and that Babylist-type registries can be rented), but no disclosed number supports relatives-per-family, grandparent conversion beyond 4.3%, or archive-stage retention. The honest base case for an index-only entrant on this loop alone is Tinybeans-shaped — roughly $5–10M revenue [estimated: Tinybeans FY26 $6.49M (S29) and Qeepsake FY25 ≈ $4.1M (estimated) bracket the size two decade-old operators of this loop reached] — not $100M; $100M needs the consolidation wedge plus multi-country plus adjacent revenue.

---

## 5. Numbers table (every number, its tag)

| # | Number | Tag |
|---|---|---|
| 1 | FamilyAlbum 30M registered (individuals), 2026-05-07; launched April 2015 | [sourced: S1, S2] |
| 2 | 15M (2022-08-14); 25M (Jan 2025); 27M (Jul 2025) | [sourced: S10; S3 p.37; S1] |
| 3 | MAU 12M (May 2026) | [sourced-secondary: S7; mixi.co.jp/en/ir/message/ via customers.md] |
| 4 | MAU/registered 40%; registration run-rate 3.6M/yr (Jul 2025→May 2026), 4.0M/yr (Jan→Jul 2025); 11 years old | [estimated: 12 ÷ 30; 3M ÷ 10 × 12; 2M ÷ 6 × 12; 2026 − 2015] |
| 5 | 65% of Japanese parents (Dec 2024); 47.1% (Aug 2022) | [sourced: S2; S10] |
| 6 | Overseas >40% (May 2026); 41.5% (Jun 2025); N. America ~20%; NA ≈ half of overseas (2022) | [sourced: S2; S3 p.37; S10] |
| 7 | Lifestyle FY2026 sales ¥17,159M (+16.0% from ¥14,795M), profit ¥876M (prior −¥128M) | [sourced: S5 p.2] |
| 8 | Lifestyle margin 5.1% | [estimated: 876 ÷ 17,159] |
| 9 | Lifestyle quarterly sales FY2024 2,421/2,129/6,131/2,736; FY2025 2,736/2,719/5,942/3,397; Q1 FY2026 3,505; segment profit (EBITDA) FY2024 −374/−308/+747/−747; FY2025 −301/−211/+1,008/−623; Q1 FY2026 −69 (¥M) | [sourced: S3 p.11] |
| 9a | FY2024 Lifestyle sales ¥13,417M, profit −¥682M | [estimated: sums of row 9] |
| 10 | Q2 FY2026 ≈ ¥3.5B (+32%), first quarterly EBITDA profit; FamilyAlbum +36.9% | [sourced-secondary: S8] |
| 11 | Q3 FY2026 ¥5,598M (−5.8%), EBITDA ¥1,079M (+7.0%) | [sourced-secondary: S9] |
| 12 | Q4 FY2026 ¥4.4B (+31.4%); focus areas +37.5%; Lifestyle "5-year CAGR of 20%" | [sourced-secondary: S7, verbatim 2026-05-18] |
| 13 | FamilyAlbum sales +37.1% Q1 FY2026; Premium+GPS ×1.5 | [sourced: S3 p.12] |
| 14 | 4.3% of June-2025 new members = paying followers | [sourced: S3 p.12] |
| 15 | Album cap 100 members | [sourced-secondary: S48 snippet; 403] |
| 16 | US prices $2.99 / $5.99 ($59) / $10.99 ($109) / stickers $3.99 | [sourced: S15] |
| 16a | UK £2.99 / £5.49 (£54.99) / £10.49 (£104.99); DE/FR €2,99 / €5,49 (€54,99) / €10,49 (€104,99) | [sourced: S15-GB; S15-DE; S15-FR] |
| 16b | Storefront ratings: GB 59k/4.8; DE 22,175/4.7; FR 51k/4.8 | [sourced: S15-GB; S15-DE; S15-FR] |
| 17 | JP ¥590 / ¥1,090 per month | [sourced-secondary: S47] |
| 18 | みてね target ¥40B sales, >20% EBITDA (~¥8B) | [sourced: S6; S4 p.36] |
| 19 | ¥40B ≈ $267M; ¥17,159M ≈ $114M | [estimated: ÷ ¥150/$ assumed] |
| 20 | MIXI consolidated ad spend FY2026 ¥27,387M (+54.5%) | [sourced-secondary: S46; not segment] |
| 20a | Lifestyle 広告宣伝費 (¥M): FY2024 358/279/940/462; FY2025 445/378/533/582; Q1 FY2026 485; consolidated FY2025 3,325/4,831/4,892/4,679, Q1 FY2026 4,181 | [sourced: S3 p.30] |
| 20b | Lifestyle ad spend FY2024 ¥2,039M (15.2% of sales); FY2025 ¥1,938M (13.1%); Q1 FY2026 13.8% | [estimated: sums ÷ rows 7, 9, 9a] |
| 20c | Ad spend per net new registered individual ¥480–540 ≈ $3.2–3.6 | [estimated: ¥1,938M ÷ 3.6–4.0M/yr; ÷150] |
| 20d | Lifestyle 外注費（原価） (¥M): FY2024 598/595/2,674/1,051 (¥4,918M, 36.7%); FY2025 538/633/2,113/958 (¥4,242M, 28.7%); Q1 FY2026 569 (16.2%) | [sourced: S3 p.30; estimated: ÷ sales] |
| 20e | Lifestyle gross margin ceiling ≤71% FY2025, ≤84% Q1 FY2026 | [estimated: 1 − 外注費 ÷ sales; true GM unknown] |
| 20f | Lifestyle headcount 207 (Q1 FY2024) → 279 (Q1 FY2026) | [sourced: S3 p.33] |
| 21 | FY2027 Lifestyle guidance: sales growth, "maintain paying rate" / "stable monetization rate", large profit increase | [sourced: S5 p.3; sourced-secondary: S7] |
| 22 | Company-wide AI utilisation >99%, ~17,600 hours/month saved | [sourced-secondary: S7] |
| 23 | S3 Standard-IA Feb 2018; Glacier IR Mar 2022; HLS Mar 2022 cut "several PB"; 7 years launch→Glacier | [sourced: S11; estimated: 2022 − 2015] |
| 24 | Free: 2-min video; Premium/Pro: 10-min; free re-encoded; Pro 1080p cap | [sourced: S12; sourced-secondary: S45] |
| 25 | 8 free prints per month, any album member (2022-06-27); "11 free prints up to 3×/month" (2025) | [sourced: S53]; [sourced-secondary: S22, 403 — unverified] |
| 26 | US campaign Jan 2025, social only, "23 million" cited | [sourced-secondary: S21] |
| 27 | 25M users: blog milestone post 2025-03-04; BusinessWire "over 25 million" 2025-01-17 | [sourced: S49]; [sourced-secondary: S22, 403 — unverified] |
| 27a | "more than 160 interviews conducted between 2024 and 2026" | [sourced: S12] |
| 28 | App Store: FamilyAlbum 380K/4.9; Tinybeans 104K/4.9; Qeepsake 15K/4.9 | [sourced: S15; S16; S17] |
| 28a | Latest versions: FamilyAlbum v23.2.0 "1d ago" (12 releases Jun 8–Nov 2); Tinybeans v5.93.0 "1d ago"; Qeepsake v4.9.21 Sep 8 | [sourced: S15; S16; S17] |
| 29 | Google Play: 10M+/367K/4.8; 500K+/4.99K/3.7; 100K+/4.95K/4.5 | [sourced: S18; S19; S20] |
| 30 | Tinybeans FY25: rev $4.82M (−11%); subs $3.32M (+12%, 69%); GM 87% (89%); opex $6.63M (−33%); adj. EBITDA −$1.44M; OCF −$1.07M | [sourced: S23] |
| 31 | Awareness +25% ("Hello Baby List Receivers Survey", n=247,500) | [sourced: S23 fn1; vendor survey] |
| 32 | >70% of new subs in 3rd/4th trimester; Babylist 9M people/yr, 650k registrants 2023, 81% first-time; term to Dec 2024, 10-day exit | [sourced: S27] |
| 33 | Q3 FY26: 49,793 + 45,525 subs (Q2 49,796 / 47,155); ARPU $75 (Q2 $78) / $64 (Q2 $77); retention 95% (93%) / 79% (77%); CAC $19 ($100) / $35 ($8); cash $1.95M (A$2.81M); OCF +$324k (pcp $76k); EBITDA +$8k | [sourced: S25; sourced-secondary: deck snippet for sub split] |
| 34 | Qeepsake: $2.7M all-stock; 20.2M shares; $1.2M upfront + $1.5M rights; 0.66× revenue; ~49k subs; retain ~40k; ~$67/sub | [sourced-secondary: S28, Nov 2025] |
| 35 | Qeepsake FY25 revenue ≈ $4.1M; subs −7% in 4 months; ARPU −17% QoQ; $67.5/retained sub | [estimated: 2.7 ÷ 0.66; 45,525 ÷ 49,000; 64 ÷ 77; 2.7M ÷ 40k] |
| 36 | FY26: rev $6.49M (+35%); subs $4.82M (+45%, 74%); adj. EBITDA +$427k; e-com $767k (+646%); cash $1.64M; 96% annual retention; Q4 ~$1.9M (+57%); ~95k paid subs; ~1M active families; Qeepsake ~80% day-one uplift | [sourced-secondary: S29 re-verified; S30] |
| 36a | Annual churn ≈ 4% (Tinybeans+), ≈ 21% (Qeepsake); runway at FY25 burn ≈ 18 months | [estimated: 1 − 0.96; 1 − 0.79; 1.64 ÷ 1.07] |
| 37 | ~93k paid subs Q4 FY26 (prior draft) | withdrawn — kalkine 403; superseded by row 36's ~95k |
| 38 | TNY A$0.035 (2026-11-03, −12.50%); 52-wk 0.035–0.160; cap A$7.33M; 1-yr −69.57% | [sourced-secondary: S32] |
| 38a | 5-year ≈ −94% | [sourced-secondary: S33 snippet, 403, unverified]; mid-2021 anchor withdrawn → [unknown] |
| 38b | ASX filings: 4C 28/10/2026; Proposed issue of securities 03/11/2026; CEO appointment 14/07/2026; Annual Report 27/08/2026 | [sourced: S50 titles/dates only; contents gated] |
| 39 | Legacy plan $39.99/yr or $4.49/mo = −47% vs $74.99; Tinybeans+ $7.99/mo | [sourced: S16; S24; estimated] |
| 40 | Tinybeans paid/active families ≈ 9.5% | [estimated: 95k ÷ 1M; vendor-claimed inputs] |
| 41 | Lifecake closed 2020-06-30; 2 months' notice; 23snaps 500k users (2013), Play updated Oct 2026; Peekaboo breach ~800k emails/100GB (Jan 2020); KinKeeper ends 2026-05-01 | [sourced-secondary: S35; S36; S37; S38; S40]; [sourced: S39] |
| 41a | Baby Pics: "5 million+ families", "#1 in 90+ countries", "30,000+" 5-star ratings | [sourced: S51; vendor claims] |
| 42 | AARP grandparents: n=3,283 (2,962 online + 321 phone); 76% tech primary; 50% of 80+ text; ~65M grandparents vs ~70M (2018); $2,654/yr (vs $2,562 in 2018); 28% ever co-resided, 11% now | [sourced: S42, re-verified] |
| 43 | AARP 50+: smartphone 90% (2025); 10 apps/quarter; 90% social media; n=3,838 | [sourced: S43] |
| 44 | Pew 2026: 65+ smartphone 79%; 14% basic phone; 50–64 91%; n=5,511 | [sourced: S44] |
| 44a | US births 2024: 3,628,934 | [sourced: S54 CDC NCHS, 2026-06-09] |
| 45 | Scenario: 1.67M paying @ $60; 16.7M active @10%; 2.36M families/yr @65% of 3.629M; 11.8M over 5 cohorts → 1.18M paying → $71M; +13% from followers at k=3; G = 67k–667k/yr; spend $2.3M–$67M; c=40% is an assumption | [estimated: methods in §4] |
| 46 | Base case "$5–10M" | [estimated: bracketed by Tinybeans FY26 $6.49M and Qeepsake FY25 ≈ $4.1M] |

## 6. Unknowns and what was tried

1. FamilyAlbum Premium subscriber count, premium vs prints revenue split, FamilyAlbum-only revenue — not in earnings summary, Q1 deck, intro deck, Integrated Report or transcripts; Q3/Q4 FY2026 decks not locatable (IR lists dynamic; irpocket paths unguessable; 3 searches). S4 scanned in full for reposted Q4 KPI slides: only capital-allocation pages are reposted.
2. Relatives per family, invite acceptance, time-to-second-member, grandparent DAU/MAU — nowhere disclosed by MIXI or Tinybeans (JP + EN searches, 2022–2026 releases, Integrated Report).
3. FamilyAlbum CAC per paying subscriber — subscriber count undisclosed; segment ad spend now sourced (S3 p.30) and converted to cost per registration only.
4. FamilyAlbum per-country *user* splits for UK/DE/FR — not disclosed (prices now sourced from the GB/DE/FR storefronts).
5. Comments/stickers counts (first disclosed in Q4 FY2026 briefing) and WAF values — deck unread; S7 transcript confirms disclosure but gives no values.
6. FamilyAlbum 2025–2026 AI feature releases — App Store release notes (12 versions), blog announcements index and S6/S12 checked; nothing found; search budget exhausted before a dedicated web search could run.
7. Tinybeans FY26 annual report (hosting cost line, 30 Jun 2026 subscriber count), Q1 FY27 4C (28/10/2026), 3 Nov 2026 securities-issue notice, July 2026 CEO release — all listed on ASX (S50) but every PDF route tried returned the ASX terms page, 404 (investors.tinybeans.com/announcements), an empty page (tinybeans.com/investors) or no JSON (OTC API); marketindex/listcorp/kalkine 403.
8. Keepy, Peekaboo Moments current status; Lifecake's stated reason for closure. (Baby Pics now identified — S51.)
9. Hospital/pediatrician/What-to-Expect/The Bump placements and Instagram/TikTok creator programmes for FamilyAlbum — none found in S6, S7, S21, S49; no search possible this round.
10. Grandparent-specific photo-app usage share (AARP/Pew give device and "technology" shares only).
11. Tinybeans long-run share-price drawdown with corporate actions adjusted — only snippet-level figures; withdrawn.
12. BusinessWire S22 wording ("over 25 million users", "11 free prints up to 3 times per month") — 403 on two fetch routes; the vendor blog gives the 2022 "8 free prints" offer and the 2025-03-04 25M milestone instead.

## 7. Source list (accessed 2026-11-03)

- S1 https://mixi.co.jp/news/2026/0507/51754/ — 30M users release (JP), 2026-05-07
- S2 https://pdf.irpocket.com/C2121/Kdx3/R43P/MfKg.pdf — 30M users release (EN), 2026-05-07 (text-extracted)
- S3 https://pdf.irpocket.com/C2121/CiMB/e1pB/f3rw.pdf — MIXI FY2026 Q1 決算説明資料, 2025-07-31 (text-extracted; p.11 segment P&L, p.30 cost breakdown, p.33 headcount, p.37 users)
- S4 https://pdf.irpocket.com/C2121/WvLb/Uhks/uhEe.pdf — Introductory Materials for Investors, 2026-06-26 (text-extracted)
- S5 https://pdf.irpocket.com/C2121/WUpy/xRhD/Awzj.pdf — 2026年3月期 決算短信, 2026-05-15 (text-extracted)
- S6 https://pdf.irpocket.com/C2121/xoA3/M9fy/XXs9/KyVH.pdf — MIXI Integrated Report 2026 (pypdf-extracted; 11.5 MB, exceeds fetch-tool limit)
- S7 https://www.investing.com/news/transcripts/earnings-call-transcript-mixi-q4-2026-earnings-beat-expectations-stock-dips-93CH-4696203 — Q4 FY2026 call, 2026-05-18 (secondary; re-read this round)
- S8 https://www.investing.com/news/transcripts/earnings-call-transcript-mixi-q2-2025-sees-stock-dip-postearnings-93CH-4390150 — Q2 FY2026 call, 2025-12-04 (secondary)
- S9 https://www.investing.com/news/company-news/mixi-q3-fy2026-slides-sports-segment-doubles-overall-revenue-up-18-93CH-4490901 — Q3 FY2026 slides summary, 2026-02-06 (secondary)
- S10 https://mixi.co.jp/news/2022/0826/12672/ — 15M users release, 2022-08-26
- S11 https://speakerdeck.com/mixi_engineers/aws-cost-reduction-method-to-support-free-and-unlimited-uploading-in-mitene-family-album — MIXI SRE talk, 2023-06-07
- S12 https://blog.family-album.com/blog/is-familyalbum-really-free-what-you-get-without-paying/ — 2026-07-26 (re-read verbatim this round)
- S13 https://blog.family-album.com/blog/familyalbum-vs-tinybeans-which-is-better-after-the-price-hike/ — 2026-07-26
- S14 https://blog.family-album.com/announcements/weve-surpassed-30-million-users-worldwide/ — 2026-05-13
- S15 https://apps.apple.com/us/app/familyalbum-photo-sharing/id935672069 (re-fetched: IAP list, version history)
- S15-GB https://apps.apple.com/gb/app/familyalbum-photo-sharing/id935672069 ; S15-DE https://apps.apple.com/de/app/familyalbum-photo-sharing/id935672069 ; S15-FR https://apps.apple.com/fr/app/familyalbum-photo-sharing/id935672069
- S16 https://apps.apple.com/us/app/tinybeans-private-family-album/id521633042 (re-fetched: IAP $7.99 / $74.99 / $39.99 / $4.49; v5.93.0)
- S17 https://apps.apple.com/us/app/qeepsake-family-photo-album/id1332312787 (re-fetched: v4.9.21 Sep 8)
- S18 https://play.google.com/store/apps/details?id=us.mitene&hl=en_US&gl=US (curl, prior round)
- S19 https://play.google.com/store/apps/details?id=com.tinybeans&hl=en_US&gl=US (curl, prior round)
- S20 https://play.google.com/store/apps/details?id=co.qeepsake.qeepsakeApp&hl=en_US&gl=US (curl, prior round)
- S21 https://www.adsoftheworld.com/campaigns/family-oriented — Jan 2025 (secondary)
- S22 https://www.businesswire.com/news/home/20250117710848/en/FamilyAlbum-by-MIXI-Support-for-Those-Affected-by-the-LA-Wildfires — 2025-01-17 (HTTP 403 on WebFetch; direct retrieval blocked; unverified this round)
- S23 https://announcements.asx.com.au/asxpdf/20250821/pdf/06n4k9jtxswjxy.pdf — Tinybeans FY25 results release, 2025-08-21 (text-extracted; this is the results release, not the statutory annual report)
- S24 https://announcements.asx.com.au/asxpdf/20250821/pdf/06n4m9jjp1zr87.pdf — FY25 results presentation (read in customers.md)
- S25 https://investorpa.com/announcement-pdf/20260428/285467.pdf — Q3 FY26 quarterly, 2026-04-28 (text-extracted; re-read for ARPU/retention/CAC rows)
- S26 https://www.investing.com/news/transcripts/earnings-call-transcript-tinybeans-group-q3-2026-sees-first-ebitda-profit-93CH-4647546 — 2026-04-29 (secondary)
- S27 https://www.otcmarkets.com/news-otcapi/news/document/content/id?id=75396 — Babylist partnership ASX release, 2024-06-18 (text-extracted)
- S28 https://channellife.com.au/story/tinybeans-to-acquire-qeepsake-for-usd-2-7m-doubling-subscribers ; https://app.dealroom.co/news/feed/tinybeans-acquires-qeepsake-for-4m ; https://www.marketscreener.com/news/tinybeans-group-limited-completed-the-acquisition-of-assets-of-qeepsake-inc-ce7d5fd2dd81ff27 — Nov 2025 (secondary; nasdaq.com primary 503)
- S29 https://newshub.medianet.com.au/2026/08/tinybeans-asxtny-posts-maiden-adjusted-ebitda-profit-in-fy26/168355/ — 2026-08-27 (release relay; re-verified incl. "~95k paid subscribers")
- S30 https://www.australiabankingtimes.com/article/937416546-tinybeans-reports-first-adjusted-ebitda-profit-as-fy26-revenue-climbs-35 — 2026-08-26 (secondary)
- S31 https://kalkine.com.au/news/announcements/tinybeans-reports-record-e-commerce-growth-and-third-consecutive-quarter-of-operating-cash-inflows — Jul 2026 (403 twice; title only)
- S32 https://www.investing.com/equities/tinybeans-group-ltd — 2026-11-03
- S33 https://simplywall.st/stocks/au/media/asx-tny/tinybeans-group-shares (403; snippet) ; https://www.marketindex.com.au/asx/TNY (403; snippet; 2021 price withdrawn)
- S35 https://trove.photo/blog/lifecake-alternatives — 2026-08-14 (secondary)
- S36 https://x.com/Lifecake/status/1256276372504236033 — 2020-05-01 (snippet)
- S37 https://en.wikipedia.org/wiki/23snaps
- S38 https://play.google.com/store/apps/details?id=com.snaps23.android&hl=en_US (snippet)
- S39 https://www.kinkeeper.app/ — shutdown notice
- S40 https://www.bitdefender.com/en-us/blog/hotforsecurity/peekaboo-moments-app-left-baby-videos-photos-and-800000-users-email-addresses-exposed-on-the-internet — Jan 2020
- S41 https://www.kinzoo.com/blog/kinzoo-launches-kinzoo-studio-retires-kinzoo-adventures
- S42 https://www.aarp.org/pri/topics/social-leisure/relationships/the-essential-role-of-grandparents/ — 2026-06-16 (re-verified verbatim)
- S43 https://www.aarp.org/pri/topics/technology/internet-media-devices/2026-technology-trends-older-adults/
- S44 https://www.pewresearch.org/internet/fact-sheet/mobile/ — survey Jan–Jun 2026
- S45 https://memorymurals.com/journal/familyalbum-review — 2026-04-01 (competitor-affiliated)
- S46 https://irbank.net/E05617/rc — MIXI ad-spend series (secondary)
- S47 https://www.pricey.jp/web/articles/6701 — JP prices (secondary)
- S48 https://help.family-album.com/hc/en-us/articles/4403090436633-How-many-people-can-join-an-album (403; snippet)
- S49 https://blog.family-album.com/announcements/ — announcements index (2022–2026), fetched 2026-11-03
- S50 https://www.asx.com.au/asx/v2/statistics/announcements.do?by=asxCode&asxCode=TNY&timeframe=D&period=M6 — TNY announcement list May–Nov 2026, fetched 2026-11-03 (PDF links idsId 03161443 / 03158464 / 03130887 / 03130916 / 03114612 / 03151032 all return the ASX terms page)
- S51 https://babypicsapp.com/ — Baby Pics (Burleigh Creative), fetched 2026-11-03
- S52 https://blog.family-album.com/announcements/familyalbumsupport-for-those-affected-by-the-la-wildfires/ — 2025-01-16
- S53 https://blog.family-album.com/announcements/get-8-free-photo-prints-every-month/ — 2022-06-27
- S54 https://www.cdc.gov/nchs/nvss/births.htm — "Births: Final Data for 2024" (dated 6/9/2026): 3,628,934 births; cross-checked against https://www.cdc.gov/nchs/data/vsrr/vsrr041.pdf (VSRR No. 41, Dec 2025, 2024 provisional denominator 3,628,934)
- Also: https://mixi.co.jp/en/news/2026/0609/52979/ (Japan Expo Paris); https://mixi.co.jp/en/ir/message/ (via customers.md); https://investors.tinybeans.com/announcements (404); https://tinybeans.com/investors/ (no documents); https://www.otcmarkets.com/otcapi/company/TNYYF/dns/news (no JSON returned)

Not readable this round: MIXI FY2026 Q3/Q4 results decks; Tinybeans Q3 FY26 deck (marketindex 403), FY26 annual report, Q1 FY27 4C, 3 Nov 2026 securities notice and July 2026 CEO release (ASX gated); nasdaq.com Qeepsake release (503); BusinessWire S22 (403); kalkine (403); nikkei.com (paywall). Per-turn web-search budget was exhausted at the start of the repair, so all additions came from direct fetches of known URLs and locally cached PDFs.

---

## 8. Audit log

Repair performed 2026-11-03 against the hostile-audit findings. Each item: what was found → what was done.

**Untagged numbers**
1. "11 years" (BLUF, Q7, §4) → tagged [estimated: launched April 2015 per S2 → 2026]; S2 quote "launched in April 2015" added to Q1.
2. "A$7M micro-cap with ~95k paid subs" (BLUF) → tagged inline [sourced-secondary: S32] and [sourced-secondary: S29].
3. Store-metrics "Last update" column (Oct 29/Oct 28/Sep 28, no source) → replaced with US App Store latest-version labels re-fetched today (FamilyAlbum v23.2.0 "1d ago"; Tinybeans v5.93.0 "1d ago"; Qeepsake v4.9.21 Sep 8) [sourced: S15/S16/S17]; note added that the old dates were of unknown origin.
4. "5GB / 20 uploads per month per S45" → split into [sourced: S24] for 5GB (~1,200 photos) and [sourced-secondary: S45] for 20 uploads/month.
5. "7 years and two storage-class migrations" → tagged [estimated: 2022 − 2015; S2, S11].
6. US births "recalled, not fetched" → replaced with 3,628,934 (2024 final) [sourced: S54 CDC NCHS, 2026-06-09], cross-checked against VSRR No. 41; scenario and numbers-table rows 44a/45 recomputed (2.36M families/yr; 11.8M; 1.18M paying; $71M).
7. c=40% → explicitly labelled an assumption in §4 item 5 and in numbers row 45, with the two indirect signals named.
8. "$5–10M" base case → tagged [estimated: bracketed by Tinybeans FY26 $6.49M and Qeepsake FY25 ≈ $4.1M]; numbers row 46 added.
9. "~70M in 2018" → re-fetched S42; the page does say "a decline from the roughly 70 million reported in AARP's 2018 Grandparents Survey" — kept, now quoted verbatim with the 2018 spend comparison also added.
10. "5-yr CAGR 20%" → re-read S7; transcript says "Net sales has grown steadily with a 5-year CAGR of 20%" for Lifestyle — kept, now quoted verbatim in the Q1 body and row 12.

**Suspect claims**
11. Marketing spend "[unknown]" (major) → corrected. S3 p.30 Lifestyle 広告宣伝費 rows transcribed (FY2024 358/279/940/462; FY2025 445/378/533/582; FY2026 Q1 485), annualised (¥2,039M / ¥1,938M; 15.2% / 13.1% of segment sales), converted to ad spend per net new registered individual (¥480–540 ≈ $3.2–3.6) with caveats (minimo/mixi2 in segment; registrations include relatives); used in Q5 CAC evidence, §4 item 5, mechanism table and rows 20a–20c. Lifestyle 外注費（原価） rows also transcribed and used for a gross-margin ceiling (Q6; rows 20d–20e). Headcount row added (20f). §6 item 3 rewritten.
12. S12 grandparent quote (major) → misquote removed from Q4 and Q7; verbatim sentence restored with its actual meaning (grandparents are subscription-savvy in general; product rule is never to charge them); interview count corrected to "more than 160 interviews conducted between 2024 and 2026". Q7 "grandparents refuse apps" conclusion restated: evidence is that they refuse to pay, not that they refuse apps.
13. 93k vs 95k (major) → S29 re-fetched and confirmed "serving ~95k paid subscribers"; kalkine 403 again; 93k withdrawn everywhere (Q2, mechanism table, row 37 marked withdrawn) and the "flat/declining" narrative re-based on the Q2→Q3 Tinybeans-core flatness and Qeepsake decline only.
14. Registrations "~3M/yr" arithmetic → corrected to ~3.6M/yr (3M ÷ 10 × 12), with the Jan→Jul 2025 run-rate (4.0M/yr) added; propagated to Q1, Q7 and row 4.
15. "Negative every year until FY2026" → restated as negative in FY2024 (−¥682M, estimated sum) and FY2025 (−¥128M), with "years before FY2024 not shown in any document read"; S3's label セグメント利益（EBITDA） noted.
16. S22 "11 free prints" / "25 million users" → still 403 (WebFetch and direct retrieval both blocked); downgraded to [sourced-secondary: S22, unverified]; replaced in the body with the vendor blog's verifiable equivalents (S52 LA-wildfires post, S53 "8 free prints every month", S49 25M milestone 2025-03-04).
17. Tinybeans price "$119.99 Family [S16; S24]" → S16 re-fetched; IAP list is $7.99/mo, $74.99/yr, Legacy $4.49/mo, $39.99/yr; $119.99 attributed to S24 only and flagged as absent from the current storefront; monthly prices added (mechanism table, row 39).
18. Qeepsake ARPU $77→$64 omission → added to Q2 (with the company's e-commerce-spike explanation and "+2% retention both platforms"), to "what has not worked", Q7 and row 35.
19. "A$1.09 mid-2021 / −97%" → withdrawn; replaced by [unknown beyond the −69.57% one-year figure]; Simply Wall St 5-yr −94% kept as snippet-only (row 38a). S32 current-day figures re-verified.
20. AI 2025–2026 single-review evidence → rewritten as [unknown] with tries listed: App Store version history (12 releases; only "Memories screen" v23.0.0), blog announcements index (S49), S12, S6; the Google Play review explicitly excluded as evidence.

**Broken/misquoted sources**
21. S12 → re-read verbatim; quote and interview phrasing fixed (items 12); video limits re-confirmed.
22. S22 → see item 16.
23. S29 → re-verified for every FY26 figure; 95k adopted (item 13).
24. S16 → see item 17.
25. PDF-extraction note (S2–S6, S23, S25, S27) → added to Q1 header and source list for future auditors.
26. S48, S31, S33 → still 403; left as snippet-only with that stated; S33 2021 anchor withdrawn.

**Missing vs brief**
27. Q1 marketing spend → added (item 11).
28. Q1 UK/DE/FR prices → fetched from the GB/DE/FR App Store storefronts (S15-GB/DE/FR); prices and rating counts added to Q1, mechanism table, rows 16a–16b.
29. Q1 AI features → tries listed; [unknown] (item 20).
30. Q1 Q4-deck KPI slides via S4 → S4 scanned in full; only capital-allocation/portfolio/shareholder-return pages are "Repost From FY2026 Q4"; comments/stickers chart confirmed absent; S7 transcript cited for the fact of disclosure.
31. Q2 Q1 FY27 4C → located on the ASX list (28/10/2026, S50) but every PDF route (ASX idsId links, investors.tinybeans.com/announcements, tinybeans.com/investors, OTC API) failed; routes and failures recorded. Also surfaced and recorded: "Proposed issue of securities" 03/11/2026, CEO appointment 14/07/2026, Head of Product 12/10/2026, Annual Report 27/08/2026 — titles only.
32. Q2 churn and runway → explicit derivations added (4% / 21% annual churn; ~18-month runway at FY25 burn; OCF positive so not binding; 3 Nov securities notice flagged as unread).
33. Q2 Qeepsake ARPU → item 18.
34. Q3 Baby Pics → babypicsapp.com fetched (S51): Burleigh Creative photo editor, vendor-claimed 5M+ families; added to Q3 table and row 41a; noted it has no invite mechanic.
35. Q5 creators / pediatrician / The Bump placements → S49, S6, S7, S21 checked; nothing found; recorded as [unknown] with the search-budget limitation stated.
36. Q6 gross-margin statement → 外注費 rows used for a ceiling (item 11); Tinybeans hosting line: FY25 "annual report" in cache identified as the results release (S23); FY26 Annual Report on ASX gated — recorded.
37. Scenario births input → item 6.

Items not fixable this round (no search budget; gated PDFs): the Q1 FY27 subscriber count, the 3 Nov 2026 securities-issue terms, the FY26 annual-report cost lines, FamilyAlbum AI releases, and creator-marketing evidence remain [unknown] with the attempts listed in §6.
