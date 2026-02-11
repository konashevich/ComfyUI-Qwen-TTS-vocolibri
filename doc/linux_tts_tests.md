# Linux Paper-to-Audio Tests (NUC Parity + Max Throughput)

Goal: run the *same paper* as the NUC test, first with matching generation parameters (same chunking + sampling), but with this machine’s optimal attention/dtype; then run a second test that pushes VRAM/throughput.

## 0) Prereqs
- Use the same input markdown file used on NUC: `Debunking_Blockchain_Global_v2.md` (path on Linux may differ).
- Model path used on NUC: `models/qwen-tts/Qwen3-TTS-12Hz-0.6B-CustomVoice`

## 1) Test A — “NUC parity” (same chunking + sampling)
This keeps the same chunking knobs that produced 229 chunks on NUC (`--max_chars 800`, `--max_batch_chars 6000`, `--batch_size 4`) and the same sampling settings, but uses the best attention/dtype available on this Linux GPU.

```bash
python scripts/paper_to_audio.py \
  /ABS/PATH/TO/Debunking_Blockchain_Global_v2.md \
  --model_path models/qwen-tts/Qwen3-TTS-12Hz-0.6B-CustomVoice \
  --output_dir output/Debunking_Blockchain_Neutral_Full_Linux_A \
  --voice Ryan \
  --batch_size 4 \
  --max_chars 800 \
  --max_batch_chars 6000 \
  --dtype auto \
  --attn_impl auto \
  --temperature 0.4 \
  --top_p 0.7 \
  --do_sample true \
  --repetition_penalty 1.1 \
  --max_new_tokens 2048
```

Expected in logs:
- `Total chunks: 229` (if the input markdown content matches the NUC file)
- `Resolved attn_impl: flash_attention_2` (if flash-attn2 is installed + GPU is sm80+)
- `Resolved dtype: bfloat16` (if bf16 is supported) else fp16

## 2) Test B — “Max throughput” (push VRAM)
Start aggressive. The script already reduces batch size on CUDA OOM, so you can safely aim high.

### Option B1: maximize batch concurrency (most common win)
```bash
python scripts/paper_to_audio.py \
  /ABS/PATH/TO/Debunking_Blockchain_Global_v2.md \
  --model_path models/qwen-tts/Qwen3-TTS-12Hz-0.6B-CustomVoice \
  --output_dir output/Debunking_Blockchain_Neutral_Full_Linux_B1 \
  --voice Ryan \
  --batch_size 16 \
  --max_chars 800 \
  --max_batch_chars 20000 \
  --dtype auto \
  --attn_impl auto \
  --temperature 0.4 \
  --top_p 0.7 \
  --do_sample true \
  --repetition_penalty 1.1 \
  --max_new_tokens 2048
```

### Option B2: reduce chunk count (less overhead) + still high batching
This usually speeds up end-to-end because there are fewer chunks to tokenize/write.

```bash
python scripts/paper_to_audio.py \
  /ABS/PATH/TO/Debunking_Blockchain_Global_v2.md \
  --model_path models/qwen-tts/Qwen3-TTS-12Hz-0.6B-CustomVoice \
  --output_dir output/Debunking_Blockchain_Neutral_Full_Linux_B2 \
  --voice Ryan \
  --batch_size 16 \
  --max_chars 1400 \
  --max_batch_chars 26000 \
  --dtype auto \
  --attn_impl auto \
  --temperature 0.4 \
  --top_p 0.7 \
  --do_sample true \
  --repetition_penalty 1.1 \
  --max_new_tokens 2048
```

## What to record (for a report like NUC)
- Chunk count
- Avg batch time (already logged per batch)
- Total runtime (wrap the command with `/usr/bin/time -v ...` if you want)
- Effective chars/sec = total_chars / total_seconds
