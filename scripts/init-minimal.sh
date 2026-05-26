#!/usr/bin/env bash
set -euo pipefail

BASE_URL="https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-./scripts/init-minimal.sh}")" && pwd 2>/dev/null || pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd 2>/dev/null || pwd)"
TARGET_DIR="${PWD}"
MODE=""
DRY_RUN=0
YES=0
FORCE=0
FILES=()
TMP_DIR=""
PACKS=("starter" "hardening" "audit")

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/init-minimal.sh --starter
  bash scripts/init-minimal.sh --hardening
  bash scripts/init-minimal.sh --audit
  bash scripts/init-minimal.sh --dry-run --starter
  curl -fsSL https://raw.githubusercontent.com/Gudvin82/vibe-coding-protocols/main/scripts/init-minimal.sh | bash -s -- --starter

Options:
  --starter      Copy the minimal starter pack
  --hardening    Copy the minimal hardening pack
  --audit        Copy the minimal audit pack
  --dry-run      Show what would be copied without changing files
  --yes          Skip confirmation prompt
  --force        Allow overwriting existing files (still prompts unless --yes)
  -h, --help     Show this help
USAGE
}

cleanup() {
  if [[ -n "$TMP_DIR" && -d "$TMP_DIR" ]]; then
    rm -rf "$TMP_DIR"
  fi
}
trap cleanup EXIT

need_curl() {
  if ! command -v curl >/dev/null 2>&1; then
    echo "ERROR: curl is required for remote bootstrap mode." >&2
    exit 1
  fi
}

source_available_locally() {
  local src="$1"
  [[ -f "$REPO_ROOT/$src" && -f "$REPO_ROOT/README.md" ]]
}

fetch_file() {
  local src="$1"
  local dst="$2"

  if source_available_locally "$src"; then
    cp "$REPO_ROOT/$src" "$dst"
    return 0
  fi

  need_curl
  curl -fsSL "$BASE_URL/$src" -o "$dst"
}

add_file() {
  local src="$1"
  local dest="$2"
  FILES+=("$src::$dest")
}

build_file_list() {
  FILES=()
  case "$MODE" in
    starter)
      add_file "AGENTS.md" "AGENTS.md"
      add_file "templates/PROJECT_MAP.md" "PROJECT_MAP.md"
      add_file "templates/PROMPTS.md" "docs/PROMPTS.md"
      add_file "prompts/product-brief-prompt.md" "docs/product-brief-prompt.md"
      ;;
    hardening)
      add_file "templates/AUDIT_BACKLOG.md" "AUDIT_BACKLOG.md"
      add_file "templates/SECURITY_BASELINE.md" "SECURITY_BASELINE.md"
      add_file "templates/THIRD_PARTY_REGISTRY.md" "THIRD_PARTY_REGISTRY.md"
      add_file "templates/SECURITY_OPERATIONS_BASELINE.md" "SECURITY_OPERATIONS_BASELINE.md"
      add_file "checklists/perimeter-security-checklist.md" "perimeter-security-checklist.md"
      add_file "checklists/external-exposure-checklist.md" "external-exposure-checklist.md"
      ;;
    audit)
      add_file "templates/AUDIT_BACKLOG.md" "AUDIT_BACKLOG.md"
      add_file "templates/SECURITY_SCANNER_REPORT.md" "SECURITY_SCANNER_REPORT.md"
      add_file "templates/SECURITY_OPERATIONS_BASELINE.md" "SECURITY_OPERATIONS_BASELINE.md"
      add_file "checklists/perimeter-security-checklist.md" "perimeter-security-checklist.md"
      add_file "checklists/database-load-scalability-checklist.md" "database-load-scalability-checklist.md"
      ;;
    "")
      echo "ERROR: choose one mode: --starter, --hardening or --audit" >&2
      usage
      exit 1
      ;;
    *)
      echo "ERROR: choose one mode: --starter, --hardening or --audit" >&2
      usage
      exit 1
      ;;
  esac
}

print_all_packs() {
  echo "Available packs:"
  for pack in "${PACKS[@]}"; do
    echo "- $pack"
  done
}

print_plan() {
  echo "Vibe Coding Protocols minimal bootstrap"
  echo "Mode: $MODE"
  echo "Target directory: $TARGET_DIR"
  echo "Dry run: $([[ "$DRY_RUN" -eq 1 ]] && echo yes || echo no)"
  echo "Force overwrite: $([[ "$FORCE" -eq 1 ]] && echo yes || echo no)"
  echo
  echo "Files to copy:"
  for entry in "${FILES[@]}"; do
    local src="${entry%%::*}"
    local dst="${entry##*::}"
    printf ' - %s -> %s\n' "$src" "$dst"
  done
}

confirm() {
  if [[ "$YES" -eq 1 ]]; then
    return 0
  fi
  echo
  read -r -p "Proceed? [y/N]: " reply
  [[ "$reply" == "y" || "$reply" == "Y" ]]
}

copy_files() {
  TMP_DIR="$(mktemp -d)"

  for entry in "${FILES[@]}"; do
    local src="${entry%%::*}"
    local dst_rel="${entry##*::}"
    local dst="$TARGET_DIR/$dst_rel"
    local tmp="$TMP_DIR/$(basename "$dst_rel")"

    mkdir -p "$(dirname "$dst")"

    if [[ -e "$dst" && "$FORCE" -ne 1 ]]; then
      echo "SKIP: $dst already exists"
      continue
    fi

    if [[ -e "$dst" && "$FORCE" -eq 1 && "$YES" -ne 1 ]]; then
      echo
      read -r -p "Overwrite $dst ? [y/N]: " overwrite
      if [[ "$overwrite" != "y" && "$overwrite" != "Y" ]]; then
        echo "SKIP: $dst"
        continue
      fi
    fi

    fetch_file "$src" "$tmp"
    cp "$tmp" "$dst"
    echo "COPIED: $dst_rel"
  done
}

for arg in "$@"; do
  case "$arg" in
    --starter) MODE="starter" ;;
    --hardening) MODE="hardening" ;;
    --audit) MODE="audit" ;;
    --dry-run) DRY_RUN=1 ;;
    --yes) YES=1 ;;
    --force) FORCE=1 ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "ERROR: unknown option: $arg" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ -z "$MODE" && "$DRY_RUN" -eq 1 ]]; then
  echo "Vibe Coding Protocols minimal bootstrap"
  print_all_packs
  echo
  echo "Dry run only. Choose one mode to see exact files, for example:"
  echo "  bash scripts/init-minimal.sh --dry-run --starter"
  exit 0
fi

build_file_list
print_plan

if [[ "$DRY_RUN" -eq 1 ]]; then
  echo
  echo "Dry run only. No files were changed."
  exit 0
fi

if ! confirm; then
  echo "Cancelled."
  exit 0
fi

copy_files

echo
if [[ "$FORCE" -eq 1 ]]; then
  echo "Done. Review copied files carefully because overwrite mode was enabled."
else
  echo "Done. Review copied files before using them in a real project."
fi
