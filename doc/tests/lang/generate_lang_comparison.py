import importlib
import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path

import soundfile as sf
import torch

PHRASE = "The quick brown fox jumps over the lazy dog"
SPEAKER = "aiden"


def resolve_dtype() -> torch.dtype:
    if torch.cuda.is_available():
        try:
            return torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
        except Exception:
            return torch.float16
    return torch.float32


def resolve_attn_impl() -> str:
    if not torch.cuda.is_available():
        return "sdpa"
    try:
        major, _ = torch.cuda.get_device_capability(0)
        if major < 8:
            return "sdpa"
        if importlib.util.find_spec("flash_attn") is None:
            return "sdpa"
        return "flash_attention_2"
    except Exception:
        return "sdpa"


def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[5]
    qwen_repo = repo_root / "ai_models" / "qwen-tts"
    output_dir = script_path.parent

    if str(qwen_repo) not in sys.path:
        sys.path.insert(0, str(qwen_repo))

    qwen_module = importlib.import_module("qwen_tts")
    Qwen3TTSModel = qwen_module.Qwen3TTSModel

    model_path = Path("/home/beast/ComfyUI-Qwen-TTS-vocolibri/ComfyUI/models/qwen-tts/Qwen3-TTS-12Hz-0.6B-CustomVoice")
    if not model_path.exists():
        fallback = repo_root / "ComfyUI" / "models" / "qwen-tts" / "Qwen3-TTS-12Hz-0.6B-CustomVoice"
        if fallback.exists():
            model_path = fallback
        else:
            raise FileNotFoundError("0.6B model not found in known paths.")

    print(f"Loading model from: {model_path}")
    print(f"dtype={str(resolve_dtype()).replace('torch.', '')}, attn_impl={resolve_attn_impl()}")

    model = Qwen3TTSModel.from_pretrained(
        str(model_path),
        device_map="cuda" if torch.cuda.is_available() else "cpu",
        torch_dtype=resolve_dtype(),
        attn_implementation=resolve_attn_impl(),
    )

    supported = model.get_supported_speakers() or []
    if SPEAKER.lower() not in [s.lower() for s in supported]:
        raise ValueError(f"Speaker '{SPEAKER}' not available. Supported: {supported}")

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    runs = [
        {
            "label": "auto",
            "language": "Auto",
        },
        {
            "label": "english",
            "language": "English",
        },
    ]

    for run in runs:
        print(f"Generating run={run['label']} language={run['language']}")
        wavs, sr = model.generate_custom_voice(
            text=PHRASE,
            speaker=SPEAKER,
            language=run["language"],
            non_streaming_mode=True,
            do_sample=True,
            top_p=0.7,
            temperature=0.4,
            repetition_penalty=1.1,
            max_new_tokens=1024,
        )

        if not wavs:
            raise RuntimeError(f"No audio returned for run={run['label']}")

        out_path = output_dir / f"qwen06b_aiden_{run['label']}_{ts}.wav"
        sf.write(str(out_path), wavs[0], sr)
        print(f"Saved: {out_path}")

    del model
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    print("Done.")


if __name__ == "__main__":
    main()
