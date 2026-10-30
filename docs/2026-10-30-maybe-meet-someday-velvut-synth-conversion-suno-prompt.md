---
last_updated: 2026-10-30T17:44:00
status: delivered
artist: Velvut
song: Maybe We'll Meet Again Someday
series_position: 8
route: suno-synth-re-render
tempo: UNVERIFIED — not documented
key: UNVERIFIED — not documented
time_signature: UNVERIFIED — not documented
vocal_range: F2-D4
suno_role: assist
direction_status: out-of-scope
master_source: studio
---

# MAYBE WE'LL MEET AGAIN SOMEDAY (Velvut) — Synth Conversion Suno Prompt Set

**Artist:** Velvut · **Song:** Maybe We'll Meet Again Someday · **Date:** 2026-10-30 · **Series:** song 8
**Route:** Suno synth re-render (reference only) · **Purpose:** arrangement direction for the GarageBand rebuild

---

## 0. Gaps and flags — read first

**This is the thinnest song file in the series.** Nothing is documented except the lyrics. All of the following are absent, and nothing has been invented to fill them:

| Missing | Consequence |
|---|---|
| No BPM | Suno chooses its own tempo. Darkwave defaults run slow — here that is closer to correct than wrong, but it is still a guess. |
| No key | No key token in the style prompt. The `predominantly minor key` descriptor from neighbouring files is not imported; it may well be wrong for a song about someone else's happiness. |
| No meter | No time signature stated. |
| No style notes (`### Style Notes` = **TBD**) | **The guitar-substitution map cannot be derived from this song.** It is inherited series-wide, not song-specific. |
| No exclude list | Series-standard exclusions applied, plus song-specific additions in §3. |

**Two lyric defects — both resolved by Principal ruling 2026-10-30:**

1. **Line 15 duplicated `I` — ruled a typo. Corrected.** `If I I could see her again someday` → `If I could see her again someday`. The vault file was patched in the same operation, so this doc and the vault now agree.
2. **`[Chorus Climax]` — ruled normalise. Corrected** to `[Final Chorus]`, a canonical label. The build instruction the old label carried is preserved in §5, where arrangement direction belongs.

One item remains flagged and needs no decision:

3. **`[Break]` is empty** — the label has no lyric lines under it. Suno will read a bare label as an instrumental section, which is the most plausible intent and almost certainly correct. Flagged, not changed.

---

## 1. Verified song facts

