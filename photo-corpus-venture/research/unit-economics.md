# Track D — Unit economics (storage + indexing + pricing + retention)

Written 2026-11-03; repaired 2026-11-03 after hostile audit (see "Audit log" at the end). All prices accessed 2026-11-03 unless a different source date is given. Currency as published (USD unless marked EUR). "Reference user" = 100 GB library defined in §2.

Tags: `[sourced: url, date]` = primary or near-primary, fetched; `[sourced-secondary: ...]` = only a third-party source was reachable, flagged; `[estimated: method with inputs]`; `[unknown]`; `[unverified: ...]` = figure recalled or snapshot-only, NOT used in any calculation.

Note on tooling: the shared web-search budget for this session was exhausted before the repair pass began; every repair below was done by direct fetch of official URLs (and of the AWS public pricing data feed and SEC EDGAR via plain HTTP). Where that failed, the attempted URLs are listed so the next agent does not repeat them.

---

## 1. Questions asked

1. Storage $/GB-month across 8 providers, egress, and cost to hold 100 GB / 500 GB.
2. What is "100 GB" in photos and minutes of video? (reference user)
3. One-time indexing cost per reference user: embeddings, VLM captions (API and local), OCR, faces — at low/mid/high tiers.
4. Ongoing cost: incremental indexing, vector DB hosting, query cost.
5. Consumer price points in market ($/mo per GB).
6. Churn / retention benchmarks.
7. Gross margin for three plans; payback vs CAC sensitivity.
8. Test A5 and the founder's "storage company economics" fear: is storage or indexing the dominant cost?

---

## 2. Findings per question

### Q1. Storage cost per GB-month (Nov 2026)

