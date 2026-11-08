---
last_updated: 2026-11-01T14:17:41
status: delivered
artist: Velvut
song: Bad
series_position: 4
route: suno-synth-re-render
tempo: 146
key: A major
time_signature: UNVERIFIED — not documented
vocal_range: F2-D4
suno_role: assist
direction_status: approved
master_source: studio
---

# BAD (Velvut) — Synth Conversion Suno Prompt Set

**Artist:** Velvut · **Song:** Bad · **Date:** 2026-10-30 · **Series:** song 4
**Route:** Suno synth re-render (reference only) · **Purpose:** direction reference for the GarageBand rebuild

---

## 0. Tempo gap — read first

**No BPM, no specific key, no time signature documented.** Nothing invented; nothing imported from Sad Song (151) or Hate Me (148).

This song is the least tolerant of a slow landing in the series — eight passes of a three-line hook at a dragged tempo does not sound bold, it sounds stuck.

---

## 1. Verified song facts

Source: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/bad.md` (read direct 2026-10-30, last_updated 2026-08-18).

| Field | Value |
|---|---|
| Tempo | UNVERIFIED — not documented |
| Key | UNVERIFIED — no specific key; file says 'minor key' only |
| Meter | UNVERIFIED — not documented |
| Vocal | Powerful baritone male, upfront |
| Style notes (verbatim) | nu-alt rock, alt-metal influences, minor key, powerful baritone vocal, upfront vocals, analog tape saturation, room reverb, wailing guitars, tight rhythm guitars, deep bass, full drum kit performance, explosive chorus lift |
| Exclusions (verbatim) | none recorded — series-standard applied |
| Structure | V1 → PC → C(x2) → V2 → PC → C(x2) → Bridge → C(x4). **Eight chorus passes total.** |
| Suno role | Suno-assist (PRD 5.4) — master_source = studio |

**Source-fidelity flags:** `neews` (Verse 2) is a typo for 'news' — **preserved verbatim, not fixed.** All parentheticals preserved. All labels canonical, no fallback needed.

---

## 2. Style prompt — paste into Style of Music

```
dark industrial synth-rock, darkwave, electro-industrial, alt-metal weight with no guitars, distorted synth bass, gated sequenced saw-bass pulses, detuned saw stack stabs, hard analog synth pads, aggressive mono-synth lead with portamento, metallic industrial percussion hits, programmed kick with weight, deep sub-bass, analog tape saturation, room reverb, parallel drum compression, quiet verses, wall-of-sound choruses, escalating chorus layers, each chorus pass adds a layer, call-and-response backing ad-libs, two-stage pre-chorus lift, powerful baritone male vocal upfront, gritty, explosive chorus lift, mantra repetition
```

No BPM, no key token — both omitted deliberately.

### Substitution map (inherited)

| Original role | Synth replacement |
|---|---|
| Tight rhythm guitars | distorted synth bass + gated sequenced saw-bass pulses |
| Wailing guitars | aggressive mono-synth lead with portamento |
| Alt-metal weight (power chords) | detuned saw stack stabs + hard analog synth pads |
| Full drum kit | metallic industrial percussion hits + programmed kick with weight |
| Deep bass | deep sub-bass, octave-doubled on final passes |

### Production textures

| Texture | Decision | Reason |
|---|---|---|
| Analog tape saturation | In, load-bearing | Only texture carried verbatim from source notes; makes stacked saws read aggressive rather than thin |
| Room reverb | In, on percussion and ad-libs only — **not** the lead vocal | Room on the vocal shortens presence, and presence is all that carries an 8-pass 3-line hook |
| Parallel compression | In, drum bus | Substituted kit has fewer transient sources; restores the weight chugging guitars supplied |

---

## 3. Exclude styles

**Core:**

```
tenor vocal, country, melodramatic, classic rock, electric guitar, acoustic guitar, rhythm guitar, lead guitar, power chords, palm-muted chugs, guitar solo, guitar amp, guitar sustain intro, wailing guitar, nu-metal guitar tone, synthwave, retro 80s, clean synth-pop, electro-pop, female vocal, polished, mastered, final
```

**Extended:**

```
dance-pop, chiptune, vaporwave, 8-bit, orchestral, symphonic, choir, pop production, clean production, bright, soft, ballad, sentimental, uplifting, handclaps, funk guitar, wah pedal, fretless bass, disco, spoken word intro, vocal chops
```

---

## 4. Title metadata

- **Title:** `Bad (Synth Conversion Reference)`
- **Fallback:** `Bad Synth Reference`

---

## 5. Creative sliders

**Mode:** Custom, no audio upload.

| Control | Value | Mode | Reasoning |
|---|---|---|---|
| **Weirdness** | **30%** | Custom | 3 lines x 8 passes — variance compounds, and one mutated pass in the final block is audibly wrong. If a pass mutates, drop to **20%**, never raise. |
| **Style Influence** | **75%** | Custom | Strongest guitar pull in the series — two named guitar parts plus alt-metal. 75% is the floor. |
| **Audio Influence** | **n/a — slider absent** | Custom (no upload) | Cover-mode if used later: **65%**. |
| **Variety** | **Off (0)** | Custom | Rewrites the prompt AND re-orders repeated lyric blocks — fatal at eight hook passes. |

**Max Mode: ON** (non-negotiable at this length/repetition). **Personalize: off.**

**Retry:** guitar → Style Influence 85%, then add `guitar-free` as first style tag. Mutated pass → Weirdness 20%. Chorus passes identical by pass 4 → Style Influence 85%. Tempo slow → no slider fixes it.

---

## 6. Lyrics field — verbatim from vault

```
[Verse 1]
The voicemail sat there hot
With your name still stuck on it
Dish in the sink, your keys gone cold
One more day I never fixed

