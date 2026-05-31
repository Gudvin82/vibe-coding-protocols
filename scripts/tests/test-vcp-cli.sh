#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

python3 -m vcp_cli --help >/dev/null
python3 -m vcp_cli version | grep -F "v0.5.0" >/dev/null
python3 -m vcp_cli route --profile production --json | grep -F '"selected_route": "Full Hardening"' >/dev/null
python3 -m vcp_cli route --profile shared-engine --json | grep -F '"adoption_pack": "shared-engine"' >/dev/null
python3 -m vcp_cli adopt --pack production --dry-run --json | grep -F '"review_gate_requirement": "Required before merge/release."' >/dev/null
python3 -m vcp_cli review plan --json | grep -F '"prompt_path": "templates/prompts/loop-code-review.md"' >/dev/null
python3 -m vcp_cli manifest validate >/dev/null
python3 -m vcp_cli benchmark run >/dev/null
python3 -m vcp_cli score --json | grep -F '"categories"' >/dev/null
python3 -m vcp_cli demo shared-engine | grep -F 'Route: Full Hardening' >/dev/null
printf '%s
' 'VCP CLI smoke tests passed.'
