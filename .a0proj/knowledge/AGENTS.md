# Knowledge Subtree — WGNR Sounds Label

## Purpose

This subtree holds reference materials, model specs, brand assets, and project-context documents for the WGNR Sounds Record Label project. It is the local knowledge base; the sysop project's knowledge subtree is a separate, sibling resource.

## Ownership

- Owned by: WGNR Sounds Label project
- Authored by: wgnr.ai Ops (orchestrator)
- Curated by: Wagner dos Santos (Principal)

## Local Contracts

- Knowledge files live under `.a0proj/knowledge/` only.
- Knowledge files are **referenced** by other project artifacts; do not duplicate content.
- Do not commit knowledge files containing secrets, API keys, or private deployment details.
- Brand assets live under `client-assets/wgnr-sounds-assets/` (local WGNR Sounds brand) — NOT under the sysop project's `client-assets/wgnr-assets/` (wgnr.ai parent brand).

## Work Guidance

- New knowledge files go in their appropriate subfolder (`client-assets/`, `main/`, `fragments/`, etc.).
- When dropping brand files, follow the handoff protocol in `client-assets/wgnr-sounds-assets/README.md`.
- Keep references absolute (paths starting from `/a0/usr/projects/wgnr_sounds_label/...`).

## Verification

- `ls -R .a0proj/knowledge/` shows the current state.
- Each subfolder (if present) has an `AGENTS.md` documenting its purpose.

## Child DOX Index

| Path | Scope |
|---|---|
| `client-assets/wgnr-sounds-assets/` | WGNR Sounds canonical brand files (scaffolded for Wagner's handoff) |
