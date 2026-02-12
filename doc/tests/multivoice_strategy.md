# Multi-Voice Audiobooks + Voice Cloning Strategy (Qwen3-TTS)
**Scope:** frequent audiobook generation, multi-character (many recurring voices), with a growing “voice database”.

## 1) What you already have in this repo
There are two distinct “voice” workflows:

### A) Preset voices (fastest)
- Uses the **CustomVoice** model (“preset speakers”: Serena, Ryan, etc.).
- No reference audio needed.
- Great when the preset library is enough.

### B) Voice cloning (for unlimited character coverage)
- Uses the **Base** model (“voice clone”).
- A clone is conditioned by a *prompt* extracted from reference audio.

This repo explicitly supports **precomputing and reusing** voice clone prompts:
- Prompt extraction: VoiceClonePromptNode (ComfyUI) or `create_voice_clone_prompt(...)` (Python API)
- Persistence: SaveVoiceNode / LoadSpeakerNode (ComfyUI)
- Multi-role batching: RoleBankNode + DialogueInferenceNode (ComfyUI)

Sources:
- Nodes overview: README.md
- Prompt extraction API: qwen_tts/inference/qwen3_tts_model.py
- Save/load prompt: nodes.py

## 2) Are clones “on the fly”? Can they be pre-made?
**Yes, clones can be pre-made and saved.**

### On-the-fly cloning (slower)
If you keep passing `ref_audio` each time you generate, the system must repeatedly:
- tokenize the reference speech into codes
- extract speaker embedding

That adds overhead and can also introduce minor variability.

### Pre-made clones (recommended for a permanent voice DB)
Do this instead:
1) Extract a reusable prompt once (from 5–15s reference audio)
2) Save it (prompt + metadata + optional reference WAV)
3) Reuse it for every future audiobook

In ComfyUI, that’s exactly what:
- VoiceClonePromptNode → SaveVoiceNode
- LoadSpeakerNode → RoleBankNode → DialogueInferenceNode
are designed for.

Bottom line: for “many audiobooks regularly”, you want **prompt extraction only once per voice**, not per chapter.

## 3) What is actually stored in a clone prompt?
The Base model’s prompt items include (simplified):
- `ref_spk_embedding`: speaker embedding (always)
- `ref_code` + `ref_text`: optional (used for ICL mode)

Two modes exist:

### Mode 1 — x-vector only (fastest prompt build)
- `x_vector_only_mode=True`
- Uses only `ref_spk_embedding`
- Doesn’t require `ref_text`
- Best when you want a huge library quickly and your reference transcripts are not available

### Mode 2 — ICL mode (often higher similarity)
- `x_vector_only_mode=False` (ICL is enabled)
- Requires `ref_text`
- Uses `ref_code` (speech tokenizer codes) + speaker embedding
- Often worth it for “main cast” voices you reuse a lot

Practical tactic for a voice DB:
- Main characters: ICL mode prompts
- Minor/background characters: x-vector-only prompts

## 4) Multi-voice audiobook performance: what matters
### What *doesn’t* matter much
- Switching between preset speaker names (CustomVoice) is basically free.

### What *does* matter
- **Model size:** 1.7B is slower than 0.6B.
- **Attention backend:** flash_attention_2 (or sage_attn if installed) is a big speed win.
- **Batch size stability:** avoid OOM thrash; a smaller stable batch is faster end-to-end.
- **Prompt extraction vs reuse:** extracting prompts repeatedly is wasted time.
- **Work scheduling:** for multi-role scripts, batching multiple lines at once is usually the biggest throughput win.

## 5) Best practice pipeline for your use case
### Step 0 — pick a “production model” per project type
- Academic / non-fiction, neutral tone, maximum throughput: **0.6B** (what you benchmarked)
- Fiction / dramatic dialog / better prosody: likely **1.7B** for final production

Tip: treat voice prompts as **model-family artifacts**.
If you standardize on 1.7B for production, build your permanent voice DB with that model.

### Step 1 — build a permanent voice library
For each voice you want to keep forever:
1) Choose reference audio (5–15s clean, minimal noise)
2) Create prompt (ICL if you have transcript; else x-vector-only)
3) Save prompt + metadata (name, tags like child/old/whimsical)

Use ComfyUI:
- VoiceClonePromptNode → SaveVoiceNode

Then you have a reusable asset in `ComfyUI/models/qwen-tts/voices/`.

### Step 2 — for each audiobook, assign characters to saved voices
- LoadSpeakerNode for each role
- Put them into a RoleBankNode
- Run DialogueInferenceNode with a script format:
  - `Narrator: ...`
  - `Alice: ...`
  - `Bob: ...`

### Step 3 — batch for speed
- Increase DialogueInferenceNode `batch_size` until it becomes unstable (OOM) and back off.
- Keep the model loaded (don’t unload between chapters).

## 6) Model comparison (0.6B vs 1.7B) for *your* goals
### 0.6B
- Pros: much faster; fits bigger batches; great for frequent generation
- Cons: prosody/stability limitations; fewer “instruct-style” capabilities
- Voice cloning: supported via Base model choice in nodes (fast)

### 1.7B
- Pros: higher quality, better fiction/dialogue, VoiceDesign is available
- Cons: slower; smaller stable batches on 10GB VRAM
- VoiceDesign: **locked to 1.7B** (per README)

Recommended tactic:
- Use 0.6B to iterate and generate quickly.
- Use 1.7B for “final render” of fiction or high-value books, and to design new archetype voices.

## 7) Suggested next benchmarks (multi-voice)
To extend performance understanding beyond single-voice narration:

1) Multi-role DialogueInference benchmark (8 roles)
- Build 8 saved prompts
- Run DialogueInferenceNode with batch sizes 2/4/8
- Measure wall time and OOM threshold

2) Compare prompt modes
- Same role, same text:
  - x-vector-only prompt
  - ICL prompt
- Measure speed and similarity quality

3) Compare models for the same multi-role script
- 0.6B vs 1.7B with same batching strategy
