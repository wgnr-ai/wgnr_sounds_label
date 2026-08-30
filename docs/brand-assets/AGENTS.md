# docs/brand-assets

## Purpose

Canonical home for **WGNR Sounds-specific brand assets** — logos, brand guide placeholder, and any label-specific visual material. This subtree is the local source of truth for WGNR Sounds visual identity until a dedicated WGNR Sounds brand guide ships.

**Cross-reference to active brand guide:** Until WGNR Sounds has its own dedicated brand guide, the **wgnr.ai brand guide** is the active brand source for WGNR Sounds:

- Active brand guide: `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-brand-guide.pdf`
- Shared brand color tokens (active until Sounds guide ships): `#6EA8DB` (primary), `#D4AF37` (secondary), `#5A6C8A` (tertiary), `#2A2D32` (dark)
- This shared-until-dedicated rule is documented at the project root in `AGENTS.md` and in the PRD §4.

## Ownership

- **Owned by:** WGNR Sounds Record Label project
- **Files dropped by:** Wagner dos Santos (Principal) — sole authority for label asset contents
- **Read by:** any wgnr.ai Ops agent or human producing WGNR Sounds label artifacts (logos, marketing collateral, release assets)

## Local Contracts

- **Drop rule:** Only Wagner adds files to this subtree. Agents reference assets here by absolute path via `.a0proj/variables.env` (`WGNR_SOUNDS_BRAND_ASSETS_DIR` for the folder; `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE` for the shared brand guide PDF).
- **Naming:** lowercase-kebab-case file names where possible. Logo variants use the `wsounds-logo<n><variant>.png` convention (e.g., `wsounds-logo1a.png`, `wsounds-logo1b.png`).
- **Placeholder handling:** the file `wgnr-sounds-brand-guide.pdf.gitkeep` is a sentinel — when the dedicated WGNR Sounds brand guide ships, drop it as `wgnr-sounds-brand-guide.pdf` and delete the `.gitkeep`. Do not delete the placeholder until the real PDF is dropped.
- **Read-only reference for agents:** agents do not modify, rename, or delete files in this subtree. They read by absolute path.
- **Update README on drop:** when Wagner adds or removes files, update `docs/brand-assets/README.md` to reflect the new inventory before the change is committed.

## Active Asset Inventory (v1.2 — 2026-08-30)

- `wgnr-sounds-logos/` — 4 PNG variants dropped by Wagner (label `wsounds-logo1a.png` through `wsounds-logo3.png`)
- `wgnr-sounds-brand-guide.pdf.gitkeep` — placeholder; the active brand guide today is the shared wgnr.ai one (path above)
- `README.md` — handoff protocol and inventory list

## Work Guidance

- Use the active shared brand guide for color and typography tokens until a dedicated WGNR Sounds guide ships.
- When the dedicated guide ships: replace `.gitkeep` with the real PDF, update `README.md`, and update the PRD §4 to mark the dedicated guide as authoritative.
- Cross-referencing the wgnr.ai parent-brand assets (logos in `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-logos/`) is allowed only for co-branded surfaces where the parent brand is also represented; for label-specific surfaces, use the WGNR Sounds logos in this subtree.

## Verification

- `ls docs/brand-assets/wgnr-sounds-logos/` returns the 4 PNG files dropped by Wagner.
- `ls docs/brand-assets/wgnr-sounds-brand-guide.pdf.gitkeep` returns the placeholder sentinel.
- The active brand guide is reachable at the path in `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE` (defined in `.a0proj/variables.env`).

## Child DOX Index

| Path | Scope |
|---|---|
| `wgnr-sounds-logos/` | WGNR Sounds logo PNG variants (4 files dropped 2026-08-30) |
| `wgnr-sounds-brand-guide.pdf.gitkeep` | Sentinel placeholder for the future dedicated WGNR Sounds brand guide PDF |
| `README.md` | Handoff protocol + inventory list |
