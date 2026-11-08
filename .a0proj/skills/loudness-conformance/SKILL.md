---
name: loudness-conformance
description: Mastering methodology for WGNR Sounds human-recorded pipeline (Velvut + Wágner), embodying Bob Ludwig's approach — dynamics are the punch, transient preservation over level, minimal justified processing, ears-first whole-song assessment, loudness-war resistance. Carries the Velvut delivery target (-14 LUFS / -1.0 dBTP / LRA 6-10 LU), true-peak discipline, and the punch doctrine (limit gain reduction, protect transients). Applies to master-engineer (Studio). Reference: docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md §9.
trigger_phrases:
  - "loudness conformance"
  - "bob ludwig mastering"
  - "master engineer protocol"
  - "punchy master"
  - "transient preservation"
  - "true peak discipline"
---

# loudness-conformance — Label-Specific Skill

> **Scope:** Mastering methodology for the WGNR Sounds human-recorded pipeline (Velvut + Wágner). Embodies Bob Ludwig's mastering philosophy fused with the project's GarageBand guide §9 delivery spec.
> **Applies to:** master-engineer agent (Studio)
> **Reference:** docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md §9 (Final mix and mastering)
> **Owner:** Wagner dos Santos (Principal) — WGNR Sounds Record Label
> **Created:** 2026-11-08 (v1.0.0) — resolves the dangling `skills_enabled` reference in the master-engineer profile

## Purpose

1. **Embody Ludwig's methodology** — punch from dynamics, transient preservation over level, minimal justified processing, loudness-war resistance.
2. **Operationalize guide §9** — the Velvut target (-14 LUFS / -1.0 dBTP / LRA 6-10 LU), GR budgets, master-against-the-chorus, the §9.2 gate, §9.7 delivery spec.
3. **Give the master-engineer a decision doctrine** — not just settings, but when to REMOVE a stage (minimalism is a Ludwig move).
4. **Preserve the rejection gate** — the §9.2 gate and no-remix clause live in the role, not here; this skill never weakens them.

## The Lineage (stated correctly)

Bob Ludwig — American mastering engineer; career stops at A&R Recording and **Sterling Sound** (where he served as VP), then Masterdisk; founded **Gateway Mastering & DVD (Portland, Maine, 1993)**, the studio he is most associated with. Career spans Led Zeppelin catalogue remasters, The Rolling Stones, Bruce Springsteen, Rush, Daft Punk's *Random Access Memories*. The Principal referenced "Bob Ludwig from Sterling Sound" — the persona is Ludwig's methodology; the lineage note keeps the history straight.

## Ludwig Doctrine — Five Pillars

| Pillar | Principle | Operational Translation |
|---|---|---|
| **1. Dynamics ARE the punch** | Loudness comes from level; punch comes from transients surviving | Peak limiter GR budget **≤3 dB** (hard ceiling 4 per guide §9.4); slower limiter attack lets transients through; measure PLR (peak-to-loudness ratio) on the final chorus block to PROVE punch |
| **2. Loudness-war resistance** | A louder master is turned DOWN by normalization; dynamics survive it | -14 LUFS target is a landing zone, not a maximum. If gaining to exactly -14 pushes GR past budget, land short and LOG the deviation — normalization absorbs it; crushed transients do not come back |
| **3. Less is more** | Every processing stage must justify itself; removing a stage is a valid move | Start from the previous chain and interrogate each stage: is it earning its passband? A bypassed glue compressor with a logged reason is MORE Ludwig than a 2 dB reduction applied on doctrine |
| **4. Ears first, whole song** | Ludwig listens start-to-finish before touching anything | The agent analog: full-file analysis pass FIRST (integrated/short-term LUFS, per-band energy, crest/PLR, mono fold) before designing any chain; master against the chorus, verify the verse still breathes (§9.6) |
| **5. Consistent measurement** | Same meter battery every time; numbers, never impressions | ebur128 + astats + ffprobe on the ACTUAL rendered file, every run: Integrated LUFS, True Peak dBTP, sample peak, LRA, plus section PLR (chorus) and verse/chorus short-term delta. State measurements, never estimates |

## The Punch Doctrine (how to make a master punchier, Ludwig-style)

Punch levers, in order of preference:

1. **Reduce limiter GR** — gain-stage down until peak GR sits ≤3 dB. This is the #1 punch move; it costs integrated LUFS and that trade is correct.
2. **Slow the limiter attack** (5 ms → 10-12 ms where the tool allows) with asc smoothing — lets drum transients poke through before limiting engages.
3. **Lighten or remove glue compression** — double-compression is a transient killer. If the mix's bus rides (automation) already carry the dynamics, the glue stage may deserve bypass — log the call either way.
4. **Tighten, don't boost, the low end** — a clean 30 Hz HPF and mud-band discipline reads as punch; added low-end level reads as flab.
5. **Never** chase punch with more output gain. That is the loudness war, and it loses on every DSP.

## Chain Discipline (guide §9.5, Ludwig-filtered)

- Corrective EQ: HPF 30 Hz; cuts only where measured (band RMS evidence), never on doctrine.
- Tonal EQ: the 10 kHz one-place rule from the mix protocol governs — if the mix carries vocal-only air, the master shelf is ZERO and that is the correct call.
- Glue: 2:1, 2-3 dB per §9.5 — but pillar 3 allows a logged bypass when GR budget or LRA floor demands it. Guide §9.6 outranks the recipe: accept the wider LRA.
- Saturation: 1-2 dB density max; the last 5%, nothing more.
- Limiter: ceiling from a MEASURED TP sweep on this material (HF-dense music overshoots its sample ceiling ~1+ dB); GR budget per pillar 1.
- Meter the result: all three numbers + section PLR, on the file.

## Hard Boundaries (mirror the role; never weakened here)

- **Rejection right and no-remix clause live in the role prompt.** This skill adds methodology; it never removes authority.
- Never invent key/tempo/time signature — UNVERIFIED unless measured and labeled as measured.
- Never write to .band bundles. Stems are read-only.
- True peak governs (report sample peak too). Zero samples over 0 dBFS.
- One master, all platforms. No per-DSP variants.
- LRA floor 6 LU is a delivery requirement — punch moves that widen LRA are safe; moves that narrow it toward the floor are not.

## Deliverable Additions (on top of the role's master report)

| Section | Required Content |
|---|---|
| **Punch Evidence** | Final-chorus PLR / crest factor, input vs output; limiter peak GR; glue GR or logged bypass reason |
| **Stage Justification** | One line per chain stage: kept/removed and why (pillar 3) |
| **Ludwig Deviation Log** | Any place the recipe lost to the target it serves (e.g., GR budget vs -14.0 exact) |

## References

- docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md §9 (governing spec)
- Ludwig methodology sources: publicly documented interviews and profiles (Sonic Scoop, Tape Op, press coverage of Gateway Mastering); doctrine pillars synthesized 2026-11-08
- dev-ticket origin: 2026-10-30 brief (mix-master-producer role split), this skill created 2026-11-08 per Principal direction ("Bob Ludwig persona, punchier masters")
- Sister skill: `stem-mix-protocol` (Andy Wallace doctrine, mix side)

---

*Created 2026-11-08. Mirrors the SKILL.md house standard; resolves the dangling `loudness-conformance` reference in `.a0proj/agents/master-engineer/agent.yaml`.*
