# .a0proj/agents

## Purpose

Project-scoped agent profiles for the WGNR Sounds Record Label project — the 10 canonical label departments translated into v2.0.0 agent profiles. These agents extend the framework for the label's specific operational context (DistroKid, Suno role matrix, ASCAP Music Publishing, BEG catalog, wgnr.ai-shared brand guide).

## Ownership

- **WGNR Sounds Record Label project** — managed by wgnr.ai agents
- **Principal:** Wagner dos Santos (sole authority for label scope)
- **Parent company:** wgnr.ai (WGNR Sounds is a division, parent-child relationship)

## Disambiguation rule

- Profiles here are **project-scoped label-department specialists**. They do NOT collide with any A0-framework built-in profile.
- For wgnr.ai SysOp work, use the project-scoped variants in `/a0/usr/projects/wgnr_ai_sysop/.a0proj/agents/`. For WGNR Sounds label work, use the profiles here.
- These agents are dispatched via the project-agent surface, not the `call_subordinate` profile registry.

## Department Roster (10 canonical, per PRD §7)

| Slug | Title | Model tier | Preset |
|---|---|---|---|
| `ar` | A&R (Artist & Repertoire) | judgment | Default Coding and Reasoning |
| `marketing` | Marketing & Promotion | judgment | Default Coding and Reasoning |
| `distribution` | Distribution & Digital Strategy | execution | Fast Sub-Agent Inference |
| `publicity` | Publicity / PR | judgment | Default Coding and Reasoning |
| `legal` | Legal & Business Affairs | precision | Default Coding and Reasoning |
| `royalties` | Royalties & Finance | execution | Fast Sub-Agent Inference |
| `studio` | Studio (Recording & Engineering) | execution | Fast Sub-Agent Inference |
| `artist-relations` | Artist Relations | judgment | Default Coding and Reasoning |
| `sync` | Sync Licensing | execution | Fast Sub-Agent Inference |
| `operations` | Operations / Label Management | judgment | Default Coding and Reasoning |

## Child DOX Index

| Path | Scope |
|---|---|
| `.a0proj/agents/ar/` | A&R (Artist & Repertoire) — Find, sign, and develop artists. The creative taste-making function of the label. |
| `.a0proj/agents/marketing/` | Marketing & Promotion — Build and execute the go-to-market plan for each release. Make listeners care. |
| `.a0proj/agents/distribution/` | Distribution & Digital Strategy — Get the music onto every relevant DSP on the right date with the right metadata. The sole integration point is DistroKid (in continuous use since 2023). |
| `.a0proj/agents/publicity/` | Publicity / PR — Earn media coverage and shape the public narrative around releases and artists. |
| `.a0proj/agents/legal/` | Legal & Business Affairs — Contracts, rights, licensing, dispute resolution. The legal backbone of the label. Documents and administers WGNR Sounds Music Publishing (ASCAP-registered). |
| `.a0proj/agents/royalties/` | Royalties & Finance — Money in, money out, money owed. Royalty accounting, statements, advances, recoupment. Future-state department — activates when volumes grow or a publishing-administration partnership is signed. |
| `.a0proj/agents/studio/` | Studio (Recording & Engineering) — Capture and finish the music — recording sessions, mixing, mastering. Active only for the human-recorded pipeline (Velvut + Wágner); AI-generated releases bypass Studio and source masters directly from Suno. |
| `.a0proj/agents/artist-relations/` | Artist Relations — Direct liaison with signed artists. Day-to-day relationship management. |
| `.a0proj/agents/sync/` | Sync Licensing — Place the label's catalog in film, TV, advertising, and video games. Adjacent-revenue engine. Aspirational — no active sync pitching today; activates if a publishing-administration partnership is signed. |
| `.a0proj/agents/operations/` | Operations / Label Management — The glue. Owns inter-department workflow, the release calendar, the budget envelope, and the reporting cadence. |

## Conventions

- Each agent profile mirrors the structure at `/a0/usr/projects/wgnr_ai_sysop/.a0proj/agents/wgnr-project-dev/` (agent.yaml + _context.md + prompts/ + plugins/).
- Model preset is canonical from `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/model_presets_v1.csv`. See each agent's `_context.md` for tier rationale and any deviation notes.
- All agents inherit the WGNR Sounds brand rule (shared-until-dedicated), the DistroKid sole-distributor contract, and the multi-genre / eclectic discipline.

## Verification

- `ls .a0proj/agents/` returns 10 directories (ar, marketing, distribution, publicity, legal, royalties, studio, artist-relations, sync, operations).
- Each directory contains `agent.yaml`, `_context.md`, `prompts/agent.system.main.role.md`, `plugins/_model_config/config.json`, `plugins/_tool_access/config.json`, `plugins/_skills/config.json`.
- `.a0proj/agents.json` registers all 10 with slug + title + model_tier + profile_type.