The rent note on the door
Felt like a thumb in the bruise
I laughed too loud
I slammed the drawer
Then I blamed the whole damn room

[Pre-Chorus]
It's in my chest
It's in my teeth
It rides my tongue
It won't leave me

I try to breathe
I try to be good
Then it flips the table
Like it knew I would

[Chorus]
The things that make me mad
The things that make me sad
The things that make me bad
(so bad, so bad)

The things that make me mad
The things that make me sad
The things that make me bad
(you know, you know)

[Verse 2]
Your half-read text at noon
Your shoes by the hallway wall
The way I hold my own bad neews
Like I'm waiting on a call

The plate I threw to glass
The words I bit too fast
I wish I could split myself in two
One that heals
One to blast

[Pre-Chorus]
It's in my pulse
It's in my hands
A little spark
I don't understand

I try to stay
Soft at the core
Then that old hurt
Keeps kicking the door

[Chorus]
The things that make me mad
The things that make me sad
The things that make me bad
(so bad, so bad)

The things that make me mad
The things that make me sad
The things that make me bad
(you know, you know)

[Bridge]
Maybe I'm not a monster
Just a man with a broken past
Too many nights I swallowed it
Too many things I never said

So if I shake, don't laugh at me
If I flinch, don't walk away
I'm trying hard to hold the line
Before I turn it all to red

[Chorus]
The things that make me mad
The things that make me sad
The things that make me bad
(so bad, so bad)

The things that make me mad
The things that make me sad
The things that make me bad
(you know, you know)

The things that make me mad
The things that make me sad
The things that make me bad
(so bad, so bad)

