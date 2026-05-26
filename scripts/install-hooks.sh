#!/usr/bin/env bash
set -euo pipefail

ROOT=$(git rev-parse --show-toplevel 2>/dev/null || true)
if [[ -z "$ROOT" ]]; then
  echo "This command must be run inside a git repository."
  exit 2
fi

HOOKS_DIR="$ROOT/.git/hooks"
HOOK_PATH="$HOOKS_DIR/pre-commit"
mkdir -p "$HOOKS_DIR"

cat > "$HOOK_PATH" <<'HOOK'
#!/usr/bin/env bash
set -euo pipefail

ROOT=$(git rev-parse --show-toplevel 2>/dev/null || pwd)
cd "$ROOT"

STAGED_FILES=$(git diff --cached --name-only)
if echo "$STAGED_FILES" | grep -E '(^|/)\.env($|(\.[^/]+$))' | grep -Ev '(^|/)\.env(\.[^/]+)?\.example$' >/dev/null 2>&1; then
  echo "pre-commit: refusing to commit staged .env-like files"
  exit 1
fi

CHANGED_COUNT=$(printf '%s\n' "$STAGED_FILES" | sed '/^$/d' | wc -l | tr -d ' ')
if [[ "$CHANGED_COUNT" -gt 15 ]]; then
  echo "pre-commit: warning - staged diff touches $CHANGED_COUNT files. Consider a smaller commit."
fi

if [[ -x scripts/vibe-check.sh || -f scripts/vibe-check.sh ]]; then
  bash scripts/vibe-check.sh --starter
else
  echo "pre-commit: scripts/vibe-check.sh not found, skipping vibe-check"
fi
HOOK

chmod +x "$HOOK_PATH"
echo "Installed pre-commit hook at $HOOK_PATH"
echo "It blocks staged .env files, warns on large staged diffs and runs bash scripts/vibe-check.sh --starter."
