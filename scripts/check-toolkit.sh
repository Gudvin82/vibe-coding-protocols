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
  AI_INTAKE.md
  AGENTS.md
  .gitattributes
  .github/copilot-instructions.md
  docs/badges.md
  docs/community.md
  docs/community-feedback.md
  docs/target-project-classifier.md
  docs/adoption-packs.md
  docs/route-map.md
  docs/demo.md
  docs/demo-output.md
  docs/release-checklist.md
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
  docs/windows.md
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
  docs/site/README.md
  docs/site/navigation.md
  docs/site/github-pages.md
  docs/site/information-architecture.md
  docs/site/publishing-checklist.md
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
  docs/release-v0.4.3.md
  docs/release-v0.4.4.md
  docs/release-v0.5.0.md
  docs/release-v0.5.1.md
  docs/release-v0.5.2.md
  docs/npm.md
  docs/init.md
  docs/adoption-packs.quickstart.md
  docs/roadmap.md
  docs/measured-impact.md
  .vcp/README.md
  protocols/integrations/README.md
  protocols/integrations/third-party-api-intake.md
  commands/third-party-api-intake.md
  protocols/review/README.md
  protocols/review/post-task-code-review.md
  commands/loop-code-review.md
  templates/prompts/loop-code-review.md
  templates/reports/code-review-report.md
  examples/review/README.md
  examples/review/loop-code-review.example.md
  examples/review/no-actionable-findings.example.md
  examples/review/rejected-finding.example.md
  docs/release-v0.3.0.md
  docs/pre-commit-hooks.md
  docs/cli-roadmap.md
  docs/release-v0.1.1.md
  scripts/README.md
  scripts/vibe-check.sh
  scripts/check-version-consistency.sh
  scripts/check-ide-rules-consistency.sh
  scripts/check-newlines.py
  scripts/tests/test-vcp-cli.sh
  scripts/tests/test-vcp-cli-windows-parity.py
  scripts/init-project.example.sh
  package.json
  pyproject.toml
  comparison.md
  llms.txt
  .vcp/manifests/vcp.manifest.json
  .vcp/manifests/protocols.manifest.json
  .vcp/manifests/adoption-packs.manifest.json
  .vcp/manifests/commands.manifest.json
  .vcp/manifests/reports.manifest.json
  .vcp/manifests/benchmarks.manifest.json
  bin/vcp
  bin/vcp.cmd
  bin/vcp.ps1
  bin/vcp-node.js
  bin/vibe-check.js
  vcp_cli/__main__.py
  vcp_cli/cli.py
  vcp_cli/version.py
  vcp_cli/doctor.py
  vcp_cli/check.py
  vcp_cli/route.py
  vcp_cli/adopt.py
  vcp_cli/score.py
  vcp_cli/manifest.py
  vcp_cli/benchmark.py
  vcp_cli/review.py
  vcp_cli/demo.py
  vcp_cli/utils.py
  vscode-extension/package.json
  vscode-extension/README.md
  vscode-extension/src/extension.ts
  assets/social-preview.svg
  assets/demo/README.md
  templates/ARCHITECTURE_MAP.md
  templates/THIRD_PARTY_REGISTRY.md
  templates/prompts/evaluate-vcp-for-my-repo.md
  templates/prompts/third-party-api-intake.md
  templates/reports/vcp-adoption-assessment.md
  templates/reports/third-party-api-intake-report.md
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
  examples/adoption/dual-production-engine/README.md
  examples/adoption/dual-production-engine/target-profile.md
  examples/adoption/dual-production-engine/recommended-pack.md
  examples/adoption/dual-production-engine/adoption-assessment.example.md
  examples/integrations/README.md
  examples/integrations/public-api-intake.example.md
  examples/integrations/third-party-registry-entry.example.md
  benchmarks/ai-adoption/README.md
  benchmarks/ai-adoption/expected/README.md
  benchmarks/ai-adoption/scenarios/new-project.json
  benchmarks/ai-adoption/scenarios/existing-mvp.json
  benchmarks/ai-adoption/scenarios/production-saas.json
  benchmarks/ai-adoption/scenarios/regulated-payments-data.json
  benchmarks/ai-adoption/scenarios/shared-engine-production.json
  benchmarks/ai-adoption/scenarios/third-party-api-intake.json
  benchmarks/ai-adoption/scenarios/maintenance-refactor.json
  benchmarks/ai-adoption/scenarios/ui-ownership.json
  benchmarks/ai-adoption/scenarios/public-site.json
  benchmarks/ai-adoption/scenarios/post-task-review.json
  examples/bad-to-good/README.md
  examples/bad-to-good/maintenance-refactor-before.md
  examples/bad-to-good/maintenance-refactor-after.md
  examples/bad-to-good/ui-ownership-before.md
  examples/bad-to-good/ui-ownership-after.md
  examples/bad-to-good/hardening-before.md
  examples/bad-to-good/hardening-after.md
  case-studies/synthetic-before-after/README.md
  case-studies/sanitized/README.md
  case-studies/sanitized/redaction-checklist.md
  case-studies/sanitized/case-study-template.md
  case-studies/sanitized/measured-impact-template.md
  case-studies/sanitized/synthetic-measured-impact-example.md
  case-studies/sanitized/ai-skim-failure-to-full-hardening/README.md
  case-studies/sanitized/shared-engine-production/README.md
  case-studies/sanitized/post-task-review-found-critical/README.md
  case-studies/redaction-guide.md
  .github/ISSUE_TEMPLATE/bug_report.md
  .github/ISSUE_TEMPLATE/docs_feedback.md
  .github/ISSUE_TEMPLATE/unsafe_guidance.md
  .github/ISSUE_TEMPLATE/integration_request.md
  .github/ISSUE_TEMPLATE/case_study_submission.md
  .github/ISSUE_TEMPLATE/share-your-agents.yml
)

required_dirs=(
  protocols
  protocols/integrations
  prompts
  templates
  templates/prompts
  agents
  examples
  examples/adoption
  examples/integrations
  benchmarks
  benchmarks/ai-adoption
  benchmarks/ai-adoption/scenarios
  checklists
  docs
  docs/integrations
  docs/site
  protocols/review
  scripts
  assets
  .github/workflows
  examples/todo-app-vibe
  examples/telegram-bot-vibe
  examples/landing-page-vibe
  examples/saas-backend-vibe
  examples/legacy-ai-mess-vibe
  examples/bad-to-good
  examples/review
  case-studies/sanitized
  .vcp
  .vcp/manifests
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
python3 -m vcp_cli manifest validate
python3 -m vcp_cli benchmark run

echo "Toolkit structure check passed."
