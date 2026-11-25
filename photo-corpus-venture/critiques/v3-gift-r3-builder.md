# v3-gift — round 3 — BUILDER critique

Written 2026-11-25. Fresh context. Variant scored: `variants/v3-gift.md` (written 2026-11-24).

## Stance

Builder. I believe shipped demos. I scored Buildability and Economics hardest, checked the 4-week spec line by line, and asked what breaks at 10,000 gifts.

**Coverage.** Read in full: SCORECARD.md, the variant, `memoir-gift-market.md`, `family-artifact-market.md`. Read the body sections (not the source lists or audit logs) of `institutional-legacy.md`, `sizing.md` Q1–Q4, `grandparent-loop.md` Q1–Q7, `digitization-market.md` Q1–Q9, `face-regulation.md` Q1–Q7, `unit-economics.md` Q1, Q6, Q7. The other research files and `assumptions/A1–A6` were read at their openings and searched by keyword (voice, speech, telephony, consent, HIPAA, print, handwriting, XMP), not end to end. `variants/current.md` was checked only for the pro-edition figures. No CHANGELOG, other v3 variant or critique was read (one command that would have printed the header of an earlier critique was blocked before it ran).

**Verdict in one line.** The call loop can be demoed in four weeks and nothing is gated by Apple or Google. The business case is weaker than the variant says: it needs a 36–52% price premium over the leader to reach its own contribution figure, the feature that would justify the premium is the one part nobody has measured, and the ceiling arithmetic rests on a Storyworth estimate the research has since withdrawn.

## Scores

| # | Dimension | Score | Evidence pointer | One-line reason |
|---|---|---|---|---|
| 1 | Pain | 5 | memoir-gift-market.md bottom line 1, Q2, Q6; digitization-market.md Q6; genealogy-market.md line 134 | People pay about $99 once for a parent's memoir (Remento >$7M in under a year, 100,000+ families). Nobody is shown paying for names on photos; self-serve tagging runs at 0.10 per scan. |
| 2 | Wedge | 5 | memoir-gift-market.md Q1 (Storyworth Voice works on a landline), Q2 (≈10 stories per family of 52 prompts), Q8 (stalled subscription is the most common bad outcome) | The payer changes no habit. The parent must phone an unknown number to start, then take 26 AI calls; the category's known failure is that elders stop. |
| 3 | Why now | 5 | memoir-gift-market.md Q5 (voice at $0.023–0.05 per minute), Q1 (Storyworth Voice, 2026), Q2 (Remento Ornament, 2026-10-22) | The cost drop is real and dated. The leader and two others have already used it. The 2024 launch price and FCC 24-17 are the variant's own fetches; no research file covers them. |
| 4 | Platform risk | 3 | memoir-gift-market.md bottom lines 3–4, Q4 table; genealogy-market.md line 47 | "Both wedges already ship at incumbents." Memory Murals already tags people and dates from voice; Remento now attaches recordings to a photo; the variant omits one and understates the other. |
| 5 | Compounding asset | 4 | grandparent-loop.md Q2 (finishing the book causes churn; Qeepsake 79% retention); family-artifact-market.md Q1 (Nixplay ~1.2% paid); digitization-market.md Q1 (83% auto-renew when backup is paid) | The recordings cannot be regenerated, which is new. The variant then gives away the retention lever (free reading forever, open export) and no asset crosses families. |
| 6 | Distribution | 4 | family-artifact-market.md Q1 (Aura: networks drove 50% of 2024 sales), Q2 (Famileo 70% word of mouth is undated, pre-2022); memoir-gift-market.md Q1, Q7 (TV, podcasts, 6% affiliate; CAC unknown) | A weekly clip to 4–7 relatives is a plausible loop with analogue evidence only. The leader buys national TV. No memoir company discloses CAC. |
| 7 | Economics | 4 | memoir-gift-market.md Q5, Q6, Q7; family-artifact-market.md Q3; no evidence found for book print cost at volume, support cost, the price premium, CAC or renewal (cap 4) | Fully tagged model, but the inputs that decide it are unevidenced. At the category's $99 the contribution is about $33, not $68. |
| 8 | Buildability | 5 | memoir-gift-market.md Q1, Q3 (two shipped phone interviewers), Q5 (response of people 70+ is unknown); ai-why-now.md Q4 (handwriting accuracy unknown) | The call can be demoed. Name accuracy, face-to-name mapping and handwriting are unmeasured, and the acceptance tests cannot be run inside the four weeks. |
| 9 | Ceiling | 2 | memoir-gift-market.md bottom lines 1–2, Q1 (Scenario A withdrawn), §3 (largest sourced revenue: Remento >$7M; largest audited: £2.62M) | The variant concedes $100M does not pencil. Its $2–24M range is built on a withdrawn Storyworth estimate. |
| 10 | Founder fit | 5 [unknown] | — | Neutral placeholder. |

