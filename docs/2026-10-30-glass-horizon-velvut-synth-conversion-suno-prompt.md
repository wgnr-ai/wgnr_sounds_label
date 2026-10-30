---
last_updated: 2026-10-30T17:44:00
status: delivered
artist: Velvut
song: Glass Horizon
series_position: 9
route: suno-synth-re-render
tempo: UNVERIFIED — not documented
key: UNVERIFIED — not documented
time_signature: UNVERIFIED — not documented
vocal_range: F2-D4
suno_role: assist
direction_status: out-of-scope
master_source: studio
---

# GLASS HORIZON (Velvut) — Synth Conversion Suno Prompt Set

**Artist:** Velvut · **Song:** Glass Horizon · **Date:** 2026-10-30 · **Series:** song 9
**Route:** Suno synth re-render (reference only) · **Purpose:** arrangement direction for the GarageBand rebuild

---

## 0. The structural problem — read first

**This is the only song in the series where production directions are written inside the lyric body.** Every other file confines direction to `### Style Notes`; this one interleaves bracketed instructions line by line:

```
[Verse 1]
[Guitar enters]                    ← direction, not lyric
[Simple driving downstrokes...]    ← direction, not lyric
Static humming through the bedroom floor   ← lyric
```

**Consequence:** the vault text cannot be pasted into Suno's lyrics field as-is. Suno would either sing the directions or choke on them. §4 therefore delivers **two blocks** — the field-ready text with directions stripped, and the vault verbatim text for the record — plus a line-by-line table of every bracket removed.

**No sung word is changed anywhere in this document. Only bracketed directions move, and they move into the style prompt where they belong.**

### Documented facts and gaps

| Field | Value | Status |
|---|---|---|
| Tempo | **UNVERIFIED — not documented** | Absence verified |
| Key | **UNVERIFIED — not documented** | Absence verified |
| Time signature | **UNVERIFIED — not documented** | Absence verified |
| Style notes | **DOCUMENTED — the strongest notes in the series** | See §2 |
| Exclusions | None recorded | Absence verified |

### The style conflict — a real one, not a formatting quirk

The file states its style twice, differently:

| Where | Says |
|---|---|
| Line 12, inline | `[Style: Post-Hardcore, Aggressive, Dynamic, Melodic Rock]` |
| Line 93, Style Notes | `Alt-rock, nu-metal, Y2K punk-pop, ... dynamic industrial rock, male baritone vocalist` |

**Post-hardcore is not in the second list. Y2K punk-pop is not in the first.** These are different records.

**Resolution taken:** the **Style Notes govern.** They are the maintained field, they are specific about instrumentation, and they are the only place the vocal is described. The line-12 `[Style:]` tag is treated as a working note from the generation session and is not carried into the prompt. If that is wrong, say so — it changes the whole tone of the render.

---

## 1. Verified song facts

