# Voice Library Manual (Preset + Cloned + Designed Voices)
**Goal:** build a permanent, reusable database of voices for multi-character audiobooks.

This repo supports two different concepts:
- **Preset voices** (no reference audio) via CustomVoice
- **Cloned voices** (from reference audio) via Base + a saved prompt (`.qvp`)
- **Designed voices** (from text description) via VoiceDesign (1.7B), which you can optionally convert into a permanent clone

---

## 0) Where voices are stored
When you save a voice in ComfyUI using SaveVoiceNode, files go here:
- `ComfyUI/models/qwen-tts/voices/`

Typical outputs per voice name (e.g. `alice_child`):
- `alice_child.qvp`  → the reusable voice prompt (tensors)
- `alice_child.json` → metadata (ref_text, version, etc.)
- `alice_child.wav`  → optional reference/preview audio

**Important:** the `.qvp` is the thing that makes the voice “pre-made”. It is **not** just a text description.

---

## 1) Choose your model strategy (0.6B vs 1.7B)
### If you want maximum throughput (many books regularly)
- Use **0.6B** for production.
- Build your voice library (prompts) using **0.6B**.

### If you want best quality for fiction/dialogue
- Use **1.7B** for production.
- Build your “final” voice library using **1.7B**.

You can still prototype voices with 0.6B and later re-extract prompts with 1.7B.

---

## 2) Reference audio requirements (for cloning)
Good reference audio is the #1 factor for clone quality.

**Recommended**
- 5–15 seconds per voice
- Single speaker only
- Clean recording (no music, no heavy reverb)
- Minimal background noise
- Normal speaking pace

**Avoid**
- Multiple speakers in one clip
- Loud music/ambience
- Strong compression artifacts
- Very quiet recordings

If you have the transcript of the reference audio, keep it (it helps quality in ICL mode).

---

## 3) Two cloning modes (pick one per voice)
The clone prompt can be extracted in two modes:

### A) “x-vector only” (fastest to build, easiest)
- Set `x_vector_only = true`
- `ref_text` is not required
- Great for building a *large* library quickly

### B) “ICL mode” (often higher similarity)
- Set `x_vector_only = false`
- `ref_text` is required (the transcript of the reference audio)
- Best for main cast voices you’ll reuse a lot

Practical tactic:
- Main characters: ICL
- Minor characters: x-vector only

---

## 4) Build a cloned voice (ComfyUI step-by-step)
### Step 1 — Load the reference audio
- Use your ComfyUI audio loader node (or whatever workflow you already use) to produce an `AUDIO` output.

### Step 2 — Extract the reusable voice prompt
Use **Qwen3 Voice Clone Prompt** (VoiceClonePromptNode):
- `ref_audio`: connect your `AUDIO`
- `ref_text`: paste transcript (recommended)
- `model_choice`: 0.6B or 1.7B
- `precision`: bf16 (recommended on NVIDIA)
- `attention`: auto (will pick flash_attention_2 if available)
- `x_vector_only`:
  - true if you don’t have transcript
  - false if you do have transcript

Output: `voice_clone_prompt`

### Step 3 — Save it to your permanent library
Use **Qwen3 Save Voice** (SaveVoiceNode):
- `voice_clone_prompt`: connect from Step 2
- `filename`: give it a stable name, e.g.
  - `narrator_neutral_m1`
  - `alice_child_v1`
  - `bob_old_gravel_v1`
- optional:
  - `audio`: connect reference audio (creates a preview WAV)
  - `ref_text`: paste transcript (stored into JSON)

Result: files written into `ComfyUI/models/qwen-tts/voices/`.

That voice is now “pre-made” and reusable forever.

---

## 5) Use a saved voice in an audiobook workflow
### Single-voice generation
- Use **Qwen3 Load Speaker (WAV)** (LoadSpeakerNode) to load the voice
- Feed its `voice_clone_prompt` into **VoiceCloneNode** (or any node that accepts `VOICE_CLONE_PROMPT`)

### Multi-character audiobook (recommended)
1) Load each character voice:
   - LoadSpeakerNode → outputs `voice_clone_prompt`
2) Put them into **Qwen3 Role Bank** (RoleBankNode)
   - `role_name_1 = Narrator`, `prompt_1 = narrator_prompt`
   - `role_name_2 = Alice`, `prompt_2 = alice_prompt`
   - etc.
3) Run **Qwen3 Dialogue Inference** (DialogueInferenceNode)
   - Provide script lines like:
     - `Narrator: Chapter one...`
     - `Alice: What are you doing?`
     - `Bob: Nothing.`
   - Tune `batch_size` upward until you hit OOM, then step back.

Performance tip: keep `unload_model_after_generate = false` while generating an entire book, so the model stays cached.

---

## 6) Make “designed” voices (text → voice), then make them permanent
If you don’t have reference audio for a character archetype:

### Step A — VoiceDesign (1.7B only)
Use **VoiceDesignNode** with a description like:
- “A young girl, slightly breathy, playful tone, high pitch”
- “An elderly man, calm, slightly raspy, slow pace”

This outputs audio (a synthetic sample voice).

### Step B — Convert the designed voice into a permanent clone
Feed that generated audio into **VoiceClonePromptNode** and then **SaveVoiceNode**.

This turns a “text-designed voice” into a reusable `.qvp` asset.

---

## 7) Naming + versioning conventions (strongly recommended)
You will accumulate many voices; naming matters.

Good patterns:
- `narrator_neutral_v1`
- `alice_child_bright_v1`
- `bob_old_gravel_v2`
- `merchant_comic_v1`

When you improve a voice, bump version suffix (`v1` → `v2`) instead of overwriting.

---

## 8) Troubleshooting
### “ref_text is required…” error
- You set `x_vector_only = false` but left `ref_text` empty.
- Fix: provide transcript OR set `x_vector_only = true`.

### OOM (out of memory)
- Reduce batch size in DialogueInferenceNode.
- Avoid running other CUDA workloads.
- Keep attention on `auto` (flash-attn2 is fastest, but still uses VRAM).

### Clone sounds wrong / unstable
- Improve reference audio quality.
- Use ICL mode with correct transcript.
- Make the reference clip longer (but keep it clean).

---

## 9) Minimal checklist (fast workflow)
1) Pick model (0.6B for speed; 1.7B for quality)
2) Pick reference audio (clean 5–15s)
3) VoiceClonePromptNode → SaveVoiceNode
4) LoadSpeakerNode anytime → reuse in RoleBank/DialogueInference
