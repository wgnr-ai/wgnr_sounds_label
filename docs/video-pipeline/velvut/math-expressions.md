# math-expressions.md — Strobe Controller + Motion Vector Driver (Velvut pipeline)

> **Artifact of:** `docs/video-pipeline/velvut/` (video-engineer, 2026-09-13)
> **Inputs:** `drums_velocity_spikes`, `guitar_velocity_tracking` (see `midi-parse-graph-spec.md`)
> **Binds:** Constitution C1 (red-only — white STRIPPED, never reintroduced), C6–C8 (movement bounds), C9 (BPM lock)

## a. Strobe Light Controller

**Input:** `drums_velocity_spikes` (float `0.0..1.0`, spike per drum hit).
**Node:** FizzNodes **Value Schedule** node.
**Behavior:** output `1.0` on every note hit, **rapid drop to `0.0` on silence**.

```
on hit:        strobe(t) = 1.0
between hits:  strobe(t) = max(0.0, strobe(t - dt) - DECAY * dt)

DECAY tuned so a hit at beat n reaches 0.0 within ~half a beat
(track: "Is This How It Ends?" @ 107 BPM = 560.7 ms/beat — tempo superseded
per Principal ruling 2026-09-14; the 148 BPM tuning is historical only):
  @107 BPM (560.7 ms/beat)  -> DECAY ≈ 3.6  (1.0 / 0.2804 s)
```

**Destination mapping — RESTRICTED:**

- `strobe(t)` maps to **RED backlight intensity ONLY**.
- The originating brief's `"pure white/hot red"` phrasing is **STRIPPED as Constitution C1 non-compliant**. Do not reintroduce white — C1: a hot red backlight/strobe atmosphere is the ONLY illumination source.
- No other node may consume `strobe(t)` (single-consumer rule keeps C1 auditable).

Optional chorus reinforcement (C9 BPM lock): schedule a secondary `1.0` pulse on bar downbeats during section-labeled `chorus` ranges from the beat map — still red-only.

## b. Motion Vector Driver

**Input:** `guitar_velocity_tracking` (float `0.0..1.0` per palm-muted downstroke).
**Node:** FizzNodes math node → video-model motion fields.

```
norm              = guitar_velocity_tracking            (already 0.0..1.0)

motion_intensity  = clamp( INTENSITY_FLOOR
                         + (INTENSITY_CEIL - INTENSITY_FLOOR) * norm,
                           INTENSITY_FLOOR, INTENSITY_CEIL )

motion_bucket_id  = round( BUCKET_FLOOR
                         + (BUCKET_CEIL - BUCKET_FLOOR) * norm )
```

**Draft-graph clamp (Constitution C6 enforced at generation time):**

```
INTENSITY_FLOOR = 0.15   # never fully static — silhouette must stay alive on the beat
INTENSITY_CEIL  = 0.85   # HARD ceiling: max velocity can NEVER yield flailing
BUCKET_FLOOR    = 32
BUCKET_CEIL     = 192
```

- Higher guitar velocity mathematically forces higher pixel displacement — **sharp, controlled slams** on downstrokes (Constitution C6), delivered through **shoulder/arm stance, minimal head movement** (C7), **never** wild/cartoonish/flailing (C6) and **never** continuous headbanging (C8). The clamp is the mathematical bound; the negative prompt block (`prompt-channels.md`) is the semantic bound. Both always active.
- Field names differ per video model (`motion_bucket_id` LTX-style, `motion_intensity` Hunyuan-style) — the video-model node stays **swappable** until the MPS probe decision lands. Wire the driver into whichever field the active model exposes.
- Movement cadence inherits the beat map (`beatmap-generator.py`): anchors land on beats, not wall-clock guesses (C9).

## Verification hooks

- Draft render shows strobe pulses decaying within ~half a beat and motion peaks co-occurring with guitar downstrokes → channel wiring correct.
- Any observed flailing at `norm = 1.0` → lower `INTENSITY_CEIL` / `BUCKET_CEIL`, re-run GATE-1 draft. Never relax the Constitution to fit a render.