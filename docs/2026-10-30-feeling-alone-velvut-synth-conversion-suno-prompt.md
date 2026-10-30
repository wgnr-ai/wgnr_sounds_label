---
last_updated: 2026-10-30T17:44:00
status: delivered
artist: Velvut
song: Feeling Alone
series_position: 10
route: suno-synth-re-render
tempo: UNVERIFIED — not documented
key: UNVERIFIED — not documented
key_quality: minor — DOCUMENTED ('minor-key drive' in style notes)
time_signature: UNVERIFIED — not documented
vocal_range: F2-D4
suno_role: assist
direction_status: approved
master_source: studio
---

# FEELING ALONE (Velvut) — Synth Conversion Suno Prompt Set

**Artist:** Velvut · **Song:** Feeling Alone · **Date:** 2026-10-30 · **Series:** song 10
**Route:** Suno synth re-render (reference only) · **Purpose:** arrangement direction for the GarageBand rebuild

---

## 0. Two conflicts in the source file — read first

### Conflict 1: the style notes specify a pre-chorus that does not exist

The Style Notes document `halftime pre chorus`. The lyric has **no pre-chorus**. The structure is:

```
[Verse 1] → [Chorus] → [Verse 2] → [Chorus] → [Guitar Solo] → [Outro Chorus]
```

Six sections, no pre-chorus, no bridge. `Halftime pre chorus` is the most specific rhythmic instruction in this file and there is nowhere to put it.

**Three readings, and the one taken:**

| Reading | Plausibility |
|---|---|
| The note describes an earlier draft that had a pre-chorus | High |
| The note describes the **last two lines of Verse 2** as a halftime moment before the second chorus | Medium — those lines are the natural lift |
| The note is aspirational — for the rebuild to add one | Low; adding a section is arrangement, not conversion |

**Taken: reading 2.** Verse 2 ends on `So I don't feel alone` repeated twice — a genuine repeated lift. The halftime feel is applied there, as an arrangement instruction, not as a new section. **Nothing is added to the lyric.** If this is wrong, say so; it is the single most consequential judgement in this document.

### Conflict 2: `[Outro Chorus]` is not a canonical label

It is the song's final chorus under a non-standard name. The Principal's ruling on Maybe We'll Meet Again Someday (2026-10-30) was to normalise the non-canonical `[Chorus Climax]` to the canonical form.

**Applied here by the same precedent: `[Outro Chorus]` → `[Final Chorus]`.** This is a documented precedent, not a fresh guess — and it is trivially reversible if you want the vault's own label kept. Flagged rather than asked, because the last ruling settled the question.

### Everything else

| Field | Value | Status |
|---|---|---|
| Tempo | **UNVERIFIED — not documented** | Absence verified |
| Key | **UNVERIFIED — not documented** | Absence verified |
| Key quality | **minor — DOCUMENTED** (`minor-key drive`) | Documented |
| Meter | **UNVERIFIED — not documented** | Absence verified |
| Style notes | **DOCUMENTED — detailed** | See §2 |
| Exclusions | None recorded | Absence verified |

**The key-quality distinction matters:** `minor-key drive` tells us the song is in a minor key without telling us which one. The style prompt therefore carries `minor-key drive` — the documented phrase — and **not** a key name. Writing `A minor` or `D minor` would be invention.

---

## 1. Verified song facts

