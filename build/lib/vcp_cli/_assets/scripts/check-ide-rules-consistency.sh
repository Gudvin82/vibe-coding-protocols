#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

files=(
  AGENTS.md
  CLAUDE.md
  templates/AGENTS.md
  templates/AGENTS.claude.md
  .cursorrules
  .windsurfrules
  .github/copilot-instructions.md
)

phrases=(
  "Memory Bank"
  "token-aware"
  "evidence map"
  "Stop Conditions"
)

problems=0

for file in "${files[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing IDE rules file: $file"
    problems=$((problems + 1))
    continue
  fi

  for phrase in "${phrases[@]}"; do
    if ! grep -iF "$phrase" "$file" >/dev/null 2>&1; then
      echo "IDE rules drift in $file: missing phrase '$phrase'"
      problems=$((problems + 1))
    fi
  done
done

for file in \
  README.md \
  README_ru.md \
  START_HERE.md \
  docs/lite-adoption-path.md \
  prompts/use-this-repo-prompt.md \
  prompts/use-this-repo-prompt_ru.md \
  templates/README.md; do
  if [[ ! -f "$file" ]]; then
    echo "Missing onboarding file: $file"
    problems=$((problems + 1))
    continue
  fi

  if ! grep -F "root \`AGENTS.md\`" "$file" >/dev/null 2>&1 \
    || ! grep -F "templates/AGENTS.md" "$file" >/dev/null 2>&1; then
    echo "Onboarding wording drift in $file: missing root/template AGENTS clarification"
    problems=$((problems + 1))
  fi
done

if (( problems > 0 )); then
  exit 1
fi

echo "IDE rules consistency check passed."