Source: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/glass-horizon.md` (read direct 2026-10-30, `last_updated: 2026-08-19T21:46:00`, `status: draft`).

| Field | Value |
|---|---|
| Title | **Glass Horizon** — no question mark |
| Album | `TBD` |
| Recording state | `draft`; no recording referenced |
| Style notes (verbatim) | Alt-rock, nu-metal, Y2K punk-pop, heavy chugging guitar riffs, snaking electronic synth loops, aggressive dance-floor stomp beat, dynamic industrial rock, male baritone vocalist, deep resonant gritty male voice, urgent and swaggering attitude |
| Structurally unusual | Inline production directions throughout (see §0, §4) |
| Vocal | **Deep resonant gritty male voice, urgent and swaggering** — song-level, documented. Artist range F2–D4 from `artist-facts.md` |
| Suno role | Suno-assist (PRD §5.4) — `master_source = studio` |

### What the style notes give us that others did not

**`snaking electronic synth loops` is already in the original.** This is the only song in the series where a synth element is documented in the source material rather than substituted in. It is the single most valuable phrase in the file — it means the synth conversion is not a replacement, it is a promotion of something that was already there.

**`aggressive dance-floor stomp beat` is a tempo instruction without a number.** It is the closest thing to a BPM this song has. Honour the feel; do not convert it into a guess.

---

## 2. Style prompt — paste into Style of Music

```
dark industrial synth-rock, electro-industrial, punk-driven, urgent, swaggering, confrontational, dance-floor stomp, distorted synth bass, hard sequenced saw-bass pulses on the beat, snaking electronic synth loops, detuned saw stack stabs, hard analog synth pads, aggressive mono-synth lead with portamento, metallic industrial percussion hits, programmed kick with weight, four-on-the-floor verse pulse, wall-of-sound choruses, explosive chord stabs, quiet-loud dynamics, tom-tom-groove verse three, sub-bass weight, analog tape saturation, room reverb, deep resonant gritty male baritone vocal upfront, urgent baritone delivery, spoken-rap bridge delivery, memorable chorus hook, abrupt cut ending
```

### What changed from the series palette, and why

This is the **fastest-reading and least dark** song in the series. The palette holds; the energy profile does not.

| Series default | This song | Reason |
|---|---|---|
| `bleak, exhausted, slow crush` | `urgent, swaggering, confrontational` | The lyric is a demand, not a lament: `Give me a reason or give me the blade`. Exhaustion would neuter it. |
| `pads and pulse, sparse verses` | `four-on-the-floor verse pulse` | `Aggressive dance-floor stomp beat` is documented. A dance-floor stomp is not sparse. |
| Static synth bass | `snaking electronic synth loops` | **Documented in the source.** Promoted, not invented. |
| Absent or implied drive | `punk-driven` | Y2K punk-pop is documented. At this energy it reads as attack, not as era pastiche. |

### Substitution map — mostly documented this time

| Original role (documented) | Synth replacement |
|---|---|
| `heavy chugging guitar riffs` | distorted synth bass + hard sequenced saw-bass pulses on the beat |
| `snaking electronic synth loops` | **kept as written — this is the one element that does not need replacing** |
| Power chords / wall of sound | detuned saw stack stabs + hard analog synth pads + explosive chord stabs |
| `octave lead guitar` | aggressive mono-synth lead with portamento |
| Tom-tom groove (verse 3) | metallic industrial percussion + programmed kick with weight |
| Guitar solo | **instrumental synth-lead break** — see §5 |

Only three of six roles are substitutions. That is the smallest conversion in the series.

### The Y2K trap

`Y2K punk-pop` is documented, and it is the highest-risk phrase in this file.

Suno reads Y2K as **production era**, not as rhythmic attitude. Give it that word and it reaches for bright compressed guitars, clean pop-punk sheen, and a chorus that sounds like 2001. That is the failure mode here — not sentimentality as on Maybe We'll Meet Again, not triumph as on Is This How It Ends?, but **a bright, dated, radio-friendly wrongness**.

**The word `Y2K` and `punk-pop` do not appear in the style prompt.** The energy is carried by `punk-driven`, `urgent`, `swaggering`, `dance-floor stomp`. The era is excluded in §3. Attitude in, production era out.

### Vocal handling

`deep resonant gritty male voice, urgent and swaggering` is a **song-level** direction and it is specific — grittier and more forward than the series baseline. It is carried nearly verbatim.

The floor is F2 and the bridge is rapid-fire; that combination is where a baritone runs out of air. The bridge is marked `spoken-rap` in the prompt to keep it in speech register rather than pushing it up into a sung line.

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
pop-punk, Y2K, 2000s, early 2000s, skate punk, blink-182, sum 41, avenged sevenfold, post-hardcore, metalcore, screamo, screaming vocals, harsh vocals, four-on-the-floor EDM, big room, hardstyle, dubstep, trance, bright compressed guitars, guitar tone, guitar feedback, nostalgic, upbeat, cheerful, party, stadium rock, triumphant, anthemic chorus, fade out, fade ending, resolving outro, final chord resolve, ambient outro
```

**Why each block exists:**

1. `pop-punk, Y2K, 2000s, early 2000s, skate punk, blink-182, sum 41` — the era trap, from §2. If Suno gets the decade, the render is bright and dated no matter how heavy the low end is.
2. `avenged sevenfold, post-hardcore, metalcore, screamo, screaming vocals, harsh vocals` — the line-12 `[Style:]` tag. Even though it is not carried into the prompt, Suno can infer post-hardcore from `aggressive` + `baritone` + fast tempo. These keep the vocal singing.
3. `four-on-the-floor EDM, big room, hardstyle, dubstep, trance` — `dance-floor stomp` plus industrial tags plus sub-bass is the standard EBM stomp recipe. The song wants a stomp, not a rave.
4. `bright compressed guitars, guitar tone, guitar feedback` — the guitar artifacts that survive a synth prompt most easily, including the ambiguous `tone` phrasing.
5. `triumphant, anthemic chorus` — the chorus is already marked `[Anthemic]` in the vault. That is a dynamic instruction (big), not an emotional one (victorious). The song is angry, not victorious.
6. `fade out, fade ending, resolving outro, final chord resolve, ambient outro` — **the vault says `[Abrupt End]`.** A fade on an abrupt-end song is a direct contradiction of the written direction. Highest-confidence ban in the set.

