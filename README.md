# WGNR Sounds Record Label

The operational backbone for **WGNR Sounds** — a real-world independent record label and **division of WGNR** (parent-child relationship, per the wgnrsounds.com tagline). This project is the virtual representation of a real-world music business owned by Wagner dos Santos.

## Status

**v1.1 — Corrected Foundation** (PRD + project skeleton + brand assets scaffold)

The v1.1 deliverable applies Wagner's primary-source corrections (2026-08-30) to v1: corrects the brand relationship from "peer-of-wgnr.ai" to **division of WGNR**, adds the active roster + historical BEG catalog, the per-artist Suno role matrix, DistroKid as the sole distributor since 2023, and **WGNR Sounds Music Publishing** as the ASCAP-registered sub-entity. v2 will scaffold agent profiles, skills, and plugins against the 10 departments defined in the PRD.

## Brand

WGNR Sounds is a **division of WGNR** (parent-child). It inherits the wgnr.ai parent brand voice and uses its own WGNR Sounds visual identity (logo + brand guide).

Canonical brand assets live in this project (scaffolded for Wagner's handoff):

- **Brand assets folder:** `.a0proj/knowledge/client-assets/wgnr-sounds-assets/` — contains `wgnr-sounds-logos/` and a brand-guide PDF placeholder, plus a README documenting the handoff protocol.
- The sysop project's `.a0proj/knowledge/client-assets/wgnr-assets/` directory holds wgnr.ai **parent-brand** assets (NOT the WGNR Sounds brand).

## Active roster

| Artist | Suno role | Pipeline |
|---|---|---|
| **Wágner** | Suno-assist only | Human-recorded → DistroKid → DSPs |
| **Velvut** | Suno-assist only | Human-recorded → DistroKid → DSPs |
| **DJ Farra** | 100% AI-generated | Suno → DistroKid → DSPs |
| **Sobralenses** | 100% AI-generated | Suno → DistroKid → DSPs |

The wgnrsounds.com website is out of date; the canonical roster is the union of the website + the Suno platform. A&R owns reconciliation in v2.

## Historical catalog

Beloved Entertainment Group (BEG, Nov 1995 – Jan 2002), NYC-based, 30+ album releases across four sub-imprints: Beloved Recordings (Compilations), Yum Recordings (Rock), Updego Entertainment (Dance / Electronic / Club), Beloved Soundtracks (Film / TV / Broadway). Strategic partnerships with Dinemec Records (Switzerland) and Crane Mountain Records (Boston). Legal status: fictitious name under WGNR, LLC.

## Contents

- `prds/PRD-wgnr-sounds-label.md` — the v1.1 build contract (start here)
- `prds/AGENTS.md` — DOX contract for the PRDs folder
- `docs/` — placeholder for v2 documentation (governance, design notes)
- `.a0proj/` — project configuration (project.json, agents.json, default_agent.json, variables.env, knowledge/)
- `.a0proj/knowledge/client-assets/wgnr-sounds-assets/` — WGNR Sounds brand assets scaffold

## What v1.1 is NOT

v1.1 does **not** include:

- Agent profiles for any department (deferred to v2)
- Skills or plugins (deferred to v2)
- Working simulation or sample catalog data
- Direct DSP integration code (DistroKid is the sole integration point)
- Royalty accounting automation
- Brand-asset content (folder scaffolded only; Wagner drops the files)

See the PRD's **Out of Scope (v1.1)** section for the full boundary.

## Conventions

- All brand references use the WGNR Sounds brand guide (local assets folder).
- Departments are **functional domains**, not pre-built agent profiles.
- Multi-genre / eclectic — departments are genre-agnostic.
- Brand assets location: `.a0proj/knowledge/client-assets/wgnr-sounds-assets/`.

## Reference

Pattern reference for project structure: the SysOp project at `/a0/usr/projects/wgnr_ai_sysop/`.
