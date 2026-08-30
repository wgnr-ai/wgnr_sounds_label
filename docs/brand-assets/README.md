# WGNR Sounds Brand Assets

> **Status:** v1.2 — Wagner dropped 4 logo PNGs on 2026-08-30. Brand-guide PDF still pending (placeholder sentinel retained).
> **Owner:** Wagner dos Santos (Principal) is the sole authority for label asset contents.
> **Last updated:** 2026-08-30

## Purpose

This folder holds the **canonical WGNR Sounds-specific brand assets** (logos, future brand-guide PDF, and any label-specific visual material).

WGNR Sounds is a **division of wgnr.ai** (parent-child). Until WGNR Sounds ships its own dedicated brand guide, the **wgnr.ai brand guide is the active brand source** for WGNR Sounds:

- Active brand guide: `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-brand-guide.pdf`
- Shared brand color tokens (active until Sounds guide ships): `#6EA8DB` (primary), `#D4AF37` (secondary), `#5A6C8A` (tertiary), `#2A2D32` (dark)
- See PRD §4 and the project-root `AGENTS.md` for the full shared-until-dedicated rule.

The wgnr.ai parent-brand logos at `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-logos/` are the parent brand reference and may be used on co-branded surfaces; for label-specific surfaces, use the WGNR Sounds logos in this subtree.

## Current inventory

- `wgnr-sounds-logos/wsounds-logo1a.png`
- `wgnr-sounds-logos/wsounds-logo1b.png`
- `wgnr-sounds-logos/wsounds-logo2a.png`
- `wgnr-sounds-logos/wsounds-logo3.png`
- `wgnr-sounds-brand-guide.pdf.gitkeep` (placeholder; active guide is the shared wgnr.ai one — see `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE` in `.a0proj/variables.env`)
- `AGENTS.md` (DOX contract for this subtree)

## Folder structure

```
docs/brand-assets/
├── README.md                              ← this file (handoff protocol + inventory)
├── AGENTS.md                              ← DOX contract for the brand-assets subtree
├── wgnr-sounds-logos/                      ← logo PNG variants
│   ├── wsounds-logo1a.png
│   ├── wsounds-logo1b.png
│   ├── wsounds-logo2a.png
│   └── wsounds-logo3.png
└── wgnr-sounds-brand-guide.pdf.gitkeep     ← sentinel; rename to drop .gitkeep when dedicated Sounds guide ships
```

## Handoff protocol (for Wagner)

1. **Drop logo PNG variants** into `wgnr-sounds-logos/`. Existing variants use `wsounds-logo<n><variant>.png`.
2. **Drop the dedicated brand guide PDF** when ready, replacing the `.gitkeep` sentinel: name it `wgnr-sounds-brand-guide.pdf` and delete the `.gitkeep`.
3. **Update this README** to reflect the new inventory before committing.
4. **Update the PRD §4** to mark the dedicated guide as authoritative (it supersedes the shared wgnr.ai guide for Sounds-specific visuals).

## Downstream reference

- The PRD at `prds/PRD-wgnr-sounds-label.md` §4.1 documents the active brand guide path and the shared-until-dedicated rule.
- The root `AGENTS.md` documents the brand boundary for label artifacts.
- The active brand guide PDF is exposed via `.a0proj/variables.env` as `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE`.
- The asset folder is exposed via `.a0proj/variables.env` as `WGNR_SOUNDS_BRAND_ASSETS_DIR`.

## Distinction from parent-brand assets

- **This folder** (`docs/brand-assets/`) — WGNR Sounds-specific brand (logos + future dedicated brand guide). Use FIRST for label surfaces.
- **SysOp project** (`/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-logos/` and `wgnr-brand-guide.pdf`) — wgnr.ai parent brand. The `wgnr-brand-guide.pdf` here is ALSO the active brand guide for WGNR Sounds until a Sounds-specific guide ships. The wgnr-logos/ folder is parent-brand only — not WGNR Sounds brand.

Until WGNR Sounds ships its dedicated brand guide, color and typography tokens come from the wgnr.ai parent brand guide (the file at the SysOp path above).
