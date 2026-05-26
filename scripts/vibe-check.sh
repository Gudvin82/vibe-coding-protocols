#!/usr/bin/env bash
set -euo pipefail

MODE=""
STRICT=0
RUN_SCANNERS=0
PASS=0
WARN=0
FAIL=0
STRUCTURE_SCORE=0
SAFETY_SCORE=0
SECRETS_SCORE=0
SCANNER_SCORE=10
RECOMMENDED=()
SCANNER_RELEVANT=0
SCANNER_SUCCESS=0
SCANNER_WARNINGS=0

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/vibe-check.sh --starter [--strict] [--scanners]
  bash scripts/vibe-check.sh --hardening [--strict] [--scanners]
  bash scripts/vibe-check.sh --audit [--strict] [--scanners]
  bash scripts/vibe-check.sh --scanners

Notes:
- --strict turns WARN into a non-zero exit code.
- --scanners optionally runs external scanners if they are already installed.
- If --scanners is passed without a mode, audit mode is assumed.
USAGE
}

add_recommended() {
  local item="$1"
  local existing
  for existing in "${RECOMMENDED[@]:-}"; do
    if [[ "$existing" == "$item" ]]; then
      return 0
    fi
  done
  RECOMMENDED+=("$item")
}

pass() {
  echo "PASS: $1"
  PASS=$((PASS + 1))
}

warn() {
  echo "WARN: $1"
  WARN=$((WARN + 1))
}

fail() {
  echo "FAIL: $1"
  FAIL=$((FAIL + 1))
}

run_check() {
  local level="$1"
  local message="$2"
  local points="$3"
  if [[ "$level" == "pass" ]]; then
    pass "$message"
    case "$4" in
      structure) STRUCTURE_SCORE=$((STRUCTURE_SCORE + points)) ;;
      safety) SAFETY_SCORE=$((SAFETY_SCORE + points)) ;;
      secrets) SECRETS_SCORE=$((SECRETS_SCORE + points)) ;;
    esac
  elif [[ "$level" == "warn" ]]; then
    warn "$message"
  else
    fail "$message"
  fi
}

for arg in "$@"; do
  case "$arg" in
    --starter|--hardening|--audit)
      if [[ -n "$MODE" ]]; then
        usage
        exit 1
      fi
      MODE="$arg"
      ;;
    --strict)
      STRICT=1
      ;;
    --scanners)
      RUN_SCANNERS=1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage
      exit 1
      ;;
  esac
done

if [[ -z "$MODE" ]]; then
  if (( RUN_SCANNERS )); then
    MODE="--audit"
  else
    usage
    exit 1
  fi
fi

project_has_file() {
  local path="$1"
  [[ -f "$path" ]]
}

project_has_any_file() {
  local candidate
  for candidate in "$@"; do
    if [[ -f "$candidate" ]]; then
      return 0
    fi
  done
  return 1
}

# Level 1: structure checks
if project_has_file README.md; then
  run_check pass "README.md present" 5 structure
else
  run_check fail "README.md missing" 0 structure
  add_recommended "README.md"
fi

if project_has_file .gitignore; then
  run_check pass ".gitignore present" 5 structure
else
  run_check fail ".gitignore missing" 0 structure
  add_recommended ".gitignore"
fi

if project_has_any_file AGENTS.md CLAUDE.md; then
  run_check pass "AI instructions file present" 5 structure
else
  run_check fail "Missing AGENTS.md or CLAUDE.md" 0 structure
  add_recommended "AGENTS.md or CLAUDE.md"
fi

if project_has_any_file PROJECT_MAP.md templates/PROJECT_MAP.md; then
  run_check pass "PROJECT_MAP reference present" 5 structure
else
  if [[ "$MODE" == "--starter" ]]; then
    run_check warn "PROJECT_MAP not found in current directory" 0 structure
  else
    run_check warn "PROJECT_MAP not found" 0 structure
  fi
  add_recommended "PROJECT_MAP.md"
fi

case "$MODE" in
  --starter)
    if project_has_any_file prompts/product-brief-prompt.md docs/product-brief-prompt.md; then
      run_check pass "Starter prompt reference present" 5 structure
    else
      run_check warn "Starter prompt reference not found" 0 structure
      add_recommended "prompts/product-brief-prompt.md"
    fi
    ;;
  --hardening|--audit)
    if project_has_any_file AUDIT_BACKLOG.md templates/AUDIT_BACKLOG.md; then
      run_check pass "AUDIT_BACKLOG reference present" 5 structure
    else
      run_check warn "AUDIT_BACKLOG not found" 0 structure
      add_recommended "AUDIT_BACKLOG.md"
    fi
    ;;
