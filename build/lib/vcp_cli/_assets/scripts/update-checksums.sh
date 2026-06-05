#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
OUT="$ROOT/SHA256SUMS"

FILES=(
  "scripts/init-minimal.sh"
  "scripts/vibe-check.sh"
  "scripts/install-hooks.sh"
  "scripts/extract-prompt.sh"
)

if command -v sha256sum >/dev/null 2>&1; then
  HASH_CMD=(sha256sum)
elif command -v shasum >/dev/null 2>&1; then
  HASH_CMD=(shasum -a 256)
else
  echo "Neither sha256sum nor shasum is available." >&2
  exit 2
fi

cd "$ROOT"
: > "$OUT"
for file in "${FILES[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing file for checksum: $file" >&2
    exit 2
  fi
  "${HASH_CMD[@]}" "$file" >> "$OUT"
done

echo "Updated $OUT"
