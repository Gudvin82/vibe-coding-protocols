#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET_DIR="${PWD}"

choices=(
  "starter:templates/AGENTS.md templates/PROJECT_MAP.md templates/PROMPTS.md"
  "hardening:templates/AUDIT_BACKLOG.md templates/SECURITY_SCANNER_REPORT.md"
  "architecture:templates/ARCHITECTURE_SOURCE_OF_TRUTH.md"
)

echo "Review-first init helper."
echo "This example does not overwrite files automatically."
echo

echo "Available packs:"
for entry in "${choices[@]}"; do
  printf ' - %s\n' "$entry"
done

echo
read -r -p "Choose pack name (starter/hardening/architecture): " pack

selected=""
for entry in "${choices[@]}"; do
  name="${entry%%:*}"
  if [[ "$name" == "$pack" ]]; then
    selected="${entry#*:}"
    break
  fi
done

if [[ -z "$selected" ]]; then
  echo "Unknown pack. Exiting without changes."
  exit 1
fi

echo "Files to copy into: $TARGET_DIR"
for file in $selected; do
  echo " - $file -> $(basename "$file")"
done

echo
read -r -p "Proceed with copy? [y/N]: " confirm
if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
  echo "Cancelled."
  exit 0
fi

for file in $selected; do
  src="$ROOT/$file"
  dst="$TARGET_DIR/$(basename "$file")"
  if [[ -e "$dst" ]]; then
    echo "Skip existing file: $dst"
    continue
  fi
  cp "$src" "$dst"
  echo "Copied: $dst"
done