Source: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/maybe-meet-someday.md` (read direct 2026-10-30, `last_updated: 2026-07-31T20:24:00`, `status: draft`).

| Field | Value | Status |
|---|---|---|
| Title | **Maybe We'll Meet Again Someday** | DOCUMENTED — no question mark, unlike Take Me Back? |
| Tempo | **UNVERIFIED — not documented** | Absence verified by direct read |
| Key | **UNVERIFIED — not documented** | Absence verified |
| Time signature | **UNVERIFIED — not documented** | Absence verified |
| Album | `TBD` | DOCUMENTED as undecided |
| Style notes | **`TBD`** — the field exists and is empty | Absence verified |
| Exclusions | **None recorded** | Absence verified |
| Recording state | Status `draft`; no recording referenced in the file | DOCUMENTED |
| Vocal (song-level) | Not documented | — |
| Vocal (artist-level) | **Powerful baritone, upfront, F2–D4** | DOCUMENTED in `velvut/artist-facts.md` |
| Suno role | Suno-assist (PRD §5.4) — `master_source = studio` | DOCUMENTED |

The vocal descriptor used in the style prompt is the **artist-level fact**, not a song-level one, and it is labelled as such. This song's own vocal direction is undocumented.

---

## 2. Style prompt — paste into Style of Music

```
dark industrial synth-rock, darkwave, electro-industrial, elegiac, aching, unresolved longing, regret without bitterness, muted momentum, distorted synth bass, gated sequenced saw-bass pulses, soft-attack detuned saw stack stabs, warm analog synth pads, filtered mono-synth lead with portamento, sparse melodic lead lines, metallic industrial percussion hits, programmed kick with weight, restrained verses, cumulative choruses, heavy not bright, minor-key emotional pull, sub-bass weight, analog tape saturation, room reverb, plate reverb on the lead, deep baritone male vocal upfront, melodic legato delivery, restrained power, memorable chorus hook, three-statement chorus
```

### What this prompt is derived from, and what it is not

**Derived from:** the series palette (Principal-approved signature sound, 2026-10-30) and the artist-level house identity in `artist-facts.md` — nu-metal / alt-rock origins, minor key, deep bass, full kit, quiet verses / wall-of-sound choruses.

**Not derived from:** this song. There are no style notes to convert. The substitution map below is inherited by default and **the Principal may overrule every row of it** — nothing in the vault says this song was guitar-led at all.

### Substitution map (inherited, not song-specific)

| Original role | Synth replacement |
|---|---|
| Rhythm guitar / power chords | detuned saw stack stabs + warm analog synth pads |
| Chugging / palm-muted rhythm | gated sequenced saw-bass pulses |
| Lead guitar melody | filtered mono-synth lead with portamento |
| Kit weight and toms | metallic industrial percussion + programmed kick with weight |
| Guitar sustain / intro wash | absent — open on a filtered pad or a bare pulse |

**Soft-attack stabs are the one deliberate departure from the series.** Every other song uses hard stabs. This lyric is a man remembering a woman gently — the attack should be rounded, not struck.

### The register judgement call

This is the first song in the series that is **sad rather than heavy**. The lyric contains no rage, no addiction, no collapse — it contains `I hope your life is beautiful`, which is generosity, not bitterness.

The trap is not triumph (as on Is This How It Ends?). It is **sentimentality** — a maudlin, weepy, wedding-song reading. The prompt holds weight so the song stays dignified: `heavy not bright`, `restrained power`, `regret without bitterness`. Do not read `elegiac` as permission to go soft.

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
maudlin, schmaltzy, tearjerker, weepy, piano ballad, soft rock, acoustic ballad, country ballad, wedding song, sentimental piano, strings swell, orchestral swell, hopeful, uplifting, major-key resolve, key change up, triumphant, anthemic, fade out, fade ending, resolving outro, final chord resolve, guitar feedback, distorted guitar harmonics
```

**Why each block exists:**

1. `maudlin, schmaltzy, tearjerker, weepy, piano ballad, soft rock, acoustic ballad, country ballad, wedding song` — the register failure mode for this song. A sad lyric plus a slow darkwave bed plus any one of these tags produces a greeting-card reading. Highest-stakes block in the set.
2. `sentimental piano, strings swell, orchestral swell` — the specific instruments Suno reaches for when it hears `elegiac`. A string swell turns regret into a movie scene.
3. `hopeful, uplifting, major-key resolve, key change up, triumphant, anthemic` — the title contains the word *maybe*. Suno will try to answer the maybe. The song does not answer it.
4. `fade out, fade ending, resolving outro, final chord resolve` — no outro is written. A fade says the story continues; a hard stop says the memory just ends. Same rule as the rest of the series.
5. `guitar feedback, distorted guitar harmonics` — the two guitar artifacts most likely to survive a synth prompt because they do not contain the word *guitar* in a form the prompt negates cleanly.

---

## 4. Lyrics field

**Verbatim from the vault as patched 2026-10-30. The two Principal rulings — typo fix on line 15, label normalisation to `[Final Chorus]` — are the only changes ever made to this lyric, and both are already in the vault. No sung word was altered by this document.**

Structure as written: `[Verse]` (two stanzas under one label — no `[Verse 2]` exists in this file) → `[Chorus]` → `[Bridge]` → `[Chorus]` → `[Break]` (empty) → `[Chorus]` → `[Final Chorus]`.

```
[Verse]
She's in my dreams everyday
Though we dated several decades away
I wrote down what I'd like to say
If I could see her again someday

She was beautiful and kind
But I was out of my mind
Moved far away without a plan
Broke her heart – yeah I'm the man

[Chorus]
I still think about you today
And all the things that I would've changed
I hope your life is beautiful
Maybe we'll meet again someday
Maybe we'll meet again someday

[Bridge]
We walked through the park, you had nothing to say
But your beautiful smile would just give it away
I've made two lifetimes worth of mistakes
But it's leaving you that haunts me everyday

[Chorus]
I still think about you today
And all the things that I would've changed
I hope your life is beautiful
Maybe we'll meet again someday
Maybe we'll meet again someday

[Break]

[Chorus]
I still think about you today
And all the things that I would've changed
I hope your life is beautiful
Maybe we'll meet again someday
Maybe we'll meet again someday

[Final Chorus]
If there could be another way
I'd turn the clocks back to that day
I want to shout out your name and say
Maybe we'll meet again someday
```

