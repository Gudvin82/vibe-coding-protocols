#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

required_files=(
  README.md
  README_en.md
  README_ru.md
  ROADMAP.md
  LICENSE
  DISCLAIMER.md
  CHANGELOG.md
  CLAUDE.md
  AGENTS.md
  .github/copilot-instructions.md
  docs/badges.md
  docs/community.md
  docs/awesome-vibe-coding-pr.md
  scripts/README.md
  scripts/init-project.example.sh
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
  assets
  .github/workflows
  examples/todo-app-vibe
  examples/telegram-bot-vibe
  examples/landing-page-vibe
  examples/saas-backend-vibe
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
