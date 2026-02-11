import time
import torch
import sys
import os
import argparse

# Argument to control if we purposefully 'break' the import
parser = argparse.ArgumentParser()
parser.add_argument("--disable_attn", action="store_true", help="Simulate flash-attn not installed")
parser.add_argument("--text", type=str, default="This is a benchmark test. " * 10)
parser.add_argument("--model_path", type=str, default=None, help="Model path or HF id (defaults to local 0.6B CustomVoice)")
parser.add_argument("--voice", type=str, default="Ryan", help="Speaker name")
parser.add_argument("--dtype", type=str, choices=["float16", "bfloat16", "float32"], default="bfloat16")
parser.add_argument("--attn_impl", type=str, choices=["sdpa", "eager", "flash_attention_2"], default="sdpa")
parser.add_argument("--disable_flash_sdp", action="store_true")
parser.add_argument("--disable_mem_efficient_sdp", action="store_true")
parser.add_argument("--force_math_sdp", action="store_true")
parser.add_argument("--seed", type=int, default=1234)
parser.add_argument("--do_sample", type=lambda v: v.lower() in ("1", "true", "yes"), default=False)
parser.add_argument("--top_k", type=int, default=0)
parser.add_argument("--top_p", type=float, default=1.0)
parser.add_argument("--temperature", type=float, default=1.0)
parser.add_argument("--repetition_penalty", type=float, default=1.0)
parser.add_argument("--max_new_tokens", type=int, default=512)
parser.add_argument("--warmup", type=int, default=1, help="Warmup runs (not timed)")
parser.add_argument("--runs", type=int, default=3, help="Timed runs for average")
args = parser.parse_args()

if args.disable_attn:
    # Hack to simulate ImportError for flash_attn
    import builtins
    real_import = builtins.__import__
    def mock_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name == 'flash_attn' or (fromlist and 'flash_attn' in name):
            raise ImportError("Benchmark disabled flash_attn")
        return real_import(name, globals, locals, fromlist, level)
    builtins.__import__ = mock_import

# Add path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

print(f"Loading model... (Flash Attn Disabled: {args.disable_attn})")

# Measure Load Time
t0 = time.time()
try:
    from qwen_tts import Qwen3TTSModel
    if args.model_path:
        model_path = args.model_path
    else:
        model_path = os.path.join(root_dir, "models", "qwen-tts", "Qwen3-TTS-12Hz-0.6B-CustomVoice")
        if not os.path.exists(model_path):
            model_path = "Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice"
    
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Running on {device}")

    if device == "cuda":
        if args.disable_flash_sdp:
            torch.backends.cuda.enable_flash_sdp(False)
        if args.disable_mem_efficient_sdp:
            torch.backends.cuda.enable_mem_efficient_sdp(False)
        if args.force_math_sdp:
            torch.backends.cuda.enable_math_sdp(True)

    if args.seed is not None:
        torch.manual_seed(args.seed)
        if device == "cuda":
            torch.cuda.manual_seed_all(args.seed)

    if args.dtype == "float16":
        dtype = torch.float16
    elif args.dtype == "bfloat16":
        dtype = torch.bfloat16
    else:
        dtype = torch.float32

    model = Qwen3TTSModel.from_pretrained(
        model_path,
        device_map=device,
        torch_dtype=dtype,
        attn_implementation=args.attn_impl,
    )
except Exception as e:
    print(f"Failed to load: {e}")
    sys.exit(1)

load_time = time.time() - t0
print(f"Model loaded in {load_time:.2f}s")

# Check if model actually detected flash attn capability (internal flag)
# Qwen model wrapper sets this or the underlying model does
try:
    if hasattr(model.model, "_supports_flash_attn_2"):
        print(f"Model internal flag _supports_flash_attn_2: {model.model._supports_flash_attn_2}")
except:
    pass

# Benchmark Generation
print("Starting generation...")
text = args.text
voice = args.voice

def run_once():
    if args.seed is not None:
        torch.manual_seed(args.seed)
        if device == "cuda":
            torch.cuda.manual_seed_all(args.seed)
    with torch.inference_mode():
        wavs, sr = model.generate_custom_voice(
            text=text,
            speaker=voice,
            do_sample=args.do_sample,
            top_k=args.top_k,
            top_p=args.top_p,
            temperature=args.temperature,
            repetition_penalty=args.repetition_penalty,
            max_new_tokens=args.max_new_tokens,
        )
    return wavs, sr

for _ in range(max(0, args.warmup)):
    run_once()

times = []
for _ in range(max(1, args.runs)):
    if device == "cuda":
        torch.cuda.synchronize()
    t_start = time.perf_counter()
    run_once()
    if device == "cuda":
        torch.cuda.synchronize()
    t_end = time.perf_counter()
    times.append(t_end - t_start)

avg = sum(times) / len(times)
print(f"Text length: {len(text)} chars")
print(f"Runs: {len(times)} | Avg: {avg:.4f}s | Min: {min(times):.4f}s | Max: {max(times):.4f}s")
print("TIMES: " + ", ".join(f"{t:.4f}" for t in times))
