---
name: comfyui-video-pipeline
description: Local ComfyUI video-pipeline runbook for WGNR Sounds — MPS/ComfyUI ops on the Mac Studio M2 Ultra, Draft-First render ladder (low-res motion-vector preview → Principal confirmation → hi-res), beat-map generation from the master track, ffmpeg stitch + finishing, and render-output hygiene. Open-weights models (LTX-Video / HunyuanVideo) only; cloud video generation permanently out of scope.
trigger_phrases:
  - comfyui
  - comfyui pipeline
  - video render
  - draft-first ladder
  - low-res preview
  - motion-vector preview
  - hi-res render
  - beat map
  - beat mapping
  - ffmpeg stitch
  - ltx-video
  - hunyuanvideo
  - mps
  - render queue
  - video pipeline
---

# comfyui-video-pipeline — Label-Specific Skill

> **Scope:** Execution runbook for the WGNR Sounds local video pipeline — ComfyUI orchestration, open-weights model ops on Apple Silicon MPS, Draft-First render ladder, beat-map generation, ffmpeg stitch + finishing, render-output hygiene. The how-to for video-engineer; the coordination surface for video-coordinator.
> **Applies to:** video-engineer (runbook owner; mandatory), video-coordinator (queue/gate-log/hygiene sections; mandatory), video-director (Draft-First ladder awareness; reference)
> **Reference:** `prds/PRD-wgnr-sounds-video-production.md` §6 (Infrastructure Rule — verbatim source), §9 (lifecycle); skill `velvut-visual-constitution` (per-render checks)
> **Owner:** Wagner dos Santos (Principal) — WGNR Sounds Record Label

## 1. Purpose

This skill is the pipeline runbook. It exists so that no agent improvises infrastructure: every render follows the same ladder, every gate is logged, every model choice is honest about its verification state, and cloud services are never touched.

## 2. Infrastructure Rule (verbatim — PRD §6, protected)

- Cloud tools are bypassed to protect the budget. Use open-weights video models (such as LTX-Video or HunyuanVideo) running locally on Apple Silicon MPS hardware (Mac Studio M2 Ultra, Principal-declared).
- ComfyUI is the orchestration surface (VERIFIED-FACT: installed and running at `/Users/wgnr/AI/comfyui/`, process `server.py` observed 2026-09-06).
- **Draft-First check logic is mandatory on every execution path: high-resolution processing cycles are FORBIDDEN until a fast, low-res preview of the motion vectors is delivered and manually confirmed by the Principal.**
- Final assembly via ffmpeg (VERIFIED-FACT: present in the ops container `/usr/bin/ffmpeg`; Mac-side stitch flow already documented in the vault `Google Ideas.md`).
- Model choice (LTX-Video vs HunyuanVideo vs both) is UNVERIFIED-CLAIM until probed on-host for MPS compatibility and speed; probe is part of scaffold acceptance.

## 3. Draft-First Render Ladder (the gate — mandatory order)

**High-resolution processing cycles are FORBIDDEN until a fast, low-res preview of the motion vectors is delivered and manually confirmed by the Principal.**

Gate steps (no step may be skipped, reordered, or batched away — each shot/sequence passes through them):

1. **GATE-1 — Build draft graph ONLY.** Configure the ComfyUI graph in draft mode: low resolution, short/preview-length motion vectors, reduced steps. Hi-res parameters are NOT set, queued, or saved into the active workflow.
2. **GATE-2 — Render low-res motion-vector preview.** Execute the draft render. Output lands in the draft area under the versioned naming scheme (`v<N>-draft`), clearly labeled DRAFT.
3. **GATE-3 — Deliver preview + recommendation to the Principal.** The preview goes to the Principal with video-director's confirm/revise/reject recommendation. An agent recommendation is NOT a confirmation.
4. **GATE-4 — Record the gate decision.** video-coordinator logs the Principal's manual confirmation in the gate log: shot ID · draft version · preview path · decision · confirmed by (Principal) · timestamp · notes.
5. **GATE-5 — Verify the record BEFORE hi-res.** video-engineer checks the gate log for a manual Principal confirmation of the exact shot + draft version. **No record = refuse the hi-res request; return the shot to draft.** This check is mandatory on every execution path.
6. **GATE-6 — Hi-res render + Constitution check.** Only confirmed shots are rendered hi-res. Every hi-res output is checked against the `velvut-visual-constitution` checklist (C1–C10) before it advances to finishing.

**Refusal duty:** if any request (from any agent, including the director or captain) asks for a hi-res cycle without a matching gate-log record, video-engineer refuses and cites GATE-5. The refusal is not negotiable and is not overridable by agent judgment.

## 4. MPS / ComfyUI Ops (video-engineer)

