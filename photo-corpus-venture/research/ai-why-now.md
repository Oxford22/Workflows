# Track G — AI capability as the "why now"

Written 2026-11-03; repaired 2026-11-03 after hostile audit (see "Audit log" at the end). All sources
accessed 2026-11-03. Every number is tagged `[sourced: url, date]`, `[estimated: method]` or `[unknown]`.
Dates on findings are the source's date, not today's.

Method note: the shared WebSearch budget was exhausted before this track started and again during the
repair, so all evidence comes from direct fetches of primary pages (vendor docs, pricing pages, model cards,
papers, GitHub READMEs/raw files, Apple/Google newsroom posts), the Hugging Face Hub API and paper index,
the Consensus paper index (abstract records only, marked secondary), and GitHub code search. Several
openai.com pages return HTTP 403 to this environment; OpenAI numbers come from developers.openai.com.
web.archive.org is blocked from this environment. Gaps caused by this are listed in §5.

---

## 1. Questions asked

1. Which vision-language / embedding models run on consumer hardware in 2026 (SigLIP 2, Apple
   Foundation Models on iOS 26/27, Visual Intelligence, Gemini Nano, Qwen2.5/3-VL small, Moondream,
   Florence-2, SmolVLM, Gemma 3n): date, size, where they run, throughput, license?
2. Cost curve: per-image captioning cost 2024 vs 2026; embedding cost curve.
3. Face recognition: state of open models; cross-age accuracy; is cross-generation clustering solvable?
4. Scanned-print specifics: restoration, dating, handwritten-caption OCR, reverse-side scanning.
5. On-device vs cloud: cost/trust effect of indexing on the user's Mac; CLIP/SigLIP throughput on
   Apple silicon; Neural Engine access for third parties.
6. Assistants/tool use over private data 2024→2026 (brief; Track E covers depth).
7. Counter-case: what Apple/Google shipped natively; is the native-vs-best-of-breed delta shrinking?

Falsification stance: for each candidate why-now I looked first for evidence that the capability
either (a) already existed before 2024 (so it is not a *dated* change) or (b) is equally or more
available to Apple/Google (so it is not *defensible*).

---

## 2. Findings per question

### Q1. Models usable on consumer hardware in 2026

