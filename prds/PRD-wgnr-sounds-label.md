# PRD: WGNR Sounds Record Label — v1.2 (Corrected Foundation)

> **Scope:** This PRD defines the v1.2 foundation for the WGNR Sounds Record Label project — the canonical department catalog, operating model, brand identity (with the **shared-until-dedicated brand-guide rule** introduced in v1.2), roster & catalog (active + historical BEG), release lifecycle, distribution pipeline (DistroKid + per-artist Suno flow), and the WGNR Sounds Music Publishing sub-entity. v1.2 absorbs Wagner's primary-source corrections (2026-08-30): (a) the active brand guide is now the **shared wgnr.ai brand guide** (not a Sounds-specific guide that doesn't yet exist); (b) casing sweep across all files (`division of WGNR` → `division of wgnr.ai`, `WGNR, LLC` → `wgnr.ai, LLC`); (c) brand-asset path refresh from `.a0proj/knowledge/client-assets/wgnr-sounds-assets/` to `docs/brand-assets/`; (d) `.a0proj/project.json` instructions field rewrite. v1.2 stops at the specification level: it does NOT scaffold agent profiles, skills, plugins, working simulations, or distribution partner integrations. Department entries are **functional domains**, not pre-built agent profiles; v2 will translate each domain into one or more agent profiles.
>
> **Must-include elements:** (1) WGNR Sounds is a **division of wgnr.ai** (parent-child), NOT a peer entity. (2) The **shared-until-dedicated brand-guide rule** is the active policy: until WGNR Sounds ships its own dedicated brand guide, the **wgnr.ai brand guide** is the active source for color and typography tokens, exposed via `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE`. (3) Brand assets live at `docs/brand-assets/` (Wagner dropped 4 logo PNGs on 2026-08-30; brand-guide PDF placeholder still pending). (4) The active roster (Wágner, Velvut, DJ Farra, Sobralenses) + the historical BEG catalog (1995–2002, 4 sub-imprints, 30+ albums). (5) Per-artist Suno role matrix: DJ Farra + Sobralenses = 100% AI-generated; Wágner + Velvut = Suno-assist only. (6) **DistroKid is the sole distributor since 2023** (not a generic DSP placeholder). (7) **WGNR Sounds Music Publishing** is an ASCAP-registered sub-entity owned by WGNR Sounds; documented under Legal & Business Affairs. (8) Multi-genre / eclectic scope — A&R is taste-maker, departments are genre-agnostic. (9) v1.2 scope is PRD + project skeleton + brand assets scaffold + casing sweep + project.json v1.2 alignment ONLY.
>
> **Must-not-compress lists:** Departments: 10 items (numbered §7.1–§7.10). Release-lifecycle phases: 7 stages. Suno role matrix: 4 artists × 4 columns (Artist / Suno role / Master source / Distribution flow). Open Questions: must be enumerated individually so each can be resolved independently in v2. BEG sub-imprints: 4 (Beloved Recordings, Yum Recordings, Updego Entertainment, Beloved Soundtracks). v1.2 §4 brand-identity subsections: 6 (4.1 active guide, 4.2 future guide, 4.3 logo assets, 4.4 color tokens, 4.5 Music Publishing unchanged, 4.6 cross-reference handling).
>
> **Counter-prompt:** After summarizing, verify: (1) Is the division-of-wgnr.ai framing (NOT sister-entity) the only stated brand relationship? (2) Is the shared-until-dedicated brand-guide rule documented (wgnr.ai guide is the active source until a Sounds guide ships)? (3) Are all 4 BEG sub-imprints named? (4) Are all 4 active artists named with their Suno role? (5) Is DistroKid named as the sole distributor with the year (2023)? (6) Is WGNR Sounds Music Publishing named as ASCAP-registered? (7) Is the brand-asset path `docs/brand-assets/` (NOT `.a0proj/knowledge/client-assets/wgnr-sounds-assets/`)? (8) Is the `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE` env-var referenced? (9) Are parent-brand references written as lowercase `wgnr.ai` (NOT uppercase `WGNR`)?

**Status:** Draft (v1.2)  
**Version:** v1.2.0  
**Date:** 2026-08-30  
**Supersedes:** v1.1.0 (commit `7f090d4`)  
**Author:** wgnr.ai Ops (Orchestrator)  
**Owners:** Wagner dos Santos (Principal) / WGNR Sounds Label project (build + manage)  
**Related:** `/a0/usr/projects/wgnr_ai_sysop/docs/projects-guide.md` (project structure), `/a0/usr/projects/wgnr_ai_sysop/prds/PRD-wgnr-task-manager.md` (PRD format reference)

---

## 1. TL;DR

WGNR Sounds is a **division of wgnr.ai** — the virtual representation of a real-world independent record label owned by wgnr.ai President Wagner dos Santos (per the wgnrsounds.com tagline). The v1.2 deliverable applies Wagner's primary-source corrections (2026-08-30) on top of v1.1: (a) the **shared-until-dedicated brand-guide rule** (the wgnr.ai brand guide is the active source until WGNR Sounds ships its own dedicated guide); (b) brand-asset path refresh to `docs/brand-assets/` (Wagner dropped 4 logos on 2026-08-30); (c) casing sweep (~30 instances: `division of WGNR` → `division of wgnr.ai`, `WGNR, LLC` → `wgnr.ai, LLC`); (d) `.a0proj/project.json` instructions field rewrite. v1.2 documents the label's identity, active + historical roster, 10 canonical departments, the operating model (including the per-artist Suno integration map), the release lifecycle, the DistroKid distribution pipeline, and the ASCAP-registered WGNR Sounds Music Publishing sub-entity. The label is multi-genre / eclectic; A&R is a taste-making function, and every department is genre-agnostic. v1.2 stops at the PRD + project skeleton + brand assets scaffold level; v2 will translate each functional domain into agent profiles, skills, and plugins.

## 2. Problem statement

