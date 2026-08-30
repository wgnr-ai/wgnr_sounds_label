# PRD: WGNR Sounds Record Label — v1 Foundation

> **Scope:** This PRD defines the v1 foundation for the WGNR Sounds Record Label project — the canonical department catalog, operating model, brand identity, and release lifecycle. It stops at the specification level: v1 does NOT scaffold agent profiles, skills, plugins, working simulations, or distribution partner integrations. Department entries are **functional domains**, not pre-built agent profiles; v2 will translate each domain into one or more agent profiles.
>
> **Must-include elements:** (1) Multi-genre / eclectic scope — A&R is taste-maker, departments are genre-agnostic. (2) Brand identity is independent of wgnr.ai — WGNR Sounds has its own logo and brand guide; wgnr.ai color tokens are NOT inherited. (3) The release lifecycle sequence: A&R signs → Recording → Marketing → Distribution → Royalties → Publicity → Artist Relations. (4) Ten canonical label departments (the user-supplied list contains 10 explicitly numbered items despite the prompt referring to '11 departments'; this is flagged in Open Questions §8). (5) v1 scope boundary is PRD + project skeleton ONLY.
>
> **Must-not-compress lists:** Departments: 10 items (numbered 1, 3, 4, 5, 6, 7, 8, 9, 10, 11 from the source prompt — item 2 was skipped; count the 10, not 11). Release-lifecycle phases: 7 stages (A&R signs, Recording, Marketing, Distribution, Royalties, Publicity, Artist Relations). Open Questions: must be enumerated individually so each can be resolved independently in v2.
>
> **Counter-prompt:** After summarizing, verify: (1) Is the multi-genre / eclectic constraint preserved (no genre specialization anywhere)? (2) Is the brand non-inheritance rule (no wgnr.ai colors) explicitly stated and applied? (3) Are all 10 canonical departments covered with the four required fields (function, primary responsibilities, deliverables, hand-offs)? (4) Is the release lifecycle a 7-stage sequence in the documented order? (5) Is the 10-vs-11 department count discrepancy surfaced in Open Questions rather than silently fixed?

**Status:** Draft  
**Version:** v1.0.0  
**Date:** 2026-08-30  
**Author:** wgnr.ai Ops (Orchestrator)  
**Owners:** Wagner dos Santos (Principal) / WGNR Sounds Label project (build + manage)  
**Related:** `/a0/usr/projects/wgnr_ai_sysop/docs/projects-guide.md` (project structure), `/a0/usr/projects/wgnr_ai_sysop/prds/PRD-wgnr-task-manager.md` (PRD format reference)

---

## 1. TL;DR

WGNR Sounds is an independent record label — the virtual representation of a real-world music business. The v1 deliverable defines the label's identity, its 10 canonical departments, the operating model that connects them, and the release lifecycle that drives day-to-day work. The label is multi-genre / eclectic; A&R is a taste-making function, and every department is genre-agnostic. Brand identity is independent of wgnr.ai: WGNR Sounds has its own logo and brand guide (referenced by absolute path, NOT inherited as color tokens). v1 stops at the PRD + project skeleton level; v2 will translate each functional domain into agent profiles, skills, and plugins.

---

## 2. Problem statement

**Source:** Wagner dos Santos directive, 2026-08-30 session.

WGNR Sounds operates as a real-world independent record label covering the full lifecycle from artist signing through royalty accounting. Before v1, there is no formal project skeleton that documents:

1. **What the label does** — no canonical list of departments or operating responsibilities.
2. **How departments interrelate** — no documented hand-offs, decision rights, or release workflow.
3. **What 'multi-genre / eclectic' actually means in practice** — without this, downstream work risks defaulting to a single-genre mental model.
4. **How the label is brand-distinct from wgnr.ai** — without a clear boundary, downstream UI work will leak wgnr.ai color tokens into label artifacts.

**Cost of status quo:** Without a v1 foundation, any v2 work on agent profiles, automation, or release operations starts from zero context. Re-discovery happens on every project. Hand-offs are implicit and tribal. Brand violations leak unnoticed. Multi-genre discipline collapses under convenience.

---

## 3. Goals & non-goals

### Goals

