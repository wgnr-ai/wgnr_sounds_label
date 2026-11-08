---
name: stem-mix-protocol
description: Stem-based mixing protocol for WGNR Sounds human-recorded pipeline (Velvut + Wágner). Embodies Andy Wallace methodology — massive tight low-end, instrument clarity, SSL-style simplicity, dynamic fader automation, fast first drafts — fused with the project's GarageBand guide §5 specifics (tape saturation, parallel compression, restrained reverb, vocal chain order, 10 kHz conflict resolution). Applies to: Studio (Recording & Engineering), mix-engineer agent. Reference: docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md §5 + §9.
trigger_phrases:
  - "stem mix protocol"
  - "andy wallace mixing"
  - "mix engineer protocol"
  - "velvut mix chain"
  - "garageband mix"
---

# stem-mix-protocol — Label-Specific Skill

> **Scope:** Stem-based mixing protocol for the WGNR Sounds human-recorded pipeline (Velvut + Wágner). Fuses Andy Wallace's legendary mixing methodology with the project's GarageBand guide §5 specifics.
> **Applies to:** Studio (Recording & Engineering), mix-engineer agent
> **Reference:** docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md §5 (The mix chain) + §9 (Final mix and mastering)
> **Owner:** Wagner dos Santos (Principal) — WGNR Sounds Record Label

## Purpose

The WGNR Sounds label's human-recorded pipeline (Velvut + Wágner) requires a repeatable, documented mixing protocol that:

1. **Embodies Andy Wallace's methodology** — massive tight low-end, instrument clarity and separation, SSL-style console simplicity, dynamic fader automation over aggressive mix-bus compression, fast first drafts capturing raw energy.
2. **Operationalizes the GarageBand guide §5** — tape saturation on synth bus, parallel compression on drum bus, deliberately restrained reverb, vocal chain order with pitch correction first, 10 kHz conflict resolution.
3. **Enables the mix-engineer agent** to execute a mix with documented panning, at least one sidechain, at least one gate, reverb sends, and measurements — not improvisation.
4. **Preserves the rejection gate** — the mix-engineer delivers a mixdown + report; the master-engineer accepts or rejects. No silent upstream repair.

This skill is the method layer between the agent's scope (what it owns) and the guide's specifics (what works for this material).

## Andy Wallace Methodology — Five Pillars

| Pillar | Principle | Operational Translation |
|---|---|---|
| **1. Massive, Tight Low-End** | Huge, well-defined bass and kick that anchor without muddying | Synth bus tape saturation (2–4 dB GR, back off 20%); parallel drum compression blended at −18 to −12 dB; master bus HPF 30 Hz, cut 200–400 Hz 1–2 dB |
| **2. Instrument Clarity & Separation** | Carve distinct space so elements remain discernible in dense arrangements | Panning map per §5; vocal HPF 100 Hz + 3.5 kHz presence; synth bus saturation adds harmonic hair without crowding; never hall reverb across mix |
| **3. Simplicity on the Console** | Rely on channel strip EQ/compression, not plugin stacks | GarageBand Amp Designer/Pedalboard for tape saturation; built-in Compressor for parallel drum crush; Channel EQ for vocal; minimal plugin count |
| **4. Dynamic Fader Automation** | Ride faders manually over aggressive mix-bus compression | Automation documented in mix report; quiet parts breathe, loud parts hit; master bus compressor gentle (2:1, 2–3 dB GR) |
| **5. Fast First Drafts** | Capture raw energy in ~30 minutes, trust initial instincts | Mix-engineer runs one pass; report documents what was deliberately left alone; no endless tweaking |

## The Mix Chain — §5 Operationalized

### 5.1 Tape Saturation (Synth Bus)
- **Route:** Layers 1–4 → Bus → Amp Designer or Pedalboard (tape/overdrive, gain low)
- **Drive:** Until grit just audible (~2–4 dB gain reduction), then back off 20%
- **Why:** Stacked saw oscillators sound plastic without it. Saturation = industrial vs. synth-pop line.
- **Wallace link:** Low-end weight comes from harmonic density, not level.

### 5.2 Parallel Compression (Drum Bus) — The Weight Mechanism
1. Duplicate drum bus to second bus
2. On duplicate: Compressor, ratio 10:1, attack fast, release fast, threshold low — crush 15–20 dB
3. Blend crushed copy under clean at −18 to −12 dB
4. **Why:** Programmed kit lacks transient sources of real kit. Restores weight guitars used to supply.
5. **Wallace link:** Parallel compression = dynamic fader automation in plugin form; weight without squashing.