**Source:** Wagner dos Santos directive, 2026-08-30 session.

WGNR Sounds operates as a real-world independent record label covering the full lifecycle from artist signing through royalty accounting, with a historical back-catalog spanning the Beloved Entertainment Group (BEG, 1995–2002) and an active roster that splits between human-recorded and 100% AI-generated pipelines. Before v1, there is no formal project skeleton that documents:

1. **What the label does** — no canonical list of departments or operating responsibilities.
2. **How departments interrelate** — no documented hand-offs, decision rights, or release workflow.
3. **What 'multi-genre / eclectic' actually means in practice** — without this, downstream work risks defaulting to a single-genre mental model.
4. **How the label is brand-related to wgnr.ai** — v1 framed WGNR Sounds as a peer entity rather than a division; v1.1 corrected it to "division of WGNR" (parent-child). v1.2 corrects the casing to **division of wgnr.ai** per Wagner's brand-name casing directive.
5. **The active roster vs. historical catalog distinction** — without a canonical roster, downstream A&R, sync, and roster reconciliation work has no source of truth.
6. **The per-artist Suno integration** — the active roster splits between 100% AI-generated (DJ Farra, Sobralenses) and human-recorded with Suno-as-assist (Wágner, Velvut). The Distribution department needs this matrix to route masters correctly.
7. **The WGNR Sounds Music Publishing sub-entity** — the ASCAP-registered publishing company is a separate legal entity from the recording label; its relationship to Legal & Business Affairs and Royalties must be documented.
8. **Which brand guide governs label visuals** — v1.1 introduced a brand non-inheritance rule that positioned wgnr.ai tokens as fallback-only. v1.2 reverses this: WGNR Sounds does not yet have its own brand guide, so it shares that of wgnr.ai (the active brand source) until a Sounds-specific guide ships.

**Cost of status quo:** Without a v1.2 foundation, any v2 work on agent profiles, automation, or release operations starts from zero context. Re-discovery happens on every project. Hand-offs are implicit and tribal. Brand violations leak unnoticed (casing or token source). Multi-genre discipline collapses under convenience. The wrong "peer-of-wgnr.ai" framing would propagate downstream and undermine the parent-child brand relationship that WGNR Sounds (the division) inherits from wgnr.ai (the parent).

## 3. Goals & non-goals

### Goals

- **G1:** Define the canonical department catalog for WGNR Sounds (the 10 departments explicitly named by the Principal).
- **G2:** Document each department's function, primary responsibilities, deliverables, and hand-offs to peer departments.
- **G3:** Specify the operating model — how departments interrelate and who owns what decisions.
- **G4:** Specify the release lifecycle — the canonical sequence of stages from A&R signing through royalty accounting.
- **G5:** Document the **division-of-wgnr.ai** brand relationship and the **shared-until-dedicated brand-guide rule** (the wgnr.ai brand guide is the active source until WGNR Sounds ships its own).
- **G6:** Preserve multi-genre discipline — departments are genre-agnostic; A&R is the only taste-making function.
- **G7:** Document the active roster (4 artists with per-artist Suno role) and the historical BEG back-catalog (1995–2002, 4 sub-imprints, 30+ albums).
- **G8:** Lock the distribution pipeline as **DistroKid (sole distributor since 2023)** with per-artist Suno flow routing.
- **G9:** Document **WGNR Sounds Music Publishing** as the ASCAP-registered publishing sub-entity owned by WGNR Sounds.
- **G10:** Surface open questions for the Principal to resolve before v2 work begins.
- **G11:** Ship a working project skeleton (this directory tree + `prds/` + `docs/` + `.a0proj/` + brand assets at `docs/brand-assets/`) so v2 can begin.

### Non-goals (v1.2)

- **NG1:** NO agent profiles. Department entries are functional domains — not yet agent.yaml definitions.
- **NG2:** NO skills or plugins. Skill scaffolding is v2 work.
- **NG3:** NO working simulation. No sample catalog data, no mock DSP uploads, no test release pipeline.
- **NG4:** NO direct DSP integration code (we use DistroKid as the sole integration point; no Spotify API, no Apple Music API, etc.).
- **NG5:** NO royalty accounting automation. Royalty statements and recoupment logic are v2+ work.
- **NG6:** NO contract templates. Legal & Business Affairs department exists as a functional domain; no actual contract files ship in v1.2.
- **NG7:** NO sync placement tooling. Catalog pitching is documented at the functional level only; Sync Licensing is aspirational.
- **NG8:** NO UI work. The label has no app, dashboard, or WebUI component in v1.2.
- **NG9:** NO dedicated WGNR Sounds brand-guide PDF. The label uses the shared wgnr.ai brand guide as the active source until a Sounds-specific guide ships.
- **NG10:** NO podcast operations. Podcast is a separate project (`wgnr_sounds_podcast`).
- **NG11:** NO BEG catalog re-release work. The historical 1995–2002 catalog is documented but not migrated to DSPs.

## 4. Brand identity

WGNR Sounds is a **division of wgnr.ai** (per the wgnrsounds.com tagline, verified by Wagner 2026-08-30). The relationship is **parent-child**, not sister-entity. WGNR Sounds inherits the wgnr.ai parent brand voice and uses its own WGNR Sounds visual identity (logos at `docs/brand-assets/wgnr-sounds-logos/`).

