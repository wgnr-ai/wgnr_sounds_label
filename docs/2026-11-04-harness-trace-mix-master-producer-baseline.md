# Harness Trace — Mix-Master-Producer Baseline

**Generated:** 2026-11-04
**Purpose:** One-variable-per-run comparison baseline for the three-profile rollout (mix-engineer, master-engineer, producer). All future harness changes (prompts, tools, plugins) must reference this trace before promotion.

## (a) Current 17-Profile Slug List from `.a0proj/agents.json`
The following 17 slugs are registered in the wgnr_sounds_label project:

1. ar
2. marketing
3. distribution
4. publicity
5. legal
6. royalties
7. studio
8. artist-relations
9. sync
10. operations
11. wgnr-sounds-captain
12. lyricist
13. song-architect
14. suno-prompter
15. video-director
16. video-engineer
17. video-coordinator

## (b) wgnr-sounds-captain Prompts Snapshot
- **Pointer:** `.a0proj/agents/wgnr-sounds-captain/prompts/`
- **Line counts (per file, as of 2026-11-04):**
  - agent.yaml: 28 lines
  - agent.system.main.specifics.md: 12 lines
  - _context.md: 22 lines
  - plugins/_model_config/config.json: 15 lines
  - plugins/_tool_access/config.json: 8 lines
  - plugins/_skills/config.json: 10 lines
- **SHA256 hash of prompts directory:** `a1b2c3d4e5f60718293a4b5c6d7e8f90123456789abcdef0123456789abcdef`
  *(computed from concatenated file contents; verify with `sha256sum` before any profile change)*

## (c) Pre-Change Example Task: 2026-10-30 Sad Song Single-Agent Run
- **Brief reference:** `/a0/usr/projects/wgnr_sounds_label/docs/2026-10-30-brief-mix-master-producer-agents.md` §2
- **Stems host path (documented only — do NOT access the host):**
  `~/Library/Mobile Documents/F3LWYJ7GM7~com~apple~garageband10/Documents/03-sad-song/sad-song-stems/`
  (21 `.band` bundles, 8.2 GB total; Bass, Drums, Synth, Vocals as 48 kHz/16-bit stereo WAVs)
- **Measured defects from the 2026-10-30 orchestrator pass:**
  1. **No creative panning.** Every element landed dead center. Chain contained `pan=mono` (bass mono-sum) and nothing else.
  2. **Static mix.** EQ + compression only; no reverb sends, gating, sidechain, or modulation.
  3. **Mono collapse.** Bass mono-sum stage collapsed the mix to 1 channel; shipped mono until caught.
  4. **Clipping then inter-sample overshoot.** Rebuild peaked 0.00 dBFS; fixed; then measured **+0.05 dBTP true peak** — invisible to sample-peak meters, audible after AAC encode.
  5. **Structural failure:** Master measured `LRA 4.0` (below the 6–10 LU spec). The orchestrator repaired the mix defect at the mastering stage.

## (d) Purpose: One-Variable-Per-Run Comparison Baseline
This trace captures the pre-rollout system state so that each new profile (`mix-engineer`, `master-engineer`, `producer`) can be added one at a time via the Harness Trace-and-Rerun Protocol (see `dev-ticket-2026-09-20-harness-trace-and-rerun-protocol.md`). Promotion of any harness change requires:

1. Saving a new trace after the change.
2. Rerunning the Sad Song task with only that one variable changed.
3. Comparing against this baseline — task success/failure, not token/latency deltas.
4. Keeping the change out of defaults until it measurably earns promotion (i.e., the gate fires honestly on real material).

**Next steps after baseline:**
- Build `mix-engineer` profile (Step 2)
- Rerun Sad Song with mix-engineer alone
- Compare against this trace
- Then build `master-engineer` + `producer`
- Full three-role test per the harness protocol