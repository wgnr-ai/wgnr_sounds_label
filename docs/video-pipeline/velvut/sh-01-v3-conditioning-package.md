# sh-01-v3-conditioning-package.md — SH-01 v3 Conditioning Package + v4 Framing Amendment ("Is This How It Ends?", Velvut)

> **Artifact of:** `docs/video-pipeline/velvut/` — authored by `video-director`, 2026-09-14 (design artifact; pipeline wiring is `video-engineer`)
> **Status:** DESIGN ONLY — no renders executed, no host access used. Handed to `video-engineer`. **v4 framing amendment applied 2026-09-14 post-GATE-3** (§2.1a/§2.1b, §4 criterion) — no re-render of v3 assets; v4 is a fresh draft wiring.
> **Governs:** Velvut Visual Constitution C1–C10 (skill `velvut-visual-constitution`), Draft-First gate (PRD §6, verbatim), `prompt-channels.md` verbatim bases.
> **Failure being fixed:** SH-01 draft v2 (16 steps + C1 fix) rendered Constitution-clean numerically; Principal visual verdict: *"just a red square with dark black clouds moving — nothing to see."* Motion confirmed, strobe/motion coupling works, **no legible figure emerges** — a C5 (silhouette readability) failure at draft scale, second occurrence. Diagnosis standing: the sampler is no longer the bottleneck — conditioning is.
> **v3 GATE-3 verdict (2026-09-14):** C5 person-readability BREAKTHROUGH — a legible guitarist figure in frame (first time; v1/v2 produced cloud only). Residual FAIL is FRAMING: neck-and-up visible only, guitar body out of frame, instrument unreadable. Root cause verified in this file (§2.1): the protected base opens with a close-up instruction; v3 anchors specified medium-full — conflicting framings, the close-up won. **NOT intentional for the main shot.** Fix = v4 amendment: §2.1a framing override (wired first — position is weight), §2.1b close-up reclassification to B-roll inserts, §4 instrument-identifiability acceptance criterion.

---

## 1. Silhouette Strategy — RULING

> **RULING: Adopt image-to-video (i2v) with a composed silhouette keyframe as the SH-01 v3 conditioning strategy — RECOMMENDED, PROBE-GATED. Pure t2v is retained as the documented fallback. The v3 conditioning below is written so both paths share identical text blocks.**

### 1.1 Why i2v (rationale)

1. **It decomposes the exact failure.** Pure t2v must simultaneously invent a legible black figure AND animate it. Twice at draft scale it resolved the frame into what the Constitution is asking for acoustically (red field + fog motion) without ever resolving the subject. i2v moves composition and legibility into a still, where they can be verified frame-perfectly against C4/C5 **before any video cycle is spent**, and leaves the video model the job it is good at: preserving given structure and animating ambient scatter (drifting fog against a hot red backlight) plus locked beat-grid motion.
2. **Silhouettes are the ideal i2v subject.** A solid-black opaque figure with a red rim edge is low-frequency, maximum-contrast structure — the easiest kind of structure for a video model to hold. The observed failure mode (figure dissolving into clouds) is the hardest t2v case and the easiest i2v case.
3. **Prompt-control gain.** In a still, figure placement, scale, fog line, rim trace, and negative space are directly composable and iterably checkable. In t2v they are requests the sampler may ignore — which is precisely what v1/v2 demonstrated.
4. **C5 becomes a pre-render gate, not a post-render autopsy.** A still that fails C4/C5 is regenerated in minutes at trivial cost. A video draft that fails C5 costs a full (even if cheap) gate cycle and a Principal disappointment.

### 1.2 Evidence table (tree docs only — no host exec performed or assumed)

| Question | Tree-docs answer | Source |
|---|---|---|
| Is i2v for HunyuanVideo 1.5 registered in the deployed node set? | **NOT evidenced.** The 2026-09-09 MPS probe recorded **HunyuanVideo 1.5 720p t2v fp16 PRESENT** (t2v only); LTX-Video ABSENT. The 2026-09-13 deploy registered 4 node packs (Advanced-ControlNet, FizzNodes, RyanOnTheInside MIDI nodes, ComfyUI-AudioReactor) — MIDI/math/audio conditioning, no video-model i2v node. Draft-graph node 15 is an explicit PLACEHOLDER: "t2v or i2v per shot silhouette strategy (PRD Open Question 5)." | PRD §13 closeout (probe 2026-09-09); tree `AGENTS.md` deploy record 2026-09-13; `draft-workflow.json` node 15 |
| Does t2v work on MPS? | **VERIFIED at draft scale** — v2 motion played and strobe/motion coupling worked. t2v is the proven mechanical path; it fails on C5 legibility, not on execution. | SH-01 v2 gate context (this tasking) |
| Is this decision anticipated? | Yes — **PRD Open Question 5** ("prompt-driven silhouettes vs image-to-video from generated stills; recommendation due after probe"). Probe landed 2026-09-09; this document is that recommendation. | PRD §10 OQ5 |

