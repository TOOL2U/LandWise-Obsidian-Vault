## ComfyUI Daily Workspace Build — 2026-04-15

### Team Briefing

**Content needs (from 2026-04-13 brief context):**
- 4 Instagram posts queued and pending approval (act_55 through act_58 — all educational pillar)
- Posts skew heavily educational; content mix gap: zero Before/After posts published to date
- Before/After format is highest-converting Instagram format per Channel 2 strategy (demonstrates tangible survey value, drives DM enquiries)
- Priority: build production-ready Before/After workflow to close this content-type gap

**Installed checkpoints / upscalers / controlnets used:**
- Primary: `juggernautXL_ragnarokBy.safetensors` (best-available SDXL photorealism)
- Upscaler: `4x-UltraSharp.pth`
- ControlNet: `controlnet-depth-sdxl-1.0.safetensors` + `controlnet-canny-sdxl-1.0.safetensors`
- IP-Adapter: `ip-adapter_sdxl.safetensors` + `clip_vision_g.safetensors`
- Note: All model references are per existing LandWise_InstagramPost_20260411 specs — assumed installed

**Missing nodes blocking higher levels:**
- AnimateDiff Evolved: not confirmed installed (blocks P3-C Reel workflow)
- HunyuanVideo / Runway Gen4: external API, not ComfyUI nodes (blocks P3 Drone Video)
- No blockers identified for P3-B (Before/After) — all required nodes available per previous workflow runs

---

### Upgrades Executed

**Blocker: ComfyUI Desktop was not running at `http://127.0.0.1:8188` at task start time.**
- `curl -sf http://127.0.0.1:8188/system_stats` returned connection refused (status 000)
- Cannot launch ComfyUI from the automation sandbox (requires native macOS `open -a ComfyUI` on user's machine)
- `jarvis_comfyui_builder.py --build-loop` could not be executed — requires live ComfyUI API

**Resolution: Workflow JSON built directly without requiring live ComfyUI.**
- Architect loop logic executed manually: inventoried existing workflows, selected next build-ladder item, built full node graph JSON, validated wiring, saved versioned file.

**Ladder levels built this session:**
- **P3-B: Before/After Comparison** — DONE (v2.0, upgraded from template)

**New workflows published to sidebar:**
- `LandWise_BeforeAfter_20260415.json` — BUILT ✅, sidebar push BLOCKED (ComfyUI DOWN)
- `LandWise_BeforeAfter_Latest.json` — BUILT ✅ (pointer updated)
- Both files saved to `config/comfyui_workflows/` and `config/comfyui_workflows/builds/`

**Workflow upgrade summary (v1.0 template → v2.0 production):**
- Model: `juggernautXL_v10` → `juggernautXL_ragnarokBy` (better photorealism on landscapes)
- CLIP encoding: `CLIPTextEncode` → `CLIPTextEncodeSDXL` dual (4096 target res, text_g + text_l)
- Sampler: `KSampler` → `KSamplerAdvanced` with `return_with_leftover_noise` for Hi-Res Fix compatibility
- Added Hi-Res Fix pass: `LatentUpscaleBy 1.5x` → `KSamplerAdvanced 15 steps denoise 0.35`
- Added `IPAdapterApply` brand consistency (weight 0.22) — matches visual identity from Instagram Post workflow
- Added 4x-UltraSharp upscale on AFTER image before compositing
- Depth ControlNet strength: 0.70 → 0.65 (more creative freedom, terrain still preserved)
- Canny ControlNet strength: 0.40 → 0.35 (softer edge match for natural land)
- Extended negative prompt (film grain, chromatic aberration, lens flare)
- Text overlay typography updated to LandWise brand colours (#C97C5D terracotta, #1A1A1A, #E6DFD5)
- Node count: 20 (template) → 27 (production)

---

### Verification

- Sidebar entries confirmed (via /userdata API): **NO — ComfyUI was DOWN**
- ComfyUI /system_stats responsive: **NO (connection refused)**
- Workflow JSON validated (wiring check): **YES — 27 nodes, all references valid, no dangling wires**
- Files saved to workspace: **YES** — `config/comfyui_workflows/LandWise_BeforeAfter_20260415.json`

**Action required when ComfyUI next starts:**
```bash
# Run this to push the workflow to ComfyUI sidebar:
curl -X POST "http://127.0.0.1:8188/userdata/workflows%2FLandWise_BeforeAfter_20260415.json?overwrite=true" \
  -H "Content-Type: application/json" \
  --data-binary @config/comfyui_workflows/LandWise_BeforeAfter_20260415.json

curl -X POST "http://127.0.0.1:8188/userdata/workflows%2FLandWise_BeforeAfter_Latest.json?overwrite=true" \
  -H "Content-Type: application/json" \
  --data-binary @config/comfyui_workflows/LandWise_BeforeAfter_Latest.json
```
Or drag-drop `config/comfyui_workflows/LandWise_BeforeAfter_20260415.json` into ComfyUI browser window.

---

### Next Recommended Upgrade

**Task:** P3-C — Instagram Reel (7–9s AnimateDiff motion)
- File: `workflow_3_instagram_reel.json` (template exists — needs production upgrade)
- Lead channel impact: **Channel 2 — Instagram Reels** (highest organic reach format on Instagram 2026)
- Blocker to resolve first: confirm `ComfyUI-AnimateDiff-Evolved` is installed
  ```bash
  ls ~/Documents/ComfyUI/custom_nodes/ | grep -i animatediff
  ```
  If missing: `python3 scripts/jarvis_comfyui_builder.py --install-nodes`
- Estimated complexity: MEDIUM (AnimateDiff adds ~8 nodes to existing pipeline)
- Content justification: Drone flyover reels showing land plots with sea view confirmation — exactly what converts fence-sitting buyers into enquiries

**Secondary:** Confirm ComfyUI auto-launch on system boot to prevent this blocker recurring.
Add to macOS Login Items: `System Settings → General → Login Items → +` → ComfyUI.app
