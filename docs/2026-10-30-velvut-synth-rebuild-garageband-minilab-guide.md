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

### 4.1 The three-layer drum stack

A single kit will not carry this music. Build three software-instrument layers and split the pattern across them. **Browse by character — no preset names**, same rule as the rest of this guide.

| Layer | Role | Where to look in GarageBand | Production goal |
|---|---|---|---|
| **Foundation (acoustic)** | the kit you hear | Drum Kit — a heavy or roomy rock kit | Natural cymbal wash, snare crack, room ambience. This is what makes it sound like a drummer. |
| **Punch (electronic)** | attack and consistency | Electronic Drum Kit — an 80s or underground-machine character | Layered under the acoustic kick and snare. Gives the mechanical consistency the acoustic kit lacks. |
| **The machine (lo-fi)** | movement | A sequencer or arpeggiator patch, pitched down | Low volume, deliberately distorted, running continuously underneath. This is the industrial clock — you should feel it more than hear it. |

**Balance:** the machine layer sits roughly **12–18 dB under** the acoustic foundation. If you can pick it out on first listen it is too loud; if muting it changes nothing, it is too quiet.

---

### 4.2 Quantization and groove — the verse/chorus engine

This is the mechanism behind the quiet-verse / wall-of-sound-chorus contrast in §8. **Split quantization strength by layer type — do not quantize the whole kit the same way.**

**Electronic layers:** quantize hard to a **1/16 grid at 100% strength**. No swing, no humanize. This is what makes the machine layer read as a machine, and it is the rhythmic signature of the style.

**Acoustic layer:** back the quantization off to **70–80% strength**, or slide the snare hits a few milliseconds *behind* the grid line. The relaxed, slightly-late snare is what gives the groove its weight — the bounce that makes a heavy chorus feel like it lands rather than attacks.

**Why the split works:** the acoustic layer carries the human feel and the electronic layer carries the precision. Quantize both hard and the track sounds like a demo; quantize neither and the machine layer stops being mechanical.

**Per section:**
- **Verse** — keep the machine layer tight and the acoustic layer at the loose setting. Half-time kick (§4.4) on top.
- **Chorus** — tighten the acoustic layer toward 90%. The chorus should feel *more* machine-driven than the verse, not less.

---

### 4.3 Industrial processing — two cheap wins

**The bitcrushed snare.** Put GarageBand's stock **Bitcrusher** directly on the acoustic snare. Drop the resolution to **12-bit** and add a *small* amount of downsampling — enough to hear grit, not enough to hear a video game. This replicates late-90s hardware samplers without buying one. Keep it on the snare only; on the whole kit it becomes a lo-fi aesthetic instead of a texture.

**The sub-kick — with a mandatory sidechain.** An 808 or long-decay sub-kick under the chorus downbeats adds real weight. **But Layer 1 (sub bass) already owns everything below ~120 Hz.** Dropping an 808 in without ducking Layer 1 gives you two low-end sources fighting for the same headroom, and the limiter will pump.

Do it this way:
1. Put the sub-kick on the electronic drum layer, triggered on chorus downbeats only.
2. Sidechain Layer 1 to the sub-kick — duck Layer 1 by **2–3 dB** for the duration of the sub-kick decay.
3. Cut the sub-kick below **35 Hz**; it is a punch, not a rumble.

If you cannot sidechain, **do not use the sub-kick.** An unsidechained 808 costs you more (mud, pumping, lost headroom) than it adds.

---

### 4.4 Two kit routes (fast vs. full control)

Pick per song.

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

### 5.5 Vocal chain — the order that matters

The baritone has to survive a wall of saw bass and get through a limiter at -14 LUFS. Build the track effects panel in this exact top-to-bottom order; ordering is not cosmetic, it changes the result.

**1. Pitch correction — 50–70% strength**
Tighten the pitch *before* anything distorting. This is the one non-obvious ordering. Distortion on an already-slightly-flat note generates harsh artifacts that no EQ can remove; tightening first means the saturation only adds harmonics, never grind.
Do not chase an obvious auto-tune effect. Velvut's baritone should sound like a person, not a plugin.

**2. Channel EQ**
- High-pass at **100 Hz** — clears mic rumble and the low end the sub bass owns.
- Gentle wide boost **+3 dB at 3.5 kHz** — presence, intelligibility through the saw wall.
- **High shelf is conditional — see the warning below.**

