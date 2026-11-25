# v4-claims — round 4 critique — TARGET CUSTOMER

Written 2026-11-25. Fresh context. Read: `SCORECARD.md`, `variants/v4-claims.md`, `research/contents-claims.md` in full (including its audit log), the bottom lines and the cited sections of the other research files and `research/assumptions/A1–A6.md`, and the headings and Ceiling of `variants/current.md`. Not read: CHANGELOG, other v4 variants, any critique.

## Stance

I am the homeowner this variant is for. The house burned six weeks ago. I have $400,000 of contents coverage. The insurer advanced part of it without a list and wants an itemized inventory with ages and prices for the rest. If I am a California total loss in a declared emergency, the advance is 60% ($240,000) and the list decides the other $160,000 [estimated: 400,000 × 0.60; 400,000 × 0.40; rule sourced in contents-claims.md 2.1]. I have an iPhone with 40,000 photos, a spouse, two adult children with their own phones, a rental, and a public adjuster asking 10–15%.

What the choice looks like from here:

| Option | What it costs me | Evidence |
|---|---|---|
| Public adjuster at 10–15% of what is still unpaid | $16,000–24,000 if the whole $160,000 is recovered [estimated: 160,000 × 0.10 to 0.15]. In California the fee cannot reduce amounts paid before the contract | contents-claims.md 2.3 (Cal. Ins. Code §15027(b)(7)); 15.9% of Los Angeles respondents hired one |
| Bevel | $0. Takes old family photos, videos, receipts; prices; exports a spreadsheet | contents-claims.md 2.4 |
| Loti's AI inventory tool | $0; its self-service claim suite is $100 a month | contents-claims.md 2.4 |
| United Policyholders spreadsheet | $0; used by 21.51% of respondents | contents-claims.md 2.8 |
| This variant | Free search, gallery and draft; $199 for the priced, attested export | variant, Business model |

The $199 is not the obstacle: it is about 0.12% of the money at stake [estimated: 199 ÷ 160,000]. The obstacles are whether it finds more than the free tools, whether my insurer accepts what it finds, and whether I have the energy to try a second tool.

## Where the variant and the repaired research disagree (the research wins)

The variant was written before `contents-claims.md` was audited. These claims in the variant are failed or unsupported.

| Variant claim | Repaired research | Effect |
|---|---|---|
| Pool of 40,000–80,000 households a year, central 60,000, "hard upper bound" 130,000–150,000 | Withdrawn (2.2; audit S4, U6). Fire segment 25,000–50,000 in an average year, about 60,000 in a peak wildfire year; other perils not sized; every share is an unanchored assumption | Every Ceiling line, the 23,900 professional pool, and the 0.1% loss chance rest on a withdrawn number. Central line A with a 37,500 pool and the variant's other inputs is about $0.24M, not $0.38M [estimated: 37,500 × 0.63 × 0.5 × 0.10 × 199] |
| High case "still itemizing" 73% | Corrected (2.1; audit S8). 27% of total-loss respondents, or 19.28% of all respondents, had 100% without a list; the funnel says "roughly half" are still asked to itemize | 73% is not a sourced itemizing share |
| Florida is the state where a paid done-for-you inventory is public adjusting | Reversed (2.6; audit S1). F.S. 626.854(1) expressly excludes "a person who photographs or inventories damaged personal property" who does not solicit or negotiate | The "NOT in v1: Florida done-for-you service" line and the Florida warning to organizers are wrong as written. Whether the carve-out covers destroyed property rebuilt from old photos is [unknown] |
| Line C: carriers at ContentsTrack's $36–45 a job; XactContents $950–1,900 a seat-year | ContentsTrack is contractor pack-out software; XactContents prices withdrawn; what carriers pay per contents claim is [unknown] (2.3, 2.7; audit S6) | Line C and its $0.2M central have no basis |
| Contents specialists $800–8,000 flat | Withdrawn (2.3). One dated example: 10% of recovery, 2018 | No flat-fee anchor exists |
| NAPIA about 600–750 members | Withdrawn; [unknown] (2.3) | Professional buyer count is unknown beyond 1,697 Texas licences |
| 38% admitted overstating a home claim | Withdrawn (2.6; audit S7). 17%, 14 countries, 2014, not home-only | Fraud context weaker and older |
| Enservio $41–56M, Encircle about $9.9M | Withdrawn (section 4; audit S5). No contents-inventory vendor has a sourced revenue | No comparable revenue at all |
| "United Policyholders recommended Bevel at a workshop" | Corrected (2.4; audit S14). A local news story, reposted, says a survivors' meeting suggested it; not an endorsement | The nonprofit channel is less proven than stated, for anyone |
| Quotation "These are features Bevel could add in weeks; they are not a company" | Not in the repaired file. 2.8(c) marks the point as the researcher's judgment, not evidence | Still plausible; not a sourced fact |
| Sensitivity (b): $18M and $45M at $300 a household | Withdrawn (audit U1, S3) | Drop |
| SB 495 listed as a dated change that shrinks the job | The percentage did not move at the default coverage ratio; the cap rose by $100,000 (2.1; audit S2) | Weaker why-now, and a weaker threat, than the variant says |
| Colorado "65% (2022)" | Year dropped (audit U12) | Minor |
| Loti is absent from the variant | A public-adjuster firm gives away an AI inventory "from your photos" and sells a $100-a-month suite (2.4) | A second free competitor, and a member of the variant's first payer class that built its own tool |