---

## 4. Lyrics field

### 4a. Field-ready block — paste this into Suno

**All bracketed production directions removed. All sung words byte-identical to the vault.**

```
[Intro]

[Verse 1]
Static humming through the bedroom floor
Feet are pacing to the hallway door
Blue light flashing from a broken screen
Living inside of a ghost machine

[Verse 2]
The air is heavy and the roof is low
Nowhere left for the mind to go
Counting the lines on the peeling paint
The silence is loud enough to make me faint

[Pre-Chorus]
Is anybody listening out in the dark?
Waiting for a match to catch a spark

[Chorus]
Break the glass horizon, tear it down!
I’m sick of drowning in a silent town!
Give me a reason or give me the blade
Look at the mess that we’ve already made!
Break it down!

[Verse 3]
The sirens are singing a familiar tune
Washing the street under a plastic moon
We bought the promise and we swallowed the lie
Watching the world under a synthetic sky

[Bridge]
Pushed to the edge
Trapped on the ledge
Can't catch a breath
Sinking to death
Give me a crack
Don't hold me back
Ready to blow
Ready to go!

[Chorus]
Break the glass horizon, tear it down!
I’m sick of drowning in a silent town!
Give me a reason or give me the blade
Look at the mess that we’ve already made!
Break it down!

[Instrumental Break]

[Chorus]
Break the glass horizon, tear it down!
I’m sick of drowning in a silent town!
Give me a reason or give me the blade
Look at the mess that we’ve already made!

[Outro]
Break it down!
Tear it down!
Glass horizon!
```

### 4b. Every bracket removed, and where it went

| Vault bracket | Disposition |
|---|---|
| `[Style: Post-Hardcore, ...]` | **Dropped.** Contradicts Style Notes; see §0. Not carried anywhere. |
| `[Solo Drum Intro]` | → `[Intro]` label; concept carried as `programmed kick with weight` + drum-forward opening in §5. |
| `[Guitar enters]` | **Dropped.** Obsolete — no guitar. Replaced by the synth-bass entry in §5. |
| `[Simple driving downstrokes on the beat]` | → style prompt: `hard sequenced saw-bass pulses on the beat`. |
| `[Guitars build]` | → style prompt: pre-chorus is implied by structure; no guitar build exists. |
| `[Wall of sound guitars]` | → style prompt: `wall-of-sound choruses`. |
| `[Sustained ringing drone chords]` | → style prompt: `hard analog synth pads`. A sustained drone is a pad, not a new element. |
| `[Explosive baritone delivery]` | → style prompt: `urgent baritone delivery`. |
| `[Quiet loud dynamics]` | → style prompt: `quiet-loud dynamics`. |
| `[Drop to Tom-Tom groove]` | → style prompt: `tom-tom-groove verse three`. |
| `[Melodic Rap Delivery]` | → style prompt: `spoken-rap bridge delivery`. **Meaning altered deliberately** — see below. |
| `[Unexpected chord progression]` | → style prompt: *not carried.* See §5; with no documented key this is unenforceable. |
| `[Anthemic]` | → style prompt: `explosive chord stabs` + `wall-of-sound choruses`. The word *anthemic* itself is excluded — see §3 item 5. |
| `[Explosive chords]` | → style prompt: `explosive chord stabs`. |
| `[Guitar Solo]` + `[Octave lead guitar]` | → `[Instrumental Break]` label; the lead content moves to the mono-synth lead. No guitar solo exists. |
| `[Explosive Outro]` | → style prompt: `abrupt cut ending`. |
| `[Abrupt End]` | → style prompt: `abrupt cut ending`. **This is the one direction with no substitute** — it is a hard requirement. |

### One deliberate change of meaning

`[Melodic Rap Delivery]` → `spoken-rap`. **Melodic rap on a baritone at speed pushes the vocal up the range**, and this song has no documented key, so there is no way to check whether that climb lands above D4 before it happens. `Spoken-rap` keeps the delivery low and rhythmic. If the Principal wants the melodic version, the bridge melody needs its range checked first — that is a real constraint, not a preference.

### Structural flags — decisions needed

1. **The third chorus drops `Break it down!`.** Choruses 1 and 2 end with it; the chorus after the solo does not. That reads as a deliberate build-and-hold, and it is the reason the outro can land `Break it down! / Tear it down!` as new material. **Preserved as written.** If it is a copy-paste omission, the third chorus gains its line and the outro loses its surprise.
2. **`[Verse 3]` follows `[Pre-Chorus Lift]`, not `[Verse 2]`.** Structurally non-standard but unambiguous — there is only one pre-chorus in the file and it sits between verses 2 and 3. Preserved as written.
3. **Mixed apostrophes.** `I’m` and `we’ve` are typographic; `Can't` and `Don't` are straight. Preserved exactly — invisible to Suno, visible to DistroKid lyric submission later.

