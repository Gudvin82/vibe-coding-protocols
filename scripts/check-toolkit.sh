#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

required_files=(
  VERSION
  METHODOLOGY_VERSION
  README.md
  README_ru.md
  ROADMAP.md
  ANTI_PATTERNS.md
  LICENSE
  DISCLAIMER.md
  CHANGELOG.md
  CLAUDE.md
  AGENTS.md
  .gitattributes
  .github/copilot-instructions.md
  docs/badges.md
  docs/community.md
  docs/community-issues.md
  docs/awesome-vibe-coding-pr.md
  docs/multi-agent-workflows.md
  docs/vibe-metrics.md
  docs/automated-vibe-check.md
  docs/ide-rules-dry-policy.md
  docs/self-dogfooding.md
  docs/release-readiness.md
  docs/adoption-feedback.md
  docs/known-limitations.md
  docs/vibe-check-doctor.md
  docs/vibe-check-init-report.md
  docs/architecture-map.md
  docs/deploy-path.md
  docs/up-to-date-docs-policy.md
  docs/ecosystem.md
  docs/mirrors.md
  docs/starter-template-intake.md
  docs/release-v0.2.1.md
  docs/pre-commit-hooks.md
  docs/cli-roadmap.md
  docs/release-v0.1.1.md
  scripts/README.md
  scripts/vibe-check.sh
  scripts/check-version-consistency.sh
  scripts/check-ide-rules-consistency.sh
  scripts/check-newlines.py
  scripts/init-project.example.sh
  assets/social-preview.svg
  templates/ARCHITECTURE_MAP.md
  examples/architecture-map-example.md
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
  examples/legacy-ai-mess-vibe
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

bash scripts/check-version-consistency.sh
bash scripts/check-ide-rules-consistency.sh
python3 scripts/check-newlines.py

echo "Toolkit structure check passed."
