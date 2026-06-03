#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

python3 -m vcp_cli --help >/dev/null
python3 -m vcp_cli version | grep -F "v0.5.9" >/dev/null
python3 -m vcp_cli doctor --json | grep -F '"manifest_directory":' >/dev/null
python3 -m vcp_cli check --fast --json | grep -F '"ok": true' >/dev/null
python3 -m vcp_cli init --print-prompt | grep -F "Read START_HERE.md first." >/dev/null
python3 -m vcp_cli evaluate --json | grep -F '"evaluation_guide_present": true' >/dev/null
python3 -m vcp_cli evaluate --print-prompt | grep -F "Do not judge from README alone." >/dev/null
python3 -m vcp_cli evaluate --json | grep -F '"llm_reference_present": true' >/dev/null
python3 -m vcp_cli evaluate --json | grep -F '"progressive_disclosure_present": true' >/dev/null
python3 -m vcp_cli route --profile production --json | grep -F '"selected_route": "Full Hardening"' >/dev/null
python3 -m vcp_cli route --profile third-party-api --json | grep -F '"manifest_route_id": "third-party-api-intake"' >/dev/null
python3 -m vcp_cli route --profile public-growth --json | grep -F '"manifest_route_id": "public-growth-playbook"' >/dev/null
python3 -m vcp_cli route --profile spec-first --json | grep -F '"manifest_route_id": "spec-first-feature"' >/dev/null
python3 -m vcp_cli adopt --pack third-party-api --dry-run --json | grep -F '"review_gate_requirement": "Required before production integration merge or release."' >/dev/null
python3 -m vcp_cli adopt --pack public-growth --dry-run --json | grep -F '"pack": "public-growth"' >/dev/null
python3 -m vcp_cli adopt --pack spec-first --dry-run --json | grep -F '"pack": "spec-first"' >/dev/null
python3 -m vcp_cli review plan --json | grep -F '"prompt_path": "templates/prompts/loop-code-review.md"' >/dev/null
python3 -m vcp_cli index validate >/dev/null
python3 -m vcp_cli index show --json | grep -F '"version": "v0.5.9"' >/dev/null
python3 -m vcp_cli index search production --json | grep -F '"query": "production"' >/dev/null
python3 -m vcp_cli cards list --json | grep -F '"total"' >/dev/null
python3 -m vcp_cli cards list --recommended --json | grep -F '"items"' >/dev/null
python3 -m vcp_cli cards list --maturity stable --json | grep -F '"items"' >/dev/null
python3 -m vcp_cli cards list --platform codex-cli --json | grep -F '"items"' >/dev/null
python3 -m vcp_cli cards validate >/dev/null
python3 -m vcp_cli cards show production-hardening --json | grep -F '"id": "production-hardening"' >/dev/null
python3 -m vcp_cli spec validate --json | grep -F '"spec_files"' >/dev/null
python3 -m vcp_cli spec template prd | grep -F "# Product Requirements Document" >/dev/null
python3 -m vcp_cli spec summary --json | grep -F '"recommended_flow"' >/dev/null
python3 -m vcp_cli workflow list --json | grep -F '"items"' >/dev/null
python3 -m vcp_cli workflow validate --json | grep -F '"ok": true' >/dev/null
python3 -m vcp_cli workflow show production-hardening --json | grep -F '"id": "production-hardening"' >/dev/null
python3 -m vcp_cli workflow search hardening --json | grep -F '"query": "hardening"' >/dev/null
python3 -m vcp_cli diagnose --json | grep -F '"difference_from_doctor"' >/dev/null
python3 -m vcp_cli diagnose --profile production --json | grep -F '"profile": "production"' >/dev/null
python3 -m vcp_cli manifest validate >/dev/null
python3 -m vcp_cli benchmark run >/dev/null
python3 -m vcp_cli score --json | grep -F '"Third-party API intake / registry"' >/dev/null
python3 -m vcp_cli score --json | grep -F '"Spec lane"' >/dev/null
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
npm run vcp -- workflow validate >/dev/null
npm run vcp -- spec validate >/dev/null
npm run vcp -- index validate >/dev/null
npm run vcp -- cards validate >/dev/null
npm run vcp -- manifest validate >/dev/null
printf '%s
' 'VCP CLI smoke tests passed.'
