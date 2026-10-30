---
last_updated: 2026-10-30T17:43:00
status: delivered
artist: Velvut
song: Nothing To Me
series_position: 3
route: suno-synth-re-render
tempo: UNVERIFIED — not documented
key: UNVERIFIED — not documented
time_signature: UNVERIFIED — not documented
vocal_range: F2-D4
suno_role: assist
direction_status: approved
master_source: studio
---

# NOTHING TO ME (Velvut) — Synth Conversion Suno Prompt Set

**Artist:** Velvut · **Song:** Nothing To Me · **Date:** 2026-10-30 · **Series:** song 3
**Route:** Suno synth re-render (reference only) · **Purpose:** direction reference for the GarageBand rebuild

---

## 0. Tempo gap — read first

**No BPM, no specific key, no time signature documented.** Nothing invented.

Suno will choose the tempo itself, and darkwave/industrial tags pull slower than a nu-alt-rock original. The render is a valid **palette / arrangement / vocal** reference and an **invalid tempo** reference. Do not A/B it against the original for tempo.

---

## 1. Verified song facts

Source: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/nothing-to-me.md` (read direct 2026-10-30, last_updated 2026-07-31).

| Field | Value |
|---|---|
| Tempo | UNVERIFIED — not documented |
| Key | UNVERIFIED — no specific key; file says 'minor key' only |
| Meter | UNVERIFIED — not documented |
| Vocal | Powerful baritone male, upfront |
| Style notes (verbatim) | nu-alt rock, alt-metal influences, minor key, powerful baritone vocal, upfront vocals, analog tape saturation, room reverb, wailing guitars, tight rhythm guitars, deep bass, full drum kit performance, explosive chorus lift |
| Exclusions (verbatim) | none recorded in file — series-standard applied |
| Structure | V1 → PC → C → V2 → PC → C. No bridge, no final chorus, no outro. |
| Suno role | Suno-assist (PRD 5.4) — master_source = studio |

---

## 2. Style prompt — paste into Style of Music

```
dark industrial synth-rock, darkwave, electro-industrial, nu-alt rock aggression, heavy, minor key, distorted synth bass, gated sequenced saw-bass pulses, detuned saw stack stabs, hard analog synth pads, aggressive mono-synth lead with portamento climbing through the pre-chorus, metallic industrial percussion hits, programmed kick with weight, deep bass, restrained verses, long wall-of-sound chorus with a mid-chorus breakdown, analog tape saturation, tight room reverb, parallel compression, powerful baritone male vocal upfront, gritty, explosive chorus lift
```

No BPM — that is the gap, not an oversight.

**Translation calls:** `alt-metal` dropped as a literal tag (bare tag pulls electric guitars); weight encoded as `nu-alt rock aggression, heavy` plus the substitution map. `minor key` written verbatim, no specific key asserted. `wailing guitars` / `tight rhythm guitars` removed — those are the elements being converted.

### Substitution map (inherited)

| Original role | Synth replacement |
|---|---|
| Chugging rhythm guitar | distorted synth bass + gated sequenced saw-bass pulses |
| Rhythm power chords | detuned saw stack stabs + hard analog synth pads |
| Wailing / lead guitar | aggressive mono-synth lead with portamento |
| Tom-tom / kit weight | metallic industrial percussion hits + programmed kick with weight |
| Guitar sustain intro | absent — opens on vocal over synth-bass pulse |

### Production textures

| Texture | Decision | Reason |
|---|---|---|
| Analog tape saturation | KEEP | Anti-drift control: difference between dark industrial and clean synth-pop |
| Room reverb | KEEP, tight room only — not hall, not plate | A large hall under dark synths invites goth-shoegaze smear and eats vocal upfrontness |
| Parallel compression | KEEP — load-bearing | The mechanism that gives a guitar-less chorus weight |

---

## 3. Exclude styles — paste into Exclude

**Core:**

```
tenor vocal, country, melodramatic, classic rock, guitar sustain intro, electric guitar, acoustic guitar, rhythm guitar, lead guitar, power chords, palm-muted chugs, guitar solo, guitar amp, synthwave, retro 80s, clean synth-pop, electro-pop, female vocal, polished, mastered, final
```

**Extended:**

```
dance-pop, chiptune, vaporwave, 8-bit, orchestral, symphonic, choir, pop production, clean production, bright, soft, ballad, sentimental, uplifting, handclaps, funk guitar, wah pedal, fretless bass, disco, goth-shoegaze, hall reverb, big room reverb, shoegaze, dream pop
```

---

## 4. Title metadata

- **Title:** `Nothing To Me (Synth Conversion Reference)`
- **Fallback:** `Nothing To Me Synth Reference`

---

## 5. Creative sliders

**Mode:** Custom, no audio upload.

| Control | Value | Mode | Reasoning |
|---|---|---|---|
| **Weirdness** | **30%** | Custom | Guitar bleed is the failure mode. Missing BPM is not a reason to deviate — weirdness does not set tempo. |
| **Style Influence** | **75%** | Custom | Source tags (nu-alt rock, alt-metal) push harder toward guitars than earlier songs; ban only holds enforced hard. |
| **Audio Influence** | **n/a — slider absent** | Custom (no upload) | Cover-mode value if used later: **65%**. |
| **Variety** | **Off (0)** | Custom | Rewrites the style prompt server-side; would strip the guitar bans and substitution map. Defaults to Normal. |

**Max Mode: ON.** **Personalize: off.**

**Retry:** guitar → Style Influence 85%. Too clean → Weirdness 45%. **Tempo wrong → no slider controls tempo.**

---

## 6. Lyrics field — verbatim from vault

```
[Verse]
My heart is slowly bleeding
My brain
My body is going insane

