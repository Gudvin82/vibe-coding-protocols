#!/usr/bin/env bash
set -euo pipefail

MODE=""
STRICT=0
RUN_SCANNERS=0
JSON_MODE=0
PASS=0
WARN=0
FAIL=0
STRUCTURE_SCORE=0
SAFETY_SCORE=0
SECRETS_SCORE=0
SCANNER_BONUS=0
SCANNER_RELEVANT=0
SCANNER_SUCCESS=0
SCANNER_WARNINGS=0
CORE_SCORE=0
SCANNER_STATUS="not_requested"
RECOMMENDED=()

PLACEHOLDER_RX='example|placeholder|changeme|your_|dummy|test|\[FILL IN|<[^>]+>|masked-example-not-real|not-real|sample'

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/vibe-check.sh --starter
  bash scripts/vibe-check.sh --hardening
  bash scripts/vibe-check.sh --audit
  bash scripts/vibe-check.sh --strict
  bash scripts/vibe-check.sh --scanners
  bash scripts/vibe-check.sh --json
  bash scripts/vibe-check.sh --help

Examples:
  bash scripts/vibe-check.sh --starter
  bash scripts/vibe-check.sh --hardening --json
  bash scripts/vibe-check.sh --audit --strict
  bash scripts/vibe-check.sh --audit --scanners

Exit codes:
  0  PASS or WARN in default mode
  1  FAIL, or WARN in --strict mode
  2  Script/runtime error

See:
  docs/vibe-check-scoring.md
USAGE
}

log_line() {
  if (( JSON_MODE == 0 )); then
    echo "$1"
  fi
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
  PASS=$((PASS + 1))
  log_line "PASS: $1"
}

warn() {
  WARN=$((WARN + 1))
  log_line "WARN: $1"
}

fail() {
  FAIL=$((FAIL + 1))
  log_line "FAIL: $1"
}

run_check() {
  local level="$1"
  local message="$2"
  local points="$3"
  local bucket="${4:-}"

  case "$level" in
    pass)
      pass "$message"
      case "$bucket" in
        structure) STRUCTURE_SCORE=$((STRUCTURE_SCORE + points)) ;;
        safety) SAFETY_SCORE=$((SAFETY_SCORE + points)) ;;
        secrets) SECRETS_SCORE=$((SECRETS_SCORE + points)) ;;
      esac
      ;;
    warn)
      warn "$message"
      ;;
    fail)
      fail "$message"
      ;;
    *)
      echo "Unknown check level: $level" >&2
      exit 2
      ;;
  esac
}

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

pattern_hit_count() {
  local regex="$1"
  local output
  output=$(rg -n --hidden \
    --glob '!.git/*' \
    --glob '!node_modules/*' \
    --glob '!dist/*' \
    --glob '!build/*' \
    --glob '!coverage/*' \
    --glob '!scripts/vibe-check.sh' \
    --glob '!examples/todo-app-starter/.env.example' \
    "$regex" . 2>/dev/null \
    | grep -viE "$PLACEHOLDER_RX" || true)
  printf '%s\n' "$output" | sed '/^$/d' | wc -l | tr -d ' '
}

pattern_hit_files() {
  local regex="$1"
  local output
  output=$(rg -n --hidden \
    --glob '!.git/*' \
    --glob '!node_modules/*' \
    --glob '!dist/*' \
    --glob '!build/*' \
    --glob '!coverage/*' \
    --glob '!scripts/vibe-check.sh' \
    --glob '!examples/todo-app-starter/.env.example' \
    "$regex" . 2>/dev/null \
    | grep -viE "$PLACEHOLDER_RX" || true)
  printf '%s\n' "$output" \
    | sed '/^$/d' \
    | cut -d: -f1 \
    | sort -u \
    | paste -sd ', ' -
}

scan_secret_pattern() {
  local label="$1"
  local regex="$2"
  local hits
  hits=$(pattern_hit_count "$regex")
  if [[ "$hits" != "0" ]]; then
    local files
    files=$(pattern_hit_files "$regex")
    if (( STRICT )); then
      run_check fail "Suspicious $label pattern found in: $files" 0 secrets
    else
      run_check warn "Suspicious $label pattern found in: $files" 0 secrets
    fi
  fi
}

