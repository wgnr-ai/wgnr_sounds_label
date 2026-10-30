---
last_updated: 2026-10-30T17:44:00
status: delivered
artist: Velvut
song: Are We Out of Time?
series_position: 12
route: suno-synth-re-render
tempo: UNVERIFIED — not documented
key: UNVERIFIED — not documented
key_quality: minor — DOCUMENTED ('minor key' in style notes)
time_signature: UNVERIFIED — not documented
vocal_range: F2-D4
suno_role: assist
direction_status: out-of-scope
master_source: studio
---

# ARE WE OUT OF TIME? (Velvut) — Synth Conversion Suno Prompt Set

**Artist:** Velvut · **Song:** Are We Out of Time? · **Date:** 2026-10-30 · **Series:** song 12
**Route:** Suno synth re-render (reference only) · **Purpose:** arrangement direction for the GarageBand rebuild

---

## 0. Read this first — the fade trap and three other gotchas

### Gotcha 1: the Outro says `fading`, and it is NOT a song fade

```
[Outro - Heavy syncopated drum accents, fading wailing guitar]
```

**The guitar fades. The song does not.** Every previous document in this series carries a standing ban on fades, and applying that ban blindly here would contradict the file.

What the instruction actually describes: the wailing lead line decays and disappears while the drums keep hitting. That is an **instrumental fade-out over a live arrangement** — the track ends on drums, hard, with the lead already gone.

**The distinction is load-bearing.** A song fade means the ending is unresolved and the listener is released. This is the opposite: the noise stops, the percussion continues, then it cuts. Getting this wrong flips the song's meaning.

### Gotcha 2: the Intro direction is inside the section label

```
[Intro - Sudden start, sharp wailing guitar riff]
```

Unlike Glass Horizon and These Phantom Walls, this file does not put directions on separate bracket lines. **The direction is embedded in the label itself**, which means a naive strip-and-paste removes it silently. It is mapped in §4b.

`Sudden start` is a real instruction and the hardest one to honour — it means no ramp-up, no count-in, no atmosphere. The song begins mid-gesture.

### Gotcha 3: the Bridge is empty

`[Bridge - Halftime breakdown, analog tape distortion, gritty guitars]` has **no lyric lines**. Same device as These Phantom Walls' empty pre-chorus, and the same problem: Suno will skip it or fill it. The halftime breakdown is the whole content.

### Gotcha 4: the title has a question mark

**Are We Out of Time?** — the `?` is in the filename, the H1, and the lyrics. It is consistent across all three, which is stronger evidence than Take Me Back?, where the evidence was a single title line. **Still not ruled on.** It matters for DistroKid metadata later; it does not matter for the Suno render, which uses the title as given.

---

## 1. Verified song facts