There is no soul
There is no feeling
I live this every day

[Pre-Chorus]
How did this happen?
There's something wrong with this place
It's like everybody's acting
And they're fake as fuck to my face

[Chorus]
Oh, oh
The older I get
The more I see that people don't care
And it's getting so clear

Because oh, you said you love me
But its clear enough to see
That all you have for me
Are Hallmark greetings

And it means nothing to me
You mean nothing to me

[Verse 2]
My head is filled with darkness
And it's creeping to my soul
I need someone to help me
Before I'm dragged down in the hole

[Pre-Chorus]
How did this happen?
There's something wrong with this place
It's like everybody's acting
And they're fake as fuck to my face

[Chorus]
Oh, oh
The older I get
The more I see that people don't care
And it's getting so clear

Because oh, you said you love me
But its clear enough to see
That all you have for me
Are Hallmark greetings

And it means nothing to me
You mean nothing to me
Nothing to me
```

**Fidelity:** zero words altered. Labels exactly as written — no bridge, no final chorus, no outro added. Profanity `fake as fuck` verbatim twice. `But its clear enough to see` — the missing apostrophe is in the source, preserved deliberately.

---

## 7. Arrangement notes

**The `Oh, oh` pickup.** Build it as a drop, not a fill: the last pre-chorus line lands hard and bare, everything falls away for a half bar, one sustained distorted bass note and room tail. The pickup rides in clean over that hole. Wall re-enters **on `The older I get`**, not on the pickup.

**The long chorus (11 lines) needs three internal stages:**

| Stage | Lines | Treatment |
|---|---|---|
| Thesis | `The older I get / …people don't care / …so clear` | Full wall, open, statement-of-fact |
| The turn | `Because oh, you said you love me…` | Density drop — pads and percussion back to pulse + vocal. `Because` is the hinge. |
| Image + payoff | `Are Hallmark greetings` → `And it means nothing to me` | See below |

**`Hallmark greetings` gets the room.** The only concrete object in an abstract lyric. Wall off completely on `That all you have for me`, the line exposed in the gap, one beat of nothing, **then** the full stack on `And it means nothing to me`.

**The lift comes from the pre-chorus, not a riff.** The mono lead climbs through the pre-chorus (portamento rising, gathering density line by line). The four lines tighten: restrained → rising → tighter → `And they're fake as fuck to my face` bare and exposed. That bare line is what makes the drop read as release.

---

## 8. Suno role verification

**Suno-assist (PRD 5.4). master_source = studio.** Reference render only, never a release master. Baritone male descriptors carried; `female vocal` and `tenor vocal` excluded. Any Suno audio beyond listening reference must come from an active paid tier (Premier plan on record; no retroactive rights on free-tier output).

---

## 9. Compatibility checklist

| # | Check | Result |
|---|---|---|
| 1 | Style prompt present | PASS |
| 2 | Lyrics verbatim from vault | PASS |
| 3 | Section labels per spec | PASS — no flag; all labels canonical |
| 4 | Labels Title Case | PASS |
| 5 | Line breaks per spec | PASS |
| 6 | Title field present | PASS |
| 7 | Negative prompt present | PASS |
| 8 | Suno role verdict, PRD 5.4 | PASS |
| 9 | Out-of-vocabulary tags flagged | PASS |
| 10 | Per-artist prompt structure | PASS |
| 11 | Key and time signature as explicit fields | PASS with flag — both UNVERIFIED |
| 12 | All four sliders specified | PASS |

**Overall: PASS.**

---

## 10. Audition notes

1. Tempo blindness first — do not compare against the original.
2. Guitar bleed — 200-500 Hz for strummed guitar body.
3. Chorus turn — does `Because oh, you said you love me` audibly change density? Flat across all 11 lines = the hinge is gone.
4. `Hallmark greetings` — intelligible and exposed, or reject.
5. `Oh, oh` pickup — did it land on a hole or get rushed?
6. Pre-chorus climb — mono lead must rise; a static riff means no lift mechanism.
7. Weight — sub-bass plus parallel-crushed percussion.
8. Structure — exactly two choruses. Ends on `Nothing to me`.
9. Vocal — powerful baritone upfront; reject tenor or polished pop-baritone.
10. Tape vs plastic — clean and modern means saturation was lost.

---

## 11. Lineage

- Song facts and lyrics: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/nothing-to-me.md`
- Series reference: `docs/2026-10-30-sad-song-velvut-synth-conversion-suno-prompt.md`
- Prompt spec: `.a0proj/skills/suno-prompt-compatibility-spec/SKILL.md`
- Role matrix: `.a0proj/skills/suno-integration/SKILL.md` (PRD 5.4)