**v1.2 introduces the shared-until-dedicated brand-guide rule** (reverses v1.1's brand non-inheritance rule):

### 4.1 Brand guide (active)

Until WGNR Sounds ships its own dedicated brand guide, the label uses the **wgnr.ai brand guide** as the active, authoritative brand source. The active brand guide path:

- **File:** `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-brand-guide.pdf`
- **Exposed via env var:** `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE` (defined in `.a0proj/variables.env`)

This is the authoritative brand reference for color tokens, typography tokens, and brand voice for WGNR Sounds until a Sounds-specific guide is created.

### 4.2 Brand guide (future)

When WGNR Sounds creates a dedicated brand guide, it goes at:

- **File:** `docs/brand-assets/wgnr-sounds-brand-guide.pdf` (replacing the current `.gitkeep` placeholder)

At that point, the dedicated guide supersedes the parent-shared guide for WGNR Sounds-specific visuals. Update `docs/brand-assets/README.md`, the project-root `AGENTS.md`, and §4 of this PRD to reflect the change.

### 4.3 Logo assets

WGNR Sounds has its own logos at:

- **Folder:** `docs/brand-assets/wgnr-sounds-logos/` — 4 PNG variants dropped by Wagner on 2026-08-30 (label `wsounds-logo1a.png` through `wsounds-logo3.png`)
- **DOX contract:** `docs/brand-assets/AGENTS.md`

Use the WGNR Sounds logos for **label-specific visuals** (primary mark for label artifacts).

The wgnr.ai parent-brand logos at `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-logos/` are the parent brand reference. They may be used where brand-aligned (e.g., co-branded surfaces), but **the WGNR Sounds logo is the primary mark for label artifacts**.

### 4.4 Color tokens

Until a dedicated WGNR Sounds brand guide exists, color and typography tokens come from the **wgnr.ai brand guide**. Use wgnr.ai tokens for label artifacts:

- Primary accent: `#6EA8DB`
- Secondary accent: `#D4AF37`
- Tertiary/muted: `#5A6C8A`
- Dark backgrounds: `#2A2D32`

**This REVERSES the v1.1 'brand non-inheritance rule'** — the wgnr.ai tokens are the active source until the Sounds guide ships. The wgnr.ai brand guide PDF is the canonical reference; the token values match the SysOp project's brand standard.

### 4.5 WGNR Sounds Music Publishing

WGNR Sounds Music Publishing is a **separately-registered legal entity** owned by WGNR Sounds. It is:

- **ASCAP-registered** for performing rights royalty management.
- The administrator of publishing rights for the WGNR Sounds catalog (active + historical BEG).
- **Distinct from WGNR Sounds the recording label** — the label is the recording entity; the publishing entity owns the songwriter/publisher share.
- Documented under §7.5 Legal & Business Affairs as the entity that administers publishing rights.
- Referenced from §7.7 Royalties & Finance for the publishing-side royalty flow (performance rights royalties flow through ASCAP; WGNR Sounds Music Publishing is the rights administrator).

### 4.6 Cross-reference handling

For shared surfaces (e.g., a wgnr.ai dashboard that lists WGNR Sounds releases), use wgnr.ai tokens as primary (already in use across the parent product) with the WGNR Sounds logo as a secondary mark. For label-specific surfaces, use wgnr.ai tokens until the Sounds guide ships, then use Sounds tokens. If a future UI must visually coexist with wgnr.ai surfaces, an explicit brand-adapter layer is required (see Open Question §10) — direct token inheritance is permitted today only because the active brand source is already the wgnr.ai guide.

## 5. Operating model

The label runs as a matrix: every release touches multiple departments in sequence, but each department has standing responsibilities that exist independent of any single release.

### 5.1 Department matrix overview

The label has **ten canonical departments** (see §7 for full definitions). They cluster into four functional groups:

| Group | Departments | Function |
|---|---|---|
| **Creative Front** | A&R, Studio (Recording & Engineering), Artist Relations | Find artists, capture sound, maintain the relationship |
| **Go-to-Market** | Marketing & Promotion, Distribution & Digital Strategy, Publicity / PR | Get the music in front of listeners, get it talked about |
| **Back-Office** | Legal & Business Affairs, Royalties & Finance | Contracts, rights, money in / money out |
| **Specialty** | Sync Licensing, Operations / Label Management | Adjacent revenue, glue that keeps the label running |

### 5.2 Decision rights

For each release, the **A&R lead** owns the artist relationship and the creative direction of the project. The **Operations / Label Management** function owns the inter-department workflow, the release calendar, and the budget envelope. Department leads own decisions within their functional domain; cross-department conflicts escalate to Operations / Label Management.

For decisions that cross group boundaries (e.g., a release strategy that affects marketing spend AND royalty commitments), the Principal (wgnr.ai President Wagner dos Santos) is the escalation point.

### 5.3 Standing-vs-project work

Most label work falls into two categories:

- **Project work** — work tied to a specific release, signing, or campaign. Owned by the relevant department lead with cross-functional coordination through Operations.
- **Standing work** — ongoing functional work (royalty statements each quarter, catalog metadata hygiene, contract renewals, rights administration) that never stops. Owned by the relevant department with no end date.

v1.2 documents this split at the conceptual level. v2 will translate it into agent responsibilities.

### 5.4 Suno Integration by Artist (NEW in v1.1)

The active roster splits between two pipelines. The per-artist Suno role determines the master source and the distribution flow:

| Artist | Suno role | Master source | Distribution flow |
|---|---|---|---|
| **DJ Farra** | 100% AI-generated music AND lyrics | Suno (download from Suno) | Suno → DistroKid → DSPs |
| **Sobralenses** | 100% AI-generated music AND lyrics | Suno (download from Suno) | Suno → DistroKid → DSPs |
| **Velvut** | Suno-assist only (song-idea assistance) | Human recording (studio) | Studio → DistroKid → DSPs |
| **Wágner** | Suno-assist only (song-idea assistance) | Human recording (studio) | Studio → DistroKid → DSPs |

**Implications for departments:**

- **Distribution & Digital Strategy (§7.3):** masters arrive from two source types (Suno download vs. studio-rendered). Metadata pipeline must distinguish them for rights-administration hand-off.
- **Legal & Business Affairs (§7.5):** Suno-generated works carry Suno's licensing terms (per Suno's commercial-use terms as of 2026-08). Human-recorded works with Suno-assist carry standard recording-agreement terms. The contract template set differs by source.
- **Royalties & Finance (§7.7):** publishing-side royalty splits must account for Suno's role in AI-generated works (Suno's commercial license terms apply).
- **A&R (§7.1):** artist signings must include a Suno-role declaration in the A&R brief (the matrix above is the canonical reference).

