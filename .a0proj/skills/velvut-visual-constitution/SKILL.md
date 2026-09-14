---
name: velvut-visual-constitution
description: Velvut Visual Constitution — the protected per-render checklist for all Velvut video renders (red-backlight-only, volumetric fog, crushed blacks + grain, zero-facial-detail silhouettes, BPM-matched movement, baritone frontman). A render that fails any item is rejected before it reaches the Principal. Embeds the Draft-First gate verbatim.
trigger_phrases:
  - velvut visual constitution
  - visual constitution
  - constitution check
  - silhouette check
  - facial detail check
  - red backlight
  - crushed blacks
  - bpm-matched movement
  - headbanging
  - per-render checklist
  - draft-first
  - hi-res forbidden
---

# velvut-visual-constitution — Label-Specific Skill

> **Scope:** Executable per-render checklist for the Velvut Visual Constitution. Every Velvut video output (draft preview, hi-res render, finished shot) is checked against this list before it advances. A render that fails any item is rejected before it reaches the Principal.
> **Applies to:** video-director (enforcement at review gates; mandatory), video-engineer (pre-render prompt/graph construction + post-render output check; mandatory). video-coordinator consumes the verdicts for gate logging.
> **Reference:** `prds/PRD-wgnr-sounds-video-production.md` §5 (Velvut Visual Constitution — verbatim source), §6 (Infrastructure Rule), §9 (lifecycle)
> **Owner:** Wagner dos Santos (Principal) — WGNR Sounds Record Label

## 1. Purpose

This skill makes "Constitution-compliant" an auditable claim. The Constitution rules below are **verbatim from the Principal brief** (PRD §5, protected). The checklist (§3) is the enforcement instrument; the Draft-First gate (§4) is the render-gating instrument. Neither is optional, and neither may be paraphrased away.

## 2. Velvut Visual Constitution (verbatim — PRD §5, protected)

