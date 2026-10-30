---
last_updated: 2026-10-30T17:44:00
status: delivered
artist: Velvut
song: Who's Calling Me?
series_position: 13
route: suno-synth-re-render
tempo: 148
key: UNVERIFIED — not documented
key_quality: minor — DOCUMENTED ('predominantly minor key' in style notes)
time_signature: UNVERIFIED — not documented
vocal_range: F2-D4
suno_role: assist
direction_status: out-of-scope
master_source: studio
---

# WHO'S CALLING ME? (Velvut) — Synth Conversion Suno Prompt Set

**Artist:** Velvut · **Song:** Who's Calling Me? · **Date:** 2026-10-30 · **Series:** song 13 of 13 (final)
**Route:** Suno synth re-render (reference only) · **Purpose:** arrangement direction for the GarageBand rebuild

---

## 0. This is the only finished song in the series — and the only approved demo

**Status: `final`.** Lyrics locked 2026-09-01. Written by the Principal — spine sections his, continuation and treatment passes by the WGNR Sounds creative team under his section-by-section calls. This is documented in the file itself and it is the strongest provenance in the series.

**The file also records an approved Suno demo:**

> Suno demo approved by the Principal the same session ("sounds like a hit, amazingly unique guitar riff")

**That sentence is the central problem of this document.** The approved element was a **guitar riff** — and this conversion deletes guitars entirely. The thing that made the demo work is exactly the thing the synth palette removes.

Every other song in this series converts something unheard. **This one converts something the Principal already approved.** That raises the bar: the substitute has to carry the same distinction the riff did, or the conversion is a downgrade.

### What that means in practice

| The riff did this | The synth lead must do this |
|---|---|
| Was the hook identity | Be the hook identity — `filtered mono-synth lead with portamento`, not a bed |
| Sat against palm-muted downstrokes | Sit against straight saw-bass pulses, rhythmically opposed |
| Was called *unique* | Be specific, not generic — this is where a preset lead fails |

**Flagged:** if the synth render comes back and the lead is anonymous, the correct response is not to re-roll at 30% weirdness — it is to consider whether this song keeps a guitar part. That is a separate decision from the rest of the series, and it is legitimate to make it differently here.

### Three more facts that shape this document

1. **148 BPM is documented** — the same figure as Take Me Back?. Both are genuine, not a copy error. This is a fast song.
2. **Directions are merged into section labels**, as on Are We Out of Time? — a naive strip loses them. Mapped in §4b.
3. **The bridge carries `steady level vocal`** — an unusual, extremely specific instruction. It means *no dynamic lift in the bridge*. See §2.

---

## 1. Verified song facts

