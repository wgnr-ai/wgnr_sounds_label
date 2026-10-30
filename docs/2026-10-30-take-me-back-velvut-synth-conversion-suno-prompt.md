---
last_updated: 2026-10-30T17:43:00
status: delivered
artist: Velvut
song: Take Me Back
series_position: 5
route: suno-synth-re-render
tempo: 148
key: UNVERIFIED — not documented
time_signature: UNVERIFIED — not documented
vocal_range: F2-D4
suno_role: assist
direction_status: approved
master_source: studio
---

# TAKE ME BACK? (Velvut) — Synth Conversion Suno Prompt Set

**Artist:** Velvut · **Song:** Take Me Back? · **Date:** 2026-10-30 · **Series:** song 5
**Route:** Suno synth re-render (reference only) · **Purpose:** direction reference for the GarageBand rebuild

---

## 1. Verified song facts

Source: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/take-me-back.md` (read direct 2026-10-30, last_updated 2026-09-03, **status: final — the only song in the vault marked final**).

| Field | Value |
|---|---|
| Title in file | `Take Me Back?` — **with a question mark** |
| Tempo | **148 BPM — DOCUMENTED** |
| Key | UNVERIFIED — no specific key; file says 'predominantly minor key' only |
| Meter | UNVERIFIED — not documented |
| Vocal | low and deep baritone, upfront |
| Style notes (verbatim) | post-alternative rock, alt-metal edge, 148 BPM, low and deep baritone vocals, close-mic guitar, tom-tom verses, distorted power chords, palm-muted downstrokes, octave lead guitar, spring reverb, tape saturation, parallel compression, quiet loud dynamics, pre-chorus lift, anthemic chorus, predominantly minor key, memorable chorus hook |
| Exclusions (verbatim) | tenor vocal, country, melodramatic, classic rock — **4 items only** |
| Structure | V1 → PC → C → V2 → PC → C → Bridge → Final Chorus → **Outro** |
| Suno role | Suno-assist (PRD 5.4) — master_source = studio |

**Flags on the file:** (1) The `?` is verified present in a final file; whether it is deliberate is not documented. (2) No key, meter, or BPM frontmatter fields — those values exist only in prose style notes. (3) Exclude list omits `guitar sustain intro`, which every sibling has.

---

## 2. Style prompt — paste into Style of Music

```
dark industrial synth-rock, darkwave, electro-industrial, 148 BPM, predominantly minor key, distorted synth bass, gated sequenced saw-bass pulses, detuned saw stack stabs, hard analog synth pads, warm analog synth tone, aggressive mono-synth lead with portamento, spring reverb on lead synth, metallic industrial percussion hits, programmed kick with weight, tape saturation, parallel compression, quiet verses, heavy choruses, drums-drop pre-chorus, anthemic chorus, cumulative arrangement lift, wistful, bittersweet, nostalgic, deep baritone male vocal upfront, exposed unaccompanied outro, memorable chorus hook
```

### The central judgement call — heavy without sinister, wistful without soft

This is the tenderest lyric in the series: paper boats, a crooked swing set, mud on shoes, sleeping till three. Two opposite failure modes.

**How it stays heavy without turning ugly.** Weight is mass, not threat:
- Weight sits in sub and low-mid — `distorted synth bass` + `programmed kick with weight`. Loud and low reads as grief with a body, not a threat.
- Saw stabs are **detuned, not dissonant**. Detune thickens; dissonance stacks minor seconds and reads as menace.
- `warm analog synth tone` specified; `cold`, `eerie`, `sinister`, `horror`, `dissonant`, `noise`, `siren`, `drone` all excluded.
- No noise beds, no sirens, no whispered doubles. One voice, forward and dry-ish.
- Harmony stays diatonic minor and lands on the tonic. A plea that never resolves reads as dread.

**How it avoids going soft.**
- **148 BPM is itself the anti-ballad guard.** The only way to hold 148 is a sequenced pulse, so the verse floor is movement, not padding.
- Nocturne instruments excluded by name: `piano, strings, orchestral, symphonic, choir, music box, celesta, ballad, soft, sentimental, tender, lullaby`.
- **The tender moments are exposed, not airy.** Exposure = fewer things playing. Softness = gentler things playing.
- The lead is mono-synth with portamento, not a bell or piano line. Clean bell tone would make it cute, and cute is where this song dies.

**Net instruction to the model: loud, low, warm, and sad. Never frightening, never gentle.**

### Substitution map (inherited)

| Original role | Synth replacement |
|---|---|
| Chugging rhythm / palm-muted downstrokes | distorted synth bass + gated sequenced saw-bass pulses |
| Distorted power chords | detuned saw stack stabs + hard analog synth pads |
| Octave lead guitar | aggressive mono-synth lead with portamento |
| Tom-tom verses / kit weight | metallic industrial percussion + programmed kick with weight |
| Close-mic guitar | close-mic distorted synth bass — transient intimacy plus low-mid body |
| Guitar sustain intro | absent — open on saw-bass pulse or single metallic hit |

### Production textures

| Texture | Decision | Reason |
|---|---|---|
| Tape saturation | KEEP | Synth bus glue; keeps the cold mechanical palette from clean 2010 electro |
| Spring reverb | KEEP, **re-targeted to the mono-synth lead only** | Documented for this song and its sibling cluster. Dropping it would break continuity for nothing. Short tank insert on the lead — never the vocal, never the master. `surf` excluded so it stays short. |
| Parallel compression | KEEP | Glues drums and bass; part of what makes this read as a record rather than a patch |

---

## 3. Exclude styles

**Core:**

```
tenor vocal, country, melodramatic, classic rock, guitar sustain intro, electric guitar, acoustic guitar, rhythm guitar, lead guitar, power chords, palm-muted chugs, guitar solo, guitar amp, synthwave, retro 80s, surf, clean synth-pop, electro-pop, ballad, soft, sentimental, tender, lullaby, piano, strings, music box, celesta, eerie, sinister, horror, dissonant, cold, noise, siren, drone, gang vocals, chant, group shout, crowd vocals, call and response, riser, build-up, snare roll, fade out, fade ending, female vocal, polished, mastered, final
```

**Extended:**

```
dance-pop, chiptune, vaporwave, 8-bit, orchestral, symphonic, choir, pop production, clean production, bright, uplifting, handclaps, funk guitar, wah pedal, fretless bass, disco, dream pop, shoegaze, ambient, spoken word, whispered vocal, double-tracked vocal, industrial noise wall, orchestral swell, key change
```

**What was added beyond the vault's four items:** `guitar sustain intro` (present in siblings, absent here — flagged, not silently absorbed), the full guitar ban block, the synth-lane bans, `surf` (new — because spring reverb was kept on the lead), the ballad-avoidance family, the sinister family, the chant family, the no-build family, and `fade out, fade ending` to protect the outro.

---

## 4. Title metadata

- **Title:** `Take Me Back? (Synth Conversion Reference)`
- **Fallback:** `Take Me Back (Synth Reference)`

The `?` earns its place: every chorus is a plea with an unanswered question, the final chorus closes on a full stop, and the outro repeats the plea four times with no reply. Titled without the mark it is a statement of intent; with it, it is a question the narrator never gets answered. **Needs a Principal ruling before DistroKid metadata.**

---

## 5. Creative sliders

**Mode:** Custom, no audio upload.

| Control | Value | Mode | Reasoning |
|---|---|---|---|
| **Weirdness** | **30%** | Custom | Guitar bleed diagnostic must stay clean; this song adds a second failure mode (sinister vs wistful), and 30% keeps that judgement in the prompt rather than the model's mood. |
| **Style Influence** | **75%** | Custom | The tag set is doing three jobs — guitar ban, ballad ban, sinister ban. Only holds enforced hard. |
| **Audio Influence** | **n/a — slider absent** | Custom (no upload) | Cover-mode if used later: **65%**. |
| **Variety** | **Off (0)** | Custom | Rewrites the style prompt and would strip the guitar exclusions and substitution map. |

**Max Mode: ON.** **Personalize: off.**

**The first documented BPM does not change the values.** A documented 148 converts tempo from a guess into a hard constraint, which argues *for* Style Influence staying at 75. The new failure mode a fast tempo introduces is tempo drift, and drift is diagnosed most cleanly at low weirdness.

**Retry:** conventional/guitar → Weirdness 45%. Wooden or chorus won't open → Style Influence 65% (never above 85%). Sinister → not a slider; check for noise bed or whispered double, re-roll. Soft/ballad → not a slider; check for piano, bell, or pad leading, re-roll.

---

## 6. Lyrics field — verbatim from vault

```
[Verse 1]
The world runs wild
Like a loose-wire kite
Skips through smoke
And bites the night

