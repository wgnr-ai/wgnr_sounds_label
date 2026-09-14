# .a0proj/skills

## Purpose

Project-scoped skills for the WGNR Sounds Record Label project — the 7 label-specific skills that translate the PRD's per-artist Suno flow, DistroKid pipeline, BEG catalog archival, ASCAP Music Publishing, roster reconciliation, and the Visual Production Layer (Velvut Visual Constitution + local ComfyUI video pipeline) into executable workflows.

## Ownership

- **WGNR Sounds Record Label project** — managed by wgnr.ai agents
- **Principal:** Wagner dos Santos

## Skills Index (7 label-specific)

| Skill | Description | Applies to |
|---|---|---|
| `suno-integration` | Per-artist Suno role mapping for WGNR Sounds. Identifies Suno role (100% AI vs. Suno-assist), routes master source (Suno vs. Studio), and ensures metadata tagging distinguishes AI-assisted from human-recorded content. | A&R, Distribution & Digital Strategy, Legal & Business Affairs, Studio, Royalties & Finance |
| `distrokid-delivery` | The DistroKid-only DSP delivery pipeline for WGNR Sounds. Sole distributor since 2023. Covers master upload, metadata hygiene, release calendar coordination, and editorial pitching windows. | Distribution & Digital Strategy, Operations / Label Management |
| `beg-catalog-metadata` | Historical BEG (Beloved Entertainment Group) catalog archival. Documents 4 sub-imprints (Beloved Recordings, Yum Recordings, Updego Entertainment, Beloved Soundtracks), 30+ album releases from 1995-2002, and strategic partnerships with Dinemec Records and Crane Mountain Records. | Sync Licensing, A&R, Distribution & Digital Strategy (re-release scope, TBD) |
| `ascap-publishing` | WGNR Sounds Music Publishing is the ASCAP-registered publishing sub-entity that administers performance rights for the catalog. Documents writer registration, ASCAP statement processing, and the master-rights-vs-publishing-rights distinction. | Legal & Business Affairs, Royalties & Finance, Sync Licensing |
| `rosters-and-catalog-reconciliation` | Multi-surface roster sync. Reconciles wgnrsounds.com (out of date), suno.com/@wgnrsounds (active roster), DistroKid catalog metadata, and the internal label catalog. A&R canonical; union of all surfaces. | A&R, Distribution & Digital Strategy, Operations / Label Management |
| `velvut-visual-constitution` | Velvut Visual Constitution — protected per-render checklist (red-backlight-only illumination, heavy volumetric fog, crushed blacks + film grain, zero-facial-detail silhouettes, BPM-matched movement, no headbanging, baritone frontman). A render that fails any item is rejected before it reaches the Principal. Embeds the Draft-First gate verbatim (PRD §5/§6). | video-director, video-engineer (Visual Production Layer v4.0.0) |
| `comfyui-video-pipeline` | Local ComfyUI video-pipeline runbook — MPS/ComfyUI ops on Mac Studio M2 Ultra (`/Users/wgnr/AI/comfyui/`), Draft-First render ladder (low-res motion-vector preview → Principal confirmation → hi-res), beat-map generation (107 BPM, 4/4 — "Is This How It Ends?", tempo superseded per Principal ruling 2026-09-14; 148 historical), ffmpeg stitch + finishing, render-output hygiene. Open-weights models only; cloud video generation permanently out of scope. | video-engineer, video-coordinator, video-director (Visual Production Layer v4.0.0) |

## Conventions

- Each SKILL.md follows the standard at `/a0/usr/projects/wgnr_ai_sysop/.a0proj/skills/dispatch-safety/SKILL.md` (frontmatter + body + references).
- Skills are enabled per-agent via `plugins/_skills/config.json` (`label_skills_enabled` field) and listed in each agent's `agent.yaml` under `skills_enabled`.
- Skills do NOT replace the canonical PRD; they operationalize the PRD sections named in each skill's frontmatter `Reference` field.

## Child DOX Index

| Path | Scope |
|---|---|
| `.a0proj/skills/suno-integration/` | Per-artist Suno role mapping for WGNR Sounds. Identifies Suno role (100% AI vs. Suno-assist), routes master source (Suno vs. Studio), and ensures metadata tagging distinguishes AI-assisted from human-recorded content. |
| `.a0proj/skills/distrokid-delivery/` | The DistroKid-only DSP delivery pipeline for WGNR Sounds. Sole distributor since 2023. Covers master upload, metadata hygiene, release calendar coordination, and editorial pitching windows. |
| `.a0proj/skills/beg-catalog-metadata/` | Historical BEG (Beloved Entertainment Group) catalog archival. Documents 4 sub-imprints (Beloved Recordings, Yum Recordings, Updego Entertainment, Beloved Soundtracks), 30+ album releases from 1995-2002, and strategic partnerships with Dinemec Records and Crane Mountain Records. |
| `.a0proj/skills/ascap-publishing/` | WGNR Sounds Music Publishing is the ASCAP-registered publishing sub-entity that administers performance rights for the catalog. Documents writer registration, ASCAP statement processing, and the master-rights-vs-publishing-rights distinction. |
| `.a0proj/skills/rosters-and-catalog-reconciliation/` | Multi-surface roster sync. Reconciles wgnrsounds.com (out of date), suno.com/@wgnrsounds (active roster), DistroKid catalog metadata, and the internal label catalog. A&R canonical; union of all surfaces. |
| `.a0proj/skills/velvut-visual-constitution/` | Velvut Visual Constitution — protected per-render checklist (C1–C10): red-backlight-only illumination, volumetric fog, crushed blacks + film grain, zero-facial-detail silhouettes, posture/hair/instrument readability, BPM-matched movement bounds, no headbanging, baritone frontman. Draft-First gate embedded verbatim (PRD §5/§6). |
| `.a0proj/skills/comfyui-video-pipeline/` | Local ComfyUI video-pipeline runbook — MPS/ComfyUI ops, Draft-First render ladder (GATE-1–GATE-6), beat-map generation (107 BPM, 4/4 — "Is This How It Ends?", tempo superseded per Principal ruling 2026-09-14; 148 historical), ffmpeg stitch + finishing, render-output hygiene. Model lock stays UNVERIFIED-CLAIM until the MPS probe. |

## Verification

- `ls .a0proj/skills/` returns 7 directories (suno-integration, distrokid-delivery, beg-catalog-metadata, ascap-publishing, rosters-and-catalog-reconciliation, velvut-visual-constitution, comfyui-video-pipeline).
- Each SKILL.md has YAML frontmatter (name, description, trigger_phrases) and a body with Purpose, canonical matrix/pipeline, and References.