Source: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/feeling-alone.md` (read direct 2026-10-30, `last_updated: 2026-10-07T14:53:00`, `status: draft`).

| Field | Value |
|---|---|
| Title | **Feeling Alone** — no question mark |
| Album | `TBD` |
| Recording state | `draft` |
| Style notes (verbatim) | alt rock, nu metal, industrial rock, deep baritone male vocals, tight palm-muted guitars, wailing lead guitar, deep bass, full drum kit, analog tape saturation, room reverb, minor-key drive, explosive chorus lift, tension build, dynamic breakdowns, 90s alt metal, halftime pre chorus, layered vocal hook |
| Structure | V1 → C → V2 → C → Guitar Solo → Outro Chorus. **No pre-chorus, no bridge.** |
| Vocal | `deep baritone male vocals` — song-level, documented. Artist range F2–D4 |
| Inline directions | **One only:** `[two bars, melodic overdriven guitar solo, driving rhythm section]` |
| Suno role | Suno-assist (PRD §5.4) — `master_source = studio` |

### What the style notes give us

Four instrumental roles are documented guitar and must be converted: `tight palm-muted guitars`, `wailing lead guitar`, and by implication the power-chord bed. `deep bass` and `full drum kit` convert with almost no loss.

Two documented dynamics matter more than the instrumentation: **`explosive chorus lift`** and **`dynamic breakdowns`**. A five-line chorus repeated four times, one of them as the outro, is a song that lives or dies on whether those lifts are real.

---

## 2. Style prompt — paste into Style of Music

```
dark industrial synth-rock, electro-industrial, 90s alt-metal weight, minor-key drive, desperate, claustrophobic, unresolved, distorted synth bass, tight gated sequenced saw-bass pulses, detuned saw stack stabs, hard analog synth pads, aggressive mono-synth lead with portamento, wailing lead synth line, metallic industrial percussion hits, programmed kick with weight, halftime breakdown in verse two, quiet-loud dynamics, explosive chorus lift, wall-of-sound choruses, tension build, sub-bass weight, analog tape saturation, room reverb, deep baritone male vocal upfront, layered vocal hook, strained and urgent delivery, memorable chorus hook
```

### What changed from the series palette, and why

| Series default | This song | Reason |
|---|---|---|
| `bleak, exhausted, slow crush` | `desperate, claustrophobic, unresolved` | The lyric is not tired — it is trapped. `I don't know if I'll survive` is fear, not fatigue. |
| Static synth bass | `tight gated sequenced saw-bass pulses` | **`tight` is documented** and it is the right word for palm-muting: short, clipped, no sustain. |
| Sparse verses / wall choruses | `quiet-loud dynamics` + `halftime breakdown in verse two` | Both documented. The verse-2 halftime is the arrangement's one structural move. |
| Lead as doubling | `wailing lead synth line` | **`wailing` is documented.** Carried as an adjective — the role is converted, the character is kept. |
| — | `layered vocal hook` | **Documented.** The only song in the series with a session-level vocal-production note. |

### The `90s alt metal` trap

Documented, and it is this song's version of Glass Horizon's Y2K problem. Suno reads *90s alt metal* as a **guitar tone and a production era** — drop-tuned grunge, dry close-miked cabs, a specific mid-forward bite.

**The era words do not appear in the style prompt.** `90s alt-metal weight` carries the mass; `dark industrial synth-rock` and `electro-industrial` carry the production. The literal decade and genre are excluded in §3.

### The register judgement call — third variant in the series

Each song so far has had its own failure mode:

| Song | Failure mode |
|---|---|
| Is This How It Ends? | Triumph — a victory anthem about addiction |
| Maybe We'll Meet Again Someday | Sentimentality — a wedding song about regret |
| **Feeling Alone** | **Self-pity — a wallow** |

The lyric is unrelievedly bleak — hopeless, alone, defeat, `I don't know if I'll survive`. There is no turn, no resolution, no second perspective. Sung over a slow bed, that becomes a pity party.

The documented dynamic is the answer: **`explosive chorus lift`**. The song is not meant to be quiet. It is meant to be a person screaming that they are alone — which is the opposite of wallowing. The prompt holds `desperate` and `claustrophobic` and `explosive chorus lift` together so the weight has forward motion.

**Second risk, running the other way:** the chorus words are plain (`I'm on my own / Feeling alone`). Given enough lift and a big enough hook, Suno can make that sound **anthemic** — a crowd singing along about despair, which is a different failure. `triumphant`, `anthemic`, `stadium` are excluded.

### Vocal handling

`deep baritone male vocals` plus **`layered vocal hook`** — documented, and it means the chorus is doubled or stacked in the original. Carried as a style instruction. In practice that helps: a stacked baritone sits lower in the mix than a single exposed one.

