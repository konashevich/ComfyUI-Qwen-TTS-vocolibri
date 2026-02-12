# TTS Test Pack

This folder contains the fixed test input (paper) plus the test configs/commands used to reproduce NUC-parity and max-throughput runs on Linux.

## Files
- `Debunking_Blockchain_Global_v2.md`: the paper input
- `nuc_report.md`, `nuc_test.md`: NUC reference report + exact command used on NUC
- `linux_tts_tests.md`: Linux commands for Test A (NUC parity) + Test B (push limits)
- `smoke_test_linux.sh`: fast validation run (2 chunks)
- `run_linux_tests.sh`: runs Test A then Test B1

## Quick start
Smoke test (recommended first):
```bash
./doc/tests/smoke_test_linux.sh
```

Full Test A (NUC parity) example:
```bash
PYTHONUNBUFFERED=1 ./.venv/bin/python -u scripts/paper_to_audio.py \
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

Monitor a background run:
```bash
tail -n 50 output/Debunking_Blockchain_Neutral_Full_Linux_A/run.log
```