The things that make me mad
The things that make me sad
The things that make me bad
(you know, you know)
```

Zero lyric text altered. `neews` stands. Parentheticals stand.

**How Suno will treat the parentheticals:** likely sung in-line by the lead (acceptable), possibly set as backing responses (better — makes the tag a structural event), possibly dropped (failure — retry with Style Influence up, never edit the lyric).

---

## 7. Arrangement — the eight-pass problem

The escalation must live in the **synth layer**, pass by pass, never in the vocal.

| Pass | Position | Synth treatment |
|---|---|---|
| 1 | after V1, first | Bare. Vocal + bass pulse + kick. No pad, no stabs. |
| 2 | after V1, second | Detuned saw stabs on the hook downbeat; ad-lib as backing response. |
| 3 | after V2, first | Hard analog pads full; mono-synth doubles the hook an octave up. |
| 4 | after V2, second | Metallic percussion layer; room send opens on hits only. |
| 5 | final block, first | **Drop the kick for the first two lines, re-enter on 'bad'.** Best fatigue-killer in the map. |
| 6 | final block, second | Saturation pushed; bass drops an octave. |
| 7 | final block, third | High-pass crawl on the bed — everything narrowed so pass 8 lands wide. |
| 8 | final block, fourth | Full band, filter open, dry stop on the last 'bad'. No fade. |

**Suno cannot follow a numbered map.** It responds to `escalating chorus layers` + `each chorus pass adds a layer`. **Passes 5 and 7 are yours to place by hand in GarageBand.**

**Two-stage pre-chorus.** Second quatrain is the lift: `It's in my chest / teeth / tongue` is restraint; `Then it flips the table` is the snap. Flat across all eight lines = lift failed, and an 8-line flat pre-chorus will outweigh a 3-line chorus.

**Bridge is the emotional turn.** `Maybe I'm not a monster` is the only self-forgiveness in a self-lacerating song. Must sound like the floor drops out: strip kick and saw stabs, vocal plus one sustained pad for the opening couplet, rebuild across `Too many nights I swallowed it`. Same bed as a verse = no turn, and the final four passes become noise.

**Verse 2 short-line cluster.** `One that heals / One to blast` need air after three long lines. Rebuild note, not a prompt fix.

---

## 8. Suno role verification

**Suno-assist (PRD 5.4). master_source = studio.** Reference render only. Baritone male descriptors carried; `female vocal` and `tenor vocal` excluded. Active paid tier required for any audio use beyond listening reference.

---

## 9. Compatibility checklist

| # | Check | Result |
|---|---|---|
| 1-10 | Standard spec checks | PASS |
| 3 | Section labels | PASS — all canonical, no fallback needed |
| 11 | Key and time signature as explicit fields | PASS with flag — both UNVERIFIED |
| 12 | All four sliders specified | PASS |

**Overall: PASS.**

---

## 10. Audition notes

1. **Pass-5 fatigue check, listen first.** Play the final chorus block and mark where attention drops. If it drops at pass 3 or 4, the escalation tags did not take.
2. **Parenthetical survival.** Can you hear them at all? Then classify: lead-sung (centre, same tail) or backing response (wider, quieter)? Absence is a fail.
3. **Two-stage pre-chorus.** Second quatrain must change dynamic — louder or emptier.
4. **Bridge departure.** If `Maybe I'm not a monster` is just another verse, fix in rebuild.
5. **Guitar bleed.** Strongest pull in the series — check 200-500 Hz, specifically for a palm-muted chug under the synth bass in verses.
6. **Weight transfer.** Sub-bass plus sequenced saw pulse.
7. **`neews`.** Note what was actually sung. Report, do not act.
8. **Ad-lib monotony.** Two tags, eight passes. If every pass delivers identically, the tags are part of the fatigue problem.
9. **Last pass.** Should be a dry stop, not a fade — rebuild instruction.

---

## 11. Lineage

- Song facts and lyrics: `/a0/usr/obsidian/05-wgnr-sounds/10-music/velvut/lyrics/bad.md`
- Series reference: `docs/2026-10-30-sad-song-velvut-synth-conversion-suno-prompt.md`
- Prompt spec: `.a0proj/skills/suno-prompt-compatibility-spec/SKILL.md`
- Role matrix: `.a0proj/skills/suno-integration/SKILL.md` (PRD 5.4)
