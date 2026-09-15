# PRD: WGNR Sounds Visual Production Layer — Local AI Video Pipeline & Agent Team

**Version:** 1.2.0 (final — PROJECT CANCELLED)
**Date:** 2026-09-06 (v1.0.0) · amended 2026-09-13 (v1.1.0 — video-project track re-bind, Principal liberty directive) · amended 2026-09-14 (v1.1.1 — video-grid tempo supersession, Principal ruling) · amended 2026-09-15 (v1.2.0 — PROJECT CANCELLED by Principal decision, see §13)
**Status:** CANCELLED (2026-09-15, Principal decision — assets archived, recoverable)
**Author:** wgnr-sounds-captain (orchestrator), from the Principal's Velvut video production brief (2026-09-06)
**Owners:** Wagner dos Santos (Principal, curator) · wgnr.ai SysOp (scaffold build) · WGNR Sounds label (operate)

## AI-Readable Block

- **Scope:** Defines a Visual Production Layer for the label — 3 new project agent profiles (`video-director`, `video-engineer`, `video-coordinator`) + 2 skills (`velvut-visual-constitution`, `comfyui-video-pipeline`) — and a localized, audio-reactive, budget-safe video generation pipeline running on the Principal's Mac Studio M2 Ultra via ComfyUI and open-weights video models (LTX-Video / HunyuanVideo) on Apple Silicon MPS. First deliverable: Velvut's first music video for "Is This How It Ends?" (Principal-declared 2026-09-13, video project; originally scoped as "Take Me Back"). Scaffold work is executed by SysOp per the companion dev-ticket.
- **Must-include elements:** (1) Velvut Visual Constitution (verbatim identity + visual rules from the Principal brief) as a protected, checkable spec; (2) Infrastructure Rule — cloud bypass, open-weights on MPS, Draft-First render gating (no hi-res cycle without low-res motion-vector preview + manual confirmation); (3) agent catalog with tiers/presets/parent departments; (4) 8-stage video production lifecycle; (5) open questions (video-project tempo AUTHORITATIVE 2026-09-14: "Is This How It Ends?" — 107 BPM, 4/4; supersedes the 2026-09-13 148 declaration and the 2026-09-06 "Take Me Back" @ 151); (6) claim labels (VERIFIED-FACT / SYNTHESIS-JUDGMENT / UNVERIFIED-CLAIM).
- **Must-not-compress lists:** Visual Constitution rules (lighting, fog, silhouette bounds, performance control); Infrastructure Rule (cloud bypass + draft-first gate); agent-to-department mapping.
- **Counter-prompt:** After summarizing, verify: (1) Are all Visual Constitution rules present verbatim? (2) Is the Draft-First gate stated as a hard prohibition, not a preference? (3) Are all 3 agents and 2 skills enumerated with tiers? (4) Is the BPM stated as 107 in 4/4 for "Is This How It Ends?" with its ruling source (Principal ruling 2026-09-14 — 148 marked historical)? (5) Are cloud video tools listed under out-of-scope?

## 1. TL;DR

Velvut needs its first music video — now "Is This How It Ends?" (video-project track re-bind, Principal-declared 2026-09-13; originally scoped as "Take Me Back", 2026-09-06) — and the label has no video-production capability. Cloud generation is ruled out — the Principal spent hundreds of dollars on Runway with no final result (Principal-reported, 2026-09-06). This PRD contracts a Visual Production Layer for the label: three new agent profiles and two skills that run a fully local, audio-reactive video pipeline on the Principal's Mac Studio M2 Ultra — ComfyUI (VERIFIED-FACT: running at `/Users/wgnr/AI/comfyui/`, process check 2026-09-06) driving open-weights video models (LTX-Video / HunyuanVideo) on Apple Silicon MPS, finished with ffmpeg. Every render cycle obeys a Draft-First gate: low-res motion-vector preview, manual Principal confirmation, then hi-res. The Velvut Visual Constitution (red-backlight-only, fog, crushed blacks, grain, zero-facial-detail silhouettes, BPM-matched movement) is protected in code logic and per-render checks. SysOp scaffolds the team per the companion dev-ticket; the label operates it.

## 2. Problem statement

- The 14-agent label roster has no video-production capability; the first Velvut music video is blocked on it.
- Cloud video tools burned budget without output (Principal-reported: "hundreds of dollars with no final result", Runway, 2026-09-06). VERIFIED-FACT (Principal statement) that cloud spend produced no deliverable; the label mandates a local pipeline to protect the budget.
- ComfyUI is already installed and running on the target hardware (VERIFIED-FACT), but no agent owns workflow engineering, render gating, or audio-reactive sync on it.
- Brand identity must be enforced across all local renders and code logic — today nothing checks a render against the Velvut visual rules.