Source: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/whos-calling-me.md` (read direct 2026-10-30, file last_updated 2026-09-01, **status: final**).

| Field | Value | Status |
|---|---|---|
| Title | **Who's Calling Me?** — with question mark | DOCUMENTED (filename, H1, lyrics) |
| Tempo | **148 BPM** | **DOCUMENTED** in style notes |
| Key | **UNVERIFIED — not documented** | No key name anywhere |
| Key quality | **minor — DOCUMENTED** (`predominantly minor key`) | Quality known, name unknown. Note *predominantly* — implies modal mixture, not a single key |
| Meter | **UNVERIFIED — not documented** | — |
| Album | `TBD` | — |
| Status | **`final`** — lyrics locked 2026-09-01 | DOCUMENTED |
| Authorship | Principal (spine) + creative team (continuation/treatment) under Principal's section calls | DOCUMENTED |
| Demo | **Suno demo approved; `amazingly unique guitar riff` cited** | DOCUMENTED — see §0 |
| Style notes (verbatim) | post-alternative rock, alt-metal edge, 148 BPM, low and deep baritone vocals, close-mic guitar, tom-tom verses, distorted power chords, palm-muted downstrokes, octave lead guitar, spring reverb, tape saturation, parallel compression, quiet loud dynamics, pre-chorus lift, anthemic chorus, predominantly minor key, memorable chorus hook | DOCUMENTED |
| Structure | Abrupt Intro → V1 → Pre-C → C → V2 → Pre-C → C → Bridge → Final Chorus | DOCUMENTED |
| Vocal | `low and deep baritone vocals`, plus `steady level vocal` in the bridge | DOCUMENTED — song-level |
| Inline directions | **7**, all embedded in section labels — see §4b | DOCUMENTED |

---

## 2. Style prompt — paste into Style of Music

```
dark industrial synth-rock, electro-industrial, post-alternative weight, alt-metal edge, 148 BPM, predominantly minor key, driving, decisive, quietly relieved and slightly unnerved, distorted synth bass, hard sequenced saw-bass pulses on straight-eighths, detuned saw stack stabs, hard analog synth pads, aggressive mono-synth lead with portamento, distinctive lead synth hook, metallic industrial percussion, heavy tom-tom drums groove in verses, programmed kick with weight, spring reverb, tape saturation, parallel compression, quiet loud dynamics, pre-chorus lift, wall-of-sound choruses, sub-bass weight, low and deep baritone male vocal upfront, steady-level bridge vocal, memorable chorus hook, hard cut ending
```

### The two-word problem: `anthemic chorus`

`anthemic chorus` is **documented in the style notes**, and it is the only song in the series where that word appears in the source material.

On Are We Out of Time? I excluded *anthemic* outright because the lyric was public alarm. **Here the word is the Principal's own instruction and the meaning is different**: this song's subject is the relief and unease of being alone. An anthemic chorus here means *big and declarative*, not *victorious*.

**So: `wall-of-sound choruses` carries the size, `anthemic` itself is not written into the prompt, and only the victory-words are excluded** (`triumphant`, `victorious`, `stadium`, `uplifting`). That respects the instruction while blocking the misread. If the render comes back too small, add `anthemic chorus` back before touching any slider.

### `steady level vocal` — the most specific instruction in the series

`[Bridge — bass, toms, rattling amp hum, steady level vocal]`

Every other verse or bridge in the series invites a build. **This one forbids it.** The vocal in the bridge stays at one level while everything else is stripped — bass, toms, amp hum.

That is a **texture section**, not a dynamic section. The narrator is recording a greeting and hearing himself be polite. The flat delivery is the whole point: he is not feeling it, he is performing it.

Carried as `steady-level bridge vocal` in the prompt. **No build, no lift, no crescendo into the final chorus.**

### `rattling amp hum`

A guitar-amp artifact, documented and specific. It is not a note — it is the sound of an amp idling. Converted as `tape saturation` plus the spring reverb bed. **Do not deliver it as guitar feedback**; the exclusions block that. If the render needs the literal hum, that is a GarageBand texture layer, not a Suno instruction.

### The 148 BPM consequence

This is the fast song of the series' documented tempos (147 on Under My Skin, 148 here and on Take Me Back?). At 148 with `pre-chorus lift` and a `steady level vocal` bridge, the arrangement has to be **intentional about where the energy sits**: verses moving, bridge flattened, choruses wide.

Fast plus industrial plus sub-bass is the EBM recipe. **`pre-chorus lift` and `quiet loud dynamics` are what keep it rock, not a club record** — both are documented and both are carried.

### `tom-tom verses` and `octave lead guitar`

- **Tom-tom verses** — documented. The same percussion character as These Phantom Walls, and the same treatment: tom-toms as the dominant voice in the verses.
- **Octave lead guitar** — documented. The synth lead doubles at the octave, as on Glass Horizon and These Phantom Walls.

### Vocal handling

`low and deep baritone vocals` — more emphatic than the series baseline. Carried as `low and deep baritone male vocal upfront`.

148 BPM. Chorus lines are short and repeated: `Who's calling me / I want to be left alone`. No climb is required by the lyric. The **bridge** is where this could go wrong — `steady level vocal` means do not let Suno push it. Keep it conversational, at the bottom of the usable range.

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
grunge, 90s, 1990s, alternative metal, nu-metal guitar tone, drop-tuned guitars, guitar feedback, amp feedback, numetal, rapcore, screaming vocals, harsh vocals, triumphant, victorious, stadium rock, stadium chorus, heroic, righteous, gospel, celebration, gang vocals, crowd vocals, singalong, four-on-the-floor EDM, big room, hardstyle, trance, dubstep, major-key resolve, key change up, soaring, epic build, bridge crescendo, building bridge, fade out, fade ending, resolving outro, final chord resolve, ambient outro, bright lead synth above the vocal
```

**Why each block exists:**

1. `grunge, 90s, 1990s, alternative metal, nu-metal guitar tone, drop-tuned guitars, guitar feedback, amp feedback` — the era trap, plus the specific risk that `rattling amp hum` summons literal feedback.
2. `numetal, rapcore, screaming vocals, harsh vocals` — `alt-metal edge` at 148 BPM is the invitation. The band has a baritone singer, not a shouter, and the bridge is deliberately flat.
3. `triumphant, victorious, stadium rock, stadium chorus, heroic, righteous, gospel, celebration, gang vocals, crowd vocals, singalong` — **the victory block.** `anthemic` is documented and permitted in spirit; victory is not. This song is about relief, not triumph.
4. `four-on-the-floor EDM, big room, hardstyle, trance, dubstep` — 148 BPM plus industrial plus sub-bass is the EBM stomp recipe.
5. `major-key resolve, key change up, soaring, epic build` — `predominantly minor key` is documented. The parenthetical *predominantly* allows modal colour, not a major resolve.
6. **`bridge crescendo, building bridge`** — the `steady level vocal` guard. This is the only song in the series where a build in the bridge is an error.
7. `fade out, fade ending, resolving outro, final chord resolve, ambient outro` — the file says `[Abrupt intro]` at the front and has no outro tag; the song ends on the final chorus. Hard cut.
8. `bright lead synth above the vocal` — the D4 ceiling guard.

---

## 4. Lyrics field

### 4a. Field-ready block — paste this into Suno

**All sung words byte-identical to the vault. Directions extracted from 7 merged labels** (mapped in §4b).

```
[Intro]