This matrix is a v1.1 deliverable; A&R + Distribution departments use it in v2.

## 6. Roster & catalog (NEW in v1.1)

The label operates with an **active roster** and a **historical back-catalog**. Both surfaces are canonical sources for downstream A&R, sync, and roster-reconciliation work.

### 6.1 Current active roster

Per Wagner dos Santos (2026-08-30), the currently active artists are:

- **Wágner** — the Principal; performs under multiple artist names
- **Velvut** — human-recorded pipeline; Suno-assist only
- **DJ Farra** — 100% AI-generated pipeline (Suno = source of masters)
- **Sobralenses** — 100% AI-generated pipeline (Suno = source of masters)

### 6.2 Historical back-catalog — Beloved Entertainment Group (BEG)

The historical catalog spans the Beloved Entertainment Group (BEG), an independent record label founded by Wagner dos Santos, NYC-based, operated **November 1995 – January 2002**. BEG produced 30+ domestic + international album releases across four sub-imprints:

| Sub-imprint | Focus |
|---|---|
| **Beloved Recordings** | Compilations |
| **Yum Recordings** | Rock |
| **Updego Entertainment** | Dance / Electronic / Club |
| **Beloved Soundtracks** | Film, television, Broadway |

**Breakthrough release:** "Ska: The Third Wave" compilation (1990s third-wave ska revival).

**Strategic partnerships (historical):**

- **Dinemec Records** (Switzerland)
- **Crane Mountain Records** (Boston)

**Historical independent artists (non-BEG sub-imprint):**

- **Buzz Prophets**
- **Nerve**

**Legal status (current):** BEG is currently filed as a **fictitious name under wgnr.ai, LLC**.

### 6.3 Roster reconciliation

The wgnrsounds.com website is **out of date** and needs updating; the canonical roster is the union of the website and the Suno platform (both surfaces are canonical sources per Wagner 2026-08-30). A&R (in v2) owns the canonical roster reconciliation.

**Two sources, one truth:** the website lists the artists; Suno has AI-generated artist profiles for the AI-pipeline artists. The label's authoritative roster is the reconciliation of both surfaces, maintained by A&R in v2.

## 7. Department catalog

Each department is documented as a **functional domain**. v1.2 does NOT scaffold agent profiles, agent.yaml files, or prompt templates for any department — that translation is v2 work.

For each department below: **Function** (one-line purpose) → **Primary responsibilities** (what the department does) → **Key deliverables** (artifacts it produces) → **Hand-offs** (where its work flows next).

### 7.1 A&R (Artist & Repertoire)

- **Function:** Find, sign, and develop artists. The creative taste-making function of the label.
- **Primary responsibilities:**
  - Scouting — monitoring demos, live shows, social signals, peer recommendations.
  - Demo review — maintaining a triage queue and a hit-rate.
  - Signing — negotiating the deal terms with Legal & Business Affairs and presenting to Operations for budget approval.
  - A&R strategy — deciding what genres and artist profiles the label pursues (constrained by multi-genre / eclectic scope).
  - Artist development — early-stage creative and career guidance after signing.
  - **Roster reconciliation (NEW in v1.1):** maintaining the canonical roster as the union of wgnrsounds.com and the Suno platform surfaces.
  - **Suno-role declaration (NEW in v1.1):** including the per-artist Suno role (see §5.4) in every A&R brief.
- **Key deliverables:** Signed recording agreements; A&R briefs for the recording project (including Suno-role declaration); demo review logs; quarterly A&R activity reports; canonical roster snapshot.
- **Hand-offs:**
  - **To Legal & Business Affairs:** deal terms for contract drafting (including Suno-role clause).
  - **To Studio (Recording & Engineering):** the A&R brief and approved creative direction for the recording project.
  - **To Artist Relations:** the signed artist transitions to ongoing relationship management.
  - **To Marketing & Promotion:** the artist profile and creative positioning for upcoming releases.

### 7.2 Marketing & Promotion

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

### 7.3 Distribution & Digital Strategy

- **Function:** Get the music onto every relevant DSP (Spotify, Apple Music, Tidal, Amazon, YouTube Music, etc.) on the right date with the right metadata. The sole integration point is **DistroKid**, in continuous use as the label's distributor since 2023.
- **Primary responsibilities:**
  - **Sole distributor: DistroKid (since 2023)** — uploads masters, metadata, artwork, credits to DistroKid; DistroKid handles delivery to all reachable DSPs.
  - **Per-artist Suno flow routing (NEW in v1.1):** for DJ Farra + Sobralenses, the master source is Suno; for Velvut + Wágner, the master source is the studio. The distribution pipeline distinguishes the two source types for metadata and rights hand-off (see §5.4 matrix).
  - **Mechanical rights:** handled via DistroKid / MLC (Mechanical Licensing Collective) registration for US compulsory mechanical licensing.
  - Release calendar — owning the master schedule of upcoming releases across all artists.
  - Metadata hygiene — ISRC / ISWC / UPC codes, songwriter splits, label copy.
  - Pre-save / pre-add / smart-link mechanics — the technical plumbing of fan conversion.
  - DSP relationship management — staying current on each platform's editorial pitching windows, algorithm changes, and feature opportunities.
- **Key deliverables:** Distribution delivery manifests; release calendar; metadata audit reports; DSP pitching briefs; Suno-vs-studio source attribution logs.
- **Hand-offs:**
  - **From Studio (Recording & Engineering):** final masters, metadata, artwork, credits (for human-recorded artists).
  - **From Suno (AI pipeline):** downloaded masters + Suno licensing documentation (for AI-generated artists).
  - **To Marketing & Promotion:** confirmed release dates and pre-save links.
  - **To Royalties & Finance:** DSP delivery confirmation for sales / streaming accrual.
  - **To Publicity / PR:** launch-day DSP links for press outreach.

