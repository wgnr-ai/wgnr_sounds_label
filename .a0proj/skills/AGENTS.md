# .a0proj/skills

## Purpose

Project-scoped skills for the WGNR Sounds Record Label project — the 5 label-specific skills that translate the PRD's per-artist Suno flow, DistroKid pipeline, BEG catalog archival, ASCAP Music Publishing, and roster reconciliation into executable workflows.

## Ownership

- **WGNR Sounds Record Label project** — managed by wgnr.ai agents
- **Principal:** Wagner dos Santos

## Skills Index (5 label-specific)

| Skill | Description | Applies to |
|---|---|---|
| `suno-integration` | Per-artist Suno role mapping for WGNR Sounds. Identifies Suno role (100% AI vs. Suno-assist), routes master source (Suno vs. Studio), and ensures metadata tagging distinguishes AI-assisted from human-recorded content. | A&R, Distribution & Digital Strategy, Legal & Business Affairs, Studio, Royalties & Finance |
| `distrokid-delivery` | The DistroKid-only DSP delivery pipeline for WGNR Sounds. Sole distributor since 2023. Covers master upload, metadata hygiene, release calendar coordination, and editorial pitching windows. | Distribution & Digital Strategy, Operations / Label Management |
| `beg-catalog-metadata` | Historical BEG (Beloved Entertainment Group) catalog archival. Documents 4 sub-imprints (Beloved Recordings, Yum Recordings, Updego Entertainment, Beloved Soundtracks), 30+ album releases from 1995-2002, and strategic partnerships with Dinemec Records and Crane Mountain Records. | Sync Licensing, A&R, Distribution & Digital Strategy (re-release scope, TBD) |
| `ascap-publishing` | WGNR Sounds Music Publishing is the ASCAP-registered publishing sub-entity that administers performance rights for the catalog. Documents writer registration, ASCAP statement processing, and the master-rights-vs-publishing-rights distinction. | Legal & Business Affairs, Royalties & Finance, Sync Licensing |
| `rosters-and-catalog-reconciliation` | Multi-surface roster sync. Reconciles wgnrsounds.com (out of date), suno.com/@wgnrsounds (active roster), DistroKid catalog metadata, and the internal label catalog. A&R canonical; union of all surfaces. | A&R, Distribution & Digital Strategy, Operations / Label Management |

## Conventions

- Each SKILL.md follows the standard at `/a0/usr/projects/wgnr_ai_sysop/.a0proj/skills/dispatch-safety/SKILL.md` (frontmatter + body + references).
- Skills are enabled per-agent via `plugins/_skills/config.json` (`label_skills_enabled` field) and listed in each agent's `agent.yaml` under `skills_enabled`.
- Skills do NOT replace the canonical PRD; they operationalize the PRD sections named in each skill's frontmatter `Reference` field.

## Child DOX Index

| Path | Scope |
|---|---|
| `.a0proj/skills/suno-integration/` | Per-artist Suno role mapping for WGNR Sounds. Identifies Suno role (100% AI vs. Suno-assist), routes master source (Suno vs. Studio), and ensures metadata tagging distinguishes AI-assisted from human-recorded content. |
| `.a0proj/skills/distrokid-delivery/` | The DistroKid-only DSP delivery pipeline for WGNR Sounds. Sole distributor since 2023. Covers master upload, metadata hygiene, release calendar coordination, and editorial pitching windows. |
| `.a0proj/skills/beg-catalog-metadata/` | Historical BEG (Beloved Entertainment Group) catalog archival. Documents 4 sub-imprints (Beloved Recordings, Yum Recordings, Updego Entertainment, Beloved Soundtracks), 30+ album releases from 1995-2002, and strategic partnerships with Dinemec Records and Crane Mountain Records. |
| `.a0proj/skills/ascap-publishing/` | WGNR Sounds Music Publishing is the ASCAP-registered publishing sub-entity that administers performance rights for the catalog. Documents writer registration, ASCAP statement processing, and the master-rights-vs-publishing-rights distinction. |
| `.a0proj/skills/rosters-and-catalog-reconciliation/` | Multi-surface roster sync. Reconciles wgnrsounds.com (out of date), suno.com/@wgnrsounds (active roster), DistroKid catalog metadata, and the internal label catalog. A&R canonical; union of all surfaces. |

## Verification

- `ls .a0proj/skills/` returns 5 directories (suno-integration, distrokid-delivery, beg-catalog-metadata, ascap-publishing, rosters-and-catalog-reconciliation).
- Each SKILL.md has YAML frontmatter (name, description, trigger_phrases) and a body with Purpose, canonical matrix/pipeline, and References.
