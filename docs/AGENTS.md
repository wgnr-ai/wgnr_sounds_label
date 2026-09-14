# docs

## Purpose

Human-facing documentation hub for the WGNR Sounds Record Label project — governance, design notes, runbooks, and changelog. Currently empty at v1; v2 will populate as departments come online and operational patterns emerge.

## Ownership

- Owned by: WGNR Sounds Label project
- Authored by: wgnr.ai Ops (orchestrator)
- Curated by: Wagner dos Santos (Principal)

## Status

v1 shipped empty. As of 2026-09-13 the directory hosts its first operational tree: `video-pipeline/velvut/` — Velvut MIDI-driven audio-reactive ComfyUI pipeline artifacts (video-engineer). See the child AGENTS.md in that tree for its binding contracts (Draft-First gate, Visual Constitution C1–C10, fact-gated repo URLs).

## What will go here in v2

- **Brand governance** — rules for how WGNR Sounds brand assets are used in label artifacts (extends the PRD's shared-until-dedicated brand-guide rule documented in §4).
- **Department runbooks** — operational procedures per department once each domain is staffed.
- **Release operations playbooks** — the actual release lifecycle in practice (extends the PRD's release lifecycle workflow).
- **Royalty accounting procedures** — once the Royalty cadence is decided (PRD Open Question §7).
- **DSP / distribution partner docs** — DistroKid is the sole integration point per PRD §7.3 + §8.1; partner docs extend that.

## Local Contracts (placeholder)

- Naming: descriptive filenames in lowercase with hyphens (e.g., `brand-governance.md`, `runbook-dsp-uploads.md`).
- Cross-references between docs use relative paths from `/a0/usr/projects/wgnr_sounds_label/`.
- Long-form documents (5+ pages) follow the wgnr.ai Ops long-form-doc convention: numbered navigation table + AI-Readable Block at the top.
- Every change must remain consistent with the v1.2 PRD's brand boundary: until a dedicated WGNR Sounds brand guide ships, the **wgnr.ai brand guide is the active source** for color and typography tokens (shared-until-dedicated rule per PRD §4).

## Verification

- `ls docs/` lists the docs in this directory; this AGENTS.md child index matches.

## Child DOX Index

| Path | Scope |
|---|---|
| `video-pipeline/velvut/` | Velvut MIDI-driven audio-reactive ComfyUI pipeline artifacts + child AGENTS.md (added 2026-09-13) |
