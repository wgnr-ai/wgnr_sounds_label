---
last_updated: 2026-10-30T17:44:00
status: delivered
artist: Velvut
song: Is This How It Ends?
series_position: 7
route: suno-synth-re-render
tempo: UNRESOLVED — see section 7
key: Am
key_status: RESOLVED (Principal 2026-09-14)
time_signature: 4/4
time_signature_status: DOCUMENTED
vocal_range: F2-D4
suno_role: assist
direction_status: approved
master_source: studio
---

# IS THIS HOW IT ENDS? (Velvut) — Synth Conversion Suno Prompt Set

**Artist:** Velvut · **Song:** Is This How It Ends? · **Date:** 2026-10-30 · **Series:** song 7
**Route:** Suno synth re-render (reference only) · **Purpose:** arrangement direction for the GarageBand rebuild

---

## 1. Verified song facts

Source: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/is-this-how-it-ends.md` (read direct 2026-10-30).

| Field | Value | Status |
|---|---|---|
| Key | **A minor** (`key: Am`) | **RESOLVED** — Principal ruling 2026-09-14. Do not reopen. |
| Time signature | **4/4** | DOCUMENTED in frontmatter |
| Tempo | **UNRESOLVED — three-way documented dispute** | See §7 |
| Vocal | Powerful baritone, upfront. **Verified range F2–D4**, chorus peaks AT the D4 ceiling in the gritty upper register after the −5 semitone transposition | DOCUMENTED — the only song in the series with a recorded range |
| Album | **This is Velvut** | DOCUMENTED (named) |
| Style notes (verbatim) | nu-alt rock, alt-metal influences, minor key, powerful baritone vocal, upfront vocals, analog tape saturation, room reverb, wailing guitars, tight rhythm guitars, deep bass, full drum kit performance, explosive chorus lift | DOCUMENTED |
| Exclusions | None recorded — series-standard applied | Absence verified |
| Recording state | **No finished recordings exist.** A TEST music video was commissioned against the current demo | DOCUMENTED |
| Suno role | Suno-assist (PRD 5.4) — master_source = studio | DOCUMENTED |

**Key resolution history (do not reopen):** frontmatter originally read `Fm`; suno.bi detected F Major / relative D Minor; the Principal transposed the demo −5 semitones in GarageBand and confirmed **A minor** by ear on 2026-09-14. Both the suno.bi relative-D-minor reading and the −5 transposition agree on A minor. This is settled.

---

## 2. Style prompt — paste into Style of Music

```
dark industrial synth-rock, darkwave, electro-industrial, bleak, exhausted, slow crush, 107 BPM, A minor, 4/4, distorted synth bass, gated sequenced saw-bass pulses, detuned saw stack stabs, hard analog synth pads, aggressive mono-synth lead with portamento, metallic industrial percussion hits, programmed kick with weight, sparse hollow verses, wall-of-sound choruses, heavy not bright, downward harmonic pull, sub-bass weight, analog tape saturation, room reverb, explosive chorus lift without triumph, deep baritone male vocal upfront, gritty upper register, strained and weary, unheroic, memorable chorus hook
```

### What changed from the Sad Song prompt, and why

Palette held. Three descriptors swapped, because Sad Song's wording would produce the wrong emotional read:

| Sad Song descriptor | This song | Reason |
|---|---|---|
| `punk aggression` | `bleak, exhausted, slow crush` | 151 BPM and furious vs. 107 BPM and depleted. Punk aggression at this tempo reads as sloganeering over a dirge. |
| `quiet verses` | `sparse hollow verses` | Verse 2 is the sobriety verse — the space needs to be hollow, not merely quiet. Hollow survives the chorus contrast better. |
| `explosive chorus lift` (bare) | `explosive chorus lift without triumph` + `heavy not bright` | **The central judgement call.** Explosive alone is read by Suno as anthemic. The pairing locks lift to weight. |

### Substitution map (inherited)

| Original role | Synth replacement |
|---|---|
| Chugging rhythm guitar | distorted synth bass + gated sequenced saw-bass pulses |
| Rhythm power chords | detuned saw stack stabs + hard analog synth pads |
| Wailing / lead guitar | aggressive mono-synth lead with portamento |
| Tom-tom and kit weight | metallic industrial percussion + programmed kick with weight |
| Guitar sustain intro | absent — open on synth-bass pulse |

More guitar to remove here proportionally than in Sad Song: `wailing guitars` and `tight rhythm guitars` are two of five instrumental roles in the original notes.

### Vocal ceiling discipline (F2–D4 verified)

A baritone chorus at D4 is the top of the usable range, so the synth bed has no headroom above it:

- **Sub-bass:** root A1 (~55 Hz), sustained.
- **Distorted synth bass:** A1–A2.
- **Pads and saw stabs:** A2–A3 working bed. Stabs may reach C4 but only in gaps where the vocal is absent.
- **Mono-synth lead:** A4–E5, instrumental space only — intro, bridge tails, outro. Never under a sung line except the third-chorus doubling.
- **Third-chorus doubling rule:** if the lead doubles the vocal melody, it doubles **an octave down**, never up. Up-doubling collides with the D4 ceiling.

### Tempo in this prompt

`107 BPM` is written in as a **render anchor**, not a canonical value. See §7.

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
triumphant, anthemic, heroic, victorious, stadium rock, stadium chorus, major-key resolve, key change up, soaring, epic build, gospel, celebration, pop-punk, fade out, fade ending, resolving outro, final chord resolve, sustained outro pad, bright lead synth above the vocal
```

