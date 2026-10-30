---
title: Brief — Mixing Engineer, Mastering Engineer, Producer agent profiles
type: brief
status: open
created: 2026-10-30
last_updated: 2026-10-30T19:02:00-04:00
owner: wgnr-sounds-captain
principal: Wagner dos Santos
handoff_to: wgnr_ai_sysop
tags:
  - brief
  - pre-prd
  - agents
  - wgnr-sounds
  - mixing
  - mastering
---

# Brief: Mixing Engineer, Mastering Engineer, Producer (pre-PRD)

> **From:** Wagner dos Santos (Principal), via wgnr-sounds-captain
> **To:** wgnr_ai_sysop project team
> **Date:** 2026-10-30
> **Status:** OPEN — pre-PRD brief, handoff for agent-profile construction
> **Deliverable back to:** `wgnr_sounds_label/.a0proj/agents/` (three new profiles) + validation report

---

## 1. The Assignment

Build three agent profiles inside the **wgnr_sounds_label** project:

| Profile key | Display name | Department home |
|---|---|---|
| `mix-engineer` | Mixing Engineer | Studio |
| `master-engineer` | Mastering Engineer | Studio |
| `producer` | Producer | Studio / A&R boundary |

All three **report to `wgnr-sounds-captain`** (the project's orchestrator). They are peers, not a chain — the Producer directs, the Mixing Engineer mixes, the Mastering Engineer masters, and none of them absorbs another's mandate.

This is a **pre-PRD brief**. SysOp's job is to determine how these three become real profiles (prompt design, tool surface, skill authoring, plugin needs) and to feed back what is feasible. The label project will write the governing PRD section afterward.

---

## 2. Why Three And Not One — The Evidence Case

This is not a headcount request. It comes from a **documented failure on 2026-10-30**, when the orchestrator performed mixing and mastering in a single pass on Velvut's *Sad Song* stems.

**What went wrong, in order:**

1. **No creative panning at all.** Every element landed dead center. The chain contained `pan=mono` (a technical bass mono-sum) and nothing else. A guitar-less industrial arrangement creates width by placement; leaving it mono-centered is a real sonic defect.
2. **Static mix.** EQ and compression only. No reverb sends, no gating, no sidechain, no modulation — despite the project's own mix guide documenting all four.
3. **Mono collapse.** The bass mono-sum stage collapsed the entire mix to one channel; shipped as a mono master until caught.
4. **Clipping, then inter-sample overshoot.** A rebuild peaked at 0.00 dBFS, was fixed, then measured **+0.05 dBTP true peak** — a defect invisible to sample-peak meters and only audible after lossy encode.
5. **The structural failure:** when the master showed `LRA 4.0` (out of spec), the orchestrator **went back into the mix and fixed a mix defect at the mastering stage.** It got away with it because it happened to notice.

Item 5 is the argument. A mastering engineer cannot fix the mix — their mandate is *reject and return*. When one agent holds both roles, the rejection gate silently disappears and upstream defects get patched downstream instead of being sent back for repair. **Separation of powers is the quality mechanism**, not the org chart.

---

## 3. Role Definitions

### 3.1 `mix-engineer` — Mixing Engineer

**Owns:** the mix. Stems in, mixdown out.

- Gain staging, bus architecture, the stereo field (panning and depth), EQ, compression, gating, sidechain dynamics, modulation, reverb/delay sends, saturation, automation.
- Creative placement: what sits where in the stereo field and why.
- Delivers a **mixdown (24-bit WAV) plus a mix report** — what was done, what was measured, what was deliberately left alone.
- **Cannot master.** Cannot apply the final delivery loudness target. Cannot make the master louder to fix a mix problem.
- **Must state** integrated LUFS, true peak, and LRA of its own mixdown before handing off.

### 3.2 `master-engineer` — Mastering Engineer

**Owns:** the master. Mixdown in, distribution-ready master out.

- Runs the **§9.2 stop-condition gate** from `docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md`.
- **Has explicit authority to REJECT a mixdown and return it** with named defects. This authority is the point of the role and must be written into the prompt as a hard right, not a suggestion.
- Final chain: corrective EQ, tonal EQ, glue compression, saturation, limiting, delivery format, true-peak verification.
- Delivers a **master (24-bit WAV) plus a mastering report** proving spec compliance.
- **Cannot re-mix.** If the mix is wrong, the answer is *return it*, never *fix it here*.

### 3.3 `producer` — Producer

**Owns:** the creative direction of the record — not the technical execution.

- Sets arrangement and sonic intent before a mix begins: reference tracks, target feel, what the song is trying to do.
- Adjudicates disputes between mix and master (e.g. "the mix is over-compressed for the dynamic target" → Producer decides whether to re-mix or accept a narrower LRA).
- Guards the **artist's creative intent** against technical convenience. Speaks for Velvut's documented style when the engineers optimize for spec instead of for the song.
- Does **not** operate a mix or master chain. Directs and adjudicates; does not execute.

**Boundary note:** Producer is distinct from `song-architect` (concept and blueprint, pre-production) and from `ar` (signing and taste-making). Producer starts where the blueprint ends and ends where the master ships.

---

## 4. Verified Environment (as of 2026-10-30 — re-verify at build time)

These were measured today on the Principal's Mac; SysOp should not re-derive them from assumption.

- **Host access is live:** `code_execution_remote` reaches the Mac (macOS 27.2, user `wgnr`).
- **GarageBand project root:** `~/Library/Mobile Documents/F3LWYJ7GM7~com~apple~garageband10/Documents/` — 21 `.band` bundles, 8.2 GB, organized by song.
- **Stem folders already exist** (e.g. `03-sad-song/sad-song-stems/` — Bass, Drums, Synth, Vocals as 48 kHz/16-bit stereo WAVs, sample-aligned).
- **ffmpeg:** `/opt/homebrew/bin/ffmpeg`, `/opt/homebrew/bin/ffprobe`. Includes `ebur128`, `loudnorm`, `stereotools`, `sidechaincompress`, `agate`, `aecho`, `afir`, `chorus`, `flanger`, `aphaser`, `acompressor`, `aexciter`, `adeclip`.
- **NOT available in this ffmpeg build:** `transient` (verified — count 0). Transient shaping needs another approach.
- **`projectData` is not safely editable** — it is an NSKeyedArchiver plist wrapping an opaque binary blob. No agent may write to a `.band` bundle. Read WAVs, never rewrite projects.

---

## 5. What Each Profile Needs (SysOp to design)

### Tools
- `code_execution_remote` (host shell on the Mac — the primary working tool for all three)
- `code_execution_tool` (container-side, for reports and vault writes)
- `text_editor` / `text_editor_remote`
- `call_subordinate` (so `producer` can direct the two engineers)
- `response`, `memory_load`, `memory_save`, `todo_tool`

### Skills to author (suggested, SysOp decides)
| Skill | Owner | Purpose |
|---|---|---|
| `stem-mix-protocol` | mix-engineer | Panning map, bus architecture, sidechain recipes, reverb strategy, per-genre placement |
| `loudness-conformance` | master-engineer | Two-pass loudnorm, true-peak vs sample-peak, LRA math, rejection criteria |
| `velvut-sonic-identity` | producer | The documented Velvut sound — what must not be optimized away |

Existing project skills relevant: `comfyui-video-pipeline` is unrelated; the Suno skills are upstream of this work.

### Plugins
SysOp's call. Likely candidates: an audio-analysis helper (LUFS/true-peak/spectral report as a tool rather than shell pipelines), and a render-queue plugin if batch catalog work is expected.

---

## 6. Hard Rules These Profiles Must Carry

1. **Never invent a key, tempo, or time signature.** Write `UNVERIFIED — not documented` and flag it.
2. **Never write to a `.band` bundle.** WAVs only.
3. **Master engineer's rejection right is absolute.** A mixdown that fails the stop-condition gate goes back.
4. **Master against the chorus, not the loudest sample.** Verify verse presence at low volume.
5. **True peak, not sample peak.** Report both; only dBTP ships.
6. **One master, all platforms.** No per-DSP variants.
7. **State measurements, never estimates.** Every loudness or peak claim comes from a meter read, not an impression.

---

## 7. Acceptance Criteria

SysOp's delivery is accepted when:

- [ ] Three profiles exist under `wgnr_sounds_label/.a0proj/agents/` with `agent.yaml`, `_context.md`, and `prompts/`, matching the structure of the existing 17 profiles.
- [ ] Each profile has a working `agent.yaml` that passes `scripts/validate_agent_yamls.py`.
- [ ] All three are registered in `.a0proj/agents.json` and reachable via `call_subordinate`.
- [ ] `producer` can dispatch to `mix-engineer` and `master-engineer`; neither engineer can dispatch to the other as a workaround.
- [ ] **Live test on real material:** `mix-engineer` takes the *Sad Song* stems and produces a mixdown with documented panning, at least one sidechain, at least one gate, and reverb sends. `master-engineer` runs the gate and either accepts to spec or rejects with named defects. Test passes if the handoff is honest — **a correct rejection counts as a pass.**
- [ ] Registry skill (`agent-registry`) updated so these profiles are discoverable.

---

## 8. Open Questions For SysOp

1. **Tool surface.** Is host shell the right primitive for mix work long-term, or should the audio-analysis logic move into a dedicated plugin tool? Shell pipelines are auditable but brittle to re-invent per song.
2. **Skill vs prompt.** Panning strategy and loudness conformance are long enough to be skills, short enough to be prompts. SysOp's call on which side of the line they land.
3. **Producer authority.** Should `producer` be able to *override* a mastering rejection, or only escalate to `wgnr-sounds-captain`? Recommend escalate-only — an override path recreates the exact failure this brief exists to prevent.
4. **Batch operation.** If the same chain runs across 22 projects, is a render-queue plugin warranted, or does per-song dispatch suffice?

---

## 9. Reference Material

- `docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md` — §5 mix chain, §9 mix/mastering/delivery (the governing spec the two engineers work to).
- `prds/PRD-wgnr-sounds-label.md` §13 — Creative Song-Production Layer.
- `.a0proj/agents/studio/` — existing department profile structure to match.
- `.a0proj/agents/AGENTS.md` — DOX contract for agent profile construction.

---

*Prepared 2026-10-30 by wgnr-sounds-captain for SysOp handoff. Every technical claim in §4 was measured on the host that day; re-verify at build time rather than trusting this document.*