[Verse 1]
There's one box left in the hall
You didn't ask me at all
I only held the door
Like a hundred times before

Phone rang the minute you were gone
First one that's mine in so long
I let it ring through to the tone
First time the phone felt like my own

[Pre-Chorus]
Seemed like this day would never come
No one's calling me
The deafening silence makes me calm
But I know it won't last long

[Chorus]
Who's calling me
I want to be left alone
Who's calling me
Leave your message at the tone.

Who's calling me
I just want to be free
Who's calling me
Get away and leave me
Get away and leave me

[Verse 2]
First night out I roamed til two
No one waiting up it's true
The calm I wanted walked in too
Room's so quiet I can hear you

The day arrived I'm on my own
Walked out free to be alone
No one calls I check the phone
The silence moved in calls it home

[Pre-Chorus]
Seemed like this day would never come
No one's calling me
The deafening silence makes me calm
But I know it won't last long

[Chorus]
Who's calling me
I want to be left alone
Who's calling me
Leave your message at the tone

Who's calling me
I just want to be free
Who's calling me
Get away and leave me

[Bridge]
Set out to tape a new hello
Tired of that voice I'd outgrown
I pressed record and stood alone
Waited for a voice like my own

Had a new line ready to say
It came out the old polite way
So I kept it let it play
Politest lie I ever made

[Final Chorus]
Who's calling me
I want to be left alone
Who's calling me
Leave your message at the tone

Who's calling me
I just want to be free
Who's calling me
Get away and leave me
```

### 4b. Every change, and where it went

| Vault label | Field label | Direction extracted and where it went |
|---|---|---|
| `[Abrupt intro — no guitar sustain]` | `[Intro]` | `abrupt` → §5: opens straight in, no atmosphere. `no guitar sustain` → obsolete, no guitar exists; the exclusion block bans `guitar sustain intro` anyway. |
| `[Verse 1 — low baritone, bass-heavy, dry snare]` | `[Verse 1]` | → prompt: `low and deep baritone male vocal upfront`. `bass-heavy` → `sub-bass weight`. `dry snare` → not carried; the industrial percussion replaces the kit and a dry snare token would fight it. |
| `[Pre-Chorus]` | `[Pre-Chorus]` | No direction embedded. The documented `pre-chorus lift` is in style notes and is carried. |
| `[Chorus]` | `[Chorus]` | No direction embedded. `anthemic chorus` handled in §2. |
| `[Verse 2]` | `[Verse 2]` | No direction embedded. |
| `[Bridge — bass, toms, rattling amp hum, steady level vocal]` | `[Bridge]` | → prompt: `steady-level bridge vocal`. `bass, toms` → the stripped texture in §5. `rattling amp hum` → `tape saturation` + `spring reverb`; not literal feedback (see §2). **Four instructions from one label.** |
| `[Final Chorus]` | `[Final Chorus]` | Canonical already. No direction embedded. |

**Nothing else was changed. No sung word was altered.**

### Structural flags — preserved as written

1. **Chorus 1 doubles its closing tag; choruses 2 and 3 do not.** Chorus 1 ends `Get away and leave me` **twice**; the second chorus and the final chorus end it **once**. This is the mirror image of Glass Horizon, where the doubled/varied element came last. **Preserved exactly** — it means the biggest statement is the *first* chorus, and the song closes narrower than it opened. That is unusual and it is almost certainly deliberate.
2. **`Leave your message at the tone.` has a full stop.** Chorus 1 does. Choruses 2 and 3 do not. Preserved exactly.
3. **`roamed til two`** — `til` without an apostrophe. Preserved exactly. Not corrected to `'til`.
4. **`The silence moved in calls it home`** — no comma or conjunction between *in* and *calls*. Preserved exactly. Reads as deliberate compression.
5. **The bridge is two four-line stanzas with no label between them.** No `[Verse]` or second `[Bridge]` marker — a blank line only. Preserved.
6. **Straight apostrophes throughout** (`There's`, `didn't`, `it's`, `I'm`, `Who's`). Preserved.