| Provider / class | $/GB-month | 100 GB /mo | 500 GB /mo | Egress | Minimums / notes | Source |
|---|---|---|---|---|---|---|
| AWS S3 Standard (us-east-1, first 50 TB) | $0.023 | $2.30 | $11.50 | $0.09/GB after first 100 GB/mo free [egress rate sourced-secondary: cloudzero 2026-07-30; free allowance sourced AWS page] | PUT/COPY/POST/LIST $0.005/1k, GET $0.0004/1k | [sourced: AWS public pricing feed https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/s3/USD/current/s3.json, region "US East (N. Virginia)", key "Standard Storage First 50 TB per GB Mo" = 0.023, "PUT COPY/POST or LIST requests" = 0.000005, "GET and all other requests" = 0.0000004; feed publication date 2026-10-15] |
| AWS S3 Glacier Instant Retrieval | $0.004 | $0.40 | $2.00 | as above | 90-day min duration [sourced: https://aws.amazon.com/s3/pricing/, 2026-11-03]; retrieval $0.03/GB | [sourced: same feed, "Glacier Instant Retrieval Storage" = 0.004, "Object Retrieval in Glacier Instant Retrieval per GB" = 0.03] |
| AWS S3 Glacier Deep Archive | $0.00099 | $0.099 | $0.495 | as above | 180-day min (AWS page); retrieval $0.02/GB standard, $0.0025/GB bulk | [sourced: same feed — "Fee for Standard Retrieval of data stored from Glacier Deep Archive" = 0.02, "Bulk" = 0.0025; the $0.00099 storage rate appears in the feed as the Intelligent-Tiering "DeepArchiveAccess" tier (rate code 82TFRVR9729PGTNP); the plain Deep Archive storage SKU is keyed by an opaque hash in the feed, so the class rate is cross-checked against [sourced-secondary: https://www.cloudzero.com/blog/s3-pricing/, 2026-07-30] which gives the same $0.00099] |
| Cloudflare R2 Standard | $0.015 | $1.50 | $7.50 | **Free** | 10 GB-mo free; Class A $4.50/M, Class B $0.36/M; no min duration | [sourced: https://developers.cloudflare.com/r2/pricing/, page "Last updated Oct 30, 2026", fetched 2026-11-03] |
| Cloudflare R2 Infrequent Access | $0.01 | $1.00 | $5.00 | Free | 30-day min; Class A $9/M, B $0.90/M | same |
| Backblaze B2 | $6.95/TB = $0.00695 | $0.695 | $3.48 | Free up to 3× avg monthly storage, then $0.01/GB | First 10 GB free; no min duration; no min file size | [sourced: https://www.backblaze.com/cloud-storage/pricing, 2026-11-03] |
| Wasabi (pay-as-you-go) | $7.99/TB = $0.00799 | **$7.99** (1 TB min) | **$7.99** | Free (no egress/API fees) | **1 TB minimum monthly charge; 90-day minimum retention** | [sourced: https://wasabi.com/pricing, 2026-11-03] |
| Hetzner Object Storage | €6.49/mo incl. 1 TB (= €0.00634/GB at full use); €0.0087/TB-hour above (≈ €6.35/TB-mo) | €6.49 | €6.49 | 1 TB/mo included, then €1/TB | Billed hourly, cap €6.49/mo; excl. VAT | [sourced: https://www.hetzner.com/storage/object-storage/, 2026-11-03] |
| Hetzner Storage Box BX11 (1 TB) | €3.20/mo (= €0.0032/GB at full use) | €3.20 | €3.20 | Unlimited traffic | Not S3: SFTP/SCP/FTP/SMB/WebDAV only; BX21 5 TB €10.90, BX31 10 TB €20.80, BX41 20 TB €40.60 | [sourced: https://www.hetzner.com/storage/storage-box/ and https://docs.hetzner.com/storage/storage-box/general, 2026-11-03] |
| Scaleway Object Storage Multi-AZ | €0.01606 | €1.61 | €8.03 | 75 GB/mo free then €0.01/GB | Requests/ingress free | [sourced-secondary: search snapshot of https://www.scaleway.com/en/pricing/storage/ — direct fetch HTTP 403 on 2026-11-03; repair-pass retries also failed: https://www.scaleway.com/en/object-storage/ (fetched, states "No request fees" and a 750 GB/h 90-day free trial but no rates) and https://www.scaleway.com/en/docs/object-storage/faq/ (HTTP 403). Rates are internally consistent with Scaleway's published hourly × 730 convention but remain unverified against the live page] |
| Scaleway One Zone | €0.00803 | €0.80 | €4.02 | same | | same |
| Scaleway Glacier | €0.00254 | €0.25 | €1.27 | same | Restore €0.009/GB | same |
| OVHcloud Object Storage Standard (S3, incl. Local Zone) | $0.00001111/GiB-hour ≈ $0.00811/GiB-month [estimated: ×730 h] | $0.81 | $4.06 | Free ("Outgoing external traffic: Free") | GiB/hour billing, no commitment | [sourced: official price list https://us.ovhcloud.com/public-cloud/prices/, Object Storage section, 2026-11-03; the EU page https://www.ovhcloud.com/en/public-cloud/prices/ truncated before the Object Storage section on two fetches; the earlier "around $0.0081/GiB" from the use-case page https://www.ovhcloud.com/en/public-cloud/uc-backup-object-storage/ matches] |
| OVHcloud Cold Archive ("Cloud Archive" on price list) | $0.0000033/GiB-hour ≈ $0.00241/GiB-month [estimated: ×730 h] | $0.24 | $1.20 | Outgoing free; **incoming $0.0121/GB** | 180-day minimum [sourced: https://www.ovhcloud.com/en/public-cloud/cold-archive/]; retrieval fee "Yes", amount not on either page → [unknown] | [sourced: https://us.ovhcloud.com/public-cloud/prices/, 2026-11-03] |

Observations:
- Spread is ~23× between S3 Standard ($0.023) and Deep Archive ($0.00099) [estimated: 0.023 ÷ 0.00099 = 23.2], and ~3.3× between S3 Standard and B2 [estimated: 0.023 ÷ 0.00695 = 3.3]. Hot, S3-API, egress-free storage bottoms out at **B2 $0.00695/GB** (US) or **Hetzner ~€0.0063/GB** (EU, but only at full 1 TB utilization).
- Egress matters for a *portability* product: re-exporting a 100 GB library costs $9.00 on S3 (after the 100 GB free allowance, which a multi-user service exhausts immediately) [estimated: 100 GB × $0.09], and $0 on R2/B2/Wasabi/OVH.
- Wasabi's 1 TB minimum and 90-day retention make it unsuitable below ~1 TB aggregate; irrelevant at scale.
- Cold classes (Glacier IR/Deep Archive, OVH Cold Archive, Scaleway Glacier) cut cost 4–23× but have 90–180-day minimums and retrieval fees; viable for originals if the product serves thumbnails/previews from hot storage and originals rarely.

### Q2. Reference user: what is 100 GB?

Inputs:
- Apple: "The file size of a ProRAW image at 12 MP resolution is approximately 25 MB and approximately 75 MB at 48 MP" and "ProRAW files are 10 to 12 times larger than HEIF or JPEG files." [sourced: https://support.apple.com/119916, published 2024-04-19]
- Therefore a 12 MP HEIF ≈ 25/12 … 25/10 = **2.1–2.5 MB**; a 48 MP HEIF ≈ 75/12 … 75/10 = **6.3–7.5 MB** [estimated: derived from the two Apple statements above].
- Apple states only that HEIF/HEVC "offer better compression than JPEG and H.264, so they use less storage space" — no percentage [sourced: https://support.apple.com/116944, 2026-11-03]. Apple publishes no per-model average photo size: **[unknown]** at the primary level.
- HEIC vs JPEG, secondary (fetched 2026-11-03): "A typical 12-megapixel HEIC photo occupies 1-3 MB"; "A 48-megapixel HEIC photo from a Pro model occupies 3-5 MB"; "A typical 12-megapixel JPEG photo occupies 3-6 MB"; "A 48-megapixel JPEG occupies 8-12 MB"; HEIC "consistently 50-60% smaller" than JPEG [sourced-secondary: https://www.heicify.com/guides/iphone-photo-formats-guide, 2026]. Per model: iPhone 17 default 24 MP HEIC "around 2–3 MB", full 48 MP HEIC "approximately 3–5 MB", 12 MP HEIC "1–2 MB", "HEIC files are roughly 40–50% smaller than equivalent JPEGs", ProRAW "25–50 MB" (page attributes these to Apple documentation but gives no Apple URL; some of its figures are self-described "editorial estimates, not measured data") [sourced-secondary: https://dblabsapps.com/statistics/iphone-storage-photos-statistics/, 2026]. The secondary HEIC ranges (1–5 MB) sit at or below the Apple-ratio-derived range (2.1–7.5 MB); the 2.5 MB assumption below is inside both.
- Video bitrates, secondary: "1080p HD at 30fps uses only about 170 MB per minute"; "4K … 60 frames per second uses approximately 400 MB per minute"; 4K Dolby Vision "approximately 700 MB per minute"; ProRes 4K "approximately 6 GB per minute" [sourced-secondary: dblabsapps, same page]. Note the file's earlier source (phonearena, iPhone-8-era Apple settings screen) gives 4K30 HEVC ≈ 170 MB/min and 1080p30 ≈ 60 MB/min; the two secondary sources disagree on which resolution 170 MB/min belongs to. **No current Apple document was found**; the Apple Camera settings screen is the primary source but is not fetchable. We keep 170 MB/min as the central per-minute figure for "typical" iPhone video and flag it [sourced-secondary, conflicting].
- Share of library bytes that is video: no primary measurement. One secondary page states "Video occupies approximately 12% of total iPhone storage on average" and "Photos and videos typically account for 15–25% of total iPhone storage" (both self-labelled "DB Labs estimate … editorial estimates, not measured data") [sourced-secondary: https://dblabsapps.com/statistics/iphone-storage-photos-statistics/]. Taken at face value those imply video = 12 ÷ 25 … 12 ÷ 15 = **48–80% of photo+video bytes** [estimated: ratio of the two secondary figures]. Status: **[unknown]** at any rigorous level; the 50% central assumption below is at the bottom of that secondary range.
- Photos per person per month: US "20.2 photos per day" [sourced: https://photutorial.com/photos-statistics/, updated 2026-09-26; page states the figure covers "individuals who actively take photos" and that several of its numbers are extrapolated from 2013 statistics scaled by user growth — treat as an upper bound, not a per-capita average]; Rise Above Research: ~1.95 trillion photos in 2026, "more than 300 photos per year for every man, woman and child" [sourced: https://riseaboveresearch.com/rise-above-research-forecasts-a-global-surge-in-photos-captured/, 2026-02-10] = ~25/mo per capita, global, all ages; 2015 Gigaom: iOS users 182/mo, Android 111/mo [sourced-secondary via photutorial, 2015].

Reference user definition [estimated: assumptions stated]:
- Assume **50% of bytes are video** (central case; sensitivity 30%/70%; secondary evidence above suggests the true share may be higher). Assume avg photo = **2.5 MB** (12 MP HEIF-dominated library with some 48 MP/JPEG; inside the Apple-derived 2.1–2.5 MB and the secondary 1–5 MB ranges).
- 100 GB = 50 GB photos ÷ 2.5 MB = **20,000 photos** + 50 GB video ÷ 170 MB/min = **~294 min (~4.9 h) of video**.
- Sensitivity: 30% video → 28,000 photos + 176 min; 70% video → 12,000 photos + 412 min.
- Items to index: 20,000 photos + video keyframes at **1 frame / 10 s** [estimated: assumption — one sampled frame per 10 s of video is a common indexing cadence; no source] = 294 × 6 = 1,764 frames → **~22,000 images to index** [estimated].
- New photos per month: **200** [estimated: judgment — anchored on the only per-device *measured* figure, Gigaom-2015 iOS 182/mo, rounded up for 2026 burst/live-photo behaviour; Photutorial's ~600/mo is for active takers and extrapolated from 2013 data so is treated as an upper bound; Rise Above's ~25/mo is a global all-ages per-capita lower bound]. At 200/mo, 20,000 photos ≈ 8 years of shooting.

### Q3. One-time indexing cost per reference user (22,000 images)

Compute prices used:
- RunPod: RTX 4090 $0.34/hr community, $0.89/hr secure; RTX A5000 $0.16/$0.27; L4 $0.44/$0.59; L40S $0.79/$1.09; A100 PCIe $1.19/$1.79; H100 SXM $2.69/$3.99 [sourced: https://www.runpod.io/pricing, 2026-11-03]
- Modal: T4 $0.000164/s ($0.59/hr), L4 $0.000222/s ($0.80/hr), A10 $0.000306/s ($1.10/hr), L40S $0.000542/s ($1.95/hr), A100-80GB $0.000694/s ($2.50/hr), H100 $0.001097/s ($3.95/hr); CPU $0.0000131/core-s ($0.047/core-hr); memory $0.00000222/GiB-s [sourced: https://modal.com/pricing, 2026-11-03]
- Lambda: A10 $1.29/hr, A100-40GB $1.99, H100 PCIe $3.29, H100 SXM $4.29, cheapest Quadro RTX 6000 $0.69 [sourced: https://lambda.ai/service/gpu-cloud, 2026-11-03]
- Replicate: CPU $0.36/hr, T4 $0.81/hr, L40S $3.51/hr, A100-80GB $5.04/hr, H100 $5.49/hr [sourced: https://replicate.com/pricing, 2026-11-03]; hosted CLIP embedding model `andreasjansson/clip-features`: "approximately $0.00022 per run" (~4,545 runs/$), Nvidia T4, "predictions usually finish in about 1 second" [sourced: https://replicate.com/andreasjansson/clip-features, 2026-11-03]
- Hetzner Cloud (all excl. VAT): CX33 (4 vCPU, 8 GB, 80 GB NVMe) **€0.0144/hr, €8.99/mo cap**; CX23 (2/4/40) €0.0096/hr, €5.99; CX43 (8/16/160) €0.0264/hr, €16.49; CPX12 (1 vCPU/2 GB/40 GB) €0.0192/hr, €11.99; CPX22 (2/4/80) €0.0320/hr, €19.99; CCX13 (2 dedicated/8 GB/80 GB) €0.0697/hr, €43.49. **On 2026-11-03 every CX, CAX, CPX and CCX plan on all three Hetzner pages showed "This product is currently unavailable. Please check back later."** [sourced: https://www.hetzner.com/cloud/cost-optimized/, https://www.hetzner.com/cloud/regular-performance/, https://www.hetzner.com/cloud/general-purpose/, 2026-11-03]. Hetzner prices are therefore used only as a *list-price* reference; the orderable baseline is DigitalOcean below.
- DigitalOcean Basic Droplets (orderable): 2 vCPU/2 GiB/60 GiB $18/mo ($0.02679/hr); 2 vCPU/4 GiB/80 GiB $24/mo; **4 vCPU/8 GiB/160 GiB $48/mo ($0.07143/hr)** [sourced: https://www.digitalocean.com/pricing/droplets, 2026-11-03]

(a) CLIP/SigLIP embeddings
- Throughput, batch 1: ViT-B-16-SigLIP **152 img/s**, ViT-B-16 150, ViT-B-32 170, ViT-L-14 54, ViT-SO400M-14-SigLIP 50 img/s on an RTX 3090, one image per call, precision unstated; SigLIP-512 42 img/s [sourced: https://gist.github.com/TACIXAT/ecd4f636bf6af28cb69d641e29d7b362, last active 2026-01-15].
- Throughput, batched (verified in repair pass): SigLIP 2 Base **3.0 ms/photo at GPU batch 32 on an RTX 4090 (~333 img/s)** vs 176 ms/photo on CPU batch 8 (Ryzen 9 9950X, ~5.7 img/s); So400m 24.7 ms GPU / 1,639 ms CPU. The same PR reports **end-to-end indexing** of 352 mixed photos at "Normal pace" of 1,752 photos/min (~29 img/s) GPU vs 389/min CPU for SigLIP 2 Base — i.e. the full pipeline (read, decode, resize, write) runs ~11× slower than the bare tower [sourced: https://github.com/storytold/lightcraft/pull/1611, open PR by bitshiftza, fetched 2026-11-03; wgpu compute kernels, pace possibly throttled].
- CPU: SigLIP-2 ONNX INT8 embedder "~130 ms" per image (~7.7 img/s, CPU unstated) [sourced-secondary: https://github.com/Berkaybbayramoglu/siglip-onnx-embedder]; Mac LiteRT 16.7 ms/img at batch 8 (~60 img/s, Apple silicon) [sourced-secondary: huggingface.co/Kairoi-LLC/siglip2-base-patch16-224-litert].
- Cost, GPU (RunPod 4090 community $0.34 / secure $0.89):
  - bare tower, batch 1 (152 img/s): 22,000 ÷ 152 = 145 s = 0.040 hr → **$0.014 / $0.036** [estimated].
  - bare tower, batch 32 (333 img/s): 0.018 hr → $0.006 / $0.016 [estimated].
  - **×3 overhead factor** [estimated: assumption covering image read + JPEG/HEIC decode + resize + result write, which the bare-tower benchmarks exclude; chosen as a round middle between 1× (tower only) and the 11× end-to-end slowdown lightcraft measured] → **$0.04–$0.11** on batch-1 figures; $0.02–$0.05 on batch-32 figures.
  - end-to-end at lightcraft's measured 29 img/s: 0.21 hr → **$0.07 / $0.19** [estimated: 22,000 ÷ 29.2 ÷ 3,600 × RunPod rates] — a sourced upper bracket for the overhead assumption.
  - Modal L4 ($0.80/hr): no sourced SigLIP throughput on L4 was found; **assume 83 img/s = ¼ of the 4090 batch-32 figure** [estimated: assumption, untested] → 0.074 hr → $0.06; ×3 → **$0.18** [estimated].
  - Replicate per-run hosted CLIP (unbatched, ~1 s/run on T4): 22,000 × $0.00022 = **$4.84** [estimated: 22,000 × sourced per-run price] — shows that per-call hosted inference is ~50–100× the batched cost.
- Cost, CPU: at 7.7 img/s → 0.79 hr; at lightcraft's 5.7 img/s → 1.08 hr. Hetzner CX33 list price €0.0144/hr → **€0.011–0.016**; DigitalOcean 4 vCPU $0.07143/hr → **$0.06–0.08**; Modal 2 cores $0.094/hr → **$0.07–0.10** [estimated].

(b) VLM caption per image via API
Assumptions [estimated]: image downscaled to 768×768; 50-token prompt; 80-token caption output. Official image-token rules:
- Gemini 2.5-generation: "Images ≤384 pixels in both dimensions count as 258 tokens. Larger images are tiled into 768x768 pixel tiles, each counting as 258 tokens." [sourced: https://aistudio.google.com/docs/tokens, 2026-11-03]. The tokens page does not say which models the rule applies to.
- **Gemini 3.x/4 generation uses a different rule**: per-image tokens are set by `media_resolution` — `low` 280, `medium` 560, `high` 1,120, `ultra_high` 2,240, and the default (`unspecified`) is **1,120**; the page states the default's token count "varies significantly between Gemini 4/3 and earlier Gemini models" [sourced: https://aistudio.google.com/docs/media-resolution, 2026-11-03]. All Gemini 3.x rows below are therefore computed at both `low` (280) and default (1,120); the prior version of this file wrongly applied 258/tile to 3.x.
- OpenAI patch models: `patch_count = ceil(width/32)×ceil(height/32)` × model multiplier; multipliers: gpt-5.4-nano **1.2**, gpt-5.4-mini **1.2**, gpt-5.6-luna 1.2, gpt-5.5/5.4/5.2 1.2, gpt-6-astra 1.2, gpt-5-mini 1.2 (**deprecated, "scheduled for shutdown"**), gpt-5-nano 1.5 (**deprecated**), gpt-4.1-mini 1.62, gpt-4.1-nano 2.46 (**deprecated**); cap 30,000 patches/image [sourced: https://developers.openai.com/api/docs/guides/images-vision, 2026-11-03]. 768×768 → 576 patches → 692 tokens at ×1.2, 864 at ×1.5, 934 at ×1.62. **gpt-6-luna is not in the multiplier table → its image cost is [unknown].**
- Claude: "Each patch is a 28×28-pixel block … costs ⌈width/28⌉ × ⌈height/28⌉ visual tokens"; Standard tier (all models before 4.7) max 1,568 px long edge / 1,568 tokens; High-resolution tier (Claude 4.7 and later, which includes Haiku 5.5) max 2,576 px / 4,784 tokens; a 768×768 or 1000×1000 image is "Not resized" on either tier, so 768 px → 784 tokens and 1000 px → 1,296 tokens on both Haiku 4.5 and Haiku 5.5 [sourced: https://platform.claude.com/docs/en/build-with-claude/vision, 2026-11-03].
- Prices per 1M tokens (standard / batch = 50% off): Gemini 2.5 Flash-Lite $0.10/$0.40; Gemini 2.5 Flash $0.30/$2.50 (deprecated; from 2026-12-01 routes to Gemini 3.5 Flash-Lite at the same $0.30/$2.50); Gemini 3.1 Flash-Lite $0.25/$1.50; Gemini 3 Flash Preview $0.50/$3.00; Gemini 3.6/3.8 Flash $0.75/$3.75 through 2026-12-31 then $1.50/$7.50 [sourced: https://aistudio.google.com/docs/pricing, 2026-11-03]. OpenAI: gpt-5-nano $0.05/$0.40 (deprecated); gpt-5-mini $0.25/$2.00 (deprecated); gpt-4.1-mini $0.40/$1.60; **gpt-5.4-nano $0.20/$1.25**; gpt-5.4-mini $0.75/$4.50; gpt-5.6-luna $0.20/$1.20; gpt-6-luna $0.10/$0.50; batch = half [sourced: https://developers.openai.com/api/docs/pricing, 2026-11-03; gpt-4.1-nano no longer listed]. Claude: **Haiku 5.5 $0.10/$0.50 for prompts ≤100k tokens** ($0.50/$2.50 above 100k), batch $0.05/$0.25; Haiku 4.5 $1/$5, batch $0.50/$2.50 [sourced: https://platform.claude.com/docs/en/about-claude/pricing, 2026-11-03].

| Model (768 px unless noted; 50-tok prompt; 80-tok caption) | Image tok | Input tok | $/image std | 22,000 std | 22,000 batch | Status |
|---|---|---|---|---|---|---|
| Gemini 2.5 Flash-Lite | 258 | 308 | $0.0000628 | **$1.38** | **$0.69** | live |
| GPT-5-nano (×1.5) | 864 | 914 | $0.0000777 | $1.71 | $0.85 | **deprecated** |
| Claude Haiku 5.5 (784 tok) | 784 | 834 | $0.000123 | **$2.71** | **$1.36** | live |
| Gemini 2.5 Flash-Lite at 1536 px (4 tiles) | 1,032 | 1,082 | $0.000140 | $3.08 | $1.54 | live |
| Claude Haiku 5.5 at 1000 px (1,296 tok) | 1,296 | 1,346 | $0.000175 | $3.84 | $1.92 | live |
| Gemini 3.1 Flash-Lite, media_resolution=low | 280 | 330 | $0.000203 | $4.46 | $2.23 | live (3.x tokenization) |
| GPT-5.6-luna (×1.2) | 692 | 742 | $0.000244 | $5.38 | $2.69 | live |
| **GPT-5.4-nano (×1.2)** | 692 | 742 | $0.000248 | **$5.46** | **$2.73** | live |
| Gemini 2.5 Flash (258) — until 2026-11-30 | 258 | 308 | $0.000292 | $6.43 | $3.22 | deprecated → 3.5 Flash-Lite |
| Gemini 3.5 Flash-Lite, low | 280 | 330 | $0.000299 | $6.58 | $3.29 | live from 2026-12-01 |
| GPT-5-mini (×1.2) | 692 | 742 | $0.000346 | $7.60 | $3.80 | **deprecated** |
| Gemini 3 Flash Preview, low | 280 | 330 | $0.000405 | $8.91 | $4.46 | live |
| Gemini 3.1 Flash-Lite, default (1,120) | 1,120 | 1,170 | $0.000413 | $9.07 | $4.54 | live |
| GPT-4.1-mini (×1.62) | 934 | 984 | $0.000522 | $11.48 | $5.74 | live |
| Gemini 3.5 Flash-Lite, default | 1,120 | 1,170 | $0.000551 | $12.12 | $6.06 | from 2026-12-01 |
| Gemini 3 Flash Preview, default | 1,120 | 1,170 | $0.000825 | $18.15 | $9.07 | live |
| GPT-5.4-mini (×1.2) | 692 | 742 | $0.000917 | $20.16 | $10.08 | live |
| Claude Haiku 4.5 (784 tok) | 784 | 834 | $0.001234 | $27.15 | $13.57 | live, superseded by 5.5 |
| Claude Haiku 4.5 at 1000 px | 1,296 | 1,346 | $0.001746 | $38.41 | $19.21 | live, superseded |

All rows [estimated: official per-token prices × official image-token formulas × stated assumptions]. If gpt-6-luna's multiplier were 1.2 it would cost ~$2.51/22k std, but its multiplier is **[unknown]** (absent from the vision guide), so it is not a row. Moondream Cloud is priced per token ($0.30/$1.00 per M, batch $0.15/$0.50 for Moondream 3.1 9B-A2B) but its image-token count is **[unknown]** [sourced: https://moondream.ai/pricing, 2026-11-03].

Takeaway (changed by the repair): the cheapest *live, non-deprecated* captioning options in Nov 2026 are Gemini 2.5 Flash-Lite ($0.69 batch) and **Claude Haiku 5.5 ($1.36 batch / $2.71 std)**; the cheapest current OpenAI small model (gpt-5.4-nano) is ~$2.73 batch. Gemini 3.x models cost 3–13× more per image than 2.5 Flash-Lite mainly because of the 1,120-token default image size, not the per-token price.

Local VLM alternatives:
- Qwen2.5-VL-3B on SaladCloud (TGI, 10 replicas): 33 img/s on RTX 3090 cluster at $1.16/hr (102,413 images per $ → $0.0098/1k); 51.4 img/s on RTX 4080 at $1.46/hr ($0.0079/1k); 7B: $0.0116–0.0178/1k; max_tokens 256, resolution unstated [sourced: https://blog.salad.com/qwen-benchmark, 2025-03-21]. → 22,000 images = **$0.17–$0.33** [estimated].
- Florence-2-large ~150 ms/image (hardware unstated) [sourced-secondary: https://botmonster.com/ai/run-vision-models-locally-florence-2-qwen-vl/] → 6.7 img/s → 0.92 hr → **$0.31** (4090 community) to $0.82 (secure) [estimated].
- Moondream: throughput **[unknown]** — searched: HF model card https://huggingface.co/vikhyatk/moondream2 (2B params, "20–40% faster response generation", no img/s), Moondream 3 Preview post https://moondream.ai/blog/moondream-3-preview (9B MoE / 2B active, "inferences are much slower than anticipated", no figures), https://moondream.ai/pricing (no latency figures); earlier: "doesn't handle batching", 184 tok/s int4 on RTX 3090 [sourced-secondary: medium.com/@geronimo7].

(c) OCR
- Tesseract (license-free). Sourced timing: on a single dense Hindi *page* on an HP Z420 workstation, LSTM engine with OpenMP+AVX = **1.8 s real / 3.8 s CPU**; without OpenMP 2.7 s; legacy engine 2.9 s; the LSTM engine uses "the order of ten times the CPU resources of the base Tesseract" [sourced: https://tesseract-ocr.github.io/tessdoc/tess4/4.0-Accuracy-and-Performance.html and https://tesseract-ocr.github.io/tessdoc/tess4/NeuralNetsInTesseract4.00.html, undated, Tesseract 4.0 era]. Consumer photos contain far less text than a full page and are downscaled, so **assume 1 s CPU/image** [estimated: assumption bracketed by the 1.8–3.8 s/page figure above; no photo-specific benchmark found] → 22,000 s = 6.1 hr → Hetzner CX33 list **€0.09**; DigitalOcean 4 vCPU **$0.44**; Modal 2-core **$0.57** [estimated].
- Cloud OCR, sourced: AWS Textract DetectDocumentText **$0.0015/page** first 1M, $0.0006 after (US West example); 1,000 pages/mo free [sourced: https://aws.amazon.com/textract/pricing/, 2026-11-03]. Google Cloud Vision TEXT_DETECTION: the page https://cloud.google.com/vision/pricing rendered only 76 characters of text on two fetches (JS-only) and the Document AI page https://cloud.google.com/document-ai/pricing likewise; the Azure Computer Vision page https://azure.microsoft.com/en-us/pricing/details/cognitive-services/computer-vision/ rendered "$-" placeholders. Google Vision's commonly cited $1.50/1,000 (1,001–5M) and $0.60/1,000 (>5M) is **[unverified: not fetched; recalled; not used in any calculation]**. All cloud-OCR arithmetic below uses Textract.
- Full library via cloud OCR: 22,000 × $0.0015 = **$33**; if only the **20%** of images that a cheap text detector flags [estimated: assumption; the true fraction of consumer photos containing legible text is [unknown]] → **$6.60**. A VLM caption pass (Gemini/GPT/Claude) already transcribes visible text, so OCR is usually $0 marginal at mid/high tiers.

(d) Face detection + embedding + clustering
- RetinaFace + ArcFace pipeline (InsightFace-style): median 12.8 ms/image, ~78 img/s on RTX 2070 SUPER; ~102 ms/image, ~9.8 img/s on CPU; 640×640 synthetic input, 30 iterations [sourced-secondary: https://github.com/sudolulo/winnow/wiki/Benchmarks]. InsightFace guidance: MobileFaceNet-class "thousands of embeddings per second" at batch 32 FP16, ResNet100-class "low hundreds" [sourced: https://www.insightface.ai/guides/choose-face-recognition-model-and-evaluate, 2026-11-03].
- GPU: 22,000 ÷ 78 = 0.078 hr → **$0.027** (4090 community) / **$0.070** (secure). CPU: 0.62 hr → Hetzner CX33 list **€0.009**; DigitalOcean **$0.045**; Modal **$0.06** [estimated]. Clustering (HDBSCAN on ~30k 512-d vectors) is seconds of CPU — negligible [estimated]. Faces per photo assumed **1.5** [estimated: assumption; no sourced figure].

Per-100 GB one-time indexing table (22,000 images). Each cell is a row computed above; the tier only selects *which* row:

| Tier | Embeddings | Faces | OCR | Captions | **Total one-time** |
|---|---|---|---|---|---|
| Low (local models, RunPod 4090 community $0.34, no VLM) | $0.04 (batch-1 ×3) – $0.07 (lightcraft end-to-end) | $0.03 | Tesseract $0.09 (CX33 list) | none | **~$0.16–0.19** |
| Mid (as Low + cheapest live caption pass at 768 px) | $0.04–0.07 | $0.03 | $0 (in-caption) – $0.09 | Qwen-3B local $0.17–0.33, Gemini 2.5 Flash-Lite batch $0.69, or Haiku 5.5 batch $1.36 | **~$0.33–$1.5** (central ~$0.85 with Flash-Lite batch) |
| High (secure-cloud GPU $0.89; current-generation caption model std tier; cloud OCR on 20%) | $0.11 (batch-1 ×3) – $0.19 (end-to-end) | $0.07 | Textract $6.60 | Haiku 5.5 1000 px $3.84, GPT-5.4-nano $5.46, or Gemini 3.1 Flash-Lite default $9.07 | **~$10.6–$15.9** |
| Max (legacy-price worst case: Haiku 4.5 std at 1000 px, or Gemini 3 Flash default; full-library cloud OCR) | $0.19 | $0.07 | Textract $33 | $18.15 (Gemini 3 Flash) – $38.41 (Haiku 4.5) | **~$51–$72** |

[estimated: sums of the rows above]. The "Max" row is retained only to show the cost of not choosing models; with Haiku 5.5 on the pricing page the Claude price point is in the Mid band, not Max.

### Q4. Ongoing cost per user per month

- New media: at 200 photos/mo [estimated, see Q2] × 2.5 MB = 0.5 GB photos; with video at an equal byte share → **~1 GB/mo library growth** → +12 GB/yr → +$0.18/mo on R2 after one year, +$0.08 on B2 [estimated: 12 GB × rate].
- Incremental indexing of ~220 images/mo [estimated: 200 photos + ~20 video keyframes]: mid tier $0.69 ÷ 22,000 × 220 = **$0.007/mo**; high tier ~$12 ÷ 22,000 × 220 = **$0.12/mo** [estimated].
- Vector storage: 512-dim float32 = 2,048 B + HNSW neighbor pointers/tuple overhead ≈ **2.3 KB/vector** [sourced-secondary: https://dev.to/multigrid/choosing-and-tuning-a-pgvector-index-1hki formula, applied to d=512, m=16] → 22,000 image vectors = 51 MB; faces at 1.5 faces/photo = 33,000 × 2.3 KB = 76 MB [estimated] → **~127 MB per user**.
  - pgvector on a 4 vCPU / 8 GB / 80 GB box (Hetzner CX33 list €8.99 — **not orderable 2026-11-03**): RAM-resident users = (8 GB − ~1.5 GB for OS + Postgres shared buffers/overhead [estimated: assumption]) ÷ 127 MB ≈ **~50 users** → €0.18/user/mo; disk-resident with per-user partitions: usable disk = 80 GB − ~20% for OS, WAL and headroom [estimated: assumption] = **64 GB** ÷ 127 MB ≈ **~500 users** → **€0.018/user/mo** [estimated].
  - **Orderable baseline — DigitalOcean 4 vCPU/8 GiB/160 GiB $48/mo**: ~50 users RAM-resident → $0.96/user; disk-resident 128 GB usable [estimated: same 20% haircut] ÷ 127 MB ≈ 1,000 users → **$0.05/user/mo** [estimated]. This $0.05 figure is used in Q7.
  - Pinecone Standard: $0.33/GB-mo storage, reads $16–18/M units, writes $4–4.50/M, **$50/mo minimum**; Starter free up to 2 GB/5 indexes [sourced: https://www.pinecone.io/pricing/, 2026-11-03] → 0.127 GB × $0.33 = **$0.042/user/mo** + minimum.
  - turbopuffer: storage ≤$0.33/GB, writes ≤$2.00/GB (10 KB min/write; 50% batch discount at ~3.2 MB), queries billed on data scanned (1.28 GB min) + returned; Launch **$16/mo min**, Scale $256 [sourced: https://turbopuffer.com/pricing, 2026-11-03] → $0.042/user/mo storage + $0.25 one-time write [estimated: 0.127 GB × $2].
- Query cost: SigLIP text-tower embedding of a query on CPU is milliseconds — negligible [estimated]. If *we* host an LLM chat layer: assume **~3,000 input + 300 output tokens/query** [estimated: assumption — a system prompt plus ~20 retrieved captions/metadata rows and a short answer] on Gemini 2.5 Flash-Lite = $0.0003 + $0.00012 = **$0.00042/query**; at **100 queries/mo** [estimated: assumption] = **$0.04/mo** [estimated]. If the corpus is exposed via MCP to the user's own assistant (BYO-AI wedge), LLM cost is **$0 to us** — the assistant vendor bills the user.

### Q5. Market price points (USD/mo unless noted)

| Product | Plan | $/mo | GB | $/GB-mo | Source |
|---|---|---|---|---|---|
| Apple iCloud+ | 50 GB / 200 GB / 2 TB / 6 TB / 12 TB | $0.99 / $2.99 / $9.99 / $29.99 / $59.99 | 50 / 200 / 2,000 / 6,000 / 12,000 | $0.0198 / $0.0150 / $0.0050 / $0.0050 / $0.0050 | [sourced: https://support.apple.com/en-us/108047, page dated 2026-09-16, fetched 2026-11-03] |
| Google One | Basic / AI Plus / AI Pro / AI Ultra | $1.99 / $4.99 / $19.99 / [unknown] | 100 / 400 / 5,000 / "starting at 20 TB" | $0.0199 / $0.0125 / $0.0040 / — | Storage sizes [sourced: https://one.google.com/about/google-ai-plans/, 2026-11-03 — page shows "400 GB storage", "5 TB storage", "Starting at 20 TB" but renders prices as blank "/mo"]; **prices [sourced-secondary: aggregator sites citing one.google.com, 2026-10]**. Official price fetch attempts (all failed to render prices): one.google.com/about/plans (×2 variants), /about/google-ai-plans/, /about/google-ai-pro/ (404), /about/basic/ (404), support.google.com/googleone/answer/9004014 (no prices), blog.google/products/google-one/google-ai-plus/ (404). The earlier "400 GB vs 2 TB" conflict for AI Plus is resolved: **400 GB** per the official plans page. |
| Ente Photos | Free 10 GB; 50 GB $2.49 ($29.88/yr); 200 GB $4.99 ($59.88/yr); 1 TB $9.99 ($119.88/yr); 2 TB $19.99 ($239.88/yr); up to 5 family members share storage free | $2.49 / $4.99 / $9.99 / $19.99 | 50 / 200 / 1,000 / 2,000 | $0.0498 / $0.0250 / $0.0100 / $0.0100 | [sourced: https://ente.com/pricing, 2026-11-03] |
| Immich | Self-hosted, free; **no hosted offering**. FUTO "started building an encrypted backup service this year and they plan to integrate it directly into Immich", closed beta "later this year", no price | — | — | — | [sourced: https://immich.app/blog/2026-march-recap, 2026-03-31] |
| PhotoPrism | Essentials and Plus, **self-hosted (no storage)**, "billed annually". The editions page is internally inconsistent: hero shows "€ 200 / mo" and "from € 600 / mo", comparison table shows "€ 2.00 / mo" and "from € 6.00 / mo" — a rendering bug; the table values (€2 / €6) are the plausible ones and are what we use, flagged. PikaPods managed hosting from $6.50/mo | €2 / €6 (table) | 0 (self-hosted) | — | [sourced: https://www.photoprism.app/editions, 2026-11-03] |
| Mylio Photos+ | ~$9.99/mo or $99–$119.99/yr, no included cloud; SecureCloud optional, price **[unknown]** | ~$9.99 | 0 | — | [sourced-secondary: reviewed.com; community.mylio.com FAQ (403)]. Official fetch attempts 2026-11-03: mylio.com/pricing/ (only "Get Special Offer" buttons, no amounts), /mylio-photos-plus/ (no prices), /plans/ (no prices), /secure-cloud-storage/ (404). Mylio does not publish list prices on its site. |
| Amazon Photos | Prime: unlimited full-res photos + 5 GB video; 100 GB $1.99 ($19.99/yr); 1 TB $6.99 ($59.99/yr); 2 TB $11.99 ($119.98/yr) | $1.99 / $6.99 / $11.99 | 100 / 1,000 / 2,000 | $0.0199 / $0.0070 / $0.0060 | [sourced-secondary: https://www.whistleout.com/CellPhones/Guides/amazon-photo-storage and https://whichonetho.io/provider/amazon-photos, May 2026]. Official fetch attempts 2026-11-03 all HTTP 503: amazon.com/photos/storage (×2), /b?node=13234696011, /photos/pricing, /clouddrive/pricing. |
| FOREVER | One-time: 10 GB $179.99 ($18/GB); 100 GB $899.99 ($9/GB); 1 TB $5,999.99 ($6/GB); 2 TB $10,999.99 ($5.50/GB) | one-time | 10–2,000 | — | [sourced: https://www.forever.com/pricing, 2026-11-03] |
| Permanent.org | One-time $10/GB; 1 GB free; fees go to an endowment | one-time | — | — | [sourced: https://www.permanent.org/why-permanent/, 2026-11-03] |
| Backblaze Computer Backup | **$9/mo monthly; $8.25/mo paid annually ($99/yr); $7.88/mo on the 2-year plan ($189)**; unlimited | $9.00 / $8.25 / $7.88 | unlimited | — | [sourced: https://www.backblaze.com/cloud-backup (monthly/2-year) and https://www.backblaze.com/cloud-backup/pricing ($99/yr), 2026-11-03] |
| Dropbox Plus | "$9.99 / month", 2 TB. The plans page has a "Billed monthly / Billed yearly" toggle but the fetched text shows only the one figure; which cycle it belongs to is **[unknown]** from the page (dropbox.com/plus and /buy/plus and help.dropbox.com/plans/dropbox-plus show no price) | $9.99 | 2,000 | $0.0050 | [sourced: https://www.dropbox.com/plans, 2026-11-03] |

Takeaway: the incumbent anchor is **$0.005/GB-mo at 2 TB** (Apple, Dropbox) and $0.004 at 5 TB (Google AI Pro, secondary price) — below B2's raw cost ($0.00695) and a third of R2. Privacy/indie anchors (Ente) sit at **$0.010–0.025/GB-mo**. A 200 GB-class tier clears at $2.99–$4.99 in market.

### Q6. Churn / retention benchmarks

- Backblaze Computer Backup (consumer-ish backup, $99/yr): **gross customer retention 91%** in Q4 2025 (90% Q4 2024), i.e. ~9% annual customer loss; Computer Backup NRR 98% (109%); customers 402,589 vs 417,845 (−3.7% YoY); ARR $65.5M "flat YoY" [sourced: https://ir.backblaze.com/news/news-details/2026/Backblaze-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results/default.aspx, 2026-02-23]. **Q1 2026**: Computer Backup gross retention 91% (90% Q1 2025), Computer Backup NRR **95%** (103%), overall NRR 103% (105%) [sourced: https://ir.backblaze.com/news/news-details/2026/Backblaze-Announces-First-Quarter-2026-Financial-Results/default.aspx, 2026-05-04]. 10-K FY2025 (fetched 2026-11-03): Computer Backup gross retention 91%/90%/91% (2025/2024/2023), customers 402,589/417,845/431,745, ARPU $163/$159/$140; B2 gross retention 89%/89%/90%; total NRR 105%/116%/109%; definition: trailing-four-quarter average of (accounts with revenue in the last month of the quarter that also had revenue in the prior-year quarter) ÷ (accounts in that prior-year quarter); and, critically for the life calculation below: **"the significant majority of our customers have subscription terms of one year or longer"** [sourced: https://www.sec.gov/Archives/edgar/data/1462056/000162828026016395/blze-20251231.htm, filed 2026]. Reconciliation: 91% gross retention and a 3.7% customer decline are consistent only if gross adds ≈ 5% of base — Backblaze is a mature, barely-growing consumer base.
- Dropbox FY2025 10-K: paying users **18.08M vs 18.22M** (−0.8%); ARPU $138.91 vs $140.23; ARR $2,526M vs $2,574M; "over 90% of revenue comes from self-serve channels"; only qualitative retention statement: "We saw better than expected improvements in customer retention and engagement, particularly across our Individual plans." No churn rate disclosed [sourced: https://www.sec.gov/Archives/edgar/data/1467623/000146762326000008/dbx-20251231.htm, filed 2026-02]. Implied churn cannot be derived: churn = gross adds + 0.8% net loss, and gross adds are not disclosed → **[unknown]**.
- Ente: publishes an open metrics dashboard since 2026-07-01 ("Ente's business metrics are open now", https://ente.com/blog/open/). Dashboard values visible on fetch: Jan 2026 — revenue "from active Ente subscriptions" $780,996 (annual view), paid customers 12,018, registered accounts 290,703; later unlabeled values $1,413,012 / 21,807 / 490,639 (the page's latest month; label not captured) [sourced: https://ente.com/open, fetched 2026-11-03]. Implied revenue per paid customer ≈ $65/yr ≈ $5.4/mo [estimated: 780,996 ÷ 12,018]. **No churn or retention metric is published** → Ente churn [unknown], but Ente's paid base roughly doubled Jan→latest month 2026 [estimated: 21,807 ÷ 12,018 = 1.8×, if the unlabeled figures are the latest month].
- RevenueCat State of Subscription Apps 2026 (115,000+ apps, >$16B revenue; report published 2026-03-19; the underlying cohort data run through 2025 and the report labels its latest cohorts "2026"):
  - Median **first annual renewal: Photo & Video 23%** (lowest, tied with Productivity); Travel/Business 40%, Utilities 35%, Media & Ent. 37% [sourced: https://www.revenuecat.com/blog/growth/average-subscription-renewal-rates-by-app-category, updated 2026-04-24].
  - Median **first monthly renewal: Photo & Video 48%** (second-lowest; Business 61%, Utilities 57%) [same].
  - Annual-plan Y1 retention overall: freemium 28%, hard paywall 27%. The same source states the complement as Y1 cancellations: "~56% … in 2025, while this worsened to ~72% in 2026" — note this is the *same* datapoint as the 27–28% retention, not an independent one; first month = 35% of all annual cancellations [sourced: https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026, 2026-03-19].
  - Trial-to-paid: Photo & Video **22.2%** (lowest category); Travel 43.5% [sourced: https://www.revenuecat.com/state-of-subscription-apps, 2026].
  - Photo & Video "cancel assurance" 25.0%, ~8 pp below next-lowest [sourced: https://www.revenuecat.com/state-of-subscription-apps-2026-education].
- Genealogy: Ancestry monthly churn **3.6%** (Q4 2009), 3.8% (2011), 3.9% (2010) — company-reported pre-buyout [sourced-secondary: geneamusings.com 2010-01; fool.com 2012-02]. Repair-pass search of EDGAR: Ancestry.com LLC (CIK 1575319) filed 10-Ks through FY2015; the FY2015 10-K (https://www.sec.gov/Archives/edgar/data/1575319/000157531916000021/acom2015123110k.htm, filed 2016-02-19, fetched 2026-11-03) contains **no churn or retention rate** — only "total subscribers … increased approximately 7%" and qualitative cancellation language. Blackstone's 2020 acquisition release could not be fetched (blackstone.com 403; ancestry.com newsroom index rendered no releases). MyHeritage: **[unknown]** — private; attempted myheritage.com/blog/2021/02/… (404 ×2) and franciscopartners.com news (404); no public churn disclosure is known to exist.
- Implication — three retention regimes, and **the plan term matters as much as the category**:
  - "Backup utility, annual term" (Backblaze: ~9%/yr loss, mostly annual contracts → mean life ≈ 12 ÷ 0.09 = **133 months** [estimated: geometric, constant annual loss]; B2 at 89% → 109 months).
  - "Photo app, annual plan" (RevenueCat Photo & Video first annual renewal 23% → expected life ≈ 12 × 1/(1−0.23) = **15.6 months** [estimated: geometric series on constant renewal; applies only to annual-billed subscribers]).
  - "Photo app, monthly plan" (RevenueCat Photo & Video first monthly renewal 48% → expected life ≈ 1/(1−0.48) = **1.9 months** [estimated: geometric on constant 48% renewal — conservative, since later-month renewal is typically higher than first-month, but no later-month figure is published for the category]).
  - A storage-bearing product behaves like the first regime *only if* it becomes the system of record on an annual term; an AI-search layer sold monthly behaves like the third.

### Q7. Gross-margin model and payback

Fee inputs: Stripe 2.9% + $0.30 per card transaction [sourced: https://stripe.com/pricing, 2026-11-03]; Apple App Store Small Business Program 15% under $1M/yr [sourced: https://developer.apple.com/app-store/small-business-program/, 2026-11-03].
Fill-rate assumption: users use **50% of plan quota on the 200 GB plan, 40% on 1 TB/2 TB plans** [estimated: assumption; actual fill [unknown]].

**Convention (stated explicitly):** "Net" = gross price minus payment fees (Stripe or App Store). Contribution = Net − storage − Other COGS. **GM % = contribution ÷ gross price**, i.e. payment fees are treated as a cost of revenue and the denominator is the sticker price.

**Other COGS derivation** (per user per month; reference user = 100 GB used; B scales 4× for 400 GB used; C scales 8× for 800 GB used and has 5 querying members):
- vector DB hosting: $0.05 (DigitalOcean disk-resident pgvector, Q4) × size multiple;
- hosted-chat queries: $0.04 per querying member (Q4);
- incremental indexing: $0.007 (mid tier, Q4) × size multiple;
- onboarding indexing amortized: $0.69 (mid tier, Q3) ÷ expected life × size multiple. Two bases are shown: **annual-plan life 15.6 mo** ($0.044 per 100 GB) and **monthly-plan life 1.9 mo** ($0.36 per 100 GB).
- A: 0.05 + 0.04 + 0.007 + 0.044 = **$0.14** (annual basis) / 0.05 + 0.04 + 0.007 + 0.36 = **$0.46** (monthly basis).
- B: 0.20 + 0.04 + 0.028 + 0.177 = **$0.45** / $1.71 (monthly basis).
- C: 0.40 + 0.20 + 0.056 + 0.354 = **$1.01** / $3.53 (monthly basis).
[estimated: arithmetic on Q3/Q4 inputs]. The table uses the annual basis; the monthly basis is applied in the payback table's 1.9-month column.

| Plan | Price | Net of fees | Storage backend | Storage at assumed fill | Other COGS | Total COGS | **GM %** | Storage at full fill → GM |
|---|---|---|---|---|---|---|---|---|
| A: $4/mo, 200 GB (100 GB used) | $4.00 | $3.58 | R2 $0.015 | $1.50 | $0.14 | $1.64 | **49%** | $3.00 → 11% |
| A | | | B2 $0.00695 | $0.70 | $0.14 | $0.84 | **69%** | $1.39 → 51% |
| A | | | S3 Std $0.023 | $2.30 | $0.14 | $2.44 | **29%** | $4.60 → −29% |
| A via App Store (15%) | $4.00 | $3.40 | R2 | $1.50 | $0.14 | $1.64 | 44% | $3.00 → 7% |
| B: $10/mo, 1 TB (400 GB used) | $10.00 | $9.41 | R2 | $6.00 | $0.45 | $6.45 | **30%** | $15.00 → −60% |
| B | | | B2 | $2.78 | $0.45 | $3.23 | **62%** | $6.95 → 20% |
| B | | | S3 Std | $9.20 | $0.45 | $9.65 | **−2%** | $23.00 → −140% |
| C: Family $15/mo, 2 TB, 5 members (800 GB used) | $15.00 | $14.27 | R2 | $12.00 | $1.01 | $13.01 | **8%** | $30.00 → −112% |
| C | | | B2 | $5.56 | $1.01 | $6.57 | **51%** | $13.90 → −4% |
| **A-index-only** (originals stay in user's iCloud/Google; we store 1.1 GB thumbnails + index) | $4.00 | $3.58 | R2 | $0.02 | $0.14 | $0.16 | **86%** | — |

All rows [estimated: price inputs from Q1/Q3/Q4 × stated fill assumptions]. Thumbnails: 22,000 × **50 KB** [estimated: assumption — a ~512 px JPEG preview] = 1.1 GB [estimated].

Payback (months = CAC ÷ monthly contribution after fees and COGS; CAC itself **[unknown]** — no photo-app CAC benchmark found). Contribution uses annual-basis Other COGS except in the 1.9-month column, which uses the monthly-basis Other COGS:

| Plan / backend | Contribution /mo | CAC $10 | CAC $25 | CAC $50 | CAC $100 | Max CAC, monthly plan, 1.9-mo life (P&V 48% monthly renewal) | Max CAC, annual plan, 15.6-mo life (P&V 23% annual renewal) | Max CAC, 133-mo life (Backblaze-like 91%, annual terms) |
|---|---|---|---|---|---|---|---|---|
| A / R2 | $1.94 | 5.1 | 12.9 | 25.7 | 51 | **$3** | $30 | $258 |
| A / B2 | $2.75 | 3.6 | 9.1 | 18.2 | 36 | **$5** | $43 | $365 |
| B / R2 | $2.97 | 3.4 | 8.4 | 16.9 | 34 | **$3** | $46 | $394 |
| B / B2 | $6.19 | 1.6 | 4.0 | 8.1 | 16 | **$9** | $96 | $823 |
| A-index-only / R2 | $3.43 | 2.9 | 7.3 | 14.6 | 29 | **$6** | $53 | $456 |

[estimated: arithmetic on the rows above; 133-month life = 12 ÷ 0.09; 15.6 = 12 ÷ 0.77; 1.9 = 1 ÷ 0.52]. **Reading:** on a monthly-billed plan with category-median retention, max tolerable CAC is single-digit dollars — effectively organic-only. The annual-plan column ($30–$96) is the binding one *if* the product is sold annually (as Backblaze and Ente's /yr pricing suggest is normal), and the Backblaze column applies only once the product proves backup-grade, system-of-record retention. The earlier version of this file used the 15.6-month life for monthly-priced plans; that was a method error.

---

## 3. Seed assumptions tested

**A5 — "Unit economics of storage + embedding + VLM per user can clear a consumer price point."** Status: **PARTIAL (holds under conditions; broken in the obvious configuration).**
- Evidence for: at 200 GB/$4 with B2 or R2 and ~50% fill, GM 49–69% with a mid-tier VLM pass included; indexing is <$1.50 one-time at mid tier even with Claude Haiku 5.5 (Q3) and <$0.01/mo incremental (Q4). At 1 TB/$10 on B2, GM 62% at 40% fill and still +20% at full fill.
- Evidence against: at full fill, R2 cannot support 1 TB/$10 (−60%) or 2 TB family/$15 (−112%); S3 Standard is negative at 1 TB/$10 even at 40% fill. Incumbents price 2 TB at $9.99 = $0.005/GB-mo, below B2's $0.00695 raw cost — a pure-storage price war is unwinnable on hot storage. The price points that clear are the *200 GB-class* tiers ($2.99–$4.99 in market) or any tier where originals are not hot-stored by us.
- Falsification searched for: whether VLM/embedding could be the blocker. It is not: the "high" tier ($10.6–15.9 one-time, using current-generation models at standard price) amortizes to ~$1/mo over an annual-plan life and ~$0.7/mo even on a 15.6-month basis; only the legacy-model "max" configuration (Haiku 4.5 at 1000 px + full cloud OCR, ~$72, or Gemini 3 Flash at default resolution + full OCR, ~$51) breaks a $4 plan — and both are avoidable choices, since Haiku 5.5 is 10× cheaper than Haiku 4.5 on the same pricing page.
- New risk surfaced by the repair: on a **monthly** plan with category-median retention (48% first renewal), the expected life is ~1.9 months; onboarding indexing then amortizes at $0.36/mo rather than $0.044/mo and max CAC is $3–9. A5 "clears a price point" on gross margin but the *acquisition* economics only work on annual terms or organic acquisition.

**Founder fear — "storage company economics": is storage or indexing the dominant cost?** Status: **HOLDS — storage dominates.**
- Over a 15.6-month expected life on Plan A/R2: storage $1.50 × 15.6 = $23.40 vs indexing $0.69 one-time + $0.007 × 15.6 = $0.80 → storage is ~97% of variable infra [estimated]. On B2: $10.84 vs $0.80 → 93%. Even on a 1.9-month life (A/R2): storage $2.88 vs indexing $0.70 → 80%. Even at the high indexing tier ($12 + $1.9), storage on R2 over 15.6 months ($23) still exceeds it.
- Indexing only dominates if (a) originals are *not* stored by us (index-only Plan A: total COGS $0.16/mo, of which onboarding + incremental indexing = $0.051 = **~32%**, rising to ~64% if the vector DB is counted as indexing; hosted queries are ~25%; thumbnail storage ~10% [estimated: components ÷ $0.158]), or (b) the product insists on legacy-priced, full-resolution, non-batched captioning.
- Corollary: the "storage company" trap is a choice. An index-plus-thumbnail architecture over the user's existing iCloud/Google/Takeout storage (or a cold tier for originals: Deep Archive $0.099/100 GB, OVH Cold $0.24) moves GM from ~49% to ~86% on a $4 plan, at the cost of not being the system of record — which Q6 suggests is exactly what drives backup-grade, annual-term retention. This is the central trade-off for the variant generator.

Other assumptions in this brief: none of A1–A4, A6 are in Track D scope.

---

## 4. Numbers table (every number used, with tag)

| Number | Value | Tag |
|---|---|---|
| S3 Standard (first 50 TB) | $0.023/GB-mo | sourced AWS pricing feed (published 2026-10-15), fetched 2026-11-03 |
| S3 Glacier IR storage / retrieval | $0.004 / $0.03 per GB | sourced AWS pricing feed |
| S3 Deep Archive storage | $0.00099/GB-mo | sourced AWS feed (appears as INT DeepArchiveAccess tier; class SKU hashed) + sourced-secondary cloudzero 2026-07-30 |
| S3 Deep Archive retrieval std / bulk | $0.02 / $0.0025 per GB | sourced AWS pricing feed |
| S3 PUT / GET per 1k | $0.005 / $0.0004 | sourced AWS pricing feed |
| S3 minimum durations GIR / DA | 90 / 180 days | sourced AWS page 2026-11-03 |
| S3 egress | $0.09/GB after 100 GB/mo free | rate sourced-secondary (cloudzero); free allowance sourced AWS page |
| S3 Standard ÷ Deep Archive; ÷ B2 | 23×; 3.3× | estimated (ratios of the rows above) |
| R2 Std / IA | $0.015 / $0.01; egress free; 10 GB free | sourced Cloudflare (page updated 2026-10-30) |
| B2 | $6.95/TB; egress free ≤3× storage then $0.01/GB; 10 GB free | sourced Backblaze 2026-11-03 |
| Wasabi | $7.99/TB; 1 TB min; 90-day retention | sourced Wasabi 2026-11-03 |
| Hetzner Object Storage | €6.49/mo incl. 1 TB + 1 TB egress; €0.0087/TB-hr over | sourced Hetzner 2026-11-03 |
| Hetzner Storage Box | BX11 €3.20 (1 TB) … BX41 €40.60 (20 TB); unlimited traffic | sourced Hetzner 2026-11-03 |
| Hetzner CX23/CX33/CX43 hourly; monthly | €0.0096/€0.0144/€0.0264; €5.99/€8.99/€16.49 — all unavailable | sourced Hetzner 2026-11-03 |
| Hetzner CPX12/CPX22; CCX13 | €0.0192/€0.0320 per hr, €11.99/€19.99; €0.0697/hr €43.49 — all unavailable | sourced Hetzner 2026-11-03 |
| DigitalOcean 2v/2G; 2v/4G; 4v/8G/160G | $18; $24; $48/mo ($0.07143/hr) | sourced DigitalOcean 2026-11-03 |
| Scaleway Multi-AZ / One-Zone / Glacier | €0.01606 / €0.00803 / €0.00254; 75 GB egress free then €0.01 | sourced-secondary (search snapshot of official page; 403 on fetch, ×2) |
| OVH Standard S3 | $0.00001111/GiB-hr ≈ $0.00811/GiB-mo; egress free | sourced OVH US price list 2026-11-03; monthly = estimated ×730 |
| OVH Cold Archive | $0.0000033/GiB-hr ≈ $0.00241/GiB-mo; incoming $0.0121/GB; 180-day min | sourced OVH price list + cold-archive page 2026-11-03 |
| ProRAW 12 MP / 48 MP file size; ratio to HEIF | ~25 MB / ~75 MB; 10–12× | sourced Apple 119916 (2024-04-19) |
| HEIF 12 MP / 48 MP (Apple-derived) | 2.1–2.5 MB / 6.3–7.5 MB | estimated (Apple ratio) |
| HEIC 12 MP / 48 MP; JPEG 12 MP / 48 MP; HEIC saving | 1–3 / 3–5 MB; 3–6 / 8–12 MB; 50–60% | sourced-secondary heicify 2026 |
| iPhone 17 24 MP HEIC / 48 MP HEIC / 12 MP HEIC; HEIC vs JPEG | 2–3 / 3–5 / 1–2 MB; 40–50% smaller | sourced-secondary dblabsapps 2026 |
| Video MB/min: 170 (4K30 HEVC per phonearena; 1080p30 per dblabs); 400 (4K60); 700 (4K DV); 6,000 (ProRes 4K) | — | sourced-secondary, conflicting; central 170 used |
| Video share of total iPhone storage; photos+videos share | 12%; 15–25% | sourced-secondary dblabsapps "editorial estimates" |
| Video share of photo+video bytes | 48–80% (derived); 50% assumed (30–70%) | estimated (ratio of the two secondary figures); assumption |
| Avg photo size assumed | 2.5 MB | estimated assumption |
| Reference user | 20,000 photos + 294 min video + 1,764 keyframes = 22,000 images | estimated |
| Keyframe cadence | 1 frame / 10 s | estimated assumption |
| Photos/day US active takers | 20.2 | sourced Photutorial 2026-09-26 (extrapolated from 2013 data; upper bound) |
| Photos/yr per capita | >300 (~25/mo) | sourced Rise Above Research 2026-02-10 |
| Photos/mo iOS 2015 | 182 | sourced-secondary (Gigaom via Photutorial) |
| New photos/mo assumed; new images indexed/mo | 200; 220 | estimated (judgment anchored on Gigaom 182) |
| SigLIP-B16 throughput batch-1 | 152 img/s (RTX 3090) | sourced gist 2026-01-15 |
| SigLIP 2 Base batch-32 GPU / CPU batch-8; end-to-end | 3.0 ms (~333 img/s) / 176 ms (~5.7 img/s); 1,752 photos/min (~29 img/s) | sourced lightcraft PR #1611 (RTX 4090, Ryzen 9 9950X) |
| SigLIP CPU int8 | ~130 ms/img | sourced-secondary GitHub |
| Overhead factor | ×3 | estimated assumption (bracketed 1×–11× by lightcraft) |
| Modal L4 SigLIP throughput | 83 img/s assumed | estimated assumption (no source) |
| Replicate clip-features | $0.00022/run, T4, ~1 s/run | sourced Replicate 2026-11-03 |
| Face pipeline | 78 img/s GPU, 9.8 img/s CPU | sourced-secondary winnow wiki |
| Faces per photo | 1.5 | estimated assumption |
| RunPod 4090 / A5000 / L4 / A100 / H100 | $0.34–0.89 / $0.16–0.27 / $0.44–0.59 / $1.19–1.79 / $2.69–3.99 per hr | sourced RunPod 2026-11-03 |
| Modal T4/L4/A10/L40S/A100-80/H100; CPU; mem | $0.59/$0.80/$1.10/$1.95/$2.50/$3.95 per hr; $0.047/core-hr; $0.008/GiB-hr | sourced Modal 2026-11-03 (per-second rates ×3600) |
| Lambda A10/A100/H100 | $1.29/$1.99/$3.29–4.29 per hr | sourced Lambda 2026-11-03 |
| Replicate CPU/T4/L40S/A100/H100 | $0.36/$0.81/$3.51/$5.04/$5.49 per hr | sourced Replicate 2026-11-03 |
| Gemini 2.5 image tokens | 258/tile of 768×768; ≤384 px = 258 | sourced Google tokens page 2026-11-03 |
| Gemini 3.x/4 image tokens | low 280 / medium 560 / high 1,120 / ultra_high 2,240; default 1,120 | sourced Google media-resolution page 2026-11-03 |
| Gemini 2.5 Flash-Lite / 2.5 Flash / 3.1 Flash-Lite / 3 Flash / 3.6 Flash | $0.10/0.40; $0.30/2.50; $0.25/1.50; $0.50/3.00; $0.75/3.75 (→$1.50/7.50 in 2027); batch 50% | sourced Google 2026-11-03 |
| OpenAI patch rule & multipliers | 32 px patches; 5.4-nano 1.2, 5.4-mini 1.2, 5.6-luna 1.2, 5-mini 1.2 (depr.), 5-nano 1.5 (depr.), 4.1-mini 1.62, 4.1-nano 2.46 (depr.); 6-luna not listed | sourced OpenAI vision guide 2026-11-03 |
| GPT-5-nano / 5-mini / 4.1-mini / 5.4-nano / 5.4-mini / 5.6-luna / 6-luna | $0.05/0.40; $0.25/2.00; $0.40/1.60; $0.20/1.25; $0.75/4.50; $0.20/1.20; $0.10/0.50; batch 50% | sourced OpenAI pricing 2026-11-03 |
| Claude patch rule; tiers | 28 px patches; Standard 1,568 px/1,568 tok; High-res (4.7+) 2,576 px/4,784 tok; 768 px = 784 tok, 1000 px = 1,296 tok | sourced Anthropic vision page 2026-11-03 |
| Claude Haiku 5.5 (≤100k prompt) / Haiku 4.5 | $0.10/$0.50, batch $0.05/$0.25 / $1/$5, batch $0.50/$2.50 | sourced Anthropic pricing 2026-11-03 |
| Caption prompt / output tokens | 50 / 80 | estimated assumption |
| Caption per 22,000 images | $0.69 (2.5 Flash-Lite batch) … $38.41 (Haiku 4.5 1000 px std); Haiku 5.5 $2.71/$1.36; GPT-5.4-nano $5.46/$2.73 | estimated |
| Moondream Cloud | $0.30/$1.00 per M tok (batch $0.15/$0.50); image tokens unknown | sourced Moondream 2026-11-03 |
| Qwen2.5-VL-3B local | $0.0079–0.015 per 1,000 images | sourced Salad 2025-03-21 |
| Florence-2-large | ~150 ms/img | sourced-secondary |
| Tesseract page timings (HP Z420, Hindi page) | LSTM+OpenMP+AVX 1.8 s real / 3.8 s CPU; legacy 2.9 s; LSTM ~10× CPU of legacy | sourced tessdoc (Tesseract 4.0 era) |
| Tesseract per photo | 1 s | estimated assumption (bracketed by above) |
| Textract | $0.0015/page (→$0.0006 >1M); 1,000/mo free | sourced AWS 2026-11-03 |
| Google Vision OCR | $1.50/1k (→$0.60 >5M) | unverified (page JS-only on fetch); not used |
| OCR-flag rate | 20% | estimated assumption |
| Indexing tiers per 100 GB | low $0.16–0.19; mid $0.33–1.5; high $10.6–15.9; max $51–72 | estimated |
| pgvector row size (512-d, HNSW m=16) | ~2.3 KB | sourced-secondary formula |
| Per-user vector footprint | ~127 MB | estimated |
| RAM-resident users per 8 GB box; usable disk on 80 GB / 160 GB | ~50 (6.5 GB usable); 64 GB / 128 GB (20% haircut) | estimated assumptions |
| pgvector cost/user: CX33 RAM / disk; DO RAM / disk | €0.18 / €0.018; $0.96 / $0.05 | estimated |
| Pinecone | $0.33/GB-mo; $50 min; reads $16–18/M; writes $4–4.50/M | sourced Pinecone 2026-11-03 |
| turbopuffer | ≤$0.33/GB storage; ≤$2/GB writes; $16 min | sourced turbopuffer 2026-11-03 |
| Query tokens; queries/mo; hosted query cost | 3,000 in + 300 out; 100; $0.00042/query, $0.04/mo | estimated assumptions |
| Library growth | ~1 GB/mo; +$0.18 (R2) / +$0.08 (B2) per mo after a year | estimated |
| iCloud+ | $0.99/50 GB, $2.99/200 GB, $9.99/2 TB, $29.99/6 TB, $59.99/12 TB | sourced Apple 108047 (2026-09-16) |
| Google One storage: AI Plus / AI Pro / AI Ultra | 400 GB / 5 TB / from 20 TB | sourced Google plans page 2026-11-03 |
| Google One prices: Basic / AI Plus / AI Pro | $1.99 / $4.99 / $19.99 | sourced-secondary (official page renders no prices) |
| Ente | $2.49/50 GB; $4.99/200 GB; $9.99/1 TB; $19.99/2 TB; 10 GB free | sourced Ente 2026-11-03 |
| Ente open metrics (Jan 2026) | revenue $780,996; paid 12,018; registered 290,703; later $1,413,012 / 21,807 / 490,639 | sourced ente.com/open 2026-11-03 (latest-month label not captured) |
| Ente revenue per paid customer | ~$65/yr | estimated |
| PhotoPrism | €2 Essentials, €6+ Plus (table; hero shows €200/€600 — page bug), self-hosted, billed annually; PikaPods $6.50 | sourced PhotoPrism 2026-11-03 |
| Mylio Photos+ | ~$9.99/mo, $99–119.99/yr, no storage; SecureCloud price unknown | sourced-secondary (official site shows no prices) |
| Amazon Photos | $1.99/100 GB; $6.99/1 TB; $11.99/2 TB; Prime unlimited photos + 5 GB video | sourced-secondary (amazon.com 503 ×5) |
| FOREVER | $9/GB at 100 GB … $5.50/GB at 2 TB one-time | sourced FOREVER 2026-11-03 |
| Permanent.org | $10/GB one-time; 1 GB free | sourced Permanent 2026-11-03 |
| Backblaze personal | $9/mo monthly; $8.25/mo annual ($99/yr); $7.88/mo 2-yr ($189) | sourced Backblaze 2026-11-03 |
| Dropbox Plus | $9.99/mo, 2 TB (billing cycle not stated in fetched text) | sourced Dropbox 2026-11-03 |
| Backblaze CB gross retention / NRR / customers Q4 2025 | 91% (90%) / 98% (109%) / 402,589 (417,845) | sourced Backblaze IR 2026-02-23 |
| Backblaze CB Q1 2026 gross retention / NRR; overall NRR | 91% (90%) / 95% (103%); 103% (105%) | sourced Backblaze IR 2026-05-04 |
| Backblaze 10-K: CB retention 2025/24/23; B2 retention; total NRR; CB ARPU | 91/90/91%; 89/89/90%; 105/116/109%; $163/$159/$140 | sourced SEC 10-K FY2025 (fetched) |
| Dropbox paying users / ARPU / ARR | 18.08M (18.22M) / $138.91 ($140.23) / $2,526M ($2,574M) | sourced SEC 10-K FY2025 |
| RevenueCat P&V annual renewal / monthly renewal / trial conv / cancel assurance | 23% / 48% / 22.2% / 25.0% | sourced RevenueCat 2026 |
| RevenueCat annual Y1 retention (= 1 − cancellations) | freemium 28%, hard paywall 27% (~72% cancel, vs ~56% prior year) | sourced RevenueCat 2026-03-19 (one datapoint, two framings) |
| Ancestry monthly churn | 3.6–3.9% (2009–2012); none disclosed in FY2015 10-K | sourced-secondary; absence sourced SEC |
| Ancestry total subscribers growth FY2015 | ~7% | sourced SEC 10-K (Ancestry.com LLC) |
| MyHeritage churn | — | unknown |
| Stripe | 2.9% + $0.30 | sourced Stripe 2026-11-03 |
| Apple SBP commission | 15% under $1M | sourced Apple 2026-11-03 |
| Plan fill rates | 50% (200 GB), 40% (1–2 TB) | estimated assumption |
| Thumbnail size; thumbnails per user | 50 KB; 1.1 GB | estimated assumption |
| Expected life: monthly P&V / annual P&V / Backblaze-like / B2-like | 1.9 / 15.6 / 133 / 109 months | estimated (geometric) |
| Onboarding amortization per 100 GB | $0.044/mo (15.6-mo) / $0.36/mo (1.9-mo) | estimated |
| Other COGS A / B / C (annual basis; monthly basis) | $0.14 / $0.45 / $1.01 ($0.46 / $1.71 / $3.53) | estimated (derivation shown in Q7) |
| GM by plan/backend; payback; max CAC | see Q7 tables | estimated |
| Storage share of variable infra, A/R2 | 97% (15.6-mo), 80% (1.9-mo) | estimated |
| Index-only COGS split | $0.16 total; indexing 32% (64% incl. vector DB); queries 25% | estimated |
| CAC | — | unknown |

---

## 5. Unknowns we could not resolve

1. **Share of library bytes that is video** — no primary or rigorous measurement; one secondary page's editorial estimates imply 48–80%; the reference user rests on a 50% assumption with 30–70% sensitivity. Highest-leverage number to measure in a pilot.
2. **Average on-device photo size for current iPhones (24 MP default)** — Apple publishes only ProRAW sizes and the HEIF ratio; secondary pages give 2–3 MB (24 MP) and 3–5 MB (48 MP) without citable Apple URLs. No per-model Apple table exists.
3. **Current Apple video bitrate table** — only an iPhone-8-era settings screen (secondary) and a secondary page that disagrees on which resolution 170 MB/min belongs to.
4. **Plan fill rate** (used GB ÷ quota) for consumer storage plans — no disclosure found; GM swings 40 points between 50% and 100% fill on R2.
5. **CAC for consumer photo/storage apps** — nothing public; payback shown only as sensitivity.
6. **Retention for a storage-bearing *photo* product specifically** — Backblaze (backup utility, 91%, annual terms) and RevenueCat Photo & Video (23% annual / 48% monthly first renewal) bracket it. Ente publishes revenue and paid-customer counts (ente.com/open) but no churn; Immich has no paid product; Mylio publishes nothing.
7. **Genealogy churn today** — Ancestry last disclosed 2012 (its FY2015 10-K as a debt registrant has no churn rate); MyHeritage never; Blackstone/Francisco Partners deal pages unreachable or 404.
8. **Dropbox churn** — 10-K gives net paying-user change only; without gross adds no churn can be implied.
9. **Google One official US prices** — the official plans page renders storage sizes but blank "/mo" prices on every fetch; 7 official URLs tried. Prices remain secondary.
10. **Amazon Photos (503 ×5) and Mylio (no prices on site, 403 on community FAQ) official pricing**; Mylio SecureCloud price.
11. **Scaleway official price table** (403 on pricing page ×2; product page and docs give no rates) — secondary only.
12. **AWS S3 egress rate** — the S3 pricing feed does not contain data-transfer SKUs and the page's rate table does not render; $0.09/GB is secondary (free 100 GB is primary).
13. **Google Cloud Vision OCR price** — page is JS-only; unverified and unused. Textract is the sourced cloud-OCR anchor.
14. **Moondream throughput** (model card, Moondream 3 post and pricing page have no img/s) and **Moondream Cloud image-token count**; **Florence-2 hardware** for the 150 ms figure.
15. **Tesseract per-photo throughput** — only full-page figures (1.8–3.8 s) are sourced; 1 s/photo is an assumption.
16. **gpt-6-luna image multiplier** — not in the OpenAI vision guide; the model is omitted from the caption table.
17. **Gemini 3.x later-month / Photo & Video later-month renewal** — RevenueCat publishes first-renewal medians only, so the 1.9-month monthly-plan life is a conservative constant-hazard estimate.
18. **Whether FUTO's Immich backup service will be priced as hosted storage** — closed beta "later this year", no price.
19. **Cold Archive retrieval fee (OVH)** — "Yes" on the product page, amount not on the price list fetched.

---

## 6. Full source list (accessed 2026-11-03 unless noted)

Primary / official:
1. https://developers.cloudflare.com/r2/pricing/ (page "Last updated Oct 30, 2026")
2. https://www.backblaze.com/cloud-storage/pricing
3. https://www.backblaze.com/cloud-backup/pricing
4. https://www.backblaze.com/cloud-backup (monthly $9 / 2-year $7.88)
5. https://wasabi.com/pricing
6. https://www.hetzner.com/storage/object-storage/
7. https://www.hetzner.com/storage/storage-box/
8. https://docs.hetzner.com/storage/storage-box/general
9. https://www.hetzner.com/cloud/cost-optimized/
10. https://www.hetzner.com/cloud/regular-performance/
11. https://www.hetzner.com/cloud/general-purpose/
12. https://www.digitalocean.com/pricing/droplets
13. https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/s3/USD/current/s3.json (AWS public pricing data feed behind the S3 pricing page; manifest publication date 2026-10-15; gzip)
14. https://aws.amazon.com/s3/pricing/ (partial — rate table did not render; free egress allowance and minimum durations only)
15. https://aws.amazon.com/textract/pricing/
16. https://us.ovhcloud.com/public-cloud/prices/ (Object Storage section)
17. https://www.ovhcloud.com/en/public-cloud/uc-backup-object-storage/
18. https://www.ovhcloud.com/en/public-cloud/cold-archive/
19. https://www.ovhcloud.com/en/public-cloud/object-storage/ (no rates; confirms free egress)
20. https://www.scaleway.com/en/object-storage/ (no rates; "No request fees")
21. https://aistudio.google.com/docs/pricing
22. https://aistudio.google.com/docs/tokens
23. https://aistudio.google.com/docs/media-resolution (Gemini 3.x/4 image tokens)
24. https://platform.claude.com/docs/en/about-claude/pricing
25. https://platform.claude.com/docs/en/build-with-claude/vision
26. https://developers.openai.com/api/docs/pricing
27. https://developers.openai.com/api/docs/guides/images-vision
28. https://lambda.ai/service/gpu-cloud
29. https://www.runpod.io/pricing
30. https://modal.com/pricing
31. https://replicate.com/pricing
32. https://replicate.com/andreasjansson/clip-features
33. https://www.pinecone.io/pricing/
34. https://turbopuffer.com/pricing
35. https://moondream.ai/pricing
36. https://moondream.ai/blog/moondream-3-preview
37. https://huggingface.co/vikhyatk/moondream2
38. https://support.apple.com/119916 (About Apple ProRAW, published 2024-04-19)
39. https://support.apple.com/116944 (HEIF/HEVC)
40. https://support.apple.com/en-us/108047 (iCloud+ prices, dated 2026-09-16)
41. https://one.google.com/about/google-ai-plans/ (storage sizes only; prices blank)
42. https://ente.com/pricing
43. https://ente.com/open and https://ente.com/blog/open/ (2026-07-01)
44. https://www.dropbox.com/plans
45. https://www.forever.com/pricing
46. https://www.permanent.org/why-permanent/
47. https://www.photoprism.app/editions
48. https://immich.app/blog/2026-march-recap (2026-03-31)
49. https://www.sec.gov/Archives/edgar/data/1467623/000146762326000008/dbx-20251231.htm (Dropbox 10-K FY2025)
50. https://ir.backblaze.com/news/news-details/2026/Backblaze-Announces-Fourth-Quarter-and-Full-Year-2025-Financial-Results/default.aspx (2026-02-23)
51. https://ir.backblaze.com/news/news-details/2026/Backblaze-Announces-First-Quarter-2026-Financial-Results/default.aspx (2026-05-04)
52. https://www.sec.gov/Archives/edgar/data/1462056/000162828026016395/blze-20251231.htm (Backblaze 10-K FY2025, fetched in full)
53. https://www.sec.gov/Archives/edgar/data/1575319/000157531916000021/acom2015123110k.htm (Ancestry.com LLC 10-K FY2015, filed 2016-02-19; no churn disclosure)
54. https://www.revenuecat.com/blog/growth/average-subscription-renewal-rates-by-app-category (updated 2026-04-24)
55. https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026 (2026-03-19)
56. https://www.revenuecat.com/state-of-subscription-apps
57. https://www.revenuecat.com/state-of-subscription-apps-2026-education
58. https://stripe.com/pricing
59. https://developer.apple.com/app-store/small-business-program/
60. https://gist.github.com/TACIXAT/ecd4f636bf6af28cb69d641e29d7b362 (OpenCLIP throughput, 2026-01-15)
61. https://github.com/storytold/lightcraft/pull/1611 (SigLIP 2 / CLIP GPU benchmarks, open PR, fetched 2026-11-03)
62. https://blog.salad.com/qwen-benchmark (2025-03-21)
63. https://www.insightface.ai/guides/choose-face-recognition-model-and-evaluate
64. https://tesseract-ocr.github.io/tessdoc/tess4/4.0-Accuracy-and-Performance.html and https://tesseract-ocr.github.io/tessdoc/tess4/NeuralNetsInTesseract4.00.html
65. https://photutorial.com/photos-statistics/ (updated 2026-09-26; original research, partly extrapolated from 2013 data)
66. https://riseaboveresearch.com/rise-above-research-forecasts-a-global-surge-in-photos-captured/ (2026-02-10)

Secondary (used only where primary unreachable; flagged inline):
67. https://www.cloudzero.com/blog/s3-pricing/ (2026-07-30) — S3 egress rate; Deep Archive cross-check
68. https://securityboulevard.com/2026/06/glacier-and-deep-archive-pricing-the-complete-2026-cost-guide/ — Glacier retrieval context (superseded by the AWS feed)
69. Scaleway pricing via search snapshot of https://www.scaleway.com/en/pricing/storage/ (403 on fetch ×2; docs FAQ 403)
70. https://github.com/sudolulo/winnow/wiki/Benchmarks — face pipeline throughput
71. https://github.com/Berkaybbayramoglu/siglip-onnx-embedder — CPU int8 latency
72. https://botmonster.com/ai/run-vision-models-locally-florence-2-qwen-vl/ — Florence-2 latency
73. https://dev.to/multigrid/choosing-and-tuning-a-pgvector-index-1hki — pgvector row-size formula
74. https://phonearena.com/news/Heres-how-much-space-Apples-new-HEVC-video-format-saves-on-an-iPhone-8_id98212 — 170 MB/min 4K30 HEVC
75. https://dblabsapps.com/statistics/iphone-storage-photos-statistics/ — HEIC/JPEG sizes by MP, video MB/min, video share of storage (self-described editorial estimates)
76. https://www.heicify.com/guides/iphone-photo-formats-guide — HEIC vs JPEG sizes at 12/48 MP
77. https://www.whistleout.com/CellPhones/Guides/amazon-photo-storage and https://whichonetho.io/provider/amazon-photos (May 2026) — Amazon Photos prices
78. https://www.lilachbullock.com/google-one-price/ and https://grabaicredits.com/en/pricing/google-ai-plans-pricing (Oct 2026) — Google One prices
79. https://www.reviewed.com/tech/features/mylio-photos-photo-storage-solution and https://community.mylio.com/posts/faq-how-much-does-mylio-photos-cost (403) — Mylio prices
80. https://www.geneamusings.com/2010/01/ancestrycom-financial-information.html and https://www.fool.com/investing/general/2012/02/16/ancestrycom-goes-out-on-a-family-tree-limb.aspx — Ancestry churn 2009–2012
81. medium.com/@geronimo7 — Moondream tok/s (int4, RTX 3090)

Attempted and failed (so the next agent does not repeat): one.google.com/about/plans (×2), /about/google-ai-pro/, /about/basic/, support.google.com/googleone/answer/9004014 and /15663611, blog.google/products/google-one/google-ai-plus/; amazon.com/photos/storage (×2), /b?node=13234696011, /photos/pricing, /clouddrive/pricing (all 503); mylio.com/pricing/, /mylio-photos-plus/, /plans/, /secure-cloud-storage/; cloud.google.com/vision/pricing (×2) and /document-ai/pricing (JS-only); azure computer-vision pricing (placeholders); dropbox.com/plus, /buy/plus, help.dropbox.com/plans/dropbox-plus (no price); backblaze.com/docs/cloud-backup-pricing (404); scaleway.com/en/pricing/storage/ and docs FAQ (403); ovhcloud.com/en/public-cloud/prices/ (truncated ×2); myheritage.com/blog/2021/02/… (404 ×2), franciscopartners.com news (404); blackstone.com Ancestry release (403), ancestry.com newsroom (no content); ocrmypdf performance page (no timings); SEC EDGAR full-text search (403; company index and submissions API worked).

---

## Audit log

Each auditor finding, and what was done (all edits in place; no sourced material that passed was removed).

**Untagged numbers**
1. L44 ratios (24×, 3.3×) → recomputed (23.2×, 3.3×) and tagged `[estimated: ratio of table rows]`.
2. L56 unlinked blog claims (12%, 50–70%) → replaced with the fetched dblabsapps figures (video 12% of storage; photos+videos 15–25%), URL and "editorial estimate" caveat given, and the implied 48–80% video share derived and tagged.
3. L73 CX33 €0.0123/hr → corrected to Hetzner's listed **€0.0144/hr** (monthly cap €8.99); all CX33-based CPU costs recomputed; all Hetzner hourly rates now quoted from the pages.
4. L76 lightcraft PR #1611 → fetched https://github.com/storytold/lightcraft/pull/1611; figures verified (3.0 ms/photo batch 32 on RTX 4090; 176 ms CPU batch 8; end-to-end 1,752 photos/min) and the URL added; the end-to-end figure is now used as a sourced upper bracket for the overhead factor.
5. L78 "Modal L4 at 75 img/s" and "×3" → the L4 throughput is now explicitly an assumption (83 img/s = ¼ of the 4090 batch-32 figure, tagged `[estimated: assumption, untested]`); the ×3 overhead factor is explained (decode/resize/I-O excluded from tower benchmarks) and bracketed by lightcraft's measured 11× end-to-end slowdown. Added Replicate's per-run hosted price as a sourced alternative.
6. L121–124 tier table inputs that matched no computed row → table rebuilt so every cell is a computed row (community vs secure RunPod rate, batch-1 vs end-to-end), with the selection rule stated.
7. L131 "~50 users RAM-resident", "64 GB usable" → methods stated (8 GB − 1.5 GB overhead ÷ 127 MB; 80 GB − 20% haircut), tagged as assumptions; DigitalOcean orderable baseline added.
8. L149 Backblaze "$9/mo" → now sourced from https://www.backblaze.com/cloud-backup ($9 monthly, $7.88 two-year).
9. L150 Dropbox "$11.99 monthly" → removed; the page shows only "$9.99 / month" and the billing cycle is marked [unknown] (three further official URLs tried, none show a price).
10. L156 Backblaze Q1 2026 → fetched the IR press release (2026-05-04), URL added; figures: CB gross retention 91%, CB NRR 95%, overall NRR 103%.
11. L172–183 "Other COGS" → full derivation shown per plan (vector DB, queries, incremental, amortized onboarding; size multiples; two amortization bases); values recomputed ($0.14 / $0.45 / $1.01).
12. L110 Google Vision "[sourced: via search snapshot]" → retagged `[unverified: not fetched; not used]` after two failed fetches of the pricing page and one of Document AI; Textract is now the only cloud-OCR price used in arithmetic.
13. L211 index-only "indexing ~60%" → recomputed: indexing proper 32%, 64% including vector DB, queries 25% (of $0.16).

**Suspect claims**
1. GPT-5.4-nano/mini multiplier "[unknown]" → corrected: the vision guide lists both at 1.2; GPT-5.4-nano row added ($5.46 std / $2.73 batch per 22k) and GPT-5.6-luna row added; unknown #11 replaced by the genuinely missing gpt-6-luna multiplier.
2. Claude row built on Haiku 4.5 only → Claude Haiku 5.5 ($0.10/$0.50, batch $0.05/$0.25) added as the current Claude price point ($2.71 std / $1.36 batch per 22k, $3.84 at 1000 px); Haiku 4.5 rows retained and marked "superseded"; the "max tier" is relabelled a legacy-price worst case and the A5 conclusion rewritten accordingly.
3. GPT-5-nano/mini anchoring High tier while deprecated → rows kept but flagged deprecated; High tier now anchored on Haiku 5.5 / GPT-5.4-nano / Gemini 3.1 Flash-Lite; gpt-4.1-nano noted as no longer on the pricing page; gpt-6-luna priced but excluded for unknown multiplier.
4. 15.6-month life applied to monthly plans → payback table now has three life columns (1.9-mo monthly-plan from the 48% monthly renewal; 15.6-mo annual-plan; 133-mo Backblaze-like); Other COGS computed on both amortization bases; the Backblaze 10-K quote that "the significant majority of our customers have subscription terms of one year or longer" added to reconcile the 91% figure with annual terms; the 3.7% customer decline reconciled against 91% retention. Max-CAC conclusions rewritten.
5. "CPX12 is orderable" → corrected: on 2026-11-03 all CPX, CX, CAX and CCX plans show "currently unavailable"; pgvector baseline moved to DigitalOcean ($0.05/user disk-resident), Hetzner retained as list-price reference only.
6. CX33 €0.0123/hr → €0.0144/hr (see above).
7. Gemini 258/tile applied to 3.x → corrected using the media-resolution page: Gemini 3.x/4 images cost 280/560/1,120 tokens by `media_resolution` with default 1,120; all 3.x rows recomputed at low and default; this materially raises Gemini 3.x caption costs.
8. RevenueCat "2025 data" vs "72% in 2026" → wording fixed (report published 2026-03-19, cohorts through 2025, labels latest as 2026); the 72% cancellation figure is now explicitly identified as the complement of the 27–28% retention, not a separate datapoint; paraphrase marked.
9. Dropbox "(annual; $11.99 monthly)" → removed (see above).
10. PhotoPrism €2/€6 → the €200/€600 vs €2.00/€6.00 inconsistency on the page is now stated; table values used and flagged.
11. GM % convention → stated explicitly (fees as cost of revenue; denominator = gross price), including the App Store row.
12. Photutorial 20.2/day → the page's own caveats ("individuals who actively take photos"; extrapolated from 2013 statistics) are quoted; it is now treated as an upper bound; the 200/mo choice is justified (anchored on the only measured per-device figure, Gigaom 182/mo) rather than "between".

**Broken or misquoted sources**
- Scaleway: two more official URLs tried (product page, docs FAQ); still secondary; stated.
- OpenAI vision guide: re-read; multipliers corrected (see above).
- Claude pricing: Haiku 5.5 added (see above).
- Hetzner regular-performance: CPX availability and CX33 hourly corrected (see above).
- Dropbox plans: qualifiers removed (see above).
- lightcraft PR #1611: URL added and verified (see above).
- Google Vision: retagged unverified (see above).
- Backblaze Q1 2026 8-K: replaced by the fetched IR press release with URL.
- AWS S3: Standard, Glacier IR, Deep Archive retrieval, PUT/GET rates now sourced from the AWS public pricing feed (published 2026-10-15); Deep Archive storage rate's provenance in the feed explained; egress rate remains secondary and is listed as unknown #12.
- OVH: rates now from the official US price list (per-GiB-hour), replacing the use-case landing page figure.

**Missing vs brief**
- Q1: AWS now primary (feed); Scaleway retried (still 403); OVH from the price list.
- Q2: HEIC vs JPEG sizes at 12/48 MP and per-model (iPhone 17 24 MP/48 MP) added from two secondary pages with caveats; Apple per-model table confirmed absent; video share bounded (48–80%) from a secondary source and still [unknown] at a rigorous level.
- Q3(a): batched SigLIP throughput verified with URL; Replicate per-image price computed; Modal figure explicitly an assumption.
- Q3(b): GPT-5.4-nano, GPT-5.6-luna, Claude Haiku 5.5 rows added; Gemini 3.x re-tokenized; Moondream throughput searched (3 official pages, none give img/s) and Moondream Cloud per-token pricing added; Florence-2 left secondary.
- Q3(c): Tesseract page-level timings sourced from tessdoc (1.8–3.8 s/page) to bracket the 1 s/photo assumption; Google Vision fetch attempted twice (JS-only), Document AI once, Azure once (placeholders) — documented.
- Q5: $/mo and GB columns filled for Google One (storage sizes now primary, prices secondary with 7 failed official attempts listed), Ente, PhotoPrism, Mylio, Amazon Photos (5 failed official attempts listed).
- Q6: Ente open-metrics dashboard found and quoted (revenue, paid customers, registered; no churn); Ancestry.com LLC FY2015 10-K fetched from EDGAR (no churn disclosure); MyHeritage/Francisco Partners and Blackstone/Ancestry pages attempted (404/403) and listed; Dropbox implied-churn derivation shown to be impossible without gross adds.
- Q7: monthly-plan variant (48% renewal → 1.9-mo life) modelled alongside the annual-plan and Backblaze-like variants; onboarding amortized on both bases.
- Numbers table: added Other COGS per plan, tier-table components, 64/128 GB usable, 50-user RAM figure, 50 KB thumbnail, 1.5 faces/photo, 1 frame/10 s, 3,000+300 query tokens, 100 queries/mo, 20% OCR-flag rate, overhead factor, Modal L4 assumption, caption prompt/output tokens, and all new sourced figures.