We were paper boats
On a backyard stream
Laughing at the storm
Like it was just a dream

[Pre-Chorus]
Now the sky feels hard
And the roads don't sing
I miss that child
Who believed in everything

[Chorus]
Take me back
Take me back
To the simple spark
To the open map
To the world of make believe

Take me back
Take me back
When we ran so free
When we slept 'til three
When it was just you and me

[Verse 2]
Now every door
Has a lock on fear
Every grin looks tired
Every day feels near

To a breaking glass
To a waiting crack
I want your fearless eyes
And the old world back

[Pre-Chorus]
Back when rain was gold
On a tin roof shine
Back when we could lose
And still feel fine

[Chorus]
Take me back
Take me back
To the simple spark
To the open map
To the world of make believe

Take me back
Take me back
When we ran so free
When we slept 'til three
When it was just you and me

[Bridge]
Give me the swing
Of a crooked swing set
Mud on our shoes
And a day we won't forget

Before the names
Before the weight
Before we learned
To close the gate

[Final Chorus]
Take me back
Take me back
To the simple spark
To the open map
To the world of make believe

Take me back
Take me back
When we ran so free
When we slept 'til three
When it was just you and me

[Outro]
Take me back
Take me back
Take me back
Take me back
```

No lyric text altered. No label added or removed. `[Final Chorus]` preserved as written (non-canonical; fallback `[Chorus]` if Suno mishandles it).

---

## 7. Arrangement notes

### The [Outro] — series first, and the song's last word

No previous song in this series had a written ending. Here it is specified: four naked repeats, nothing after them.

This must be the most exposed moment in the track, not a fade. The wall drops away after the final chorus and the baritone is left alone — voice, plus at most one sustained sub tone. Four repeats, dry-ish, the last allowed to sit in the room rather than resolve.

The final chorus already ends on `just you and me` — a full stop. The outro then refuses to stop. That is the point of the song: the question in the title is never answered, and the outro is where the not-answering lives. **Losing the outro to a fade deletes the argument.**

### The doubled hook — escalation without chant

`Take me back / Take me back` opens both blocks of every chorus, three passes. Identical text three times is a real risk: Suno renders identical blocks identically, and a repeated pair rendered as two hard stabs becomes a chant.

1. **Phrasing:** one phrase breathed through, legato, second repeat equal or softer. Two syllables, one gesture.
2. **Accumulation:** each pass adds a layer while the vocal delivery stays the same. Escalation happens around the voice, not in it. The voice getting louder is what turns a plea into a slogan.
3. **Exclusions:** `gang vocals, chant, group shout, crowd vocals, call and response` all excluded.

### Pre-chorus — the ground giving way, not a build

The documented pre-chorus is four lines of loss. The wrong render turns it into a lift into the chorus. The intended move is **subtraction**: drums drop out, sub narrows, the voice is left more exposed, harmony suspends before the chorus lands on the tonic. A riser, snare roll, or filter sweep is the failure.

The second pre-chorus (`Back when rain was gold`) is possibly the most exposed vocal moment before the bridge — same section type with the opposite content, present-tense loss then past-tense warmth. It should be the quietest full-band moment on the track.

### Bridge — plain, not cute

`Give me the swing / Of a crooked swing set / Mud on our shoes` is the most childlike line in the series. It must stay plain-spoken inside the industrial palette. A music box, celesta, or nursery-rhyme cadence here is a reject.

---

## 8. Suno role verification

**Suno-assist (PRD 5.4). master_source = studio.** Reference render only. Baritone male descriptors carried; `female vocal` and `tenor vocal` excluded. Any Suno audio beyond listening reference must come from an active paid tier (Premier on record; no retroactive rights on free-tier output).

---

## 9. Compatibility checklist

| # | Check | Result |
|---|---|---|
| 1 | Style prompt present | PASS |
| 2 | Lyrics verbatim | PASS |
| 3 | Section labels per spec | PASS with flag — `[Final Chorus]` non-canonical, preserved |
| 4-6 | Title Case, line breaks, title field | PASS |
| 7 | Negative prompt present | PASS |
| 8 | Suno role verdict | PASS |
| 9 | Out-of-vocabulary tags flagged | PASS |
| 10 | Per-artist structure | PASS |
| 11 | Key and time signature as explicit fields | PASS with flag — both UNVERIFIED |
| 12 | All four sliders specified | PASS |

**Overall: PASS.**

---

## 10. Audition notes — in priority order

1. **Sinister test.** Threatening rather than sad = failed, however good it sounds. Listen for noise bed, siren/drone pad, whispered/double-tracked vocal, clustered dissonant stabs.
2. **Soft test.** Chorus must gain weight over the verse. Any piano, string pad, bell, celesta, or music box = immediate fail.
3. **Guitar bleed.** 200-500 Hz for strummed guitar body.
4. **Tempo drive.** 148 is the fastest documented tempo in the series and darkwave defaults slow. Verse must be carried by a sequenced gated pulse at 148, not a padded sustain. Compare against the clock, not against feel.
5. **Pre-chorus — subtraction, not build.** Riser, snare roll, filter sweep = failure.
6. **Doubled hook — no chant.** One legato phrase; two hard identical stabs or a group shout = reject.
7. **Outro — the made-or-lost moment.** Last fifteen seconds: four naked repeats, drums gone, no wall, no fade.
8. **Bridge — plain, not cute.**
9. **Verse 2 label collision.** `To a breaking glass / To a waiting crack` are chorus-shaped fragments inside a verse — Suno may jump early into the chorus shape. Re-roll, do not edit.
10. **`slept 'til three`.** Check the elision survives; awkward `until three` is a delivery artifact, re-roll.
11. **Vocal.** Deep baritone, upfront. Reject tenor or polished pop-baritone first.
12. **Intro.** Gated saw-bass pulse or single metallic hit — never a swelling pad.

---

## 11. Open items for the Principal

1. **Rule on the `?`** — deliberate or not, before it reaches DistroKid metadata.
2. **Vault exclude list** — add `guitar sustain intro` for series consistency.
3. **Vault frontmatter** — add `key`, `time_signature`, `bpm` fields; key and meter as `UNVERIFIED — not documented`.

---

## 12. Lineage

- Song facts and lyrics: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/take-me-back.md`
- Series reference: `docs/2026-10-30-sad-song-velvut-synth-conversion-suno-prompt.md`
- Prompt spec: `.a0proj/skills/suno-prompt-compatibility-spec/SKILL.md`
- Role matrix: `.a0proj/skills/suno-integration/SKILL.md` (PRD 5.4)
