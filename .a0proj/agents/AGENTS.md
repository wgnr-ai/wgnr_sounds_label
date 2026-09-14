# .a0proj/agents

## Purpose

Project-scoped agent profiles for the WGNR Sounds Record Label project — the 10 canonical label departments translated into v2.0.0 agent profiles. These agents extend the framework for the label's specific operational context (DistroKid, Suno role matrix, ASCAP Music Publishing, BEG catalog, wgnr.ai-shared brand guide).

## Ownership

- **WGNR Sounds Record Label project** — managed by wgnr.ai agents
- **Principal:** Wagner dos Santos (sole authority for label scope)
- **Parent company:** wgnr.ai (WGNR Sounds is a division, parent-child relationship)

## Disambiguation rule

- Profiles here are **project-scoped label-department specialists**. They do NOT collide with any A0-framework built-in profile.
- For wgnr.ai SysOp work, use the project-scoped variants in `/a0/usr/projects/wgnr_ai_sysop/.a0proj/agents/`. For WGNR Sounds label work, use the profiles here.
- These agents are dispatched via the project-agent surface, not the `call_subordinate` profile registry.

## Per-Artist Vocal Identity (Principal declaration, 2026-08-31)

- **Wágner** and **Velvut** vocalist: **Wagner dos Santos (Principal) — baritone male singer.**
- All creative work for **Wágner** or **Velvut** — blueprints, lyric perspective, Suno prompts, studio plans — MUST assume **baritone male vocals**, regardless of the vocalist/sex of any reference or inspiration track (a female-performed reference does NOT change this).
- Suno prompt sets for these two artists use male-vocal descriptors and exclude `female vocal` in the negative prompt (see `suno-prompt-compatibility-spec` §5–§6).
- **DJ Farra** and **Sobralenses** (100% AI-generated) are NOT bound by this rule; their vocal personas are chosen per project.

## Project Orchestrator (Captain)

| Slug | Title | Model tier | Preset |
|---|---|---|---|
| `wgnr-sounds-captain` | WGNR Sounds Captain (project orchestrator) | judgment | Default Coding and Reasoning |

The Captain auto-selects for new chats in this project via `.a0proj/default_agent.json` (`{"agent": "wgnr-sounds-captain"}`), per the canonical pattern at `/a0/usr/projects/wgnr_ai_sysop/docs/designs/2026-08-18-project-default-agent.md`. The Captain delegates execution to the 10 department agents and activates the 5 label-specific skills per PRD §7.

## Department Roster (10 canonical, per PRD §7)

| Slug | Title | Model tier | Preset |
|---|---|---|---|
| `ar` | A&R (Artist & Repertoire) | judgment | Default Coding and Reasoning |
| `marketing` | Marketing & Promotion | judgment | Default Coding and Reasoning |
| `distribution` | Distribution & Digital Strategy | execution | Fast Sub-Agent Inference |
| `publicity` | Publicity / PR | judgment | Default Coding and Reasoning |
| `legal` | Legal & Business Affairs | precision | Default Coding and Reasoning |
| `royalties` | Royalties & Finance | execution | Fast Sub-Agent Inference |
| `studio` | Studio (Recording & Engineering) | execution | Fast Sub-Agent Inference |
| `artist-relations` | Artist Relations | judgment | Default Coding and Reasoning |
| `sync` | Sync Licensing | execution | Fast Sub-Agent Inference |
| `operations` | Operations / Label Management | judgment | Default Coding and Reasoning |

## Creative Production Layer (v3.0.0)

| Slug | Title | Model tier | Preset | Parent dept (subfunction) |
|---|---|---|---|---|
| `song-architect` | Song Architect (Song Concept & Blueprint) | judgment | Default Coding and Reasoning | A&R (song-concept) |
| `lyricist` | Lyricist (Song Lyrics) | judgment | Default Coding and Reasoning | Studio (creative-writing) |
| `suno-prompter` | Suno Prompter (Suno Export) | judgment | Default Coding and Reasoning | Distribution & Digital Strategy (Suno export) |

