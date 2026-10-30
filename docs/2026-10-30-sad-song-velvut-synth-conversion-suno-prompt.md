---
last_updated: 2026-10-30T17:43:00
status: delivered
artist: Velvut
song: Sad Song
series_position: 1
route: suno-synth-re-render
tempo: 151
key: D minor
time_signature: UNVERIFIED — not documented
vocal_range: F2-D4
suno_role: assist
direction_status: approved
master_source: studio
---

# SAD SONG (Velvut) — Synth Conversion Suno Prompt Set

**Artist:** Velvut · **Song:** Sad Song · **Date:** 2026-10-30
**Author:** WGNR Sounds Captain (dispatch: suno-prompter) · **Principal:** Wagner dos Santos
**Route:** Suno synth re-render (not stems swap) · **Purpose:** direction reference for the Principal's GarageBand rebuild

**Outcome (Principal, 2026-10-30):** first render auditioned and rated as working — _came out great_.

---

## 1. Verified song facts

Sourced from `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/sad-song.md` (read direct, 2026-10-30) and `artist-facts.md`.

| Field | Value |
|---|---|
| Tempo | 151 BPM |
| Key | D minor |
| Meter | 4/4 |
| Vocal | Deep baritone male, upfront |
| Original style notes (verbatim) | punk-rock with nu-metal and industrial rock influences, 151bpm, d minor, chugging rhythm, deep baritone male vocals, memorable chorus hook, melodic with surprising chord changes |
| Original exclusions (verbatim) | tenor vocal, country, melodramatic, classic rock, guitar sustain intro |
| Suno role | Suno-assist (PRD 5.4) — master_source = studio |

Range note carried forward: D minor sits at the top of Velvut's usable key map (peak-at-D4-ceiling), so the vocal sits high in the range rather than comfortably under it.

---

## 2. Style prompt — paste into Style of Music

```
dark industrial synth-rock, darkwave, electro-industrial, punk aggression, heavy, 151 BPM, D minor, distorted synth bass, gated sequenced saw-bass pulses, detuned saw stack stabs, hard analog synth pads, aggressive mono-synth lead with portamento, metallic industrial percussion hits, programmed kick with weight, quiet verses, wall-of-sound choruses, mantra repetition, deep baritone male vocal upfront, gritty, memorable chorus hook, surprising chord changes
```

### Guitar-to-synth substitution map

| Original guitar or kit role | Synth replacement |
|---|---|
| Chugging rhythm guitar | distorted synth bass + gated sequenced saw-bass pulses |
| Rhythm power chords | detuned saw stack stabs + hard analog synth pads |
| Lead or wailing guitar | aggressive mono-synth lead with portamento |
| Tom-tom and kit weight | metallic industrial percussion hits + programmed kick with weight |
| Guitar sustain intro | intentionally absent — open on synth-bass pulse |

---

## 3. Exclude styles — paste into Exclude

**Core:**

```
tenor vocal, country, melodramatic, classic rock, guitar sustain intro, electric guitar, acoustic guitar, rhythm guitar, lead guitar, power chords, palm-muted chugs, guitar solo, guitar amp, synthwave, retro 80s, clean synth-pop, electro-pop, female vocal, polished, mastered, final
```

**Extended (if the field allows):**

```
dance-pop, chiptune, vaporwave, 8-bit, orchestral, symphonic, choir, pop production, clean production, bright, soft, ballad, sentimental, uplifting, handclaps, funk guitar, wah pedal, fretless bass, disco
```

---

## 4. Title metadata

- **Title:** `Sad Song (Synth Conversion Reference)`
- **Fallback if parentheses rejected:** `Sad Song Synth Reference`

---

## 5. Creative sliders — as used on the approved render

**Mode:** Custom, no audio upload (re-render route)

| Control | Value | Reasoning |
|---|---|---|
| **Weirdness** | **30%** | Guitar bleed is the failure mode; low weirdness keeps any stray guitar a prompt problem, diagnosable in one retry rather than variance noise. |
| **Style Influence** | **75%** | Combats the punk + heavy + distorted guitar reflex; the guitar ban only holds if the tag set is enforced hard. |
| **Audio Influence** | **0% — slider does not appear** | Only exists when reference audio is uploaded; the re-render has none. Cover-mode value if used later: **65%**. |
| **Variety** | **Off (0)** | Variety rewrites the style prompt server-side and would strip the guitar exclusions and the substitution map. v6 default is Normal, so this must be set manually. |

**Max Mode: ON** (toggle, not a slider) — 2x credits; holds vocal and style consistency across a track over two minutes and is Suno's own recommendation for style transfer.
**Personalize: off** (inert at Variety Off).

### One-variable retry protocol

- Too conventional or guitar-adjacent: Weirdness 30% -> 45%. Change nothing else.
- Rigid or wooden: Style Influence 75% -> 65%. Do not push higher; contradiction worsens.

---

## 6. Lyrics field — verbatim from vault, labels as written