**Why each block exists:**

1. `triumphant, anthemic, heroic, victorious, stadium rock, stadium chorus` — the emotional-register bans. Subject is addiction and suicidal ideation. A heavy industrial chorus is one decision away from sounding like a victory anthem, which inverts the song's meaning. Highest-stakes exclusion in the set.
2. `major-key resolve, key change up, soaring, epic build` — the rock moves that manufacture triumph. The song is in A minor and ends on a question; a relative-major resolve would answer it.
3. `gospel, celebration, pop-punk` — the adjacent genres that turn a dark chorus communal. Suno reaches for these on "powerful vocal + heavy chorus".
4. `fade out, fade ending, resolving outro, final chord resolve, sustained outro pad` — no written ending exists. Left alone Suno will fade. A fade says the story continues; a hard cut says it does not.
5. `bright lead synth above the vocal` — the D4 ceiling guard.

---

## 4. Lyrics field — VERBATIM, conflict-free

**Nothing for the Principal to rule on.** Verified by direct read: no embedded production parentheticals, no typos, no profanity, all three chorus blocks byte-identical, three plain `[Chorus]` labels (no `[Final Chorus]` on this song).

One cosmetic note: the vault labels the first verse `[Verse]` and the second `[Verse 2]` — asymmetric but both canonical. Preserved as written.

```
[Verse]
To all the ghosts of my lovers
I apologize
To all the saints and my brothers
Hope I made you proud
To all the fakes and the others
I can see you now

[Chorus]
And I can hear the devil calling me
And this time I might just let him in
With a tear in my eye and a bottle in my hand
Is this how it ends?
Is this how it ends?

[Verse 2]
I've been sober for years now
But the voices say I can't be alone
And they've been saying I'm nothing
I need something that will turn off my mind

[Chorus]
And I can hear the devil calling me
And this time I might just let him in
With a tear in my eye and a bottle in my hand
Is this how it ends?
Is this how it ends?

[Bridge]
And now I'm falling
And now I'm calling for you
And now I'm crawling
And now I'm drowning for you

[Chorus]
And I can hear the devil calling me
And this time I might just let him in
With a tear in my eye and a bottle in my hand
Is this how it ends?
Is this how it ends?
```

Lyric text and section labels unaltered. Structure V → C → V2 → C → Bridge → C preserved exactly.

---

## 5. Three-identical-chorus fatigue management

Different problem from Bad's eight passes. Bad's fatigue was repetition *density*; this song's is *flatness*. Three narrative passes at one weight means the song has one chorus played three times.

| Pass | Position | Target read | Arrangement |
|---|---|---|---|
| 1 | After Verse 1 | Statement, almost resigned | Moderate. `With a tear in my eye` exposed — vocal dry, no doubling, pads only. Percussion enters on `Is this how it ends?` |
| 2 | After Verse 2 (sobriety verse) | Realisation — the darkest | **Thin, not thick.** Percussion half-time under the first two lines. Identical words land as a man noticing he is repeating himself. |
| 3 | After Bridge | Collapse — heaviest | Full stack, sub-bass maximised, lead doubling an octave down. The question is asked last and answered never. |

**Known limitation:** Suno cannot be told "pass 2 is quieter" without editing the lyrics field, and the field stays clean. Expect the render to flatten the three passes — **that flattening is what the GarageBand rebuild exists to fix.** Do not judge the concept on whether the render differentiates them; judge it on whether the palette and register are right.

---

## 6. Creative sliders

**Mode:** Custom, no audio upload. Held at validated series values — no deviation.

