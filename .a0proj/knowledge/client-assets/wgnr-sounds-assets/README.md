# WGNR Sounds Brand Assets

> **Status:** v1.1 scaffold — folders created, **files NOT yet dropped** by Wagner.
> **Owner:** Wagner dos Santos (Principal) is responsible for dropping the canonical brand files into this folder.
> **Last updated:** 2026-08-30

## Purpose

This folder holds the **canonical WGNR Sounds brand assets** — distinct from the wgnr.ai parent-brand assets that live at `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/`.

WGNR Sounds is a **division of WGNR** (parent-child). It inherits the wgnr.ai parent brand voice and uses its own WGNR Sounds visual identity.

## Folder structure

```
wgnr-sounds-assets/
├── README.md                              ← this file (handoff protocol)
├── wgnr-sounds-logos/                      ← logo PNG variants go here
│   └── .gitkeep
└── wgnr-sounds-brand-guide.pdf.gitkeep     ← rename to remove .gitkeep once PDF is dropped
```

## Handoff protocol (for Wagner)

1. **Drop logo PNG variants** into `wgnr-sounds-logos/`. Recommended variants:
   - transparent + opaque
   - light + dark
   - multiple sizes from 50px to 3000px
   - file naming: `wgnr-sounds-logo_<size>.png` or similar
2. **Drop the canonical brand guide PDF** into this folder, named `wgnr-sounds-brand-guide.pdf` (replace the `.gitkeep` placeholder).
3. **Update this README** to list the actual files dropped (so downstream agents have an authoritative inventory).

## Downstream reference

The PRD at `prds/PRD-wgnr-sounds-label.md` §4.1 references this folder as the canonical location. The root `AGENTS.md` directs all label artifact styling to this folder first (with wgnr.ai tokens as documented fallback only).

## Distinction from parent-brand assets

- **This folder** (`wgnr-sounds-assets/`) — WGNR Sounds brand. Sub-brand visuals. Use FIRST.
- **SysOp project** (`/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/`) — wgnr.ai parent brand. FALLBACK ONLY where the WGNR Sounds guide is silent.

Do NOT use the parent-brand assets as a substitute for WGNR Sounds assets. The two are different brands with different visual identities.