run_optional_scanner() {
  local label="$1"
  local install_hint="$2"
  shift 2
  SCANNER_RELEVANT=$((SCANNER_RELEVANT + 1))
  if command -v "$1" >/dev/null 2>&1; then
    if "$@" >/dev/null 2>&1; then
      SCANNER_SUCCESS=$((SCANNER_SUCCESS + 1))
      pass "$label completed"
    else
      SCANNER_WARNINGS=$((SCANNER_WARNINGS + 1))
      warn "$label reported findings or returned a non-zero status"
    fi
  else
    SCANNER_WARNINGS=$((SCANNER_WARNINGS + 1))
    warn "$label not found. See docs/scanner-integration.md. Install hint: $install_hint"
  fi
}

history_pattern_warning() {
  local label="$1"
  local needle="$2"
  if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    return 0
  fi
  if git log --all --full-history -S "$needle" --format='%H' -- . >/dev/null 2>&1; then
    local count
    count=$(git log --all --full-history -S "$needle" --format='%H' -- . 2>/dev/null | sed '/^$/d' | wc -l | tr -d ' ')
    if [[ "$count" != "0" ]]; then
      warn "$label appeared in git history. Review and rotate if the value was ever real."
    fi
  fi
}

for arg in "$@"; do
  case "$arg" in
    --starter|--hardening|--audit)
      if [[ -n "$MODE" ]]; then
        usage
        exit 2
      fi
      MODE="$arg"
      ;;
    --strict)
      STRICT=1
      ;;
    --scanners)
      RUN_SCANNERS=1
      ;;
    --json)
      JSON_MODE=1
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
done

if [[ -z "$MODE" ]]; then
  if (( STRICT || RUN_SCANNERS || JSON_MODE )); then
    MODE="--audit"
  else
    usage
    exit 2
  fi
fi

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
  run_check warn "PROJECT_MAP not found" 0 structure
  add_recommended "PROJECT_MAP.md"
fi

case "$MODE" in
  --starter)
    if project_has_any_file \
      prompts/product-brief-prompt.md \
      prompts/product-brief-prompt_en.md \
      docs/product-brief-prompt.md; then
      run_check pass "Starter prompt reference present" 5 structure
    else
      run_check warn "Starter prompt reference not found" 0 structure
      add_recommended "prompts/product-brief-prompt_en.md"
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

env_ref_regex='process\.env|ENV\[|os\.getenv|dotenv|DATABASE_URL|'\
'API_KEY|TOKEN|SECRET|PASSWORD|OPENAI_API_KEY|'\
'ANTHROPIC_API_KEY|BOT_TOKEN|TELEGRAM_BOT_TOKEN'
if rg -n --hidden --glob '!.git/*' --glob '!node_modules/*' --glob '!dist/*' --glob '!build/*' "$env_ref_regex" . >/dev/null 2>&1; then
  if project_has_any_file .env.example .env.local.example .env.production.example examples/todo-app-starter/.env.example; then
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
  if project_has_any_file \
    SECURITY_OPERATIONS_BASELINE.md \
    templates/SECURITY_OPERATIONS_BASELINE.md \
    && project_has_any_file \
      THIRD_PARTY_REGISTRY.md \
      templates/THIRD_PARTY_REGISTRY.md; then
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

if project_has_file package.json; then
  if project_has_any_file package-lock.json pnpm-lock.yaml yarn.lock bun.lockb; then
    run_check pass "JavaScript lockfile present" 5 safety
  else
    run_check warn "package.json present without package-lock.json, pnpm-lock.yaml, yarn.lock or bun.lockb" 0 safety
  fi
fi

if project_has_any_file requirements.txt pyproject.toml; then
  if project_has_any_file poetry.lock uv.lock requirements.lock.txt; then
    run_check pass "Python dependency lock or pinned export present" 5 safety
  else
    run_check warn "Python dependency manifest present without poetry.lock, uv.lock or requirements.lock.txt" 0 safety
  fi
