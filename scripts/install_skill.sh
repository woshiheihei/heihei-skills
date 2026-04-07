#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE_DIR="$ROOT_DIR/skills/x-thread-context-capture"
TARGET_BASE="${CODEX_HOME:-$HOME/.codex}/skills"
TARGET_DIR="$TARGET_BASE/x-thread-context-capture"

if [[ ! -d "$SOURCE_DIR" ]]; then
  echo "Source skill not found: $SOURCE_DIR" >&2
  exit 1
fi

mkdir -p "$TARGET_BASE"
rm -rf "$TARGET_DIR"
cp -R "$SOURCE_DIR" "$TARGET_DIR"

echo "Installed x-thread-context-capture to:"
echo "  $TARGET_DIR"
