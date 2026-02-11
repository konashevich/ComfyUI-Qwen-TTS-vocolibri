import os
import sys
import argparse
import re
import torch
import numpy as np
import soundfile as sf
import logging
import gc
from tqdm import tqdm
from typing import Optional

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Add module path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

try:
    from qwen_tts import Qwen3TTSModel
except ImportError:
    # Try local import if package is not installed in site-packages
    try:
        sys.path.insert(0, os.path.join(root_dir, "qwen_tts"))
        from qwen_tts import Qwen3TTSModel
    except ImportError as e:
        logger.error(f"Failed to import Qwen3TTSModel: {e}")
        sys.exit(1)

def clean_markdown(text):
    """
    Cleans markdown text for TTS processing.
    """
    # Remove metadata block if present (YAML front matter)
    text = re.sub(r'^---\n.*?\n---\n', '', text, flags=re.DOTALL)
    
    # Remove citations like [1], [1, 2], [1-3]
    text = re.sub(r'\[\d+(?:,\s*\d+)*(?:-\d+)?\]', '', text)
    
    # Remove Markdown links: [text](url) -> text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    
    # Remove images: ![alt](url) -> ""
    text = re.sub(r'!\[[^\]]*\]\([^)]+\)', '', text)
    
    # Remove bold/italic markers (* or _)
    text = re.sub(r'[*_]{1,3}([^*_]+)[*_]{1,3}', r'\1', text)
    
    # Remove headers ### Header -> Header.
    text = re.sub(r'#{1,6}\s*(.*)', r'\1.', text)
    
    # Remove simple URLs
    text = re.sub(r'http[s]?://\S+', ' ', text)
    
    # Replace newlines within paragraphs with spaces to avoid weird pauses
    # But preserve double newlines (paragraphs)
    # text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text) # This is risky for lists
    
    return text.strip()

def split_text(text, max_chars=800):
    """
    Splits text into chunks small enough for the model context.
    """
    # Split by double newlines (paragraphs)
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""
    
    for para in paragraphs:
        para = para.strip()
        if not para: continue
        
        # Simple cleanup of line breaks within paragraph
        para = para.replace('\n', ' ')
        
        if len(current_chunk) + len(para) < max_chars:
            if current_chunk:
                current_chunk += "\n" + para
            else:
                current_chunk = para
        else:
            if current_chunk:
                chunks.append(current_chunk)
            
            # If paragraph itself is too huge, split by sentences
            if len(para) > max_chars:
                # Simple sentence split
                sentences = re.split(r'(?<=[.!?])\s+', para)
                current_chunk = ""
                for sent in sentences:
                    if len(current_chunk) + len(sent) < max_chars:
                        if current_chunk:
                            current_chunk += " " + sent
                        else:
                            current_chunk = sent
                    else:
                        if current_chunk:
                            chunks.append(current_chunk)
                        current_chunk = sent
                # continue with whatever remains in current_chunk
            else:
                current_chunk = para
                
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

