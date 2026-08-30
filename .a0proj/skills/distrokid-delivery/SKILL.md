---
name: distrokid-delivery
description: The DistroKid-only DSP delivery pipeline for WGNR Sounds. Sole distributor since 2023. Covers master upload, metadata hygiene, release calendar coordination, and editorial pitching windows.. Applies to: Distribution & Digital Strategy, Operations / Label Management. Reference: PRD §7.3 (Distribution & Digital Strategy) + PRD §8.1 (Release Lifecycle Stage 4).
trigger_phrases:
  - "distrokid upload"
  - "dsp delivery"
  - "release calendar"
  - "metadata hygiene"
  - "isrc"
  - "pre-save"
---

# distrokid-delivery — Label-Specific Skill

> **Scope:** The DistroKid-only DSP delivery pipeline for WGNR Sounds. Sole distributor since 2023. Covers master upload, metadata hygiene, release calendar coordination, and editorial pitching windows.
> **Applies to:** Distribution & Digital Strategy, Operations / Label Management
> **Reference:** PRD §7.3 (Distribution & Digital Strategy) + PRD §8.1 (Release Lifecycle Stage 4)
> **Owner:** Wagner dos Santos (Principal) — WGNR Sounds Record Label

## Purpose

DistroKid is the **sole distributor for WGNR Sounds** since 2023 (per PRD §7.3). This skill is the canonical pipeline for master upload, metadata hygiene, release calendar coordination, and editorial pitching through DistroKid.

## Pipeline (canonical)

1. **Master upload** — Upload to DistroKid via the standard DistroKid UI or API (if API access is configured). Technical specs per DSP are enforced by DistroKid automatically.
2. **Metadata hygiene** — Ensure every release carries:
   - `ISRC` (International Standard Recording Code) — assigned per master
   - `ISWC` (International Standard Musical Work Code) — for the composition
   - `UPC` (Universal Product Code) — for the release
   - `songwriter splits` — explicit percentages; route to WGNR Sounds Music Publishing for ASCAP performance rights
   - `label copy` — `WGNR Sounds` (parent: wgnr.ai, division)
   - `master source tag` — `suno` for AI-generated (DJ Farra, Sobralenses); `studio` for human-recorded (Velvut, Wágner)
3. **Release calendar** — Confirm the release date with Operations / Label Management before scheduling. DistroKid supports scheduling ahead of release date.
4. **Editorial pitching windows** — Track each DSP's editorial pitching windows (Spotify, Apple Music, Tidal, Amazon, YouTube Music). Submit pitch materials via DistroKid where supported, or directly to DSPs where required.

## Mechanical Rights

Handled via DistroKid / MLC (Mechanical Licensing Collective) for US compulsory mechanical licensing. No separate mechanical registration by WGNR Sounds.

## Pre-save / Pre-add / Smart-links

DistroKid provides smart-link generation; use them for fan conversion mechanics. Coordinate with Marketing & Promotion for the campaign timeline.

## References

- PRD §7.3 (Distribution & Digital Strategy)
- PRD §8.1 (Release Lifecycle — Stage 4: Distribution delivers)
- Skill `suno-integration` (upstream — Suno role determines master source)
- Skill `rosters-and-catalog-reconciliation` (cross-reference — DSP roster vs. wgnrsounds.com vs. Suno)


*Skill created 2026-08-30 (v2.0.0). Mirrors the SKILL.md standard at `/a0/usr/projects/wgnr_ai_sysop/.a0proj/skills/dispatch-safety/SKILL.md`.*