The variant's prices for ProofList and Contents.team, the NAIC model text, the NAPIA red-flag page, the fraud statistics and the 2026-03-30 assistant guide are its own fetches and are in no research file. No score below rises on them.

Arithmetic checked and correct on the variant's own inputs: per-photo cost $0.0033–0.0066 at the token prices in unit-economics.md Q3; cost table sums; 89% / 73% / 44% gross margin; 28% with nine free users per buyer; the three line A products; 358,000 households for $100M at $279.

## Scores

| # | Dimension | Score | Evidence pointer | One-line reason |
|---|---|---|---|---|
| 1 | Pain | 6 | contents-claims.md 2.1 (53% / 56.37% told to list every item; half struggle with itemization; "over 5,000 line items"); 2.3 (15.9% hired a public adjuster, 7.8% a contents specialist); 2.5 (no post found paying a stand-alone fee) | The most acute pain of any variant and I am paying for it in months of evenings; it happens once in a lifetime, 42% of respondents were paid without a list, and nobody was found paying for an inventory tool |
| 2 | Wedge | 5 | contents-claims.md 2.5 (United Policyholders already says friends and family may have photos; a survivor says "even though I have photographs to look at, it's exhausting"); 2.4 (no entrant pools relatives' libraries); 2.6 (24% / 28.30% must state when or where each item was obtained); funnel row "usable pre-loss interior photos" [unknown]; platform-access.md Q1 (limited library access) | I would run the free search if someone I trust handed me the link, and my spouse and children would too; the share of my list it recovers is unmeasured and the same first step (upload old photos) already exists free |
| 3 | Why now | 4 | contents-claims.md 2.1 (SB 495 did not move the percentage), 2.4 (Bevel since 2025-01; three hackathon prototypes); unit-economics.md Q3 (vision prices) | Dated changes exist, but the fires and cheap vision models helped a free tool first, and the statute change is smaller than the variant says |
| 4 | Platform risk | 3 | contents-claims.md 2.4, 2.8(c) (Bevel and Loti free; the two differentiators judged addable); platform-access.md Q1 (limited access); memory-product-sdk.md Q6 (guideline 5.1.1(iii)) | The differentiator disappears if I tap "limited access", and the incumbent needs no platform's help to copy it |
| 5 | Compounding asset | 2 | Variant, Compounding asset; contents-claims.md 2.3 (Enservio price database, 2016), 2.4 (Bevel "3M+ items") | My photos are used once and deleted; I never come back; the price table starts behind two others |
| 6 | Distribution | 3 | contents-claims.md 2.4 (a survivors' meeting suggested Bevel; ">25%" is one funding digest's relay of a company claim), 2.3 (national adjuster count [unknown]), 2.4 (Loti built its own); sizing.md Q5 (every keyword route failed) | In my fire zone the name passed between neighbours is Bevel; no channel is evidenced for a paid second tool, and between disasters there is none |
| 7 | Economics | 4 | Variant, Economics (arithmetic verified); unit-economics.md Q3, Q7; contents-claims.md bottom line 1 and revenue scenarios (no stand-alone price observed; $1.2–2.3M at observed adoption); sizing.md Q4–Q5 (CAC anchor $35, derived $65–90; cost per click [unknown]) | Costs are modelled and tagged, but the $199 price has never been observed, free users cut margin to 28%, there is no repeat purchase, and central revenue does not cover a three-person team |
| 8 | Buildability | 6 | contents-claims.md 2.4 (three hackathon photo-to-inventory prototypes); ios-feasibility.md feasibility table (Vision labels free; local copies about 1536×2048), Q2–Q3; platform-access.md Q1 | Demoable in four weeks; the location query's recall and instance merge are untested, and ios-feasibility.md has no finding on how many photos carry a location |
| 9 | Ceiling | 1 | contents-claims.md section 4 revenue scenarios ($1.2–2.3M fire segment, $4.7M all perils, at observed price and adoption); bottom line 6 (no vendor revenue sourced) | Below the $5–45M band that has meant 2–3; the variant's own $0.5–4.8M falls further once the withdrawn pool is replaced |
| 10 | Founder fit | 5 [unknown] | — | Not stated by the founder |

**Total: 39** (founder fit is a flagged neutral 5).

## The single most damaging objection

**The step the variant charges for has no observed buyer, and I am the proof.** At six weeks, the tool my neighbours pass around is free, already turns old family photos into a priced spreadsheet, and says it works with carriers (contents-claims.md 2.4). The variant's own Economics section says its free tier must stop before item listing for most photos, or margin falls to 28%. So on the day I compare them, the newcomer's free tier does less than the incumbent's, and the $199 buys me two things: an automatic search I can approximate by typing my address into Photos, and a date stamp per line. Neither answers what my adjuster actually asks for, which is age, price and, for 24–28% of claimants, when and where each item was bought (2.6). A photo shows the sofa existed in 2019; it does not show it was in the house in 2025.

The fallback payer does not rescue it. The variant sells first to public adjusters, and the one adjuster firm in the research (Loti) built its own photo inventory and gives it away. The research found no forum post, no price page and no survey in which a household paid a stand-alone fee for inventory software after a loss (2.5; bottom line 1). The variant's falsifier 4 is, on current evidence, already half-met.

## Weakest dimension

**Ceiling (1).** At the only observed software price and the only observed paid-specialist adoption rate, the fire segment yields $1.2–2.3M a year (contents-claims.md section 4). Nine figures requires charging a percentage and dealing with the insurer, which is a licensed public-adjusting firm competing for a fee pool that adjusters and attorneys already hold. The variant says this itself.

## Strongest dimension and why

**Pain (6).** This is the first variant where the customer has a deadline, a named counterparty, and five or six figures riding on a document they must produce. 53–56% of Los Angeles respondents were still told to list every item a year on; half struggled with it; 15.9% gave a public adjuster a share of their recovery. I would do almost anything that made this list shorter. It is held at 6 because it happens once, a large minority are paid without a list, United Policyholders' first advice is to negotiate a cash-out and skip the list, and none of that willingness has yet shown up as money paid for a tool.

## What I would actually do, and who else would take part

- **First step.** Yes, if it came from a neighbour, a United Policyholders volunteer or my adjuster. No, from a search ad. Full-library permission to an unknown company, six weeks after the fire, needs a trusted introduction. Most of my 40,000 photos were taken at home, so "approve what to upload" means reviewing thousands of pictures of a house that no longer exists; the variant's ten minutes is optimistic.
- **My spouse and adult children.** Yes. The ask is small, time-bound and for their own family home. This is the most willing supplier group of any variant so far. More distant relatives: some. Android relatives get a manual upload with no search, so the pooled part works for iPhone families only.
- **What I give up.** Full library access; interior photos of my home held by a start-up for up to 36 months; and my signature on every AI-drafted line. If a line is wrong, the fraud question lands on me, not on the tool.
- **If the start-up dies.** The export is mine, which is good. But California gives me 36 months to claim replacement cost, and a company whose central revenue is about $1.5M against $0.9M of spend may not be there in month ten. The variant says nothing about what I keep if it closes.
- **Would I recommend it?** Only if it found items Bevel missed and my adjuster paid on them. Neither is known.

## Unknowns research could resolve before the next round

1. Do insurers pay contents lines whose only proof is a dated pre-loss photo? Search carrier claim guidance, state insurance department complaint data and United Policyholders material for acceptance or rejection of photo-evidenced items in the 2025 Los Angeles claims.
2. What do Bevel and Loti ship today: direct import from iCloud or Google Photos, invitations to relatives, a photo and capture date per line? And what share of Bevel's free users buy anything (the reported $60-a-year tier, or brokerage)?
3. What share of iPhone photos carry location metadata, and what share of users grant full rather than limited photo-library access when an app asks?
4. How many licensed public adjusters are there nationally, and what claim or contents software do they pay for today, at what price (state licensee open data; pricing pages of adjuster claim-management tools)?
5. What is the cost per click on "public adjuster", "fire claim contents inventory" and "home inventory after fire" in a declared disaster county?

## Three questions for the founder

1. Has anyone on the team worked a contents claim as an adjuster, public adjuster or claimant, and can you put the five-home test in front of five burned-out households and five public adjusters within a month?
2. In one sentence, what do you tell me that makes me install a second tool when my neighbours already use a free one? If there is no such sentence, would you rather give this away inside the organizer product or license it to Bevel, Loti or adjuster firms?
3. If the company closes in month ten of my 36-month replacement-cost window, what exactly do I still hold: photos, hashes, the working list, in a format another tool or my adjuster can open?
