# Academic Paper to TTS Generation Report
**Host Machine:** NUC (Windows)
**Date:** February 12, 2026

## 1. Project Overview
This report documents the end-to-end process of converting a full-length academic paper into a professional, neutral-tone audiobook using the Qwen3-TTS 0.6B model on local hardware.

## 2. Source Information
- **Original File:** `C:\Users\akona\OneDrive\Dev\Public-VS-Private\Debunking_Blockchain_Global_v2.md`
- **Content:** "Debunking Blockchain" (Comprehensive Analysis)
- **Size:**
  - Characters: 133,038
  - Words: 18,215
  - Semantic Chunks: 229 (Generated via paragraph and sentence splitting)

## 3. Generation Infrastructure
### Target Script
The generation was handled by a custom-optimized narrator script:
- **Script Path:** `scripts/paper_to_audio.py`
- **Key Feature:** Multi-chunk batch processing with dynamic VRAM management (`clamp_batch_size`).

### Hardware Configuration (NUC)
- **Device:** NVIDIA GPU (via CUDA)
- **Attention Implementation:** `sdpa` (Scaled Dot Product Attention)
- **Precision:** `bfloat16` (BF16)

## 4. Sampling & Tone Optimization
To avoid the unstable/emotional prosody common in the 0.6B model, "Academic Neutrality" was enforced via the following sampling parameters:
- **Temperature:** `0.4` (Constrains randomness to stabilize pitch)
- **Top_P:** `0.7` (Nucleus sampling)
- **Repetition Penalty:** `1.1`
- **Model Variant:** Qwen3-TTS-12Hz-0.6B-CustomVoice

## 5. Performance Results (nuc_test.md)
The following throughput was observed during the generation run:

| Metric | Value |
| :--- | :--- |
| **Batch Size** | 4 chunks/batch |
| **Avg. Time per Batch** | ~121 seconds |
| **Efficiency Factor** | 2.43x speedup vs. sequential mode |
| **Character Rate** | ~6.5 chars per second |
| **Total Runtime** | ~1 hour 55 minutes |

## 6. Output Artifacts
- **Output Directory:** `output/Debunking_Blockchain_Neutral_Full/`
- **Final Result:** `full_audiobook.wav` (Merged from 229 individual parts)

---
*Report generated for user: akona*