### Flag detail

**Duplicated `I` (line 15) — fixed.** The line now reads as shown above. Arrangement consequence: it loses one syllable. Do not pad that gap with a synth stab or an extra kick — let the phrase breathe shorter. The vault carries the same correction.

**`[Chorus Climax]` → `[Final Chorus]` — normalised.** Canonical per the spec. The build the old label spelled out is not lost: it lives in §5, where arrangement direction belongs. Any lift on the final pass comes from the style prompt and those notes, never from a non-standard label.

**`[Break]` empty:** left empty. If the render chokes or sings the word, replace the label with `[Instrumental Break]`.

---

## 5. Arrangement notes

### The chorus is a three-statement, not a three-repeat

Unlike Is This How It Ends?, the three `[Chorus]` blocks here are **byte-identical** and are followed by a fourth pass with different words. That makes the song four choruses long, not three — and the fourth is the only one that changes.

| Pass | Position | Target read | Arrangement |
|---|---|---|---|
| 1 | After verse | Recollection — flat, factual | Pads and pulse only. Percussion enters on `I hope your life is beautiful`. |
| 2 | After bridge | The confession lands | Full stack. Bridge exit is the loudest point before the ending. |
| 3 | After `[Break]` | Return — quieter than pass 2 | **Pull back.** Pass 3 after a break reads as the narrator settling, not building. |
| 4 (`[Final Chorus]`) | End | The only real lift | Full stack plus lead doubling an octave down. Different words, higher line: `If there could be another way` is the emotional peak of the song and the only place the melody should rise. |

### The empty `[Break]` is load-bearing

It sits between chorus 2 and chorus 3, and it is the song's only instrumental space. On the demo this is where a guitar would have had a moment. On the synth rebuild it is the one place the mono-synth lead carries a melodic idea instead of doubling a vocal. Do not fill it with a drum fill.

### No outro exists

`[Final Chorus]` is the last labelled section and the last line is `Maybe we'll meet again someday`. There is no `[Outro]`, no final tag, no repeat of the title as a closing statement. **A fade is a fail** — same rule as the rest of the series.

But note the difference from Is This How It Ends?: that song ends on an unanswered question, so a hard cut is the correct answer. This song ends on `I want to shout out your name and say` — a line that **leads into** the title. A hard cut on the title phrase is right; a hard cut *before* it would truncate the sentence.

---

## 6. Creative sliders

**Mode:** Custom, no audio upload. Held at validated series values — no deviation.

| Control | Value | Mode | Reasoning |
|---|---|---|---|
| **Weirdness** | **30%** | Custom | The failure mode is a register fault (sentimentality), exactly like Is This How It Ends?. Low weirdness keeps that a diagnosable prompt problem rather than variance. Also: with no documented BPM, this is the song where an unexpected tempo choice is most likely, and low weirdness makes it reproducible rather than random. |
| **Style Influence** | **75%** | Custom | The song-specific exclusion block is the largest in the series — ten sentimentality bans plus the uplift and fade bans. It only holds when enforced hard. |
| **Audio Influence** | **n/a — slider absent** | Custom (no upload) | Cover-mode value if the demo is used as reference later: **65%**. |
| **Variety** | **Off (0)** | Custom | Would rewrite the style prompt server-side and strip the sentimentality block. This song cannot absorb that — without those bans, `elegiac` becomes a wedding song. |

**Max Mode: ON.** **Personalize: off.**

**Retry ladder:**

- Maudlin / greeting-card read → check for a piano or string tag slipping through; re-roll before touching sliders.
- Tempo far off the demo (once the demo tempo is known) → this is not a slider fault. Suno chose. Re-roll with a BPM written into the style prompt once a value exists.
- Guitar bleed (200–500 Hz body) → Style Influence 85%.
- Structure collapsed, `[Break]` swallowed → Weirdness 20%.

---

## 7. Tempo, key, meter — the gap, stated plainly

**Nothing is documented for this song.** No frontmatter field, no prose value, no detector reading, no MIDI map. There is no dispute here to adjudicate — there is an absence.

