#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$ROOT_DIR"

PYTHON_BIN="$ROOT_DIR/.venv/bin/python"
if [[ ! -x "$PYTHON_BIN" ]]; then
  if command -v python3 >/dev/null 2>&1; then
    PYTHON_BIN="python3"
  else
    PYTHON_BIN="python"
  fi
fi

INPUT_FILE="doc/tests/Debunking_Blockchain_Global_v2.md"
MODEL_PATH="ComfyUI/models/qwen-tts/Qwen3-TTS-12Hz-0.6B-CustomVoice"
VOICE="Ryan"

if [[ ! -f "$INPUT_FILE" ]]; then
  echo "Missing input file: $INPUT_FILE" >&2
  exit 1
fi

echo "== Test A: NUC parity (auto attn/dtype) =="
"$PYTHON_BIN" scripts/paper_to_audio.py \
  "$INPUT_FILE" \
  --model_path "$MODEL_PATH" \
  --output_dir output/Debunking_Blockchain_Neutral_Full_Linux_A \
  --voice "$VOICE" \
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

echo "== Test B1: Push throughput (higher batch + batch chars; auto backoff on OOM) =="
"$PYTHON_BIN" scripts/paper_to_audio.py \
  "$INPUT_FILE" \
  --model_path "$MODEL_PATH" \
  --output_dir output/Debunking_Blockchain_Neutral_Full_Linux_B1 \
  --voice "$VOICE" \
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
