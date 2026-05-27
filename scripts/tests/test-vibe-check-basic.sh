#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)
FIXTURES="$ROOT/scripts/tests/fixtures"
TMP_PARENT=$(mktemp -d)
trap 'rm -rf "$TMP_PARENT"' EXIT

assert_contains() {
  local haystack="$1"
  local needle="$2"
  if [[ "$haystack" != *"$needle"* ]]; then
    echo "Expected to find: $needle" >&2
    exit 1
  fi
}

assert_json_key() {
  local json_input="$1"
  local expr="$2"
  JSON_INPUT="$json_input" python3 - "$expr" <<'PY'
import json
import os
import sys
expr = sys.argv[1]
data = json.loads(os.environ["JSON_INPUT"])
value = eval(expr, {"__builtins__": {}}, {"data": data})
if not value:
    raise SystemExit(1)
PY
}

make_temp_repo() {
  local name="$1"
  local source="$FIXTURES/$name"
  local target="$TMP_PARENT/$name"
  rm -rf "$target"
  mkdir -p "$target"
  if [[ -d "$source" ]]; then
    cp -R "$source"/. "$target"/
  fi
  printf '%s\n' "$target"
}

help_output=$(bash "$ROOT/scripts/vibe-check.sh" --help)
assert_contains "$help_output" "Usage:"
assert_contains "$help_output" "--doctor"
assert_contains "$help_output" "--init-report"

repo_json=$(cd "$ROOT" && bash scripts/vibe-check.sh --audit --json)
assert_contains "$repo_json" '"placeholder_excluded":'
assert_contains "$repo_json" '"artifact_version_warnings":'
assert_contains "$repo_json" '"content_quality_warnings":'
python3 -c 'import json,sys; json.loads(sys.stdin.read())' <<<"$repo_json" >/dev/null

doctor_json=$(cd "$ROOT" && bash scripts/vibe-check.sh --doctor --json)
assert_contains "$doctor_json" '"mode": "doctor"'
assert_contains "$doctor_json" '"recommended_route":'
python3 -c 'import json,sys; json.loads(sys.stdin.read())' <<<"$doctor_json" >/dev/null

init_json=$(cd "$ROOT" && bash scripts/vibe-check.sh --init-report --json)
assert_contains "$init_json" '"mode": "init-report"'
assert_contains "$init_json" '"copy_first":'
python3 -c 'import json,sys; json.loads(sys.stdin.read())' <<<"$init_json" >/dev/null

starter_dir=$(make_temp_repo starter-good)
starter_json=$(cd "$starter_dir" && bash "$ROOT/scripts/vibe-check.sh" --starter --json)
assert_json_key "$starter_json" "data['fail'] == 0"
assert_json_key "$starter_json" "data['status'] in ('pass', 'warn')"

hardening_dir=$(make_temp_repo hardening-good)
hardening_json=$(cd "$hardening_dir" && bash "$ROOT/scripts/vibe-check.sh" --audit --json)
assert_json_key "$hardening_json" "data['fail'] == 0"

empty_dir=$(make_temp_repo empty-repo)
set +e
empty_json=$(cd "$empty_dir" && bash "$ROOT/scripts/vibe-check.sh" --starter --json)
empty_code=$?
set -e
if [[ "$empty_code" -ne 0 && "$empty_code" -ne 1 ]]; then
  echo "Unexpected exit code for empty fixture: $empty_code" >&2
  exit 1
fi
assert_contains "$empty_json" '"status":'

leak_dir=$(make_temp_repo env-leak)
cat <<'DOC' > "$leak_dir/.env"
SECRET=synthetic-test-value
DOC
set +e
env_json=$(cd "$leak_dir" && bash "$ROOT/scripts/vibe-check.sh" --audit --json)
env_code=$?
set -e
if [[ "$env_code" -eq 2 ]]; then
  echo "Unexpected runtime failure in env-leak fixture" >&2
  exit 1
fi
assert_json_key "$env_json" "data['fail'] >= 1 or data['warn'] >= 1"

empty_backlog_dir=$(make_temp_repo empty-audit-backlog)
empty_backlog_json=$(cd "$empty_backlog_dir" && bash "$ROOT/scripts/vibe-check.sh" --audit --json)
assert_json_key "$empty_backlog_json" "data['content_quality_warnings'] > 0"

outdated_dir=$(make_temp_repo outdated-vcp-version)
outdated_json=$(cd "$outdated_dir" && bash "$ROOT/scripts/vibe-check.sh" --starter --json)
assert_json_key "$outdated_json" "data['artifact_version_warnings'] > 0"

flattened_dir=$(make_temp_repo flattened-docs)
python3 - <<'PY' "$flattened_dir"
from pathlib import Path
import sys
root = Path(sys.argv[1])
(root / "flattened.md").write_text("# Title " + ("x" * 700), encoding="utf-8")
PY
set +e
flattened_output=$(cd "$flattened_dir" && python3 "$ROOT/scripts/check-newlines.py" "$flattened_dir" 2>&1)
flattened_code=$?
set -e
if [[ "$flattened_code" -eq 0 ]]; then
  echo "Expected check-newlines.py to fail for flattened docs fixture" >&2
  exit 1
fi
assert_contains "$flattened_output" "flattened.md"

missing_sha_dir=$(make_temp_repo missing-sha256sums)
missing_sha_json=$(cd "$missing_sha_dir" && bash "$ROOT/scripts/vibe-check.sh" --starter --json)
assert_json_key "$missing_sha_json" "data['status'] == 'warn'"
assert_json_key "$missing_sha_json" "data['warn'] >= 1"

printf '%s\n' 'Basic vibe-check tests passed.'
