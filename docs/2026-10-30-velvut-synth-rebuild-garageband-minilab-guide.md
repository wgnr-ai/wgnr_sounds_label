# Velvut Synth Rebuild — GarageBand + Arturia MiniLab 37

**Purpose:** DAW-side reference for rebuilding the Suno synth-conversion renders as human-recorded masters.
**Date:** 2026-10-30 · **Author:** WGNR Sounds Captain · **Principal:** Wagner dos Santos
**Companion docs:** `docs/2026-10-30-sad-song-velvut-synth-conversion-suno-prompt.md` and the per-song prompt sets.

> **Reading rule:** instrument names below are real and stable. **Preset names inside them are not specified** — GarageBand's Alchemy library and Arturia's Analog Lab library change between versions, and inventing a preset name is worse than none. Where it says *browse the category*, open the instrument and filter by the described character.

---

## 1. One-time setup (do this once, then never again)

1. **Connect the MiniLab 37** by USB before opening GarageBand. It is class-compliant — no driver needed.
2. GarageBand → **Settings → MIDI** → confirm the MiniLab appears as an input. Leave "MIDI input" on.
3. GarageBand → **Settings → Audio** → set the output device to your interface, buffer to **128 samples** for playing, **256** for mixing. Lower buffer = less latency = better for performance takes.
4. Create a **Software Instrument** track. That is the only track type you need for every synth part.
5. On the track, open **Smart Controls** (press `B`). This is your performance surface — it maps the MiniLab's encoders to the instrument automatically. Map what you use most to the first two encoders: **filter cutoff** and **filter resonance**.
6. **Save a project template** with the five tracks from §2 already created and named. Rebuilding the track stack by hand for every song is the single biggest time sink.

**MiniLab note:** the controller auto-maps to the focused instrument in most DAWs. If the encoders do nothing, click the instrument track first, then touch an encoder — it binds to whatever parameter is under the cursor in Smart Controls.

---

## 2. The five-layer Velvut stack

Every song in this series uses the same five layers. Build all five, then mute/solo per song.

| # | Layer | Role it replaced | GarageBand | Arturia | Range |
|---|---|---|---|---|---|
| 1 | **Sub bass** | deep bass guitar | Alchemy (bass category) or Retro Synth | **Mini V** | C1–C2 |
| 2 | **Saw bass pulse** | chugging rhythm guitar / palm mutes | Retro Synth (Analog) | **Jun-6 V** or **Jup-8 V** | C1–C2 |
| 3 | **Pads / stabs** | power chords | Alchemy (pads) | **Jup-8 V** or **Prophet V** | C3–C4 |
| 4 | **Mono lead** | wailing / octave lead guitar | Retro Synth (Mono) | **Mini V** or **ARP 2600 V** | C4–C5 |
| 5 | **Metallic percussion** | tom toms, kit weight | Drum Machine Designer | **CZ V** or **DX7 V** | C3–C5 |

---

## 3. Layer recipes

### Layer 1 — Sub bass

- **Waveform:** sine or triangle. Nothing brighter.
- **Filter:** low-pass at ~200 Hz, no resonance.
- **Envelope:** instant attack, fast decay, sustain off. It should be felt, not heard as a note.
- **Play:** root notes only, one octave below the saw bass. Hold through the bar.
- **Level:** the loudest thing in the low end. If you can't feel it in your chest at conversation volume, it's too quiet.

### Layer 2 — Saw bass pulse (the chug replacement)

This is the layer that carries the song. Get it right and everything else is decoration.

- **Waveform:** two or three detuned sawtooths, detune spread wide (roughly ±12–20 cents).
- **Filter:** low-pass around 400–800 Hz with **resonance at 25–40%**. The resonance is what gives it edge.
- **Envelope:** short attack (~5 ms), short decay (~120 ms), sustain ~40%, short release. **Staccato.** This is the palm-mute.
- **The gate:** in GarageBand, put a **Noise Gate** before the amp. Set threshold so it clips the tail, attack fast, release ~30 ms. That chop is the chug. Without the gate it sounds like a synth playing a bassline; with it, it sounds like a rhythm guitar.
- **Play:** straight eighth notes on the root. On the chorus, octave jumps on the last two eighths of the bar.

### Layer 3 — Pads and stabs (power chord replacement)

Two uses, one instrument:

**Pads (sustained):**
- Saw-based, slow attack (~300 ms), long release (~1.5 s), filter around 1.5–2.5 kHz.
- Detune wide. Wide detune = wall of sound. Narrow detune = thin.
- Verses: **pads off entirely.** They enter at the pre-chorus and stay for the chorus. This is what makes the chorus lift.

**Stabs (rhythmic):**
- Same patch, but attack instant, decay ~200 ms, release short.
- Play the chord on the downbeat only. One hit per bar. This is the power-chord replacement, and it should hit like a punch, not a wash.

### Layer 4 — Mono lead (the guitar solo / octave line)

- **Mono mode ON. Legato/glide ON, portamento ~60–120 ms.** The glide is non-negotiable — it is what makes a synth read as a *played* lead rather than a sequence.
- **Waveform:** single saw or square, filter ~2–3 kHz, resonance 20%.
- **Add movement:** map cutoff to the mod wheel. Ride it on sustained notes. A static lead sounds like a preset; a moving filter sounds like a player.
- **Play:** in the chorus, double the vocal melody an octave up. In the verse, leave it out — save it.

### Layer 5 — Metallic percussion

- **CZ V** (phase distortion) is the best tool for this — it makes glassy, metallic, clangy tones that no analog synth produces. **DX7 V** is the alternate (FM bell tones).
- **Play:** short hits on the backbeat with the main kick, and a single hit per bar in verses. Treat it as the tom fill replacement.
- **Pitch it:** tune hits to the key where you can. Untuned metal against a tuned bass is what makes industrial sound cheap.

---

## 4. Drums

Two routes. Pick per song.

**Route A — Drummer (fast, human-feeling)**
1. Add a Drummer track. Choose a **rock/alternative** character.
2. In the Drummer editor, set **Complexity low, Loudness high, Swing 0**. Turn *off* the fills — you want a machine-tight backbeat, not a session player showing off.
3. **Convert to MIDI:** right-click the region → *Convert to MIDI Region*. Now you can edit every hit and swap samples.

**Route B — Drum Machine Designer (full control, the industrial sound)**
1. Add a Drum Machine Designer track.
2. Load a sample per pad. **Layering is the whole trick:** every kick = an acoustic kick + a synthesized click on top. That click is what makes it cut through a saw-bass wall.
3. Snare: acoustic snare + a short noise burst, the noise ~6 dB under.

**Both routes:**
- **Kick:** deep and short. If it rings, it fights the sub bass. Cut everything below 40 Hz.
- **Verses:** half-time feel — kick on 1 and 3 only. This is the quiet-loud contrast; if the verse groove is busy, the chorus can't lift.
- **Chorus:** add a second kick layer an octave down, and open the hats.

---

## 5. The mix chain — the three textures that make it heavy

This is where the conversion lives or dies. A guitar-less arrangement loses weight unless you add it back deliberately.

### 5.1 Tape saturation (on the synth bus, not per-track)

- Route layers 1–4 to a **bus**, then put **Amp Designer or Pedalboard (tape/overdrive pedal, gain low)** on the bus.
- Drive it until you can *just* hear the grit — roughly 2–4 dB of gain reduction. Then back off 20%.
- **Why:** without it, stacked saw oscillators sound plastic and modern. Saturation is the difference between industrial and synth-pop. If a mix sounds clean and 2010s, this is the fix.

### 5.2 Parallel compression (on the drum bus) — the weight mechanism

1. Duplicate the drum bus to a second bus.
2. On the duplicate, insert **Compressor**, ratio 10:1, attack fast, release fast, threshold low — crush it hard, 15–20 dB of reduction.
3. Blend the crushed copy under the clean one at roughly **-18 to -12 dB**.
4. **Why:** a programmed kit has fewer transient sources than a real kit. This is what restores the weight that chugging guitars used to supply. Skip it and the chorus is loud but thin.

### 5.3 Reverb — deliberately restrained

- **Vocal:** short room or plate, ~0.4–0.8 s. The baritone must stay upfront and dry-ish. Long reverb on the vocal pushes it back and kills the presence the hook depends on.
- **Percussion:** a small room on the metallic hits so they have a space to live in.
- **Never:** hall reverb across the mix. It smears the low end into mud and turns industrial into goth-shoegaze.

### 5.4 Master bus

- **Channel EQ:** high-pass at 30 Hz. Cut 200–400 Hz by 1–2 dB if it's muddy. That is the guitar-corpse band — nothing there should be booming.
- **Compressor:** ratio 2:1, attack 20 ms, release auto, 2–3 dB reduction. Gentle.
- **Limiter:** last. Ceiling -1 dB.

