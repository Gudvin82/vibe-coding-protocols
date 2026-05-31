#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

python3 -m vcp_cli --help >/dev/null
python3 -m vcp_cli version | grep -F "v0.5.1" >/dev/null
python3 -m vcp_cli doctor --json | grep -F '"powershell_first_mode_supported": true' >/dev/null
python3 -m vcp_cli check --fast --json | grep -F '"ok": true' >/dev/null
python3 -m vcp_cli route --profile production --json | grep -F '"selected_route": "Full Hardening"' >/dev/null
python3 -m vcp_cli route --profile third-party-api --json | grep -F '"manifest_route_id": "third-party-api-intake"' >/dev/null
python3 -m vcp_cli adopt --pack third-party-api --dry-run --json | grep -F '"review_gate_requirement": "Required before production integration merge or release."' >/dev/null
python3 -m vcp_cli review plan --json | grep -F '"prompt_path": "templates/prompts/loop-code-review.md"' >/dev/null
python3 -m vcp_cli manifest validate >/dev/null
python3 -m vcp_cli benchmark run >/dev/null
python3 -m vcp_cli score --json | grep -F '"Third-party API intake / registry"' >/dev/null
printf '%s
' 'VCP CLI smoke tests passed.'
