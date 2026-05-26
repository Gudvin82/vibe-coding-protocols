#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

required_files=(
  README.md
  LICENSE
  DISCLAIMER.md
  CHANGELOG.md
  CLAUDE.md
  AGENTS.md
)

required_dirs=(
  protocols
  prompts
  templates
  agents
  examples
  checklists
  docs
  scripts
  .github/workflows
)

for file in "${required_files[@]}"; do
  [[ -f "$file" ]] || { echo "Missing required file: $file"; exit 1; }
done

for dir in "${required_dirs[@]}"; do
  [[ -d "$dir" ]] || { echo "Missing required directory: $dir"; exit 1; }
done

empty_md=$(find . -type f -name '*.md' -size 0 | sed 's#^./##')
if [[ -n "$empty_md" ]]; then
  echo "Empty markdown files found:"
  echo "$empty_md"
  exit 1
fi

echo "Toolkit structure check passed."
