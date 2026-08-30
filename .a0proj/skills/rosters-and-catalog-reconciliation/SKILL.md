---
name: rosters-and-catalog-reconciliation
description: Multi-surface roster sync. Reconciles wgnrsounds.com (out of date), suno.com/@wgnrsounds (active roster), DistroKid catalog metadata, and the internal label catalog. A&R canonical; union of all surfaces.. Applies to: A&R, Distribution & Digital Strategy, Operations / Label Management. Reference: PRD §6.3 (Roster reconciliation).
trigger_phrases:
  - "roster reconciliation"
  - "wgnrsounds.com out of date"
  - "suno profile"
  - "active roster"
  - "historical catalog"
---

# rosters-and-catalog-reconciliation — Label-Specific Skill

> **Scope:** Multi-surface roster sync. Reconciles wgnrsounds.com (out of date), suno.com/@wgnrsounds (active roster), DistroKid catalog metadata, and the internal label catalog. A&R canonical; union of all surfaces.
> **Applies to:** A&R, Distribution & Digital Strategy, Operations / Label Management
> **Reference:** PRD §6.3 (Roster reconciliation)
> **Owner:** Wagner dos Santos (Principal) — WGNR Sounds Record Label

## Purpose

The WGNR Sounds roster and catalog live across multiple surfaces, each with a different canonical authority and refresh cadence. **wgnrsounds.com is out of date** (per Wagner 2026-08-30); the canonical roster is the **union of all surfaces**. This skill enforces the reconciliation methodology.

## Surfaces

| Surface | Authoritative for | Refresh cadence |
|---|---|---|
| **wgnrsounds.com** (website) | Public-facing roster | Out of date; Marketing rebuild pending |
| **suno.com/@wgnrsounds** | AI-pipeline artist profiles (DJ Farra, Sobralenses) | As-released |
| **DistroKid catalog metadata** | DSP-delivered catalog | As-released |
| **Internal label catalog** (PRD §8 placeholder) | Internal release IDs, ISRC / ISWC / UPC tracking | Per-release |

## Reconciliation Methodology

1. **Union, not intersection** — if an artist or release appears on ANY surface, include it in the canonical reconciliation unless explicitly archived.
2. **A&R is canonical for active roster** — A&R owns the active roster (per PRD §7.1) and resolves conflicts.
3. **Distribution is canonical for DSP catalog** — Distribution owns the DistroKid metadata (per PRD §7.3) and resolves DSP-catalog conflicts.
4. **Surface deltas logged** — when a surface differs from the canonical, log the delta with timestamp and surface source. Reconcile weekly.

## Active Roster (PRD §6.1, canonical)

| Artist | Suno role | Pipeline |
|---|---|---|
| **Wágner** | Suno-assist only | Human-recorded → DistroKid → DSPs |
| **Velvut** | Suno-assist only | Human-recorded → DistroKid → DSPs |
| **DJ Farra** | 100% AI-generated | Suno → DistroKid → DSPs |
| **Sobralenses** | 100% AI-generated | Suno → DistroKid → DSPs |

## Historical Catalog (PRD §6.2, canonical)

See skill `beg-catalog-metadata` for the BEG catalog and sub-imprints (Beloved Recordings, Yum Recordings, Updego Entertainment, Beloved Soundtracks + Buzz Prophets + Nerve).

## Open Questions

- PRD §2 (Roster website update ownership — Marketing vs. A&R)
- PRD §3 (Suno profile ownership — Marketing vs. Distribution)
- PRD §4 (BEG catalog treatment on DSPs)
- PRD §8 (Catalog prefix — internal label catalog prefix TBD)

## References

- PRD §6.1 (Current active roster)
- PRD §6.2 (Historical back-catalog — BEG)
- PRD §6.3 (Roster reconciliation requirement)
- PRD §7.1 (A&R — owns canonical roster)
- PRD §7.3 (Distribution — owns DSP catalog)
- Skill `suno-integration` (cross-reference — per-artist Suno role for the active roster)
- Skill `beg-catalog-metadata` (cross-reference — BEG catalog scope)
- Skill `distrokid-delivery` (cross-reference — DistroKid metadata is a reconciliation surface)


*Skill created 2026-08-30 (v2.0.0). Mirrors the SKILL.md standard at `/a0/usr/projects/wgnr_ai_sysop/.a0proj/skills/dispatch-safety/SKILL.md`.*
