#!/usr/bin/env python3
"""beatmap-generator.py — Velvut BPM-parameterized beat/bar timestamp generator.

WGNR Sounds / Visual Production Layer — video-engineer artifact (authored 2026-09-13).
Emits the JSON beat map consumed by the ComfyUI graphs (draft-workflow.json) and the
ffmpeg finishing chain: every shot length, cut point, and movement anchor references
beat/bar indexes from this map — never wall-clock guesses (Constitution C9).

TRACK / BPM — AUTHORITATIVE (tempo superseded per Principal ruling 2026-09-14 —
148 marked historical; 107 BPM confirmed by canonical MIDI export (flat 107.0),
stems curve (104.79–109.83, avg ≈107), and Principal authorization):
  * Track: "Is This How It Ends?" — 107 BPM, 4/4 -> ~560.7 ms/beat, ~2.2430 s/bar.
  * The canonical export's tempo map is flat 107.0; the stems-merge curve concurs.
    Historical: Principal-declared 148 (2026-09-13, superseded 2026-09-14);
    "Take Me Back" @ 151 and "Who's Calling Me?" @ 148 are catalog references only.
  RETIME = flip TRACK_BPM (one constant) or pass --bpm. Everything recomputes.

ONSET VERIFICATION — REQUIRED GATE (not a note):
  verify_onsets() MUST be implemented and MUST PASS against the master audio
  BEFORE any render timing uses this map. The gate validates the 107 grid AND
  maps the section boundaries. Maps carry "onset_verified": false until then
  and are render-timing-BLOCKED.

Usage:
    python3 beatmap-generator.py --bpm 107 --duration 210 --out beatmap.json
    python3 beatmap-generator.py --verify-audio master.wav   # REQUIRED gate (stub raises until implemented)
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from datetime import datetime, timezone
from pathlib import Path

# ============================ CONFIG — single source of retiming truth ============================
TRACK_NAME = "Is This How It Ends?"  # Principal ruling 2026-09-13 (Velvut video project)
TRACK_BPM = 107.0              # AUTHORITATIVE — tempo superseded per Principal ruling 2026-09-14 (see docstring)
TIME_SIG_BEATS_PER_BAR = 4     # 4/4
DURATION_SECONDS = 210.0       # PLACEHOLDER runtime — set from the master audio at deploy

# Section template for "Is This How It Ends?" (dark introspection, addiction, regret;
# question-chorus hook — title x2). NO fabricated timestamps: start_bar stays None
# until populated from master-audio onset analysis at deploy.
# Dynamics mapping: verse/pre-chorus = quiet introspective (low baritone over tom-toms);
# chorus = wall of sound (distorted power chords, anthemic question hook).
SECTION_TEMPLATE = [
    {"label": "intro",        "start_bar": None, "note": "populate from master-audio onsets"},
    {"label": "verse-1",      "start_bar": None, "note": "quiet — low baritone over tom-toms"},
    {"label": "pre-chorus",   "start_bar": None, "note": "build — quiet side of the quiet/loud split"},
    {"label": "chorus-1",     "start_bar": None, "note": "wall of sound — distorted power chords, question hook"},
    {"label": "verse-2",      "start_bar": None, "note": "quiet — low baritone over tom-toms"},
    {"label": "chorus-2",     "start_bar": None, "note": "wall of sound — question hook x2"},
    {"label": "bridge",       "start_bar": None, "note": "introspective breakdown — populate from master"},
    {"label": "final-chorus", "start_bar": None, "note": "wall of sound — anthemic lift"},
    {"label": "outro",        "start_bar": None, "note": "resolve/decay — populate from master"},
]

ONSET_CHECK_TOLERANCE_MS = 25.0  # max acceptable beat-grid offset after phase alignment
# ==================================================================================================


def seconds_per_beat(bpm: float) -> float:
    if bpm <= 0:
        raise ValueError(f"BPM must be > 0, got {bpm}")
    return 60.0 / bpm


def generate_map(bpm: float, duration_s: float, sections: list[dict]) -> dict:
    """Compute beat/bar timestamps and attach section labels to bars."""
    if duration_s <= 0:
        raise ValueError(f"duration must be > 0, got {duration_s}")

    spb = seconds_per_beat(bpm)            # seconds per beat
    spb_ms = spb * 1000.0                  # ms per beat
    bar_s = spb * TIME_SIG_BEATS_PER_BAR   # seconds per bar
    n_bars = int(math.ceil(duration_s / bar_s))

    # SECTION_TEMPLATE ships start_bar=None on every entry (no fabricated
    # timestamps). Only entries populated from master-audio onset analysis
    # participate in labeling; bars before mapping stay "unmapped".
    ordered = sorted(
        (s for s in sections if s.get("start_bar") is not None),
        key=lambda s: s["start_bar"],
    )

    bars = []
    for b in range(n_bars):
        label = "unmapped"  # populated via onset analysis at deploy
        for s in ordered:
            if b >= s["start_bar"]:
                label = s["label"]
        bars.append({"index": b, "time_s": round(b * bar_s, 4), "section": label})

    beats = []
    for i in range(n_bars * TIME_SIG_BEATS_PER_BAR):
        beats.append({
            "index": i,
            "beat_in_bar": i % TIME_SIG_BEATS_PER_BAR,
            "bar": i // TIME_SIG_BEATS_PER_BAR,
            "time_s": round(i * spb, 4),
        })

    config = {
        "track_title": TRACK_NAME,
        "bpm": bpm,
        "bpm_source": "CONFIRMED working tempo — Principal-declared 2026-09-13, video project",
        "time_sig": f"{TIME_SIG_BEATS_PER_BAR}/4",
        "ms_per_beat": round(spb_ms, 1),
        "s_per_bar": round(bar_s, 4),
        "duration_s": duration_s,
        "n_bars": n_bars,
        "onset_verified": False,
        "onset_check": "REQUIRED GATE — verify_onsets() MUST pass against master audio BEFORE render-timing use (no prior documented tempo for this track)",
        "generated_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "generator": "beatmap-generator.py (docs/video-pipeline/velvut/)",
    }
    return {"config": config, "sections": ordered, "beats": beats, "bars": bars}


def verify_onsets(beatmap_path: str, audio_path: str,
                  tolerance_ms: float = ONSET_CHECK_TOLERANCE_MS) -> dict:
    """REQUIRED GATE — onset-verification drift check against the master audio.

    "Is This How It Ends?" runs on the AUTHORITATIVE 107 BPM grid (tempo
    superseded per Principal ruling 2026-09-14 — 148 marked historical; confirmed
    by canonical MIDI export + stems curve). This gate validates the 107 grid AND
    maps the section boundaries. NO render timing may consume the beat map while
    config.onset_verified is false.

    Implement at deploy (host side) when the master audio exists:
      1. Extract onsets (librosa.beat.beat_track constrained to TRACK_BPM, or aubio).
      2. Align the generated beat grid to the onsets (global phase offset first).
      3. Report mean offset, max offset, accumulated drift per minute.
      4. PASS if max offset <= tolerance_ms; set config.onset_verified = true.
      5. FAIL -> retime TRACK_BPM / fix grid before ANY render timing uses the map.
    """
    raise NotImplementedError(
        f"REQUIRED GATE not satisfied: onset verification requires the master audio (got: {audio_path!r}); "
        "map is render-timing-BLOCKED while config.onset_verified is false."
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Generate the Velvut JSON beat map (BPM-parameterized; one constant retimes everything).")
    p.add_argument("--bpm", type=float, default=TRACK_BPM,
                   help=f"track BPM (default {TRACK_BPM} — AUTHORITATIVE, Principal ruling 2026-09-14)")
    p.add_argument("--duration", type=float, default=DURATION_SECONDS,
                   help=f"track runtime seconds (default {DURATION_SECONDS}; set from master audio)")
    p.add_argument("--out", default="beatmap.json", help="output JSON path")
    p.add_argument("--verify-audio", default=None, metavar="AUDIO",
                   help="REQUIRED gate: run onset verification against the master audio (stub raises until implemented)")
    args = p.parse_args(argv)

    beatmap = generate_map(args.bpm, args.duration, SECTION_TEMPLATE)
    Path(args.out).write_text(json.dumps(beatmap, indent=2) + "\n", encoding="utf-8")

    cfg = beatmap["config"]
    print(f"beat map -> {args.out}")
    print(f"  track={cfg['track_title']}  bpm={cfg['bpm']}  time_sig={cfg['time_sig']}  "
          f"ms_per_beat={cfg['ms_per_beat']}  s_per_bar={cfg['s_per_bar']}")
    print(f"  bars={cfg['n_bars']}  beats={len(beatmap['beats'])}  "
          f"sections_mapped={sum(1 for s in beatmap['sections'])}/{len(SECTION_TEMPLATE)}")
    print(f"  onset_verified={cfg['onset_verified']}  (REQUIRED GATE — MUST pass before render-timing use)")

    if args.verify_audio:
        verify_onsets(args.out, args.verify_audio)  # REQUIRED gate: raises until implemented

    unmapped = [s["label"] for s in SECTION_TEMPLATE if s["start_bar"] is None]
    if unmapped:
        print(f"  NOTE: section boundaries pending master-audio onset analysis: {', '.join(unmapped)}",
              file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())