| Model | Date | Size | Runs on | License | Source |
|---|---|---|---|---|---|
| SigLIP 2 (B/16, L/16, So400m, g) | 2025-02-21 | 86M / 303M / 400M / 1B vision towers (HF card lists 375M total for B/16 incl. text tower; 1,136M for So400m-naflex) | CPU, M-series, VPS; Immich ships it | Apache-2.0 | [sourced: https://huggingface.co/blog/siglip2 and HF Hub API cards google/siglip2-*, 2025-02-21] |
| Apple Foundation Models (on-device) | iOS 26: 2025-06-09; image input: iOS 27.0 | ~3B params, 2 bits/weight; ViTDet-L 300M vision encoder | Apple Intelligence devices (iPhone 15 Pro/16+, iPad A17 Pro/M1+, Mac M1+) | Apple system framework (free, no API cost) | [sourced: https://machinelearning.apple.com/research/apple-foundation-models-2025-updates, 2025-06-09; https://developer.apple.com/tutorials/data/documentation/foundationmodels/imageattachmentcontent.json, introducedAt 27.0] |
| Gemini Nano via ML Kit GenAI Prompt API | Prompt API "offered in beta" (no date on page) | Gemini 1.0 report: Nano-1 1.8B, Nano-2 3.25B, "4-bit quantized for deployment" (2023-12-19). Sizes of the ML Kit "nano-v2/v3/v4" generations: [unknown — not on any Google page fetched] | Pixel 9/10/11, Galaxy S26 / Z Fold7-8, many OEMs (list below) | Google ML Kit GenAI terms | [sourced: https://developers.google.com/ml-kit/genai; https://developers.google.com/ml-kit/genai/prompt/android; https://arxiv.org/abs/2312.11805 Table 1, 2023-12-19] |
| Gemma 3n E2B / E4B | 2025-06-26 | 5B raw / ~2B effective (1.91B); 8B raw / ~4B effective; runs in ~2 GB / ~3 GB | phones, laptops; LiteRT, MLX, llama.cpp, Ollama | Gemma Terms of Use (not OSI). Gemma 4: terms page links a "Gemma 4 license" whose page is the Apache-2.0 text [estimated: inferred from the linked page https://ai.google.dev/gemma/apache_2 containing the Apache License 2.0 text; the terms page itself does not say "Apache"] | [sourced: https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/, 2025-06-26; https://ai.google.dev/gemma/docs/gemma-3n; https://ai.google.dev/gemma/terms, last modified 2026-04-01] |
| Qwen2.5-VL-3B / 7B Instruct | 2025-01-26 | 3.75B / 8.29B | M-series via MLX (mlx-vlm lists Qwen2.5-VL); VPS with GPU | 3B: "qwen-research" (not Apache); 7B: Apache-2.0 | [sourced: HF Hub API cards Qwen/Qwen2.5-VL-3B-Instruct (3,754,622,976 params, createdAt 2025-01-26), Qwen/Qwen2.5-VL-7B-Instruct (8,292,166,656)] |
| Qwen3-VL-2B / 4B Instruct | 2025-10 (card updated 2025-10-23 / 2025-10-15) | 2.13B / 4.44B | M-series via MLX; VPS with GPU | Apache-2.0 | [sourced: HF Hub API cards Qwen/Qwen3-VL-2B-Instruct, Qwen/Qwen3-VL-4B-Instruct] |
| Moondream 3 (preview) | 2025-09-18 | 9B MoE, 2B active; 32K context | GPU; "inference much slower than anticipated" at preview | Moondream Model License 1.0 (commercial OK; hosted general-purpose inference needs separate license) | [sourced: https://moondream.ai/blog/moondream-3-preview, 2025-09-18; https://moondream.ai/licenses/model/1.0, effective 2026-07-07] |
| Moondream 2 | last release 2025-06-21 (card modified 2026-09-23) | 1.93B (card: "2B", BF16) | CPU/M-series ("mps") | Apache-2.0 | [sourced: https://huggingface.co/vikhyatk/moondream2; HF Hub API] |
| Florence-2 base / large | paper 2023-11-10; weights mid-2024 | 0.23B / 0.77B | CPU, M-series | MIT | [sourced: https://huggingface.co/microsoft/Florence-2-large; HF card microsoft/Florence-2-base 231.6M] |
| SmolVLM-256M / 500M | 2025-01-23 | 256M / 500M (93M SigLIP vision encoder) | "consumer laptops, or even potentially browser-based inference"; transformers, MLX, ONNX; WebGPU demo | Apache-2.0 | [sourced: https://huggingface.co/blog/smolervlm, 2025-01-23; HF card HuggingFaceTB/SmolVLM-256M-Instruct] |
| MobileCLIP2 (Apple) | 2025-08-28 | S0 11.4M → L/14 304M image tower | iPhone (ANE), Mac | code MIT; weights Apple ML Research Model TOU ("apple-amlr") | [sourced: https://github.com/apple/ml-mobileclip, 2025-08-28; https://huggingface.co/apple/MobileCLIP2-S4] |

Details that matter for the venture:

- **Apple on-device image input arrived in iOS 27, not 26.** The iOS 26 framework docs introduced the
  on-device 3B model (WWDC25: "3 billion parameters, each quantized to 2 bits", "not designed for world
  knowledge or advanced reasoning") [sourced: https://developer.apple.com/videos/play/wwdc2025/286/, 2025-06].
  Apple's 2025 report says the on-device model "understand[s] image and text inputs" with "the more efficient
  ViTDet-L backbone with 300M parameters for on-device deployment", but says nothing about exposing it
  to developers [sourced: machinelearning.apple.com 2025 updates, 2025-06-09]. The current docs JSON
  lists `ImageAttachmentContent` with `introducedAt: 27.0` on every platform, and an article "Analyzing
  images with multimodal prompting" that says "Perform image analysis with the on-device model first"
  [sourced: developer.apple.com foundationmodels JSON + analyzing-images JSON, 2026]. iOS 27 also adds
  `PrivateCloudComputeLanguageModel`, Dynamic Profiles (agents), a `LanguageModel` protocol so apps can
  route the same session to Claude, Gemini, MLX or Core AI models, and a **Core AI** framework (27.0)
  that runs custom models on CPU/GPU/Neural Engine with a "Background Inference" entitlement
  [sourced: https://developer.apple.com/tutorials/data/documentation/coreai.json; https://developer.apple.com/foundation-models-framework/, 2026].
  Throughput of the on-device 3B model: Apple's report says KV-cache sharing cuts memory 37.5% and is
  "significantly improving the time-to-first-token" but publishes no tokens/s or TTFT figure and names no
  device [sourced: same report]; absolute throughput [unknown].
- **Apple PCC is free for small developers:** "developers who are enrolled in the App Store Small Business
  Program and have fewer than two million first-time App Store downloads can access the Apple Foundation
  Models running on Private Cloud Compute with no cloud API cost", subject to daily usage limits;
  "Expanded access ... will be available for a fee in the future" [sourced: https://developer.apple.com/foundation-models-framework/, 2026].
- **Gemini Nano for third-party apps is beta/preview, multimodal, and device-gated.** The Prompt API page
  says it "accepts text or multimodal (image and text) inputs" and "is offered in beta" [sourced:
  https://developers.google.com/ml-kit/genai/prompt/android]. The ML Kit overview page does not use the
  words "beta" or "Prompt API"; it names `GenerativeModel` (direct model access) and `AgentRunner`, and says
  "Different versions of Gemini Nano run on different devices" [sourced: https://developers.google.com/ml-kit/genai].
  Supported devices by Nano generation, as listed on that page:
  nano-v2 = Honor Magic V5/7/7 Pro; iQOO 13; Motorola Razr 60 Ultra / Razr Ultra 2025; OnePlus 13/13s;
  OPPO Find N5; POCO F7 Ultra, F8 Pro/Ultra, X7 Pro, X8 Pro; realme GT 7 Pro; Samsung Galaxy Z Fold7, Z TriFold;
  vivo X200 FE, T4 Ultra; Xiaomi 14T Pro, 15, 15T, 15T Pro, 15 Ultra, 17, 17 Ultra, Pad Mini.
  nano-v3 = Pixel 9/10 series, Galaxy S26/S26+/Ultra, OnePlus 15/15R, Xperia 1 VIII, Sharp AQUOS R11, Lenovo
  tablets, several Honor/iQOO/OPPO/realme/vivo models.
  nano-v4 = Pixel 11 series, Galaxy Z Flip8/Fold8/Fold8 Ultra [sourced: https://developers.google.com/ml-kit/genai].
  Model size: the only Google-published Nano sizes are from the Gemini 1.0 report, "1.8B (Nano-1) and 3.25B
  (Nano-2) parameters ... It is 4-bit quantized for deployment" [sourced: https://arxiv.org/abs/2312.11805,
  Table 1, 2023-12-19]; neither developer.android.com/ai/gemini-nano nor the ML Kit pages state sizes for
  nano-v2/v3/v4 [unknown]. There is also an on-device **Embedding API**
  (EmbeddingGemma 2, 768-d, text+image, 140 soft tokens per image, 256-token limit) in *preview*, requiring
  the AICore Developer Preview program [sourced: https://developers.google.com/ml-kit/genai/embedding/android].
  Falsification: Nano is not on the long tail of Android devices; a product that depends on it covers only
  the flagship/upper-mid devices listed above. Install-base share [unknown — no primary source found].
- **Visual Intelligence** shipped 2024-12-11 on iPhone 16 (Camera Control), with ChatGPT and Google
  search hand-offs [sourced: https://www.apple.com/newsroom/2024/12/apple-intelligence-now-features-image-playground-genmoji-and-more/, 2024-12-11];
  extended to on-screen content in iOS 26 [sourced: Apple newsroom 2025-06-09]; iOS 27 adds "Siri mode"
  in Camera [sourced: https://www.apple.com/ios/, 2026]. It is a camera/screen feature, not a library
  indexer, so it neither helps nor threatens the corpus idea directly.
- **Throughput (CPU, non-Apple):** Immich's benchmark on a Ryzen 7800X3D ("without acceleration"; mean of
  100 passes): ViT-B-16-SigLIP2 5.81 ms/image, 3,038 MiB, recall 84.86; ViT-SO400M-16-SigLIP2-384 56.57 ms,
  3,854 MiB, recall 85.99; ViT-B-32 openai 2.26 ms [sourced: https://docs.immich.app/features/searching, page
  stamp 2026-10-21]. That is ~172 img/s and ~18 img/s respectively [estimated: 1000/5.81, 1000/56.57].
  A 2-vCPU VPS at roughly 1/6 of a 7800X3D's throughput would do ~29 img/s on B/16, i.e. ~1 hour per
  100k photos excluding decode/IO [estimated: 172/6 → 100,000/29/3600; the 1/6 factor is a guess from
  core count and clocks, not measured]. GPU-VPS cost per hour for VLM captioning: [unknown — no pricing page
  fetched this session].
- **Throughput (Apple, CLIP-class):** Apple's MobileCLIP2 README table lists image-encoder latency
  B 10.4 ms, S0 1.5 ms, L/14 57.9 ms, S4 19.6 ms (plus text encoder 3.3–6.6 ms). The table has no device
  column; the only device named is in the S4 highlight sentence, "2.5x lower latency measured on iPhone12
  Pro Max" [sourced: https://github.com/apple/ml-mobileclip, 2025-08-28]. Attributing every row to the
  iPhone 12 Pro Max is an assumption [estimated: same README, same table, same measurement style].
  Apple's Core ML MobileCLIP (v1) card repeats the same latencies without a device; the iOS demo-app README
  lists "Ideal Latency" S0 2.1 ms, S1 5.8 ms, S2 6.9 ms, B(LT) 13.7 ms, again with no device named
  [sourced: https://huggingface.co/apple/coreml-mobileclip; https://github.com/apple/ml-mobileclip/blob/main/ios_app/README.md].
  Apple's own face embedding "completes in less than 4ms" per face on the Neural Engine, "8x improvement
  over an equivalent model running on GPU" [sourced: https://machinelearning.apple.com/research/recognizing-people-photos, 2021-07-28].
  **No published SigLIP 2 / CLIP images-per-second figure on M1–M4 was found** [unknown]. Sources checked:
  mlx-examples CLIP README (supports openai/clip-vit-base-patch32 and -large-patch14; "no throughput,
  benchmark, images/sec, latency, or hardware (M1/M2/M3/M4) figures") [sourced: https://github.com/ml-explore/mlx-examples/blob/main/clip/README.md];
  mlx-vlm README (Apple-silicon figures only for Gemma 4 26B-A4B: ~31–52 tok/s generation on "Apple Silicon
  (Metal)", chip not named; nothing for CLIP) [sourced: https://github.com/Blaizzy/mlx-vlm]; the open-source
  iOS CLIP-search app Queryable (defaults to MobileCLIP-S2; "no figures for indexing speed") [sourced:
  https://github.com/mazzzystar/Queryable]. If an M-series Mac merely matched the phone-class 10.4 ms per
  image for a B-size encoder, 100k photos ≈ 100,000 × 10.4 ms ≈ 17 min of encoder time, and decode/IO would
  dominate [estimated: 100,000 × 10.4 ms; assumes M-series ≥ the iPhone-class figure, whose device
  attribution is itself the assumption above — treat as an order-of-magnitude bound, not a benchmark].
- **Throughput (VLMs on consumer hardware):** Gemma 3n's MobileNet-V5 encoder "Processes up to 60 frames per
  second on a Google Pixel" and "Natively supports resolutions of 256x256, 512x512, and 768x768 pixels";
  "Gemma 3n natively supports image, audio, video, and text inputs and text outputs" [sourced:
  https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/, 2025-06-26]. Moondream 2's
  2025-06-21 release claims "20–40 % faster response generation" (relative only) [sourced:
  https://huggingface.co/vikhyatk/moondream2]. SmolVLM's blog gives throughput only as an A100 chart
  [sourced: https://huggingface.co/blog/smolervlm, 2025-01-23]. Florence-2 and Qwen2.5/3-VL cards give no
  speed figures. Apple's FastVLM README claims "85x faster Time-to-First-Token" than LLaVA-OneVision-0.5B
  without naming the hardware [sourced: https://github.com/apple/ml-fastvlm, CVPR 2025]. Absolute
  images/sec for Qwen2.5/3-VL small, Moondream, Florence-2, SmolVLM and the Apple 3B model on M-series or a
  VPS: [unknown].
- **Prior art caveat (falsification of "new"):** Immich's server defaults are `facialRecognition.modelName:
  'buffalo_l'` and `clip.modelName: 'ViT-B-32__openai'` [sourced: https://raw.githubusercontent.com/immich-app/immich/main/server/src/dtos/config.dto.ts;
  https://docs.immich.app/install/config-file, updated 2026-10-21], and its ML README says "This project
  utilizes facial recognition models from the InsightFace project" and lists antelopev2, buffalo_l, buffalo_m,
  buffalo_s [sourced: https://github.com/immich-app/immich/blob/main/machine-learning/README.md]. (The
  feature page docs.immich.app/features/facial-recognition names no model: "There are a few different models
  available; the default is typically considered the best".) Immich also ships SigLIP 2 for smart search
  [sourced: docs.immich.app/features/searching]. Ente runs MobileCLIP + YOLO5Face + MobileFaceNet on-device
  across platforms, with desktop indexing then sync to mobile [sourced: https://ente.com/ml/, undated].
  The Apple MobileCLIP (v1) Core ML export dates to CVPR 2024 (HF card updated 2024-11-19) and the Queryable
  iOS CLIP app predates it [sourced: HF apple/coreml-mobileclip; github.com/mazzzystar/Queryable]. So local
  CLIP + face clustering in self-hosted/open apps predates 2024 [estimated: from the CVPR-2024 MobileCLIP
  date and the 2021 Apple face-clustering write-up; the exact first-ship dates of Immich/Ente ML were not
  fetched]; what is new since 2024 is *quality per watt* (SigLIP 2, MobileCLIP2) and *OS-level* VLMs
  (Apple iOS 27, Gemini Nano), not the existence of local indexing.

### Q2. Cost curve: captioning and embeddings

Formulas (vendor-documented):
- OpenAI tile models: gpt-4o/gpt-4.1 = 85 base + 170 per 512-px tile; gpt-4o-mini = 2,833 base + 5,667 per
  tile; gpt-5 = 70 + 140. Patch models: tokens = ceil(w/32)·ceil(h/32)·multiplier; gpt-5-nano 1.5,
  gpt-5.4-nano 1.2, gpt-5.6-luna 1.2, gpt-6-astra 1.2; gpt-6-luna is not listed on the vision page
  [sourced: https://developers.openai.com/api/docs/guides/images-vision, 2026]. For gpt-6-luna I assume the
  1.2 multiplier of every other 5.4+/5.6/6-series model [estimated: sibling models' multiplier].
- Gemini: 258 tokens if both sides ≤384 px; else 768-px tiles at 258 tokens each; a 1024² image ≈ 4 tiles
  [sourced: https://aistudio.google.com/docs/image-understanding, 2026].

Prices (per 1M tokens, input/output):
- gpt-4o $2.50/$10.00 (this is the gpt-4o-2024-08-06 price still listed; the 2024-05-13 snapshot is
  "Shut down", 2024-08-06 and 2024-11-20 "Deprecated"; the model page lists one price for all snapshots)
  [sourced: https://developers.openai.com/api/docs/pricing and /models/gpt-4o, 2026]. The May-2024 launch
  price: openai.com returns 403 and web.archive.org is blocked here, so no OpenAI primary page could be
  fetched; LiteLLM's maintained price table lists `gpt-4o-2024-05-13` at $5.00/$15.00 and
  `gpt-4o-2024-08-06` at $2.50/$10.00 per 1M [sourced (secondary, third-party dated table):
  https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json, fetched 2026-11-03].
  Both baselines are shown below.
- gpt-4o-mini $0.15/$0.60 (released 2024-07-18) [sourced: developers.openai.com pricing + changelog].
- gpt-5-nano $0.05/$0.40 (released 2025-08-07). Status is mixed: still listed and billable on the pricing
  page with no deprecation marker, no deprecation entry in the changelog, but the vision guide's footnote
  marks it "Deprecated and scheduled for shutdown" [sourced: developers.openai.com pricing, changelog,
  images-vision guide, 2026]. Treated below as "still purchasable, flagged".
- gpt-5.4-nano $0.20/$1.25 (2026-03-17); gpt-5.6-luna $0.20/$1.20 — after a dated cut: "Starting July 30,
  GPT-5.6 Luna costs 80% less" (2026-07-30), implying a pre-cut price of $1.00/$6.00 [estimated: current
  price ÷ 0.2]; **gpt-6-luna $0.10/$0.50**, released 2026-09-22, "Our most efficient model for focused,
  high-volume tasks", input modalities "Text and images", 1,050,000-token context; batch/flex half price
  [sourced: developers.openai.com pricing, changelog, https://developers.openai.com/api/docs/models/gpt-6-luna, 2026].
- Gemini 2.5 Flash-Lite $0.10/$0.40 (GA 2025-07-22). **Not deprecated**: the deprecations page says
  "`gemini-2.5-flash-lite` is not deprecated and remains available through the API until further notice";
  the pricing page has no deprecation callout for it. (It is `gemini-2.5-flash`, not Flash-Lite, that is
  deprecated and routes to gemini-3.5-flash-lite on 2026-12-01.) Gemini 3.1 Flash-Lite $0.25/$1.50
  (shutdown no earlier than 2027-05-07); Gemini 3.5 Flash-Lite $0.30/$2.50; batch tiers are half price
  [sourced: https://aistudio.google.com/docs/pricing; https://aistudio.google.com/docs/deprecations;
  https://developers.googleblog.com/en/gemini-25-flash-lite-is-now-stable-and-generally-available/, 2025-07-22].

Per-image caption cost, 1024×1024 input, 60 output tokens [estimated: formulas × prices above; standard
(non-batch) tier]:

| Model (date) | Input tokens | Cost / image | Cost / 100k photos |
|---|---|---|---|
| gpt-4o at May-2024 $5/$15 (secondary source) | 765 | $0.0047 | $470 |
| gpt-4o high detail (price as of 2024-08) | 765 | $0.0025 | $250 |
| gpt-4o-mini high detail (2024-07) | 25,501 | $0.0038 | $383 |
| Gemini 2.5 Flash-Lite (2025-07; supported) | 1,032 | $0.00013 | $13 |
| gpt-5-nano (2025-08; billable, flagged on vision page) | 1,536 | $0.00010 | $10 |
| gpt-5.4-nano (2026-03) | 1,229 | $0.00032 | $32 |
| gpt-5.6-luna (2026-07-30 price) | 1,229 | $0.00032 | $32 |
| **gpt-6-luna (2026-09-22)** | 1,229 (assumed 1.2×) | **$0.00015** | **$15** |
| Gemini 3.1 Flash-Lite (2026) | 1,032 | $0.00035 | $35 |
| Gemini 3.5 Flash-Lite (2026) | 1,032 | $0.00046 | $46 |

Batch tiers halve these: gpt-6-luna batch ≈ $0.000077/image ≈ $8 per 100k; Gemini 2.5 Flash-Lite batch
≈ $0.000064/image ≈ $6 per 100k [estimated: batch prices $0.05/$0.25 and $0.05/$0.20 × same tokens].

Reading the curve [estimated: ratios of the table]:
- Versus gpt-4o at its 2024-08 price ($0.0025/image), the cheapest *currently supported, non-flagged*
  frontier-family tiers are **~16x cheaper (gpt-6-luna, $0.00015)** and **~20x cheaper (Gemini 2.5
  Flash-Lite, $0.00013)**; gpt-5-nano is ~25x cheaper. Versus the May-2024 launch price ($0.0047,
  secondary source), those become ~31x / ~37x / ~47x.
- The curve is not monotonic. OpenAI's per-image floor was set by gpt-5-nano in 2025-08 ($0.00010); its
  2026-03 gpt-5.4-nano was 3x pricier per image; then the 2026-07-30 80% cut to gpt-5.6-luna and the
  2026-09-22 gpt-6-luna brought the newest tier back to within 1.5x of the 2025 floor. Google's 2025 tier
  (2.5 Flash-Lite) remains available and is still its cheapest; its 3.1/3.5 Flash-Lite tiers are 2.7–3.6x
  pricier per image [estimated: $0.00035/$0.00013, $0.00046/$0.00013]. Net: the floor was reached in
  mid-2025 and 2026 has held roughly flat around it (OpenAI re-approaching it after a bump; Google holding
  its 2025 tier open), not "drifted up".

Embeddings:
- text-embedding-3-small $0.02/M, -large $0.13/M [sourced: developers.openai.com pricing, 2026]. Launch
  price in Jan 2024 is recalled as identical; the launch post returns 403 [unknown-verified]. Text
  embedding price is flat 2024→2026; no cost curve there.
- Multimodal embeddings are the change: Gemini Embedding 2 image input $0.45/M tokens = "$0.00012 per
  image" (batch $0.225/M = $0.00006) → $12 per 100k photos standard [sourced: aistudio pricing, 2026;
  estimated ×100k]. Voyage voyage-multimodal-3/3.5: $0.60 per billion pixels, floor 50k px, cap 2 MP, i.e.
  $0.00003–$0.0012 per image → $60 per 100k 1-MP images [sourced: https://docs.voyageai.com/docs/pricing,
  2026; estimated ×100k].
- Local SigLIP 2 embedding cost: electricity only [estimated: see Q1 throughput].

### Q3. Face recognition and cross-age clustering

Open models and licenses:
- InsightFace `buffalo_l` (default pack; SCRFD-10GF detector + ResNet50@WebFace600K): LFW 99.83, CFP-FP 99.33,
  AgeDB-30 98.23, IJB-C(E4) 97.25, MR-ALL 91.25; 326 MB. **"available for non-commercial research purposes
  only"** [sourced: https://github.com/deepinsight/insightface/blob/master/python-package/docs/model_zoo.md
  and python-package/README.md]. This is the pack Immich uses by default: `facialRecognition.modelName:
  'buffalo_l'` in the server defaults and the documented config file [sourced: immich config.dto.ts raw;
  https://docs.immich.app/install/config-file, 2026-10-21], and Immich's ML README notes InsightFace's
  permission "does not extend to the redistribution or commercial use of their models by third parties"
  [sourced: https://github.com/immich-app/immich/blob/main/machine-learning/README.md].
  arcface_torch training README: Glint360K r100 IJB-C(1e-4) 97.55, WebFace42M r100 97.70 [sourced:
  https://github.com/deepinsight/insightface/blob/master/recognition/arcface_torch/README.md].
- AdaFace (MIT license): R100 WebFace12M LFW 99.82, CFP-FP 99.26, CPLFW 94.57, **CALFW 96.12, AgeDB 98.00**,
  IJB-C 97.66 [sourced: https://github.com/mk-minchul/AdaFace, README]. This is the commercially usable
  option at parity with buffalo_l.
- Apple Photos: AirFace-style lightweight embedding, ArcFace-style margin loss, greedy + hierarchical
  agglomerative clustering, entirely on-device, "typically overnight during device charging"; the write-up
  does not discuss aging or children growing up [sourced: machinelearning.apple.com recognizing-people-photos, 2021-07-28].
- Google Photos face groups: no claim of cross-age matching; uses clothing cues; "isn't available in all
  geographic regions" [sourced: https://support.google.com/photos/answer/6128838].

Cross-age evidence (falsify "cluster faces across generations"):
- AgeDB protocol (now fetched): AgeDB has "16,488 images ... 568 distinct subjects", ages 1–101, "average age
  range for each subject is 50.3 years"; the verification protocols follow LFW's, "10 folds, with each fold
  consisting of 300 intra-class and 300 [inter]-class pairs", and "in each protocol the age difference of each
  pair's faces is equal to a fixed, predefined value, i.e., 5, 10, 20 and 30 years" — so AgeDB-30 is the
  30-year-gap protocol [sourced: https://ibug.doc.ic.ac.uk/media/uploads/documents/agedb.pdf, CVPR-W 2017].
- Adult cross-age: CALFW (2017) found accuracy "drops about 10%-17% on CALFW" versus LFW for the deep models
  of the time [sourced: https://arxiv.org/abs/1708.08197, 2017-08-28]. By 2022 AdaFace reaches 96.12 on
  CALFW and 98.00 on AgeDB-30 [sourced: AdaFace README]. So adult-to-older-adult over three decades is
  ~solved on clean celebrity benchmarks, and was solved **before 2024** — not a why-now.
- Child → adult, 2017 baseline: Deb, Nain, Jain, "Longitudinal Study of Child Face Recognition" (CLF dataset,
  919 subjects aged 2–18): fused COTS+FaceNet verification TAR@0.1%FAR falls from **90.18% at 1 year to
  73.33% at 3 years**; COTS-A alone 81.94% → 49.33%; "80% of the population ... can be successfully recognized
  at 0.1% FAR ... for an elapsed time of 2.5, 2, and 2.5 years"; prior ITWCC work: "24% TAR at 0.1% FAR" from
  infancy to adulthood [sourced: https://arxiv.org/pdf/1711.03990, 2017-11-10, Table 3 and conclusions].
- Child → child, 2024–2026 results (abstract records via the Consensus index; the IEEE full texts were not
  fetched — secondary): Singh et al., "Longitudinal Evaluation of Child Face Recognition and the Impact of
  Underlying Age" (IJCB 2024), YFA database, 330 subjects aged 3–18 collected over 8 years at 6-month
  intervals: average TAR@0.1%FAR **98.52% at a 2-year gap, 95.68% at 4 years, 87.24% at 6 years, 71.32% at
  8 years**; "highest drop ... in the age group of (3-5) years" [sourced (secondary):
  https://consensus.app/papers/details/8faa260fb22e52a1af017925c5a9005b/, 2024]. Hossain et al. (IJCB 2025),
  infants/toddlers 0–3 years over 24 months with FaceNet/ArcFace/MagFace/CosFace: TAR@0.1%FAR **30.7% for
  0–6 months, 64.7% for 2.5–3 years**; domain-adversarial training "improves TAR by more than 12%"
  [sourced (secondary): https://consensus.app/papers/details/d08223c3e3955057898e6276d04e05bd/, 2025].
  Hossain et al. (WACVW 2026): synthetic-augmented MagFace fine-tuning "substantially reduces error rates"
  on YFA for 6–36-month gaps (no figures in abstract) [sourced (secondary):
  https://consensus.app/papers/details/102afd15f81d54c0bbea8b245eb68024/, 2026].
  Reading: 2024-era ArcFace/MagFace-class models are markedly better than the 2017 COTS/FaceNet result over
  2–4-year gaps (95–98% vs 73–90%), but accuracy still decays to ~71% at 8 years, and **no study of
  child-in-1970 ↔ adult-today (multi-decade) matching was found** [unknown]. The 2024-26 work is academic
  (IJCB/WACV workshops), not a shipped product capability.
- Scanned-print degradation: no benchmark of ArcFace/AdaFace on scanned 1970s prints was found [unknown].

Verdict: "Grandparent in a 1970 print ↔ grandparent today" (adult → aged adult) is feasible with
human confirmation; "child in 1970 print ↔ same person as adult today" remains an open research problem —
the best 2024 longitudinal data covers 8 years of childhood, not decades. The honest product claim is
"assisted merging with user confirmation", not automatic cross-generation clustering. No dated change
since 2024 here that a product could rely on.

### Q4. Scanned prints: restoration, dating, handwritten captions, reverse side

- Restoration: "Bringing Old Photos Back to Life" (CVPR 2020 oral; TPAMI 2022) — scratch detection +
  restoration + face enhancement, MIT license; repo "archived by the owner on Oct 3, 2026 ... read-only"
  [sourced: https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life]. GFPGAN (CVPR 2021), Apache-2.0,
  blind face restoration [sourced: https://github.com/TencentARC/GFPGAN]. Both predate 2024 — no why-now.
  Google Photos' 2025–26 editing posts cover consumer edits, not scanned-print restoration: Nano Banana AI
  templates (2025-11-11); face "touch-up tools" (heal, smooth, under eyes, irises, teeth, eyebrows, lips;
  Android, ≥4 GB RAM; 2026-04-20); Wardrobe / Moods / Remix / portrait editing (2026-09-24). None of the
  three posts mentions restoring old or scanned photos [sourced:
  https://blog.google/products-and-platforms/products/photos/nano-banana-ai-templates-ask-photos/, 2025-11-11;
  https://blog.google/products-and-platforms/products/photos/new-touch-up-tools-google-photos/, 2026-04-20;
  https://blog.google/products-and-platforms/products/photos/google-photos-updates/, 2026-09-24].
- Dating a print: this is a studied task with datasets. "Date Estimation in the Wild" (DEW, Müller et al.,
  2017): "more than one million images crawled from Flickr", acquisition years 1930–1999; CNN baselines
  "already superior to annotations of untrained humans" [sourced (secondary, abstract record):
  https://consensus.app/papers/details/82bb099e50c158f7867ed1d2e0e9d2f2/, 2017]. DEXPERT (ECIR 2024)
  adds DEW-B (balanced, more 1930–1969 images) and reports MAE on the DEW test set: Müller ResNet50 7.12
  years, ConvNext-Base 4.75, DEXPERT 4.55; on DEW-B: ResNet50 5.72, ConvNext 4.10, DEXPERT 4.46; dataset
  available on request for research, no license stated [sourced: https://github.com/cesc47/DEXPERT, ECIR 2024].
  So "which decade" is answerable at ~4–5-year MAE by specialized models — mostly pre-2024 capability
  (2017 dataset; 2024 model), trained on Flickr-era photos, not on family-album scans. VLM zero-shot
  photo-dating is unmeasured [unknown]; the closest proxy is zero-shot *face age* estimation:
  VLAgeBench (2026-03-27) and the 2026-02-08 benchmark in which "The best-performing VLM (Gemini 3 Flash
  Preview, MAE 4.32) surpasses the strongest non-LLM model (MiVOLO, MAE 5.10) by 15%" — i.e. 15% lower MAE
  than an off-the-shelf non-LLM baseline, zero-shot, not "the top specialized model" in general [sourced:
  https://arxiv.org/abs/2603.26015; https://arxiv.org/abs/2602.07815 (v1 2026-02-08, v3 2026-10-24), abstracts].
- Handwritten captions on backs: TrOCR (2021) fine-tuned on IAM handwriting; model card gives no CER
  [sourced: https://huggingface.co/microsoft/trocr-large-handwritten; https://arxiv.org/abs/2109.10282].
  OCRBench v2 (2024-12-31): "most LMMs score below 50 (100 in total)" and are "prone to errors in ...
  handwritten content extraction" [sourced: https://arxiv.org/abs/2501.00321]. PP-OCRv5 (2026-03-25):
  a 5M-parameter OCR "competitive with many billion-parameter VLMs" on standard OCR benchmarks
  [sourced: https://arxiv.org/abs/2603.24373]. Cloud OCR price proxy: AWS Textract Detect Document Text
  $1.50 per 1,000 pages (first 1M), i.e. $0.0015 per print back → $150 per 100k [sourced:
  https://aws.amazon.com/textract/pricing/; estimated ×100k]. Google Cloud Vision/Document AI pricing
  pages did not render [unknown]. A gpt-6-luna or Gemini 2.5 Flash-Lite pass at ~$0.00013–0.00015/image is
  ~10x cheaper than Textract [estimated: Q2 table ÷ $0.0015]. Apple's iOS 27 Foundation Models integrate
  the Vision framework "like OCR for precise text extraction ... all on-device" [sourced:
  developer.apple.com/foundation-models-framework/]. Accuracy on faded cursive on photo paper: [unknown] —
  needs a hands-on test, not a benchmark.
- Reverse-side scanning: a shipping product category. Epson FastFoto FF-680W: "Single-Step Technology"
  lets you "capture both the image and any handwritten notes on the back in a single scan"; "Scan as fast
  as 1 photo per second at 300 dpi" (footnote: average over thirty-six 4"×6" photos); spec "80 ppm/160 ipm";
  "Our Price" $629.99, on sale $529.99 at access time [sourced: https://epson.com/For-Home/Scanners/Photo-Scanners/FastFoto-FF-680W-Wireless-High-speed-Photo-and-Document-Scanning-System/p/B11B237201
  and https://epson.com/fastfoto, accessed 2026-11-03]. So captured backs are a solved input problem for
  users who own a ~$530–630 scanner; the unsolved part is reading them (above). Not a why-now.

### Q5. On-device vs cloud

- Neural Engine is available to third parties through Core ML (`MLComputeUnits.all` /
  `.cpuAndNeuralEngine`, since iOS 12 / macOS 10.14) [sourced: developer.apple.com coreml mlcomputeunits JSON];
  Apple published the ANE transformer reference in 2022 ("up to 10 times faster", "14 times" lower peak memory
  on iPhone 13) [sourced: https://machinelearning.apple.com/research/neural-engine-transformers, 2022-06-06].
  iOS/macOS 27 add Core AI with a Background Inference entitlement for the Neural Engine [sourced: coreai.json].
  Background indexing on iPhone remains constrained by OS scheduling; Apple's own face clustering runs
  "overnight during device charging" [sourced: recognizing-people-photos, 2021]. Ente works around this by
  recommending desktop indexing then sync [sourced: ente.com/ml].
- Apple-silicon CLIP/SigLIP images/sec: [unknown] (see Q1 for what was checked). The only hardware-attributed
  Apple figures are phone-class MobileCLIP latencies (device attribution partly assumed) and Apple's <4 ms
  per-face ANE embedding (2021).
- Cost effect: at the Q1 throughput bound, indexing 100k photos with a B-size CLIP/SigLIP encoder on an
  M-series Mac is on the order of tens of minutes of accelerator time and $0 marginal [estimated: Q1
  17-min bound]; the same job via Gemini Embedding 2 is $12 and via gpt-6-luna captions is ~$15 (batch ~$8)
  [estimated: Q2]. Cloud indexing is already cheap enough that cost alone does not force on-device;
  the on-device argument is trust and the "storage company" killer.
- Trust effect (dated): Google's 2026-10-16 update to the Ask Photos post states that if users enable
  "Connected Content Apps", Photos data "will be processed to personalize other Google experiences",
  "can also be used to show ads" depending on settings, and "can also be used to train generative AI models"
  [sourced: https://blog.google/products/photos/ask-photos-google-io-2024/, update 2026-10-16]. Apple's
  position is the opposite ("not stored or accessible to Apple or anyone else" for PCC) [sourced:
  developer.apple.com/foundation-models-framework/]. A local-first indexer has a concrete, dated trust
  contrast with Google as of October 2026.

### Q6. Assistants and tools over private data (brief)

- MCP announced 2024-11-25 [sourced: https://www.anthropic.com/news/model-context-protocol]. Spec revisions
  2024-11-05, 2025-03-26, 2025-06-18 (OAuth resource servers, elicitation, structured output), 2025-11-25
  (OIDC discovery, URL elicitation, tasks, formal governance), 2026-07-28 [sourced: modelcontextprotocol.io
  changelogs and llms.txt].
- Claude Integrations (remote MCP servers in the consumer app) 2025-05-01; on Pro/Max/Team/Enterprise by
  2025-06-03 [sourced: https://claude.com/blog/integrations].
- Gemini app: "You can connect personal or third-party apps by linking their Model Context Protocol (MCP)
  server" [sourced: https://support.google.com/gemini/answer/13695044, 2026 page].
- ChatGPT: the Apps SDK URL now resolves to "Plugins" docs — plugins = "skills, MCP servers, and optional UI",
  distributed via the ChatGPT Directory, with a path for local MCP servers [sourced:
  https://developers.openai.com/apps-sdk → plugins docs, 2026; launch date not on page — unknown].
- Apple (opposite direction): iOS 27 App Intents "Entity schemas contribute your content to the Spotlight
  semantic index for personal context understanding" so Siri AI can use third-party app content; and the
  Foundation Models `LanguageModel` protocol lets apps call Claude/Gemini from the same API [sourced:
  https://developer.apple.com/ios/; /foundation-models-framework/, 2026].
  Net: "attach a private corpus to any assistant" went from nonexistent (mid-2024) to standard across all
  three assistants (2026). This is the clearest dated change found in this track.

### Q7. Counter-case: native features

- Apple: natural-language photo/video search ("Maya skateboarding in a tie-dye shirt") shipped with iOS 18.1
  on 2024-10-28, U.S. English, on "iPhone 16, iPhone 16 Plus, iPhone 16 Pro, iPhone 16 Pro Max, iPhone 15 Pro,
  iPhone 15 Pro Max, iPad with A17 Pro or M1 and later, and Mac with M1 and later" — so every M1+ Mac
  qualifies; the restriction bites on iPhone (15 Pro / 16+ only) [sourced:
  https://www.apple.com/newsroom/2024/10/apple-intelligence-is-available-today-on-iphone-ipad-and-mac/, 2024-10-28].
  iOS 27 "Siri AI" is "available in beta", "rolling out in English" (6 languages to start), "not initially
  available in the EU", "not available for users under 13", with server-side features "subject to daily
  usage limits"; Photos gets Spatial Reframing/Extend/Clean Up and "load ... up to 70% faster"
  [sourced: https://www.apple.com/ios/, 2026]. The seed's claim that voice photo search is native in iOS 27
  Siri AI holds, with those caveats.
- Google: Ask Photos announced 2024-05-14 (Gemini; "experimental feature rolling out over the coming months")
  [sourced: blog.google 2024-05-14]; "rolling out to more than 100 new countries and regions, and 17 new
  languages", "Available to eligible users with Gemini features in Photos enabled" (2025-11-11); "Ask"
  button on Android and iOS in the U.S. (2026-02-10) [sourced: blog.google posts 2025-11-11, 2026-02-10].
  Later 2026 Photos posts are about editing (touch-up 2026-04-20; Wardrobe, Moods, Remix, portrait editing in
  "Gemini Spark" for AI Pro/Ultra subscribers 2026-09-24) rather than search [sourced: blog.google 2026-04-20,
  2026-09-24].
- Is the delta shrinking? Qualitatively: for **single-library semantic search**, yes, shrinking to ~zero
  on supported devices/regions; both vendors ship it, Apple on-device. For **cross-account merge,
  open-model access, and portability**: neither vendor exposes the photo corpus to a non-house assistant
  (Apple's semantic index serves Siri; Ask Photos serves Gemini), and neither claims cross-age face merging.
  The delta there has not shrunk; but note Apple is moving the *other* direction (third-party content into
  Siri, third-party LLMs into apps), which could let a native-adjacent app close it without migrating data.
  Quantitatively: [unknown] — no public retrieval-quality benchmark comparing Apple Photos / Google Photos
  search against open CLIP/SigLIP retrieval was found; Immich publishes recall scores for its own models
  (84.86 / 85.99 on its eval, 2026-10-21) but Apple and Google publish no comparable figure, so "shrinking
  or growing" cannot be measured from public data.
- Regional/eligibility gaps are the native features' weak spot: Siri AI not in EU at launch; Apple search
  on iPhone needs 15 Pro / 16+ (but any M1+ Mac); Ask Photos "eligible users" only; Google face groups
  "not available in all regions" [sourced: as above]. These are a dated opening, but one Apple/Google can
  close at will.

---

## 3. Seed assumptions tested (this track's remit)

| Assumption | Status | Evidence |
|---|---|---|
| "AI capability is the dated why-now" (rubric) | **partial** | Local indexing (CLIP + faces) existed pre-2024 in Immich/Ente/Queryable; what is dated is (a) OS-level VLM/image APIs (Apple iOS 27 image input + Core AI, Gemini Nano multimodal beta), (b) ~16–25x cheaper cloud captioning than Aug-2024 gpt-4o (floor mid-2025; gpt-6-luna 2026-09-22; Gemini 2.5 Flash-Lite still supported), (c) assistants accepting private corpora via MCP (2024-11 → 2026). (c) is the strongest. |
| A4 (Apple/Google won't ship cross-account merge + open AI access) | **partial / holds so far** | No cross-account merge or open-model corpus access found in Apple iOS 27 or Google Photos 2025–26 posts. But Apple's App Intents semantic index + `LanguageModel` protocol show Apple is building adjacent plumbing. |
| A5 (unit economics clear a consumer price point) — compute part | **holds (compute only)** | Captioning 100k photos ≈ $10–46 cloud standard tier ($6–8 batch) or ~$0 on-device; multimodal embedding $12 (Gemini) / $60 (Voyage) per 100k. Storage economics are Track-E/F territory, not tested here. |
| A6 (assistants accept a private corpus as a tool with low friction) | **holds** | Claude Integrations (2025-05), Gemini app MCP servers (2026), ChatGPT plugins on MCP (2026). Friction level (OAuth, directory review) not measured — Track E. |
| Founder's rejection: voice photo search is native in iOS 27 Siri AI / Google Ask Photos | **holds, with gaps** | Siri AI beta, English-first, no EU, 13+; Ask Photos "eligible users", 100+ countries since 2025-11. |
| Wedge claim: "cluster faces across generations" | **broken for child→adult across decades; partial for adult→aged adult and for short child gaps** | CLF 2017: 90.18% → 73.33% TAR in 3 years; YFA 2024: 98.5% (2 yr) → 71.3% (8 yr) for children; adults 98% on the AgeDB 30-year protocol since ≤2022. No multi-decade child→adult result exists. Also Immich's default face pack (buffalo_l) is non-commercial; AdaFace (MIT) is the usable equivalent. |
| Implicit: handwriting on print backs is machine-readable | **unknown** | Backs are capturable (Epson FastFoto single-step duplex); LMMs weak at handwriting (OCRBench v2); no benchmark on photo-back cursive. Needs a hands-on test. |

---

## 4. Numbers table

| Number | Tag |
|---|---|
| Apple on-device model ~3B params, 2 bits/weight, 300M ViTDet-L vision encoder; KV-cache sharing −37.5% memory | [sourced: machinelearning.apple.com 2025 updates, 2025-06-09] |
| Apple on-device model tokens/s or TTFT | [unknown — not published] |
| `ImageAttachmentContent` introducedAt 27.0 (iOS/macOS/visionOS/watchOS) | [sourced: developer.apple.com foundationmodels imageattachmentcontent.json] |
| Core AI framework introduced 27.0 | [sourced: developer.apple.com coreai.json] |
| PCC free for Small Business Program devs with <2M first-time downloads | [sourced: developer.apple.com/foundation-models-framework/] |
| SigLIP 2 sizes 86M/303M/400M/1B; HF cards 375.2M (B/16 full) and 1,135.7M (So400m-naflex) | [sourced: hf.co/blog/siglip2 2025-02-21; HF Hub API] |
| Gemma 3n E2B 5B raw/1.91B effective/~2 GB; E4B 8B raw/~4B effective/~3 GB; 2025-06-26; encoder up to 60 fps on a Pixel; 256/512/768 px | [sourced: developers.googleblog.com gemma-3n guide; ai.google.dev/gemma/docs/gemma-3n] |
| Gemma 4 licence = Apache-2.0 | [estimated: inferred from the linked page ai.google.dev/gemma/apache_2 being the Apache-2.0 text; terms page last modified 2026-04-01] |
| Qwen2.5-VL 3.75B (qwen-research) / 8.29B (Apache-2.0), 2025-01-26 | [sourced: HF Hub API] |
| Qwen3-VL 2.13B / 4.44B; Apache-2.0; Oct 2025 | [sourced: HF Hub API] |
| Moondream 3: 9B MoE, 2B active, 32K ctx, 2025-09-18; Moondream 2: 2B, last release 2025-06-21, "20–40% faster" | [sourced: moondream.ai blog; hf.co/vikhyatk/moondream2] |
| Florence-2 0.23B / 0.77B, MIT | [sourced: hf.co/microsoft/Florence-2-large] |
| SmolVLM 256M / 500M, 2025-01-23; throughput only on A100 (image) | [sourced: hf.co/blog/smolervlm] |
| Gemini Nano-1 1.8B, Nano-2 3.25B, 4-bit quantized (2023-12-19) | [sourced: arxiv.org/abs/2312.11805 Table 1] |
| Gemini Nano nano-v2/v3/v4 sizes | [unknown — not on ML Kit or developer.android.com pages] |
| MobileCLIP2 image-encoder latency B 10.4 ms, S0 1.5 ms, L/14 57.9 ms, S4 19.6 ms; params S0 11.4M, B 86.3M, L/14 304.3M, S4 321.6M; released 2025-08-28 | [sourced: github.com/apple/ml-mobileclip] |
| Those latencies measured on iPhone 12 Pro Max | [estimated: device named only in the S4 highlight sentence of the same README] |
| MobileCLIP iOS demo "Ideal Latency" S0 2.1 ms, S1 5.8 ms, S2 6.9 ms, B(LT) 13.7 ms (device not stated) | [sourced: github.com/apple/ml-mobileclip/blob/main/ios_app/README.md] |
| Immich 7800X3D (no acceleration, mean of 100 passes): SigLIP2 B/16 5.81 ms, 3,038 MiB, recall 84.86; SO400M-384 56.57 ms, 3,854 MiB, 85.99; ViT-B-32 2.26 ms | [sourced: docs.immich.app/features/searching, 2026-10-21] |
| ~172 img/s and ~18 img/s derived from above | [estimated: 1000/ms] |
| 2-vCPU VPS ~29 img/s, ~1 h per 100k | [estimated: 1/6 of 7800X3D, assumption not measured] |
| 100k photos ≈ 17 min of B-size encoder time on M-series | [estimated: 100,000 × 10.4 ms; assumes M-series ≥ phone-class figure; order-of-magnitude bound] |
| SigLIP/CLIP images/sec on M1–M4 | [unknown — mlx-examples CLIP README, mlx-vlm, Queryable, Apple Core ML cards all checked; none publishes it] |
| Immich defaults: face `buffalo_l`, CLIP `ViT-B-32__openai`, minScore 0.7, maxDistance 0.5, minFaces 3 | [sourced: immich server/src/dtos/config.dto.ts raw; docs.immich.app/install/config-file 2026-10-21] |
| Apple face embedding <4 ms, 8x vs GPU; clustering 3.5 s vs 205.8 s | [sourced: machinelearning.apple.com recognizing-people-photos, 2021-07-28] |
| EmbeddingGemma 2 on-device: 768-d, 256 tokens, 140 soft tokens/image, ≤768 px short side | [sourced: developers.google.com/ml-kit/genai/embedding/android] |
| Gemini Nano device lists (nano-v2/v3/v4) | [sourced: developers.google.com/ml-kit/genai] |
| gpt-4o $2.50/$10; gpt-4o-mini $0.15/$0.60; gpt-5-nano $0.05/$0.40; gpt-5.4-nano $0.20/$1.25; gpt-5.6-luna $0.20/$1.20; gpt-6-luna $0.10/$0.50 (batch $0.05/$0.25); text-embedding-3-small $0.02 | [sourced: developers.openai.com/api/docs/pricing] |
| gpt-6-luna released 2026-09-22; GPT-5.6 Luna −80% on 2026-07-30; gpt-5.4-nano 2026-03-17; gpt-5-nano 2025-08-07; gpt-4o-mini 2024-07-18 | [sourced: developers.openai.com/api/docs/changelog] |
| gpt-5.6-luna pre-cut price $1.00/$6.00 | [estimated: current price ÷ 0.2] |
| gpt-4o May-2024 $5/$15 | [sourced (secondary): LiteLLM model_prices_and_context_window.json entry gpt-4o-2024-05-13; no OpenAI primary page reachable] |
| Image tokens: gpt-4o 85+170/tile; gpt-4o-mini 2,833+5,667/tile; gpt-5 70+140; multipliers 1.5 (5-nano), 1.2 (5.4-nano, 5.6-luna, 6-astra), 2.46 (4.1-nano) | [sourced: developers.openai.com images-vision guide] |
| gpt-6-luna image multiplier 1.2 | [estimated: not on vision page; sibling models' value] |
| Gemini 258 tokens/≤384 px image or per 768-px tile; 3,600 images/request; 20 MB inline | [sourced: aistudio.google.com/docs/image-understanding] |
| Gemini 2.5 Flash-Lite $0.10/$0.40 (batch $0.05/$0.20; GA 2025-07-22; not deprecated); 2.5 Flash deprecated → 3.5 Flash-Lite 2026-12-01; 3.1 Flash-Lite $0.25/$1.50 (shutdown ≥2027-05-07); 3.5 Flash-Lite $0.30/$2.50; Embedding 2 image $0.45/M = $0.00012/image (batch $0.00006); gemini-embedding-001 $0.15 | [sourced: aistudio.google.com/docs/pricing; /docs/deprecations; developers.googleblog.com 2.5 Flash-Lite GA post] |
| Voyage multimodal $0.60/B pixels, $0.00003–$0.0012/image; text $0.02–$0.12/M | [sourced: docs.voyageai.com/docs/pricing] |
| Per-image caption costs ($0.0047 gpt-4o May-24 … $0.0025 gpt-4o Aug-24 … $0.00015 gpt-6-luna … $0.00013 Gemini 2.5 FL … $0.00010 gpt-5-nano … $0.00046 Gemini 3.5 FL) and per-100k ($10–$470); batch $6–8/100k | [estimated: formulas × prices, 1024² image, 60 output tokens] |
| 16x / 20x / 25x decline vs Aug-2024 gpt-4o; 31x / 37x / 47x vs May-2024 | [estimated: ratios above] |
| Google 3.1/3.5 Flash-Lite 2.7–3.6x the 2.5 Flash-Lite per-image cost | [estimated: $0.00035/$0.00013, $0.00046/$0.00013] |
| buffalo_l: LFW 99.83, CFP-FP 99.33, AgeDB-30 98.23, IJB-C 97.25, MR-ALL 91.25, 326 MB; non-commercial | [sourced: insightface model_zoo.md] |
| AdaFace R100 WebFace12M: LFW 99.82, CFP-FP 99.26, CPLFW 94.57, CALFW 96.12, AgeDB 98.00, IJB-C 97.66; MIT | [sourced: github.com/mk-minchul/AdaFace] |
| arcface_torch Glint360K r100 IJB-C 97.55; WebFace42M r100 97.70 | [sourced: insightface arcface_torch README] |
| AgeDB: 16,488 images, 568 subjects, ages 1–101, avg range 50.3 yr; protocols 10 folds × 300+300 pairs at 5/10/20/30-year gaps | [sourced: ibug.doc.ic.ac.uk agedb.pdf, 2017] |
| CALFW: accuracy "drops about 10%-17%" vs LFW (2017) | [sourced: arxiv.org/abs/1708.08197] |
| CLF children: Fused TAR@0.1%FAR 90.18% (1 yr) → 73.33% (3 yr); COTS-A 81.94% → 49.33%; 80% recognizable for 2–2.5 yrs; ITWCC 24% TAR | [sourced: arxiv.org/pdf/1711.03990, 2017-11-10] |
| YFA (IJCB 2024): 330 subjects aged 3–18, 8 years, 6-month intervals; TAR@0.1%FAR 98.52% (2 yr), 95.68% (4 yr), 87.24% (6 yr), 71.32% (8 yr) | [sourced (secondary): Consensus abstract record 8faa260f…, Singh et al. 2024] |
| Infants/toddlers (IJCB 2025): TAR@0.1%FAR 30.7% (0–6 mo), 64.7% (2.5–3 yr); DANN +12% TAR | [sourced (secondary): Consensus abstract record d08223c3…, Hossain et al. 2025] |
| DEW: >1M Flickr images, 1930–1999 (2017); DEXPERT MAE 4.55 yr on DEW (ResNet50 baseline 7.12; ConvNext 4.75); DEW-B 4.46 / 4.10 / 5.72 | [sourced: github.com/cesc47/DEXPERT (ECIR 2024); DEW figures via Consensus abstract record (secondary)] |
| VLM age estimation: best VLM MAE 4.32 (Gemini 3 Flash Preview) vs MiVOLO 5.10 = 15% lower; VLM avg 5.65 vs non-LLM 9.88; 34 models, 8 datasets | [sourced: arxiv.org/abs/2602.07815, 2026-02-08] |
| Epson FastFoto FF-680W: 1 photo/s at 300 dpi; 80 ppm/160 ipm; $629.99 (sale $529.99); scans backs in one pass | [sourced: epson.com product page, accessed 2026-11-03] |
| Textract $1.50 / 1,000 pages (first 1M), $0.60 after; free 1,000 pages/mo | [sourced: aws.amazon.com/textract/pricing/] |
| OCRBench v2: most LMMs <50/100; 10,000 QA pairs; 31 scenarios | [sourced: arxiv.org/abs/2501.00321, 2024-12-31] |
| PP-OCRv5 5M params | [sourced: arxiv.org/abs/2603.24373, 2026-03-25] |
| ANE transformers: up to 10x faster, 14x lower peak memory (iPhone 13), 2022-06-06 | [sourced: machinelearning.apple.com neural-engine-transformers] |
| MCP dates 2024-11-25 (announce); specs 2024-11-05, 2025-03-26, 2025-06-18, 2025-11-25, 2026-07-28 | [sourced: anthropic.com; modelcontextprotocol.io] |
| Claude Integrations 2025-05-01; broadened 2025-06-03 | [sourced: claude.com/blog/integrations] |
| Apple NL photo search 2024-10-28 (iOS 18.1; iPhone 15 Pro/16+, iPad A17 Pro/M1+, Mac M1+); Visual Intelligence 2024-12-11; iOS 26 2025-06-09 | [sourced: Apple newsroom posts on those dates] |
| iOS 27 Photos "up to 70% faster" (50,000-asset library test) | [sourced: apple.com/ios] |
| Ask Photos 2024-05-14; +100 countries/17 languages 2025-11-11; Ask button 2026-02-10; touch-up tools 2026-04-20 (Android, ≥4 GB RAM); Wardrobe/Moods/Remix 2026-09-24 | [sourced: blog.google posts] |
| Google data-use update 2026-10-16 (Photos data → personalization, ads, gen-AI training if enabled) | [sourced: blog.google ask-photos post, update note] |
| GPU-VPS cost per hour; Nano install-base share; Apple/Google native search retrieval quality | [unknown] |

---

## 5. Unknowns we could not resolve

1. GPT-4o's May-2024 list price from an OpenAI primary page — openai.com returns 403 and web.archive.org is
   blocked from this environment; the $5/$15 figure rests on LiteLLM's dated third-party table.
2. Published SigLIP 2 / CLIP images-per-second on M1–M4 (MLX or Core ML). Checked: mlx-examples CLIP README,
   mlx-vlm README, Apple ml-mobileclip README + iOS app README + Core ML HF card, Queryable README. None
   publishes it; WebSearch was unavailable for community benchmarks.
3. Absolute throughput of Qwen2.5/3-VL small, Moondream 2/3, Florence-2, SmolVLM and Apple's on-device 3B
   on M-series or a VPS; GPU-VPS hourly cost.
4. Whether any 2024–2026 face model handles child→adult matching across *decades*; the best new data (YFA)
   covers 8 years of childhood; IEEE full texts not fetched (abstract records only).
5. Accuracy of any OCR (TrOCR, PP-OCRv5, gpt-6-luna, Gemini Flash-Lite, Apple Vision) on faded handwriting
   on photo backs; no benchmark exists for that domain.
6. VLM zero-shot accuracy at dating a *scanned print* (DEW/DEXPERT cover Flickr-era photos with specialized
   models; no VLM result).
7. Gemini Nano nano-v2/v3/v4 parameter counts, install-base share, and GA timing for the Prompt/Embedding
   APIs (still beta/preview).
8. Launch date of ChatGPT Apps SDK / plugins (page undated; 403 on openai.com) — Track E.
9. Google Cloud Vision / Document AI handwriting pricing (pages did not render).
10. gpt-6-luna's image-token multiplier (absent from the vision guide; 1.2 assumed).
11. Real-world precision of Immich/Ente clustering on multi-decade family archives — no primary data.
12. Any quantitative native-vs-open retrieval-quality comparison (Q7).

---

## 6. "Why now" scorecard

Strength 1–10 = how strong and how *dated since 2024* the change is. Defensible = whether the same change
helps a startup at least as much as it helps Apple/Google.

| Candidate why-now | Strength | Evidence (dated) | Defensible? |
|---|---|---|---|
| **Assistants accept private corpora as tools (MCP)** | **8** | MCP 2024-11-25; Claude Integrations 2025-05-01; Gemini app MCP servers 2026; ChatGPT plugins on MCP 2026; spec rev 2026-07-28 | Partly. It lets any assistant read a user-owned corpus; Apple/Google have *not* exposed their photo corpora this way (Siri index, Ask Photos are closed). Risk: Apple's App Intents semantic index goes the other way and could make a native-adjacent app sufficient. |
| **OS-level on-device VLM/image APIs** | **7** | Apple Foundation Models image input + Core AI at iOS 27.0 (WWDC26, 2026); PCC free for small devs; Gemini Nano Prompt API multimodal (beta), Embedding API (preview) | Weakly. Apple built this for every developer; it removes the startup's compute cost but equally lowers barriers for every photo app and for Apple itself. Device-gated: Apple Intelligence requires iPhone 15 Pro / 16+ or M1+ Mac/iPad [sourced: Apple newsroom 2024-10-28]; Gemini Nano runs only on the listed Pixel/Samsung/OEM flagship models [sourced: ML Kit device list], which are 2024–26 releases [estimated: from the model names in that list]. |
| **Cloud captioning cost collapse** | **7** | Per image, the cheapest supported non-flagged tiers are ~16x (gpt-6-luna, 2026-09-22) and ~20x (Gemini 2.5 Flash-Lite, GA 2025-07-22, not deprecated) cheaper than gpt-4o at 2024-08 prices, ~31–37x vs May-2024 (secondary); gpt-5-nano ~25x; dated 80% cut to GPT-5.6 Luna 2026-07-30; 100k photos ≈ $10–46 standard, $6–8 batch. Floor reached mid-2025; 2026 roughly flat around it, not rising. | No. Same prices for everyone. It does fix A5's compute leg, and the 2026 cut/launch dates show vendors still competing downward at the low end. |
| **Open embedding/VLM quality per watt** | **5** | SigLIP 2 (2025-02), MobileCLIP2 (2025-08), Qwen3-VL 2B/4B (2025-10), Gemma 3n (2025-06), SmolVLM (2025-01); all Apache/MIT except Gemma 3n and Qwen2.5-VL-3B | No. Immich/Ente already ship these; Apple/Google have better in-house models. It makes a startup *possible*, not *distinct*. |
| **Trust contrast with Google** | **5** | Google 2026-10-16: connected Photos data may personalize other services, serve ads, train gen-AI if user opts in | Yes versus Google, no versus Apple (Apple's PCC privacy story is stronger than a startup's). Policy, not capability; can be reversed. |
| **Handwriting OCR on print backs via VLMs** | **4** | Cheap ($0.00013–0.00015/image) and backs are capturable (Epson FastFoto single-step duplex, ~$530–630), but LMMs documented weak on handwriting (2024-12); specialized 5M-param OCR (2026-03) rivals VLMs on standard benchmarks | Partly — niche enough that Apple/Google may not bother; accuracy unproven. |
| **Photo dating (which decade)** | **3** | Specialized models reach ~4.5-year MAE on Flickr-era photos (DEW 2017; DEXPERT ECIR 2024); VLM zero-shot unmeasured | No — mostly pre-2024 capability; Apple/Google can ship it trivially if they care. |
| **Cross-generation face clustering** | **2** | Adult cross-age solved pre-2024 (AdaFace 2022, AgeDB-30 98%); child→adult: 2017 CLF 90% → 73% in 3 yrs; 2024 YFA 98.5% (2 yr) → 71.3% (8 yr); no multi-decade child→adult result; default open pack non-commercial | Not a why-now at all. Any claim must be "assisted, user-confirmed merging". |
| **Native features leave regional/eligibility gaps** | **3** | Siri AI not in EU, 13+, English-first (2026); Apple search needs iPhone 15 Pro+ (any M1 Mac works); Ask Photos "eligible users"; face groups not all regions | No — gaps close at Apple/Google's discretion. |

Bottom line for the rubric: AI capability alone is **not** the dated change — local CLIP/face indexing
predates 2024 and Apple/Google now ship semantic search natively. The defensible dated change is the
combination of (1) assistants that can be pointed at a user-owned corpus (2024-11 → 2026, all three
vendors) with (2) OS-level on-device models that make a zero-marginal-cost, privacy-preserving indexer
feasible for a small team (iOS 27, 2026), with (3) cloud captioning now cheap enough (~$15 per 100k photos
standard, ~$8 batch, as of 2026-09) that the cloud fallback is a rounding error in unit economics. The
family-archive wedge's "cross-generation faces" claim does not survive the evidence and should be
rewritten as assisted, user-confirmed merging.

---

## 7. Full source list (all accessed 2026-11-03)

Apple
1. https://developer.apple.com/tutorials/data/documentation/foundationmodels.json
2. https://developer.apple.com/tutorials/data/documentation/foundationmodels/analyzing-images-with-multimodal-prompting.json
3. https://developer.apple.com/tutorials/data/documentation/foundationmodels/imageattachmentcontent.json
4. https://developer.apple.com/tutorials/data/documentation/coreai.json
5. https://developer.apple.com/tutorials/data/documentation/coreml/mlcomputeunits.json
6. https://developer.apple.com/tutorials/data/documentation/ios-ipados-release-notes/ios-ipados-27-release-notes.json
7. https://developer.apple.com/foundation-models-framework/
8. https://developer.apple.com/ios/
9. https://developer.apple.com/videos/play/wwdc2025/286/
10. https://developer.apple.com/videos/play/wwdc2026/242/
11. https://machinelearning.apple.com/research/apple-foundation-models-2025-updates (2025-06-09; note 2026-09-09)
12. https://machinelearning.apple.com/research/recognizing-people-photos (2021-07-28)
13. https://machinelearning.apple.com/research/neural-engine-transformers (2022-06-06)
14. https://github.com/apple/ml-mobileclip (2025-08-28); https://github.com/apple/ml-mobileclip/blob/main/ios_app/README.md
15. https://www.apple.com/newsroom/2024/06/introducing-apple-intelligence-for-iphone-ipad-and-mac/ (2024-06-10)
16. https://www.apple.com/newsroom/2024/10/apple-intelligence-is-available-today-on-iphone-ipad-and-mac/ (2024-10-28)
17. https://www.apple.com/newsroom/2024/12/apple-intelligence-now-features-image-playground-genmoji-and-more/ (2024-12-11)
18. https://www.apple.com/newsroom/2025/06/apple-elevates-the-iphone-experience-with-ios-26/ (2025-06-09)
19. https://www.apple.com/ios/ (iOS 27 marketing page, 2026)
19a. https://huggingface.co/apple/coreml-mobileclip (CVPR 2024; card updated 2024-11-19)
19b. https://huggingface.co/apple/MobileCLIP2-S4 (licence apple-amlr)
19c. https://github.com/apple/ml-fastvlm (CVPR 2025)

Google
20. https://developers.google.com/ml-kit/genai
21. https://developers.google.com/ml-kit/genai/prompt/android
22. https://developers.google.com/ml-kit/genai/embedding/android
23. https://developer.android.com/ai/gemini-nano
24. https://ai.google.dev/gemma/docs/gemma-3n
25. https://ai.google.dev/gemma/terms (last modified 2026-04-01); https://ai.google.dev/gemma/apache_2 (Apache-2.0 text)
26. https://developers.googleblog.com/en/introducing-gemma-3n-developer-guide/ (2025-06-26)
27. https://aistudio.google.com/docs/pricing
27a. https://aistudio.google.com/docs/deprecations
27b. https://developers.googleblog.com/en/gemini-25-flash-lite-is-now-stable-and-generally-available/ (2025-07-22)
28. https://aistudio.google.com/docs/image-understanding
29. https://blog.google/products/photos/ask-photos-google-io-2024/ (2024-05-14; update 2026-10-16)
30. https://blog.google/products/photos/rss/
31. https://blog.google/products-and-platforms/products/photos/nano-banana-ai-templates-ask-photos/ (2025-11-11)
32. https://blog.google/products-and-platforms/products/photos/ask-button-ask-photos-tips/ (2026-02-10)
32a. https://blog.google/products-and-platforms/products/photos/new-touch-up-tools-google-photos/ (2026-04-20)
33. https://blog.google/products-and-platforms/products/photos/google-photos-updates/ (2026-09-24)
34. https://support.google.com/photos/answer/6128838
35. https://support.google.com/gemini/answer/13695044
36. https://huggingface.co/blog/siglip2 (2025-02-21); https://arxiv.org/abs/2502.14786
36a. https://arxiv.org/abs/2312.11805 (Gemini 1.0 report, 2023-12-19; Table 1 via HF papers mirror)

OpenAI / Anthropic / MCP / Voyage
37. https://developers.openai.com/api/docs/pricing
37a. https://developers.openai.com/api/docs/models/gpt-6-luna
38. https://developers.openai.com/api/docs/guides/images-vision
39. https://developers.openai.com/api/docs/changelog
40. https://developers.openai.com/api/docs/models/gpt-4o
40a. https://raw.githubusercontent.com/BerriAI/litellm/main/model_prices_and_context_window.json (secondary, dated price table)
41. https://developers.openai.com/apps-sdk (resolves to Plugins docs)
42. https://www.anthropic.com/news/model-context-protocol (2024-11-25)
43. https://claude.com/blog/integrations (2025-05-01)
44. https://modelcontextprotocol.io/specification/2025-06-18/changelog
45. https://modelcontextprotocol.io/specification/2025-11-25/changelog
46. https://modelcontextprotocol.io/llms.txt
47. https://docs.voyageai.com/docs/pricing
48. https://aws.amazon.com/textract/pricing/

Models, papers, OSS
49. Hugging Face Hub API cards: google/siglip2-so400m-patch16-naflex, google/siglip2-base-patch16-224, google/gemma-3n-E4B-it, moondream/moondream3-preview, Qwen/Qwen3-VL-2B-Instruct, Qwen/Qwen3-VL-4B-Instruct, Qwen/Qwen2.5-VL-3B-Instruct, Qwen/Qwen2.5-VL-7B-Instruct, HuggingFaceTB/SmolVLM-256M-Instruct, microsoft/Florence-2-base, microsoft/trocr-large-handwritten, vikhyatk/moondream2
50. https://huggingface.co/blog/smolervlm (2025-01-23)
51. https://huggingface.co/microsoft/Florence-2-large
52. https://huggingface.co/microsoft/trocr-large-handwritten; https://arxiv.org/abs/2109.10282
53. https://moondream.ai/blog/moondream-3-preview (2025-09-18); https://moondream.ai/licenses/model/1.0 (2026-07-07); https://huggingface.co/vikhyatk/moondream2
54. https://github.com/mk-minchul/AdaFace
55. https://github.com/deepinsight/insightface/blob/master/python-package/README.md
56. https://github.com/deepinsight/insightface/blob/master/python-package/docs/model_zoo.md
57. https://github.com/deepinsight/insightface/blob/master/recognition/arcface_torch/README.md
58. https://arxiv.org/abs/1711.03990 and https://arxiv.org/pdf/1711.03990 (Deb, Nain, Jain, 2017-11-10)
59. https://arxiv.org/abs/1708.08197 (CALFW, 2017-08-28)
59a. https://ibug.doc.ic.ac.uk/media/uploads/documents/agedb.pdf (AgeDB, CVPR-W 2017; text extracted locally with pdftotext)
59b. Consensus abstract records (secondary): Singh et al. IJCB 2024 https://consensus.app/papers/details/8faa260fb22e52a1af017925c5a9005b/; Hossain et al. IJCB 2025 https://consensus.app/papers/details/d08223c3e3955057898e6276d04e05bd/; Hossain et al. WACVW 2026 https://consensus.app/papers/details/102afd15f81d54c0bbea8b245eb68024/; Müller et al. 2017 DEW https://consensus.app/papers/details/82bb099e50c158f7867ed1d2e0e9d2f2/
59c. https://github.com/cesc47/DEXPERT (ECIR 2024)
60. https://arxiv.org/abs/2501.00321 (OCRBench v2, 2024-12-31)
61. https://arxiv.org/abs/2603.24373 (PP-OCRv5, 2026-03-25)
62. https://arxiv.org/abs/2603.26015; https://arxiv.org/abs/2602.07815 (VLM age estimation, 2026)
63. https://github.com/microsoft/Bringing-Old-Photos-Back-to-Life (archived 2026-10-03)
64. https://github.com/TencentARC/GFPGAN
65. https://github.com/ml-explore/mlx-examples/blob/main/clip/README.md
65a. https://github.com/Blaizzy/mlx-vlm
65b. https://github.com/mazzzystar/Queryable
66. https://docs.immich.app/features/searching (stamp 2026-10-21)
67. https://docs.immich.app/features/facial-recognition (2026-10-21)
68. https://docs.immich.app/administration/system-settings
68a. https://docs.immich.app/install/config-file (2026-10-21)
68b. https://raw.githubusercontent.com/immich-app/immich/main/server/src/dtos/config.dto.ts
68c. https://github.com/immich-app/immich/blob/main/machine-learning/README.md
69. https://ente.com/ml/
70. https://epson.com/For-Home/Scanners/Photo-Scanners/FastFoto-FF-680W-Wireless-High-speed-Photo-and-Document-Scanning-System/p/B11B237201; https://epson.com/fastfoto

---

## Audit log

Each auditor finding and what was done (all re-verified by direct fetch on 2026-11-03 unless noted).

Untagged numbers
- L97 "100k photos ≈ 17 min": rewritten as an explicit `[estimated: 100,000 × 10.4 ms; assumes M-series ≥
  phone-class figure]` order-of-magnitude bound, with the dependency on the device-attribution assumption
  stated; also added to the numbers table.
- L102 "self-hosted apps have had CLIP + face clustering since 2023": replaced with a tagged `[estimated]`
  claim grounded in the dated sources that were fetched (Apple MobileCLIP Core ML CVPR 2024 card, Apple's
  2021 face-clustering write-up, Queryable) and an explicit note that Immich/Ente first-ship dates were
  not fetched.
- L142-143 Google 3.x Flash-Lite "2.5–3x" and "floor reached in 2025 and drifted up": recomputed and tagged
  (2.7–3.6x `[estimated]`); the trend sentence rewritten (see major findings below).
- L72 "nano-v2 = 2024-25 Chinese OEM flagships": replaced by the verbatim device list from the ML Kit page.
- L374 scorecard "2023+ Pro iPhones; 2024+ Android flagships": replaced with the sourced Apple device rule and
  the sourced Nano device list, with the "2024–26 releases" characterization tagged `[estimated]`.
- L83 "f32": removed; now quotes the page's "without acceleration" and "mean of 100 passes".

Suspect claims
- (major) Gemini 2.5 Flash-Lite "deprecated; routes to 3.5 Flash-Lite 2026-12-01": corrected. Re-fetched
  pricing page (no deprecation callout on 2.5 Flash-Lite; the 2026-12-01 routing is for `gemini-2.5-flash`)
  and the deprecations page ("`gemini-2.5-flash-lite` is not deprecated and remains available through the API
  until further notice"). Table row relabelled "supported"; GA date 2025-07-22 added from Google's blog.
- (major) gpt-6-luna omitted: added ($0.10/$0.50, image input confirmed on its model page, released
  2026-09-22 per changelog, batch $0.05/$0.25), plus the 2026-07-30 "GPT-5.6 Luna costs 80% less" cut
  (pre-cut price tagged as an estimate). The cost-curve conclusion, §3 row 1, scorecard row 3 and the bottom
  line were rewritten: cheapest supported tiers ~16x/~20x cheaper than Aug-2024 gpt-4o; floor mid-2025,
  2026 roughly flat, not rising.
- (minor) buffalo_l "applies to the packs Immich uses by default" unsupported by cited pages: now sourced to
  Immich's `server/src/dtos/config.dto.ts` defaults (`modelName: 'buffalo_l'`), the documented config file
  on docs.immich.app/install/config-file (2026-10-21), and the ML README's InsightFace licence note; the
  feature page's lack of a model name is stated.
- (minor) nano-v2 "Chinese OEM": replaced with the verbatim list (includes Motorola and Samsung).
- (minor) Gemma 4 Apache-2.0: re-fetched terms page (links "Gemma 4 license" → ai.google.dev/gemma/apache_2)
  and the linked page (Apache License 2.0 text, no mention of Gemma 4); tagged `[estimated: inferred from
  the linked page]`.
- (minor) VLM age estimation "15% better than the top specialized model": re-fetched abstract; now quotes
  "surpasses the strongest non-LLM model (MiVOLO, MAE 5.10) by 15%" and states it is a zero-shot comparison
  against an off-the-shelf non-LLM baseline; dates corrected to v1 2026-02-08 / v3 2026-10-24.
- (minor) MobileCLIP2 latencies "on iPhone 12 Pro Max": re-fetched README; the table has no device column
  and the device appears only in the S4 highlight sentence. Device attribution moved to a separate
  `[estimated]` row; Core ML card and iOS-app README added (no device named there either).
- (minor) Google Photos restoration cites: fetched the Photos RSS feed and identified the 2026-04-20 post
  (face touch-up tools, Android, ≥4 GB RAM) and fetched it; it does not mention restoration. Text rewritten to
  say which post announced what and that none covers scanned-print restoration; URL added to source list.
- (minor) Apple NL search "iPhone 15 Pro/16+ only": re-fetched newsroom post; now quotes the full device list
  including iPad A17 Pro/M1+ and Mac M1+, and notes the Mac case explicitly in Q7 and the scorecard.
- (minor) "≥100 img/s on M-series" extrapolation: removed. mlx-examples CLIP README re-fetched (no numbers)
  and reported as such; mlx-vlm, Queryable, Apple Core ML cards checked and reported; Apple-silicon img/s
  marked `[unknown]` with the search trail; the 17-min figure kept only as a tagged bound.
- (minor) gpt-5-nano "deprecated": re-fetched pricing page (listed, no marker), changelog (no deprecation
  entry) and vision guide (footnote "Deprecated and scheduled for shutdown"); text and table now say
  "billable, flagged on vision page" and the headline ratios use non-flagged tiers.

Broken or misquoted sources
- aistudio pricing / deprecations: fixed as above.
- developers.openai.com pricing / gpt-6-luna / changelog: fixed as above.
- ai.google.dev/gemma/terms: fixed as above.
- developers.google.com/ml-kit/genai: device list corrected; "beta"/"Prompt API" wording now attributed to
  /ml-kit/genai/prompt/android only.
- arxiv 2602.07815: paraphrase fixed.
- docs.immich.app facial-recognition / system-settings: no longer used to support the default-model claim.
- github.com/apple/ml-mobileclip: device attribution fixed.
- docs.immich.app/features/searching: "f32" removed.
- blog.google 2026-04-20: URL found via RSS and added.
- arxiv.org/pdf/1711.03990: confirmed by auditor; unchanged.
- Verified-as-stated items: unchanged.

Missing vs brief
- Q1 throughput per model: added Gemma 3n encoder 60 fps on Pixel (sourced), Moondream 2 relative speedup,
  SmolVLM (A100-only chart), FastVLM TTFT claim (no hardware), Apple 3B (no published figure), mlx-vlm
  Apple-silicon figures (Gemma 4 only); remaining absolute figures marked `[unknown]`; GPU-VPS cost `[unknown]`.
- Q1 Qwen2.5-VL: added (3B 3.75B qwen-research; 7B 8.29B Apache-2.0; 2025-01-26). Gemma 3n image input now
  stated ("natively supports image, audio, video, and text inputs").
- Q1 Gemini Nano size: added Nano-1 1.8B / Nano-2 3.25B, 4-bit, from the Gemini 1.0 report (via HF papers
  mirror); developer.android.com/ai/gemini-nano fetched and reported as giving no sizes; nano-v2/v3/v4 sizes
  remain `[unknown]`.
- Q2 GPT-4o May-2024 price: web.archive.org is blocked here (documented); the OpenAI gpt-4o model page lists
  one price for all snapshots; LiteLLM's raw dated price table fetched and used as a clearly-labelled
  secondary source ($5/$15 for gpt-4o-2024-05-13); both baselines shown. Cheapest 2026 model re-identified
  as gpt-6-luna / non-deprecated Gemini 2.5 Flash-Lite.
- Q4 reverse-side scanning: Epson FastFoto FF-680W product page fetched (single-step two-sided capture of
  handwritten notes, 1 photo/s, $629.99 list / $529.99 sale).
- Q4 dating a print: DEW (2017) and DEXPERT/DEW-B (ECIR 2024) found and quoted (MAE 4.55 / 4.46 years);
  VLM zero-shot still `[unknown]`; scorecard row added.
- Q5 Apple-silicon benchmarks: mlx-examples README result reported (none); other candidate sources checked
  and reported; `[unknown]` retained with the search trail; 17-min figure tagged.
- Q3 AgeDB-30 protocol: AgeDB paper PDF fetched and text-extracted; protocol quoted (5/10/20/30-year gaps,
  10 folds × 300+300 pairs). 2024–26 cross-age work: Singh et al. IJCB 2024 (YFA), Hossain et al. IJCB 2025
  and WACVW 2026 added via Consensus abstract records (labelled secondary; IEEE full texts not fetched).
- Q7 quantitative delta: explicitly marked `[unknown]` with the reason (no public Apple/Google retrieval
  benchmark; only Immich publishes recall).
- Scorecard row 3 re-scored (6 → 7) on the corrected evidence; bottom line updated.

Not done (tooling): WebSearch budget was exhausted for the whole repair, so community benchmarks and any
page whose URL I could not derive were out of reach; those gaps are listed in §5 rather than filled.
