#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
FIXTURES="$ROOT/scripts/tests/fixtures"

assert_contains() {
  local haystack="$1"
  local needle="$2"
  if [[ "$haystack" != *"$needle"* ]]; then
    echo "Expected to find: $needle" >&2
    exit 1
  fi
}

help_output=$(bash "$ROOT/scripts/vibe-check.sh" --help)
assert_contains "$help_output" "Usage:"

json_output=$(cd "$ROOT" && bash scripts/vibe-check.sh --audit --json)
assert_contains "$json_output" '"placeholder_excluded":'
assert_contains "$json_output" '"artifact_version_warnings":'
python3 -c 'import json,sys; json.loads(sys.stdin.read())' <<<"$json_output" >/dev/null

starter_dir="$FIXTURES/starter-repo"
rm -rf "$starter_dir"
mkdir -p "$starter_dir"
cat > "$starter_dir/README.md" <<'DOC'
# Starter fixture
DOC
cat > "$starter_dir/.gitignore" <<'DOC'
.env
node_modules
dist
build
*.log
DOC
cat > "$starter_dir/AGENTS.md" <<'DOC'
<!-- vcp-artifact: AGENTS -->
<!-- vcp-version: v0.1.11 -->
<!-- methodology-version: v1.4 -->

# AGENTS
DOC
cat > "$starter_dir/PROJECT_MAP.md" <<'DOC'
<!-- vcp-artifact: PROJECT_MAP -->
<!-- vcp-version: v0.1.11 -->
<!-- methodology-version: v1.4 -->

# PROJECT_MAP
DOC
cat > "$starter_dir/SECURITY_BASELINE.md" <<'DOC'
<!-- vcp-artifact: SECURITY_BASELINE -->
<!-- vcp-version: v0.1.11 -->
<!-- methodology-version: v1.4 -->

# SECURITY_BASELINE
DOC
cat > "$starter_dir/.env.example" <<'DOC'
APP_TOKEN=[example-placeholder]
DOC
mkdir -p "$starter_dir/prompts"
cat > "$starter_dir/prompts/product-brief-prompt_en.md" <<'DOC'
# Product Brief
DOC
cat > "$starter_dir/package.json" <<'DOC'
{
  "name": "starter-fixture",
  "version": "0.0.0"
}
DOC
cat > "$starter_dir/package-lock.json" <<'DOC'
{}
DOC
starter_json=$(cd "$starter_dir" && bash "$ROOT/scripts/vibe-check.sh" --starter --json)
assert_contains "$starter_json" '"status": "pass"'
python3 -c 'import json,sys; json.loads(sys.stdin.read())' <<<"$starter_json" >/dev/null

empty_dir="$FIXTURES/empty-repo"
rm -rf "$empty_dir"
mkdir -p "$empty_dir"
set +e
empty_output=$(cd "$empty_dir" && bash "$ROOT/scripts/vibe-check.sh" --starter --json)
empty_code=$?
set -e
if [[ "$empty_code" -ne 1 && "$empty_code" -ne 0 ]]; then
  echo "Unexpected exit code for empty fixture: $empty_code" >&2
  exit 1
fi
assert_contains "$empty_output" '"status":'
python3 -c 'import json,sys; json.loads(sys.stdin.read())' <<<"$empty_output" >/dev/null

env_dir="$FIXTURES/env-repo"
rm -rf "$env_dir"
mkdir -p "$env_dir"
cat > "$env_dir/README.md" <<'DOC'
# Env fixture
DOC
cat > "$env_dir/.gitignore" <<'DOC'
.env
node_modules
dist
build
*.log
DOC
cat > "$env_dir/AGENTS.md" <<'DOC'
# AGENTS
DOC
cat > "$env_dir/.env" <<'DOC'
SECRET=real-looking-value
DOC
set +e
env_json=$(cd "$env_dir" && bash "$ROOT/scripts/vibe-check.sh" --audit --json)
env_code=$?
set -e
if [[ "$env_code" -eq 2 ]]; then
  echo "Unexpected runtime failure in env fixture" >&2
  exit 1
fi
assert_contains "$env_json" '"status":'
assert_contains "$env_json" '"placeholder_excluded":'
python3 -c 'import json,sys; json.loads(sys.stdin.read())' <<<"$env_json" >/dev/null

echo "Basic vibe-check tests passed."
