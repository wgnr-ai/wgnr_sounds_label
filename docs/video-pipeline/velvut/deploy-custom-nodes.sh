#!/usr/bin/env bash
# =============================================================================
# deploy-custom-nodes.sh — Mac-side ComfyUI custom-node installer
# Velvut MIDI-driven audio-reactive pipeline (WGNR Sounds / Visual Production Layer)
# =============================================================================
# HOST:   Mac Studio M2 Ultra — ComfyUI CORE at /Users/wgnr/AI/comfyui/ComfyUI (NESTED —
#         verified on-host 2026-09-13 ~22:55 EDT; supersedes the flat-path assumption)
# SERVER: core server on *:8188 (PID observed 1663, 2026-09-13) — check queue BEFORE restart.
# RUN AS: operator on the Mac host — exec consent LIVE 2026-09-13 (A0 CLI, user wgnr).
# STATUS: DEPLOYED 2026-09-13 ~23:14 EDT (host exec consent live, user wgnr) —
#         4 packs cloned to the nested core custom_nodes; requirements via the core
#         venv (torch untouched at 2.11.0); server restarted via launchd
#         com.wgnr.comfyui; all 4 packs verified registered via /object_info
#         (incl. MIDILoader / MIDIFeatureExtractor / MIDIToAudio).
#
# WHAT IT INSTALLS (git clone into ${COMFY_DIR}/custom_nodes/):
#   1. ComfyUI-Advanced-ControlNet — precision movement anchors
#      https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet   (URL verified 2026-09-13)
#   2. ComfyUI_FizzNodes — wave functions / scheduled value frames
#      https://github.com/FizzleDorf/ComfyUI_FizzNodes              (URL verified 2026-09-13;
#       repo name uses an UNDERSCORE)
#   3. MIDI reader — RyanOnTheInside (PINNED DEFAULT, Principal-overridable):
#      Principal-overridable default, 2026-09-13, unanswered modal — auto-selected
#      per goal-mode autonomy. No standalone "ComfyUI-MIDI" repo exists (verified
#      2026-09-13, 4 web checks incl. exact-name); Jovimetrix MIDI READER rejected
#      (live device capture, NOT MIDI file loading). URL verified 2026-09-13 via
#      search-index listing:
#        https://github.com/ryanontheinside/ComfyUI_RyanOnTheInside
#      Override: export COMFYUI_MIDI_REPO=<url> before running.
#   3b. Audio-frame onset cross-verification — ComfyUI-AudioReactor (verified):
#        https://github.com/tocubed/ComfyUI-AudioReactor (public repo, verified
#        2026-09-13; Load Audio (from Path), Audio Frame, Shadertoy)
#      Distinct roles: RyanOnTheInside = MIDI note data (.mid parsing);
#      AudioReactor = audio-frame onset cross-verification of the beat map.
#      BOTH installed.
#
# IDEMPOTENT: safe to re-run. Already-installed repos are skipped (fast-forward
#             pulled only with UPDATE=1). No overwrites of foreign directories.
# CLOUD RULE: git clone from GitHub only. NO cloud video-generation services —
#             permanently out of scope (Principal direction 2026-09-06).
# =============================================================================
set -euo pipefail

COMFY_DIR="${COMFY_DIR:-/Users/wgnr/AI/comfyui/ComfyUI}"
CUSTOM_NODES="${COMFY_DIR}/custom_nodes"
UPDATE="${UPDATE:-0}"   # UPDATE=1 -> also fast-forward pull installed repos

mkdir -p "${CUSTOM_NODES}"

install_node () {
  local name="$1" url="$2"
  local dest="${CUSTOM_NODES}/${name}"
  if [ -d "${dest}/.git" ]; then
    if [ "${UPDATE}" = "1" ]; then
      echo "[update] ${name} -> git -C ${dest} pull --ff-only"
      git -C "${dest}" pull --ff-only
    else
      echo "[skip]   ${name} already installed (${dest})"
    fi
  elif [ -d "${dest}" ]; then
    echo "[warn]   ${dest} exists but is NOT a git checkout — inspect manually, no overwrite."
  else
    echo "[clone]  ${name} from ${url}"
    git clone "${url}" "${dest}"
  fi
}

# --- 1. Advanced-ControlNet (precision movement anchors) — URL verified 2026-09-13 ---
install_node "ComfyUI-Advanced-ControlNet" "https://github.com/Kosinkadink/ComfyUI-Advanced-ControlNet"

# --- 2. FizzNodes (wave functions / value-schedule frames) — URL verified 2026-09-13 --
install_node "ComfyUI_FizzNodes" "https://github.com/FizzleDorf/ComfyUI_FizzNodes"

# --- 3. MIDI reader — RyanOnTheInside (Principal-overridable default) ----------------
# Principal-overridable default, 2026-09-13, unanswered modal — auto-selected per
# goal-mode autonomy. Override: export COMFYUI_MIDI_REPO=<url> before running.
COMFYUI_MIDI_REPO="${COMFYUI_MIDI_REPO:-https://github.com/ryanontheinside/ComfyUI_RyanOnTheInside}"
install_node "ComfyUI_RyanOnTheInside" "${COMFYUI_MIDI_REPO}"

# --- 3b. ComfyUI-AudioReactor — URL VERIFIED 2026-09-13 (tocubed) --------------------
install_node "ComfyUI-AudioReactor" "https://github.com/tocubed/ComfyUI-AudioReactor"

# --- Post-install checklist ----------------------------------------------------------
echo
echo "Done cloning. Restart ComfyUI, then confirm node registration in the browser:"
echo "  [ ] Advanced-ControlNet nodes (movement anchors)"
echo "  [ ] FizzNodes: Value Schedule + float math nodes"
echo "  [ ] RyanOnTheInside MIDI nodes (.mid parsing — MIDI note data)"
echo "  [ ] AudioReactor nodes (audio-frame onset cross-verification)"
echo "  [ ] MPS probe state (PRD Open Question 4): HunyuanVideo 1.5 PRESENT; LTX-Video ABSENT"
echo "      -> set the video-model node in draft-workflow.json accordingly (swappable)."
echo
echo "Then follow midi-parse-graph-spec.md to wire the graph."