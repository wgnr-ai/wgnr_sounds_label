---
last_updated: 2026-10-30T17:44:00
status: delivered
artist: Velvut
song: These Phantom Walls
series_position: 11
route: suno-synth-re-render
tempo: 92
key: UNVERIFIED — not documented
key_quality: minor — DOCUMENTED ('minor key' in style notes)
time_signature: UNVERIFIED — not documented
vocal_range: F2-D4
suno_role: assist
direction_status: approved
master_source: studio
---

# THESE PHANTOM WALLS (Velvut) — Synth Conversion Suno Prompt Set

**Artist:** Velvut · **Song:** These Phantom Walls · **Date:** 2026-10-30 · **Series:** song 11
**Route:** Suno synth re-render (reference only) · **Purpose:** arrangement direction for the GarageBand rebuild

---

## 0. This song breaks the series palette in three documented ways

This is the first song in the series where the **source material contradicts the established synth palette**, rather than merely adding to it. Three documented instructions have no home in the palette as built:

| Documented | Conflicts with | Consequence |
|---|---|---|
| `no syncopation` | `gated sequenced saw-bass pulses` (every prior song) | The gate is inherently syncopated. It cannot be used here. |
| `straight quarter-note downstrokes` | anything sequenced, stuttered, or 16th-based | Quarter notes, on the beat, unbroken. |
| `long sustained wall-of-sound drone chords` | `detuned saw stack stabs` (hard attack, every prior song) | Stabs are the opposite of sustain. Pads and drones lead instead. |

**These are not stylistic preferences. They are written instructions in the source file, and they are specific.** The prompt below obeys all three, which makes it the least like the other ten songs in the series.

**If the goal is a coherent Velvut synth album, this song is the outlier** — and it should be. A 92 BPM song with no syncopation and sustained drones is a different animal from a 148 BPM stutter-gate song, and forcing the palette onto it would break the song to preserve the series.

### Second deviation: the pre-chorus has no lyrics

`[Pre-Chorus Lift]` contains exactly one direction — `[Guitars build]` — and **no sung lines**. It is a purely instrumental section between verse 2 and the first chorus. There is nothing to sing there; the build is the content.

### Two documented assets

- **92 BPM is real.** A confirmed tempo in a series where most songs have none. This is the slowest confirmed Velvut tempo on record (against 147, 148, and 107).
- **`heavy tom-tom drums groove` plus `[Drop to Tom-Tom groove]`** — tom-tom is named twice. It is the defining percussion character, not a decoration.

---

## 1. Verified song facts

