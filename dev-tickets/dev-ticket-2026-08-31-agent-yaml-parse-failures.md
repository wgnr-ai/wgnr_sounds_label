---
title: Four project agents silently dropped from callable profile list (agent.yaml parse failures)
status: open
priority: P2
created: 2026-08-31
---

## Summary

Four WGNR Sounds project agents (`royalties`, `sync`, `lyricist`, `suno-prompter`) were silently absent from the `call_subordinate` callable profile list because their `agent.yaml` files failed YAML parsing. The framework's discovery helper (`helpers/subagents.py`) skips unparseable agent definitions **without any warning**, hiding the failure. Data fix applied and verified 2026-08-31; the open work is a framework-level guard so silent agent drops can never recur unnoticed.

## Context

- **Symptom (2026-08-31, chat TuHvZw0D):** `call_subordinate` with `profile="lyricist"` raised `RepairableException: Agent profile 'lyricist' not found` — despite `lyricist` being registered in `.a0proj/agents.json` (v3.0.0, 14 agents) with a complete file set (agent.yaml + _context.md + prompts/ + plugins/).
- **Scope discovered on diagnosis:** FOUR agents affected, not one — `royalties`, `sync`, `lyricist`, `suno-prompter` all absent from `get_available_agents_dict()`. Went unnoticed since scaffold day 2026-08-30 because nothing surfaces the drop.
- **Root cause (framework-runtime probe, `subagents._read_agent_definition`):**
  - `royalties/agent.yaml` line 3 — unquoted colon in `description` (`v2+ trigger: volumes grow`) → `yaml.scanner.ScannerError`
  - `sync/agent.yaml` line 3 — unquoted colon in `description` (`Catalog assets: active roster`) → `yaml.scanner.ScannerError`
  - `suno-prompter/agent.yaml` line 11 — unquoted colon in `context` (`Skill: suno-prompt-compatibility-spec`) → `yaml.scanner.ScannerError`
  - `lyricist/agent.yaml` line 30 — `- mcp:lusha_mcp:*` indented 1 space instead of 2, breaking the block sequence → `yaml.parser.ParserError`
- **Aggravating factor:** `helpers/subagents.py` `_get_agents_list_from_dir()` catches parse failures and skips the agent silently. An agent that exists on disk, is registered in `agents.json`, and has a complete file set simply vanishes from the callable list — no log, no warning, no startup error.

## Fix Applied (2026-08-31, verified)

1. Quoted the three offending scalars (`royalties` + `sync` `description`; `suno-prompter` `context`).
2. Fixed the `lyricist` line-30 indentation (1 → 2 spaces).
3. **Verification (framework runtime, `/opt/venv-a0/bin/python`):** all 14 `agent.yaml` files parse; `get_available_agents_dict('wgnr_sounds_label')` returns all 14 expected project agents (23 total). Probe scripts: `/tmp/diag2_subagents.py`, `/tmp/diag3_verify.py` (session-local).

## Remaining Work (why this ticket is still open)

**Framework guard against silent agent drops.** `helpers/subagents.py` should not skip unparseable agent definitions without a trace. Candidate approaches (decide in implementation):

- (a) Log a warning (logger + console) naming the agent dir and the parse error when a definition fails to load; and/or
- (b) Surface dropped-but-registered agents: cross-check `agents.json` registrations against discovered agents at project load and warn on any registered-but-not-discovered slug; and/or
- (c) Add a validation mode / health check that validates every `agent.yaml` in a project's agents dir (could live as a project-level check script — no framework edit needed).

Note: `helpers/subagents.py` is Agent Zero framework core — per `/a0/AGENTS.md` permissions, modifying it requires Principal approval. Option (c) avoids framework changes entirely and can ship inside this project today.

**Filed with SysOp 2026-09-06 (Principal-directed):** `/a0/usr/projects/wgnr_ai_sysop/dev-tickets/dev-ticket-2026-09-06-agent-yaml-silent-drop-guard.md`. This ticket stays open until the guard ships and is verified against the acceptance criteria above.

## Acceptance Criteria

- [x] All four agents (`royalties`, `sync`, `lyricist`, `suno-prompter`) load and are callable via `call_subordinate` (verified 2026-08-31)
- [x] All 14 project `agent.yaml` files parse cleanly (verified 2026-08-31)
- [ ] A guard exists so an unparseable/dropped agent definition is visible (log warning, discovery cross-check, or project-level validation script)
- [ ] Guard verified by intentionally breaking one agent.yaml in a scratch copy and observing the warning/failure surface

## Files Affected

- `.a0proj/agents/royalties/agent.yaml` (fixed: quoted description)
- `.a0proj/agents/sync/agent.yaml` (fixed: quoted description)
- `.a0proj/agents/suno-prompter/agent.yaml` (fixed: quoted context)
- `.a0proj/agents/lyricist/agent.yaml` (fixed: line-30 indent)
- Future: `helpers/subagents.py` (guard — pending approach decision + Principal approval for framework edit) or project-local validation script

## Verification Steps

1. `cd /a0 && /opt/venv-a0/bin/python -c "from helpers import subagents; a = subagents.get_available_agents_dict('wgnr_sounds_label'); expected = ['ar','artist-relations','distribution','legal','lyricist','marketing','operations','publicity','royalties','song-architect','studio','sync','suno-prompter','wgnr-sounds-captain']; print('MISSING:', [e for e in expected if e not in a])"` → must print `MISSING: []`
2. Raw parse check: iterate all `.a0proj/agents/*/agent.yaml` with `yaml.safe_load` → zero exceptions
3. (After guard work) break a scratch agent.yaml and confirm the drop is visibly surfaced