**3. Compressor — threshold -24 dB, ratio 4:1, attack 15 ms, release 200 ms**
The point is to pin the vocal so a spoken verse and a full-voice chorus arrive at the same apparent level. Ratio 6:1 if the take is genuinely screamed. Enable auto-gain or make up the level manually.

**4. Distortion / saturation — drive 5–15%, mix ~30%**
Low drive only. This adds harmonic "hair" that lets the vocal slice through the synth bus without needing more level. It mimics a pushed console preamp. Above 15% drive it stops being texture and starts being an effect.

**5. Stereo delay — 1/8 left, 1/4 right, mix 10–15%**
This replaces reverb as the space-creator, and it is consistent with §5.3: reverb pushes a vocal back, a tightly-timed stereo delay makes it sound big while keeping it locked forward. Keep feedback low — this is depth, not an echo effect.

> **⚠ 10 kHz conflict — resolve it here or it doubles up.** The source material this section was adapted from boosts +3 dB at 10 kHz on the vocal *and* the master chain in §9.5 allows a further +1 to +1.5 dB high shelf. Stacking both puts up to +4.5 dB at 10 kHz on the finished master, which produces hiss on the cymbals and sibilance on the baritone.
>
> **Rule: pick one place for the air.** Either take +2 to +3 dB at 10 kHz on the vocal track and set the §9.5 master shelf to **zero**, or leave the vocal flat above 8 kHz and take the +1 to +1.5 dB at master. Do not do both.

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

## 9. Final mix and mastering — streaming-ready delivery

§5 gets the song heavy. This section gets it *finished*, and gets the file a DSP will accept without a rejection or a quiet-sounding master.

### 9.1 Final mix pass — five moves, in this order

1. **Gain stage the buses.** Peak every bus (drums, synth, vocal, FX) to roughly **-6 dBFS** before it hits the mix bus. Leave the master fader at unity. Mix with faders down, not the master up.
2. **Sub-bass discipline.** High-pass everything that is not the sub at **30 Hz**. Keep **everything below ~120 Hz mono** — a stereo sub is the single most common reason an industrial mix sounds flabby on a car system and disappears on a phone.
3. **The vocal wins.** If the vocal is competing, take 1–2 dB out of the synth bus at 1–3 kHz rather than boosting the vocal. Making room always beats adding level.
4. **Pull the mix-bus limiter off.** The limiter in §5.4 is a *safety catch* so you do not clip while you work. It is not a master. Bypass it before mixdown or you will master a mix that is already limited — that is how you get a master with no transients left.
5. **Reference check on three systems.** Studio monitors, one pair of consumer headphones, and a phone speaker. If the low end only exists on the monitors, it does not exist.

### 9.2 The stop condition — when the mix is actually done

Run this before you render the mixdown and again before you master. A mix that fails any of these is not finished, and mastering amplifies decisions rather than fixing them.

- The chorus lift is audible **on phone speakers**, not just monitors or headphones.
- The baritone is intelligible on every system without reading the lyric sheet.
- Nothing pumps when the kick and the sub hit together.
- The song survives a mono fold-down — no element disappears.
- You can hear the difference between verse and chorus with the volume at low level.

### 9.3 Mixdown settings

| Setting | Value | Why |
|---|---|---|
| Sample rate | **44.1 kHz** (or 48 kHz if the session is already there) | the distributor accepts either; do not upsample a 44.1 session to 48. |
| Bit depth | **24-bit** | Headroom for mastering. 16-bit at mixdown throws away resolution you cannot get back. |
| Dither | **Off** | Dither is applied once, at the very end, and only if the final delivery is 16-bit. |
| Master peak | **-6 dBFS** headroom | The mastering chain needs room to work. |
| Tail | **2 s minimum**, to natural decay | Truncated tails are the most common drop-in review failure. |

Render the mixdown **without** the master-bus limiter and **without** any master-bus compressor. Those belong to §9.5.

### 9.4 The Velvut mastering target

One master, all platforms. Do not cut per-DSP versions — every major service normalizes on playback, so a louder master is turned down and a quieter master is turned up. What survives normalization is **dynamic structure**, not level.

| Target | Value | Reason |
|---|---|---|
| Integrated loudness | **-14 LUFS** | The common normalization anchor across Spotify, YouTube Music, Amazon and Tidal. |
| True peak | **-1.0 dBTP** | Lossy encoding (AAC/Opus) overshoots. -1.0 dBTP prevents inter-sample clipping after encode. |
| Loudness range (LRA) | **6–10 LU** | Velvut is dynamic-by-genre. Below 6 LU the choruses stop lifting. |
| Max limiting | **3–4 dB** gain reduction | More than that and the sub-bass transients are gone. |

