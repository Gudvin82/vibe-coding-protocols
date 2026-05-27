#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

REPO_VERSION="$(tr -d '[:space:]' < VERSION)"
METHODOLOGY_VERSION="$(tr -d '[:space:]' < METHODOLOGY_VERSION)"
problems=0

check_contains() {
  local file="$1"
  local needle="$2"
  local label="$3"

  if [[ ! -f "$file" ]]; then
    echo "Missing file: $file"
    problems=$((problems + 1))
    return
  fi

  if ! grep -F "$needle" "$file" >/dev/null 2>&1; then
    echo "Version mismatch in $file: missing $label -> $needle"
    problems=$((problems + 1))
  fi
}

check_contains README.md "repo-${REPO_VERSION}" "README badge"
check_contains README.md "$REPO_VERSION" "README repository package"
check_contains README_ru.md "$REPO_VERSION" "README_ru repository package"
check_contains CHANGELOG.md "$REPO_VERSION" "CHANGELOG entry"
check_contains docs/versioning.md "Repository package \`$REPO_VERSION\`" "docs/versioning repo version"
check_contains docs/versioning.md "Web methodology \`$METHODOLOGY_VERSION\`" "docs/versioning methodology version"
check_contains "docs/release-${REPO_VERSION}.md" "$REPO_VERSION" "release notes title"

for file in templates/*.md; do
  [[ -e "$file" ]] || continue
  case "$file" in
    templates/README.md|\
    templates/*_ru.md|\
    templates/LEGAL_CHECKLIST.md|\
    templates/PAYMENT_FISCALIZATION_CHECKLIST.md|\
    templates/PROMPTS.md|\
    templates/SCALABILITY_BACKLOG.md|\
    templates/SECURITY_SCANNER_REPORT.md)
      continue
      ;;
  esac
  check_contains "$file" "<!-- vcp-version: $REPO_VERSION -->" "template marker"
  check_contains "$file" "<!-- methodology-version: $METHODOLOGY_VERSION -->" "methodology marker"
done

if (( problems > 0 )); then
  exit 1
fi

echo "Version consistency check passed for $REPO_VERSION / $METHODOLOGY_VERSION."
