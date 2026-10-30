---
last_updated: 2026-10-30T17:43:00
status: delivered
artist: Velvut
song: Under My Skin
series_position: 6
route: suno-synth-re-render
tempo: 147
key: C# minor
time_signature: UNVERIFIED — not documented
vocal_range: F2-D4
suno_role: assist
direction_status: approved
master_source: studio
---

# UNDER MY SKIN (Velvut) — Synth Conversion Suno Prompt Set

**Artist:** Velvut · **Song:** Under My Skin · **Date:** 2026-10-30 · **Series:** song 6
**Route:** Suno synth re-render (reference only) · **Purpose:** direction reference for the GarageBand rebuild

**Principal ruling 2026-10-30:** lyrics version **(B)** approved for the render. Version (A) is what the vault file holds.

---

## 0. Status: applied vs open

| Item | State |
|---|---|
| Style prompt (guitar-free, 147 BPM, C# minor) | DELIVERED |
| Lyrics field — version (B) | **APPROVED by Principal 2026-10-30** |
| Lyrics field — version (A) | Retained below as the vault's current state |
| Negative prompt | DELIVERED |
| Title metadata | DELIVERED |
| Creative sliders (all four) | DELIVERED — held at series values |
| Compatibility checklist | PASS |
| **OPEN — vault file still holds version (A)** | Not edited. Vault is Principal-owned. |
| **OPEN — vault frontmatter gap** | No `tempo`, `key`, or `time_signature` fields; values exist only in the free-text Style Notes line. |
| **OPEN — chord progression not documented** | Style Notes say 'surprising chord changes' only. No progression recorded. None invented. |

---

## 1. Verified song facts

Source: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/under-my-skin.md` (read direct 2026-10-30).

| Field | Value | Status |
|---|---|---|
| Tempo | **147 BPM** | DOCUMENTED |
| Key | **C# minor** | DOCUMENTED |
| Time signature | **UNVERIFIED — not documented** | No value in file. Not inferred. |
| Vocal | Deep baritone male, upfront | DOCUMENTED |
| Frontmatter | last_updated 2026-09-18T19:32:00, status: draft, album: TBD | Read direct |
| Style notes (verbatim) | alt-rock with nu-metal and industrial rock influences, 147bpm, c# minor, chugging rhythm, deep baritone male vocals, memorable chorus hook, melodic with surprising chord changes | DOCUMENTED |
| Exclusions | **None recorded in this file** | Read direct |
| Suno role | Suno-assist (PRD 5.4) — master_source = studio | DOCUMENTED |

**First song in the series with BOTH tempo and key documented.**

---

## 2. Style prompt — paste into Style of Music

### Primary

```
dark industrial synth-rock, darkwave, electro-industrial, heavy, driving, 147 BPM, C# minor, distorted synth bass, heavy distorted synth-bass groove, gated sequenced saw-bass pulses, sixteenth-note stutter gate, detuned saw stack stabs, hard analog synth pads, aggressive mono-synth lead with portamento, metallic industrial percussion, noise-scrape textures, programmed kick with weight, quiet verses, wall-of-sound choruses, back-to-back final choruses, no breakdown, no bridge, deep baritone male vocal upfront, gritty baritone delivery, staccato clipped verse delivery, memorable chorus hook, surprising chord changes, harmonic movement in the pads, plate reverb on final hit, hard cut ending
```

### Short fallback (if the field truncates)

**UNVERIFIED:** the exact Style field character cap is not documented in the compatibility spec. If the interface clips the Primary prompt:

```
dark industrial synth-rock, darkwave, electro-industrial, 147 BPM, C# minor, heavy distorted synth-bass groove, gated saw-bass sequencer, detuned saw stabs, metallic percussion, mono-synth lead, deep gritty baritone male vocal, wall-of-sound choruses, surprising chord changes, hard cut ending
```

### Substitution map (inherited)

| Original role | Synth replacement |
|---|---|
| Chugging rhythm guitar | distorted synth bass + gated sequenced saw-bass pulses + 16th stutter gate |
| Rhythm power chords | detuned saw stack stabs + hard analog synth pads |
| Lead or wailing guitar | aggressive mono-synth lead with portamento |
| Tom and kit weight | metallic industrial percussion + programmed kick with weight |
| Guitar scratch (outro) | noise-scrape texture + plate-reverb final hit |
| Guitar sustain intro | intentionally absent — open on the gated pulse |

### Three production decisions

**1. The word 'chugging' is deliberately absent from the style prompt.** It is documented twice — in Style Notes and in the Verse 1 parenthetical — and it is guitar vocabulary that reliably pulls a palm-muted guitar at 147 BPM. The rhythm concept survives as `gated sequenced saw-bass pulses` + `sixteenth-note stutter gate`. The word is banned. Translation, not deletion: the chug attack is preserved, its instrument is not.

**2. The saw pulse is specified as 8th-note gated with 16th-note stutter accents — not flat 16ths.** At 147 BPM, unbroken 16th-note saw pulses read as EBM/four-on-the-floor stomp, which is not the target and competes with the programmed kick. The 8th-note bed keeps the chug weight; the 16th stutter provides the attack transient where the guitar chug would have been.

**3. 'Heavy bass groove' transfers with zero translation — it is the one gift in the file.** The Verse 2 parenthetical documents it and the Style Notes corroborate it. It becomes `heavy distorted synth-bass groove` verbatim.

### The harmonic risk — structural answer

This is the most likely casualty of the conversion, so the answer is structural, not a tag:

- **The sequenced saw bass does NOT carry harmony.** It pedals on C#. A 147 BPM sequencer given chord responsibility reduces every progression to root-fifth-eight — which is precisely how 'surprising chord changes' becomes a four-chord loop.
- **The hard analog pads carry the real voicings**, held rather than stabbed, so extension tones sound.
- **The mono-synth lead arpeggiates through the extension notes** so the harmony stays audible even over a static bass.
- **`harmonic movement in the pads` is a positive instruction** in the prompt, not just an absence.

The actual progression is **not documented** — the file says only *surprising chord changes*. If the guitar-version chords exist, the rebuild should preserve them note-for-note, and the pads are where they live.

---

## 3. Lyrics field

### Version (B) — APPROVED by the Principal 2026-10-30

Only production parentheticals changed. Sung lyrics byte-identical to the vault.

```
[Verse 1]
(Staccato gated pulse, clipped delivery)
Poking holes in my skin
Paper face cheap grin
Same game same lies
Your static screams in my eyes

You don't belong in my head
Shut it down leave it dead
Out of time out of your mind
I've had enough of your kind

[Pre-Chorus]
(Tension building, industrial rise)
Here comes that buzz in the wire
In the wire
Hands on the gate getting tighter
Getting tighter
Too close now I can taste it
One more move and I break it

[Chorus]
(Explosive lift, full synth wall, powerful vocals)
Under my skin
You won't get in
Under my skin
Burn it down let the rage begin
Under my skin
Under my skin

[Verse 2]
(Heavy bass groove, gritty delivery)
Boots on the floor back in the frame
Same dead stare same fake name
Hands at the door prying at the seams
Trying to crawl through the cracks in my machine

I keep it locked I keep it sealed
No room left for whatever you deal
Every step you take gets cut clean through
I spit out the noise I shut down you

[Pre-Chorus]
(Tension building, industrial rise)
Here comes that buzz in the wire
In the wire
Hands on the gate getting tighter
Getting tighter
Too close now I can taste it
One more move and I break it

[Chorus]
(Explosive lift, full synth wall, powerful vocals)
Under my skin
You won't get in
Under my skin
Burn it down let the rage begin
Under my skin
Under my skin

[Chorus]
(Maximum energy)
Under my skin
You won't get in
Under my skin
Burn it down let the rage begin
Under my skin
Under my skin

[Outro]
(Abrupt industrial cut, metallic noise-scrape, dead silence)
```

### Change log for (B)

| # | From | To | Rationale |
|---|---|---|---|
| 1 | `(Staccato, chugging rhythm)` | `(Staccato gated pulse, clipped delivery)` | Keeps staccato + the chug attack; swaps guitar vocabulary for the synth substitute |
| 2 | `(Explosive lift, heavy guitars, powerful vocals)` | `(Explosive lift, full synth wall, powerful vocals)` | Applied to **both** instances. Lift and weight preserved |
| 3 | `(Abrupt industrial finish, guitar scratch)` | `(Abrupt industrial cut, metallic noise-scrape, dead silence)` | The scratch gesture survives as texture, not instrument |
| — | `tighter,` (2nd pre-chorus) | `tighter` | Punctuation only; normalized to match the first pre-chorus |
| — | `don’t` (U+2019) | `don't` (U+0027) | Apostrophe normalization — see below |
| — | kept verbatim | `(Tension building, industrial rise)`, `(Heavy bass groove, gritty delivery)`, `(Maximum energy)`, `(Dead silence)` | Genre-neutral, do real work. Nothing dropped |

### Apostrophe audit

The vault file is **mixed**, not uniformly curly:

| Line | Text | Codepoint |
|---|---|---|
| 18 | `You don’t belong in my head` | U+2019 (typographic) |
| 21 | `I've had enough of your kind` | U+0027 |
| 35, 65, 74 | `You won't get in` | U+0027 |

**Counts: 1 × U+2019, 4 × U+0027.** Version (B) normalizes all five to ASCII so Suno gets one tokenization of the contraction class. The typographic apostrophe stays in the vault as written — the file was not touched.

---

## 4. Negative prompt — paste into Exclude

### Core

```
tenor vocal, country, melodramatic, classic rock, guitar sustain intro, electric guitar, acoustic guitar, rhythm guitar, lead guitar, power chords, palm-muted chugs, chugging guitar, nu-metal guitar, guitar solo, guitar amp, guitar scratch, synthwave, retro 80s, clean synth-pop, electro-pop, female vocal, polished, mastered, final, breakdown, bridge, half-time drop, gang vocals, chant, fade out
```

### Extended

```
dance-pop, EDM, big room, four-on-the-floor, chiptune, vaporwave, 8-bit, orchestral, symphonic, choir, pop production, clean production, bright, soft, ballad, sentimental, uplifting, handclaps, funk guitar, wah pedal, fretless bass, disco, pop-punk, metalcore, screamo, rap, spoken interlude, strings
```

### Five song-specific additions

| Addition | What it prevents |
|---|---|
| `breakdown, bridge, half-time drop` | **This song has no bridge.** Suno adds one by reflex on an 8-section form. The back-to-back chorus pair is the only structural escalation and must not be interrupted. |
| `gang vocals, chant` | The chorus is 6 lines of which 4 are the title. Without this, the triple pass turns into a crowd chant. |
| `four-on-the-floor, EDM, big room` | 147 BPM plus industrial tags is a standing invitation to EBM stomp. |
| `fade out` | The song ends on a cut, not a fade. |
| `guitar scratch, chugging guitar, nu-metal guitar` | Even in version (B) the lineage is nu-metal; the exclude field is the enforcement layer. |

---

## 5. Title metadata

- **Title:** `Under My Skin (Synth Conversion Reference)`
- **Fallback:** `Under My Skin Synth Reference`

---

## 6. Creative sliders

**Mode:** Custom, no audio upload. Held at validated series values — no deviation.

| Control | Value | Mode | Reasoning |
|---|---|---|---|
| **Weirdness** | **30%** | Custom | Most structural detail to protect in the series — documented key, no bridge, unbroken double chorus. Weirdness improvises structure, so low keeps any deviation a diagnosable prompt fault. |
| **Style Influence** | **75%** | Custom | Guitar reflex is strongest here (source lineage is literally nu-metal); the fix is removing guitar words from the lyrics field plus the exclude list, not pushing this slider — raising it amplifies whatever tags exist, it does not subtract guitar. |
| **Audio Influence** | **n/a — slider absent** | Custom (no upload) | If run in Cover mode with the original guitar track as reference: **65%**. |
| **Variety** | **Off (0)** | Custom | Most destructive setting for this song — would strip the guitar exclusions and the no-breakdown instruction, then collapse the consecutive-chorus pair into a generic form. v6 defaults to Normal; set manually. |

**Max Mode: ON.** **Personalize: off.**

### Retry ladder

- **Guitar audible** (primary failure mode): check the lyrics field first — if version (A) is loaded, switch to (B) before touching a slider. That is the actual cause.
- **Still guitar-adjacent after (B):** Style Influence 75% → 80%. One permitted upward move for this song.
- **Rigid or wooden:** Style Influence 75% → 65%. Never above 80%.
- **Structure broken** (bridge appears, chorus pair separated): Weirdness 30% → 20%.

---

## 7. Suno role verification

**Suno-assist (PRD 5.4). master_source = studio.** Reference render only. Baritone male descriptors carried; `female vocal` and `tenor vocal` excluded; `polished, mastered, final` excluded to prevent treating output as a master. Any Suno audio beyond listening reference must come from an active paid tier (Premier plan on record; no retroactive rights on free-tier output).

---

## 8. Compatibility checklist

| # | Check | (A) Verbatim | (B) Approved |
|---|---|---|---|
| 1 | Style prompt present | PASS | PASS |
| 2 | Lyrics field present, verbatim from vault | PASS | PASS — sung lyrics byte-identical |
| 3 | Section labels per spec | PASS | PASS |
| 4 | Labels Title Case | PASS | PASS |
| 5 | Line breaks per spec | PASS | PASS |
| 6 | Title field present | PASS | PASS |
| 7 | Negative prompt present | PASS | PASS |
| 8 | Suno role verdict | PASS — Suno-assist | PASS — Suno-assist |
| 9 | Out-of-vocabulary tags flagged | PASS with flag | PASS with flag |
| 10 | Per-artist structure | PASS — Velvut | PASS — Velvut |

**Overall: PASS for both.** Check 3 note: all labels used (`[Verse 1]`, `[Verse 2]`, `[Pre-Chorus]`, `[Chorus]`, `[Outro]`) are canonical. The repeated `[Chorus]` is a duplicate of a canonical label — valid, and what the Principal wrote.

**Unverified values disclosed:** time signature; Style field character cap; chord progression.

---

## 9. Audition notes

**Palette fit vs harmonic difficulty.** Most explicitly industrial lyric in the series — wire, static, machine, noise, gate, sealed, shut down, cut clean through. On *atmosphere* this is the easiest conversion in six. It is simultaneously the **hardest harmonic conversion**, because 'surprising chord changes' is documented and a 147 BPM sequencer is the fastest way to lose it. Do not let the first win hide the second.

### 9.1 The double chorus

Structure: V1 → PC → C → V2 → PC → C → C → Outro, **no bridge**. The two consecutive `[Chorus]` labels are the same label twice, not `[Final Chorus]`. The only written differentiator is `(Maximum energy)`.

**Escalation must be timbral and dynamic** — the words are identical and cannot carry it:

1. **Open the saw stack.** Pass 2 adds a second detuned saw layer an octave up. Wider, not louder.
2. **Drop the pads for one beat before the downbeat.** The hole makes re-entry read as escalation; adding layers alone reads as more of the same.
3. **Push the mono lead into a counter-line.** Pass 1: lead supports. Pass 2: lead answers between phrases.

**Must not happen:** new lyrics, changed hook, key change, or a breakdown between the two passes. The `breakdown, bridge, half-time drop` exclusions exist for exactly this.

### 9.2 The abrupt ending

`[Outro]` contains no sung lyrics — only the parenthetical then `(Dead silence)`. The song ends in silence.

Reach for it with `plate reverb on final hit` + `hard cut ending` in the style prompt, the rewritten parenthetical, and `fade out` in excludes. The reverb tail on the last hit is what makes a cut read as *abrupt* rather than *truncated* — abrupt needs a decay that is then severed.

**Expect one of three:** (a) correct cut with short tail; (b) a 1-3 second fade appended despite the exclude; (c) the Outro filled with unrequested vocal or a swelling pad. All recoverable. **The true abrupt stop is a GarageBand edit.** Coax, cut by hand. Do not spend retries chasing sample-accurate silence from the renderer.

### 9.3 The pre-chorus stutter-hook

```
Here comes that buzz in the wire
In the wire
Hands on the gate getting tighter
Getting tighter
Too close now I can taste it
One more move and I break it
```

Lines 1 and 3 land the content; lines 2 and 4 are echoes of their own tails, not restatements. Lines 5 and 6 run clean with no repetition — the stutter stops, and that release is the lift.

**Failure mode:** Suno treats the echo as an independent line of equal weight, so all six come out flat and the section becomes a list. If lines 2 and 4 sound as loud as lines 1 and 3, the mechanic broke.

**Direction:** the repeat is quieter, tighter, rhythmically gated — a stutter throw, not a second delivery. In a synth palette, let the echo ride a short gated delay so the tail becomes a rhythmic device. The two clean closing lines are the payoff and must be the loudest vocal moment in the section.

### 9.4 The six-line chorus

`Under my skin / You won't get in / Under my skin / Burn it down let the rage begin / Under my skin / Under my skin`

Four of six lines are the title. The words do not vary; the delivery must.

| Pass | Vocal treatment |
|---|---|
| 1 (after V1) | Close-mic, restrained power, bass-heavy. Sits *under* the wall. |
| 2 (after V2) | Open up. Single upper harmony on `Burn it down let the rage begin` only. |
| 3 (consecutive) | Double-tracked, no harmony, raw. Maximum energy by delivery, not addition. |

**The line that carries the hook is not the title — it is `Burn it down let the rage begin`.** The only line with forward motion; the refusal turning into a threat. If it gets less weight than the title repeats, the chorus has become the chant.

### 9.5 Listen in order

1. **Guitar bleed — check the lyrics field first.** Version (A) in the field means the prompt still says 'heavy guitars' twice. Listen 200-500 Hz; check the outro for a pick scrape.
2. **Harmonic movement.** Count distinct chords. Sitting on C# for a full chorus means the sequencer was given harmonic responsibility.
3. **Weight transfer.** Chug must live in sub-bass and the gated pulse.
4. **Tempo drive.** 147 BPM; padded verse pulse will drag.
5. **Double chorus.** Did a bridge or breakdown appear? Did pass 3 escalate?
6. **Outro.** Cut or fade?
7. **Vocal.** Deep baritone, upfront.
8. **Pre-chorus.** Echoes quieter than the lines they echo?
9. **Intro.** Gated pulse or single metallic hit — never a swelling pad.

### 9.6 Range note — derived, not documented

The vault does not record a vocal range ceiling for this song. Carry-forward from the Sad Song reference: D minor sits at the top of the usable key map (peak at D4). **C# minor is a semitone below D minor**, so the peak sits at approximately C#4 — marginally more comfortable. **This is a derivation from another song's documented note, not a fact from this file.** Confirm against the rebuild.

---

## 10. Lineage

- Song facts and lyrics: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/under-my-skin.md` (read direct 2026-10-30)
- Series reference: `docs/2026-10-30-sad-song-velvut-synth-conversion-suno-prompt.md`
- Prompt spec: `.a0proj/skills/suno-prompt-compatibility-spec/SKILL.md`
- Role matrix: `.a0proj/skills/suno-integration/SKILL.md` (PRD 5.4)
- DAW guide: `docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md`
- Slider semantics verified 2026-10-30 against help.suno.com Creative Sliders article
