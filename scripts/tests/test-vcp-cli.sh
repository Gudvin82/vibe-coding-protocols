#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

python3 -m vcp_cli --help >/dev/null
python3 -m vcp_cli version | grep -F "v0.5.7" >/dev/null
python3 -m vcp_cli doctor --json | grep -F '"manifest_directory":' >/dev/null
python3 -m vcp_cli check --fast --json | grep -F '"ok": true' >/dev/null
python3 -m vcp_cli init --print-prompt | grep -F "Read START_HERE.md first." >/dev/null
python3 -m vcp_cli evaluate --json | grep -F '"evaluation_guide_present": true' >/dev/null
python3 -m vcp_cli evaluate --print-prompt | grep -F "Do not judge from README alone." >/dev/null
python3 -m vcp_cli evaluate --json | grep -F '"llm_reference_present": true' >/dev/null
python3 -m vcp_cli route --profile production --json | grep -F '"selected_route": "Full Hardening"' >/dev/null
python3 -m vcp_cli route --profile third-party-api --json | grep -F '"manifest_route_id": "third-party-api-intake"' >/dev/null
python3 -m vcp_cli route --profile public-growth --json | grep -F '"manifest_route_id": "public-growth-playbook"' >/dev/null
python3 -m vcp_cli adopt --pack third-party-api --dry-run --json | grep -F '"review_gate_requirement": "Required before production integration merge or release."' >/dev/null
python3 -m vcp_cli adopt --pack public-growth --dry-run --json | grep -F '"pack": "public-growth"' >/dev/null
python3 -m vcp_cli review plan --json | grep -F '"prompt_path": "templates/prompts/loop-code-review.md"' >/dev/null
python3 -m vcp_cli manifest validate >/dev/null
python3 -m vcp_cli benchmark run >/dev/null
python3 -m vcp_cli score --json | grep -F '"Third-party API intake / registry"' >/dev/null
python3 -m vcp_cli score --json | grep -F '"LLM citation and AI-agent entry"' >/dev/null
python3 -m vcp_cli backlog validate >/dev/null
python3 -m vcp_cli backlog list --json | grep -F '"ok": true' >/dev/null
python3 -m vcp_cli backlog report --json | grep -F '"counts_by_status"' >/dev/null
python3 -m vcp_cli backlog add --title "Synthetic backlog test item" --type idea --priority P3 --source manual --dry-run --json | grep -F '"dry_run": true' >/dev/null
python3 -m vcp_cli backlog move --id VCP-001 --status doing --dry-run --json | grep -F '"dry_run": true' >/dev/null
python3 -m vcp_cli backlog done --id VCP-001 --validation "tests green" --review "accepted" --dry-run --json | grep -F '"dry_run": true' >/dev/null
python3 -m vcp_cli backlog archive --id VCP-002 --reason "Synthetic archive path" --dry-run --json | grep -F '"dry_run": true' >/dev/null
npm run vcp -- doctor >/dev/null
npm run vcp -- evaluate >/dev/null
npm run vcp -- route --profile production >/dev/null
npm run vcp -- route --profile public-growth >/dev/null
npm run vcp -- manifest validate >/dev/null
printf '%s
' 'VCP CLI smoke tests passed.'