esac

# Level 2: content checks
if project_has_file .gitignore; then
  if rg -n '^\.env(\*|\..*)?$|^\.env$' .gitignore >/dev/null 2>&1; then
    run_check pass ".gitignore covers .env-like files" 5 safety
  else
    run_check warn ".gitignore does not clearly ignore .env-like files" 0 safety
  fi

  if rg -n '^node_modules/?$|^dist/?$|^build/?$' .gitignore >/dev/null 2>&1; then
    run_check pass ".gitignore covers build output directories" 5 safety
  else
    run_check warn ".gitignore does not clearly ignore node_modules/dist/build" 0 safety
  fi

  if rg -n '^\*\.log$|^logs/?$' .gitignore >/dev/null 2>&1; then
    run_check pass ".gitignore covers log files" 5 safety
  else
    run_check warn ".gitignore does not clearly ignore *.log or logs/" 0 safety
  fi
fi

env_ref_regex='process\.env|ENV\[|os\.getenv|dotenv|DATABASE_URL|API_KEY|TOKEN|SECRET|PASSWORD'
if rg -n --hidden --glob '!.git/*' --glob '!node_modules/*' --glob '!dist/*' --glob '!build/*' "$env_ref_regex" . >/dev/null 2>&1; then
  if project_has_any_file .env.example .env.local.example .env.production.example; then
    run_check pass "Env-like references have a companion .env.example" 5 safety
  elif project_has_any_file templates/SECURITY_BASELINE.md templates/SECURITY_OPERATIONS_BASELINE.md; then
    run_check pass "Env-like references have a documented baseline" 5 safety
  else
    run_check warn "Env-like references found without .env.example" 0 safety
    add_recommended ".env.example"
  fi
else
  run_check pass "No env-like patterns detected in quick scan" 5 safety
fi

if [[ "$MODE" == "--hardening" || "$MODE" == "--audit" ]]; then
  if project_has_any_file SECURITY_OPERATIONS_BASELINE.md templates/SECURITY_OPERATIONS_BASELINE.md && project_has_any_file THIRD_PARTY_REGISTRY.md templates/THIRD_PARTY_REGISTRY.md; then
    run_check pass "Security operations and third-party registry references present" 5 safety
  else
    run_check warn "Security operations or third-party registry reference missing" 0 safety
    add_recommended "SECURITY_OPERATIONS_BASELINE.md"
    add_recommended "THIRD_PARTY_REGISTRY.md"
  fi
else
  if project_has_any_file templates/SECURITY_BASELINE.md SECURITY_BASELINE.md templates/SECURITY_OPERATIONS_BASELINE.md; then
    run_check pass "Baseline security file reference present" 5 safety
  else
    run_check warn "No baseline security file reference found" 0 safety
    add_recommended "SECURITY_BASELINE.md or SECURITY_OPERATIONS_BASELINE.md"
  fi
fi

# Level 2b: secrets hygiene
real_env_files=$(find . -maxdepth 3 -type f \( -name '.env' -o -name '.env.*' \) ! -name '.env.example' ! -name '.env.*.example' | sed '/^$/d' || true)
if [[ -n "$real_env_files" ]]; then
  run_check fail "Real .env-like file found in repository" 0 secrets
else
  run_check pass "No .env-like file found" 10 secrets
fi

suspicious_artifacts=$(find . -maxdepth 2 \( -name 'backup.zip' -o -name 'dump.sql' -o -name '*.log' \) -print | sed '/^$/d' || true)
if [[ -n "$suspicious_artifacts" ]]; then
  run_check warn "Possible public exposure artifacts found near repository root" 0 secrets
else
  run_check pass "No obvious backup/dump/log artifacts near repository root" 5 secrets
fi

secret_hits=$(rg -n --hidden --glob '!.git/*' --glob '!node_modules/*' --glob '!dist/*' --glob '!build/*' --glob '!coverage/*' '(API_KEY|TOKEN|SECRET|PASSWORD|PRIVATE_KEY|DATABASE_URL)\s*[:=]' . 2>/dev/null \
  | grep -viE 'example|placeholder|changeme|your_|\[FILL IN|masked-example-not-real|not-real|sample|dummy|test-only' || true)
if [[ -n "$secret_hits" ]]; then
  if (( STRICT )); then
    run_check fail "Suspicious secret-like assignment detected; review and remove or mask it" 0 secrets
  else
    run_check warn "Suspicious secret-like assignment detected; review and remove or mask it" 0 secrets
  fi