### 7.4 Publicity / PR

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

### 7.5 Legal & Business Affairs

- **Function:** Contracts, rights, licensing, dispute resolution. The legal backbone of the label. Also documents and administers **WGNR Sounds Music Publishing** (ASCAP-registered).
- **Primary responsibilities:**
  - Contract drafting — recording agreements, distribution agreements, producer agreements, work-for-hire, NDA, releases.
  - Rights administration — registering rights with collecting societies, maintaining the chain-of-title documentation.
  - **WGNR Sounds Music Publishing (NEW in v1.1):** administering publishing rights for the catalog on behalf of the writers through the ASCAP-registered sub-entity. Performance rights royalties flow through ASCAP; WGNR Sounds Music Publishing is the rights administrator.
  - Licensing — mechanical (via DistroKid / MLC, see §7.3), synchronization (in coordination with Sync Licensing, see §7.9 — aspirational), neighboring rights.
  - Dispute resolution — handling claims, counter-claims, royalty disputes, infringement notices.
  - Compliance — staying current on copyright law, rights-society rules, and platform-specific licensing requirements.
  - **Suno licensing terms (NEW in v1.1):** maintaining awareness of Suno's commercial-use license terms as they apply to AI-generated masters under DJ Farra and Sobralenses.
- **Key deliverables:** Executed contracts; chain-of-title documentation; license grants; dispute resolution memos; WGNR Sounds Music Publishing registration documentation; Suno-license attestation for AI-pipeline releases.
- **Hand-offs:**
  - **From A&R:** deal terms for contract drafting (including Suno-role clause).
  - **To Royalties & Finance:** executed contracts for royalty setup.
  - **To Sync Licensing:** master and publishing rights availability for pitching.
  - **To Distribution & Digital Strategy:** rights metadata for DSP registration.

### 7.6 Studio (Recording & Engineering)

- **Function:** Capture and finish the music — recording sessions, mixing, mastering. **Active only for the human-recorded pipeline** (Velvut + Wágner per §5.4); AI-generated releases (DJ Farra + Sobralenses) bypass Studio and source masters directly from Suno.
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

### 7.7 Royalties & Finance

- **Function:** Money in, money out, money owed. Royalty accounting, statements, advances, recoupment. **Future-state department** in v1.1 (see §7.7.1).

#### 7.7.1 Current state and why it's documented

- **Current state (v1.1):** No royalty tooling exists. Royalties are currently **insignificant** (Wagner is the sole artist, performing under multiple artist names). Royalty accounting is not a day-to-day operation today.
- **Why documented:** Department exists structurally for v2 and beyond. When volumes grow (additional artists, sync placements, publishing revenue), this department activates.
- **Publishing-side royalties:** Administered by **WGNR Sounds Music Publishing** (ASCAP-registered, see §4.5 + §7.5). Performance rights royalties flow through ASCAP; WGNR Sounds Music Publishing is the rights administrator on behalf of the writers.

#### 7.7.2 Future-state primary responsibilities (v2+)

- Royalty accounting — calculating artist, songwriter, producer, and label share per release and per statement period.
- Royalty statements — preparing and distributing statements to rights-holders.
- Advances — tracking advance balances, recoupment status, and unrecouped positions.
- Audits — responding to artist-side audit requests and conducting rights-holder audits where appropriate.
- Financial reporting — label P&L, unit economics, cash-flow forecasting.
- **Key deliverables (v2+):** Royalty statements; recoupment ledgers; financial reports; audit responses.
- **Hand-offs (v2+):**
  - **From Distribution & Digital Strategy:** DSP sales / streaming data.
  - **From Legal & Business Affairs:** executed contracts defining share splits and advance terms.
  - **From Marketing & Promotion:** campaign cost data.
  - **To Artist Relations:** statements and recoupment status for artist communication.

### 7.8 Artist Relations

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

### 7.9 Sync Licensing (aspirational, NEW in v1.1)

- **Function:** Place the label's catalog in film, TV, advertising, and video games. Adjacent-revenue engine. **Aspirational** — no active sync pitching today.
- **Current state (v1.1):**
  - Aspirational. No active sync pitching today.
  - **Open path (NEW in v1.1):** Wagner is open to moving publishing rights to a third-party publishing administrator that can actively place music in film/TV/ad placements.
  - **Catalog assets available for sync (NEW in v1.1):** Current active roster (Wágner, Velvut, DJ Farra, Sobralenses) + historical BEG catalog (30+ albums across 4 sub-imprints — Beloved Recordings, Yum Recordings, Updego Entertainment, Beloved Soundtracks). Instrumental cuts, alternate mixes, and stems availability varies by release.
  - **v2 trigger (NEW in v1.1):** Activate sync pitching if a publishing-administration partnership is signed.
- **Future-state primary responsibilities (v2+):**
  - Catalog pitching — proactive pitching to music supervisors, ad agencies, trailer houses, game studios.
  - Brief response — answering inbound briefs from supervisors.
  - License negotiation — drafting and negotiating sync licenses within policy.
  - Catalog metadata — keeping sync-friendly metadata current (instrumental versions, stems, alt mixes, BPM, mood tags).
  - Reporting — tracking placements, license fees, and revenue.
- **Key deliverables (v2+):** Sync pitch decks; executed sync licenses; sync metadata packages; placement reports.
- **Hand-offs (v2+):**
  - **From Legal & Business Affairs:** confirmed master and publishing rights availability.
  - **From Studio (Recording & Engineering):** sync-friendly versions (instrumentals, stems) when available.
  - **To Royalties & Finance:** sync license fees for revenue accounting.

### 7.10 Operations / Label Management

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
  - **To the Principal (wgnr.ai President Wagner dos Santos):** operating reports and cross-department decisions.
  - **To every department:** budget approvals and release calendar changes.