---

## 5. Arrangement notes

### The three-chorus ladder

Unlike the previous songs, these choruses are **not identical**. The third is missing its closing shout, which is the arrangement.

| Pass | Position | Arrangement |
|---|---|---|
| 1 | After pre-chorus | Full stack, first payoff. `Break it down!` lands as a demand. |
| 2 | After bridge | Heaviest. Bridge exit is a release of pressure; chorus 2 is the crash. |
| 3 | After instrumental break | **Full stack, no closing shout.** The phrase is withheld. `Break it down!` is heard in the listener's head and does not arrive. |
| Outro | End | The withheld line returns as `Break it down! / Tear it down! / Glass horizon!` — three lines, three levels, then cut. |

### The intro carries the whole concept

`[Solo Drum Intro]` is a real instruction and it survives the conversion intact: the synth rebuild opens with **programmed drums alone**. Not a pad, not a pulse — drums, and nothing else, until the bass enters.

That is the last genuinely acoustic-sounding element the song had. Opening on it tells the listener the energy is real before a single synth note appears.

### The instrumental break replaces the guitar solo

The vault gives it two instructions: `[Guitar Solo]` and `[Octave lead guitar]`. The **octave** part is what matters — the synth lead should play the solo line doubled at the octave, which is exactly the mono-synth lead with portamento doing what the octave lead guitar did.

The break is short. It is a bridge to the final chorus, not a showcase.

### The bridge is the riskiest 20 seconds in the song

Eight lines and a raising pattern (`Pushed / Trapped / Can't / Sinking / Give / Don't / Ready / Ready`), delivered at speed. On the demo this would have been a melodic rap over a guitar figure. On the synth rebuild:

- **Keep it low.** Spoken register, not sung. The words are already a rhythm.
- **Do not build under it.** The lyric already climbs (`Ready to blow` → `Ready to go!`). A synth build underneath is a second climb competing with the first.
- **`[Unexpected chord progression]` is not enforced.** With no documented key there is no target to hit, and a prompt asking for unexpected harmony on an undetermined key invites a random modulation. The line is dropped — flagged here rather than silently ignored.

### Ending

`[Abrupt End]` is written. The style prompt carries `abrupt cut ending`; the exclusions ban every fade, resolve, and ambient tail. **Cut on the word `horizon!`.** A ring-out is a fail; a fade is a fail.

---

## 6. Creative sliders

**Mode:** Custom, no audio upload. Held at validated series values — this song gets the least deviation of any in the series.

| Control | Value | Mode | Reasoning |
|---|---|---|---|
| **Weirdness** | **30%** | Custom | The risk here is an era collision (Y2K pop-punk vs. industrial), and a collision is easiest to diagnose at low weirdness. Also the highest-energy song in the series — variance compounds with tempo. |
| **Style Influence** | **75%** | Custom | The era bans and the EDM bans are what keep `dance-floor stomp` from becoming a rave. They only hold enforced hard. |
| **Audio Influence** | **n/a — slider absent** | Custom (no upload) | Cover-mode value if the demo is used as reference later: **65%**. |
| **Variety** | **Off (0)** | Custom | Would rewrite the style prompt server-side and strip the Y2K and EDM blocks. Either of those slipping through ruins the render at this energy. |

**Max Mode: ON.** **Personalize: off.**

**Retry ladder:**

- Bright / dated / pop-punk read → check for `Y2K` or `pop-punk` bleeding in; re-roll before touching sliders.
- Pure EBM stomp (four-on-the-floor with no punk edge) → Style Influence 85%.
- Screamed or harsh vocal → `screaming vocals` ban is holding; re-roll, do not accept the take.
- Structure collapsed, intro or break swallowed → Weirdness 20%.
- Ended on a fade → the single hardest fail. Re-roll; do not edit the ending in post.

---

## 7. Tempo, key, meter — the gap

**Nothing documented.** No frontmatter field, no prose value, no detector reading.

**What the file does give, without a number:**

- `aggressive dance-floor stomp beat` — a mid-to-fast, on-the-beat feel. A stomp is not a shuffle and not a half-time dirge.
- `urgent and swaggering attitude` — tempo is part of attitude; a slow read contradicts the lyric.
- Nine short chorus lines with exclamation marks, a sixteen-bar-feel verse, and a bridge that is eight fragments. **The lyric density itself argues against a slow tempo** — these lines do not fit at 107 BPM.

