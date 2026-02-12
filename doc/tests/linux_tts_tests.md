# Linux Paper-to-Audio Tests (NUC Parity + Max Throughput)

Goal: run the *same paper* as the NUC test, first with matching generation parameters (same chunking + sampling), but with this machine’s optimal attention/dtype; then run a second test that pushes VRAM/throughput.

Paper input in this repo:
- `doc/tests/Debunking_Blockchain_Global_v2.md`

## 1) Test A — “NUC parity” (same chunking + sampling)
Same chunking knobs that produced 229 chunks on NUC (`--max_chars 800`, `--max_batch_chars 6000`, `--batch_size 4`) and the same sampling settings.

```bash
python scripts/paper_to_audio.py \
  doc/tests/Debunking_Blockchain_Global_v2.md \
  --model_path ComfyUI/models/qwen-tts/Qwen3-TTS-12Hz-0.6B-CustomVoice \
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

## 2) Test B — “Max throughput” (push VRAM)
Start aggressive. The script auto-reduces batch size on CUDA OOM.

### Option B1: maximize batch concurrency
```bash
python scripts/paper_to_audio.py \
  doc/tests/Debunking_Blockchain_Global_v2.md \
  --model_path ComfyUI/models/qwen-tts/Qwen3-TTS-12Hz-0.6B-CustomVoice \
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

### Option B2: reduce chunk count (less overhead)
```bash
python scripts/paper_to_audio.py \
  doc/tests/Debunking_Blockchain_Global_v2.md \
  --model_path ComfyUI/models/qwen-tts/Qwen3-TTS-12Hz-0.6B-CustomVoice \
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