F2 floor, no documented key, four choruses. Keep the chorus in the mid-baritone zone; there is no headroom information to plan against.

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
grunge, 90s, 1990s, alternative metal, nu-metal guitar tone, drop-tuned guitars, guitar feedback, numetal, rapcore, screaming vocals, harsh vocals, screaming, self-pity, maudlin, wallowing, miserable, dirge, funeral, slowcore, doom, anthemic, stadium rock, triumphant, victorious, uplifting chorus, hopeful ending, major-key resolve, key change up, fade out, fade ending, resolving outro, final chord resolve, ambient outro, spoken word
```

**Why each block exists:**

1. `grunge, 90s, 1990s, alternative metal, nu-metal guitar tone, drop-tuned guitars, guitar feedback` — the era trap from §2. Suno will otherwise deliver a 1996 guitar record with a synth pad on top.
2. `numetal, rapcore, screaming vocals, harsh vocals, screaming` — **the band is fronted by a baritone singer, not a shouter.** `nu metal` is documented in the style notes and is the single descriptor most likely to summon a screamed vocal or a rap verse. This song has neither.
3. `self-pity, maudlin, wallowing, miserable, dirge, funeral, slowcore, doom` — the wallow failure mode. A slow, miserable read of `I don't know if I'll survive` is a different and worse song than the documented one.
4. `anthemic, stadium rock, triumphant, victorious, uplifting chorus, hopeful ending` — the opposite failure. `Explosive chorus lift` means big, not victorious; the lyric never resolves.
5. `major-key resolve, key change up` — `minor-key drive` is documented. The song does not turn.
6. `fade out, fade ending, resolving outro, final chord resolve, ambient outro` — the Outro Chorus is the last section and it is a full chorus, not a tag. It should end on the chorus, hard.
7. `spoken word` — guards against Suno deciding the plain, repetitive chorus works better half-spoken.

---

## 4. Lyrics field

### 4a. Field-ready block — paste this into Suno

**All sung words byte-identical to the vault. One bracket removed** (the guitar-solo direction, mapped in §4b). One label normalised per the 2026-10-30 precedent.

```
[Verse 1]
These emotions in my mind
They take control of my life
Feeling hopeless all of the time
And I don't know if I'll survive

[Chorus]
I'm on my own
Searching for sins to atone
Feeling alone
With my feelings
Of hopelessness and defeat

[Verse 2]
God, please grant me strength
To become the person I was
To become the person I was
So I don't feel alone
So I don't feel alone

[Chorus]
I'm on my own
Searching for sins to atone
Feeling alone
With my feelings
Of hopelessness and defeat

[Instrumental Break]

[Final Chorus]
I'm on my own
Searching for sins to atone
Feeling alone
With my feelings
Of hopelessness and defeat
```

### 4b. What was changed, and where it went

| Vault element | Disposition |
|---|---|
| `[Guitar Solo]` | → `[Instrumental Break]`. No guitar exists; the mono-synth lead takes the solo role. |
| `[two bars, melodic overdriven guitar solo, driving rhythm section]` | → style prompt: `wailing lead synth line` + `aggressive mono-synth lead with portamento`. **Two bars** is carried in §5, not in the prompt — Suno cannot count bars. |
| `[Outro Chorus]` | → `[Final Chorus]` — canonical, per the 2026-10-30 precedent (see §0). |
| Everything else | **Byte-identical.** No sung word touched. |

### Structural flags — preserved as written

1. **Verse 2 repeats two lines, each exactly twice** — `To become the person I was` ×2, `So I don't feel alone` ×2. That is a written doubling, not a typo, and it is where the halftime feel lands (§5). Preserved exactly.
2. **No bridge.** Unique in the series so far. The song goes chorus → solo → final chorus, and the solo is the only thing between the last two choruses.
3. **The chorus never changes.** All four passes are byte-identical. There is no progression, no final variant, no withheld line. This is the opposite problem to Glass Horizon, where the third chorus was missing its shout.
4. **`With my feelings` is grammatically odd** — it is the one awkward line in the song. Preserved exactly; it may well be deliberate (a clinical, flat phrasing against the emotional content). Not a defect to fix.
5. **Straight apostrophes throughout** (`I'm`, `don't`, `I'll`). Preserved.

---

## 5. Arrangement notes

### Four identical choruses — the fatigue is the structure

There is no textual variation at all. The arrangement has to carry every distinction.