fi

# Level 2b: secrets hygiene
real_env_files=$(
  find . -maxdepth 4 -type f \
    \( -name '.env' -o -name '.env.*' \) \
    ! -name '.env.example' \
    ! -name '.env.*.example' \
    | sed '/^$/d' || true
)
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

scan_secret_pattern 'OpenAI key prefix' 'sk-[A-Za-z0-9]{12,}'
scan_secret_pattern 'OpenAI project key prefix' 'sk-proj-[A-Za-z0-9_-]{12,}'
scan_secret_pattern 'GitHub personal access token' 'ghp_[A-Za-z0-9]{20,}'
scan_secret_pattern 'GitHub fine-grained token' 'github_pat_[A-Za-z0-9_]{20,}'
scan_secret_pattern 'AWS access key' 'AKIA[0-9A-Z]{12,}'
scan_secret_pattern 'JWT-like token' 'eyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9._-]{8,}\.[A-Za-z0-9._-]{8,}'
scan_secret_pattern 'postgres connection string with password' 'postgres(ql)?://[^:@/[:space:]]+:[^@/[:space:]]+@'
scan_secret_pattern 'mongodb connection string with password' 'mongodb\+srv://[^:@/[:space:]]+:[^@/[:space:]]+@'
scan_secret_pattern 'redis connection string with password' 'redis://[^:@/[:space:]]+:[^@/[:space:]]+@'
scan_secret_pattern 'private key block' 'BEGIN PRIVATE KEY'
scan_secret_pattern 'OPENAI_API_KEY assignment' 'OPENAI_API_KEY\s*[:=]'
scan_secret_pattern 'ANTHROPIC_API_KEY assignment' 'ANTHROPIC_API_KEY\s*[:=]'
scan_secret_pattern 'BOT_TOKEN assignment' 'BOT_TOKEN\s*[:=]'
scan_secret_pattern 'TELEGRAM_BOT_TOKEN assignment' 'TELEGRAM_BOT_TOKEN\s*[:=]'
scan_secret_pattern 'generic secret-like assignment' '(API_KEY|TOKEN|SECRET|PASSWORD|PRIVATE_KEY|DATABASE_URL)\s*[:=]'

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  if git log --all --full-history --format='%H' -- '*.env' 2>/dev/null | sed '/^$/d' | head -1 >/dev/null; then
    if [[ -n "$(git log --all --full-history --format='%H' -- '*.env' 2>/dev/null | sed '/^$/d' | head -1)" ]]; then
      warn ".env appeared in git history. Review whether any historical secret needs rotation."
    fi
  fi
  history_pattern_warning 'API_KEY marker' 'API_KEY'
  history_pattern_warning 'SECRET marker' 'SECRET'
fi

if (( FAIL == 0 )) && (( WARN == 0 )); then
  run_check pass "No suspicious secret-like assignments detected in quick scan" 10 secrets
fi

for public_doc in ARCHITECTURE.md PROJECT_MAP.md AGENTS.md; do
  if [[ -f "$public_doc" ]]; then
    warn "Public root $public_doc exists; make sure public docs are sanitized"
  fi
done

# Level 3: optional scanner integration
if (( RUN_SCANNERS )); then
  if project_has_any_file package.json package-lock.json; then
    run_optional_scanner 'npm audit' 'npm audit --audit-level=high' npm audit --audit-level=high
  fi

  if project_has_file pnpm-lock.yaml; then
    run_optional_scanner 'pnpm audit' 'pnpm audit' pnpm audit
  fi

  if project_has_any_file requirements.txt pyproject.toml; then
    run_optional_scanner 'pip-audit' 'pip install pip-audit' pip-audit
  fi

  if project_has_file Cargo.lock; then
    run_optional_scanner 'cargo audit' 'cargo install cargo-audit' cargo audit
  fi

  run_optional_scanner \
    'gitleaks detect --no-git' \
    'brew install gitleaks or https://github.com/gitleaks/gitleaks' \
    gitleaks detect --no-git
  run_optional_scanner \
    'trufflehog filesystem .' \
    'brew install trufflehog or https://github.com/trufflesecurity/trufflehog' \
    trufflehog filesystem .
  run_optional_scanner \
    'trivy fs .' \
    'brew install trivy or https://github.com/aquasecurity/trivy' \
    trivy fs .
  run_optional_scanner \
    'semgrep --config auto' \
    'brew install semgrep or https://semgrep.dev/docs/getting-started/' \
    semgrep --config auto