```
[Verse 1]
It's a sham
It's a sham
It's a sham
It's a sham
Nobody gives a damn

All is fake
All is fake
All is fake
All is fake
This whole town is a snake

Get away
Get away
Get away
Get away
I've got nothing left to say

Break it down
Break it down
Break it down
Break it down
Burn it all down to the ground

[Pre-Chorus]
Turn around
Don't make a sound
Time to go underground

[Chorus]
Don't look at me with those venomous eyes
Trying to distract while another one dies
This crooked game, I won't play along
While you write the words to this sad song

Don't look at me with those venomous eyes
Trying to distract while another one dies
This crooked game, I won't play along
While you write the words to this sad song
Sad song
Sad song

[Verse 2]
It's a lie
It's a lie
It's a lie
It's a lie
Watch this town rot and die

No escape
No escape
No escape
No escape
From this twisted, ugly shape

Lost my way
Lost my way
Lost my way
Lost my way
Live to fight another day

Tear it up
Tear it up
Tear it up
Tear it up
Had enough of this bitter cup

[Pre-Chorus]
Turn around
Don't make a sound
Time to go underground

[Chorus]
Don't look at me with those venomous eyes
Trying to distract while another one dies
This crooked game, I won't play along
While you write the words to this sad song

Don't look at me with those venomous eyes
Trying to distract while another one dies
This crooked game, I won't play along
While you write the words to this sad song
Sad song
Sad song

[Bridge]
Pull the plug, let the whole thing drop
Don't look back, don't even stop
If it cracks, let it crack real wide
I'm stepping through the other side

[Final Chorus]
Don't look at me with those venomous eyes
Trying to distract while another one dies
This crooked game, I won't play along
While you write the words to this sad song

Don't look at me with those venomous eyes
Trying to distract while another one dies
This crooked game, I won't play along
While you write the words to this sad song

Don't look at me with those venomous eyes
Trying to distract while another one dies
This crooked game, I won't play along
While you write the words to this sad song
Sad song
Sad song
Sad song
```

No lyric text altered. `[Final Chorus]` is not in the compatibility spec's canonical label table; it is preserved because it is the Principal's written label. Fallback if Suno mishandles it is `[Chorus]`.

---

## 7. Compatibility checklist result

| # | Check | Result |
|---|---|---|
| 1 | Style prompt present (genre, style, instrumentation, vocal) | PASS |
| 2 | Lyrics field present, verbatim from vault | PASS |
| 3 | Section labels per spec | PASS with flag (`[Final Chorus]`) |
| 4 | Labels Title Case | PASS |
| 5 | Line breaks per spec | PASS |
| 6 | Title field present | PASS |
| 7 | Negative prompt present | PASS |
| 8 | Suno role verdict, PRD 5.4-consistent | PASS — Suno-assist, master_source studio |
| 9 | Out-of-vocabulary tags flagged | PASS — flagged, in-vocab anchors available as fallback |
| 10 | Per-artist prompt structure | PASS — Velvut structure |

**Overall: PASS.** Palette descriptors outside the spec vocabulary (`industrial synth-rock`, `darkwave`, `gated sequenced saw-bass pulses`, and similar) are flagged as unverified against the current interface, not invalid — the spec's vocabulary list is explicitly non-exhaustive.

---

## 8. Rights and pipeline note

Velvut is Suno-assist; the production master is the human recording. This render is a concept and arrangement reference, not a release master. Any Suno audio used beyond listening reference must come from a generation made on an active paid tier — Premier plan on record, no retroactive rights on free-tier output.

---

## 9. Audition notes (what was checked)

1. **Guitar bleed** — primary failure mode; listen 200-500 Hz for strummed guitar body.
2. **Weight transfer** — the chug must live in sub-bass and sequenced saw pulse; thinner low end than the guitar version is a failure, not a stylistic trade.
3. **Tempo drive** — darkwave defaults slower; at 151 BPM the verse pulse must be sequenced, not padded.
4. **Chord integrity** — the hook is the surprising chord changes; flattening into a four-chord loop means the palette smeared the harmony.
5. **Chorus lift** — must read heavier, not prettier.
6. **Vocal** — deep baritone, upfront; reject tenor or polished pop-baritone before judging anything else.
7. **Intro** — synth-bass pulse or a single metallic hit, never a swelling pad.

**Bridge idea for the GarageBand rebuild (not a Suno expectation):** power-down on 'Pull the plug' — filter collapse or tape-stop — then a violent re-open at the final chorus. Suno can be coaxed toward this but not commanded; build by hand.

---

## 10. Lineage

- Song facts and lyrics: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/sad-song.md`
- Lyric review: `docs/2026-10-06-sad-song-velvut-review.md`
- Prompt spec: `.a0proj/skills/suno-prompt-compatibility-spec/SKILL.md`
- Role matrix: `.a0proj/skills/suno-integration/SKILL.md` (PRD 5.4)
- Slider semantics verified 2026-10-30 against help.suno.com Creative Sliders article and the bitwize creative-sliders reference
