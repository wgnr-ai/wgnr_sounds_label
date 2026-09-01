# dev-tickets

## Purpose
Engineering tickets for the WGNR Sounds Record Label project. Each ticket tracks a discrete unit of engineering work — bug fix, scaffold defect, framework gap, or follow-up. Used by label agents (and the Principal) to coordinate work and ensure nothing falls through the cracks.

## Ownership
- WGNR Sounds Record Label project — managed by wgnr.ai agents under the Principal (Wagner dos Santos)
- Author: the agent who opened the ticket

## Local Contracts

### Naming
- Convention: `dev-ticket-<YYYY-MM-DD>-<topic>.md` — all lowercase, kebab-case, ISO date prefix

### Required sections
- Summary (1-2 sentences)
- Context (why this ticket exists — symptom, root cause, evidence)
- Acceptance criteria (checkable list)
- Files affected (paths)
- Verification steps (how to confirm done)

### Status lifecycle
- `Open` → `In Progress` → `Review` → `Closed`
- Status is **required in YAML frontmatter** (machine-readable; the session-start mailbox reads it):
  ```
  ---
  title: <one-line>
  status: open|in_progress|review|closed
  priority: P0|P1|P2|P3
  created: YYYY-MM-DD
  ---
  ```
- `Closed` tickets are append-only; corrections get a new ticket

## Work Guidance
- New tickets are created when an agent identifies work that needs another agent (or future-self) to pick up
- One ticket = one reviewable unit of work. Split if scope grows
- Framework-core file changes (anything under `/a0` outside `usr/`) require Principal approval — keep that work itemized in the ticket, not executed unilaterally

## Child DOX Index

| Path | Scope |
|---|---|
| `dev-ticket-2026-08-31-agent-yaml-parse-failures.md` | Four agents silently dropped from callable list (agent.yaml parse failures) — data fix done + verified; framework guard open |