**What this means for the render:** Suno chooses. At this song's descriptor density it will likely land mid-to-fast, and it may well land right by feel — but *by feel is not verified*.

**It is also the one song in the series where an uninvented guess would be least harmful**, because the arrangement (dance-floor stomp, tom-tom groove, instrumental break) constrains tempo more than the style prompt does. That is an argument for not inventing a number, not against measuring one.

**Before the GarageBand rebuild:** measure the demo's BPM, key, and meter, and write them into the vault frontmatter. This song and Maybe We'll Meet Again Someday are the two weakest anchors in the series.

---

## 8. Suno role verification + compatibility checklist

**Suno-assist (PRD §5.4). `master_source = studio`.** `status: draft`, no recording referenced. This render is an arrangement reference for a song not yet recorded. Not a release master, not a demo replacement.

Baritone male descriptors carried, including the song-level `gritty` and `urgent and swaggering`. `female vocal` and `tenor vocal` excluded. `polished, mastered, final` excluded.

| # | Check | Result |
|---|---|---|
| 1 | Style prompt present | PASS |
| 2 | Lyrics verbatim from vault | **PASS WITH FLAGS** — every sung word byte-identical, but **17 bracketed production directions were stripped** (fully mapped in §4b) |
| 3 | Section labels per spec | **PASS WITH FLAG** — `[Pre-Chorus Lift]`→`[Pre-Chorus]`, `[Guitar Solo]`→`[Instrumental Break]` |
| 4 | Labels Title Case | PASS |
| 5 | Line breaks per spec | PASS |
| 6 | Title field present | PASS — no question mark |
| 7 | Negative prompt present | PASS |
| 8 | Suno role verdict | PASS — Suno-assist |
| 9 | Out-of-vocabulary tags flagged | **PASS WITH FLAGS** — the vault's inline directions are not a valid lyrics field; handled in §4a/§4b. Also *punk-driven*, *dance-floor stomp*, *spoken-rap* as non-standard style vocabulary |
| 10 | Per-artist structure | PASS — Velvut |
| 11 | Key and time signature as explicit fields | **FAIL — both UNVERIFIED, not documented.** Written as such in frontmatter, never inferred |
| 12 | All four sliders specified | PASS |

**Overall: PASS WITH FLAGS.** Two flags are structural rather than faults: check 2 because this file's format demands stripping, and check 11 because the values do not exist.

---

## 9. Audition notes

1. **Era test — the primary judgement call.** If it sounds like 2001, it has failed however energetic it is. Listen for bright compressed guitars, a clean pop-punk sheen, a chorus that resolves upward. This song should sound like a machine tearing a room apart, not like a warp tour.
2. **Stomp vs. rave.** Should feel like a crowd moving, not like a drop. If the four-on-the-floor dominates and the saw-bass attack is buried, it went EBM — Style Influence 85% and re-roll.
3. **The intro.** Drums alone before anything else. If a pad or a bass pulse is already running at second one, the instruction was ignored — but note Suno may overrule this regardless; it is the most likely instruction to be dropped.
4. **Vocal.** Gritty and forward, singing not shouting. Any screamed or harsh tone is a fail (`screaming vocals`, `harsh vocals` excluded).
5. **Bridge.** Low, fast, spoken-adjacent, no build underneath. If it climbs into a sung melody, the range constraint was not respected.
6. **Third chorus vs. the two before it.** It is missing `Break it down!`. If all three sound identical, the structural difference is being flattened by the render — judge the palette, not the dynamic nuance.
7. **The ending.** Hard cut on `horizon!`. A fade, a ring-out, or a final chord is a fail. This is the highest-confidence instruction in the song.
8. **Tempo.** Unknown by design. Judge whether it feels urgent and swaggering. Do not compare against a number.

---

## 10. Lineage

- Song facts, lyrics, and inline directions: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/glass-horizon.md` (read direct 2026-10-30)
- Vocal range and artist identity: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/artist-facts.md`
- Series reference: `docs/2026-10-30-sad-song-velvut-synth-conversion-suno-prompt.md`
- Structure and slider semantics: `docs/2026-10-30-is-this-how-it-ends-velvut-synth-conversion-suno-prompt.md`
- Prompt spec: `.a0proj/skills/suno-prompt-compatibility-spec/SKILL.md`
- Role matrix: `.a0proj/skills/suno-integration/SKILL.md` (PRD §5.4)
- DAW guide: `docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md`
