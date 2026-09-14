# midi-parse-graph-spec.md — Velvut MIDI Parse Layer (ComfyUI graph spec)

> **Artifact of:** `docs/video-pipeline/velvut/` (video-engineer, 2026-09-13; re-bound 2026-09-13)
> **Track:** "Is This How It Ends?" — 107 BPM, 4/4 (~560.7 ms/beat, ~2.2430 s/bar — tempo superseded per Principal ruling 2026-09-14; 148 historical) · render tree `velvut/is-this-how-it-ends/sh-NN/vN-<stage>`
> **Binds:** Draft-First gate (PRD §6, verbatim) · Velvut Visual Constitution C1–C10 (`velvut-visual-constitution` skill)
> **Feeds:** `math-expressions.md` (channel math) → `draft-workflow.json` (GATE-1 draft graph)
> **Status:** DEPLOYED 2026-09-13 (4 node packs live, MIDILoader verified). Canonical `master.mid` received 2026-09-14 (Principal full-song export, parse-clean; 8-stems merge preserved as `master-stems-merge.mid`). Beat map generated from canonical grid. Onset verification vs master audio REQUIRED before render timing.

## 1. Purpose

Defines the parse layer of the MIDI-driven audio-reactive pipeline: how the master MIDI file is loaded inside ComfyUI and converted into the two float control channels that drive (a) red strobe intensity and (b) motion vectors. Everything downstream references these two channels by name — no node re-derives note data on its own.

## 2. Node inventory

| Graph role | Node (deploy-time mapping) | Verified? |
|---|---|---|
| Load MIDI file | RyanOnTheInside MIDI nodes — `.mid` note data (PINNED DEFAULT) | URL verified 2026-09-13 (search-index listing) |
| Audio-frame onset cross-verification | ComfyUI-AudioReactor (tocubed) — distinct role, BOTH installed | Repo verified 2026-09-13 (public) |
| Track separation | MIDI track/channel extract on the loaded MIDI | n/a (graph wiring) |
| Drum spike conversion | FizzNodes float-conversion math node | Repo verified 2026-09-13 |
| Guitar value tracking | FizzNodes value-tracking node | Repo verified 2026-09-13 |

## 3. Channel A — drum/snare/tom-tom track → downbeat spikes

1. **Load MIDI node** loads the canonical `master.mid` (Principal full-song export 2026-09-14; parse-clean under vanilla mido = the ROTI MIDILoader code path).
2. Route the **drum/snare/tom-tom track** through a **FizzNodes float-conversion math node**:
   - every note-on velocity `v` (0–127) maps to `v / 127.0`;
   - the node emits a **value spike on every downbeat / note hit**, collapsing back toward `0.0` between hits.
3. Output contract: `drums_velocity_spikes` — float stream, `0.0..1.0`, spike per hit.

CONFIRMED 2026-09-14 (pitch-profiled canonical export): T0 conductor — **flat 107.0 BPM**, PPQ 480 · T1 tom/percussion-hybrid ch0 (2,682 notes; toms 41/48 dominant — the song's tom-tom identity) · T2 bass-register ch1 (826 notes; pitches 25–30) · T3 **"drums"** kit ch2 (1,836 notes; HH 719 / Kick 528 / Snare 298) · T4 melodic lead ch3 (283 notes). Channel A (strobe) = **T3 + T1** (kit + toms). Channel B (motion) = **T2 + T4** (bass + melodic lead). TEMPO: canonical is flat 107.0; stems curve 104.79→109.83 (avg ≈107) concurs; Principal-declared 148 is contradicted by BOTH MIDI sources — final arbiter = onset check vs master audio. Canonical carries 5,627 notes vs stems' 8,219 (vocals/synth/keys content absent from the single-file export) — `master-stems-merge.mid` is the fallback if that content is ever needed for reactivity.

## 4. Channel B — guitar/bass track → downstroke durations

1. Route the **guitar/bass track** to a **value-tracking node**:
   - note-on/note-off pairs map to **hold-duration floats** for each palm-muted downstroke;
   - normalizes stroke length so short muted chugs and sustained accents are numerically distinct.
2. Output contract: `guitar_velocity_tracking` — float stream, `0.0..1.0`, one value per downstroke.

## 5. Wiring (GATE-1 draft graph orientation)

```
velvut/is-this-how-it-ends/master.mid
   │
   ├─ drums track ──► FizzNodes float-conversion ──► drums_velocity_spikes ─► [math-expressions §a]
   │                                                        │                  Value Schedule → RED backlight intensity ONLY
   └─ guitar/bass track ─► value-tracking node ──────► guitar_velocity_tracking ─► [math-expressions §b]
                                                                            │
                                                     motion_bucket_id / motion_intensity ◄┘ (video-model node, swappable)
```

## 6. Binding constraints on this layer

- **Draft-First:** this parse layer first executes inside `draft-workflow.json` (GATE-1) — low-res, preview-length. No hi-res parameters exist in the draft artifact.
- **C1 (red-only):** channel A drives RED backlight intensity ONLY. The originating brief's "pure white/hot red" phrasing is stripped as C1 non-compliant; white is never reintroduced anywhere in this pipeline.
- **C6/C7/C8 (movement bounds):** channel B passes through the hard clamp defined in `math-expressions.md` §b before touching any motion field — velocity must never yield flailing, headbanging, or head-driven movement.
- **C9 (BPM lock):** timing anchors derive from `beatmap.json` — 107 BPM, 4/4, ~560.7 ms/beat, ~2.2430 s/bar (tempo superseded per Principal ruling 2026-09-14 — 148 marked historical; 107 confirmed by canonical MIDI export, stems curve, and Principal authorization) — and the onset-verification gate in `beatmap-generator.py` is REQUIRED before render timing (validates the 107 grid + maps sections).
- **Model lock:** the motion fields (`motion_bucket_id` / `motion_intensity`) land on the video-model node, which stays SWAPPABLE until the MPS probe decision (HunyuanVideo 1.5 present locally; LTX-Video absent — probe 2026-09-09).

## 7. Reader assignment + open items

**MIDI reader assignment (Principal-overridable default, 2026-09-13, unanswered modal — auto-selected per goal-mode autonomy):**

- **MIDI note data (`.mid` parsing):** RyanOnTheInside (`ComfyUI_RyanOnTheInside`) — loads the master `.mid`, emits the note velocity/transient streams for channels A/B (§3/§4).
- **Audio-frame onset cross-verification:** ComfyUI-AudioReactor (tocubed) — audio-file reactivity feeding the `verify_onsets()` drift check against the master audio. Distinct role, BOTH installed by `deploy-custom-nodes.sh`.
- Override any time: `export COMFYUI_MIDI_REPO=<url>`, re-run the installer.

**Open items (block GATE-1, not authoring):**

1. **Master audio** from the Principal — onset verification (validates the authoritative 107 grid + maps section boundaries), render-timing lock. Sole remaining GATE-1 blocker. (Historical: tempo arbiter 148 vs 107 — RESOLVED per Principal ruling 2026-09-14; 107 authoritative.)
2. ~~`.mid` file from the Principal~~ **RESOLVED 2026-09-14** — canonical `master.mid` received, verified, promoted; parse config pinned (track indexes above).

DEPLOYED 2026-09-13 ~23:14 EDT: all 4 node packs installed + verified registered via /object_info — MIDILoader / MIDIFeatureExtractor / MIDIToAudio (RyanOnTheInside) confirmed live on the running server.