## 8. Release lifecycle workflow

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

### 8.1 Stage-by-stage

1. **A&R signs** — A&R identifies and signs an artist. Legal finalizes the contract (including the Suno-role clause per §7.1). Artist Relations picks up the relationship.
2. **Studio records** — Studio (Recording & Engineering) executes the recording project per the A&R brief. **Active only for human-recorded artists (Velvut, Wágner).** AI-generated releases (DJ Farra, Sobralenses) skip Studio; the master is downloaded directly from Suno per §5.4. Final masters, metadata, and artwork are produced (or downloaded).
3. **Marketing plans** — Marketing & Promotion builds the release campaign in coordination with Publicity. Distribution confirms the release date and pre-save mechanics via DistroKid.
4. **Distribution delivers** — Distribution & Digital Strategy uploads masters to **DistroKid** (sole distributor since 2023) on the agreed date. DistroKid handles delivery to all reachable DSPs.
5. **Royalties accrues** — Royalties & Finance begins accruing streaming / sales data from the DSPs (via DistroKid reporting). Future-state — see §7.7.1 for current-state rationale.
6. **Publicity amplifies** — Publicity / PR coordinates press coverage, interviews, and editorial pitching around the launch and post-launch window.
7. **Artist Relations sustains** — Artist Relations handles the ongoing artist relationship through the post-release period, including tour coordination, check-ins, and statement communication.

### 8.2 Cross-stage coordination

Marketing, Publicity, and Distribution must coordinate the launch window as a single synchronized moment. Operations / Label Management owns the calendar. Royalties & Finance joins the standup once DSP data starts flowing.

## 9. Open questions (for Wagner to resolve before v2)

1. **Music Publishing Administration as 11th department** — Should WGNR Sounds Music Publishing (the ASCAP-registered sub-entity, see §4.5 + §7.5) be promoted to its own department, or remain documented under Legal & Business Affairs? v1.2 default: documented under Legal & Business Affairs (one canonical sub-entity reference rather than two parallel departments). **Rationale for keeping under Legal & Business Affairs:** the publishing sub-entity has no functional operations distinct from Legal & Business Affairs in v1.2 scope; it exists as a legal-entity reference for rights administration. If a v2 publishing-administration partnership activates (per §7.9), this may need to be re-evaluated.
2. **Roster website update ownership** — Should A&R own the website roster page rebuild, or Marketing? (Likely Marketing for the page itself; A&R for the canonical roster source-of-truth.)
3. **Suno profile ownership** — Should Marketing maintain the Suno profile alongside DSP profiles, or treat Suno as a separate channel owned by Distribution? (Suno = source of masters for AI-generated releases per §5.4, so Distribution may be the natural owner.)
4. **BEG catalog treatment on DSPs** — Are the historical BEG releases (30+ albums across 4 sub-imprints, 1995–2002) currently on DSPs via DistroKid, or only on original physical/digital format from 1995–2002? Affects Sync Licensing catalog scope (§7.9).
5. **Real-world roster size at v2 kickoff** — How many artists are signed at v2 kickoff? Drives agent-profile concurrency assumptions.
6. **Sync priorities** — If sync activates (per §7.9), which verticals matter most: film / TV / advertising / video games / all? Drives Sync Licensing agent scoping.
7. **Royalty accounting cadence** — When Royalties & Finance activates (v2+), what cadence: quarterly, semi-annual, annual?
8. **Catalog prefix** — What is the internal label catalog prefix used for release IDs? (Currently `WGNR_SOUNDS_CATALOG_PREFIX` placeholder in `variables.env`.)
9. **Timezone for release calendar** — What is the label's home timezone for release-day alignment? (Currently `UTC` placeholder.)
10. **Brand-adapter layer** — If a future WGNR Sounds UI must visually coexist with wgnr.ai surfaces (e.g., a shared dashboard), how is the brand boundary preserved at the visual layer? Today's active brand source is the wgnr.ai guide, so direct token use is consistent; once the Sounds guide ships, an explicit brand-adapter layer may be required (see §4.2 + §4.6).
11. **wOS activation** — Should the v2 project wire `wgnr_ai_os` plugin instructions into `.a0proj/instructions/`? v1.2 deliberately does not; this is a v2 activation decision.
12. **Git remote** — Should the project be published to a new `github.com/wgnr-ai/wgnr_sounds_label.git` repo? v1.2 is local-only pending Wagner's review.
13. **WGNR Sounds brand-guide creation trigger** — When does Wagner plan to author a dedicated WGNR Sounds brand guide (vs. continuing to use the shared wgnr.ai guide)? Drives the §4.2 activation pathway.

## 10. Out of scope (v1.2)

v1.2 ships only the project skeleton, the corrected PRD, and the brand assets scaffold. The following are explicitly out of scope and deferred:

- **Agent profiles** for any of the 10 departments (`.a0proj/agents/` is intentionally empty).
- **Skills and skill scaffolding** (`.a0proj/skills/` is intentionally absent).
- **Plugin configurations** (`.a0proj/plugins/` is intentionally absent).
- **Working simulation** — no sample catalog data, no mock releases, no test DSP uploads.
- **Direct DSP integration code** — DistroKid is the sole integration point; no Spotify/Apple/Tidal API code.
- **Royalty accounting automation** — no calculation engine ships.
- **Contract templates** — Legal & Business Affairs is a functional domain only.
- **Sync placement tooling** — Sync Licensing is aspirational; no pitch-deck templates or outreach sequences ship.
- **WebUI / dashboard / app work** — no UI components ship.
- **Dedicated WGNR Sounds brand-guide PDF** — the active brand source is the shared wgnr.ai guide (per §4.1); a Sounds-specific guide ships later per §4.2.
- **Podcast operations** — podcast is a separate project (`wgnr_sounds_podcast`).
- **BEG catalog re-release** — historical catalog documented in §6.2 but not migrated to DSPs.

## 11. References

