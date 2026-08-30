# WGNR Sounds Label

## Purpose

WGNR Sounds is a **division of WGNR** (parent-child) — the virtual representation of a real-world independent record label owned by Wagner dos Santos. This project is the operational backbone for label functions, including creative signing (A&R), go-to-market (marketing, distribution, publicity), back-office (legal, royalties, Music Publishing sub-entity), the studio side (recording and engineering), artist relations, sync licensing, and overall label management. The canonical 10-department catalog lives in `prds/PRD-wgnr-sounds-label.md` §7. **WGNR Sounds Music Publishing** (ASCAP-registered) is documented as a sub-entity under §7.5 Legal & Business Affairs in the PRD.

## Project Identity

- **Display name:** WGNR Sounds Record Label
- **Directory name:** `wgnr_sounds_label`
- **Brand:** Division of WGNR (parent-child relationship; WGNR Sounds inherits the wgnr.ai parent brand voice and uses its own WGNR Sounds visual identity via the local brand guide, NOT wgnr.ai color tokens as the primary source).
- **Genre scope:** Multi-genre / eclectic. A&R is taste-maker rather than genre specialist. Departments are genre-agnostic.

## DOX Framework

This project follows the wgnr.ai Ops DOX framework. AGENTS.md files are binding work contracts. Read this file and every AGENTS.md on the path to any target before editing.

The canonical wOS behavioral standard lives at `/a0/usr/plugins/wgnr_ai_os/prompts/wos-spec.promptinclude.md`. v1 of this project does not yet wire wOS into `.a0proj/instructions/` — that activation is a v2 deliverable.

## Core Contract

- AGENTS.md files are binding work contracts for their subtrees.
- Departments are documented in the PRD as **functional domains**, NOT pre-built agent profiles. v1 stops at the PRD level.
- All brand identity references use the WGNR Sounds brand guide (parent-child inheritance from wgnr.ai brand voice). Do NOT use wgnr.ai color tokens as the primary source for WGNR Sounds artifacts.
- The brand assets live at the canonical local path `.a0proj/knowledge/client-assets/wgnr-sounds-assets/` documented in the PRD's §4.1. Do not duplicate or relocate them.

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
- Document the parent-child brand relationship with wgnr.ai (WGNR Sounds is a division of WGNR).

## Child DOX Index

| Path | Scope |
|---|---|
| `prds/AGENTS.md` | Product Requirements Documents — build contracts (v1: one PRD for label foundation) |
| `docs/AGENTS.md` | Human-facing docs hub (placeholder for v2) |

## Related Paths

- **PRD:** `prds/PRD-wgnr-sounds-label.md` — v1 label foundation PRD (canonical department catalog, operating model, release lifecycle)
- **Brand assets (WGNR Sounds):** `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-logos/` (PNG variants) and `wgnr-brand-guide.pdf` (canonical brand guide). These live in the SysOp project's knowledge subtree — reference them from the PRD; do NOT copy or relocate.
- **SysOp reference project:** `/a0/usr/projects/wgnr_ai_sysop/` — pattern reference for skeleton structure, DOX conventions, and project configuration.

## v1.1 Scope Boundary

This v1.1 deliverable is **PRD + project skeleton + brand assets scaffold ONLY**. v2 will add agent profiles, skills, and plugins. Do not scaffold agents/, skills/, or plugins/ at this stage.

## Brand Non-Inheritance Rule

WGNR Sounds is a **division of WGNR** (parent-child). Use the WGNR Sounds brand guide (at `.a0proj/knowledge/client-assets/wgnr-sounds-assets/`) as the primary source for label visuals. Where the WGNR Sounds brand guide is silent, fall back to wgnr.ai tokens. If a future UI must coexist with wgnr.ai surfaces, use an explicit brand-adapter layer (NOT direct token inheritance).

**Do NOT** use wgnr.ai color palette (#6EA8DB / #D4AF37 / #5A6C8A) anywhere as the primary source — defer to the WGNR Sounds brand guide once Wagner drops the assets. The wgnr.ai parent-brand assets (currently in the sysop project) are correctly referenced as parent-brand fallback only, NOT as WGNR Sounds brand assets.

Use only the WGNR Sounds brand guide referenced above.