Source: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/are-we-out-of-time.md` (read direct 2026-10-30, file last_updated 2026-07-31, status draft).

| Field | Value | Status |
|---|---|---|
| Title | **Are We Out of Time?** — with question mark | DOCUMENTED (filename, H1, lyrics all agree) |
| Tempo | **UNVERIFIED — not documented** | Absence verified |
| Key | **UNVERIFIED — not documented** | No key name anywhere |
| Key quality | **minor — DOCUMENTED** (`minor key`) | Quality known, name unknown |
| Meter | **UNVERIFIED — not documented** | — |
| Album | `TBD` | — |
| Recording state | `draft` | — |
| Style notes (verbatim) | alt rock, nu-metal influences, minor key, powerful baritone vocal, upfront vocals, analog tape saturation, room reverb, wailing guitars, tight rhythm guitars, deep bass, full drum kit performance, explosive chorus lift | DOCUMENTED |
| Structure | Intro → V → Pre-C → C → V → **Bridge (empty)** → Pre-C → C → Outro → End | DOCUMENTED |
| Vocal | `powerful baritone vocal, upfront vocals` — song-level. Artist range F2–D4 | DOCUMENTED |
| Inline directions | **9**, all embedded in section labels — see §4b | DOCUMENTED |

### This song and Is This How It Ends? share a style-note block

The lists are nearly identical — same `alt rock`, `nu-metal influences`, `minor key`, `powerful baritone vocal`, `upfront vocals`, `analog tape saturation`, `room reverb`, `wailing guitars`, `tight rhythm guitars`, `deep bass`, `full drum kit performance`, `explosive chorus lift`.

**That means the style notes cannot differentiate the two songs.** Everything that makes this song distinct has to come from the lyric and the arrangement, not from the palette. §2 does that work explicitly.

### What is genuinely different here: the subject

Every other song in the series is personal — addiction, regret, isolation, entrapment. **This is the only Velvut song that looks outward.** Collapse, greed, sirens, a corner store closing, `Who are we fighting for / Why do they make us bleed`.

That changes the failure mode (§2) and it changes what the arrangement owes the vocal.

---

## 2. Style prompt — paste into Style of Music

```
dark industrial synth-rock, electro-industrial, punk-driven urgency, minor key, public collapse, anxious, wide-eyed rather than mournful, distorted synth bass, hard sequenced saw-bass pulses, syncopated drum accents, detuned saw stack stabs, hard analog synth pads, aggressive mono-synth lead with portamento, wailing lead synth line, metallic industrial percussion hits, programmed kick with weight, tom-tom-groove verses, halftime breakdown in the bridge, quiet-loud dynamics, explosive chorus lift, wall-of-sound choruses, sub-bass weight, analog tape saturation, room reverb, powerful baritone male vocal upfront, urgent delivery, memorable chorus hook, sudden cold start
```

### Differentiating from Is This How It Ends? — the real work

Both songs have the same style notes and the same palette. If the render does not differentiate them, the album has two songs that sound alike.

| Dimension | Is This How It Ends? | This song |
|---|---|---|
| Subject | Personal — addiction, suicidal ideation | Public — collapse, greed, a failing world |
| Emotional position | Collapse from inside | Alarm from outside |
| Register words | `bleak, exhausted, slow crush` | `public collapse, anxious, wide-eyed` |
| Vocal stance | Strained, weary, unheroic | Urgent, awake, accusing |
| Opening | Opens on a synth-bass pulse | **`sudden cold start` — begins mid-gesture** |
| Ending | Hard cut on an unanswered question | Drums continue after the lead decays, then cut |

**The single most important differentiator is the vocal stance.** Is This How It Ends? is a man drowning. This is a man watching something else drown and being angry about it. Same voice, opposite direction of attention.

### The register judgement call — fourth variant in the series

| Song | Failure mode |
|---|---|
| Is This How It Ends? | Triumph |
| Maybe We'll Meet Again Someday | Sentimentality |
| Feeling Alone | Self-pity |
| **Are We Out of Time?** | **Protest grandiosity — a rally anthem** |

The lyric is the most quotable in the series: `I can smell it burn`, `I can taste the greed`, `Are we out of time?` Those lines want a stadium. Given a big enough chorus and a baritone at full power, Suno will produce something that sounds like a benefit single — righteous, communal, and completely wrong for a band whose whole identity is private dread.

The counterweight is `anxious` and `wide-eyed rather than mournful`. **The song is not certain. It is frightened.** A protest anthem knows the answer; this song ends on the question twice and never resolves it.

### Syncopated drum accents — the opposite of These Phantom Walls

Worth stating because the two documents sit next to each other in this series:

- **These Phantom Walls:** `no syncopation`. Gated pulses banned, eight exclusion terms enforce it.
- **This song:** `syncopated drum accents` documented twice (chorus and outro).

The palettes look contradictory and are not. These Phantom Walls is a 92 BPM trapped-in-a-room song; this is a mid-tempo alarm. **Do not carry the no-syncopation exclusions here** — they would strip a documented instruction.

### Vocal handling

`powerful baritone vocal, upfront vocals` — same wording as Is This How It Ends?. The differentiator is delivery, not descriptor: `urgent delivery` against that song's `strained and weary`.

F2 floor. The chorus sits on short, declarative lines — `I can smell it burn / I can taste the greed` — which are rhythmically tight and do not require a climb. The title question `Are we out of time?` repeated twice is the only line that invites a rise. Cap it at the B3–C#4 planning zone; do not let it reach D4.

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
protest song, rally, anthem, stadium rock, stadium chorus, triumphant, victorious, righteous, heroic, uplifting, hopeful, singalong, crowd vocals, gang vocals, choir vocals, marching drums, military snare, bagpipes, political punk, folk punk, gospel, celebration, major-key resolve, key change up, soaring, epic build, fade out, fade ending, song fade, resolving outro, final chord resolve, sustained outro pad, ambient outro, ascending outro, bright lead synth above the vocal
```

