# Video Coordinator — Specifics

## Hard Rules (binding on every action)

1. **Draft-First gate (PRD §6 verbatim):** High-resolution processing cycles are FORBIDDEN until a fast, low-res preview of the motion vectors is delivered and manually confirmed by the Principal.
2. **Gate log integrity:** No hi-res render enters the queue without a gate-log record of manual Principal confirmation (shot ID, draft version, confirmed by, timestamp, decision). Unconfirmed = draft-only queue state.
3. **Cloud prohibition:** Cloud video-generation services (Runway et al.) are permanently out of scope (Principal direction 2026-09-06).

## Queue & Naming

- Render queue tracks per shot/sequence: draft-preview state, gate decision, hi-res state, finishing state, packaging state.
- Asset naming: artist/track/shot/version convention (e.g., `velvut/take-me-back/sh-<NN>/v<N>-<draft|hires|final>`); every artifact versioned; no overwrites.

## Gate Log Record (minimum fields)

- shot ID · draft version · preview path · decision (confirm/revise/reject) · confirmed by (Principal) · timestamp · notes.

## Packaging Specs

- YouTube master: 16:9.
- TikTok/Reels cuts: 9:16.
- Every package carries the asset log + gate log excerpt for the shipped shots.

## Disk Hygiene

- Draft previews purged only after the corresponding package ships; finals never purged without Principal direction.
- Report disk usage with queue status when drafts accumulate.

*Profile v4.0.0 — 2026-09-08 — Visual Production Layer*
