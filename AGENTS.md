# WGNR Sounds Label

## Purpose

WGNR Sounds is a **division of wgnr.ai** (parent-child) — the virtual representation of a real-world independent record label owned by Wagner dos Santos. This project is the operational backbone for label functions, including creative signing (A&R), go-to-market (marketing, distribution, publicity), back-office (legal, royalties, Music Publishing sub-entity), the studio side (recording and engineering), artist relations, sync licensing, and overall label management. The canonical 10-department catalog lives in `prds/PRD-wgnr-sounds-label.md` §7. **WGNR Sounds Music Publishing** (ASCAP-registered) is documented as a sub-entity under §7.5 Legal & Business Affairs in the PRD.

## Project Identity

- **Display name:** WGNR Sounds Record Label
- **Directory name:** `wgnr_sounds_label`
- **Brand:** Division of wgnr.ai (parent-child relationship; until a dedicated WGNR Sounds brand guide ships, the **wgnr.ai brand guide is the active brand source** — see "Brand Identity" below and PRD §4 for the shared-until-dedicated rule).
- **Genre scope:** Multi-genre / eclectic. A&R is taste-maker rather than genre specialist. Departments are genre-agnostic.

## DOX Framework

This project follows the wgnr.ai Ops DOX framework. AGENTS.md files are binding work contracts. Read this file and every AGENTS.md on the path to any target before editing.

The canonical wOS behavioral standard lives at `/a0/usr/plugins/wgnr_ai_os/prompts/wos-spec.promptinclude.md`. v1 of this project does not yet wire wOS into `.a0proj/instructions/` — that activation is a v2 deliverable.

## Core Contract

- AGENTS.md files are binding work contracts for their subtrees.
- Departments are documented in the PRD as **functional domains**, NOT pre-built agent profiles. v1 stops at the PRD level.
- Brand identity references use the **wgnr.ai brand guide** as the active source for color and typography tokens, until a dedicated WGNR Sounds brand guide ships (shared-until-dedicated rule per PRD §4). The active brand guide path is exposed via `.a0proj/variables.env` as `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE`.
- WGNR Sounds-specific brand assets (logos, future dedicated brand guide) live at `docs/brand-assets/`, documented in the PRD's §4.1. Do not duplicate or relocate them.

## Read Before Editing

1. Read this AGENTS.md (project root).
2. Walk to the target path; read every AGENTS.md found.
3. Use the nearest AGENTS.md as the local contract and parent docs for repo-wide rules.

## Update After Editing

For v1, every meaningful change requires a DOX pass before the task is done. v1 has only the project root AGENTS.md plus child docs at `prds/` and `docs/`; update the relevant doc and refresh any Child DOX Index it carries.

## Hierarchy

- Root AGENTS.md — project purpose, identity, and top-level rules.
- `prds/AGENTS.md` — Product Requirements Documents (build contracts).
- `docs/AGENTS.md` — Human-facing documentation (governance, design notes — currently empty).

## Style

- Keep AGENTS.md files concise, current, and operational.
- Document stable contracts, not diary entries.
- Document the parent-child brand relationship (WGNR Sounds is a division of wgnr.ai; until a dedicated WGNR Sounds brand guide ships, the wgnr.ai brand guide is the active source per the shared-until-dedicated rule).

## Child DOX Index

| Path | Scope |
|---|---|
| `prds/AGENTS.md` | Product Requirements Documents — build contracts (v1: one PRD for label foundation) |
| `docs/AGENTS.md` | Human-facing docs hub (placeholder for v2) |

## Related Paths

- **PRD:** `prds/PRD-wgnr-sounds-label.md` — v1.2 label foundation PRD (canonical department catalog, operating model, release lifecycle, brand-guide sharing rule)
- **Brand assets (WGNR Sounds):** `docs/brand-assets/wgnr-sounds-logos/` — 4 PNG variants dropped by Wagner on 2026-08-30 (label `wsounds-logo1a.png` through `wsounds-logo3.png`).
- **Active brand guide (shared wgnr.ai):** `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-brand-guide.pdf` — active source for color and typography tokens until a dedicated WGNR Sounds guide ships. Exposed via `.a0proj/variables.env` as `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE`.
- **wgnr.ai parent-brand logos:** `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-logos/` — parent brand reference; usable on co-branded surfaces, NOT the WGNR Sounds label logo.
- **SysOp reference project:** `/a0/usr/projects/wgnr_ai_sysop/` — pattern reference for skeleton structure, DOX conventions, and project configuration.

## v1.2 Scope Boundary

This v1.2 deliverable is **PRD + project skeleton + brand asset scaffold + casing sweep + project.json v1.2 alignment ONLY**. v2 will add agent profiles, skills, and plugins. Do not scaffold agents/, skills/, or plugins/ at this stage.

## Brand Identity (Shared-Until-Dedicated Rule)

WGNR Sounds is a **division of wgnr.ai** (parent-child). Until WGNR Sounds ships its own dedicated brand guide:

1. The **wgnr.ai brand guide is the active source** for color and typography tokens (`#6EA8DB`, `#D4AF37`, `#5A6C8A`, `#2A2D32`). Use these tokens for label artifacts.
2. The **wgnr.ai brand guide path** is `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-brand-guide.pdf` (also exposed via `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE`).
3. The **WGNR Sounds logos** live in `docs/brand-assets/wgnr-sounds-logos/` (4 PNG variants) and are the primary mark for label-specific artifacts.
4. **When a dedicated WGNR Sounds brand guide ships**, drop it as `docs/brand-assets/wgnr-sounds-brand-guide.pdf` (replacing the `.gitkeep` placeholder), update `docs/brand-assets/README.md` and the PRD §4, and switch this rule to "WGNR Sounds brand guide is primary; wgnr.ai tokens are fallback."
5. **Co-branded surfaces** (e.g., a wgnr.ai dashboard that lists WGNR Sounds releases) use wgnr.ai tokens as primary, with the WGNR Sounds logo as a secondary mark.

This rule reverses the v1.1 'brand non-inheritance rule' (which incorrectly positioned wgnr.ai tokens as fallback-only). The v1.2 rule is: until a Sounds guide exists, wgnr.ai tokens ARE the active brand source. See PRD §4 for the full policy.
