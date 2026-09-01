---
name: suno-prompt-compatibility-spec
description: Canonical Suno prompt format specification — what makes a prompt "verified Suno-compatible". Use this skill when generating Suno prompts to ensure output will produce a valid track in Suno's interface.
trigger_phrases:
  - suno prompt
  - suno compatible
  - suno format
  - suno tags
  - suno lyrics format
  - "[verse]"
  - "[chorus]"
  - "[bridge]"
  - suno style
  - suno genre
---

# suno-prompt-compatibility-spec — Label-Specific Skill

> **Scope:** Canonical reference for the Suno prompt format used by the WGNR Sounds suno-prompter agent. Defines what "verified Suno-compatible" means and provides the verification checklist the suno-prompter runs before emitting any Suno-ready prompt set.
> **Applies to:** suno-prompter (mandatory before emission); song-architect + lyricist (referenced for Suno-format conventions)
> **Reference:** PRD §5.4 (Suno Integration by Artist); suno.com platform docs
> **Owner:** Wagner dos Santos (Principal) — WGNR Sounds Record Label

## 1. Purpose

This skill exists to make the **"verified Suno-compatible"** claim auditable. The suno-prompter agent MUST run the verification checklist (§7) before emitting any Suno-ready prompt set; without this skill, the claim is unfalsifiable.

Why this matters for WGNR Sounds:
- The label ships both human-recorded (Velvut, Wágner) and AI-generated (DJ Farra, Sobralenses) tracks through DistroKid.
- Suno's prompt format is the upstream input for every AI-generated release and a critical ideation tool for every human-recorded release.
- Suno's interface and prompt conventions evolve; the skill body must be reviewed against the current Suno interface and updated when Suno's format changes.

> **Source-verification status (2026-08-30, v3.0.0 scaffold):**
> - §2 (Suno prompt anatomy), §4 (Lyrics formatting rules), §7 (Verification checklist): **documented from Suno help center conventions widely observed across the platform's documentation and help articles**. Confidence: HIGH for the structure (4 fields per prompt set). Confidence: MEDIUM for exact field-name spelling and any UI hints; recommend Wagner review against the current suno.com interface.
> - §3 (Genre tag vocabulary), §5 (Negative prompt rules), §6 (Per-artist role mapping): **observed from the wgnrsounds.com published catalog** + Suno's user-facing prompt examples in their help docs. Confidence: MEDIUM. UNVERIFIED claims are marked explicitly below; recommend Wagner verify against current Suno interface and the catalog.
> - §8 (References) lists the authoritative sources for re-verification.

## 2. Suno prompt anatomy

A Suno-ready prompt set has four fields. Each must be present.

| Field | Purpose | Required? |
|---|---|---|
| **Style prompt** (a.k.a. "Style of Music", "Tags") | Comma-separated genre + style + instrumentation + vocal style descriptors | YES |
| **Lyrics field** (a.k.a. "Lyrics") | Formatted lyrics with section labels | YES |
| **Title** | Track title (used for the generated output filename and metadata) | YES |
| **Negative prompt / exclusions** (a.k.a. "Exclude", "Exclude styles") | Comma-separated list of what to avoid in the generation | RECOMMENDED |

> **v3.0.0 deviation from a flat Suno input:** the wgnr_sounds_label suno-prompter emits a **structured markdown document** that maps cleanly to the four Suno fields above. Wagner (or the user) copies the four fields into suno.com's interface. The markdown format is a WGNR Sounds convention, not a Suno convention.

## 3. Genre tag vocabulary

> **Source-verification status:** MEDIUM. The genre vocabulary below is drawn from Suno's help-center examples and observed Suno outputs in the wgnrsounds.com catalog. Suno is permissive about genre tags; the list below is **non-exhaustive**. UNVERIFIED tags should be marked `UNVERIFIED` in the emitted prompt and reviewed by Wagner against the current Suno interface.