- `/a0/usr/projects/wgnr_ai_sysop/prds/PRD-wgnr-task-manager.md` — PRD format reference (TL;DR, AI-Readable Block, problem statement, goals / non-goals, traceability).
- `/a0/usr/projects/wgnr_ai_sysop/docs/projects-guide.md` — project structure and `project.json` schema reference.
- `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-logos/` — wgnr.ai parent-brand logo PNG variants (NOT the WGNR Sounds label logo; WGNR Sounds logos live at `docs/brand-assets/wgnr-sounds-logos/`).
- `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-brand-guide.pdf` — wgnr.ai parent-brand guide, also serving as the **active brand source for WGNR Sounds** until a dedicated Sounds guide ships (shared-until-dedicated rule per §4.1).
- `docs/brand-assets/` — WGNR Sounds brand assets folder (4 logos dropped by Wagner on 2026-08-30 + brand-guide PDF placeholder sentinel).
- `/a0/usr/projects/wgnr_ai_sysop/prompt_includes/ai-readable-document-pattern.promptinclude.md` — AI-Readable Block convention used in this PRD.

## 12. Closeout checklist

- [x] AI-Readable Block present (Scope, Must-include, Must-not-compress, Counter-prompt), updated for v1.2 corrections (shared-until-dedicated rule + path refresh).
- [x] TL;DR paragraph ≤ 200 words.
- [x] Problem statement with source attribution (Wagner 2026-08-30 + v1 corrections) and updated G5 casing.
- [x] Goals numbered (G1–G11) with G5 explicitly noting shared-until-dedicated rule.
- [x] Non-goals numbered (NG1–NG11) and explicitly call out v1.2 scope boundaries.
- [x] Brand identity section corrected: **division of wgnr.ai** (NOT sister-entity); §4.1 documents active wgnr.ai brand guide; §4.4 reverses v1.1 non-inheritance rule; Music Publishing sub-entity documented (§4.5).
- [x] Operating model with department grouping, decision rights, and §5.4 Suno Integration matrix.
- [x] §6 Roster & Catalog: 4 active artists (§6.1) + BEG historical catalog with 4 sub-imprints (§6.2) + roster reconciliation (§6.3); BEG legal status updated to fictitious name under wgnr.ai, LLC.
- [x] Department catalog with function / responsibilities / deliverables / hand-offs for each of the 10 departments, with §7.3 DistroKid pipeline, §7.5 Music Publishing, §7.6 Studio scope, §7.7 future-state Royalties, §7.9 aspirational Sync.
- [x] Release lifecycle as a 7-stage sequence (updated §8.1 for Suno-pipeline bypass at Stage 2).
- [x] Open questions enumerated individually (13 items, including new ones for Music Publishing-as-11th-dept, Roster website ownership, Suno profile ownership, BEG catalog DSP status, brand-guide creation trigger).
- [x] Out-of-scope section listing what v1.2 does NOT include (NG9 updated: dedicated WGNR Sounds brand-guide PDF deferred; shared wgnr.ai guide is the active source).
- [x] References with absolute paths to canonical supporting files (including `docs/brand-assets/` for Sounds-specific assets and `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE` for the active shared guide).
- [x] DOX closeout: root `AGENTS.md`, `prds/AGENTS.md`, `docs/AGENTS.md`, `docs/brand-assets/AGENTS.md` updated for v1.2 changes.

---

## 13. v1.2 changelog

| Change | Type | Details |
|---|---|---|
| Shared-until-dedicated brand-guide rule (NEW in v1.2) | Correction | Replaces v1.1's brand non-inheritance rule. Until WGNR Sounds ships its own dedicated brand guide, the **wgnr.ai brand guide is the active source** for color and typography tokens. Active path: `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-brand-guide.pdf`. Exposed via `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE` env var. §4.1 + §4.4. |
| §4 brand-identity rewrite | Reframe | §4 reorganized into 6 subsections (4.1 active guide, 4.2 future guide, 4.3 logo assets, 4.4 color tokens, 4.5 Music Publishing, 4.6 cross-reference handling). Documents the brand-guide sharing rule + dedicated-guide creation pathway. |
| Casing sweep across all files | Correction | ~30 instances corrected: `division of WGNR` → `division of wgnr.ai`, `WGNR, LLC` → `wgnr.ai, LLC`. Preserves label name `WGNR Sounds`, sub-entity name `WGNR Sounds Music Publishing`, project display name `WGNR Sounds Record Label`, env-var naming `WGNR_SOUNDS_*`. Per Wagner 2026-08-30 brand-name casing directive. |
| Brand-asset path refresh | Correction | `.a0proj/knowledge/client-assets/wgnr-sounds-assets/` → `docs/brand-assets/`. Wagner's manual edit (2026-08-30) moved the assets to `docs/brand-assets/wgnr-sounds-logos/` (4 PNGs) and `docs/brand-assets/wgnr-sounds-brand-guide.pdf.gitkeep` (placeholder). The old path is no longer scaffolded. |
| `.a0proj/project.json` instructions field rewrite | Correction | v1's stale framing (`sister entity`, wrong asset path, 11-dept count) replaced with v1.2-correct content: division-of-wgnr.ai framing, 10 departments, active shared brand guide path, DistroKid, ASCAP Music Publishing. Description field also updated. |
| `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE` env var | New | Added to `.a0proj/variables.env`. Points to the shared wgnr.ai brand guide PDF. Used by the §4.1 + §4.4 active-source rule. |
| `docs/brand-assets/AGENTS.md` | New file | DOX contract for the brand-assets subtree — documents the active-source brand guide rule, the logo inventory, and the placeholder handling protocol. |
| `docs/brand-assets/README.md` rewritten | Update | Inventory reflects 4 PNG logos dropped by Wagner + brand-guide PDF placeholder sentinel. Documents the shared-until-dedicated rule for downstream readers. |
| Root `AGENTS.md` `## Brand Non-Inheritance Rule` section | Replaced | Replaced with `## Brand Identity (Shared-Until-Dedicated Rule)` documenting the v1.2 active-source policy in 5 numbered points. |
| `prds/AGENTS.md` `## v1.1 Brand Framing` section | Renamed + updated | Renamed to `## v1.2 Brand Framing`; updated to reference `docs/brand-assets/` and the active shared wgnr.ai guide. |
| `docs/AGENTS.md` brand-rule references | Updated | Local Contracts line updated to reference v1.2 shared-until-dedicated rule (was brand non-inheritance rule). Open Question §3 reference updated (Royalty cadence §7). |
| `README.md` brand section + Conventions | Updated | Reflects v1.2 shared-until-dedicated rule; brand-asset path corrected to `docs/brand-assets/`; historical catalog legal-status updated to wgnr.ai, LLC. |
| BEG catalog legal-status update | Correction | §6.2 — fictitious name under `wgnR, LLC` → `wgnr.ai, LLC` per Wagner's casing directive. |
| §11 References update | Update | Added `docs/brand-assets/` reference; clarified wgnr.ai brand-guide PDF serves dual role (wgnr.ai parent + active Sounds guide). |
| Open Question §13 added | New | When does Wagner plan to author a dedicated WGNR Sounds brand guide? Drives the §4.2 activation pathway. |
| AI-Readable Block update | Update | Must-include elements + counter-prompt updated for v1.2: shared-until-dedicated rule, `docs/brand-assets/` path, `WGNR_SOUNDS_ACTIVE_BRAND_GUIDE` env var, lowercase `wgnr.ai` parent-brand references. |