| Control | Value | Mode | Reasoning |
|---|---|---|---|
| **Weirdness** | **30%** | Custom | The emotional register is the failure mode here, not guitar. Low weirdness keeps a wrong-register render a diagnosable prompt fault rather than variance. |
| **Style Influence** | **75%** | Custom | The exclusion stack is doing heavy work — register bans, resolve bans, fade bans. It only holds enforced hard. |
| **Audio Influence** | **n/a — slider absent** | Custom (no upload) | Cover-mode value if used later with the demo as reference: **65%**. |
| **Variety** | **Off (0)** | Custom | Would rewrite the style prompt server-side and strip the register bans and the fade bans — the two most load-bearing blocks in this set. |

**Max Mode: ON.** **Personalize: off.**

**Retry ladder:** triumphant/anthemic read → not a slider, check for a major resolve or a bright lead, re-roll. Guitar bleed → Style Influence 85%. Structure collapsed (bridge misplaced) → Weirdness 20%.

---

## 7. Tempo — the three-way dispute, stated plainly

Three documented values, all from the vault file:

| Source | Value |
|---|---|
| Frontmatter (`tempo: 104`) | 104 BPM — 2026-09-11 session |
| suno.bi detector | 107.3 BPM measured (half/double feel: 54 / 215) |
| MIDI tempo map from 8 Principal stems | ≈105 BPM early, drifting to ≈109.4 late (373 beats / 93 bars / ~3:29) |

**These converge. They are not errors.** The source recording genuinely accelerates — roughly +4 BPM across three and a half minutes. The frontmatter and detector readings bracket the curve.

**What this means for the render:** Suno cannot follow a tempo curve. It quantizes to one tempo. Whatever number goes in the field is a compromise.

**Recommendation: build at fixed 107 BPM.** It is the curve's midpoint and matches the detector. The cost is the ~2.4 BPM late acceleration — the final chorus loses a little of the push it has on the demo.

**The alternative:** if you want the drift preserved, the MIDI tempo map governs and the test video already conforms to it. That path means GarageBand follows the map, and the Suno render is only a palette reference with the tempo treated as approximate.

**Still required before final render timing:** onset verification against the master audio. The 148 BPM figure floating in the video docs is **UNVERIFIED for this song** — it is not a half/double of the measured curve.

---

## 8. Suno role verification + compatibility checklist

**Suno-assist (PRD 5.4). master_source = studio.** No finished recordings exist; this render is an arrangement reference for a song not yet recorded. It is not a release master, not a demo replacement, and not the audio bed for the test video. Baritone male descriptors carried; `female vocal` and `tenor vocal` excluded; `polished, mastered, final` excluded.

| # | Check | Result |
|---|---|---|
| 1 | Style prompt present | PASS |
| 2 | Lyrics verbatim from vault | PASS — conflict-free |
| 3 | Section labels per spec | PASS — all canonical, no flag |
| 4 | Labels Title Case | PASS |
| 5 | Line breaks per spec | PASS |
| 6 | Title field present | PASS — question mark load-bearing |
| 7 | Negative prompt present | PASS |
| 8 | Suno role verdict | PASS — Suno-assist |
| 9 | Out-of-vocabulary tags flagged | PASS with flag |
| 10 | Per-artist structure | PASS — Velvut |
| 11 | Key and time signature as explicit fields | **PASS — both DOCUMENTED** (A minor, 4/4) |
| 12 | All four sliders specified | PASS |

**Overall: PASS.**

---

## 9. Audition notes

1. **Register test — the primary judgement call.** If the chorus sounds victorious, the song has failed, however good it sounds. Listen for: a major-key resolve, a rising key change, a bright lead above the vocal, a sustained pad ending. Any of those means a register ban did not hold.
2. **Guitar bleed.** 200-500 Hz for strummed guitar body.
3. **Vocal ceiling.** The chorus peaks at D4. If a synth sits above the vocal in the chorus, the mix has no headroom and the voice will sound buried.
4. **Chorus differentiation.** Expect partial flattening — judge the palette and register, not the pass-to-pass dynamics.
5. **Bridge anaphora.** `And now I'm falling / calling / crawling / drowning` — four lines, same opening, escalating. The arrangement must mark the ladder without a guitar build. If all four sit at one level, the bridge is a list.
6. **Ending.** No written outro. A fade is a fail — a hard cut says the story stops.
7. **Tempo.** 107 anchor. If the render drags, darkwave defaults are the cause, not the input value.

---

## 10. Lineage

- Song facts and lyrics: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/is-this-how-it-ends.md` (read direct 2026-10-30)
- Key resolution: Principal ruling 2026-09-14, recorded in that file
- Series reference: `docs/2026-10-30-sad-song-velvut-synth-conversion-suno-prompt.md`
- Prompt spec: `.a0proj/skills/suno-prompt-compatibility-spec/SKILL.md`
- Role matrix: `.a0proj/skills/suno-integration/SKILL.md` (PRD 5.4)
- DAW guide: `docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md`