else
  run_check pass "No suspicious secret-like assignments detected in quick scan" 10 secrets
fi

for public_doc in ARCHITECTURE.md PROJECT_MAP.md AGENTS.md; do
  if [[ -f "$public_doc" ]]; then
    warn "$public_doc exists at repository root; check whether this is appropriate for a public repo or webroot context"
  fi
done

run_optional_scanner() {
  local label="$1"
  local binary="$2"
  local install_hint="$3"
  shift 3
  local cmd=("$@")

  SCANNER_RELEVANT=$((SCANNER_RELEVANT + 1))
  if ! command -v "$binary" >/dev/null 2>&1; then
    warn "$label not found; see docs/scanner-integration.md ($install_hint)"
    SCANNER_WARNINGS=$((SCANNER_WARNINGS + 1))
    return 0
  fi

  local log_file
  log_file=$(mktemp)
  if "${cmd[@]}" >"$log_file" 2>&1; then
    pass "$label completed without blocking findings in this lightweight pass"
    SCANNER_SUCCESS=$((SCANNER_SUCCESS + 1))
  else
    warn "$label reported findings or did not complete cleanly; review its output manually"
    SCANNER_WARNINGS=$((SCANNER_WARNINGS + 1))
  fi
  rm -f "$log_file"
}

if (( RUN_SCANNERS )); then
  echo
  echo "Optional scanner stage"
  run_optional_scanner "Gitleaks" "gitleaks" "https://github.com/gitleaks/gitleaks" gitleaks detect --no-git --source . --redact
  run_optional_scanner "Trivy" "trivy" "https://trivy.dev/" trivy fs .
  run_optional_scanner "Semgrep" "semgrep" "https://semgrep.dev/" semgrep --config auto .

  if [[ -f package-lock.json || -f package.json ]]; then
    run_optional_scanner "npm audit" "npm" "https://docs.npmjs.com/cli/v10/commands/npm-audit" npm audit --audit-level=high
  fi

  if [[ -f pnpm-lock.yaml ]]; then
    run_optional_scanner "pnpm audit" "pnpm" "https://pnpm.io/cli/audit" pnpm audit
  fi

  if [[ -f requirements.txt || -f pyproject.toml ]]; then
    run_optional_scanner "pip-audit" "pip-audit" "https://pypi.org/project/pip-audit/" pip-audit
  fi

  if [[ -f Cargo.lock ]]; then
    run_optional_scanner "cargo audit" "cargo-audit" "https://github.com/RustSec/rustsec/tree/main/cargo-audit" cargo audit
  fi

  if (( SCANNER_RELEVANT == 0 )); then
    warn "No optional scanner targets detected for this repository"
    SCANNER_SCORE=10
  else
    SCANNER_SCORE=$((5 + (SCANNER_SUCCESS * 20 / SCANNER_RELEVANT)))
    if (( SCANNER_SCORE > 25 )); then
      SCANNER_SCORE=25
    fi
  fi
else
  SCANNER_SCORE=10
fi

TOTAL_SCORE=$((STRUCTURE_SCORE + SAFETY_SCORE + SECRETS_SCORE + SCANNER_SCORE))

if (( FAIL > 0 )); then
  RESULT="FAIL"
elif (( WARN > 0 )); then
  RESULT="WARN"
else
  RESULT="PASS"
fi

echo
printf 'VIBE CHECK SCORE: %d/100\n' "$TOTAL_SCORE"
printf '%s\n' 'Breakdown:'
printf -- '- Structure: %d/25\n' "$STRUCTURE_SCORE"
printf -- '- Safety files: %d/25\n' "$SAFETY_SCORE"
printf -- '- Secrets hygiene: %d/25\n' "$SECRETS_SCORE"
printf -- '- Optional scanners: %d/25\n' "$SCANNER_SCORE"

echo
printf 'Result: %s\n' "$RESULT"
printf 'Status: PASS=%d WARN=%d FAIL=%d\n' "$PASS" "$WARN" "$FAIL"
printf '%s\n' 'This is a readiness signal, not a security certification.'

echo "Next recommended files to add or review:"
if (( ${#RECOMMENDED[@]} == 0 )); then
  echo "- none"
else
  printf -- '- %s\n' "${RECOMMENDED[@]}"
fi

if (( STRICT )); then
  if (( FAIL > 0 )); then
    exit 2
  fi
  if (( WARN > 0 )); then
    exit 1
  fi
  exit 0
fi

if (( FAIL > 0 )); then
  exit 1
fi

exit 0