## 3. Goals & non-goals

### Goals
1. Scaffold 3 project agents + 2 skills (SysOp build, label operate) forming a Visual Production Layer parallel to the Creative Production Layer (PRD-wgnr-sounds-label.md §13).
2. Local open-weights video generation on Apple Silicon MPS via ComfyUI; zero cloud video spend.
3. Audio-reactive pipeline synced to the track's BPM ("Is This How It Ends?" — 107 BPM, 4/4 — tempo superseded per Principal ruling 2026-09-14 — 148 marked historical; 107 BPM confirmed by canonical MIDI export (flat 107.0), stems curve (104.79–109.83, avg ≈107), and Principal authorization).
4. Draft-First gating as a hard rule: fast low-res motion-vector preview before any hi-res processing cycle; manual confirmation required.
5. Velvut Visual Constitution enforced in code logic and checked per render cycle.
6. First deliverable: Velvut "Is This How It Ends?" music video assets (track re-bind, Principal-declared 2026-09-13, video project).

### Non-goals (v1.0.0)
- Any cloud video-generation service (Runway et al.) — out of scope permanently unless the Principal reverses.
- Live-action filming/production crews.
- Changes to the audio pipeline (Suno/studio flow, PRD §5.4/§13) or DistroKid distribution flow.
- Agent Zero framework core changes (separate SysOp tickets).

## 4. Position in the label

A Visual Production Layer — NOT a new label department. It sits beside the Creative Production Layer (v3.0.0), consuming finished songs upstream and handing packaged video assets to Marketing & Promotion (campaign) and Distribution & Digital Strategy (platform specs) downstream. Multi-genre discipline preserved: the layer is artist-agnostic; the Visual Constitution is per-artist (Velvut first, encoded as a skill so future artists get their own constitution skills).

## 5. Velvut Visual Constitution (verbatim from Principal brief — protected)