---

## 5. Arrangement notes

### The lead is the whole bet

The approved demo's selling point was `amazingly unique guitar riff`. That riff is being deleted. **The mono-synth lead is not a supporting part on this song — it is the replacement for the reason the song was approved.**

Practical consequences for the rebuild:

- **It must be a hook, not a texture.** Specific intervals, recognisable, repeatable across the song.
- **Portamento is what makes it read as a lead rather than a sequence** — that is why it is in the prompt.
- **Do not bury it under the vocal.** It should be the highest non-vocal element in the choruses.
- **If it comes back anonymous, that is a real failure** — see §0 for the escalation.

### The bridge is stripped, flat, and quiet — by instruction

`bass, toms, rattling amp hum, steady level vocal`. Four elements, no pads, no lead, no build.

| Element | Treatment |
|---|---|
| Bass | Present, simple, no distortion increase |
| Toms | Present — the percussion texture, not a groove |
| Amp hum | Tape saturation + reverb bed |
| Vocal | **Steady level. No lift. Conversational.** |

**Do not add a rising pad, a lead line, or a filter sweep.** The emptiness is the joke of the section — he rehearses a new voice and delivers the old one.

Expect Suno to build here regardless. It is the most likely instruction in the document to be ignored.

### The intro is abrupt — same instruction as Are We Out of Time?

Full arrangement on beat one. `no guitar sustain` meant no wash across the opening; on the synth rebuild that translates to **no pad swell, no reverb bloom, nothing atmospheric.**

### Chorus ladder — biggest first

| Pass | Position | Arrangement |
|---|---|---|
| 1 | After pre-chorus 1 | **The fullest.** Doubled closing tag, `Get away and leave me` twice. This is the peak of the song. |
| 2 | After pre-chorus 2 | Full, but the tag lands once. Narrower than pass 1. |
| 3 (`[Final Chorus]`) | End | Full, tag once, then cut. No expansion, no final ad-lib. |

**This is a descending shape.** Most songs build to a final chorus; this one opens at maximum and closes tighter. That is a deliberate written choice and the arrangement must respect it — **do not add a lift to the final chorus.**

### Ending

No `[Outro]`, no `[End]` tag. The last line is `Get away and leave me`. **Cut dead on it.** A fade is excluded; a ring-out is excluded.

---

## 6. Creative sliders

**Mode:** Custom, no audio upload. Values held at series standard.

| Control | Value | Mode | Reasoning |
|---|---|---|---|
| **Weirdness** | **30%** | Custom | The failure mode is an anonymous lead, and anonymity is a prompt/spec problem, not a variance problem. Low weirdness keeps it diagnosable. |
| **Style Influence** | **75%** | Custom | The anti-victory block, the EBM block, and the bridge-crescendo guard all have to hold. This song has the most specific exclusions in the series. |
| **Audio Influence** | **n/a — slider absent** | Custom (no upload) | Cover-mode value if the approved demo is used as reference: **65%**. This is the one song where an audio reference would be genuinely worth it — the approved demo exists. |
| **Variety** | **Off (0)** | Custom | Would rewrite the style prompt server-side and strip the bridge guard and the victory block. |

**Max Mode: ON.** **Personalize: off.**

**Retry ladder:**

- Anonymous / generic lead → **the primary failure.** Re-roll before touching sliders; if it persists across three takes, escalate per §0 (this is where the guitar-part question gets asked).
- Bridge builds → the `bridge crescendo` guard failed; check the exclusion is present, re-roll.
- Reads as a club/EBM record at 148 BPM → Style Influence 85%.
- Guitar tone bleeds through → Style Influence 85%.
- Screamed or harsh vocal → re-roll, do not accept.
- Sounds victorious → check for `triumphant`/`stadium` slipping in.

---

## 7. Tempo, key, meter

### Tempo — documented