- **G1:** Define the canonical department catalog for WGNR Sounds (the 10 departments explicitly named by the Principal).
- **G2:** Document each department's function, primary responsibilities, deliverables, and hand-offs to peer departments.
- **G3:** Specify the operating model — how departments interrelate and who owns what decisions.
- **G4:** Specify the release lifecycle — the canonical sequence of stages from A&R signing through royalty accounting.
- **G5:** Lock the brand boundary — WGNR Sounds uses its own logo and brand guide; wgnr.ai color tokens are NOT inherited.
- **G6:** Preserve multi-genre discipline — departments are genre-agnostic; A&R is the only taste-making function.
- **G7:** Surface open questions for the Principal to resolve before v2 work begins.
- **G8:** Ship a working project skeleton (this directory tree + `prds/` + `docs/` + `.a0proj/`) so v2 can begin.

### Non-goals (v1)

- **NG1:** NO agent profiles. Department entries are functional domains — not yet agent.yaml definitions.
- **NG2:** NO skills or plugins. Skill scaffolding is v2 work.
- **NG3:** NO working simulation. No sample catalog data, no mock DSP uploads, no test release pipeline.
- **NG4:** NO distribution partner integrations. DSP endpoints and aggregator accounts are placeholder variables only.
- **NG5:** NO royalty accounting automation. Royalty statements and recoupment logic are v2+ work.
- **NG6:** NO contract templates. Legal & Business Affairs department exists as a functional domain; no actual contract files ship in v1.
- **NG7:** NO sync placement tooling. Catalog pitching is documented at the functional level only.
- **NG8:** NO UI work. The label has no app, dashboard, or WebUI component in v1.
- **NG9:** NO wgnr.ai color tokens, CSS variables, or theme references anywhere in label artifacts.

---

## 4. Brand identity

WGNR Sounds is an **independent sister entity** to wgnr.ai. It is **not** a wgnr.ai sub-brand and does **not** inherit wgnr.ai's brand colors, typography, or theme tokens.

### 4.1 Canonical brand assets

The WGNR Sounds logo and brand guide already exist as canonical assets. They live in the SysOp project's knowledge subtree (not in `/a0/usr/knowledge/` — the SysOp knowledge base is the authoritative location for shared client assets):

- **Logo PNG variants** (25 files, transparent + opaque, light + dark, multiple sizes from 50px to 3000px):
  `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-logos/`
