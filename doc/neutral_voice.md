# Neutral Voice Configuration for Qwen3-TTS 0.6B

## The Challenge
The Qwen3-TTS 0.6B model, while faster than the 1.7B variant, often exhibits unstable prosody (reported as "emotional" or "erratic" tone) when used with default sampling parameters. This is because the default temperature (`1.0`) is tuned for the larger model's distribution, causing the smaller model to sample low-probability tokens that result in exaggerated or hallucinated emotions.

## The Solution
To achieve a professional, neutral, or academic reading style, you must constrain the model's random sampling. We have identified a specific set of parameters that stabilize the output.

### Recommended Parameters
These settings have been hardcoded as defaults in `scripts/paper_to_audio.py` as of Feb 2026.

| Parameter | Value | Reason |
| :--- | :--- | :--- |
| **Temperature** | `0.4` | Drastically reduces randomness. Default 1.0 is too chaotic for 0.6B. |
| **Top_P** | `0.7` | (Nucleus Sampling) Restricts the token pool to the top 70% probability mass. |
| **Repetition Penalty** | `1.1` | Slightly higher than default (1.0) to prevent stuttering in "monotone" modes. |
| **Do Sample** | `True` | **Crucial.** You must enable sampling for these parameters to take effect. |

### Usage in Scripts
When running the `paper_to_audio.py` script, these defaults are applied automatically. You can override them if needed, but for academic narration, strictly adhere to:

```bash
python scripts/paper_to_audio.py "paper.md" \
  --do_sample true \
  --temperature 0.4 \
  --top_p 0.7 \
  --repetition_penalty 1.1 \
  --voice Ryan
```

### Why "Instruct" Prompting Doesn't Work
The 0.6B model **does not support** the "Voice Design" (Instruct) feature found in the 1.7B model. You cannot control the tone by prompting "Speak in a sad voice" or "Speak professionally". You effectively control the tone *indirectly* via the entropy (temperature) of the generation.
