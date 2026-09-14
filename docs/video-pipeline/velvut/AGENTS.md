# docs/video-pipeline/velvut — Velvut MIDI-Driven Audio-Reactive Pipeline Artifacts

## Purpose

Deploy-ready artifact set for the Velvut MIDI-driven audio-reactive ComfyUI pipeline (Mac Studio M2 Ultra, MPS). Authored 2026-09-13 by `video-engineer`; re-bound 2026-09-13 to **"Is This How It Ends?"** @ 107 BPM, 4/4 (tempo superseded per Principal ruling 2026-09-14 — 148 historical). Host DEPLOY EXECUTED 2026-09-13: 4 node packs live in the nested core, server relaunched via launchd.

## Ownership

- Authored/updated by: `video-engineer` (ComfyUI pipeline artifacts).
- Consumed by: Principal (gate), `video-director` (treatment alignment), `video-coordinator` (render queue, gate log, naming tree).

## Local Contracts (binding on every artifact here)

1. **Draft-First gate (PRD §6, verbatim):** hi-res processing cycles are FORBIDDEN until a low-res motion-vector preview is Principal-confirmed and gate-logged. `draft-workflow.json` must never contain hi-res parameters.
2. **Velvut Visual Constitution C1–C10:** binds every prompt, graph, and math artifact. C1: red backlight is the ONLY illumination — the brief's `"pure white/hot red"` phrasing is stripped; white is never reintroduced.
3. **Track/BPM (RESOLVED 2026-09-14):** "Is This How It Ends?" — **107 BPM, 4/4 → ~560.7 ms/beat, ~2.2430 s/bar** — tempo superseded per Principal ruling 2026-09-14 — 148 marked historical; 107 BPM confirmed by canonical MIDI export (flat 107.0), stems curve (104.79–109.83, avg ≈107), and Principal authorization. `TRACK_BPM = 107.0` in `beatmap-generator.py` is the single constant. The onset-verification gate remains REQUIRED — it validates the 107 grid AND maps section boundaries. (Historical: 148 declared 2026-09-13; "Take Me Back" @ 151, 2026-09-06.)
4. **Fact-gate on repo URLs:** only verified URLs are hardcoded in `deploy-custom-nodes.sh` — Advanced-ControlNet, FizzNodes, RyanOnTheInside (MIDI reader, pinned default), ComfyUI-AudioReactor (audio-frame onset cross-verification). Pinned default marked: *Principal-overridable default, 2026-09-13, unanswered modal — auto-selected per goal-mode autonomy.* No standalone "ComfyUI-MIDI" repo exists (verified 2026-09-13). Never pattern-guess.
5. **No cloud video-generation services, ever** (Principal direction 2026-09-06).
6. **Naming/hygiene:** render tree `velvut/is-this-how-it-ends/sh-NN/vN-<stage>`; no overwrites; drafts never mixed into finals.

## Contents

| File | Role |
|---|---|
| `deploy-custom-nodes.sh` | Mac-side idempotent custom-node installer — DEPLOYED 2026-09-13 (4 packs live in the nested core, registration verified) |
| `midi-parse-graph-spec.md` | Parse layer: MIDI → `drums_velocity_spikes` + `guitar_velocity_tracking` |
| `math-expressions.md` | Strobe controller (red-only) + motion vector driver (clamped) |
| `prompt-channels.md` | Verbatim brief conditioning channels + mandatory negative block (track-agnostic) |
| `beatmap-generator.py` | BPM-parameterized beat/bar map generator (TRACK_BPM = 107.0, authoritative); REQUIRED onset-verification gate (validates the 107 grid + maps section boundaries) |
| `draft-workflow.json` | GATE-1 draft graph (low-res, preview-length, swappable video-model node) |

## Verification

- `bash -n deploy-custom-nodes.sh` — syntax check; EXECUTED on-host 2026-09-13 (deployment complete, registration verified).
- `python3 -m py_compile beatmap-generator.py`; live run emits valid JSON.
- `python3 -m json.tool draft-workflow.json` — valid JSON.
- Beat math: 107 → 560.7 ms/beat, 2.2430 s/bar.

## Open items (exactly one — blocks GATE-1)

1. **`.mid` file from the Principal** (parse config + MIDI track indexes).

RESOLVED: Track/BPM (2026-09-13, Local Contracts #3). MIDI reader PINNED (Local Contracts #4, Principal-overridable). Host DEPLOY EXECUTED 2026-09-13 ~23:14 EDT (exec consent live): 4 node packs installed to the nested core (`/Users/wgnr/AI/comfyui/ComfyUI/custom_nodes/`) — Advanced-ControlNet 27a67fe, FizzNodes 7d6ea60, RyanOnTheInside 52daf66, AudioReactor 75a2432; requirements via the core venv (torch 2.11.0 untouched); server restarted via launchd `com.wgnr.comfyui` (KeepAlive, identical relaunch); all 4 packs verified registered via /object_info — incl. **MIDILoader / MIDIFeatureExtractor / MIDIToAudio** (RyanOnTheInside, semantic names) and 79 Audio* classes (AudioReactor).

## Child DOX Index

(none)