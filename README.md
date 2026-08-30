# WGNR Sounds Record Label

The operational backbone for **WGNR Sounds** — an independent record label. This project is the virtual representation of a real-world music business.

## Status

**v1 — Foundation** (PRD + project skeleton only)

The v1 deliverable is a single PRD that catalogs the canonical label departments and operating model. v2 will scaffold agent profiles, skills, and plugins against the departments defined here.

## Brand

WGNR Sounds is an **independent sister entity** to wgnr.ai. It uses its own logo and brand guide; it does **not** inherit wgnr.ai brand colors or tokens.

Canonical brand assets live in the SysOp project knowledge base:

- **Logo (PNG variants):** `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-logos/`
- **Brand guide (PDF):** `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-brand-guide.pdf`

## Contents

- `prds/PRD-wgnr-sounds-label.md` — the v1 build contract (start here)
- `prds/AGENTS.md` — DOX contract for the PRDs folder
- `docs/` — placeholder for v2 documentation (governance, design notes)
- `.a0proj/` — project configuration (project.json, agents.json, default_agent.json, variables.env)

## What v1 is NOT

v1 does **not** include:

- Agent profiles for any department (deferred to v2)
- Skills or plugins (deferred to v2)
- Working simulation or sample catalog data
- Distribution partner integrations
- Royalty accounting automation

See the PRD's **Out of Scope (v1)** section for the full boundary.

## Conventions

- All brand references must use the WGNR Sounds brand guide.
- Departments are **functional domains**, not pre-built agent profiles.
- Multi-genre / eclectic — departments are genre-agnostic.

## Reference

Pattern reference for project structure: the SysOp project at `/a0/usr/projects/wgnr_ai_sysop/`.