### 5.3 Reverb — Deliberately Restrained
- **Vocal:** Short room or plate, 0.4–0.8 s. Baritone stays upfront and dry-ish.
- **Percussion:** Small room on metallic hits so they have space.
- **Never:** Hall reverb across mix. Smears low end into mud; turns industrial into goth-shoegaze.
- **Wallace link:** Clarity = separation. Reverb pushes back; delay creates depth while locking forward.

### 5.4 Master Bus
- **Channel EQ:** HPF 30 Hz. Cut 200–400 Hz by 1–2 dB if muddy (guitar-corpse band).
- **Compressor:** Ratio 2:1, attack 20 ms, release auto, 2–3 dB reduction. Gentle.
- **Limiter:** Last. Ceiling −1 dB.
- **Wallace link:** Simplicity. Channel strip only. No plugin stacks.

### 5.5 Vocal Chain — Order Matters
**Build track effects panel top-to-bottom; ordering changes result.**

1. **Pitch correction — 50–70% strength** — Tighten *before* distortion. Distortion on flat note = harsh artifacts no EQ removes. Velvut baritone = person, not plugin.
2. **Channel EQ** — HPF 100 Hz (clears mic rumble, clears sub bass). Gentle wide boost +3 dB at 3.5 kHz (presence through saw wall). High shelf conditional — see 10 kHz conflict.
3. **Compressor** — Threshold −24 dB, ratio 4:1, attack 15 ms, release 200 ms. Pin vocal so verse and chorus arrive at same apparent level. Ratio 6:1 if screamed. Auto-gain or manual makeup.
4. **Distortion/Saturation** — Drive 5–15%, mix ~30%. Low drive only. Adds harmonic "hair" to slice through synth bus. Above 15% = effect, not texture.
5. **Stereo delay** — 1/8 left, 1/4 right, mix 10–15%. Replaces reverb as space-creator. Feedback low = depth, not echo.

### 5.6 The 10 kHz Conflict — Hard Rule
- §5.5 boosts +3 dB at 10 kHz on vocal track.
- §9.5 allows +1 to +1.5 dB master shelf.
- Stacking both = up to +4.5 dB at 10 kHz on master → hiss on cymbals, sibilance on baritone.
- **Rule: Pick ONE place for the air.** Either vocal +2 to +3 dB at 10 kHz + master shelf ZERO, OR vocal flat above 8 kHz + master shelf +1 to +1.5 dB. Never both.
- **Wallace link:** Clarity = frequency discipline. No stacking.

## Mix Report — Required Deliverable

The mix-engineer MUST produce a mix report documenting:

| Section | Required Content |
|---|---|
| **Panning Placement** | Per-element panning positions with creative rationale |
| **Sidechain** | At least one documented sidechain (source → target, threshold, ratio) |
| **Gate** | At least one documented gate (element, threshold, range) |
| **Reverb Sends** | Send levels, types, decay times per element |
| **Measurements** | Integrated LUFS, true peak (dBTP), LRA of mixdown |
| **Deliberately Left Alone** | What was not touched and why |

## Hard Boundaries (Non-Negotiable)

- **Cannot master.** Cannot apply delivery loudness target. Cannot raise loudness to fix mix problem.
- **Never invent** key, tempo, or time signature. Write `UNVERIFIED — not documented` and flag.
- **Never write** to `.band` bundles. Stems are read-only WAVs.
- **State measurements, never estimates.** Every loudness/peak claim from meter read.
- **Peers not chain.** Producer directs, master-engineer masters, mix-engineer absorbs neither mandate.
- **One master, all platforms.** No per-DSP variants.
- **True peak, not sample peak.** Report both; only dBTP ships.

## Integration with mix-engineer Agent

- Enabled via `agent.yaml` → `skills_enabled: ["stem-mix-protocol"]`
- Loaded on dispatch; provides the method layer for the Sad Song test and all Velvut/Wágner mixes
- The agent executes the protocol; the protocol defines the decisions

## References

- docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md §5 (The mix chain) + §9 (Final mix and mastering)
- Andy Wallace methodology: Recording Revolution "3 Mixing Secrets from the Legendary Andy Wallace"; Tape Op Interview #25
- PRD §13 (Creative Song-Production Layer)
- dev-ticket-2026-10-30-mix-master-producer-agent-profiles.md (acceptance criteria)
- Harness trace: docs/2026-11-04-harness-trace-mix-master-producer-baseline.md

---

*Skill created 2026-11-07. Mirrors the SKILL.md standard at `/a0/usr/projects/wgnr_ai_sysop/.a0proj/skills/dispatch-safety/SKILL.md`.*