**Total: 42** (founder fit is a flagged neutral 5).

## Numbers checked against the research

Where the variant and the repaired research disagree, the research wins.

| Variant claim | Research | Result |
|---|---|---|
| Storyworth "~$13.5–45M a year"; "150,000–500,000 plans a year"; category "210,000–560,000 gifts… $20–52M" | Scenario A "rested on two invented drivers… and is deleted"; Storyworth revenue and customers are [unknown] (memoir-gift-market.md Q1, audit items 2 and 16) | **Failed.** Every Ceiling line that multiplies by 0.34–0.91% inherits it. |
| Completion proxy "~16 stories per Remento order" | Withdrawn; ≈10 stories per family (memoir-gift-market.md Q2) | **Failed.** Completion is worse than the variant assumed. |
| 75+ smartphone ownership "43% for 2021" | Withdrawn, no URL (family-artifact-market.md Q5, numbers row 31) | **Failed.** The 40% booklet share has no anchor either way. |
| Memory Murals: "$69/year founding price", stories "typed or spoken by the user" | $99.99 a year; "People & dates tagged automatically from your voice" (memoir-gift-market.md Q4, S92) | **Failed / understated.** The nearest product already extracts names from speech. |
| "None runs an interviewer over the family's photos and emits a per-photo record" | True only for the full combination; the gap is "narrower than first written" (bottom line 4) | Holds narrowly. |
| No mention of the Remento Ornament | Launched 2026-10-22: "one photo, every story behind it", $29.99 (Q2, S76) | **Omitted.** It weakens load-bearing assumption 7 a month before the variant was written. |
| Magic Interviews sits on the $199 tier | Homepage says $199 only; Storyworth's own blogs say Color ($99) also includes it (Q1) | Unresolved. If the blogs are right, the comparison price is $99. |
| Famileo "70% of subscriptions come from word of mouth" | Undated passage, pre-2022, from when Famileo had 700,000 users (family-artifact-market.md Q2) | Stale; presented as current. |
| Voice cost $12.5 central, $7.2–27.9, with 25% overhead | Mid-priced stacks $19–30 with 30% overhead and chapter writing; $9–67 across all prices (memoir-gift-market.md Q5) | Inside the range; the central figure picks the second-cheapest stack. |
| Booklet: $7.00 print + $2.27–2.56 First-Class flat | Same figures; First-Class is the required class (family-artifact-market.md Q3) | **Holds.** |
| Book $35.91 for 100 pages; Media Mail $5.13 | Not in any research file (variant's own fetch of list prices). Research resolved the mail class for journals only | Not supported. See Economics notes. |
| LifeBio "over $2 million" as the institutional cap | May include grants: $5.37M of NIH awards FY2020–26 (institutional-legacy.md bottom line 2). The $8–28M channel framing was withdrawn; the arithmetic runs $1.7M–$85M (Q8) | The variant's $0–2M line is unaffected; its "$7.5–28.3M" aside is stale. |
| Voice as biometric data: "Illinois and Texas" | Washington's My Health My Data Act lists "voice recordings" from which a template can be extracted as biometric data, treats it as consumer health data, and carries a private right of action (face-regulation.md Q3) | **Missed.** The product stores exactly such recordings. |
| TCPA, call-recording consent, text-sender registration, carrier labelling | No research file covers any of them | No evidence found. The legal design rests on the variant's own reading of one FCC ruling and on search snippets. HIPAA is not addressed anywhere. |
| "import back into Apple Photos and Google Photos albums" with names | Apple Photos will not import person names from metadata; Google is [unknown] (ios-feasibility.md Q9) | Names survive only as keywords. |
| Arithmetic (revenue per gift, COGS sum, renewal base, $184, 542,000 gifts) | Recomputed | Internally correct. |

## Economics notes (why 4)

1. **The $68 contribution needs a premium the research does not support.** The variant's net gift price is $135. The category "anchors at $99" (memoir-gift-market.md Q6); Storyworth Color is $89 on sale and Remento discounts up to $50 in Q4. Re-running the variant's own cost table with only the price and card fee changed:

   | Net gift price | Revenue incl. 0.2 extra books | COGS | Contribution | Gross margin |
   |---|---|---|---|---|
   | $135 (variant) | $148.8 | $81.2 | $68 | 46% |
   | $99 (category anchor) | $112.8 | $80.1 | $33 | 29% |
   | $89 (Storyworth Color on sale) | $102.8 | $79.8 | $23 | 22% |

   The only sourced CAC in the project is Qeepsake's $35; the derived paid-install figure is $65–90 (sizing.md Q4). At the category price this does not pay back on the first order, and the variant says itself that it has to.
2. **The book is costed at 100 pages; the product spec implies up to 156.** One photo per spread at 2–3 photos per call over 26 calls is 52–78 photos, so 104–156 pages. At the variant's own Blurb rate that is $36.59–45.43 for the first copy, up to $11 more per gift once the 0.2 extra copies are included.
3. **Media Mail at $5.13 is an assumption.** Print-on-demand vendors normally ship on their own rate cards, and whether a personalised photo book qualifies for Media Mail was not researched. (This is my own caution, not a research finding.)
4. **Missing cost lines:** reprints for wrong names (the variant's own "ruined gift" case), refunds for gifts never activated, sender registration and number reputation, affiliate fees (6% at Storyworth).
5. **Throughput against the promise.** The gift accepts 300 photos and gets through 52–78 a year at full call completion, 36–55 at the 70% acceptance threshold. Most of what the family uploads is still in the queue when the book prints.
6. **Less talk time than the nearest competitor for more money.** Tell Mel Standard is 12 interview hours for $129 (memoir-gift-market.md Q3). This is 2.6 hours and a book for $135–149.
7. Renewal, completion and CAC are [unknown] for every company in the category (memoir-gift-market.md Q7). The loop takes 12 months to close once.

## The 4-week spec, line by line

| Spec line | Verdict | Note |
|---|---|---|
| Wk 1: web upload by link | Buildable | — |
| Wk 1: browser capture of print fronts and backs | Buildable, low quality | Glare, skew and cropping in a mobile browser are Photomyne's whole product. Fine for a demo. |
| Wk 1: vision description, people boxes | Buildable | Commodity. |
| Wk 1: handwriting OCR on backs | **Research-grade unknown** | Large models score below 50 of 100 on OCRBench v2 and are "prone to errors in handwritten content extraction"; faded cursive on photo paper "needs a hands-on test" (ai-why-now.md Q4). Why-now item 7 prices it and assumes it works. |
| Wk 2: voice agent over telephony | Buildable | Storyworth and Tell Mel ship one. Not measured: turn-taking with slow, hard-of-hearing speakers on a narrowband line. |
| Wk 2: inbound consent call | Buildable; **activation risk** | The parent must dial an unknown number printed on a card to talk to a machine. No evidence on how many do. |
| Wk 2: scheduled outbound with retries and voicemail | **Policy-gated at scale** | Fine for 10 families. At volume, new numbers placing AI calls get spam-labelled; the variant marks cost and lead time [unknown]. Voicemail detection misfires on slow answerers. |
| Wk 2: texted link to a tap-to-talk page | **Platform-gated** | US carriers require sender registration before application texts are delivered; approval can take longer than the week this is scheduled for. No research on it. |
| Wk 2: dual-channel recording | Buildable | Avoids a speaker-identification model, as claimed. |
| Wk 3: transcript to per-photo record | Buildable, **accuracy unknown** | Surnames and place names from speakers over 75 on a phone line: no measurement exists in the research. |
| Wk 3: "the woman on the left" to a detection box | **Research-grade for landline users** | Caller and interviewer do not share a view; the numbered booklet identifies the photo, not the person. |
| Wk 3: spell-back for names | Buildable, poor experience | Letter-by-letter spelling with a hard-of-hearing caller on 8 kHz audio, several times a call. |
| Wk 3: family feed, corrections, weekly digest with audio | Buildable | Clips go to every relative within an hour with no review by the parent. See 10k notes. |
| Wk 4: book PDF with QR codes to a print API | Buildable | Each QR code is a promise to host the audio for as long as the book exists. |
| Wk 4: read-only MCP endpoint | Buildable, off the critical path | Proves nothing about the loop. Cut it. |
| Wk 4: pilot with 10 parents from friends and family | **Cannot test the acceptance criteria** | One or two calls per parent in the time left. "70% of scheduled calls completed" and "95% of names correct after review" need weeks of calls; the book and renewal need a year. Friends and family inflate answer rates. |
| Acceptance: 95% of names correct after one family review | Measures the relatives, not the system | The number that matters is accuracy before review. |

**Smallest thing that proves the loop:** one phone number, one hosted voice model, 10 parents who are not friends, 20 photos each, three weeks of calls. Measure first-call activation, calls completed, named photos per call and name accuracy before any relative touches the record. Skip the book, the feed and MCP.

**Ugliest technical risk:** the variant names it correctly. Proper names and the right face, from an old voice on a narrowband line, with no shared view. Everything that separates this from Storyworth Unlimited lives in that step, and its failure is printed in hardcover.

## What breaks at 10,000 gifts

- **Call volume and labelling.** 260,000 scheduled calls a year, bunched into January to March because the gift sells in Q4 and calls are weekly for eight weeks. That is the outbound pattern carrier analytics flag.
- **The dead and the declining.** About 1.68M Americans aged 75+ die each year (sizing.md Q2) and 44% of assisted-living residents have dementia (institutional-legacy.md Q1). At this scale the system will phone households where the storyteller has died or can no longer consent, unless a relative tells it first. The only control in the spec is what the payer discloses at purchase.
- **Unreviewed broadcast.** Whatever a parent says about a living relative is sent to siblings and cousins within the hour. A review gate fixes that and removes the day-1 value the Wedge section depends on.
- **Support.** 10,000 callers aged 70–90, 10,000 payers and 40,000–70,000 relatives on a $6 allowance per gift.
- **Book season.** Month-12 books for Q4 gifts fall in the next Q4, the print peak, with proof approval by the family first.
- **Data-loss liability.** The company holds "the only copy of what the parent said", promises free access forever and prints links to it in books. HereAfter AI's site is gone and its recordings are available "by email request only" per a competitor (memoir-gift-market.md Q3). There is no funding line for perpetual hosting.
- **Legal exposure.** Washington's health-data law reaches stored voice recordings with a private right of action (face-regulation.md Q3). A stored face rectangle plus a name is untested (Q7). TCPA, all-party recording consent and HIPAA (if a hospice or community ever passes resident details) have no research behind them.

## Most damaging objection

**The variant only earns its $68 contribution at a net price 36–52% above the category leader, and the one feature that could justify the premium is the one nobody has shown working.** Storyworth already sells a phone interviewer with follow-up questions, photo prompts, a colour book and QR audio at $99–199; Tell Mel sells 12 hours of AI phone interviews for $129; Remento sells a photo-anchored recording product at $29.99; Memory Murals already tags people and dates from speech. Priced where the category prices, this variant clears about $23–33 a gift before acquisition, against a $35 sourced CAC and a $65–90 derived one. What is left to charge more for is the per-photo name record, which depends on name recognition from elderly speech on a phone line and on tying a spoken "on the left" to a face, both unmeasured, and which the four-week demo as specified cannot measure. Buyers in this category have so far paid for the book.

## Weakest dimension

**Ceiling (2).** The variant's own honest range is $2–24M, and the inputs behind it were withdrawn in the research repair. The largest sourced revenue in the category is Remento's >$7M, earned after a national television deal. Among the dimensions that building can change, **Economics (4)** is the weakest.

## Strongest dimension

**Wedge (5, tied with Pain, Why now and Buildability).** This is the first variant since round 0 whose adoption path needs no library migration, no platform API and no app on the user's side: the payer makes a purchase 100,000+ Remento families have already made, and the parent uses a telephone. It stops at 5 because the parent must make the first call and then keep answering, and the category's one completion number is 10 stories out of 52.

## Unknowns research could resolve before the next round

1. What word and proper-name error rates do current telephony speech models report for speakers aged 75+ on 8 kHz phone audio, and is there any published figure for surnames or place names?
2. How does Storyworth Voice actually work: who places the call, is Magic Interviews on the $99 Color plan or only the $199 plan, and does any Storyworth or Remento help page describe a question asked about an uploaded photo with the people in it saved?
3. What does a one-off 8×10 hardcover of 100–160 colour pages cost through a print API (Lulu, Blurb, Gelato, Peecho, Mixam) including the vendor's own shipping, and does a personalised photo book qualify for USPS Media Mail?
4. What are the current lead times and fees for US text-sender registration and for caller-identity registration with the carrier analytics firms, and what answer rates do registered versus unlabelled outbound calls get among people 65+?
5. Does a server-stored interview recording count as biometric or consumer health data under Washington RCW 19.373, do any memoir or voice-recording services restrict Washington, and how does the TCPA treat an AI-voice call placed under a third party's purchase (consent from the called party, revocation handling)?

## Three questions for the founder

1. This is an operations business with printed booklets, book proofs, reprints and phone support for people in their eighties. Do you want to run that, and who answers the phone in January?
2. The loop takes 12 months to close once (gift, calls, book, renewal). Do you have the runway to fund a first cohort before you know completion or renewal?
3. Would you still build this at $99 with roughly $33 of contribution per gift, and what do you have that a profitable 13-person Storyworth does not: an audience, a television or podcast channel, or relationships inside senior living?