The 3 creative agents are NOT label departments — they form a separate **Creative Production Layer** that operates upstream of the label's release pipeline. Workflow: `song-architect` (blueprint) → `lyricist` (lyrics) → `suno-prompter` (Suno-ready prompts). The `suno-prompt-compatibility-spec` skill is the canonical Suno format reference for `suno-prompter` (mandatory before emission). Cross-reference: PRD §13 (Creative Song-Production Layer, v3.0.0).

## Visual Production Layer (v4.0.0)

| Slug | Title | Model tier | Preset | Parent dept (subfunction) |
|---|---|---|---|---|
| `video-director` | Video Director (Treatment & Vision) | judgment | Default Coding and Reasoning | Marketing & Promotion (visual-creative) |
| `video-engineer` | Video Engineer (ComfyUI Pipeline) | precision | Default Coding and Reasoning | Studio (video-engineering) |
| `video-coordinator` | Video Coordinator (Render Ops & Delivery) | execution | Fast Sub-Agent Inference | Operations / Label Management (render-ops) |

The 3 video agents form a separate **Visual Production Layer** (NOT an 11th department), parallel to the Creative Production Layer. It consumes finished songs upstream and hands packaged video assets to Marketing & Promotion and Distribution & Digital Strategy downstream. Hard rules binding on all three: the **Draft-First gate** (hi-res render cycles FORBIDDEN until a low-res motion-vector preview is manually confirmed by the Principal), the **Velvut Visual Constitution** (per-artist, enforced via the `velvut-visual-constitution` skill), and the **cloud prohibition** (Runway et al. permanently out of scope — Principal direction 2026-09-06). Pipeline runbook: `comfyui-video-pipeline` skill (ComfyUI at `/Users/wgnr/AI/comfyui/`, open-weights models on Apple Silicon MPS, ffmpeg finishing). Cross-reference: `prds/PRD-wgnr-sounds-video-production.md` §4/§7 (Visual Production Layer, v4.0.0). First deliverable: Velvut "Is This How It Ends?" music video (107 BPM, 4/4 — tempo superseded per Principal ruling 2026-09-14; 148 historical).

## Child DOX Index