**UNVERIFIED-CLAIM items the engineer must close at deploy before any i2v render (both are GATE-1-internal, zero cost to the gate):**

1. **i2v weights presence** — the probe verified t2v weights only. Confirm (or download — open weights, local, fully inside the Infrastructure Rule) the HunyuanVideo 1.5 **i2v** variant on the Mac Studio.
2. **i2v sampler path** — node 15 PLACEHOLDER must resolve to a concrete i2v-capable node in the deployed set; if none exists, that is a hard stop on the i2v path for v3 and the fallback ships.
3. **Local image-generation engine** — the keyframe still is generated via the label's local image generation per Principal tasking (2026-09-14); the specific engine is **not documented in this tree** and is the engineer's deploy confirmation. Never a cloud tool (Infrastructure Rule).

### 1.3 Risks and mitigations

| Risk | Mitigation |
|---|---|
| i2v weights/sampler absent on MPS | Fallback ships unchanged: v3 = strengthened t2v (anchors + negatives below). No package rework — conditioning is shared. |
| i2v unexecuted on MPS (speed/memory unknown) | The **first i2v draft render IS the probe**: GATE-1 envelope (320×180, 49 frames, 6 steps) makes the verification cheap and fully inside the Draft-First gate. Result reports to the Principal at GATE-3 like any draft. |
| Figure drift/degradation over clip length | Keep shots draft-length short (49 frames @ 24 fps ≈ 2.04 s ≈ bar 1 of the curve grid); cuts land on beatmap bar boundaries; each shot re-anchors from its keyframe. |
| Keyframe/conditioning mismatch | Keyframe composes to the SAME framing intent as the conditioning: the §2.1a v4 WIDE performance framing (the base's close-up is reclassified to B-roll inserts per §2.1b). Still must pass the §4 acceptance gate before entering the graph. |
| Still generator produces near-compliant frames that get hand-tuned into non-compliance | No hand-patching: a still failing any C1–C5 item is regenerated. The acceptance gate is the only path into the graph. |

### 1.4 Fallback (explicit)

If either deploy verification in §1.2 fails, v3 ships as **strengthened t2v**: §2 anchor blocks + §3 negative additions apply verbatim to the t2v path. t2v remains VERIFIED-executable; the anchors/negatives target its C5 failure directly.

**PRD note (for Principal/captain — not edited by this artifact):** this ruling is the Open Question 5 recommendation. On Principal confirmation, OQ5 should be marked RESOLVED with this doc as evidence; OQ4 (model lock) remains open and untouched — nothing here locks LTX vs HunyuanVideo.

---

## 2. Revised SH-01 Conditioning — verbatim bases + structural anchor append blocks

**Wiring rule (binding):** the three positive formulas in `prompt-channels.md` are VERBATIM-protected — never edited, never reordered. The **v4 framing override + v3 anchor block are appended after the base text — v4 override FIRST** (v4 wiring order: §5 note 7) — as a separate conditioning segment (single merged encode or dual-encode concat — engineer's wiring choice at deploy). The mandatory negative block (§3) stays on every channel verbatim.

**Intro-ambiguity parameterization:** beatmap section 1 (0.0–9.52 s, bars 1–4, 16 beats, first onset 0.06 s) is **UNLABELED and unconfirmed**. Anchor motion language below is therefore intensity-neutral and beat-locked; intensity is carried by parameter tokens resolved at wiring, never by prose that assumes quiet vs loud:

```text
{{INTRO_MOTION_CEIL}}   # conservative wiring placeholder: 0.55 until section-1 label confirmed.
                        # On confirmation: quiet-intro  -> keep 0.55
                        #                 loud-intro   -> restore protected ceiling 0.85
```

The math-expressions.md driver clamp (FLOOR 0.15 / protected CEIL 0.85) is untouched by default; a section-scoped ceiling is an engineer wiring option only if implemented as a clean, auditable parameter — never by editing the protected math spec.

### 2.1 SH-01 — Guitarist channel (primary)

**BASE (verbatim — `prompt-channels.md` Channel 1, DO NOT EDIT):**

```text
Grounded cinematic live-action music video, 16:9, close-up on a sleek black matte solid-body electric guitar, sharp clean geometric edges, low-slung strap. An anonymous dark silhouette guitarist slamming heavy downstrokes. Crushed deep blacks, underexposed, blinding hot red backlight bleeding through dense volumetric fog, fine film grain, raw atmospheric depth.
```

**v4 FRAMING OVERRIDE BLOCK (wired FIRST — before the v3 anchor block; strongest anchor position so the wide framing wins the base's close-up line):**

```text
WIDE SHOT — full performance framing. Full figure visible head to hips, center frame. The entire guitar in frame — headstock to body clearly silhouetted. Instrument shape readable at a glance: electric guitar, double-cutaway body outline against the red backlight. This is a wide performance shot, NOT a close-up — any close-up on the guitar is reserved for separate B-roll insert shots and must not affect this framing. Single anonymous guitarist silhouette, pure solid opaque black, center frame, roughly one third of the frame height, head and shoulders above the fog line.
```

**v3 ANCHOR BLOCK (appended after the v4 override):**

```text
Single anonymous guitarist silhouette, pure solid opaque black with ZERO facial detail, center frame, medium-full figure occupying roughly one third of the frame height, head and shoulders rising above the fog line. Guitar body low at the hips on a low-slung strap, neck cutting a clean diagonal, full instrument silhouette clearly readable against the red backlight. Wide negative space of dense red-scattered fog around the figure; frame edges fall to crushed deep blacks. Static locked-off tripod framing — no pan, no zoom, no camera shake. The figure performs sharp, hard-hitting, controlled downstrokes locked to the beat grid, played through shoulder and arm stance, head steady with minimal head movement; no continuous headbanging. The silhouette stays a distinct solid-black human form for the entire shot — it never dissolves into smoke, never merges with the fog, read completely by posture, hair, and instrument shape. Movement accents land on the beatmap curve grid, not wall-clock. Motion intensity ceiling: {{INTRO_MOTION_CEIL}}.
```

**Known tension, stated honestly:** the protected base contains "slamming heavy downstrokes." If section 1 confirms as a quiet-introspective intro, that base phrase will over-drive the figure. The anchor's control/stance/ceiling language is the counterweight. If the tension proves render-visible at GATE-3, the escalation is a Principal ruling on the protected base — not a silent engineer edit.

**v4 CLOSE-UP RECLASSIFICATION (answers the Principal's GATE-3 question):** The neck-and-up framing in v3 was **NOT intentional** for the main performance shot — it was the protected base's `close-up on a sleek black matte solid-body electric guitar` line winning the framing conflict against the v3 anchors. The close-up intent is real and protected — it belongs to **B-ROLL INSERT shots** for the edit (neck / fretting-hand detail inserts), not the main shot. The base text stays untouched AND its intent is honored in the right place: the §2.1a override routes main-shot framing to wide and reserves the close-up for inserts. Scale note: the override leads — its "full figure visible head to hips" + "roughly one third of the frame height" governs; the v3 anchor's "medium-full" phrasing is superseded by the override (same ~⅓ height, explicit head-to-hips span).

**B-roll insert shot descriptor (for later insert shots):**

```text
guitar neck and fretting-hand silhouette close-up
```

(7 words; silhouette-safe, C4-compatible by construction.)

### 2.2 Anchor template — drummer / bassist channels (same structure, for SH-NN variants)

Same append rule, same tokens. Compact forms (expand to full SH-01 detail when those shots are cut). **No v4 override needed here** — verified against `prompt-channels.md`: only Channel 1 (guitarist) carries a close-up instruction in its base; the drummer and bassist bases contain no framing conflict.

**Drummer:**
```text
Single drummer silhouette, pure solid opaque black with ZERO facial detail, seated center frame behind the dark minimalist kit, head and shoulders above the fog line, kit silhouette clearly readable — cymbal rims and shell edges traced by the red backlight. Wide red-fog negative space; crushed deep blacks at frame edges. Static locked-off tripod framing — no pan, no zoom, no camera shake. Heavy overhead stick strikes locked to the beat grid, controlled and hard-hitting, torso-driven, no continuous headbanging; figure never dissolves into the smoke, read completely by posture, arm arc, and kit shape. Movement accents land on the beatmap curve grid. Motion intensity ceiling: {{INTRO_MOTION_CEIL}}.
```

**Bassist:**
```text
Single bassist silhouette, pure solid opaque black with ZERO facial detail, broad stance center frame, head and shoulders above the fog line, heavy solid-body bass slung extremely low, full instrument silhouette clearly readable against the red backlight. Wide red-fog negative space; crushed deep blacks at frame edges. Static locked-off tripod framing — no pan, no zoom, no camera shake. Slow, controlled rhythmic weight shifts locked to the beat grid, shoulder-and-arm driven, head steady with minimal head movement; figure never dissolves into the fog, read completely by posture, hair, and instrument shape. Movement accents land on the beatmap curve grid. Motion intensity ceiling: {{INTRO_MOTION_CEIL}}.
```

**Constitution mapping (all anchor blocks):** C1/C2/C3 language inherited from the verbatim bases and reinforced (red backlight, dense fog, crushed blacks); C4 verbatim ("ZERO facial detail"); C5 verbatim ("read completely by posture, hair, and instrument shape") + **v4 criterion: instrument identifiable by silhouette alone from any single frame** (enforced at the §4 gate); C6/C7/C8 explicit (sharp/hard-hitting/controlled, shoulder-arm stance, minimal head movement, no continuous headbanging); C9 via curve-grid anchoring (beatmap.json authoritative); C10 not triggered by SH-01 (instrumental shot — no performance/lip-sync logic; baritone frontman rule applies to frontman shots later in the sequence).

---

## 3. Negative-Prompt Strengthening

**MANDATORY block — stays verbatim on every channel (prompt-channels.md):**

```text
facial features, visible face, eyes, mouth, front lighting, white lights, other-color lights, headbanging, wild flailing movement, cartoonish motion, bright exposure
```

**v3 ADDITIONS block (appended after the mandatory block, same negative encode):**

```text
abstract blob composition, no visible figure, abstract shapes only, formless, figure-less frame, indistinct silhouette, silhouette dissolving into smoke, red haze without subject, empty frame, multiple figures, camera movement, camera shake, zoom, text, watermark
```

| Addition | Targets |
|---|---|
| `abstract blob composition`, `abstract shapes only`, `formless`, `figure-less frame`, `no visible figure`, `indistinct silhouette`, `silhouette dissolving into smoke`, `red haze without subject`, `empty frame` | The observed v2 failure mode — figure-less red-field composition (C5) |
| `multiple figures` | Single-figure shot discipline (SH-01 is one guitarist) |
| `camera movement`, `camera shake`, `zoom` | Protects the static-tripod ruling in §2 |
| `text`, `watermark` | Standard render hygiene |

**Wiring note for video-engineer (honesty on token semantics):** CLIP does not parse negation. The three task-mandated phrases (`no visible figure`, `abstract shapes only`, `formless`) are included verbatim as required; of these, `abstract shapes only` and `formless` carry clean suppressible concept tokens, while the negation token in `no visible figure` is weak noise and its content tokens (`visible figure`) may push the wrong way. Recommend a one-draft A/B: mandatory + additions as written vs. the same list with `no visible figure` replaced by the positive-suppressible `figure-less composition`. Report which wins at GATE-3; the mandatory block is untouched either way.

---

## 4. Keyframe Still Spec (i2v path — SH-01 guitarist keyframe)

**Only generated if the §1.2 deploy verifications pass.** Generated via the label's local image generation (Principal tasking 2026-09-14; engine = engineer deploy confirmation; never cloud). 16:9.

**Positive prompt (v4 reframe — WIDE performance framing):**

```text
Grounded cinematic live-action photograph, 16:9 widescreen. WIDE SHOT — full performance framing: a single anonymous guitarist in pure solid-black silhouette with ZERO facial detail, seen from behind at a three-quarter angle, full figure visible head to hips, center frame, head and shoulders rising above the fog line. The entire guitar in frame — headstock to body clearly silhouetted — sleek black matte solid-body electric guitar slung low on a low-slung strap, sharp clean geometric edges, instrument shape readable at a glance: double-cutaway body outline, headstock breaking the fog line. Blinding hot red backlight behind the figure bleeding through heavy, dense volumetric fog scattering the red light, a red rim tracing shoulders, hair, and the guitar edge. Everything in front of the figure falls to crushed deep blacks — high-contrast underexposed, fine film grain, raw atmospheric depth, dark negative space at the frame edges. The figure is read completely by posture, hair, and instrument shape. Instrument identifiable by silhouette alone from this single frame.
```

**Negative prompt (mandatory block + v3 additions, verbatim from §3 — both blocks):** as §3.

**Technical:** aspect 16:9; generate at ≥1280×720 (matches the HunyuanVideo 1.5 720p hi-res path; downscales cleanly to the 320×180 draft envelope). Store as `velvut/is-this-how-it-ends/sh-01/keyframes/kf-v2.png` — the v4 reframe supersedes the v3-framing keyframe spec; `kf-v1` is reserved for the superseded generation, no overwrites (keyframes version like renders).

**Acceptance gate — the still is checked against the Constitution BEFORE it may enter any graph:** C1 (red-only illumination — no other source), C2 (heavy dense fog scattering red), C3 (crushed blacks + grain, grounded live-action look), C4 (ZERO facial detail), C5 (readable by posture/hair/instrument shape — **v4 criterion: instrument identifiable by silhouette alone from any single frame**). C6–C9 are motion checks — N/A for a still. C10 N/A (instrumental). **Any C1–C5 FAIL = regenerate; no hand-patching.** Pass = the still becomes the i2v first frame.

---

## 5. v3/v4 Draft Wiring Notes (video-engineer)

1. **Both paths share the conditioning.** Wire §2.1a v4 override + v3 anchors + §3 negatives regardless of path; attach §4 keyframe only on the i2v path.
2. **i2v probe = GATE-1 draft.** First i2v render runs inside the protected draft envelope (320×180, 49 frames, 24 fps, 6 steps — draft-workflow.json node 16 values). The probe result reports at GATE-3; no hi-res cycle is implied or requested anywhere in this package.
3. **Node 15 resolution:** swap the PLACEHOLDER per §1.2 verifications (i2v node if verified; t2v node on fallback). Motion driver wiring (node 9 fields) unchanged per math-expressions.md.
4. **Draft window anchor:** 49 frames @ 24 fps ≈ 2.04 s from first onset 0.06 s ≈ **bar 1 (beats 0–3) of the curve grid** — strobe/motion accents verify against beatmap.json beats 0–3 (0.06 / 0.631 / 1.203 / 1.774 s).
5. **Resolve `{{INTRO_MOTION_CEIL}}` at wiring** (placeholder 0.55; per §2 rules on label confirmation). Record the resolved value in the draft report so GATE-3 judgment sees it.
6. **Onset/section state:** beatmap.json grid is onset-verified PASS (curve, median 7.6 ms); section 1 label remains UNLABELED/unconfirmed — parameters stay pending by design.
7. **v4 wiring order (binding):** base → **§2.1a v4 FRAMING OVERRIDE FIRST** → v3 anchor block → negatives. Earlier tokens carry more weight; the override must lead every added segment so the wide framing wins the base's close-up line. The i2v keyframe (§4) composes to the same wide framing.

---

## 6. Sources (claims in this artifact)

| Claim | Source |
|---|---|
| 107 BPM 4/4 reference grid (~560.7 ms/beat); curve 104.79–109.83 authoritative; 148 historical | Constitution skill §2; PRD §5/§10 OQ1; tree AGENTS.md Local Contract #3 |
| Section 1 = 0.0–9.52 s, bars 1–4, 16 beats, first onset 0.06 s, UNLABELED/unconfirmed; curve onset-verified PASS (median 7.6 ms, 90.9% coverage, CURVE_WINS) | `beatmap.json` (generated 2026-09-14) |
| HunyuanVideo 1.5 720p **t2v** fp16 PRESENT; LTX-Video ABSENT | PRD §13 closeout (MPS probe 2026-09-09) |
| 4 node packs deployed + registration-verified (MIDI/AudioReactor/ControlNet/FizzNodes); no i2v node evidenced | tree `AGENTS.md` deploy record 2026-09-13 |
| Draft envelope 320×180 / 49 frames / 24 fps / 6 steps; node 15 PLACEHOLDER "t2v or i2v per shot silhouette strategy" | `draft-workflow.json` nodes 15–16 |
| Verbatim bases + mandatory negative block; close-up instruction present in Channel 1 only | `prompt-channels.md` |
| Driver clamp 0.15/0.85, buckets 32/192; strobe single-consumer red-only | `math-expressions.md` |
| Keyframe still sourced from label's local image generation; cloud prohibited | Principal tasking 2026-09-14; PRD §6 Infrastructure Rule |
| i2v weights presence, i2v sampler path, local image engine identity — **UNVERIFIED**, deploy items | §1.2 of this artifact |
| SH-01 v3 GATE-3 Principal verdict + v4 amendment authorization (verbatim: *"I see a young man playing the guitar but I only see the neck of the guitar up so no idea which instrument it is. Is that intentional?"*) | Principal GATE-3 feedback, 2026-09-14 |