**Why each block exists:**

1. `protest song, rally, anthem, stadium rock, stadium chorus, triumphant, victorious, righteous, heroic, uplifting, hopeful, singalong, crowd vocals, gang vocals, choir vocals` — **the highest-stakes block in the set.** The lyric is quotable and public-facing. Every one of these turns it into something a crowd sings together, which inverts the song from alarm into resolve.
2. `political punk, folk punk, marching drums, military snare, bagpipes` — the specific instruments and genres Suno reaches for when it hears `sirens`, `fighting`, `bleed`. A snare march makes it a protest march.
3. `major-key resolve, key change up, soaring, epic build` — `minor key` is documented. The song does not turn, and the question is never answered.
4. `fade out, fade ending, song fade, resolving outro, final chord resolve, sustained outro pad, ambient outro, ascending outro` — **this is the Gotcha 1 block.** The file says `fading wailing guitar`, and Suno will read the word *fading* as a song fade unless told otherwise. The instrument fades; the track cuts. Every fade variant is excluded so only the guitar can decay.
5. `bright lead synth above the vocal` — the D4 ceiling guard, standard across the series.

---

## 4. Lyrics field

### 4a. Field-ready block — paste this into Suno

**All sung words byte-identical to the vault. Directions stripped from 9 section labels** (mapped in §4b). Labels normalised to canonical form.

```
[Intro]

[Verse 1]
Every morning I watch the sun rise
In the distance I hear so many cries
How much longer do we have now
It's not a question of when or how

Sirens cut through the 6 a.m. haze
News on the radio feels out of place
Kids with their phones and their heads down low
Watching the damage while the old walls go

[Pre-Chorus]
Do we deserve any better after all
With everything we let fall?

[Chorus]
I can smell it burn
I can taste the greed
Who are we fighting for
Why do they make us bleed

Feels like it's going to burst
Feels like it's been a lifetime
I can't help but wonder
Are we out of time?
Are we out of time?

[Verse 2]
Boxes on the porch, bills on the chair
Nobody says it, but everybody's scared
We keep saying maybe tomorrow's the day
While the whole thing slips a little more away

I saw the corner store with the taped-up sign
Closed for the third time in a month this time
If there's a line between fixed and done
We crossed it quiet, one by one

[Bridge]

[Pre-Chorus]
Do we deserve any better after all
With everything we let fall?

[Chorus]
I can smell it burn
I can taste the greed
Who are we fighting for
Why do they make us bleed

Feels like it's going to burst
Feels like it's been a lifetime
I can't help but wonder
Are we out of time?
Are we out of time?

[Outro]
```

### 4b. Every change, and where it went

**All nine directions were embedded in section labels.** Each is extracted here:

| Vault label | Field label | Direction extracted and where it went |
|---|---|---|
| `[Intro - Sudden start, sharp wailing guitar riff]` | `[Intro]` | `sudden start` → prompt: `sudden cold start`. `sharp wailing guitar riff` → prompt: `wailing lead synth line`. **This is Gotcha 2** — stripping the label would have lost both. |
| `[Verse - Tom-tom drum groove, deep bass]` | `[Verse 1]` | → prompt: `tom-tom-groove verses`; `deep bass` is already in the core palette as `distorted synth bass` + `sub-bass weight`. |
| `[Pre-Chorus - Tight rhythm guitars building tension]` | `[Pre-Chorus]` | → prompt: `hard sequenced saw-bass pulses` carries the tension build; `tight` is a guitar descriptor with no synth equivalent worth inventing. |
| `[Chorus - Explosive lift, heavy wailing guitars, syncopated drum accents, powerful vocal performance]` | `[Chorus]` | → prompt: `explosive chorus lift`, `wall-of-sound choruses`, `wailing lead synth line`, `syncopated drum accents`, `powerful baritone male vocal upfront`. **Four documented instructions from one label.** |
| `[Verse - Back to tom-tom groove, clean bass]` | `[Verse 2]` | → prompt: `tom-tom-groove verses`. `clean bass` is the one instruction **dropped deliberately** — see below. |
| `[Bridge - Halftime breakdown, analog tape distortion, gritty guitars]` | `[Bridge]` | → prompt: `halftime breakdown in the bridge`. `analog tape distortion` → `analog tape saturation`. `gritty guitars` → `detuned saw stack stabs` at the point where the bridge would sit. Empty section — see §5. |
| `[Pre-Chorus - Building up, rhythm guitars punching]` | `[Pre-Chorus]` | → prompt: already covered by the saw-bass pulses. `punching` is guitar-attack language with no added information. |
| `[Chorus - Explosive lift, full volume, upfront vocals]` | `[Chorus]` | → prompt: `explosive chorus lift`, `wall-of-sound choruses`, `powerful baritone male vocal upfront`. `full volume` is the same instruction as explosive lift. |
| `[Outro - Heavy syncopated drum accents, fading wailing guitar]` | `[Outro]` | → prompt: `syncopated drum accents`; `fading wailing guitar` → the lead decay described in §5. **This is Gotcha 1.** |
| `[End]` | *removed* | Not a lyrics-field construct. Enforced in §5 as a hard cut after the drums. |

### One instruction dropped deliberately: `clean bass`

Verse 2 is marked `Back to tom-tom groove, **clean bass**` — the only place in the file where the bass is specified as clean rather than distorted.

**It is not carried.** Reason: the entire synth conversion rests on the distorted synth bass being the rhythm instrument. A `clean bass` token in the style prompt would let Suno read the whole bass part as clean, and Suno cannot scope a style token to one verse. **The dynamic change it implies is preserved as an arrangement note instead** (§5: verse 2 pulls the distortion back, not off).

If you want a genuinely clean bass in verse 2, that is a GarageBand decision, not a Suno one — flag it in the rebuild.

### Structural flags — preserved as written

1. **The bridge is empty.** No lyric lines at all. Preserved as an empty label.
2. **Two verses, two pre-choruses, two choruses — all byte-identical within type.** The pre-chorus and chorus repeat word-for-word. Nothing changes across the song except the verses.
3. **Verse 1 and Verse 2 are each two four-line stanzas under one label.** No `[Verse 2]` label exists in the vault for the second stanza of each — the stanza break is a blank line. Labelled `[Verse 1]` / `[Verse 2]` in the field block for Suno's benefit; the stanzas themselves are unaltered.
4. **`We crossed it quiet, one by one`** — *quiet* used as an adverb where standard English wants *quietly*. Preserved exactly. It reads as deliberate compression and it improves the line.
5. **Straight apostrophes throughout** (`It's`, `can't`, `there's`, `everybody's`, `tomorrow's`). Preserved.

---

## 5. Arrangement notes

### The sudden start is the hardest instruction in the song

