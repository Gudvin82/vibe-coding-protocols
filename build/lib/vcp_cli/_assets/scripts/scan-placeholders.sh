#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "This is a lightweight placeholder scan, not a security scan."

matches=$(rg -n --glob '!*.git/*' --glob '!scripts/LICENSE-MIT' --glob '!scripts/scan-placeholders.sh' '(API_KEY=|TOKEN=|PASSWORD=|DATABASE_URL=)' . || true)

if [[ -z "$matches" ]]; then
  echo "No secret-like assignment patterns found."
  exit 0
fi

allowed=$(printf '%s\n' "$matches" | rg '\[masked-example-not-real\]|\[example-placeholder\]' || true)
blocked=$(printf '%s\n' "$matches" | rg -v '\[masked-example-not-real\]|\[example-placeholder\]' || true)

if [[ -n "$blocked" ]]; then
  echo "Potentially unsafe placeholder patterns found:"
  printf '%s\n' "$blocked"
  exit 1
fi

echo "Only explicit example placeholders were found:"
printf '%s\n' "$allowed"