**Why not louder:** a -9 LUFS master is normalized back down to -14 and you keep the pumping for free. Loudness is not a competitive advantage on streaming — it is a tax on transients.

**Caveat:** platform normalization values are published targets and have changed before. Re-verify against current platform documentation at each release cycle rather than treating the table above as permanent.

### 9.5 Master chain — order matters

1. **Corrective EQ.** High-pass at **30 Hz**. Cut **200–400 Hz** by 1–2 dB if it is muddy — that is the guitar-corpse band from §5.4 and it must not be booming.
2. **Tonal EQ.** Gentle high shelf, **+1 to +1.5 dB at 10 kHz maximum**. Velvut wants *air*, not sizzle; if the cymbals start to hiss, you have gone too far.
3. **Bus glue compressor.** Ratio **2:1**, attack **20 ms**, release auto, **2–3 dB** reduction. This is the §5.4 compressor, now committed rather than auditioned.
4. **Saturation.** Tape or console character, **1–2 dB** of density, no more. The heavy lifting was done on the synth bus in §5.1 — this is the last 5%.
5. **Limiter, last.** Ceiling **-1.0 dBTP**. Watch the gain-reduction meter: stay under 4 dB. If you need more, fix the mix.
6. **Meter the result.** Integrated LUFS, true peak, and LRA — all three, not just peak.

GarageBand has no LUFS meter built in. Read loudness with an external meter on the master output rather than trusting the peak meter alone — peak level and perceived loudness are not the same thing.

### 9.6 The two failure modes specific to this style

**Limiter pumping on the sub.** Layer 1 and the kick arrive together and both want the same headroom. If the limiter is working hard, the whole mix breathes with the kick. Fix: automate the sub down 1–2 dB under the kick, do not raise the limiter ceiling.

**Mastered to the loudest moment.** The chorus is the loudest thing in the song, so it sets the ceiling — and the verses end up quiet after normalization. Master against the **chorus**, then check the verse is still present at low volume. If a slow track (92 BPM territory) needs it, accept a wider LRA rather than crushing the quiet sections up.

### 9.7 Delivery specs — the file that gets accepted

| Item | Required |
|---|---|
| Container | **WAV** (24-bit, 44.1 kHz) — the distributor's preferred input |
| Loudness | -14 LUFS integrated |
| True peak | **-1.0 dBTP** |
| Leading silence | **None** — trim to the first transient |
| Trailing silence | None beyond the natural decay; do not fade out a written ending |
| Channels | Stereo, phase-checked |
| Clipping | Zero samples over 0 dBFS |

### 9.8 RouteNote upload checklist

Before upload, confirm for each song:

- [ ] File is the **24-bit WAV master**, not the mixdown and not an MP3.
- [ ] Integrated loudness reads **-14 LUFS**, true peak **-1.0 dBTP**.
- [ ] **Title** matches the vault lyric file exactly, including any question mark — see the `Take Me Back?` ruling still open on the Velvut blockers list.
- [ ] **Key** and **time signature** entered only if documented. If the vault says `UNVERIFIED`, leave it out of the metadata — do not guess to fill the field.
- [ ] Artist name, ISRC assignment, and release date set in RouteNote.
- [ ] Master file archived to the Velvut masters folder, not left only on the working drive.

### 9.9 Pre-delivery QA — listen once more before it leaves

1. Full playthrough at **low volume** — this is where a bad master shows up first.
2. Full playthrough on **phone speaker** — the sub is gone; does the song still work?
3. **Mono fold-down** — no element vanishes, no phase cancellation on the synth bus.
4. **Loudness read after encode**, not just the WAV: a lossy pass can push true peak past -1.0 dBTP.
5. Confirm the file in RouteNote's player matches what you heard locally before submitting for review.

---

## 10. What this guide does not cover

- **Exact preset names.** Deliberate — the libraries vary by version and a wrong preset name wastes your time at the DAW. Browse by the character described.
- **Vocal recording chain.** Separate topic; the baritone is yours to record, and the Suno reference vocal is a placeholder, not a target.
- **Per-platform master variants.** One master serves all platforms (§9.4); do not cut DSP-specific versions. Velvut masters still route through Studio for sign-off and RouteNote for delivery (§9.8).

---

*Built 2026-10-30 alongside the Velvut synth-conversion series (Sad Song, Hate Me, Nothing To Me, Bad, Take Me Back?). Instrument families verified as stable product knowledge; preset-level specifics intentionally omitted.*
