import importlib
import importlib.util
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import soundfile as sf
import torch
from faster_whisper import WhisperModel

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


def normalize_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def phrase_detected(text: str) -> bool:
    norm = normalize_text(text)
    return "quick brown fox" in norm and "lazy dog" in norm


def transcribe_file(asr: WhisperModel, wav_path: Path) -> str:
    segments, _ = asr.transcribe(str(wav_path), beam_size=5, language="en")
    return " ".join([seg.text.strip() for seg in segments]).strip()


def main() -> None:
    script_path = Path(__file__).resolve()
    repo_root = script_path.parents[5]
    qwen_repo = repo_root / "ai_models" / "qwen-tts"
    output_dir = script_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    if str(qwen_repo) not in sys.path:
        sys.path.insert(0, str(qwen_repo))

    Qwen3TTSModel = importlib.import_module("qwen_tts").Qwen3TTSModel

    model_path = repo_root / "ai_models" / "qwen-tts" / "ComfyUI" / "models" / "qwen-tts" / "Qwen3-TTS-12Hz-0.6B-CustomVoice"
    if not model_path.exists():
        fallback = repo_root / "ComfyUI" / "models" / "qwen-tts" / "Qwen3-TTS-12Hz-0.6B-CustomVoice"
        if fallback.exists():
            model_path = fallback
        else:
            raise FileNotFoundError("0.6B model not found in known paths.")

    model = Qwen3TTSModel.from_pretrained(
        str(model_path),
        device_map="cuda" if torch.cuda.is_available() else "cpu",
        torch_dtype=resolve_dtype(),
        attn_implementation=resolve_attn_impl(),
    )

    supported = model.get_supported_speakers() or []
    if SPEAKER.lower() not in [s.lower() for s in supported]:
        raise ValueError(f"Speaker '{SPEAKER}' not available. Supported: {supported}")

    asr = WhisperModel("tiny.en", device="cuda" if torch.cuda.is_available() else "cpu", compute_type="float16" if torch.cuda.is_available() else "int8")

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    attempts = [
        {
            "name": "baseline_auto",
            "language": "Auto",
            "do_sample": True,
            "top_p": 0.7,
            "temperature": 0.4,
            "repetition_penalty": 1.1,
            "max_new_tokens": 1024,
        },
        {
            "name": "english_constrained_sampling",
            "language": "English",
            "do_sample": True,
            "top_p": 0.3,
            "temperature": 0.2,
            "repetition_penalty": 1.15,
            "max_new_tokens": 120,
        },
        {
            "name": "english_deterministic",
            "language": "English",
            "do_sample": False,
            "top_p": 0.7,
            "temperature": 0.4,
            "repetition_penalty": 1.1,
            "max_new_tokens": 120,
        },
        {
            "name": "english_deterministic_short",
            "language": "English",
            "do_sample": False,
            "top_p": 0.7,
            "temperature": 0.4,
            "repetition_penalty": 1.1,
            "max_new_tokens": 80,
        },
    ]

    report = []
    success = None

    for idx, cfg in enumerate(attempts, start=1):
        print(f"Attempt {idx}/{len(attempts)}: {cfg['name']}")
        wavs, sr = model.generate_custom_voice(
            text=PHRASE,
            speaker=SPEAKER,
            language=cfg["language"],
            non_streaming_mode=True,
            do_sample=cfg["do_sample"],
            top_p=cfg["top_p"],
            temperature=cfg["temperature"],
            repetition_penalty=cfg["repetition_penalty"],
            max_new_tokens=cfg["max_new_tokens"],
        )

        if not wavs:
            result = {
                "attempt": idx,
                "config": cfg,
                "file": None,
                "transcript": "",
                "passed": False,
                "reason": "no_audio",
            }
            report.append(result)
            continue

        out_file = output_dir / f"qwen06b_{SPEAKER}_{cfg['name']}_{ts}.wav"
        sf.write(str(out_file), wavs[0], sr)

        transcript = transcribe_file(asr, out_file)
        passed = phrase_detected(transcript)

        result = {
            "attempt": idx,
            "config": cfg,
            "file": str(out_file),
            "transcript": transcript,
            "passed": passed,
        }
        report.append(result)

        print(f"  transcript: {transcript[:220]}")
        print(f"  passed: {passed}")

        if passed:
            success = result
            break

    report_file = output_dir / f"qwen06b_{SPEAKER}_verification_report_{ts}.json"
    report_file.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    del model
    if torch.cuda.is_available():
        torch.cuda.empty_cache()

    if success:
        print("SUCCESS: phrase detected")
        print(f"Winning file: {success['file']}")
        print(f"Report: {report_file}")
    else:
        print("FAILED: phrase not detected in all attempts")
        print(f"Report: {report_file}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