**What this means for the render:**

1. **Tempo:** Suno chooses. Darkwave and electro-industrial defaults sit in a slow-to-mid range, which is plausibly right for an elegiac song — but *plausible is not verified*. Do not A/B this render against the demo for tempo. It is a valid palette, arrangement, and vocal reference and an **invalid tempo reference**.
2. **Key:** no key token in the style prompt. Any harmonic claim about this render is unverifiable.
3. **Meter:** not documented. Nothing stated.

**Before the GarageBand rebuild:** establish the demo's actual BPM, key, and meter by measurement, then write them back into the vault file's frontmatter. Until that happens this song is the weakest anchor in the series — the rebuild would be matching a reference whose timing is unknown.

---

## 8. Suno role verification + compatibility checklist

**Suno-assist (PRD §5.4). `master_source = studio`.** No finished recording is referenced by this song's file (`status: draft`). This render is an arrangement reference for a song not yet recorded. It is not a release master and not a demo replacement.

Baritone male descriptors carried (artist-level fact). `female vocal` and `tenor vocal` excluded. `polished, mastered, final` excluded.

| # | Check | Result |
|---|---|---|
| 1 | Style prompt present | PASS |
| 2 | Lyrics verbatim from vault | PASS — byte-identical to the vault as patched 2026-10-30 |
| 3 | Section labels per spec | PASS — `[Final Chorus]` canonical after Principal ruling 2026-10-30 |
| 4 | Labels Title Case | PASS |
| 5 | Line breaks per spec | PASS |
| 6 | Title field present | PASS — no question mark, matching the vault |
| 7 | Negative prompt present | PASS |
| 8 | Suno role verdict | PASS — Suno-assist |
| 9 | Out-of-vocabulary tags flagged | **PASS WITH FLAGS** — empty `[Break]` label; *elegiac* and *unresolved longing* as non-standard style vocabulary |
| 10 | Per-artist structure | PASS — Velvut |
| 11 | Key and time signature as explicit fields | **FAIL — both UNVERIFIED, not documented.** Written as `UNVERIFIED — not documented` in frontmatter, never inferred. |
| 12 | All four sliders specified | PASS |

**Overall: PASS WITH FLAGS.** Lyrics and labels are now fully spec-clean after the two Principal rulings. Check 11 cannot pass on this file — the values do not exist. That is a vault gap, not a prompt defect.

---

## 9. Audition notes

1. **Sentimentality test — the primary judgement call.** If it sounds like a wedding song, a movie montage, or a sympathy card, the render has failed however pretty it is. Listen for: a piano, a string swell, a major resolve, an uplifting lift on `I hope your life is beautiful`. That line is the test point — it should land as generosity from a man who lost, not as a blessing.
2. **Tempo.** Unknown by design. Judge whether it feels elegiac and forward-moving; do not judge it against a number, because there is no number.
3. **Guitar bleed.** 200–500 Hz for strummed body; also listen for feedback tails at section boundaries, which the extended exclusions target.
4. **The `[Break]`.** Should be instrumental space with a melodic lead idea. If it is silence, or a drum fill, the section was misread.
5. **Four-chorus fatigue.** Pass 1, 2, 3 are identical words. Expect Suno to flatten them. Judge the palette and the register; the differentiation is the rebuild's job.
6. **`[Final Chorus]`.** The only pass with different words and the only place the melody should rise. If it lands at the same level as the three before it, the label was ignored.
7. **Ending.** Must stop on or after `Maybe we'll meet again someday` in the climax. A fade is a fail; a cut before the title phrase truncates the sentence.

---

## 10. Lineage

- Song facts and lyrics: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/maybe-meet-someday.md` (read direct 2026-10-30)
- Vocal identity and house sonic identity: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/artist-facts.md`
- Series reference: `docs/2026-10-30-sad-song-velvut-synth-conversion-suno-prompt.md`
- Slider semantics and structure: `docs/2026-10-30-is-this-how-it-ends-velvut-synth-conversion-suno-prompt.md`
- Prompt spec: `.a0proj/skills/suno-prompt-compatibility-spec/SKILL.md`
- Role matrix: `.a0proj/skills/suno-integration/SKILL.md` (PRD §5.4)
- DAW guide: `docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md`