- ComfyUI install: `/Users/wgnr/AI/comfyui/` (Mac Studio M2 Ultra host). **PATH PRECISION (verified on-host 2026-09-13): the ComfyUI CORE is nested — `/Users/wgnr/AI/comfyui/ComfyUI/`; `custom_nodes/` and `models/` live under the nested core dir, and the core venv python is `/Users/wgnr/AI/comfyui/ComfyUI/venv/bin/python`.** Host operations require the A0 CLI connector active in-session — never assume host access; signal the Principal when a host step is required.
- Device: Apple Silicon MPS (not CUDA). Expect MPS-specific constraints: memory ceiling vs unified memory, ops without MPS kernels falling back to CPU, and slower attention paths. Benchmark before promising render times.
- Model lock discipline: LTX-Video and HunyuanVideo are both UNVERIFIED-CLAIM for MPS compatibility/speed until the on-host probe (label PRD Open Question 4). Do not lock a model in any workflow spec before the probe results land. Build graphs so the video-model node is swappable (text-to-video and image-to-video variants per silhouette strategy).
- Pipeline hygiene: one graph change at a time; version graph JSON alongside outputs; never mutate a graph that produced an approved output without forking the version.

## 5. Beat-Map Generation (audio-reactive sync)

From the master track, generate the beat map BEFORE storyboarding renders:

1. "Is This How It Ends?" constants: **107 BPM, 4/4** → ~560.7 ms per beat, ~2.2430 s per bar — tempo superseded per Principal ruling 2026-09-14 — 148 marked historical; 107 BPM confirmed by canonical MIDI export (flat 107.0), stems curve (104.79–109.83, avg ≈107), and Principal authorization.
2. Compute beat/bar timestamps over the full runtime (beat index × 0.5607 s; bar index × 2.2430 s) and mark section boundaries (verse = quiet introspective low baritone over tom-toms; chorus = wall-of-sound distorted power chords) from the track structure.
3. Emit the beat map as the shared sync artifact (JSON/markdown table) — every shot's duration, cut point, and movement anchor references beat/bar indexes, not wall-clock guesses.
4. Verify the map against the actual master audio (onset check) before it is used to time renders — a silent drift of even a few ms/beat accumulates over a full track. The check remains REQUIRED: it validates the 107 grid AND maps the section boundaries (`beatmap-generator.py` `verify_onsets()` gate).

## 6. ffmpeg Stitch + Finishing Chain

- ffmpeg is available in the ops container at `/usr/bin/ffmpeg` (VERIFIED-FACT 2026-09-06); Mac-side stitch flow documented in the vault `Google Ideas.md`.
- Finishing chain implements the Velvut look per the Constitution: crushed deep blacks, high-contrast underexposed grade, film grain pass. Do not "enhance" beyond the Constitution — no brightening, no noise reduction that kills the grain.
- Cut timing comes from the beat map (§5): cuts land on beat/bar boundaries.
- Platform masters: YouTube 16:9; TikTok/Reels 9:16 (video-coordinator owns packaging; ffmpeg renders per spec).
- Every stitch command is recorded with the package (reproducibility): inputs, filter chain, output spec.

## 7. Render-Output Hygiene

- All outputs land under the versioned naming tree owned by video-coordinator: `velvut/is-this-how-it-ends/sh-<NN>/v<N>-<draft|hires|final>`. No overwrites; every artifact versioned.
- Drafts and finals never share a directory state; drafts are clearly labeled.
- Failed/discarded renders are reported to video-coordinator for purge — not silently deleted on the host.
- Draft previews are purged only after the corresponding package ships; finals are never purged without Principal direction. Disk usage is reported with queue status when drafts accumulate.

## 8. Verification (per render cycle)

- Draft cycle: GATE-1/2/3 followed? Draft clearly labeled and versioned? Recommendation delivered to the Principal?
- Gate record: exact shot + draft version present in the gate log with Principal attribution before any hi-res?
- Hi-res cycle: Constitution checklist (C1–C10) run and passed before finishing?
- Finish: cut points on the beat map? Grain/blacks per Constitution? Package carries the stitch command + gate-log excerpt?

## 9. References

- `prds/PRD-wgnr-sounds-video-production.md` §6 (Infrastructure Rule), §9 (lifecycle), §10 (open questions — model lock pending probe)
- Skill `velvut-visual-constitution` (per-render checklist C1–C10 + Draft-First gate enforcement)
- Vault: `/a0/usr/obsidian/03-wgnr-sounds/10-music/velvut/promotions/Google Ideas.md` (Mac-side stitch flow)
- ComfyUI: `/Users/wgnr/AI/comfyui/` (VERIFIED-FACT 2026-09-06)