### 3.1 Canonical genre anchors (commonly observed, documented)

- `rock`, `pop`, `hip-hop`, `electronic`, `EDM`, `indie`, `alternative`, `jazz`, `blues`, `country`, `folk`, `metal`, `punk`, `ska`, `reggae`, `soul`, `R&B`, `funk`, `dance`, `house`, `techno`, `trance`, `ambient`
- `acoustic`, `electric`, `orchestral`, `symphonic`, `choral`, `a cappella`
- `lo-fi`, `chiptune`, `synthwave`, `vaporwave`, `retro`, `8-bit`

### 3.2 Effect / production descriptors

- `reverb`, `delay`, `distortion`, `overdrive`, `fuzz`, `phaser`, `flanger`, `chorus`
- `lo-fi`, `clean`, `polished`, `rough`, `punchy`, `warm`, `cold`, `bright`, `dark`
- `analog`, `tape`, `vinyl`, `lo-fi`, `hi-fi`
- `dry`, `wet`, `wide`, `narrow`

### 3.3 Vocal descriptors

- `male vocal`, `female vocal`, `duet`, `choir`, `harmonies`, `spoken word`, `rap`, `singing`, `humming`, `whisper`, `shout`, `falsetto`
- `raspy`, `breathy`, `smooth`, `gritty`, `ethereal`, `operatic`

### 3.4 Multi-tag combinations

Suno accepts comma-separated multi-tag combinations. WGNR Sounds is **multi-genre / eclectic**, so combinations like `ska, punk, horn section` or `EDM, house, female vocal, reverb` are appropriate.

### 3.5 UNVERIFIED tags (require Wagner verification before use)

- Any genre or effect tag not listed in §3.1-§3.3: emit as `UNVERIFIED: <tag>` and require Wagner to confirm against the current Suno interface before paste.

## 4. Lyrics formatting rules

> **Source-verification status:** HIGH for section-label conventions (documented in Suno help center and observed across thousands of Suno outputs).

### 4.1 Section labels (mandatory for "verified Suno-compatible")

Use bracketed section labels in the Lyrics field. The canonical labels Suno recognizes:

| Label | Use |
|---|---|
| `[Intro]` | Instrumental or vocal intro |
| `[Verse]` / `[Verse 1]` / `[Verse 2]` | Verse sections (numbered if multiple) |
| `[Pre-Chorus]` | Pre-chorus lift |
| `[Chorus]` | Chorus / hook section |
| `[Post-Chorus]` | Post-chorus tag |
| `[Bridge]` | Bridge (departure from verse-chorus structure) |
| `[Outro]` | Ending section |
| `[Instrumental]` / `[Instrumental Break]` | Pure-instrumental interlude |
| `[Break]` | Brief pause / break |
| `[Hook]` | Standalone hook |
| `[Spoken Word]` | Spoken (not sung) section |
| `[Skit]` | Skit / interlude |

### 4.2 Capitalization

Suno is case-insensitive for section labels, but the **convention** is `[Title Case]` (first letter capitalized, rest lowercase). Use this consistently.

### 4.3 Line breaks

- One blank line between sections.
- One lyric line per output line (do NOT wrap multiple lines into one output line).
- Empty sections (e.g., `[Instrumental]` with no following lines) are valid.

### 4.4 Metadata injection points

Suno does NOT support custom metadata tokens in the lyrics field. Title + any artist metadata goes in the Title field, NOT in the lyrics.

## 5. Negative prompt rules

> **Source-verification status:** MEDIUM. Suno's "Exclude" / negative-prompt feature is documented but the precise accepted syntax is observed from Suno outputs and the wgnrsounds.com catalog, not from a single authoritative source. UNVERIFIED claims are marked.

### 5.1 When to use a negative prompt

- When the track should be **instrumental only** (e.g., a backing track for a human-recorded release): emit `vocals, singing, spoken word` in the negative prompt.
- When a specific genre is unwanted but adjacent to the target: emit `<unwanted_genre>`.
- When the vocal style must be avoided: emit `male vocal` or `female vocal` (whichever is unwanted).

