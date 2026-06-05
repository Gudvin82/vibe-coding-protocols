#!/usr/bin/env bash
set -euo pipefail

MODE="starter"
DRY_RUN=0

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/install-hooks.sh --mode starter
  bash scripts/install-hooks.sh --mode hardening
  bash scripts/install-hooks.sh --mode audit
  bash scripts/install-hooks.sh --mode starter --dry-run

Default:
  --mode starter
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode)
      shift
      MODE="${1:-}"
      ;;
    --dry-run)
      DRY_RUN=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage
      exit 2
      ;;
  esac
  shift
done

case "$MODE" in
  starter|hardening|audit)
    ;;
  *)
    echo "Unsupported mode: $MODE" >&2
    usage
    exit 2
    ;;
esac

ROOT=$(git rev-parse --show-toplevel 2>/dev/null || true)
if [[ -z "$ROOT" ]]; then
  echo "This command must be run inside a git repository."
  exit 2
fi

HOOKS_DIR="$ROOT/.git/hooks"
HOOK_PATH="$HOOKS_DIR/pre-commit"
VIBE_FLAG="--$MODE"

echo "Installing pre-commit hook in $MODE mode."
echo "Use --mode hardening or --mode audit for existing or production projects."

if (( DRY_RUN )); then
  cat <<DRYRUN
Dry run only. The hook would:
- install at $HOOK_PATH
- block staged .env or .env.* files
- allow .env.example
- warn on large staged diffs
- run: bash scripts/vibe-check.sh $VIBE_FLAG
- conditionally run: check-version-consistency, validate-links and check-newlines if those scripts exist
DRYRUN
  exit 0
fi

mkdir -p "$HOOKS_DIR"

cat > "$HOOK_PATH" <<HOOK
#!/usr/bin/env bash
set -euo pipefail

ROOT=\$(git rev-parse --show-toplevel 2>/dev/null || pwd)
cd "\$ROOT"

STAGED_FILES=\$(git diff --cached --name-only)
if echo "\$STAGED_FILES" | grep -E '(^|/)\\.env($|(\\.[^/]+$))' | grep -Ev '(^|/)\\.env(\\.[^/]+)?\\.example$' >/dev/null 2>&1; then
  echo "pre-commit: refusing to commit staged .env-like files"
  exit 1
fi

CHANGED_COUNT=\$(printf '%s\n' "\$STAGED_FILES" | sed '/^$/d' | wc -l | tr -d ' ')
if [[ "\$CHANGED_COUNT" -gt 15 ]]; then
  echo "pre-commit: warning - staged diff touches \$CHANGED_COUNT files. Consider a smaller commit."
fi

if [[ -x scripts/vibe-check.sh || -f scripts/vibe-check.sh ]]; then
  bash scripts/vibe-check.sh $VIBE_FLAG
else
  echo "pre-commit: scripts/vibe-check.sh not found, skipping vibe-check"
fi

if [[ -f VERSION && -f scripts/check-version-consistency.sh ]]; then
  bash scripts/check-version-consistency.sh
fi

if [[ -f scripts/validate-links.sh ]] && command -v python3 >/dev/null 2>&1; then
  python3 scripts/validate-links.sh
fi

if [[ -f scripts/check-newlines.py ]] && command -v python3 >/dev/null 2>&1; then
  python3 scripts/check-newlines.py
fi
HOOK

chmod +x "$HOOK_PATH"
echo "Installed pre-commit hook at $HOOK_PATH"
echo "It blocks staged .env files, warns on large staged diffs, runs bash scripts/vibe-check.sh $VIBE_FLAG and conditionally runs link/newline/version checks when present."