**Sonic identity (for audio-reactive mapping):**
- Project track: "Is This How It Ends?" — **107 BPM, 4/4** (~560.7 ms/beat, ~2.2430 s/bar) — tempo superseded per Principal ruling 2026-09-14 — 148 marked historical; 107 BPM confirmed by canonical MIDI export (flat 107.0), stems curve (104.79–109.83, avg ≈107), and Principal authorization. House identity: nu-metal and alt-rock (Principal ruling 2026-09-12).
- Dynamics: heavy quiet-loud contrasts; verse = quiet introspective — low, deep baritone vocal over driving tom-tom beats; chorus = massive walls of distorted power chords and anthemic question hooks.
- (Re-bind history: track pinned 2026-09-13 under the Principal's liberty directive; tempo 148 declared 2026-09-13, superseded to 107 on 2026-09-14. All visual rules below are untouched.)

**Aesthetic:** Grounded cinematic live-action look, high-contrast underexposed, crushed deep blacks, film grain.

**Lighting:** A hot red backlight/strobe atmosphere is the ONLY illumination source. Environment filled with heavy, dense volumetric fog scattering the red light.

**Character bounds:** Musicians must be pure black silhouettes with ZERO facial detail (no visible eyes, mouth, or facial structure). They are read completely by posture, hair, and instrument shape.

**Performance control:** Movement sharp, hard-hitting, controlled, matched to BPM — NOT wild, cartoonish, or flailing. Guitarist plays through shoulder/arm stance with minimal head movement. No continuous headbanging.

**Baritone-vocalist consistency (existing Principal rule, 2026-08-31):** Velvut vocals = Wagner dos Santos, baritone male. Any lip-sync-adjacent or silhouette performance logic assumes the baritone frontman.

## 3. Per-Render Checklist (enforcement — every output)

Run on **every** Velvut video output before it advances: draft previews (motion quality subset), hi-res renders (full list), and finished shots after ffmpeg processing (full list). Any FAIL = reject the render; it does NOT reach the Principal and does NOT enter the queue as approved.

| # | Check | Pass condition | FAIL means |
|---|---|---|---|
| C1 | Red-only illumination | A hot red backlight/strobe atmosphere is the ONLY illumination source; no other light color/source visible | Any secondary light source or non-red key light |
| C2 | Volumetric fog | Environment filled with heavy, dense volumetric fog scattering the red light | Thin/absent fog; fog that does not scatter the red light |
| C3 | Crushed blacks + grain | Grounded cinematic live-action look, high-contrast underexposed, crushed deep blacks, film grain | Lifted blacks, flat video look, missing grain |
| C4 | Zero facial detail | Musicians are pure black silhouettes with ZERO facial detail — no visible eyes, mouth, or facial structure | Any readable facial feature on any musician |
| C5 | Silhouette readability | Figures are read completely by posture, hair, and instrument shape | Posture/hair/instrument illegible at target resolution |
| C6 | Movement bounds | Movement sharp, hard-hitting, controlled, matched to BPM — NOT wild, cartoonish, or flailing | Flailing, cartoonish, or uncontrolled motion |
| C7 | Guitarist stance | Guitarist plays through shoulder/arm stance with minimal head movement | Guitarist performance driven by head movement |
| C8 | No headbanging | No continuous headbanging | Continuous or recurring headbanging |
| C9 | BPM lock | Movement and cuts matched to BPM ("Is This How It Ends?": 107 BPM, 4/4 → ~560.7 ms per beat, ~2.2430 s per bar — tempo superseded per Principal ruling 2026-09-14; 148 historical) | Movement/cuts off the beat map |
| C10 | Baritone frontman | Any lip-sync-adjacent or silhouette performance logic assumes the baritone frontman (Velvut vocals = Wagner dos Santos, baritone male) | Performance logic assuming any other vocal persona |

**Verdict format (per render):** `PASS` / `FAIL` per item C1–C10, overall verdict, rejected renders return to the render owner with the failing item IDs. video-director records verdicts at review gates; video-coordinator logs them in the gate log.

## 4. Draft-First Gate (verbatim — PRD §6, protected)

**Draft-First check logic is mandatory on every execution path: high-resolution processing cycles are FORBIDDEN until a fast, low-res preview of the motion vectors is delivered and manually confirmed by the Principal.**

Explicit gate steps (mandatory order — no step may be skipped or reordered):

1. **GATE-1 (draft only):** Render ONLY a fast, low-res motion-vector preview of the shot/sequence. Hi-res settings are not touched.
2. **GATE-2 (deliver preview):** Deliver the low-res preview to the Principal with the draft judgment recommendation (video-director).
3. **GATE-3 (manual confirmation):** Await the Principal's manual confirmation, recorded by video-coordinator in the gate log (shot ID, draft version, decision, confirmed by, timestamp). An agent recommendation is NOT a confirmation.
4. **GATE-4 (verify record):** Before any hi-res cycle, video-engineer verifies a gate-log record of manual Principal confirmation exists for the exact shot + draft version. No record = refuse the hi-res request and return the shot to draft.
5. **GATE-5 (hi-res + checklist):** Only then render hi-res, and run the §3 checklist on every hi-res output before it advances to finishing.

## 5. Pre-Render Prompt Hygiene (video-engineer)

When building prompts/graphs, encode the Constitution at generation time — do not rely on post-hoc correction:
- Positive prompt elements: red backlight / red strobe, dense volumetric fog, backlit black silhouettes, underexposed high-contrast, film grain, cinematic live-action look.
- Negative prompt exclusions: facial features, visible face, eyes, mouth, front lighting, white/other-color lights, headbanging, wild flailing movement, cartoonish motion, bright exposure.
- BPM anchoring: shot length and movement pacing expressed in beats/bars at 107 BPM 4/4 (~560.7 ms/beat, ~2.2430 s/bar — "Is This How It Ends?", tempo superseded per Principal ruling 2026-09-14; 148 historical).

## 6. References

- `prds/PRD-wgnr-sounds-video-production.md` §5 (Constitution, verbatim source), §6 (Infrastructure Rule), §9 (lifecycle)
- Skill `comfyui-video-pipeline` (render runbook — Draft-First ladder implementation)
- Gate log + naming: `.a0proj/agents/video-coordinator/` specifics
- Vault: `/a0/usr/obsidian/03-wgnr-sounds/10-music/velvut/`