### 5.2 Negative-prompt format

Comma-separated list of tags to exclude. Same vocabulary as the Style prompt (§3).

### 5.3 UNVERIFIED claims

- The exact list of negative-prompt tags Suno recognizes is **NOT fully documented** publicly. UNVERIFIED: any tag that has not been observed in Suno outputs should be flagged.

## 6. Per-artist role mapping (per PRD §5.4)

The WGNR Sounds roster splits between two pipelines. The Suno role drives the prompt structure.

| Artist | Suno role | Prompt structure notes |
|---|---|---|
| **DJ Farra** | 100% AI-generated | Suno generates full track. Style prompt carries full instrumentation + vocal style + mood + arrangement. Lyrics field carries finished lyrics formatted per §4. Negative prompt typically empty or minimal. |
| **Sobralenses** | 100% AI-generated | Same as DJ Farra. |
| **Velvut** | Suno-assist only | Suno used for song-idea / concept testing. Style prompt may be exploratory; the production track is human-recorded in Studio, NOT from Suno. Negative prompt may include `polished, mastered, final` to discourage treating the Suno output as a release master. **Vocal identity (Principal-declared 2026-08-31): Wagner dos Santos — baritone male.** All Velvut work assumes baritone male vocals regardless of reference-track vocalist; style prompts use male-vocal descriptors, negative prompt excludes `female vocal`. |
| **Wágner** | Suno-assist only | Same as Velvut — including the baritone male vocal identity (Wagner dos Santos is the vocalist). |

**Critical:** the suno-prompter agent MUST emit the Suno role verdict in every prompt set, with rationale linking back to PRD §5.4.

## 7. Verification checklist (mandatory gate before emission)

The suno-prompter agent runs this checklist against its own output before emitting. If ANY check fails, the affected section is re-done; the prompt set is NOT emitted broken.

```
[ ] Style prompt present? (genre + style + instrumentation + vocal style)
[ ] Lyrics field present?
[ ] Lyrics field uses section labels per §4.1? ([Verse], [Chorus], [Bridge], etc.)
[ ] Section labels use Title Case per §4.2?
[ ] Lyrics have line breaks per §4.3?
[ ] Title field present?
[ ] Negative prompt present (recommended, even if empty)?
[ ] Suno role verdict present and consistent with blueprint (per PRD §5.4)?
[ ] UNVERIFIED tags flagged in §3.5 manner?
[ ] Per-artist prompt structure matches §6?
```

## 8. References

- **PRD §5.4 — Suno Integration by Artist** — canonical matrix for per-artist Suno role.
- **suno.com** — the platform. Suno's help center documents section-label conventions and basic prompt structure. (Public documentation is partial; the canonical source of truth is the current suno.com interface — review before each release.)
- **wgnrsounds.com published catalog** — observed Suno outputs for the DJ Farra + Sobralenses 100% AI releases. Reference for genre-tag combinations that have produced working tracks.
- **WGNR Sounds Music Publishing (ASCAP-registered)** — required rights-clearance context for any Suno-generated release; route via Legal & Business Affairs for license-term verification.

## 9. Maintenance

- **Owner:** Wagner dos Santos (Principal).
- **Update cadence:** review against current Suno interface at the start of every release cycle; update §3 (genre vocabulary) and §5 (negative-prompt rules) as Suno evolves.
- **Verification status:** MEDIUM at v3.0.0 scaffold. UNVERIFIED claims (marked explicitly above) require Wagner confirmation before being relied upon for releases.
- **Origin:** v3.0.0 — scaffolded 2026-08-30 as part of the Creative Song-Production Layer (PRD §13).

---

*Skill v3.0.0 — 2026-08-30 — Creative Song-Production Layer (v3.0.0) — owner: Wagner dos Santos*