| Path | Scope |
|---|---|
| `.a0proj/agents/wgnr-sounds-captain/` | WGNR Sounds Captain — project orchestrator. Coordinates the 10 label departments and 5 label-specific skills per PRD §7. Auto-selected for new chats via `.a0proj/default_agent.json`. |
| `.a0proj/agents/ar/` | A&R (Artist & Repertoire) — Find, sign, and develop artists. The creative taste-making function of the label. |
| `.a0proj/agents/marketing/` | Marketing & Promotion — Build and execute the go-to-market plan for each release. Make listeners care. |
| `.a0proj/agents/distribution/` | Distribution & Digital Strategy — Get the music onto every relevant DSP on the right date with the right metadata. The sole integration point is DistroKid (in continuous use since 2023). |
| `.a0proj/agents/publicity/` | Publicity / PR — Earn media coverage and shape the public narrative around releases and artists. |
| `.a0proj/agents/legal/` | Legal & Business Affairs — Contracts, rights, licensing, dispute resolution. The legal backbone of the label. Documents and administers WGNR Sounds Music Publishing (ASCAP-registered). |
| `.a0proj/agents/royalties/` | Royalties & Finance — Money in, money out, money owed. Royalty accounting, statements, advances, recoupment. Future-state department — activates when volumes grow or a publishing-administration partnership is signed. |
| `.a0proj/agents/studio/` | Studio (Recording & Engineering) — Capture and finish the music — recording sessions, mixing, mastering. Active only for the human-recorded pipeline (Velvut + Wágner); AI-generated releases bypass Studio and source masters directly from Suno. |
| `.a0proj/agents/artist-relations/` | Artist Relations — Direct liaison with signed artists. Day-to-day relationship management. |
| `.a0proj/agents/sync/` | Sync Licensing — Place the label's catalog in film, TV, advertising, and video games. Adjacent-revenue engine. Aspirational — no active sync pitching today; activates if a publishing-administration partnership is signed. |
| `.a0proj/agents/operations/` | Operations / Label Management — The glue. Owns inter-department workflow, the release calendar, the budget envelope, and the reporting cadence. |
| `.a0proj/agents/song-architect/` | Song Architect — Creative Production Layer (v3.0.0). Develops the song idea — concept, structure, arrangement, genre/mood/tempo blueprint. Per-artist Suno role pre-check (PRD §5.4) is mandatory in every blueprint. Upstream of `lyricist` and `suno-prompter`. Department affiliation: A&R (song-concept subfunction). |
| `.a0proj/agents/lyricist/` | Lyricist — Creative Production Layer (v3.0.0). Writes finished song lyrics as a complete deliverable for the WGNR Sounds roster. Multi-genre fluency; structural awareness (verse/pre-chorus/chorus/hook/bridge/outro); metadata header. Department affiliation: Studio (creative-writing subfunction). |
| `.a0proj/agents/suno-prompter/` | Suno Prompter — Creative Production Layer (v3.0.0). Translates the song blueprint + finished lyrics into verified Suno-compatible prompts. Per-artist Suno role (PRD §5.4) determines 100% AI vs Suno-assist prompt structure. Skill: `suno-prompt-compatibility-spec` is mandatory before emission. Department affiliation: Distribution & Digital Strategy (Suno export subfunction). |
| `.a0proj/agents/video-director/` | Video Director — Visual Production Layer (v4.0.0). Central vision-holder per artist (Velvut first): treatment, storyboard, shot list, Constitution enforcement at review gates, draft-preview judgment recommendations to the Principal. Department affiliation: Marketing & Promotion (visual-creative subfunction). Skills: `velvut-visual-constitution`, `comfyui-video-pipeline`. |
| `.a0proj/agents/video-engineer/` | Video Engineer — Visual Production Layer (v4.0.0). ComfyUI workflow graphs, open-weights model ops on Apple Silicon MPS, Draft-First render ladder implementation, audio-reactive beat mapping (107 BPM, 4/4 — "Is This How It Ends?", tempo superseded per Principal ruling 2026-09-14; 148 historical), ffmpeg stitch + finishing. Department affiliation: Studio (video-engineering subfunction). Skills: `velvut-visual-constitution`, `comfyui-video-pipeline`. |
| `.a0proj/agents/video-coordinator/` | Video Coordinator — Visual Production Layer (v4.0.0). Render-queue ops, asset naming + version tracking, Draft-First gate logging, disk hygiene, delivery packaging per platform specs (YouTube 16:9, TikTok/Reels 9:16). Department affiliation: Operations / Label Management (render-ops subfunction). Skill: `comfyui-video-pipeline`. |

## Conventions

- The wgnr-sounds-captain profile mirrors the structure at `/a0/usr/projects/wgnr_ai_sysop/.a0proj/agents/sysop-captain/` (agent.yaml + prompts/agent.system.main.specifics.md + plugins/_model_config/ + assets/avatar.webp). Department agent profiles mirror the structure at `/a0/usr/projects/wgnr_ai_sysop/.a0proj/agents/wgnr-project-dev/` (agent.yaml + _context.md + prompts/ + plugins/).
- Model preset is canonical from `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/model_presets_v1.csv`. See each agent's `_context.md` for tier rationale and any deviation notes.
- All agents inherit the WGNR Sounds brand rule (shared-until-dedicated), the DistroKid sole-distributor contract, and the multi-genre / eclectic discipline.

## Verification

- `ls .a0proj/agents/` returns 17 directories (10 departments + wgnr-sounds-captain + 3 Creative Production Layer + 3 Visual Production Layer).
- Each directory contains `agent.yaml`, `_context.md`, `prompts/agent.system.main.role.md`, `plugins/_model_config/config.json`, `plugins/_tool_access/config.json`, `plugins/_skills/config.json` (captain also carries `assets/`).
- `.a0proj/agents.json` registers all 17 with slug + title + model_tier + profile_type.
- `.a0proj/scripts/validate_agent_yamls.py` exits 0 (all agent.yaml parse).
