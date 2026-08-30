# WGNR Sounds Record Label

The operational backbone for **WGNR Sounds** — a real-world independent record label and **division of wgnr.ai** (parent-child relationship, per the wgnrsounds.com tagline). This project is the virtual representation of a real-world music business owned by Wagner dos Santos.

## Status

**v1.2 — Corrected Foundation** (PRD + project skeleton + brand assets scaffold + casing sweep + project.json alignment)

v1.2 applies Wagner's v1.2 corrections (2026-08-30) to v1.1: documents the **shared-until-dedicated brand guide rule** (wgnr.ai brand guide is the active source until WGNR Sounds ships its own guide), refreshes the brand-asset path to `docs/brand-assets/` (Wagner dropped 4 logos on 2026-08-30), corrects ~30 casing violations (`division of WGNR` → `division of wgnr.ai`, `WGNR, LLC` → `wgnr.ai, LLC`), and rewrites the v1-stale `project.json` instructions field. v1.1's deliverable scope is preserved (division-of-wgnr.ai framing, 10 departments, per-artist Suno matrix, DistroKid, BEG catalog, WGNR Sounds Music Publishing sub-entity). v2 will scaffold agent profiles, skills, and plugins against the 10 departments.

## Brand

WGNR Sounds is a **division of wgnr.ai** (parent-child). It inherits the wgnr.ai parent brand voice and uses its own WGNR Sounds visual identity (logos at `docs/brand-assets/wgnr-sounds-logos/`).

**Shared-until-dedicated brand guide rule (NEW in v1.2):** Until WGNR Sounds ships its own dedicated brand guide, the **wgnr.ai brand guide is the active brand source** for color and typography tokens. Active path: `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-brand-guide.pdf` (also exposed via `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE` in `.a0proj/variables.env`).

Canonical brand assets live in this project:

- **Brand assets folder:** `docs/brand-assets/` — contains `wgnr-sounds-logos/` (4 PNG variants dropped by Wagner on 2026-08-30), a brand-guide PDF placeholder (`.gitkeep` sentinel), and a README documenting the handoff protocol.
- The sysop project's `.a0proj/knowledge/client-assets/wgnr-assets/` directory holds wgnr.ai **parent-brand** assets (logos + the brand guide PDF that doubles as the active Sounds guide until a Sounds-specific guide ships).

## Active roster

| Artist | Suno role | Pipeline |
|---|---|---|
| **Wágner** | Suno-assist only | Human-recorded → DistroKid → DSPs |
| **Velvut** | Suno-assist only | Human-recorded → DistroKid → DSPs |
| **DJ Farra** | 100% AI-generated | Suno → DistroKid → DSPs |
| **Sobralenses** | 100% AI-generated | Suno → DistroKid → DSPs |

The wgnrsounds.com website is out of date; the canonical roster is the union of the website + the Suno platform. A&R owns reconciliation in v2.

## Historical catalog

Beloved Entertainment Group (BEG, Nov 1995 – Jan 2002), NYC-based, 30+ album releases across four sub-imprints: Beloved Recordings (Compilations), Yum Recordings (Rock), Updego Entertainment (Dance / Electronic / Club), Beloved Soundtracks (Film / TV / Broadway). Strategic partnerships with Dinemec Records (Switzerland) and Crane Mountain Records (Boston). Legal status: fictitious name under wgnr.ai, LLC.

## Contents

- `prds/PRD-wgnr-sounds-label.md` — the v1.2 build contract (start here)
- `prds/AGENTS.md` — DOX contract for the PRDs folder
- `docs/` — placeholder for v2 documentation (governance, design notes)
- `.a0proj/` — project configuration (project.json, agents.json, default_agent.json, variables.env, knowledge/)
- `docs/brand-assets/` — WGNR Sounds brand assets (4 logos dropped by Wagner on 2026-08-30 + brand-guide PDF placeholder)

## What v1.2 is NOT

v1.2 does **not** include:

- Agent profiles for any department (deferred to v2)
- Skills or plugins (deferred to v2)
- Working simulation or sample catalog data
- Direct DSP integration code (DistroKid is the sole integration point)
- Royalty accounting automation
- A dedicated WGNR Sounds brand guide PDF (the shared wgnr.ai brand guide is the active source per the shared-until-dedicated rule; dedicated guide ships later)

See the PRD's **Out of Scope (v1.2)** section for the full boundary.

## Conventions

- Brand references use the **wgnr.ai brand guide** as the active source for color and typography tokens until a dedicated WGNR Sounds guide ships (shared-until-dedicated rule per PRD §4).
- Departments are **functional domains**, not pre-built agent profiles.
- Multi-genre / eclectic — departments are genre-agnostic.
- Brand assets location: `docs/brand-assets/` (WGNR Sounds logos + future dedicated brand guide).

## Reference

Pattern reference for project structure: the SysOp project at `/a0/usr/projects/wgnr_ai_sysop/`.