`Sudden start` means the track begins at full commitment — no intro pad, no riser, no fade-in, no count-in. On the original this was a sharp wailing guitar riff hitting cold.

**In the rebuild:** the mono-synth lead hits on beat one, mid-phrase, with the full rhythm section already running. Nothing enters gradually.

Expect Suno to add an atmosphere or a drum pickup regardless. That is the most likely instruction in this document to be ignored, and it should be noted rather than accepted silently.

### The empty bridge is a halftime breakdown, not a solo

`[Bridge - Halftime breakdown, analog tape distortion, gritty guitars]` with no words. Same situation as These Phantom Walls' empty pre-chorus, with one difference: **this one names `halftime`.**

So the section is not silence and not a lead showcase — it is a rhythmic collapse. The drums drop to half time, the tape saturation pushes, the low end gets dirtier, and nobody sings. Then the pre-chorus punches back in.

Do not fill it with a lead line. The halftime is the event.

### Chorus and pre-chorus repeat verbatim — the arrangement carries the change

| Pass | Position | Arrangement |
|---|---|---|
| Pre-Chorus 1 | After verse 1 | Tighter, building. Bass entering. |
| Chorus 1 | After pre-chorus 1 | Full stack. First payoff. |
| Pre-Chorus 2 | After empty bridge | **Punchier than the first** — this is the exit from the halftime collapse, so it should feel like a slam back into gear. |
| Chorus 2 | After pre-chorus 2 | Full stack, no further build. Slightly heavier low end than chorus 1. |

**Known limitation, as always:** Suno cannot be told "chorus 2 is heavier" without editing lyrics it must keep clean. Expect flattening. Judge palette and register.

### The ending — the fade that is not a fade

This is the Gotcha 1 resolution, stated as an arrangement:

1. **Lead decays.** The mono-synth lead fades out across the outro. That is the documented `fading wailing guitar`.
2. **Drums keep hitting.** `Heavy syncopated drum accents` continue underneath, now exposed because the lead is gone.
3. **Hard cut.** `[End]` is written. The drums stop. No ring-out, no resolve, no ambient tail.

**A song-wide fade is a fail.** The distinction is that the listener never gets released — the arrangement thins to percussion and then stops dead. That is the opposite feeling from a fade-out.

---

## 6. Creative sliders

**Mode:** Custom, no audio upload. Values held at series standard.

| Control | Value | Mode | Reasoning |
|---|---|---|---|
| **Weirdness** | **30%** | Custom | The failure mode is a register fault (protest grandiosity), same as every other song in the series. Low weirdness keeps a wrong register a readable prompt fault rather than variance. |
| **Style Influence** | **75%** | Custom | Fourteen exclusions exist purely to stop this becoming a rally anthem, plus the fade block. It only holds enforced hard. |
| **Audio Influence** | **n/a — slider absent** | Custom (no upload) | Cover-mode value if the demo is used as reference later: **65%**. |
| **Variety** | **Off (0)** | Custom | Would rewrite the style prompt server-side and strip the anti-anthem and anti-fade blocks — the two most load-bearing in this set. |

**Max Mode: ON.** **Personalize: off.**

**Retry ladder:**

- Rally / anthem / crowd-singalong read → check for `uprising`, `rise`, or `unite` language slipping in; re-roll before touching sliders.
- Song fade at the end → the Gotcha 1 block failed. Re-roll; do not fix the ending in post.
- Guitar bleed → Style Influence 85%.
- Sounds too close to Is This How It Ends? → check the vocal stance. If it reads weary rather than alert, the prompt lost `anxious` and `wide-eyed`.
- No sudden start → expected; note it, judge the rest.

---

## 7. Tempo, key, meter

### Tempo — undocumented

No BPM, no prose value, no detector reading. **Not inferred.**

What the file implies without a number: `syncopated drum accents`, a halftime bridge, and short declarative chorus lines. A halftime bridge only means something against a tempo it can halve, which suggests a mid-tempo at least. **That is a reading, not a measurement.**

