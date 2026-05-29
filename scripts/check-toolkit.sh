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
  docs/community-feedback.md
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
  docs/cli.md
  docs/integrations/README.md
  docs/integrations/claude-code.md
  docs/integrations/codex.md
  docs/integrations/cursor.md
  docs/integrations/windsurf.md
  docs/integrations/github-copilot.md
  docs/integrations/jetbrains-junie.md
  docs/ide-plugins.md
  docs/boundary-linting.md
  docs/markdown-style.md
  docs/ecosystem-references.md
  docs/security-tooling-landscape.md
  docs/protocol-index.md
  docs/public-site-readiness.md
  docs/seo-ai-crawler-readiness.md
  docs/vibe-check-doctor.md
  docs/vibe-check-init-report.md
  docs/architecture-map.md
  docs/deploy-path.md
  docs/up-to-date-docs-policy.md
  docs/ecosystem.md
  docs/mirrors.md
  docs/mirror-sync.md
  docs/starter-template-intake.md
  docs/update-copied-artifacts.md
  docs/prompt-drift-control.md
  docs/vibe-check-reference.md
  docs/npm-wrapper.md
  docs/python-wrapper.md
  docs/vscode-extension.md
  docs/release-v0.4.2.md
  docs/release-v0.3.0.md
  docs/pre-commit-hooks.md
  docs/cli-roadmap.md
  docs/release-v0.1.1.md
  scripts/README.md
  scripts/vibe-check.sh
  scripts/check-version-consistency.sh
  scripts/check-ide-rules-consistency.sh
  scripts/check-newlines.py
  scripts/init-project.example.sh
  package.json
  pyproject.toml
  comparison.md
  llms.txt
  bin/vibe-check.js
  vcp_cli/__main__.py
  vscode-extension/package.json
  vscode-extension/README.md
  vscode-extension/src/extension.ts
  assets/social-preview.svg
  templates/ARCHITECTURE_MAP.md
  templates/protocol-pack-metadata.yml
  templates/reports/security-review-scope.md
  templates/public-site/README.md
  templates/public-site/llms.txt
  templates/public-site/robots.txt
  templates/public-site/schema-org.organization.jsonld
  templates/public-site/schema-org.website.jsonld
  templates/public-site/schema-org.software-source-code.jsonld
  templates/public-site/schema-org.breadcrumb-list.jsonld
  templates/public-site/schema-org.faq-page.jsonld
  examples/architecture-map-example.md
  examples/bad-to-good/README.md
  examples/bad-to-good/maintenance-refactor-before.md
  examples/bad-to-good/maintenance-refactor-after.md
  examples/bad-to-good/ui-ownership-before.md
  examples/bad-to-good/ui-ownership-after.md
  examples/bad-to-good/hardening-before.md
  examples/bad-to-good/hardening-after.md
  case-studies/synthetic-before-after/README.md
  case-studies/redaction-guide.md
  .github/ISSUE_TEMPLATE/share-your-agents.yml
)

required_dirs=(
  protocols
  prompts
  templates
  agents
  examples
  checklists
  docs
  docs/integrations
  scripts
  assets
  .github/workflows
  examples/todo-app-vibe
  examples/telegram-bot-vibe
  examples/landing-page-vibe
  examples/saas-backend-vibe
  examples/legacy-ai-mess-vibe
  examples/bad-to-good
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
