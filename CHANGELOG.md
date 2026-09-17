# Changelog

All notable changes to the WGNR Sounds Record Label project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] — 2026-09-15

### Added
- Visual Production Layer scaffold complete (SysOp, 2026-09-09): 3 agent profiles (`video-director`, `video-engineer`, `video-coordinator`) under `.a0proj/agents/` + 2 skills (`velvut-visual-constitution`, `comfyui-video-pipeline`) under `.a0proj/skills/`; `agents.json` v4.0.0 (17 agents); `.a0proj/agents/AGENTS.md` Visual Production Layer section + Child DOX rows; skills index extended to 7. Draft-First gate (GATE-1–GATE-6) and Velvut Visual Constitution (C1–C10) embedded verbatim in skill logic. MPS compatibility probe DEFERRED — requires host-bridge session (see sysop dev-ticket note).
- `.a0proj/scripts/validate_agent_yamls.py` — standalone agent.yaml health check (stdlib+PyYAML; per-agent OK/FAIL, exit 1 on failure). Closes the guard deliverable of `dev-tickets/dev-ticket-2026-08-31-agent-yaml-parse-failures.md` alongside the framework-level warning + agents.json cross-check guards shipped in Agent Zero `helpers/subagents.py` (sysop dev-ticket-2026-09-06-agent-yaml-silent-drop-guard, break-tested 2026-09-06).
- `prds/PRD-wgnr-sounds-video-production.md` (v1.0.0 draft) — Visual Production Layer: 3 video agents (`video-director`, `video-engineer`, `video-coordinator`) + 2 skills; local ComfyUI / open-weights (LTX-Video, HunyuanVideo) pipeline on Mac Studio M2 Ultra MPS; Velvut Visual Constitution; Draft-First render gating; first deliverable Velvut "Take Me Back" music video. `prds/AGENTS.md` Child DOX Index extended.
- SysOp scaffold ticket: `wgnr_ai_sysop/dev-tickets/dev-ticket-2026-09-06-wgnr-sounds-video-team-scaffold.md` (P1). Cloud video generation (Runway) permanently out of scope per Principal (budget loss, no deliverable).
- SysOp framework ticket: `wgnr_ai_sysop/dev-tickets/dev-ticket-2026-09-06-agent-yaml-silent-drop-guard.md` (P2) — silent agent.yaml parse-drop guard; local originating ticket annotated with the cross-file.
- SysOp build PRD filed: `wgnr_ai_sysop/prds/PRD-wgnr-sounds-video-team-scaffold.md` (their template; SysOp index row added). Label PRD stays authoritative for domain spec. Both SysOp tickets restructured to full TEMPLATE.md shape (info table, assignee/related, Malfunction/Root cause for the guard).
- BPM resolved (Principal-declared): "Take Me Back" = 151 BPM, 4/4 (~397 ms/beat, ~1.588 s/bar) — applied across PRD (Goals, Sonic Identity, Open Question 1) and counter-prompt.

### Changed
- Bumped wOS conformance reference from v0.7 to v0.8 across 14 agent prompt files in `.a0proj/agents/`. Cross-project wOS propagation per sysop Task #2 — canonical wOS is v0.8 per `/a0/usr/plugins/wgnr_ai_os/prompts/wos-spec.promptinclude.md`.
- README consistency fix per Principal rulings (2026-09-15): roster AI-involvement taxonomy corrected (Wágner: no AI; Velvut: Suno ideation collaborator only, never generator), legal entity string corrected to WGNR, LLC — aligned with sysop global knowledge identity docs. Sweep extended: correction applied to all agent `_context.md` roster tables, `beg-catalog-metadata` SKILL.md, and the PRD §6.2 current-status line; suno-prompter workflow vocabulary (PRD §5.4 "Suno-assist" term, which now mismatches Wágner's no-AI status) intentionally left for a PRD §5.4 revision.
