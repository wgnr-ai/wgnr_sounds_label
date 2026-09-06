# Changelog

All notable changes to the WGNR Sounds Record Label project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased] — 2026-09-06

### Added
- `prds/PRD-wgnr-sounds-video-production.md` (v1.0.0 draft) — Visual Production Layer: 3 video agents (`video-director`, `video-engineer`, `video-coordinator`) + 2 skills; local ComfyUI / open-weights (LTX-Video, HunyuanVideo) pipeline on Mac Studio M2 Ultra MPS; Velvut Visual Constitution; Draft-First render gating; first deliverable Velvut "Take Me Back" music video. `prds/AGENTS.md` Child DOX Index extended.
- SysOp scaffold ticket: `wgnr_ai_sysop/dev-tickets/dev-ticket-2026-09-06-wgnr-sounds-video-team-scaffold.md` (P1). Cloud video generation (Runway) permanently out of scope per Principal (budget loss, no deliverable).
- SysOp framework ticket: `wgnr_ai_sysop/dev-tickets/dev-ticket-2026-09-06-agent-yaml-silent-drop-guard.md` (P2) — silent agent.yaml parse-drop guard; local originating ticket annotated with the cross-file.
- SysOp build PRD filed: `wgnr_ai_sysop/prds/PRD-wgnr-sounds-video-team-scaffold.md` (their template; SysOp index row added). Label PRD stays authoritative for domain spec. Both SysOp tickets restructured to full TEMPLATE.md shape (info table, assignee/related, Malfunction/Root cause for the guard).
- BPM resolved (Principal-declared): "Take Me Back" = 151 BPM, 4/4 (~397 ms/beat, ~1.588 s/bar) — applied across PRD (Goals, Sonic Identity, Open Question 1) and counter-prompt.

### Changed
- Bumped wOS conformance reference from v0.7 to v0.8 across 14 agent prompt files in `.a0proj/agents/`. Cross-project wOS propagation per sysop Task #2 — canonical wOS is v0.8 per `/a0/usr/plugins/wgnr_ai_os/prompts/wos-spec.promptinclude.md`.