fi

if (( RUN_SCANNERS == 0 )); then
  SCANNER_STATUS="not_requested"
  SCANNER_BONUS=0
else
  if (( SCANNER_RELEVANT == 0 )); then
    SCANNER_STATUS="not_applicable"
    SCANNER_BONUS=0
  else
    if (( SCANNER_SUCCESS == SCANNER_RELEVANT )); then
      SCANNER_STATUS="available"
    elif (( SCANNER_SUCCESS > 0 )); then
      SCANNER_STATUS="partially_available"
    else
      SCANNER_STATUS="not_fully_available"
    fi
    SCANNER_BONUS=$(( (SCANNER_SUCCESS * 10) / SCANNER_RELEVANT ))
  fi
fi

CORE_SCORE=$(( ((STRUCTURE_SCORE + SAFETY_SCORE + SECRETS_SCORE) * 100) / 75 ))

STATUS="pass"
EXIT_CODE=0
if (( FAIL > 0 )); then
  STATUS="fail"
  EXIT_CODE=1
elif (( WARN > 0 )); then
  STATUS="warn"
  if (( STRICT )); then
    EXIT_CODE=1
  fi
fi

if (( JSON_MODE )); then
  mode_name=${MODE#--}
  strict_value=false
  if (( STRICT )); then
    strict_value=true
  fi
  printf '{\n'
  printf '  "score": %s,\n' "$CORE_SCORE"
  printf '  "core_score": %s,\n' "$CORE_SCORE"
  printf '  "scanner_bonus": %s,\n' "$SCANNER_BONUS"
  printf '  "scanner_status": "%s",\n' "$SCANNER_STATUS"
  printf '  "status": "%s",\n' "$STATUS"
  printf '  "pass": %s,\n' "$PASS"
  printf '  "warn": %s,\n' "$WARN"
  printf '  "fail": %s,\n' "$FAIL"
  printf '  "mode": "%s",\n' "$mode_name"
  printf '  "strict": %s\n' "$strict_value"
  printf '}\n'
else
  log_line "SUMMARY: $PASS pass, $WARN warn, $FAIL fail"
  log_line "VIBE CHECK CORE SCORE: $CORE_SCORE/100"
  if [[ "$SCANNER_STATUS" == "available" ]]; then
    log_line "OPTIONAL SCANNERS: available"
  elif [[ "$SCANNER_STATUS" == "partially_available" ]]; then
    log_line "OPTIONAL SCANNERS: partially available"
  elif [[ "$SCANNER_STATUS" == "not_applicable" ]]; then
    log_line "OPTIONAL SCANNERS: not applicable"
  elif [[ "$SCANNER_STATUS" == "not_requested" ]]; then
    log_line "OPTIONAL SCANNERS: not requested"
  else
    log_line "OPTIONAL SCANNERS: not fully available"
  fi
  log_line "SCANNER BONUS: $SCANNER_BONUS/10"
  log_line "Breakdown:"
  log_line "- Structure: $STRUCTURE_SCORE/25"
  log_line "- Safety files: $SAFETY_SCORE/25"
  log_line "- Secrets hygiene: $SECRETS_SCORE/25"
  log_line "This is a readiness signal, not a security certification."
  if (( ${#RECOMMENDED[@]} > 0 )); then
    log_line "Recommended next artifacts: ${RECOMMENDED[*]}"
  fi
fi

exit "$EXIT_CODE"
