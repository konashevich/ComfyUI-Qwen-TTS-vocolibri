import os
import sys
import torch
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add module path
current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from qwen_tts import Qwen3TTSModel

def test():
    model_path = os.path.join(root_dir, "models", "qwen-tts", "Qwen3-TTS-12Hz-0.6B-CustomVoice")
    device = "cpu" # Force CPU for debugging
    text = "Hello, this is a test of the small model."
    
    logger.info(f"Loading {model_path} on {device}...")
    try:
        model = Qwen3TTSModel.from_pretrained(
            model_path, 
            device_map=device, 
            torch_dtype=torch.float32
        )
    except Exception as e:
        logger.error(f"Failed to load: {e}")
        return

    logger.info("Generating...")
    try:
        wavs, sr = model.generate_custom_voice(text=text, speaker="Ryan")
        logger.info(f"Success! Generated audio with sample rate {sr}")
    except Exception as e:
        logger.error(f"Generation failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test()