**Sonic identity (for audio-reactive mapping):**
- Project track: "Is This How It Ends?" — **107 BPM, 4/4** (~560.7 ms/beat, ~2.2430 s/bar) — tempo superseded per Principal ruling 2026-09-14 — 148 marked historical; 107 BPM confirmed by canonical MIDI export (flat 107.0), stems curve (104.79–109.83, avg ≈107), and Principal authorization. House identity: nu-metal and alt-rock (Principal ruling 2026-09-12).
- Dynamics: heavy quiet-loud contrasts; verse = quiet introspective — low, deep baritone vocal over driving tom-tom beats; chorus = massive walls of distorted power chords and anthemic question hooks.
- (Re-bind note: previously pinned to "Take Me Back" @ 151 BPM, 2026-09-06; re-pinned 2026-09-13 under the Principal's liberty directive for the video project. All visual rules below are untouched.)

**Aesthetic:** Grounded cinematic live-action look, high-contrast underexposed, crushed deep blacks, film grain.

**Lighting:** A hot red backlight/strobe atmosphere is the ONLY illumination source. Environment filled with heavy, dense volumetric fog scattering the red light.

**Character bounds:** Musicians must be pure black silhouettes with ZERO facial detail (no visible eyes, mouth, or facial structure). They are read completely by posture, hair, and instrument shape.

**Performance control:** Movement sharp, hard-hitting, controlled, matched to BPM — NOT wild, cartoonish, or flailing. Guitarist plays through shoulder/arm stance with minimal head movement. No continuous headbanging.

**Baritone-vocalist consistency (existing Principal rule, 2026-08-31):** Velvut vocals = Wagner dos Santos, baritone male. Any lip-sync-adjacent or silhouette performance logic assumes the baritone frontman.

## 6. Infrastructure Rule (verbatim intent from Principal brief — protected)

- Cloud tools are bypassed to protect the budget. Use open-weights video models (such as LTX-Video or HunyuanVideo) running locally on Apple Silicon MPS hardware (Mac Studio M2 Ultra, Principal-declared).
- ComfyUI is the orchestration surface (VERIFIED-FACT: installed and running at `/Users/wgnr/AI/comfyui/`, process `server.py` observed 2026-09-06).
- **Draft-First check logic is mandatory on every execution path:** high-resolution processing cycles are FORBIDDEN until a fast, low-res preview of the motion vectors is delivered and manually confirmed by the Principal.
- Final assembly via ffmpeg (VERIFIED-FACT: present in the ops container `/usr/bin/ffmpeg`; Mac-side stitch flow already documented in the vault `Google Ideas.md`).
- Model choice (LTX-Video vs HunyuanVideo vs both) is UNVERIFIED-CLAIM until probed on-host for MPS compatibility and speed; probe is part of scaffold acceptance.

## 7. Agent catalog (Visual Production Layer)

| Slug | Title | Model tier | Preset | Parent dept (subfunction) |
|---|---|---|---|---|
| `video-director` | Video Director (Treatment & Vision) | judgment | Default Coding and Reasoning | Marketing & Promotion (visual-creative) |
| `video-engineer` | Video Engineer (ComfyUI Pipeline) | precision | Default Coding and Reasoning | Studio (video-engineering) |
| `video-coordinator` | Video Coordinator (Render Ops & Delivery) | execution | Fast Sub-Agent Inference | Operations / Label Management (render-ops) |

- **video-director** — central vision-holder per artist (Velvut first): treatment, storyboard, shot list, Visual Constitution enforcement at review gates, draft-preview judgment recommendations to the Principal.
- **video-engineer** — ComfyUI workflow graphs (text-to-video / image-to-video), open-weights model ops on MPS, Draft-First render ladder implementation, audio-reactive beat mapping, ffmpeg stitch + finishing chain (crushed blacks, grain).
- **video-coordinator** — render queue ops, asset naming + version tracking, gate logging (which drafts were confirmed, by whom, when), disk hygiene on the Mac Studio, delivery packaging per platform specs (YouTube 16:9, TikTok/Reels 9:16).

## 8. Skills (2)

- **`velvut-visual-constitution`** — the §5 rules as an executable per-render checklist: red-only illumination, fog density/scatter, crushed blacks + grain, zero-facial-detail silhouette check, posture/hair/instrument readability, BPM-matched movement bounds, no-headbanging rule, baritone frontman assumption. A render that fails any item is rejected before it reaches the Principal.
- **`comfyui-video-pipeline`** — the §6 runbook: MPS/ComfyUI ops, draft-first ladder (low-res motion-vector preview → Principal confirmation → hi-res), beat-map generation from the master track, ffmpeg stitch command, render-output hygiene.

## 9. Video production lifecycle

1. **Treatment** (`video-director`) — concept from song blueprint + Visual Constitution.
2. **Storyboard & shot list** (`video-director`) — per-shot prompts, silhouette strategy, fog/lighting notes.
3. **Draft renders** (`video-engineer`) — low-res motion-vector previews only.
4. **Principal gate** — manual confirmation per shot/sequence (Draft-First gate; mandatory).
5. **Hi-res renders** (`video-engineer`) — only confirmed shots; Constitution check on every output (`video-director` + skill).
6. **Audio-reactive sync & finishing** (`video-engineer`) — beat mapping to BPM, cut timing, ffmpeg stitch, color/grain finish.
7. **Versioned packaging** (`video-coordinator`) — platform-spec deliverables, asset log, gate log.
8. **Release** — handoff to Marketing & Promotion (campaign) and Distribution & Digital Strategy (platform delivery).

## 10. Open questions (Principal to resolve)

1. **Video-project track tempo** — RESOLVED 2026-09-14: **"Is This How It Ends?" — 107 BPM, 4/4** (~560.7 ms/beat, ~2.2430 s/bar) — tempo superseded per Principal ruling 2026-09-14 — 148 marked historical; 107 BPM confirmed by canonical MIDI export (flat 107.0), stems curve (104.79–109.83, avg ≈107), and Principal authorization. Onset verification against the master audio remains REQUIRED before render timing (validates the 107 grid + maps section boundaries; beatmap-generator.py gate). (Historical: 148 Principal-declared 2026-09-13 — superseded 2026-09-14; "Take Me Back" @ 151, 2026-09-06.)
2. **Deliverable shape** — full-track music video, vertical clip series (TikTok/Reels), or both; runtime targets per format.
3. **Render envelope on the Mac Studio** — acceptable session length / overnight batches; disk budget for drafts + finals.
4. **Model lock** — LTX-Video vs HunyuanVideo (or both): decide after the on-host MPS probe (UNVERIFIED-CLAIM until then).
5. **Silhouette source strategy** — prompt-driven silhouettes vs image-to-video from generated stills; recommendation due after probe.

## 11. Out of scope

Cloud video services; live-action production; audio/Suno pipeline changes; DistroKid changes; framework core edits; budget for external vendors.

## 12. References

- Principal video production brief (session 2026-09-06) — source of §5 and §6.
- `prds/PRD-wgnr-sounds-label.md` — §5.4 Suno role matrix, §13 Creative Production Layer pattern.
- Vault: `/a0/usr/obsidian/03-wgnr-sounds/10-music/velvut/promotions/Google Ideas.md` — rebrand rollout + ffmpeg stitch flow.
- Vault: `/a0/usr/obsidian/03-wgnr-sounds/10-music/velvut/lyrics/` — track lyrics (video-project track: "Is This How It Ends?"; lyric file on file per the vault songbook).
- ComfyUI: `/Users/wgnr/AI/comfyui/` (VERIFIED-FACT 2026-09-06).
- Companion SysOp ticket: `/a0/usr/projects/wgnr_ai_sysop/dev-tickets/dev-ticket-2026-09-06-wgnr-sounds-video-team-scaffold.md`.
- SysOp build PRD (SysOp-side build contract for this scaffold): `/a0/usr/projects/wgnr_ai_sysop/prds/PRD-wgnr-sounds-video-team-scaffold.md`. This label PRD remains the authoritative domain spec.

## 13. DOX closeout checklist

- [x] PRD filed in `prds/` per naming contract
- [x] `prds/AGENTS.md` Child DOX Index row added
- [x] SysOp scaffold dev-ticket filed
- [x] At scaffold time (SysOp): `.a0proj/agents/AGENTS.md` Visual Production Layer section + `agents.json` + Child DOX Index (done 2026-09-09; skills index + CHANGELOG updated)
- [x] At scaffold time: skills under `.a0proj/skills/` per §8 (done 2026-09-09; Draft-First gate GATE-1–GATE-6 + Constitution C1–C10 embedded as explicit gate steps)
- [x] MPS probe results appended (Open Question 4) — DONE 2026-09-09 00:38 ET via SysOp host-bridge probe: torch 2.11.0 MPS available=True; HunyuanVideo 1.5 720p t2v fp16 model PRESENT locally; LTX-Video ABSENT (download needed if chosen); custom_nodes lacks video helper nodes (install needed before first render). Model lock can now proceed on evidence; Draft-First gate governs first low-res preview.
- [x] v1.1.0 amendment (2026-09-13) — video-project track re-bind: "Is This How It Ends?" @ 148 BPM, 4/4 (Principal-declared 2026-09-13, video project; liberty directive) supersedes "Take Me Back" @ 151 (2026-09-06). Minimal substitution in §5 sonic identity — all verbatim visual rules untouched; §1 TL;DR, Goals #3/#6, §10 OQ1, §12 references updated; skills `velvut-visual-constitution` (§2 sonic identity, C9 parenthetical, §5 anchoring) + `comfyui-video-pipeline` (§5 constants, §7 naming tree) re-pinned to 148 / 405.4 ms / 1.6216 s. Onset verification elevated to REQUIRED gate (no prior documented tempo for the new track).
- [x] v1.1.1 amendment (2026-09-14) — video-grid tempo supersession: **107 BPM, 4/4** (~560.7 ms/beat, ~2.2430 s/bar) — tempo superseded per Principal ruling 2026-09-14 — 148 (declared 2026-09-13) marked historical; 107 confirmed by canonical MIDI export (flat 107.0) and stems curve (104.79–109.83, avg ≈107). §5 sonic identity, Goal #3, §10 OQ1, AI-Readable Block re-pinned — all verbatim visual rules untouched. beatmap.json already on the canonical 107 grid (369 beats / 93 bars); onset gate stays REQUIRED (validates the 107 grid + maps sections).
- [x] v1.2.0 amendment (2026-09-15) — **PROJECT CANCELLED** by Principal decision ("execute" on Option 1 of 3: end entirely; rationale: time-to-progress ratio). Terminal state: pipeline fully deployed + verified (4 node packs, HunyuanVideo 1.5 t2v, MIDI reader live); section map locked (8 Principal labels over the onset-verified grid); 4 draft iterations completed — v3 achieved the legibility breakthrough (identifiable guitarist figure; C1 100% red / 0% blue), v4 wide-framing rendered awaiting review at cancellation. GRID CORRECTION for the record: after v1.1.1 pinned 107 flat, full onset verification proved the song genuinely ACCELERATES 104.79→109.83 BPM — the authoritative render grid is the tempo curve, not any constant. Assets preserved & recoverable: `docs/video-pipeline/velvut/` complete tree (re-timed master.mid, labeled beatmap.json, conditioning packages, specs) + Mac drafts (`output/velvut/is-this-how-it-ends/sh-01/`, v1–v4 webp/mp4/stills). All Constitution rules, Draft-First gate law, and skills remain filed as durable reference for any future revival. Task `7d70ae55-a8fa-4e49-a250-7c72fd6829c5` = cancelled.
