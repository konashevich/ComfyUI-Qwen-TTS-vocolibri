# 🚀 SuperJet Mode: Optimized Qwen-TTS Setup

This environment has been tuned for maximum performance on Linux with NVIDIA hardware.

## 🛠 Optimization Stack

- **Python**: 3.12.3
- **PyTorch**: 2.5.1 + cu124 (High-performance GPU build)
- **Flash Attention 2**: Installed (Version 2.8.3). This provides O(N²) -> O(N) memory efficiency and significant speedups in transformer layers.
- **ONNX Runtime GPU**: Configured with `CUDAExecutionProvider` and `TensorrtExecutionProvider`.
- **System Audio**: `SoX` v14.4.2 installed via `apt` for high-throughput wave processing.

## 🏎 How to Run

Use the optimized launcher script in the root directory:

```bash
./run-comfyui.sh
```

## 🔍 Performance Verification

You can verify the "SuperJet" status by running:

```bash
./.venv/bin/python -c "import torch; import flash_attn; print(f'GPU: {torch.cuda.get_device_name(0)} | Flash Attn 2: {flash_attn.__version__}')"
```

## 🔋 Hardware Horsepower
- **GPU**: NVIDIA RTX 3080
- **Execution**: Forced GPU path. If CUDA is not available, the system is configured to halt rather than fall back to slow CPU inference.
- **Cooling**: Expect high fan RPM during generation—this setup utilizes all available hardware resources.
