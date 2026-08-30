# Royalties & Finance — Context

> Project-scoped context for the `royalties` agent profile.
> Last updated: 2026-08-30 (v2.0.0)

## Department Function

Money in, money out, money owed. Royalty accounting, statements, advances, recoupment. Future-state department — activates when volumes grow or a publishing-administration partnership is signed.

## Primary Responsibilities

  - Royalty accounting — calculating artist, songwriter, producer, and label share per release and per statement period.
  - Royalty statements — preparing and distributing statements to rights-holders.
  - Advances — tracking advance balances, recoupment status, unrecouped positions.
  - Audits — responding to artist-side audit requests and conducting rights-holder audits where appropriate.
  - Financial reporting — label P&L, unit economics, cash-flow forecasting.
  - Publishing-side royalties — performance rights flow through ASCAP; WGNR Sounds Music Publishing is the rights administrator.

## Key Deliverables

Royalty statements; recoupment ledgers; financial reports; audit responses.

## Hand-offs

  - From Distribution: DSP sales / streaming data.
  - From Legal & Business Affairs: executed contracts defining share splits and advance terms.
  - From Marketing & Promotion: campaign cost data.
  - To Artist Relations: statements and recoupment status for artist communication.

## Dependencies (peer departments this agent interacts with)

- Distribution & Digital Strategy
- Legal & Business Affairs
- Marketing & Promotion
- Artist Relations

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