| Pass | Position | Arrangement |
|---|---|---|
| 1 | After verse 1 | Full stack but **not the biggest**. Establishes the hook. `Layered vocal hook` fully active. |
| 2 | After verse 2 | **The biggest.** This is the one the halftime lift launches. Everything after this is descent. |
| 3 | After instrumental break | Return, slightly reduced. The solo has spent the energy; this pass is the aftermath. |
| 4 (`[Final Chorus]`) | End | Full stack, no further build. **Ends the song.** No tag, no repeat, no ring-out. |

**Known limitation, as with every song in this series:** Suno cannot be told "pass 2 is loudest" without editing the lyrics field, and the field stays clean. The render will flatten them. Judge the palette, not the dynamics.

### The verse-2 halftime is the one real structural move

This is where `halftime pre chorus` is applied (see §0). Verse 2 runs five lines: two lines of prayer, then two doubled lines. The halftime lands on the **doubled lines** — `To become the person I was` ×2 and `So I don't feel alone` ×2 — so the repetition is heard as a stutter against a half-speed feel rather than as a plain repeat.

That is the moment the second chorus launches from. If it does not land, the second chorus has nothing to lift off.

### The break is two bars, and that is the whole solo

`[two bars, melodic overdriven guitar solo, driving rhythm section]` — the duration is documented and it is short. Two bars is a turnaround, not a showcase.

**In the rebuild: two bars of mono-synth lead, melodic, over the full rhythm section (not a drum break).** The `driving rhythm section` note means the band keeps moving underneath. Do not drop to drums-only; that is a different and much longer gesture.

### Ending

`[Final Chorus]` is the last section. The last line is `Of hopelessness and defeat` — the song ends on the word *defeat*.

**End hard, on that word.** A fade is a fail (excluded). A ring-out is a fail. Do not resolve.

---

## 6. Creative sliders

**Mode:** Custom, no audio upload. Held at validated series values.

| Control | Value | Mode | Reasoning |
|---|---|---|---|
| **Weirdness** | **30%** | Custom | Two opposite failure modes (wallow and anthem) mean diagnosis matters more than range. Low weirdness makes a wrong register a readable prompt fault. |
| **Style Influence** | **75%** | Custom | The era block and the anti-wallow block both have to hold hard. Seven exclusions exist purely to stop this becoming a 1996 guitar record. |
| **Audio Influence** | **n/a — slider absent** | Custom (no upload) | Cover-mode value if the demo is used as reference later: **65%**. |
| **Variety** | **Off (0)** | Custom | Would rewrite the style prompt server-side and strip the anti-wallow and era blocks — the two that keep this song from being either miserable or nostalgic. |

**Max Mode: ON.** **Personalize: off.**

**Retry ladder:**

- Slow / dirge / miserable read → check for a `doom`, `slowcore`, or `ballad` tag slipping in; re-roll before touching sliders.
- Screamed or harsh vocal → `screaming vocals` ban not holding at this descriptor density. Re-roll; do not accept the take.
- Grunge guitar tone → Style Influence 85%.
- Anthemic / crowd-singalong chorus → `anthemic` and `triumphant` are both excluded; if it still reads victorious, drop `explosive chorus lift` from the prompt and re-roll.
- No halftime in verse 2 → Weirdness 20%.

---

## 7. Tempo, key, meter — the gap

**No BPM, no specific key, no meter.** No frontmatter field, no prose value, no detector reading.

**What the file does give, without a number:**

- **`minor-key drive`** — the song is in a minor key. Which one is not recorded. The prompt carries the phrase, never a key name.
- **`halftime pre chorus`** — an explicit statement that a halftime feel exists somewhere in the song. Half of an unknown tempo is still unknown, and this does not narrow the range.
- **`tension build`, `dynamic breakdowns`, `explosive chorus lift`** — three dynamic instructions. none of which fixes a tempo.

**This is the least tempo-constrained song in the series.** Glass Horizon's `dance-floor stomp` and Is This How It Ends?'s measured 107 at least point at a feel. This file points at dynamics only, and dynamics are tempo-agnostic — the same arrangement works at 80 or at 140.