---

## 6. Song quick-reference

Documented values only. `UNVERIFIED` means the vault does not contain it — do not guess, measure it off the original.

| Song | BPM | Key | Notes |
|---|---|---|---|
| Sad Song | **151** | **D minor** | Series reference song, Principal-approved |
| Hate Me | **148** | UNVERIFIED (minor only) | Gang vocals on the hook — unison, dry, 2–4 dB under lead |
| Take Me Back? | **148** | UNVERIFIED (minor only) | Written outro — four naked repeats, no fade |
| Who's Calling Me? | **148** | UNVERIFIED | — |
| Under My Skin | **147** | **C# minor** | — |
| These Phantom Walls | **92** | UNVERIFIED | Slow, no syncopation, wall-of-sound drone chords |
| Is This How It Ends? | 104–105 *(conflict)* | Am *(frontmatter)* | Key/tempo conflict unresolved — needs your ruling |
| Nothing To Me | UNVERIFIED | UNVERIFIED | — |
| Bad | UNVERIFIED | UNVERIFIED | Eight chorus passes — see pass map |
| Are We Out of Time? | UNVERIFIED | UNVERIFIED | — |
| Glass Horizon | UNVERIFIED | UNVERIFIED | Already has synth loops + industrial stomp — shortest hop |
| Feeling Alone | UNVERIFIED | UNVERIFIED | — |
| Maybe We'll Meet Again Someday | UNVERIFIED | TBD | Style notes not written |

**If a BPM is UNVERIFIED:** tap tempo against the original recording before you build anything. GarageBand has no tap-tempo, but you can set a region to loop and nudge the project tempo until the clicks align with the transients.

---

## 7. Troubleshooting — diagnose by symptom

| Symptom | Cause | Fix |
|---|---|---|
| **Thin chorus** | No parallel compression, or sub bass muted | Turn on §5.2. Check layer 1 is actually playing in the chorus. |
| **Sounds like synth-pop, not industrial** | Tape saturation missing or too clean | Add drive on the synth bus (§5.1). Cut above 8 kHz. |
| **Muddy, no punch** | Pads are in the verses, or too much 200–400 Hz | Mute pads until the pre-chorus. EQ-cut the guitar-corpse band (§5.4). |
| **Sounds cheap / video-game** | Metallic hits not tuned to the key | Pitch the layer-5 hits to the root (§3 layer 5). |
| **Lead sounds like a preset, not a player** | No portamento, no filter movement | Turn on glide, ride cutoff on the mod wheel (§3 layer 4). |
| **Chorus doesn't lift** | Verse groove too busy, or pads already playing | Half-time the verse kick (§4). Pads off in verse. |
| **Everything is loud but nothing hits** | Master compressor working too hard | Back it to 2 dB reduction. Fix the layers, not the master. |
| **Sounds sinister instead of sad** | Noise beds, detuned dissonance, long verb | Remove noise layers. Detune *wide* but never stack minor seconds. Short room verb only. |

---

## 8. Session order (the sequence that actually finishes songs)

1. **Set tempo and key** from §6. If UNVERIFIED, measure first — never build on a guess.
2. **Program drums** (Route A or B). Get the verse/chorus contrast right before anything else.
3. **Build layers 1 and 2** (sub + saw pulse). Play the whole song, verses and choruses. This is 60% of the sound.
4. **Add layer 3 pads**, chorus only. Listen to the lift.
5. **Add layer 5 metallic percussion.** The track should now feel finished without a lead.
6. **Add layer 4 lead** — chorus only.
7. **Record the vocal.** Do this before the mix. The vocal dictates what the synths should be doing.
8. **Mix chain** (§5). Then stop.

---

## 9. What this guide does not cover

- **Exact preset names.** Deliberate — the libraries vary by version and a wrong preset name wastes your time at the DAW. Browse by the character described.
- **Vocal recording chain.** Separate topic; the baritone is yours to record, and the Suno reference vocal is a placeholder, not a target.
- **Mastering.** Velvut masters route through Studio and DistroKid, not this document.

---

*Built 2026-10-30 alongside the Velvut synth-conversion series (Sad Song, Hate Me, Nothing To Me, Bad, Take Me Back?). Instrument families verified as stable product knowledge; preset-level specifics intentionally omitted.*
