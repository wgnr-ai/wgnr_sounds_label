---
name: suno-integration
description: Per-artist Suno role mapping for WGNR Sounds. Identifies Suno role (100% AI vs. Suno-assist), routes master source (Suno vs. Studio), and ensures metadata tagging distinguishes AI-assisted from human-recorded content.. Applies to: A&R, Distribution & Digital Strategy, Legal & Business Affairs, Studio, Royalties & Finance. Reference: PRD §5.4 (Suno Integration by Artist).
trigger_phrases:
  - "suno role"
  - "ai generated"
  - "suno assist"
  - "human recorded"
  - "master source"
  - "ai pipeline"
---

# suno-integration — Label-Specific Skill

> **Scope:** Per-artist Suno role mapping for WGNR Sounds. Identifies Suno role (100% AI vs. Suno-assist), routes master source (Suno vs. Studio), and ensures metadata tagging distinguishes AI-assisted from human-recorded content.
> **Applies to:** A&R, Distribution & Digital Strategy, Legal & Business Affairs, Studio, Royalties & Finance
> **Reference:** PRD §5.4 (Suno Integration by Artist)
> **Owner:** Wagner dos Santos (Principal) — WGNR Sounds Record Label

## Purpose

The WGNR Sounds active roster splits between two pipelines. The per-artist Suno role determines the master source, the distribution flow, the contract template set, and the metadata tagging for rights administration. This skill enforces the per-artist Suno role mapping at every touchpoint.

## Canonical Matrix (PRD §5.4)

| Artist | Suno role | Master source | Distribution flow |
|---|---|---|---|
| **DJ Farra** | 100% AI-generated music AND lyrics | Suno (download from Suno) | Suno → DistroKid → DSPs |
| **Sobralenses** | 100% AI-generated music AND lyrics | Suno (download from Suno) | Suno → DistroKid → DSPs |
| **Velvut** | Suno-assist only (song-idea assistance) | Human recording (studio) | Studio → DistroKid → DSPs |
| **Wágner** | Suno-assist only (song-idea assistance) | Human recording (studio) | Studio → DistroKid → DSPs |

## Workflow

1. **Identify artist** — confirm artist name against the active roster (Wagner dos Santos 2026-08-30).
2. **Confirm Suno role** — look up the matrix above. Do not infer; the matrix is canonical.
3. **Match pipeline** — AI-pipeline artists route Suno → DistroKid. Human-recorded artists route Studio → DistroKid.
4. **Metadata tagging** — tag every release with `suno_role: <role>` and `master_source: <suno|studio>` for rights administration and reporting hand-off.
5. **Best practices** (Suno prompt-crafting for label release quality):
   - Match the label's multi-genre / eclectic discipline — Suno prompts should explore rather than narrow.
   - For 100% AI-generated releases (DJ Farra, Sobralenses): download the highest-quality WAV master; retain Suno's commercial license attestation per the 2026-08 Suno terms.
   - For Suno-assist (Velvut, Wágner): use Suno only for song-idea exploration; record the final master in studio.

## Implications for Departments (per PRD §5.4)

- **A&R** — include Suno-role declaration in every A&R brief.
- **Distribution & Digital Strategy** — masters arrive from two source types; metadata pipeline must distinguish them.
- **Legal & Business Affairs** — Suno-generated works carry Suno's licensing terms; human-recorded with Suno-assist carry standard recording-agreement terms. Contract template set differs by source.
- **Royalties & Finance** — publishing-side splits must account for Suno's role in AI-generated works (Suno's commercial license terms apply).

## References

- PRD §5.4 (Suno Integration by Artist) — canonical matrix
- PRD §7.1 (A&R — Suno-role declaration)
- PRD §7.3 (Distribution & Digital Strategy — per-artist Suno flow routing)
- PRD §7.5 (Legal & Business Affairs — Suno licensing terms)
- PRD §7.6 (Studio — active only for human-recorded pipeline)
- Skill `distrokid-delivery` (downstream — DSP delivery pipeline)


*Skill created 2026-08-30 (v2.0.0). Mirrors the SKILL.md standard at `/a0/usr/projects/wgnr_ai_sysop/.a0proj/skills/dispatch-safety/SKILL.md`.*