**148 BPM, written in the style notes.** Not inferred, and **not a copy of Take Me Back?'s 148** — both songs genuinely carry that figure independently. Carried verbatim.

This is the fastest documented tempo in the series alongside Under My Skin (147) and Take Me Back? (148).

### Key — quality documented, name not

`predominantly minor key` is in the style notes. **Which key is not recorded.** Note the qualifier: *predominantly* implies modal mixture within a minor-key frame, not a single fixed key.

The prompt carries `predominantly minor key` exactly, and excludes `major-key resolve` and `key change up`. **No key name is written.** Frontmatter records the key as UNVERIFIED with a separate documented `key_quality`.

### Meter — undocumented

No time signature anywhere. **Not inferred.**

---

## 8. Suno role verification + compatibility checklist

**Suno-assist (PRD §5.4). `master_source = studio`.** Status `final` with an **approved Suno demo** — but per the role matrix the demo is not the master. Studio capture/mix/master governs. This render is an arrangement reference, not a release master and not a replacement for the approved demo.

Low and deep baritone carried; `steady-level bridge vocal` carried; `female vocal` and `tenor vocal` excluded; `polished, mastered, final` excluded.

| # | Check | Result |
|---|---|---|
| 1 | Style prompt present | PASS |
| 2 | Lyrics verbatim from vault | PASS — every sung word byte-identical, including `til`, the missing comma, and the full stop |
| 3 | Section labels per spec | **PASS WITH FLAG** — 7 labels normalised; all embedded directions extracted and mapped in §4b |
| 4 | Labels Title Case | PASS |
| 5 | Line breaks per spec | PASS |
| 6 | Title field present | **PASS WITH FLAG** — question mark present in filename, H1 and lyrics. **Not ruled on** for DistroKid metadata |
| 7 | Negative prompt present | PASS |
| 8 | Suno role verdict | PASS — Suno-assist |
| 9 | Out-of-vocabulary tags flagged | **PASS WITH FLAGS** — `steady-level bridge vocal`, `distinctive lead synth hook`, `quietly relieved and slightly unnerved` as non-standard style vocabulary |
| 10 | Per-artist structure | PASS — Velvut |
| 11 | Key and time signature as explicit fields | **PARTIAL — tempo DOCUMENTED (148), key quality DOCUMENTED (predominantly minor), key name and meter UNVERIFIED** |
| 12 | All four sliders specified | PASS |

**Overall: PASS WITH FLAGS.** The lyric provenance is the strongest in the series (final, Principal-authored spine); the open items are the title question mark and the anonymous-lead risk.

---

## 9. Audition notes

1. **The lead test — the primary judgement call.** The approved demo's selling point was a unique guitar riff. If the synth lead is anonymous, the conversion has failed the one thing the Principal already liked. Everything else is secondary.
2. **Bridge test.** Flat, stripped, no build. If the vocal lifts or a pad swells, `steady level vocal` was ignored — likely, so note it rather than fixing it in post.
3. **Shape test.** Chorus 1 should be the biggest, not the last one. If the final chorus is the peak, the descending shape was flattened.
4. **Tempo.** 148 documented. Fast and forward-moving. If it drags, darkwave defaults are the cause — not the input value.
5. **EBM test.** Should read as a rock song with machines, not as a club record. If four-on-the-floor dominates, Style Influence 85%.
6. **Vocal.** Low and deep, singing. Any scream or harsh tone is an instant reject.
7. **Ending.** Hard cut on `Get away and leave me`. No fade, no ring-out.
8. **The garbled line.** `The silence moved in calls it home` — if Suno smooths it into something grammatical, that is a lyric change and it is wrong.

---

## 10. Lineage

- Song facts, lyrics, authorship note, approved-demo record: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/whos-calling-me.md` (read direct 2026-10-30, **status: final**)
- Vocal range and artist identity: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/artist-facts.md`
- Tempo sibling (148 BPM, independently documented): `docs/2026-10-30-take-me-back-velvut-synth-conversion-suno-prompt.md`
- Speed sibling (147 BPM): `docs/2026-10-30-under-my-skin-velvut-synth-conversion-suno-prompt.md`
- Series reference: `docs/2026-10-30-sad-song-velvut-synth-conversion-suno-prompt.md`
- Prompt spec: `.a0proj/skills/suno-prompt-compatibility-spec/SKILL.md`
- Role matrix: `.a0proj/skills/suno-integration/SKILL.md` (PRD §5.4)
- DAW guide: `docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md`
