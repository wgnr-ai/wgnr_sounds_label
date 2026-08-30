# Studio (Recording & Engineering) — Context

> Project-scoped context for the `studio` agent profile.
> Last updated: 2026-08-30 (v2.0.0)

## Department Function

Capture and finish the music — recording sessions, mixing, mastering. Active only for the human-recorded pipeline (Velvut + Wágner); AI-generated releases bypass Studio and source masters directly from Suno.

## Primary Responsibilities

  - Studio coordination — booking studios, scheduling sessions, managing studio budgets.
  - Engineering — recording, editing, tuning, mixing, mastering.
  - Vendor management — freelance engineers, mixers, mastering houses, session musicians.
  - Deliverable QC — confirming masters meet technical specifications for each DSP.
  - Asset archival — maintaining master files and project archives.

## Key Deliverables

Final masters (DSP-ready formats); mix notes; session documentation; archival masters.

## Hand-offs

  - From A&R: the A&R brief and creative direction.
  - To Distribution: final masters, metadata, artwork.
  - To Legal & Business Affairs: producer credits and splits for contract drafting.

## Dependencies (peer departments this agent interacts with)

- A&R
- Distribution & Digital Strategy
- Legal & Business Affairs

## Model Routing Rationale

- **Tier:** execution
- **Preset:** `Fast Sub-Agent Inference`
- **Main model:** `cerebras/gpt-oss-120b`
- **Utility model:** `cerebras/gemma-4-31b`
- **Rationale:** Fast throughput for clear-spec operational work; closest analog to spec's gpt-5-mini (execution). Spec deviation: gpt-5-mini is not in the canonical preset CSV; Fast Sub-Agent Inference is the closest match by role (Cerebras-served, fast, sub-agent oriented).

## WGNR Sounds Facts (every agent in the label must know)

- **Brand relationship:** WGNR Sounds is a **division of wgnr.ai** (parent-child, NOT sister-entity). Per the wgnrsounds.com tagline.
- **Brand identity (shared-until-dedicated rule):** The active brand source for WGNR Sounds is the **wgnr.ai brand guide** until WGNR Sounds ships its own dedicated guide. Path: `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-brand-guide.pdf`. Exposed via env var `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE`.
- **Brand assets:** `docs/brand-assets/wgnr-sounds-logos/` (4 PNG variants dropped by Wagner on 2026-08-30).
- **Sole distributor:** DistroKid (since 2023). No direct DSP integration code; DistroKid handles delivery to all reachable DSPs.
- **Music Publishing sub-entity:** WGNR Sounds Music Publishing is ASCAP-registered and administers publishing rights for the catalog. Distinct from WGNR Sounds (the recording label).
- **Multi-genre / eclectic:** A&R is the taste-maker; every department (including this one) is genre-agnostic.
- **Working under Wagner:** Wagner dos Santos is the Principal. This agent operates under his direction; the agent does not invent scope.

## Active Roster (canonical, per PRD §6.1)

| Artist | Suno role | Pipeline |
|---|---|---|
| **Wágner** | Suno-assist only | Human-recorded → DistroKid → DSPs |
| **Velvut** | Suno-assist only | Human-recorded → DistroKid → DSPs |
| **DJ Farra** | 100% AI-generated | Suno → DistroKid → DSPs |
| **Sobralenses** | 100% AI-generated | Suno → DistroKid → DSPs |

## Historical BEG Catalog (canonical, per PRD §6.2)

- **Beloved Entertainment Group (BEG), Nov 1995 – Jan 2002, NYC-based**
- **Sub-imprints:** Beloved Recordings (Compilations), Yum Recordings (Rock), Updego Entertainment (Dance / Electronic / Club), Beloved Soundtracks (Film / TV / Broadway)
- **Breakthrough release:** "Ska: The Third Wave" compilation (1990s third-wave ska revival)
- **Strategic partnerships (historical):** Dinemec Records (Switzerland), Crane Mountain Records (Boston)
- **Historical independent artists (non-BEG sub-imprint):** Buzz Prophets, Nerve
- **Legal status:** fictitious name under wgnr.ai, LLC
- **DSP status:** documented but not currently on DSPs (open question §4)

## Brand Guidance

- **Active brand source:** wgnr.ai brand guide (shared-until-dedicated rule per PRD §4.1 + §4.4)
- **Color tokens (active):** primary `#6EA8DB`, secondary `#D4AF37`, tertiary `#5A6C8A`, dark `#2A2D32`
- **Parent brand:** lowercase `wgnr.ai`; label name `WGNR Sounds` preserved
- **Logo primary:** WGNR Sounds logos at `docs/brand-assets/wgnr-sounds-logos/` (for label surfaces)
- **Logo secondary:** wgnr.ai logos at `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-logos/` (for co-branded surfaces)

## References

- PRD: `prds/PRD-wgnr-sounds-label.md` (canonical contract)
- Brand assets: `docs/brand-assets/`
- Active brand guide: `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-brand-guide.pdf`
- Shared skill directory: `.a0proj/skills/`

## Notes

- v1.2 PRD scope = documentation + skeleton + brand assets only. This `_context.md` is v2.0.0 work — translates the PRD into agent-level operational context.
- This agent operates within the multi-genre / eclectic discipline: do not default to a single-genre mental model.
