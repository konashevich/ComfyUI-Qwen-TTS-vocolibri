# NUC TTS Generation Summary (nuc_test.md)

This file contains the command and configuration used for the final generation on the NUC hardware.

## Execution Command
```powershell
C:\Users\akona\OneDrive\Dev\ComfyUI-Qwen-TTS\.venv\Scripts\python.exe scripts/paper_to_audio.py `
  "C:\Users\akona\OneDrive\Dev\Public-VS-Private\Debunking_Blockchain_Global_v2.md" `
  --model_path "models/qwen-tts/Qwen3-TTS-12Hz-0.6B-CustomVoice" `
  --output_dir "output/Debunking_Blockchain_Neutral_Full" `
  --voice Ryan `
  --batch_size 4 `
  --dtype bfloat16 `
  --attn_impl sdpa `
  --temperature 0.4 `
  --top_p 0.7 `
  --do_sample true `
  --repetition_penalty 1.1 `
  --max_new_tokens 2048
```

## Technical Specs
- **Model:** Qwen3-TTS 0.6B (Custom Voice Wrapper)
- **Host:** NUC
- **VRAM Optimization:** `max_batch_chars: 6000`
- **Output:** 229 chunks merged into single WAV.