- **Brand guide PDF** (canonical typography, logo usage rules, do/don't list, color specifications):
  `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-brand-guide.pdf`

### 4.2 Brand non-inheritance rule

Downstream artifacts (UI, marketing collateral, release assets, internal documents) for WGNR Sounds MUST:

- Reference colors and typography from the WGNR Sounds brand guide only.
- Never hardcode `#6EA8DB`, `#D4AF37`, `#5A6C8A`, or `#2A2D32` — these are wgnr.ai tokens.
- Never apply wgnr.ai CSS variables or theme tokens.
- Use the logo variants from the canonical assets directory only.

### 4.3 Cross-reference handling

If a future document or UI element must visually align with wgnr.ai (e.g., a shared dashboard), the alignment MUST go through an explicit brand-adapter layer, not by token inheritance. The brand-adapter layer is a v2 design question (see Open Questions §8).

---

## 5. Operating model

The label runs as a matrix: every release touches multiple departments in sequence, but each department has standing responsibilities that exist independent of any single release.

### 5.1 Department matrix overview

The label has **ten canonical departments** (see §6 for full definitions). They cluster into four functional groups:

| Group | Departments | Function |
|---|---|---|
| **Creative Front** | A&R, Studio (Recording & Engineering), Artist Relations | Find artists, capture sound, maintain the relationship |
| **Go-to-Market** | Marketing & Promotion, Distribution & Digital Strategy, Publicity / PR | Get the music in front of listeners, get it talked about |
| **Back-Office** | Legal & Business Affairs, Royalties & Finance | Contracts, rights, money in / money out |
| **Specialty** | Sync Licensing, Operations / Label Management | Adjacent revenue, glue that keeps the label running |

### 5.2 Decision rights

For each release, the **A&R lead** owns the artist relationship and the creative direction of the project. The **Operations / Label Management** function owns the inter-department workflow, the release calendar, and the budget envelope. Department leads own decisions within their functional domain; cross-department conflicts escalate to Operations / Label Management.

For decisions that cross group boundaries (e.g., a release strategy that affects marketing spend AND royalty commitments), the Principal (Wagner) is the escalation point.

### 5.3 Standing-vs-project work

Most label work falls into two categories:

- **Project work** — work tied to a specific release, signing, or campaign. Owned by the relevant department lead with cross-functional coordination through Operations.
- **Standing work** — ongoing functional work (royalty statements each quarter, catalog metadata hygiene, contract renewals, rights administration) that never stops. Owned by the relevant department with no end date.

v1 documents this split at the conceptual level. v2 will translate it into agent responsibilities.

---

## 6. Department catalog

Each department is documented as a **functional domain**. v1 does NOT scaffold agent profiles, agent.yaml files, or prompt templates for any department — that translation is v2 work.

For each department below: **Function** (one-line purpose) → **Primary responsibilities** (what the department does) → **Key deliverables** (artifacts it produces) → **Hand-offs** (where its work flows next).

### 6.1 A&R (Artist & Repertoire)

- **Function:** Find, sign, and develop artists. The creative taste-making function of the label.
- **Primary responsibilities:**
  - Scouting — monitoring demos, live shows, social signals, peer recommendations.
  - Demo review — maintaining a triage queue and a hit-rate.
  - Signing — negotiating the deal terms with Legal & Business Affairs and presenting to Operations for budget approval.
  - A&R strategy — deciding what genres and artist profiles the label pursues (constrained by multi-genre / eclectic scope).
  - Artist development — early-stage creative and career guidance after signing.
- **Key deliverables:** Signed recording agreements; A&R briefs for the recording project; demo review logs; quarterly A&R activity reports.
- **Hand-offs:**
  - **To Legal & Business Affairs:** deal terms for contract drafting.
  - **To Studio (Recording & Engineering):** the A&R brief and approved creative direction for the recording project.
  - **To Artist Relations:** the signed artist transitions to ongoing relationship management.
  - **To Marketing & Promotion:** the artist profile and creative positioning for upcoming releases.

### 6.2 Marketing & Promotion

- **Function:** Build and execute the go-to-market plan for each release. Make listeners care.
- **Primary responsibilities:**
  - Release campaign planning — pre-release, release-week, post-release phases.
  - Social media — owned channels, content calendar, community engagement.
  - Paid media — DSP ad buys, social ads, search, influencer partnerships.
  - Content — visuals, videos, behind-the-scenes, artist interviews for owned channels.
  - Performance reporting — campaign-level ROAS, channel attribution.
- **Key deliverables:** Release campaign plans; content calendars; paid media reports; artist-facing marketing briefs.
- **Hand-offs:**
  - **From A&R:** artist profile and creative positioning.
  - **From Distribution & Digital Strategy:** release date, DSP delivery confirmation, pre-save / pre-add mechanics.
  - **To Publicity / PR:** synchronized press moments.
  - **To Royalties & Finance:** campaign cost data for unit-economics reporting.

### 6.3 Distribution & Digital Strategy

- **Function:** Get the music onto every relevant DSP (Spotify, Apple Music, Tidal, Amazon, YouTube Music, etc.) on the right date with the right metadata.
- **Primary responsibilities:**
  - DSP delivery — uploading masters, metadata, artwork, credits.
  - Release calendar — owning the master schedule of upcoming releases across all artists.
  - Metadata hygiene — ISRC / ISWC / UPC codes, songwriter splits, label copy.
  - Pre-save / pre-add / smart-link mechanics — the technical plumbing of fan conversion.
  - DSP relationship management — staying current on each platform's editorial pitching windows, algorithm changes, and feature opportunities.
- **Key deliverables:** Distribution delivery manifests; release calendar; metadata audit reports; DSP pitching briefs.
- **Hand-offs:**
  - **From Studio (Recording & Engineering):** final masters, metadata, artwork, credits.
  - **To Marketing & Promotion:** confirmed release dates and pre-save links.
  - **To Royalties & Finance:** DSP delivery confirmation for sales / streaming accrual.
  - **To Publicity / PR:** launch-day DSP links for press outreach.

### 6.4 Publicity / PR

- **Function:** Earn media coverage and shape the public narrative around releases and artists.
- **Primary responsibilities:**
  - Press release drafting and distribution.
  - Media relationships — maintaining ongoing relationships with editors, journalists, playlisters, and broadcast outlets.
  - Interview coordination — arranging and prepping artists for press.
  - Embargo management — coordinating what drops when, especially around release week.
  - Crisis communications — handling negative press or public incidents.
- **Key deliverables:** Press releases; media lists; interview prep documents; coverage reports.
- **Hand-offs:**
  - **From Marketing & Promotion:** synchronized campaign moments.
  - **From Distribution & Digital Strategy:** launch-day DSP links for press kits.
  - **To Artist Relations:** press schedule coordination around artist availability.

### 6.5 Legal & Business Affairs

- **Function:** Contracts, rights, licensing, dispute resolution. The legal backbone of the label.
- **Primary responsibilities:**
  - Contract drafting — recording agreements, distribution agreements, producer agreements, work-for-hire, NDA, releases.
  - Rights administration — registering rights with collecting societies, maintaining the chain-of-title documentation.
  - Licensing — mechanical, synchronization (in coordination with Sync Licensing), neighboring rights.
  - Dispute resolution — handling claims, counter-claims, royalty disputes, infringement notices.
  - Compliance — staying current on copyright law, rights-society rules, and platform-specific licensing requirements.
- **Key deliverables:** Executed contracts; chain-of-title documentation; license grants; dispute resolution memos.
- **Hand-offs:**
  - **From A&R:** deal terms for contract drafting.
  - **To Royalties & Finance:** executed contracts for royalty setup.
  - **To Sync Licensing:** master and publishing rights availability for pitching.
  - **To Distribution & Digital Strategy:** rights metadata for DSP registration.

### 6.6 Royalties & Finance

- **Function:** Money in, money out, money owed. Royalty accounting, statements, advances, recoupment.
- **Primary responsibilities:**
  - Royalty accounting — calculating artist, songwriter, producer, and label share per release and per statement period.
  - Royalty statements — preparing and distributing statements to rights-holders.
  - Advances — tracking advance balances, recoupment status, and unrecouped positions.
  - **Audits** — responding to artist-side audit requests and conducting rights-holder audits where appropriate.
  - Financial reporting — label P&L, unit economics, cash-flow forecasting.
- **Key deliverables:** Royalty statements; recoupment ledgers; financial reports; audit responses.
- **Hand-offs:**
  - **From Distribution & Digital Strategy:** DSP sales / streaming data.
  - **From Legal & Business Affairs:** executed contracts defining share splits and advance terms.
  - **From Marketing & Promotion:** campaign cost data.
  - **To Artist Relations:** statements and recoupment status for artist communication.

### 6.7 Studio (Recording & Engineering)

- **Function:** Capture and finish the music — recording sessions, mixing, mastering.
- **Primary responsibilities:**
  - Studio coordination — booking studios, scheduling sessions, managing studio budgets.
  - Engineering — recording, editing, tuning, mixing, mastering the audio.
  - Vendor management — relationships with freelance engineers, mixers, mastering houses, session musicians.
  - Deliverable QC — confirming masters meet technical specifications for each DSP.
  - Asset archival — maintaining the master files and the project archives.
- **Key deliverables:** Final masters (in DSP-ready formats); mix notes; session documentation; archival masters.
- **Hand-offs:**
  - **From A&R:** the A&R brief and creative direction.
  - **To Distribution & Digital Strategy:** final masters, metadata, artwork.
  - **To Legal & Business Affairs:** producer credits and splits for contract drafting.

### 6.8 Artist Relations

- **Function:** Direct liaison with signed artists. Day-to-day relationship management.
- **Primary responsibilities:**
  - Single point of contact — every signed artist has an Artist Relations contact.
  - Conflict resolution — handling disagreements, scope disputes, expectation mismatches between artist and label departments.
  - Tour and appearance coordination — supporting live activity where it intersects with release strategy.
  - Career check-ins — periodic structured conversations about the artist's trajectory.
  - Wellness support — connecting artists to mental-health, financial-planning, or career-coaching resources when needed.
- **Key deliverables:** Artist communication logs; check-in notes; conflict-resolution memos; tour coordination plans.
- **Hand-offs:**
  - **From A&R:** the artist transitions to Artist Relations post-signing.
  - **From Royalties & Finance:** statements and recoupment positions for artist communication.
  - **To Operations / Label Management:** escalations when department conflicts can't be resolved at the Artist Relations level.

### 6.9 Sync Licensing

- **Function:** Place the label's catalog in film, TV, advertising, and video games. Adjacent-revenue engine.
- **Primary responsibilities:**
  - Catalog pitching — proactive pitching to music supervisors, ad agencies, trailer houses, game studios.
  - Brief response — answering inbound briefs from supervisors.
  - License negotiation — drafting and negotiating sync licenses within policy.
  - Catalog metadata — keeping sync-friendly metadata current (instrumental versions, stems, alt mixes, BPM, mood tags).
  - Reporting — tracking placements, license fees, and revenue.
- **Key deliverables:** Sync pitch decks; executed sync licenses; sync metadata packages; placement reports.
- **Hand-offs:**
  - **From Legal & Business Affairs:** confirmed master and publishing rights availability.
  - **From Studio (Recording & Engineering):** sync-friendly versions (instrumentals, stems) when available.
  - **To Royalties & Finance:** sync license fees for revenue accounting.

### 6.10 Operations / Label Management

- **Function:** The glue. Owns inter-department workflow, the release calendar, the budget envelope, and the reporting cadence.
- **Primary responsibilities:**
  - Release calendar — the master schedule of all upcoming releases across all artists.
  - Inter-department workflow — sequencing and unblocking cross-functional work.
  - Budget — the label's overall budget envelope and per-release budget approval.
  - Reporting — operating reports to the Principal on label health (catalog, releases, financials at a glance).
  - Cross-department escalation point — the place conflicts go when they can't resolve within or between the department pair.
- **Key deliverables:** Release calendar; weekly / monthly operating reports; per-release budget approvals; inter-department workflow templates.
- **Hand-offs:**
  - **From every department:** project status and escalations.
  - **To the Principal (Wagner):** operating reports and cross-department decisions.
  - **To every department:** budget approvals and release calendar changes.

---

## 7. Release lifecycle workflow

A canonical release moves through seven stages in sequence. Each stage has a primary owner and at least one supporting department.

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  1. A&R     │──▶│  2. Studio  │──▶│ 3. Marketing │──▶│ 4. Distrib. │
│   signs     │    │  records    │    │  plans      │    │  delivers   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
                                                                │
                                                                ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ 7. Artist   │◀──│  6. Publicity│◀──│ 5. Royalties│
│  Relations  │    │  amplifies  │    │  accrues    │
└─────────────┘    └─────────────┘    └─────────────┘
```

### 7.1 Stage-by-stage

1. **A&R signs** — A&R identifies and signs an artist. Legal finalizes the contract. Artist Relations picks up the relationship.
2. **Studio records** — Studio (Recording & Engineering) executes the recording project per the A&R brief. Final masters, metadata, and artwork are produced.
3. **Marketing plans** — Marketing & Promotion builds the release campaign in coordination with Publicity. Distribution confirms the release date and pre-save mechanics.
4. **Distribution delivers** — Distribution & Digital Strategy uploads masters to every DSP on the agreed date.
5. **Royalties accrues** — Royalties & Finance begins accruing streaming / sales data from the DSPs.
6. **Publicity amplifies** — Publicity / PR coordinates press coverage, interviews, and editorial pitching around the launch and post-launch window.
7. **Artist Relations sustains** — Artist Relations handles the ongoing artist relationship through the post-release period, including tour coordination, check-ins, and statement communication.

### 7.2 Cross-stage coordination

Marketing, Publicity, and Distribution must coordinate the launch window as a single synchronized moment. Operations / Label Management owns the calendar. Royalties & Finance joins the standup once DSP data starts flowing.

---

## 8. Open questions (for Wagner to resolve before v2)

1. **Department count** — the user-supplied department list numbered items 1, 3, 4, 5, 6, 7, 8, 9, 10, 11 — that's **10 departments**, not 11 as stated in the prompt. Is there an 11th department that should be added (e.g., Catalog & Repertoire Administration, Digital Archive, Brand & Creative)?
2. **Real-world roster size** — how many artists are signed at v2 kickoff? Drives agent-profile concurrency assumptions.
3. **Distribution partners** — which aggregators and DSP-direct relationships does WGNR Sounds use? (DistroKid, TuneCore, AWAL, CD Baby, or direct DSP agreements?)
4. **Sync priorities** — which verticals matter most: film / TV / advertising / video games / all? Drives Sync Licensing agent scoping.
5. **Royalty accounting cadence** — quarterly, semi-annual, annual? Drives Royalties & Finance workflow design.
6. **Catalog prefix** — what is the internal label catalog prefix used for release IDs? (Currently `WGNR_SOUNDS_CATALOG_PREFIX` placeholder in `variables.env`.)
7. **Timezone for release calendar** — what is the label's home timezone for release-day alignment? (Currently `UTC` placeholder.)
8. **Brand-adapter layer** — if a future WGNR Sounds UI must visually coexist with wgnr.ai surfaces (e.g., a shared dashboard), how is the brand boundary preserved at the visual layer? The PRD forbids color-token inheritance; an adapter pattern is the open design question.
9. **wOS activation** — should the v2 project wire `wgnr_ai_os` plugin instructions into `.a0proj/instructions/`? v1 deliberately does not; this is a v2 activation decision.
10. **Git remote** — should the project be published to a new `github.com/wgnr-ai/wgnr_sounds_label.git` repo? v1 is local-only.

---

## 9. Out of scope (v1)

v1 ships only the project skeleton and this PRD. The following are explicitly out of scope and deferred:

- **Agent profiles** for any of the 10 departments (`.a0proj/agents/` is intentionally empty).
- **Skills and skill scaffolding** (`.a0proj/skills/` is intentionally absent).
- **Plugin configurations** (`.a0proj/plugins/` is intentionally absent).
- **Working simulation** — no sample catalog data, no mock releases, no test DSP uploads.
- **Distribution partner integrations** — DSP endpoints in `variables.env` are placeholder comments.
- **Royalty accounting automation** — no calculation engine ships.
- **Contract templates** — Legal & Business Affairs is a functional domain only.
- **Sync placement tooling** — no pitch-deck templates, no outreach sequences.
- **WebUI / dashboard / app work** — no UI components ship.
- **wgnr.ai brand tokens in any label artifact.**

---

## 10. References

- `/a0/usr/projects/wgnr_ai_sysop/prds/PRD-wgnr-task-manager.md` — PRD format reference (TL;DR, AI-Readable Block, problem statement, goals / non-goals, traceability).
- `/a0/usr/projects/wgnr_ai_sysop/docs/projects-guide.md` — project structure and `project.json` schema reference.
- `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-logos/` — canonical WGNR Sounds logo PNG variants.
- `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-brand-guide.pdf` — canonical WGNR Sounds brand guide.
- `/a0/usr/projects/wgnr_ai_sysop/prompt_includes/ai-readable-document-pattern.promptinclude.md` — AI-Readable Block convention used in this PRD.

---

## 11. Closeout checklist

- [x] AI-Readable Block present (Scope, Must-include, Must-not-compress, Counter-prompt).
- [x] TL;DR paragraph ≤ 200 words.
- [x] Problem statement with source attribution.
- [x] Goals numbered (G1–G8).
- [x] Non-goals numbered (NG1–NG9) and explicitly call out v1 scope boundaries.
- [x] Brand identity section with canonical asset paths and non-inheritance rule.
- [x] Operating model with department grouping and decision rights.
- [x] Department catalog with function / responsibilities / deliverables / hand-offs for each of the 10 departments explicitly named.
- [x] Release lifecycle as a 7-stage sequence.
- [x] Open questions enumerated individually for independent resolution.
- [x] Out-of-scope section listing what v1 does NOT include.
- [x] References with absolute paths to canonical supporting files.
- [x] DOX closeout: root `AGENTS.md` and `prds/AGENTS.md` updated to reference this PRD.
