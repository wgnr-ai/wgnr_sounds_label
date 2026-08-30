# prds

## Purpose

Product Requirements Documents for the WGNR Sounds Record Label project. Each PRD is a build contract for an AI agent (or human) to build, integrate, or operate a capability on the label's operational backbone.

## Ownership

- Owned by: WGNR Sounds Label project
- Authored by: wgnr.ai Ops (orchestrator)
- Curated by: Wagner dos Santos (Principal)
- PRDs are written for AI agent understanding — detailed, executable, and concrete (exact paths, function signatures, acceptance criteria).

## Local Contracts

- Naming: `PRD-<topic>.md` (hyphen-separated topic; lowercase).
- Each PRD carries: title, version, date, status, author, owners, AI-Readable Block, TL;DR, problem statement, goals & non-goals, identity/brand, operating model, department catalog, release lifecycle, open questions, out of scope, references, DOX closeout checklist.
- Status lifecycle: Draft → Approved → In-Build → Shipped → Archived.
- Every change to a shipped feature requires a new PRD version (do not rewrite history; append a new version section).
- Cross-references between PRDs use relative paths from `/a0/usr/projects/wgnr_sounds_label/`.
- Departments appear in PRDs as **functional domains**, not agent profiles. Agent profile scaffolding is a separate activity (deferred to v2).

## v1.2 Brand Framing

WGNR Sounds is a **division of wgnr.ai** (parent-child relationship). The PRD references:

- The local brand assets path at `docs/brand-assets/` (Wagner dropped 4 logos on 2026-08-30; brand-guide PDF placeholder still pending).
- Until a dedicated WGNR Sounds brand guide ships, the **wgnr.ai brand guide is the active brand source** at `/a0/usr/projects/wgnr_ai_sysop/.a0proj/knowledge/client-assets/wgnr-assets/wgnr-brand-guide.pdf` (shared-until-dedicated rule per PRD §4).
- WGNR Sounds Music Publishing (ASCAP-registered sub-entity) documented under §7.5 Legal & Business Affairs.
- DistroKid as the sole distributor since 2023 (§7.3).
- The per-artist Suno role matrix (§5.4) — DJ Farra + Sobralenses are 100% AI-generated; Wágner + Velvut are Suno-assist only.
- The active roster (§6.1) and the historical BEG catalog (§6.2).

## Work Guidance

- New PRDs go in this folder, not `docs/` (which is for governance + research notes).
- Prefer concrete handles over adjectives ("60-day recoupment window", not "reasonable recoupment").
- Keep each PRD ≤ 20k chars unless complexity demands more.
- Label every specific claim: VERIFIED-FACT (cited) / SYNTHESIS-JUDGMENT / UNVERIFIED-CLAIM.
- Brand references use the **wgnr.ai brand guide** as the active source for color and typography tokens (shared-until-dedicated rule per PRD §4). The WGNR Sounds brand guide, when it ships, will supersede the shared one for Sounds-specific visuals.

## Verification

- `ls prds/` lists PRDs; this AGENTS.md child index matches.
- Each PRD's §1 TL;DR is one paragraph (≤ 200 words).
- Each PRD has an AI-Readable Block immediately after the title (Scope, Must-include, Must-not-compress, Counter-prompt).

## Child DOX Index

| Path | Scope |
|---|---|
| `PRD-wgnr-sounds-label.md` | v1.1 foundation PRD — label identity (division-of-WGNR framing), operating model, 10 canonical departments, per-artist Suno role matrix, DistroKid distribution pipeline, WGNR Sounds Music Publishing sub-entity, active roster + BEG historical catalog, release lifecycle, open questions |
