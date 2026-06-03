#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

REPO_VERSION="$(tr -d '[:space:]' < VERSION)"
METHODOLOGY_VERSION="$(tr -d '[:space:]' < METHODOLOGY_VERSION)"
VCP_MANIFEST=".vcp/manifests/vcp.manifest.json"
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
check_contains "$VCP_MANIFEST" "\"package_version\": \"$REPO_VERSION\"" "vcp manifest package version"
check_contains "$VCP_MANIFEST" "\"methodology_version\": \"$METHODOLOGY_VERSION\"" "vcp manifest methodology version"
check_contains llms-full.txt "$REPO_VERSION" "llms-full repo version"
check_contains CITATION.cff "version: \"$REPO_VERSION\"" "CITATION.cff version"

if [[ -f package.json ]]; then
  check_contains package.json "\"version\": \"${REPO_VERSION#v}\"" "package.json version"
fi

if [[ -f pyproject.toml ]]; then
  check_contains pyproject.toml "version = \"${REPO_VERSION#v}\"" "pyproject.toml version"
fi

if [[ -f vcp_cli/__init__.py ]]; then
  check_contains vcp_cli/__init__.py "__version__ = \"${REPO_VERSION#v}\"" "vcp_cli version"
fi

while IFS= read -r file; do
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
done < <(find templates -name '*.md' | sort)

stale_versions=(
  "v0.1.11"
  "v0.2.0"
  "v0.2.1"
  "v0.2.2"
  "v0.3.0"
  "v0.4.0"
  "v0.4.1"
  "v0.4.2"
  "v0.4.3"
  "v0.4.4"
  "v0.5.0"
  "v0.5.1"
  "v0.5.2"
  "v0.5.3"
  "v0.5.4"
  "v0.5.5"
  "v0.5.6"
  "v0.5.7"
  "v0.5.8"
  "v0.5.9"
  "v0.6.0"
  "v0.6.1"
)

entry_files=(
  README.md
  README_ru.md
  docs/versioning.md
  PROJECT_MAP.md
  package.json
  pyproject.toml
  llms.txt
  llms-full.txt
)

for file in "${entry_files[@]}"; do
  [[ -f "$file" ]] || continue
  for stale in "${stale_versions[@]}"; do
    if [[ "$stale" == "$REPO_VERSION" ]]; then
      continue
    fi
    if grep -F "$stale" "$file" >/dev/null 2>&1; then
      echo "Stale version marker in $file: $stale"
      problems=$((problems + 1))
    fi
  done
done

if (( problems > 0 )); then
  exit 1
fi

echo "Version consistency check passed for $REPO_VERSION / $METHODOLOGY_VERSION."