Source: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/these-phantom-walls.md` (read direct 2026-10-30, file last_updated 2026-08-16, status draft).

| Field | Value | Status |
|---|---|---|
| Title | **These Phantom Walls** — no question mark | DOCUMENTED |
| Tempo | **92 BPM** | **DOCUMENTED** — written in style notes |
| Key | **UNVERIFIED — not documented** | No key name anywhere |
| Key quality | **minor — DOCUMENTED** (`minor key`) | Quality known, name unknown |
| Meter | **UNVERIFIED — not documented** | — |
| Album | `TBD` | — |
| Recording state | `draft` | — |
| Style notes (verbatim) | post-alternative rock, alt-metal, 92 BPM, low baritone male vocals, heavy tom-tom drums groove, spring reverb, quiet loud dynamics, minor key, straight quarter-note downstrokes, long sustained wall-of-sound drone chords, no syncopation | DOCUMENTED |
| Structure | V1 → V2 → Pre-Chorus (instrumental) → C → V3 → Bridge → C → Solo → C → Outro → Abrupt End | DOCUMENTED |
| Vocal | `low baritone male vocals` — song-level. Artist range F2–D4 | DOCUMENTED |
| Inline directions | **13** — see §4b | DOCUMENTED |

### What the style notes give us that no other file has

Three of these phrases are **negative instructions**, which are rare and unusually valuable:

- **`no syncopation`** — tells us what not to do, explicitly.
- **`straight quarter-note downstrokes`** — names the exact rhythmic subdivision.
- **`long sustained wall-of-sound drone chords`** — names the exact note length.

Together they describe a rhythmic identity precisely enough that the main uncertainty left is timbre, not feel. That is a better starting position than Glass Horizon or Feeling Alone, which had only dynamics.

---

## 2. Style prompt — paste into Style of Music

```
dark industrial synth-rock, electro-industrial, post-alternative weight, alt-metal heft, slow crush, claustrophobic, entrapped, 92 BPM, minor key, distorted synth bass, straight quarter-note synth-bass downstrokes, no syncopation, unsequenced, long sustained wall-of-sound drone chords, hard analog synth pads, slow-attack detuned saw pads, filtered mono-synth lead with portamento, metallic industrial percussion, heavy tom-tom drums groove, programmed kick with weight, spring reverb, quiet loud dynamics, wall-of-sound choruses, sub-bass weight, analog tape saturation, room reverb, low baritone male vocal upfront, melodic rap bridge delivery, memorable chorus hook, abrupt cut ending
```

### The three palette breaks, resolved

| Instruction | What replaces the series default |
|---|---|
| `no syncopation` | **No gated sequencer. No 16th stutter. No off-beat accents.** The bass plays quarter notes and nothing else. `unsequenced` is written into the prompt to reinforce it. |
| `straight quarter-note downstrokes` | Carried almost verbatim as `straight quarter-note synth-bass downstrokes`. The word *downstroke* is a guitar term; it is kept because it describes the attack direction, and the prompt already bans the instrument. |
| `long sustained wall-of-sound drone chords` | `long sustained wall-of-sound drone chords` + `slow-attack detuned saw pads`. **Stabs are out.** The hard-attack stack from every prior song is replaced by slow attack and long sustain. |

### What the palette keeps

Everything structural survives: the dark industrial base, the distorted synth bass, the mono-synth lead as the guitar-lead substitute, the industrial percussion, sub-bass weight, tape saturation, and the baritone vocal at the front. **The song still sounds like the series. It just does not move like it.**

### The 92 BPM consequence

92 BPM with straight quarters and no syncopation is a **slow, deliberate march**. There is no rhythmic interest to hide behind — every element is exposed on the beat, and any timing error is audible immediately.

That is why `no syncopation` is the most important instruction in this file and the one most likely to be violated. Suno's default behaviour at a slow industrial tempo is to add a gated pulse to create movement. **Here, that movement is the error.**

### Melodic rap — kept this time

Glass Horizon's `[Melodic Rap Delivery]` was converted to `spoken-rap` because that song had no documented key and no documented tempo, so there was no way to know whether a melodic climb would exceed the D4 ceiling.

**This song keeps the melodic rap.** 92 BPM is slow — a melodic bridge line has time to move without climbing. The range risk that forced the change on Glass Horizon does not exist at this tempo. `melodic rap bridge delivery` is written into the prompt, not `spoken-rap`.

That is a per-song decision, not a reversal. The constraint that drove it on Glass Horizon is absent here.

### The `alt-metal` trap

Documented, and it is the same era risk as Glass Horizon's Y2K and Feeling Alone's 90s alt metal. Suno reads *alt-metal* as a guitar tone and a production era — drop tuning, dry cabs, a specific mid bite.

The phrase appears as **`alt-metal heft`** (mass, not genre) and the literal terms are excluded in §3.

### Vocal handling

`low baritone male vocals` — the word is **low**, not just baritone. That is more specific than the series baseline and it is carried as `low baritone male vocal upfront`.

At 92 BPM the vocal has room. F2 is the floor and nothing in this lyric pushes toward the ceiling — the highest-risk moment is the melodic rap bridge, and at this tempo that is manageable.

---

## 3. Exclude styles — paste into Exclude

**Core:**

```
tenor vocal, country, melodramatic, classic rock, guitar sustain intro, electric guitar, acoustic guitar, rhythm guitar, lead guitar, power chords, palm-muted chugs, guitar solo, guitar amp, synthwave, retro 80s, clean synth-pop, electro-pop, female vocal, polished, mastered, final
```

**Extended:**

```
dance-pop, chiptune, vaporwave, 8-bit, orchestral, symphonic, choir, pop production, clean production, bright, soft, ballad, sentimental, uplifting, handclaps, funk guitar, wah pedal, fretless bass, disco
```

**Song-specific additions — required, not optional:**

```
syncopated, syncopation, off-beat accents, gated sequencer, stutter gate, sixteenth-note pulses, sequenced bassline, arpeggiated synth, EDM, four-on-the-floor, big room, trance, dubstep, grunge, 90s, 1990s, alternative metal, nu-metal guitar tone, drop-tuned guitars, guitar feedback, numetal, rapcore, screaming vocals, harsh vocals, anthemic, stadium rock, triumphant, victorious, uplifting chorus, major-key resolve, key change up, fade out, fade ending, resolving outro, final chord resolve, ambient outro, bright lead synth above the vocal
```

**Why each block exists:**

1. `syncopated, syncopation, off-beat accents, gated sequencer, stutter gate, sixteenth-note pulses, sequenced bassline, arpeggiated synth` — **the highest-stakes block in the set.** The source file says `no syncopation` explicitly. Suno will add rhythmic interest at a slow tempo unless prevented. Eight terms exist to prevent it.
2. `EDM, four-on-the-floor, big room, trance, dubstep` — the other way Suno creates movement at 92 BPM. A slow stomp with a synth bass is one decision from a club record.
3. `grunge, 90s, 1990s, alternative metal, nu-metal guitar tone, drop-tuned guitars, guitar feedback` — the era trap from §2.
4. `numetal, rapcore, screaming vocals, harsh vocals` — the melodic rap bridge is a delivery instruction, not a genre invitation. Nu metal is the most likely wrong turn.
5. `anthemic, stadium rock, triumphant, victorious, uplifting chorus, major-key resolve, key change up` — the chorus is a question, not a declaration: `Am I still here? Is this my fate?` A victorious setting answers a question the lyric leaves open.
6. `fade out, fade ending, resolving outro, final chord resolve, ambient outro` — **the vault says `[Abrupt End]`.** Hard requirement.
7. `bright lead synth above the vocal` — the D4 ceiling guard, standard across the series.

---

## 4. Lyrics field

### 4a. Field-ready block — paste this into Suno

**All sung words byte-identical to the vault. 13 inline directions stripped, 4 section labels normalised** (all mapped in §4b).

```
[Intro]