### Key — quality documented, name not

`minor key` is in the style notes. Which minor key is not recorded. The prompt carries `minor key` exactly as documented, and the exclusions ban `major-key resolve` and `key change up`. Frontmatter records the key as UNVERIFIED with a separate documented `key_quality`.

### Meter — undocumented

No time signature anywhere. Not inferred.

---

## 8. Suno role verification + compatibility checklist

**Suno-assist (PRD §5.4). `master_source = studio`.** `status: draft`, no recording referenced. Arrangement reference for a song not yet recorded. Not a release master, not a demo replacement.

Powerful baritone carried (`powerful baritone vocal`, `upfront vocals`). `female vocal` and `tenor vocal` excluded. `polished, mastered, final` excluded.

| # | Check | Result |
|---|---|---|
| 1 | Style prompt present | PASS |
| 2 | Lyrics verbatim from vault | PASS — every sung word byte-identical |
| 3 | Section labels per spec | **PASS WITH FLAG** — 9 labels normalised; all embedded directions extracted and mapped in §4b |
| 4 | Labels Title Case | PASS |
| 5 | Line breaks per spec | PASS |
| 6 | Title field present | **PASS WITH FLAG** — question mark present in filename, H1 and lyrics. **Not ruled on** for DistroKid metadata |
| 7 | Negative prompt present | PASS |
| 8 | Suno role verdict | PASS — Suno-assist |
| 9 | Out-of-vocabulary tags flagged | **PASS WITH FLAGS** — `sudden cold start`, `public collapse`, `wide-eyed rather than mournful`, `syncopated drum accents` as non-standard style vocabulary |
| 10 | Per-artist structure | PASS — Velvut |
| 11 | Key and time signature as explicit fields | **PARTIAL — key quality DOCUMENTED (minor); tempo, key name and meter UNVERIFIED.** Nothing inferred |
| 12 | All four sliders specified | PASS |

**Overall: PASS WITH FLAGS.** Two flags need your attention: the title question mark, and the `fading` reading in §0.

---

## 9. Audition notes

1. **Anthem test — the primary judgement call.** If it sounds like a crowd could sing it together, it has failed. Listen for: a march snare, a gang vocal, a resolve, a rising key change on `Are we out of time?` The song is frightened, not righteous.
2. **The fade test.** Two things must both be true: the lead decays, AND the song does not. If the whole track fades out, Gotcha 1 failed.
3. **The sudden start.** Full arrangement on beat one. If there is a pad intro, a riser, or a count-in, the instruction was ignored — likely, and worth noting rather than fixing.
4. **Differentiation from Is This How It Ends?** Same palette, same style notes. If the two renders sound like siblings, check the vocal stance first: weary vs. alert.
5. **The empty bridge.** Should be a halftime rhythmic collapse, not a lead solo and not silence.
6. **Syncopation.** Documented here and banned in These Phantom Walls. Do not carry that song's exclusions into this one.
7. **Vocal ceiling.** `Are we out of time?` is the only line that invites a climb. B3–C#4 planning zone; anything at D4 is over the cap.

---

## 10. Lineage

- Song facts, lyrics, embedded directions: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/are-we-out-of-time.md` (read direct 2026-10-30)
- Vocal range and artist identity: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/artist-facts.md`
- Sibling song and shared style notes: `docs/2026-10-30-is-this-how-it-ends-velvut-synth-conversion-suno-prompt.md`
- Syncopation contrast: `docs/2026-10-30-these-phantom-walls-velvut-synth-conversion-suno-prompt.md`
- Series reference: `docs/2026-10-30-sad-song-velvut-synth-conversion-suno-prompt.md`
- Prompt spec: `.a0proj/skills/suno-prompt-compatibility-spec/SKILL.md`
- Role matrix: `.a0proj/skills/suno-integration/SKILL.md` (PRD §5.4)
- DAW guide: `docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md`
