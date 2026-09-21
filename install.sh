#!/usr/bin/env bash
# SPDX-License-Identifier: CC-BY-NC-SA-4.0
# ==============================================================================
# Script Name: install.sh
# Description: Installs the "Windows 7 Enhanced" icon theme for the current
#              user into:
#                  ${XDG_DATA_HOME:-$HOME/.local/share}/icons/windows-7-enhanced
#
#              No username is hardcoded: the destination is resolved from the
#              environment, so it works for any user.
#
# Theme       : Windows 7 Enhanced (icons)
# Original    : "Plasma SVG Win7 Theme" by Blackcrack (Blackysgate.de)
# Enhanced by : Leon Khoo
#
# Usage:
#   ./install.sh              install / update the icon theme
#   ./install.sh --uninstall  remove it
#   ./install.sh --help
# ==============================================================================

set -euo pipefail

THEME_ID="windows-7-enhanced"
SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
DATA_HOME="${XDG_DATA_HOME:-$HOME/.local/share}"
ICON_BASE="${DATA_HOME}/icons"
TARGET_DIR="${ICON_BASE}/${THEME_ID}"

info() { printf '\033[1;34m==>\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33mwarning:\033[0m %s\n' "$*" >&2; }
die()  { printf '\033[1;31merror:\033[0m %s\n' "$*" >&2; exit 1; }

usage() {
    cat <<EOF
Installs the "Windows 7 Enhanced" icon theme for the current user.

Usage:
  $(basename "${BASH_SOURCE[0]}")              install / update
  $(basename "${BASH_SOURCE[0]}") --uninstall  remove
  $(basename "${BASH_SOURCE[0]}") --help       show this help

Destination: \${XDG_DATA_HOME:-\$HOME/.local/share}/icons/${THEME_ID}
EOF
}

refresh_caches() {
    command -v gtk-update-icon-cache >/dev/null 2>&1 \
        && gtk-update-icon-cache -q -t -f "${TARGET_DIR}" 2>/dev/null || true
    command -v xdg-icon-resource >/dev/null 2>&1 && xdg-icon-resource forceupdate 2>/dev/null || true
    if command -v kbuildsycoca6 >/dev/null 2>&1; then
        kbuildsycoca6 --noincremental >/dev/null 2>&1 || true
    elif command -v kbuildsycoca5 >/dev/null 2>&1; then
        kbuildsycoca5 --noincremental >/dev/null 2>&1 || true
    fi
}

install_theme() {
    [ -f "${SCRIPT_DIR}/${THEME_ID}/index.theme" ] \
        || die "Run this script from the root of the windows-7-enhanced-icons repo."

    info "Source      : ${SCRIPT_DIR}"
    info "Destination : ${TARGET_DIR}"

    rm -rf -- "${TARGET_DIR}"
    mkdir -p -- "${TARGET_DIR}"
    tar -C "${SCRIPT_DIR}/${THEME_ID}" -cf - . | tar -C "${TARGET_DIR}" -xf -

    refresh_caches
    echo
    info "Installed successfully. Select it in System Settings -> Appearance -> Icons."
}

uninstall_theme() {
    if [ -d "${TARGET_DIR}" ]; then
        info "Removing ${TARGET_DIR}"
        rm -rf -- "${TARGET_DIR}"
        refresh_caches
        info "Uninstalled."
    else
        warn "Icon theme is not installed at ${TARGET_DIR}."
    fi
}

main() {
    case "${1:-}" in
        --uninstall|-u) uninstall_theme ;;
        --help|-h)      usage ;;
        "")             install_theme ;;
        *)              die "Unknown option: $1 (use --help)" ;;
    esac
}

main "$@"
