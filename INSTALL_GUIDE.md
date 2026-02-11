# ComfyUI-Qwen-TTS — Full Install & Recovery Guide (Windows + NVIDIA)

This guide reflects the working setup and fixes from the full install journey. Follow it exactly to reinstall on a new machine or to recover a broken setup.

---

## 0) Prerequisites

- Windows 10/11
- NVIDIA GPU + recent NVIDIA driver
- Python 3.12
- Git

Optional but recommended:
- Visual Studio Build Tools (only if compiling extra CUDA libs like `flash-attn` later)

---

## 1) Clone repository

```powershell
cd C:\Users\<YOU>\OneDrive\Dev

git clone https://github.com/flybirdxx/ComfyUI-Qwen-TTS.git
cd ComfyUI-Qwen-TTS
```

---

## 2) Create venv (Python 3.12) and install dependencies

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python -m pip install --upgrade pip setuptools wheel
.\.venv\Scripts\python -m pip install -r .\requirements.txt
```

---

## 3) Install CUDA-enabled PyTorch (GPU)

This setup uses CUDA 12.1 wheels and is confirmed working:

```powershell
.\.venv\Scripts\python -m pip install --index-url https://download.pytorch.org/whl/cu121 --upgrade --force-reinstall \
  torch==2.5.1+cu121 torchaudio==2.5.1+cu121 torchvision==0.20.1+cu121
```

Verify GPU is visible:

```powershell
.\.venv\Scripts\python -c "import torch; print('torch', torch.__version__); print('cuda available', torch.cuda.is_available()); print('cuda version', torch.version.cuda)"
```

---

## 4) Install ComfyUI in the same workspace

```powershell
if (!(Test-Path .\ComfyUI)) { git clone https://github.com/comfyanonymous/ComfyUI.git ComfyUI }
.\.venv\Scripts\python -m pip install -r .\ComfyUI\requirements.txt
```

---

## 5) Install Qwen-TTS custom nodes into ComfyUI

This copies the custom node package into ComfyUI.

```powershell
New-Item -ItemType Directory -Force .\ComfyUI\custom_nodes\ComfyUI-Qwen-TTS | Out-Null
robocopy .\ .\ComfyUI\custom_nodes\ComfyUI-Qwen-TTS /E /XD .git .venv ComfyUI models | Out-Null
```

Copy local model weights into ComfyUI models:

```powershell
New-Item -ItemType Directory -Force .\ComfyUI\models\qwen-tts | Out-Null
robocopy .\models\qwen-tts .\ComfyUI\models\qwen-tts /E | Out-Null
```

---

## 6) Install SoX (required by TTS pipeline)

```powershell
winget install -e --id ChrisBagwell.SoX
```

SoX path used by the working run script:

```
%LOCALAPPDATA%\Microsoft\WinGet\Packages\ChrisBagwell.SoX_Microsoft.Winget.Source_8wekyb3d8bbwe\sox-14.4.2
```

---

## 7) Fixes applied for compatibility

These are required with the current combination of models + `transformers`:

- Added fallback to fill missing `pad_token_id`
- Added fallback for unsupported RoPE type (`default` → `linear`)
- Added safe AutoProcessor loading with `fix_mistral_regex=True` if supported
- Downgraded `transformers` to 4.57.2 to avoid tokenizer errors

The applied fixes are already in this repo. If you pull new code and regress, re-apply:

```powershell
.\.venv\Scripts\python -m pip install --upgrade "transformers==4.57.2"
```

---

## 8) Run ComfyUI (recommended script)

Use the script created in this repo:

```powershell
.\scripts\run-comfyui.ps1
```

This sets SoX in PATH and launches ComfyUI on port 8188.

Open in browser:
- http://127.0.0.1:8188

**Do not** open `http://0.0.0.0:8188` in a browser.

---

## 9) Load a TTS workflow (avoid image workflow)

ComfyUI defaults to an image workflow. For TTS use one of:

- example/example.json
- example/Custom Save Voice.json
- example/Multi-character dialogue.json

In the UI: Menu → Load → pick a file.

---

## 10) Common errors & fixes

### A) "CheckpointLoaderSimple: ckpt_name not in []"
You loaded an image workflow. Load a TTS workflow instead.

### B) "Invalid audio file" in LoadAudio
Place the file in ComfyUI/input or upload directly in the node.

### C) "pad_token_id" missing
Fix is already included in this repo. If it reappears, re-apply patch to `qwen_tts/core/models/configuration_qwen3_tts.py` and the copy in `ComfyUI/custom_nodes/...`.

### D) "KeyError: 'default'" from RoPE
Your `transformers` lacks a `default` RoPE mapping. The fallback patch is already included and forces `linear` with `factor=1.0`.

### E) "_patch_mistral_regex got multiple values"
Downgrade `transformers` to 4.57.2 and keep the AutoProcessor fallback code.

### F) Audio outputs sound like gibberish
This happened with `transformers` 5.0.0. Downgrading to 4.57.2 fixed it.

---

## 11) Optional speedups (not required)

- `flash-attn` and `triton` are optional but require CUDA Toolkit + VS Build Tools + matching Torch build.
- Current setup uses PyTorch SDPA and works correctly without them.

---

## 12) Known working environment summary

- Python 3.12
- PyTorch 2.5.1 + cu121
- transformers 4.57.2
- CUDA driver with RTX 3060 (laptop)
- ComfyUI 0.10.0

---

## 13) Quick health check

```powershell
.\.venv\Scripts\python -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```

In ComfyUI: run `Qwen3-TTS CustomVoice` and listen in `PreviewAudio`.

---

If anything breaks after updates, this guide is the stable restore path.