## 14. v1.1 changelog

| Change | Type | Details |
|---|---|---|
| Brand relationship: peer-entity → division of WGNR | Correction | Per Wagner's verification of wgnrsounds.com tagline. The framing was corrected from peer-entity to division-of-WGNR (parent-child). (v1.2 corrects the casing to **division of wgnr.ai**.) |
| Brand assets location: sysop project → local project | Correction | Brand assets scaffolded at `/a0/usr/projects/wgnr_sounds_label/docs/brand-assets/` (originally at `.a0proj/knowledge/client-assets/wgnr-sounds-assets/` per v1.1; refreshed in v1.2). Subfolders `wgnr-sounds-logos/` (4 PNGs dropped by Wagner on 2026-08-30) and `wgnr-sounds-brand-guide.pdf.gitkeep` placeholder + handoff README. |
| WGNR Sounds Music Publishing sub-entity added | New section | §4.5 + §7.5 — ASCAP-registered, owned by WGNR Sounds, distinct from the recording label, administers publishing rights. Documented under Legal & Business Affairs (NOT a separate department). |
| Department count: 11 → 10 | Reconciliation | v1's `prds/AGENTS.md` and root `AGENTS.md` references to "11-department catalog" corrected to 10. The original 10-vs-11 ambiguity in v1 was a miscount of the user-supplied list; v1.1 confirmed 10 departments. (v1.2 preserves this correction.) |
| DistroKid as sole distributor | Update | §7.3 + §8.1 — generic DSP language replaced with **DistroKid (sole distributor since 2023)**. Mechanical rights via DistroKid / MLC. NG4 updated from "NO distribution partner integrations" to "NO direct DSP integration code". |
| Per-artist Suno role matrix | New section | §5.4 + §7.1 + §7.3 + §7.5 + §7.6 + §8.1 — DJ Farra + Sobralenses = 100% AI-generated (Suno = source of masters); Wágner + Velvut = Suno-assist only (human-recorded pipeline). |
| Active roster | New section | §6.1 — 4 active artists: Wágner, Velvut, DJ Farra, Sobralenses. |
| BEG historical catalog | New section | §6.2 — Beloved Entertainment Group 1995–2002, NYC-based, 30+ albums, 4 sub-imprints (Beloved Recordings, Yum Recordings, Updego Entertainment, Beloved Soundtracks), breakthrough "Ska: The Third Wave" compilation, strategic partnerships (Dinemec Records, Crane Mountain Records), historical independent artists (Buzz Prophets, Nerve), legal status as fictitious name under wgnr.ai, LLC. (v1.2 corrects the casing from WGNR, LLC.) |
| Royalties reframed as future-state | Reframe | §7.7 — v1 framed Royalties as a fully active department. v1.1 explicitly documents current state (no tooling, volumes insignificant), future-state activation trigger (volumes grow + partnership activations), and publishing-side royalty flow (via WGNR Sounds Music Publishing + ASCAP). |
| Sync Licensing reframed as aspirational | Reframe | §7.9 — v1 framed Sync as a fully active department. v1.1 explicitly documents current state (aspirational, no active pitching), the open path (Wagner is open to a third-party publishing administrator), the catalog assets available (active roster + BEG 30+ albums), and the v2 trigger (publishing-administration partnership signed). |
| Roster reconciliation requirement | New section | §6.3 — wgnrsounds.com is out of date; the canonical roster is the union of website + Suno. A&R owns reconciliation in v2. |
| Studio scope clarified | Update | §7.6 + §8.1 — Studio is active only for the human-recorded pipeline. AI-generated releases (DJ Farra, Sobralenses) bypass Studio and source masters directly from Suno. |
| Podcast project name | Update | NG10 — `wgnr_sounds_podcast` is a separate project; podcast operations are out of scope for this PRD. |
| Open Questions rewritten | Update | §9 — 12 enumerated questions including new Music Publishing-as-11th-dept question, Roster website ownership, Suno profile ownership, BEG catalog DSP status. Resolved questions removed (department count, distribution partner, sync priorities, royalty cadence, podcast name). |
| AI-Readable Block updated | Update | Must-include elements and counter-prompt updated to reflect v1.1 corrections (division-of-WGNR framing, BEG sub-imprints, per-artist Suno role, DistroKid year, ASCAP Music Publishing). |