def main():
    parser = argparse.ArgumentParser(description="Convert academic paper (Markdown) to narrated audio using Qwen-TTS.")
    parser.add_argument("input_file", help="Path to input Markdown file")
    parser.add_argument("--output_dir", default="output_audio", help="Directory to save audio files")
    parser.add_argument("--model_path", default=None, help="Path to Qwen-TTS model. Defaults to local models/qwen-tts/Qwen3-TTS-12Hz-1.7B-CustomVoice")
    parser.add_argument("--voice", default="Serena", help="Preset voice name for CustomVoice model")
    parser.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu", help="Device to run inference on")
    parser.add_argument(
        "--attn_impl",
        default=None,
        choices=["auto", "sdpa", "eager", "flash_attention_2"],
        help="Attention implementation override. Use 'auto' (or omit) to prefer flash-attn2 when available, else sdpa.",
    )
    parser.add_argument(
        "--dtype",
        default=None,
        choices=["auto", "float16", "float32", "bfloat16"],
        help="Override model dtype. Use 'auto' (or omit) to pick bf16 when supported on CUDA, else fp16.",
    )
    parser.add_argument(
        "--disable_flash_sdp",
        action="store_true",
        help="Disable PyTorch Flash SDP kernel (useful for CUDA assert issues).",
    )
    parser.add_argument(
        "--disable_mem_efficient_sdp",
        action="store_true",
        help="Disable PyTorch memory-efficient SDP kernel.",
    )
    parser.add_argument(
        "--force_math_sdp",
        action="store_true",
        help="Force PyTorch math SDP kernel.",
    )
    parser.add_argument("--no_flash_attn", action="store_true", help="Disable Flash Attention (useful for smaller models that might have compatibility issues)")
    parser.add_argument("--seed", type=int, default=None, help="Random seed to stabilize generation across chunks")
    parser.add_argument("--deterministic", action="store_true", help="Try to enforce deterministic behavior for reproducible output")
    parser.add_argument("--do_sample", type=lambda v: v.lower() in ("1", "true", "yes"), default=True, help="Enable sampling (more variation). Default True for better tone control")
    parser.add_argument("--top_k", type=int, default=0, help="Top-k sampling (0 disables).")
    parser.add_argument("--top_p", type=float, default=0.7, help="Top-p (nucleus) sampling. Default 0.7 for stability")
    parser.add_argument("--temperature", type=float, default=0.4, help="Sampling temperature. Default 0.4 for neutral tone")
    parser.add_argument("--repetition_penalty", type=float, default=1.1, help="Penalty to reduce repetition. Default 1.1")
    parser.add_argument("--max_new_tokens", type=int, default=None, help="Maximum number of new codec tokens to generate per chunk.")
    parser.add_argument("--batch_size", type=int, default=8, help="Number of chunks to generate per batch (higher uses more VRAM)")
    parser.add_argument("--max_chars", type=int, default=800, help="Max characters per chunk for splitting")
    parser.add_argument("--max_batch_chars", type=int, default=6000, help="Cap total characters per batch to avoid very long batches (0 disables)")
    parser.add_argument("--start_chunk", type=int, default=0, help="Start chunk index (inclusive)")
    parser.add_argument("--end_chunk", type=int, default=None, help="End chunk index (exclusive)")
    parser.add_argument("--max_chunks", type=int, default=None, help="Limit number of chunks processed (from start_chunk)")
    
    args = parser.parse_args()

    def _cuda_info() -> str:
        if not torch.cuda.is_available():
            return "CUDA not available"
        try:
            name = torch.cuda.get_device_name(0)
        except Exception:
            name = "unknown"
        try:
            cap = torch.cuda.get_device_capability(0)
            cap_s = f"sm{cap[0]}{cap[1]}"
        except Exception:
            cap_s = "unknown"
        return f"{name} ({cap_s})"

    def _flash_attn2_available() -> bool:
        if args.no_flash_attn:
            return False
        if args.device != "cuda" or not torch.cuda.is_available():
            return False
        try:
            major, _minor = torch.cuda.get_device_capability(0)
            if major < 8:
                return False
        except Exception:
            return False
        try:
            import flash_attn  # noqa: F401
        except Exception:
            return False
        return True

    def _resolve_dtype() -> torch.dtype:
        requested = args.dtype
        if requested is None or requested == "auto":
            if args.device == "cuda" and torch.cuda.is_available():
                try:
                    return torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
                except Exception:
                    return torch.float16
            return torch.float32

        if requested == "float16":
            return torch.float16
        if requested == "bfloat16":
            if args.device == "cuda" and torch.cuda.is_available():
                try:
                    if torch.cuda.is_bf16_supported():
                        return torch.bfloat16
                except Exception:
                    pass
                logger.warning("Requested bfloat16, but bf16 is not supported on this CUDA device. Falling back to float16.")
                return torch.float16
            logger.warning("Requested bfloat16 on non-CUDA device. Falling back to float32.")
            return torch.float32
        if requested == "float32":
            return torch.float32

        logger.warning(f"Unknown dtype '{requested}', falling back to auto")
        args.dtype = "auto"
        return _resolve_dtype()

    def _resolve_attn_impl() -> Optional[str]:
        requested = args.attn_impl
        if requested is None or requested == "auto":
            return "flash_attention_2" if _flash_attn2_available() else "sdpa"

        if requested == "flash_attention_2" and not _flash_attn2_available():
            logger.warning("Requested flash_attention_2, but flash-attn2 is unavailable. Falling back to sdpa.")
            return "sdpa"
        return requested

    if args.device == "cuda":
        if args.disable_flash_sdp:
            torch.backends.cuda.enable_flash_sdp(False)
        if args.disable_mem_efficient_sdp:
            torch.backends.cuda.enable_mem_efficient_sdp(False)
        if args.force_math_sdp:
            torch.backends.cuda.enable_math_sdp(True)

    if args.no_flash_attn:
        # Hack to simulate ImportError for flash_attn
        import builtins
        real_import = builtins.__import__
        def mock_import(name, globals=None, locals=None, fromlist=(), level=0):
            if name == 'flash_attn' or (fromlist and 'flash_attn' in name):
                raise ImportError("User disabled flash_attn via CLI")
            return real_import(name, globals, locals, fromlist, level)
        builtins.__import__ = mock_import
        logger.info("Flash Attention explicitly disabled.")

    if args.deterministic:
        torch.backends.cudnn.benchmark = False
        torch.backends.cudnn.deterministic = True
        try:
            torch.use_deterministic_algorithms(True, warn_only=True)
        except Exception:
            pass

    if args.seed is not None:
        torch.manual_seed(args.seed)
        if args.device == "cuda":
            torch.cuda.manual_seed_all(args.seed)
    
    # Resolve model path
    model_path = args.model_path
    if not model_path:
        # Default local path
        default_path = os.path.join(root_dir, "models", "qwen-tts", "Qwen3-TTS-12Hz-1.7B-CustomVoice")
        if os.path.exists(default_path):
            model_path = default_path
        else:
            # Fallback to HuggingFace ID if local not found
            model_path = "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice"
            logger.info(f"Local model not found, using HuggingFace ID: {model_path}")

    logger.info(f"Using model: {model_path}")
    logger.info(f"Device: {args.device}")
    if args.device == "cuda":
        logger.info(f"CUDA device: {_cuda_info()}")

    # Load Text
    if not os.path.exists(args.input_file):
        logger.error(f"Input file not found: {args.input_file}")
        sys.exit(1)
        
    with open(args.input_file, 'r', encoding='utf-8') as f:
        raw_text = f.read()
        
    logger.info("Cleaning text...")
    clean_text = clean_markdown(raw_text)
    
    logger.info(f"Split text into chunks...")
    chunks = split_text(clean_text, max_chars=args.max_chars)
    logger.info(f"Total chunks: {len(chunks)}")

    # Limit chunk range if requested
    start_idx = max(0, args.start_chunk)
    end_idx = args.end_chunk if args.end_chunk is not None else len(chunks)
    end_idx = min(len(chunks), max(start_idx, end_idx))
    if args.max_chunks is not None:
        end_idx = min(end_idx, start_idx + max(0, args.max_chunks))
    if start_idx > 0 or end_idx < len(chunks):
        chunks = chunks[start_idx:end_idx]
        logger.info(f"Using chunk range [{start_idx}, {end_idx}) -> {len(chunks)} chunks")
    
    # Load Model
    logger.info("Loading Qwen-TTS model...")
    try:
        dtype = _resolve_dtype()
        attn_impl = _resolve_attn_impl()
        logger.info(f"Resolved dtype: {str(dtype).replace('torch.', '')}")
        if attn_impl:
            logger.info(f"Resolved attn_impl: {attn_impl}")

        model_kwargs = {
            "device_map": args.device,
            "torch_dtype": dtype,
        }
        if attn_impl:
            model_kwargs["attn_implementation"] = attn_impl
        model = Qwen3TTSModel.from_pretrained(model_path, **model_kwargs)
    except Exception as e:
        logger.error(f"Failed to load model: {e}")
        sys.exit(1)
        
    # Check supported speakers if using CustomVoice
    # Usually model wrapper handles this, but let's check attributes if available
    if hasattr(model.model, "get_supported_speakers"):
        speakers_map = model.model.get_supported_speakers()
        speakers_list = list(speakers_map.keys()) if hasattr(speakers_map, 'keys') else list(speakers_map)
        logger.info(f"Available speakers: {speakers_list}")
        
        # Case insensitive match
        voice_found = False
        for s in speakers_list:
            if s.lower() == args.voice.lower():
                args.voice = s
                voice_found = True
                break
        
        if not voice_found:
            logger.warning(f"Voice '{args.voice}' not in supported speakers. Using default or first available.")
            if speakers_list:
                args.voice = speakers_list[0]

    os.makedirs(args.output_dir, exist_ok=True)
    
    # Generate
    logger.info("Starting generation...")
    all_audio = []
    sample_rate = 24000 # Default fallback
    
    had_cuda_assert = False
    def generate_batch(batch_indices, batch_texts, batch_speakers):
        if args.seed is not None:
            torch.manual_seed(args.seed)
            if args.device == "cuda":
                torch.cuda.manual_seed_all(args.seed)

        wavs, sr = model.generate_custom_voice(
            text=batch_texts,
            speaker=batch_speakers,
            non_streaming_mode=True,
            do_sample=args.do_sample,
            top_k=args.top_k,
            top_p=args.top_p,
            temperature=args.temperature,
            repetition_penalty=args.repetition_penalty,
            max_new_tokens=args.max_new_tokens if args.max_new_tokens is not None else 2048,
        )

        for idx, audio_data in zip(batch_indices, wavs):
            chunk_file = os.path.join(args.output_dir, f"part_{idx:03d}.wav")
            sf.write(chunk_file, audio_data, sr)
            all_audio.append(audio_data)
        return sr

    def clamp_batch_size(texts, requested_size):
        if args.max_batch_chars <= 0:
            return requested_size
        total = 0
        count = 0
        for t in texts[:requested_size]:
            t_len = len(t)
            if count > 0 and total + t_len > args.max_batch_chars:
                break
            total += t_len
            count += 1
        return max(1, count)

    i = 0
    total = len(chunks)
    while i < total:
        batch_indices = list(range(i, min(i + args.batch_size, total)))
        i = batch_indices[-1] + 1

        pending_indices = []
        pending_texts = []
        for idx in batch_indices:
            chunk = chunks[idx]
            chunk_file = os.path.join(args.output_dir, f"part_{idx:03d}.wav")

            if os.path.exists(chunk_file):
                try:
                    data, sr = sf.read(chunk_file)
                    all_audio.append(data)
                    sample_rate = sr
                except Exception:
                    pass
                continue

            if not chunk.strip():
                continue

            pending_indices.append(idx)
            pending_texts.append(chunk)

        if not pending_indices:
            continue

        batch_size = clamp_batch_size(pending_texts, min(args.batch_size, len(pending_indices)))
        while batch_size > 0:
            try:
                batch_start = torch.cuda.Event(enable_timing=True) if args.device == "cuda" else None
                batch_end = torch.cuda.Event(enable_timing=True) if args.device == "cuda" else None
                logger.info(f"Generating batch of {batch_size} chunks (remaining: {len(pending_indices)})...")
                sub_indices = pending_indices[:batch_size]
                sub_texts = pending_texts[:batch_size]
                sub_speakers = [args.voice] * batch_size
                if batch_start is not None:
                    batch_start.record()
                sample_rate = generate_batch(sub_indices, sub_texts, sub_speakers)
                if batch_end is not None:
                    batch_end.record()
                    torch.cuda.synchronize()
                    elapsed = batch_start.elapsed_time(batch_end) / 1000.0
                    logger.info(f"Batch completed in {elapsed:.2f}s")

                # Process any remaining chunks in this pending list
                pending_indices = pending_indices[batch_size:]
                pending_texts = pending_texts[batch_size:]
                if not pending_indices:
                    break
                batch_size = clamp_batch_size(pending_texts, min(args.batch_size, len(pending_indices)))
            except RuntimeError as e:
                err = str(e).lower()
                if "out of memory" in err:
                    logger.warning("CUDA OOM: reducing batch size and retrying...")
                    if args.device == "cuda":
                        try:
                            torch.cuda.synchronize()
                        except Exception:
                            pass
                        gc.collect()
                        try:
                            torch.cuda.empty_cache()
                        except Exception:
                            logger.warning("CUDA empty_cache failed after OOM; continuing with smaller batch.")
                    batch_size //= 2
                    batch_size = clamp_batch_size(pending_texts, batch_size)
                    if batch_size == 0:
                        raise
                    continue
                if "flattened indices" in err or "internal assert" in err:
                    logger.warning("Batch padding error: reducing batch size and retrying...")
                    if args.device == "cuda":
                        try:
                            torch.cuda.synchronize()
                        except Exception:
                            pass
                        gc.collect()
                        try:
                            torch.cuda.empty_cache()
                        except Exception:
                            logger.warning("CUDA empty_cache failed after error; continuing with smaller batch.")
                    batch_size //= 2
                    batch_size = clamp_batch_size(pending_texts, batch_size)
                    if batch_size == 0:
                        raise
                    continue
                raise
            except Exception as e:
                logger.error(f"Error processing batch starting at chunk {sub_indices[0] if sub_indices else 'unknown'}: {e}")
                if "device-side assert" in str(e).lower():
                    had_cuda_assert = True
                    logger.error("CUDA device-side assert detected. Aborting generation to avoid invalid output.")
                break

        if had_cuda_assert:
            break
            
    # Combine (Optional)
    if all_audio and not had_cuda_assert:
        logger.info("Combining all audio parts...")
        combined_audio = torch.cat([torch.tensor(a) for a in all_audio]) if isinstance(all_audio[0], torch.Tensor) else np.concatenate(all_audio)
        
        full_output = os.path.join(args.output_dir, "full_audiobook.wav")
        sf.write(full_output, combined_audio, sample_rate)
        logger.info(f"Full audiobook saved to {full_output}")
    elif had_cuda_assert:
        logger.warning("Skipped combining audio due to CUDA errors. Fix the issue and re-run.")

    logger.info("Done.")

if __name__ == "__main__":
    main()
