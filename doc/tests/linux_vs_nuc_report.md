# NUC vs Linux TTS Paper Benchmark (Qwen3-TTS 0.6B)
**Date:** 2026-02-12

This compares the NUC reference run against two Linux runs on this machine using the same paper and the same “academic neutral” sampling settings.

## Common test input
- Paper: `doc/tests/Debunking_Blockchain_Global_v2.md`
- Total chunks: **229** (with `--max_chars 800`)

## Common sampling (tone)
- `--temperature 0.4`
- `--top_p 0.7`
- `--repetition_penalty 1.1`
- `--do_sample true`
- `--max_new_tokens 2048`

## Results
| Run | Host | GPU | Model | attn_impl | dtype | max_chars | max_batch_chars | batch_size | Chunks | Batches | Avg batch (s) | Wall time | Output |
|---:|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | NUC (Windows) | (not recorded) | Qwen3-TTS-12Hz-0.6B-CustomVoice | sdpa | bfloat16 | 800 | 6000 | 4 | 229 | ~58* | ~121 | **1:55:00** | full_audiobook.wav (229 parts) |
| 2 | Linux (this machine) — Test A | RTX 3080 (sm86) | Qwen3-TTS-12Hz-0.6B-CustomVoice | flash_attention_2 (auto) | bfloat16 (auto) | 800 | 6000 | 4 | 229 | 58 | 69.33 | **1:07:04** | 476.4 MB |
| 3 | Linux (this machine) — Test B1 | RTX 3080 (sm86) | Qwen3-TTS-12Hz-0.6B-CustomVoice | flash_attention_2 (auto) | bfloat16 (auto) | 800 | 20000 | 8** | 229 | 24 | 83.47 | **0:35:45** | 484.4 MB |

\* NUC batches are inferred as ~229/4 ≈ 58 (same as the Linux Test A structure).

\** Test B1 originally attempted `batch_size=16` but repeatedly hit CUDA OOM and fell back to 8. The final timed run was restarted at stable `batch_size=8` to avoid OOM thrash.

## Speedups (by wall time)
- Linux Test A vs NUC: $\frac{1:55:00}{1:07:04} \approx 1.71\times$ faster
- Linux Test B1 vs NUC: $\frac{1:55:00}{0:35:45} \approx 3.22\times$ faster
- Linux Test B1 vs Linux Test A: $\frac{1:07:04}{0:35:45} \approx 1.88\times$ faster

## Notes / interpretation
- The biggest win vs NUC is using `flash_attention_2` (when available) instead of `sdpa`.
- Pushing throughput on this RTX 3080 is mainly about increasing *stable* batch concurrency. `batch_size=16` was not stable here for this workload, but `batch_size=8` was.
- Batch times have occasional long outliers (both A and B1) which can come from variable chunk lengths, CUDA allocator state, or transient GPU contention.

## Are we at max speed on this machine?
Probably **close**, but not proven-max.

What we already learned:
- `batch_size=16` is too high (OOM thrash), so the headroom is **somewhere between 8 and 16**.
- The current best end-to-end run (B1) is dominated by model compute, with some variability from chunk lengths and occasional long batches.

## Next experiments (to try beating 0:35:45)

### 1) Find the highest stable batch size (no OOM)
Try `10`, then `12`:

```bash
PYTHONUNBUFFERED=1 ./.venv/bin/python -u scripts/paper_to_audio.py \
	doc/tests/Debunking_Blockchain_Global_v2.md \
	--model_path ComfyUI/models/qwen-tts/Qwen3-TTS-12Hz-0.6B-CustomVoice \
	--output_dir output/Debunking_Blockchain_Neutral_Full_Linux_B_batch10 \
	--voice Ryan \
	--batch_size 10 \
	--max_chars 800 \
	--max_batch_chars 0 \
	--dtype auto \
	--attn_impl auto \
	--temperature 0.4 \
	--top_p 0.7 \
	--do_sample true \
	--repetition_penalty 1.1 \
	--max_new_tokens 2048
```

If `10` is stable, repeat with `--batch_size 12`.

### 2) Reduce chunk count (less overhead)
Keep batching high, but reduce chunks by increasing chunk size:

```bash
PYTHONUNBUFFERED=1 ./.venv/bin/python -u scripts/paper_to_audio.py \
	doc/tests/Debunking_Blockchain_Global_v2.md \
	--model_path ComfyUI/models/qwen-tts/Qwen3-TTS-12Hz-0.6B-CustomVoice \
	--output_dir output/Debunking_Blockchain_Neutral_Full_Linux_B2 \
	--voice Ryan \
	--batch_size 8 \
	--max_chars 1400 \
	--max_batch_chars 0 \
	--dtype auto \
	--attn_impl auto \
	--temperature 0.4 \
	--top_p 0.7 \
	--do_sample true \
	--repetition_penalty 1.1 \
	--max_new_tokens 2048
```

### 3) Compare bf16 vs fp16 (sometimes fp16 is a bit faster)
Same as B1 but force fp16:

```bash
PYTHONUNBUFFERED=1 ./.venv/bin/python -u scripts/paper_to_audio.py \
	doc/tests/Debunking_Blockchain_Global_v2.md \
	--model_path ComfyUI/models/qwen-tts/Qwen3-TTS-12Hz-0.6B-CustomVoice \
	--output_dir output/Debunking_Blockchain_Neutral_Full_Linux_B_fp16 \
	--voice Ryan \
	--batch_size 8 \
	--max_chars 800 \
	--max_batch_chars 0 \
	--dtype float16 \
	--attn_impl auto \
	--temperature 0.4 \
	--top_p 0.7 \
	--do_sample true \
	--repetition_penalty 1.1 \
	--max_new_tokens 2048
```

Practical tip: make sure nothing else is using the GPU during these runs (browser tabs, other CUDA jobs), because the long-batch outliers often correlate with contention.

## Artifacts
- Test A output: `output/Debunking_Blockchain_Neutral_Full_Linux_A/`
- Test B1 output: `output/Debunking_Blockchain_Neutral_Full_Linux_B1/`
- Logs: `run.log` inside each output directory