[Verse 1]
These four walls they seem closer now
It's like I feel their breath on me somehow
Every tick from the clock hits like a nail
Driving in the hours down the same old trail

[Verse 2]
The shadows stretch across the floor
Like iron bars across a heavy door
I hear the floorboards groan beneath the weight
Of every second that I sit and wait

[Pre-Chorus]

[Chorus]
These phantom walls, a room I never chose
The longer I stay the more of me goes
Tell me there’s a door, or tell me straight
Am I still here? Is this my fate?
These phantom walls.

[Verse 3]
The dirty window stains the afternoon
A hollow world that’s entirely out of tune
I trace the dark across a lonely shelf
A total stranger talking to myself

[Bridge]
This heavy air
Won't leave my chest
It locks me down
Won't let me rest

I hunt for seams
A chip, a crack
A broken edge
To claw me back

[Chorus]
These phantom walls, a room I never chose
The longer I stay the more of me goes
Tell me there’s a door, or tell me straight
Am I still here? Is this my fate?
These phantom walls.

[Instrumental Break]

[Chorus]
These phantom walls, a room I never chose
The longer I stay the more of me goes
Tell me there’s a door, or tell me straight
Am I still here? Is this my fate?

[Outro]
These phantom walls, a room I never chose
The longer I stay the more of me goes
Tell me there’s a door, or tell me straight
Am I still here? Is this my fate?
These phantom walls.
These phantom walls.
```

### 4b. Every change, and where it went

**Section labels normalised (4):**

| Vault | Field-ready | Reason |
|---|---|---|
| `[Solo Drum Intro]` | `[Intro]` | Canonical label. **The drum-only concept is preserved** in §5 — this is a real instruction, not a formatting fix. |
| `[Pre-Chorus Lift]` | `[Pre-Chorus]` | Canonical. The word *lift* moves to §5. |
| `[Guitar Solo]` | `[Instrumental Break]` | No guitar exists; the mono-synth lead takes the role. |
| `[Abrupt End]` | *removed* | Not a lyrics-field construct. Carried as `abrupt cut ending` in the prompt and enforced in §5. |

**Inline directions stripped (13):**

| Vault bracket | Disposition |
|---|---|
| `[Guitar enters]` | Dropped — obsolete, no guitar. |
| `[Simple driving downstrokes on the beat]` | → prompt: `straight quarter-note synth-bass downstrokes` |
| `[Guitars build]` | → §5. The pre-chorus build is arrangement; Suno cannot build an empty section on command. |
| `[Wall of sound guitars]` | → prompt: `wall-of-sound choruses` |
| `[Sustained ringing drone chords]` | → prompt: `long sustained wall-of-sound drone chords` + `slow-attack detuned saw pads` |
| `[Quiet loud dynamics]` | → prompt: `quiet loud dynamics` |
| `[Drop to Tom-Tom groove]` | → prompt: `heavy tom-tom drums groove` |
| `[Melodic Rap Delivery]` | → prompt: `melodic rap bridge delivery` — **kept, not converted** (see §2) |
| `[Unexpected chord progression]` | → **not carried.** No key documented; unexpected harmony on an undetermined key invites random modulation. Flagged in §5. |
| `[Anthemic]` | → prompt: `wall-of-sound choruses`. The word itself is excluded (see §3 item 5). |
| `[Explosive chords]` | → prompt: `wall-of-sound choruses` |
| `[Octave lead guitar]` | → prompt: `filtered mono-synth lead with portamento`; octave doubling carried in §5 |
| `[Explosive Outro]` | → prompt: `abrupt cut ending` |

### Structural flags — preserved as written

1. **Chorus 3 withholds the tag.** Choruses 1 and 2 and the outro all end with `These phantom walls.` — the third chorus does not. It stops on `Am I still here? Is this my fate?` Preserved exactly. This is the same withheld-phrase device as Glass Horizon, and it is what makes the doubled tag in the outro land.
2. **The pre-chorus is empty.** No lyric lines at all. Preserved as an empty label, not deleted.
3. **The outro is a fifth chorus with an extra tag.** It repeats the full chorus, then adds `These phantom walls.` twice. Structurally the song has five chorus statements, not three.
4. **Mixed apostrophes.** `It's` and `Won't` are straight; `there’s` and `that’s` are typographic. Preserved exactly — invisible to Suno, visible to DistroKid lyric submission later.
5. **`Tell me there’s a door, or tell me straight`** — *tell me straight* means be direct. Not a defect.

---

## 5. Arrangement notes

### Five chorus statements, and only one withholds the tag

| Pass | Position | Arrangement |
|---|---|---|
| 1 | After pre-chorus | First payoff. Full drone stack, tom-toms driving. Tag lands. |
| 2 | After bridge | Heaviest. The bridge exit releases into this one. Tag lands. |
| 3 | After instrumental break | **Tag withheld.** Ends open on the question. Do not fill the gap. |
| 4 (`[Outro]`) | End | Full chorus, tag lands, then **tag repeated once more** — `These phantom walls.` twice, then cut. |

All chorus lines across all passes are byte-identical. The only textual variation in the entire song is the withheld tag on pass 3 and the doubled tag on pass 4.

### The pre-chorus is the build, and it has no words

This is the arrangement's hardest ask. `[Guitars build]` sits under an empty section — on the original, a guitar would have risen across those bars and delivered the chorus.

**In the rebuild:** the build is carried by the pads and the tom-toms, not by a lead. Long sustained drone chords swell; the tom-tom pattern intensifies; nothing else enters. **Do not add a lead line to fill the emptiness.** The emptiness is the point — the listener waits for the chorus.

Suno cannot reliably execute an empty built section. Expect the render to either skip it or fill it. Judge the concept, not the execution.

### The tom-tom groove is named twice

`heavy tom-tom drums groove` in the style notes and `[Drop to Tom-Tom groove]` in verse 3. Two mentions means it is the song's percussion identity, not a colour.

**In practice:** the tom-toms should be audible as the dominant drum voice in the verses, not buried under a kick-and-snare pattern. Verse 3 drops further into them.

### No syncopation — the discipline

At 92 BPM with nothing syncopated, the song has no rhythmic friction. Everything lands on the beat.

**This is the hardest instruction in the set for Suno to honour**, because the default fix for a slow industrial track is a gated pulse. The exclusions block eight rhythmic terms for this reason. If the render has a stutter, a gate, or an off-beat accent, the take is wrong regardless of how good it sounds.

### The instrumental break

`[Guitar Solo]` + `[Octave lead guitar]`, same as Glass Horizon. The mono-synth lead plays the solo line doubled at the octave. Short — a bridge to the final chorus, not a showcase.

### `[Unexpected chord progression]` is not enforced

With no documented key there is no target to hit, and a prompt asking for unexpected harmony on an undetermined key invites a random modulation. Dropped here rather than silently ignored.

### Ending

`[Abrupt End]` is written. **Cut after the second `These phantom walls.`** A ring-out on the drone is tempting and wrong — the drone is the thing the song is trapped inside. Letting it fade means the walls win by default. Cutting means they stay walls.

---

## 6. Creative sliders

**Mode:** Custom, no audio upload. Values held at series standard.

| Control | Value | Mode | Reasoning |
|---|---|---|---|
| **Weirdness** | **30%** | Custom | The failure mode is rhythmic, not tonal — Suno adding syncopation. Low weirdness makes an added gate a readable prompt fault rather than variance. |
| **Style Influence** | **75%** | Custom | The eight-term no-syncopation block and the era block both have to hold hard. This is the song where prompt adherence matters most, because the default behaviour actively fights the instruction. |
| **Audio Influence** | **n/a — slider absent** | Custom (no upload) | Cover-mode value if the demo is used as reference later: **65%**. |
| **Variety** | **Off (0)** | Custom | Would rewrite the style prompt server-side and strip the no-syncopation block — the single instruction this song cannot lose. |

**Max Mode: ON.** **Personalize: off.**

**Retry ladder:**

- Syncopation or a gated pulse appears → the primary failure. Re-roll before touching sliders; if it persists, Style Influence 85%.
- Reads as a club or EDM track → check for `four-on-the-floor` or `trance` bleeding in; re-roll.
- Grunge / alt-metal guitar tone → Style Influence 85%.
- Tempo drifts far from 92 → 92 BPM is documented and is written in the prompt. Check it is present before assuming drift is unavoidable.
- Anthemic chorus → `anthemic` and `triumphant` are excluded; if it still reads victorious, weaken `wall-of-sound choruses` and re-roll.

---

## 7. Tempo, key, meter

### Tempo — documented

**92 BPM, written in the style notes.** Not inferred. It is carried verbatim into the prompt.

This is the slowest confirmed Velvut tempo on record (against 147, 148, and 107). **Do not A/B this render against the other songs for energy** — it is meant to be slower and heavier.

### Key — quality documented, name not

`minor key` is in the style notes. **Which minor key is not recorded anywhere** — no frontmatter field, no detector reading, no MIDI evidence.

The prompt carries `minor key` exactly as documented, plus the exclusions ban `major-key resolve` and `key change up`. **No key name is written, and none should be** — the frontmatter records the key as UNVERIFIED — not documented, with a separate `key_quality` field recording the documented minor quality.

### Meter — undocumented

No time signature anywhere. `straight quarter-note downstrokes` suggests a regular metre without stating one. **Not inferred.**

---

## 8. Suno role verification + compatibility checklist

**Suno-assist (PRD §5.4). `master_source = studio`.** `status: draft`, no recording referenced. Arrangement reference for a song not yet recorded. Not a release master, not a demo replacement.

Low baritone male vocal carried (`low baritone male vocals`), plus `melodic rap bridge delivery`. `female vocal` and `tenor vocal` excluded. `polished, mastered, final` excluded.

| # | Check | Result |
|---|---|---|
| 1 | Style prompt present | PASS |
| 2 | Lyrics verbatim from vault | **PASS WITH FLAGS** — every sung word byte-identical; 13 inline directions stripped (mapped in §4b) |
| 3 | Section labels per spec | **PASS WITH FLAG** — 4 normalisations: `[Solo Drum Intro]`→`[Intro]`, `[Pre-Chorus Lift]`→`[Pre-Chorus]`, `[Guitar Solo]`→`[Instrumental Break]`, `[Abrupt End]` removed |
| 4 | Labels Title Case | PASS |
| 5 | Line breaks per spec | PASS |
| 6 | Title field present | PASS — no question mark |
| 7 | Negative prompt present | PASS |
| 8 | Suno role verdict | PASS — Suno-assist |
| 9 | Out-of-vocabulary tags flagged | **PASS WITH FLAGS** — `no syncopation` and `unsequenced` are negative instructions, unusual in a style prompt; *post-alternative weight*, *alt-metal heft*, *slow crush* as non-standard vocabulary |
| 10 | Per-artist structure | PASS — Velvut |
| 11 | Key and time signature as explicit fields | **PARTIAL — tempo DOCUMENTED (92), key quality DOCUMENTED (minor), key name and meter UNVERIFIED.** Recorded exactly as such; nothing inferred |
| 12 | All four sliders specified | PASS |

**Overall: PASS WITH FLAGS.** Check 11 is the strongest of any gap song — a real tempo and a real key quality, but still no key name or meter.

---

## 9. Audition notes

1. **Syncopation test — the primary judgement call.** If there is a gate, a stutter, an off-beat accent, or a 16th-note pulse anywhere, the render has failed the song's most explicit instruction. This outranks every other note.
2. **Tempo test.** 92 BPM, and it should feel slow and deliberate, not sluggish. If it drags, check whether the drums are carrying the march — tom-toms and kick, on the beat.
3. **Drone test.** The chords should be sustained and swelling, not struck. If the choruses have hard stabs, the palette from the other songs leaked in.
4. **The empty pre-chorus.** Expect Suno to skip or fill it. If it fills it with a lead line, that is a concept failure — note it, do not accept it as the intended build.
5. **The bridge.** Melodic rap, at 92 BPM, with room to move. If it comes back as speech or as a shouted rap, the delivery instruction was lost.
6. **Five chorus statements.** All identical words. Expect flattening. The one variation that matters is pass 3 withholding `These phantom walls.`
7. **The ending.** Hard cut after the second tag. A fade, a ring-out, or a resolve is a fail. The drone must stop.

---

## 10. Lineage

- Song facts, lyrics, inline directions, tempo and key quality: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/these-phantom-walls.md` (read direct 2026-10-30)
- Vocal range and artist identity: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/artist-facts.md`
- Label-normalisation precedent: `docs/2026-10-30-maybe-meet-someday-velvut-synth-conversion-suno-prompt.md` (Principal ruling 2026-10-30)
- Melodic-rap divergence from: `docs/2026-10-30-glass-horizon-velvut-synth-conversion-suno-prompt.md` (that song converted to spoken-rap for range reasons absent here)
- Series reference: `docs/2026-10-30-sad-song-velvut-synth-conversion-suno-prompt.md`
- Prompt spec: `.a0proj/skills/suno-prompt-compatibility-spec/SKILL.md`
- Role matrix: `.a0proj/skills/suno-integration/SKILL.md` (PRD §5.4)
- DAW guide: `docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md`