**What this means for the render:** Suno chooses, and it has almost nothing constraining it. Unlike the other gap songs, do not expect the descriptor density to land it close. This is the render most likely to come back at a tempo the Principal rejects on first listen, and **that would not be a prompt defect** — it would be the missing measurement showing up.

**Before the GarageBand rebuild:** measure the demo's BPM, key, and meter. This song joins Maybe We'll Meet Again Someday and Glass Horizon as the three weakest anchors in the series.

---

## 8. Suno role verification + compatibility checklist

**Suno-assist (PRD §5.4). `master_source = studio`.** `status: draft`, no recording referenced. Arrangement reference for a song not yet recorded. Not a release master, not a demo replacement.

Baritone male descriptors carried (`deep baritone male vocals`, `layered vocal hook`). `female vocal` and `tenor vocal` excluded. `polished, mastered, final` excluded.

| # | Check | Result |
|---|---|---|
| 1 | Style prompt present | PASS |
| 2 | Lyrics verbatim from vault | PASS — every sung word byte-identical; one bracket removed (§4b) |
| 3 | Section labels per spec | **PASS WITH FLAG** — `[Guitar Solo]`→`[Instrumental Break]`, `[Outro Chorus]`→`[Final Chorus]` (precedent applied, reversible) |
| 4 | Labels Title Case | PASS |
| 5 | Line breaks per spec | PASS |
| 6 | Title field present | PASS — no question mark |
| 7 | Negative prompt present | PASS |
| 8 | Suno role verdict | PASS — Suno-assist |
| 9 | Out-of-vocabulary tags flagged | **PASS WITH FLAGS** — `90s alt-metal weight`, `halftime breakdown`, `wailing lead synth line` as non-standard style vocabulary |
| 10 | Per-artist structure | PASS — Velvut |
| 11 | Key and time signature as explicit fields | **FAIL — both UNVERIFIED, not documented.** Key *quality* (minor) is documented and recorded separately; no key name exists |
| 12 | All four sliders specified | PASS |

**Overall: PASS WITH FLAGS.** Check 11 fails on this file by design — no key name, no meter.

---

## 9. Audition notes

1. **Wallow test.** If it sounds like a man feeling sorry for himself, it has failed. Listen for: a slow tempo with no forward motion, a sparse chorus, a sustained pad under the hook. The chorus should feel like pressure escaping, not like sighing.
2. **Anthem test — the opposite failure.** If the chorus sounds like a stadium singalong about depression, that is also a fail. The lift is weight, not victory.
3. **Verse 2 halftime.** The doubled lines should stutter against a half-speed feel. If verse 2 is a straight continuation of verse 1, the only structural move in the song did not happen.
4. **Vocal.** Deep baritone, layered on the hook, singing — not shouted, not rapped. Any scream is an instant reject.
5. **The break.** Two bars, melodic lead, full rhythm section underneath. If it is a drum solo, or four bars, or a full section, it is wrong.
6. **Chorus fatigue.** All four are identical words. Expect flattening; judge palette and register.
7. **Ending.** Hard stop on `defeat`. A fade, a ring-out, or a resolve is a fail.
8. **Tempo.** Unknown, and uniquely unconstrained by this file. Judge whether it moves. Do not compare against a number — there is no number, and this is the render most likely to need a re-roll on tempo alone.

---

## 10. Lineage

- Song facts, lyrics, and inline direction: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/feeling-alone.md` (read direct 2026-10-30)
- Vocal range and artist identity: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/artist-facts.md`
- Label-normalisation precedent: `docs/2026-10-30-maybe-meet-someday-velvut-synth-conversion-suno-prompt.md` (Principal ruling 2026-10-30)
- Series reference: `docs/2026-10-30-sad-song-velvut-synth-conversion-suno-prompt.md`
- Structure and slider semantics: `docs/2026-10-30-is-this-how-it-ends-velvut-synth-conversion-suno-prompt.md`
- Prompt spec: `.a0proj/skills/suno-prompt-compatibility-spec/SKILL.md`
- Role matrix: `.a0proj/skills/suno-integration/SKILL.md` (PRD §5.4)
- DAW guide: `docs/2026-10-30-velvut-synth-rebuild-garageband-minilab-guide.md`
