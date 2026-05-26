#!/usr/bin/env bash
set -euo pipefail

MODE="${1:-}"
PASS=0
WARN=0
FAIL=0

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

case "$MODE" in
  --starter|--hardening|--audit) ;;
  *)
    echo "Usage: bash scripts/vibe-check.sh --starter|--hardening|--audit"
    exit 1
    ;;
esac

if [[ -f README.md ]]; then
  pass "README.md present"
else
  fail "README.md missing"
fi

if [[ -f .gitignore ]]; then
  pass ".gitignore present"
else
  fail ".gitignore missing"
fi

if [[ -f AGENTS.md || -f CLAUDE.md ]]; then
  pass "AI instructions file present"
else
  fail "Missing AGENTS.md or CLAUDE.md"
fi

if [[ -f PROJECT_MAP.md || -f templates/PROJECT_MAP.md ]]; then
  pass "PROJECT_MAP reference present"
else
  if [[ "$MODE" == "--starter" ]]; then
    warn "PROJECT_MAP not found in current directory"
  else
    warn "PROJECT_MAP not found"
  fi
fi

if [[ "$MODE" == "--hardening" || "$MODE" == "--audit" ]]; then
  if [[ -f AUDIT_BACKLOG.md || -f templates/AUDIT_BACKLOG.md ]]; then
    pass "AUDIT_BACKLOG reference present"
  else
    warn "AUDIT_BACKLOG not found"
  fi

  if [[ -f SECURITY_OPERATIONS_BASELINE.md || -f templates/SECURITY_OPERATIONS_BASELINE.md ]]; then
    pass "SECURITY_OPERATIONS_BASELINE reference present"
  else
    warn "SECURITY_OPERATIONS_BASELINE not found"
  fi

  if [[ -f THIRD_PARTY_REGISTRY.md || -f templates/THIRD_PARTY_REGISTRY.md ]]; then
    pass "THIRD_PARTY_REGISTRY reference present"
  else
    warn "THIRD_PARTY_REGISTRY not found"
  fi
fi

if rg -n --hidden   --glob '!*.git/*'   --glob '!.github/*'   '(process\.env|ENV\[|os\.getenv|dotenv|DATABASE_URL|API_KEY|TOKEN)'   . >/dev/null 2>&1; then
  if [[ -f .env.example || -f templates/SECURITY_BASELINE.md ]]; then
    pass "env-related reference has companion example or baseline"
  else
    warn "Env-like patterns found without .env.example"
  fi
else
  pass "No env-like patterns detected in quick scan"
fi

if find . -maxdepth 2 -name '.env' | grep -q .; then
  fail "Real .env file found in repository"
else
  pass "No .env file found"
fi

suspicious_artifacts=$(find . -maxdepth 2 \( -name 'backup.zip' -o -name 'dump.sql' -o -name '*.log' \) -print | sed '/^$/d' || true)
if [[ -n "$suspicious_artifacts" ]]; then
  warn "Possible public exposure artifacts found near repository root"
fi

for public_doc in ARCHITECTURE.md PROJECT_MAP.md AGENTS.md; do
  if [[ -f "$public_doc" ]]; then
    warn "$public_doc exists at repository root; check whether this is appropriate for a public repo or webroot context"
  fi
done

echo
if (( FAIL > 0 )); then
  RESULT="FAIL"
elif (( WARN > 0 )); then
  RESULT="WARN"
else
  RESULT="PASS"
fi

echo "Result: $RESULT"
echo "Summary: PASS=$PASS WARN=$WARN FAIL=$FAIL"

echo "Next recommended files to add or review:"
[[ ! -f README.md ]] && echo "- README.md"
[[ ! -f .gitignore ]] && echo "- .gitignore"
[[ ! -f AGENTS.md && ! -f CLAUDE.md ]] && echo "- AGENTS.md or CLAUDE.md"
[[ ! -f PROJECT_MAP.md && ! -f templates/PROJECT_MAP.md ]] && echo "- PROJECT_MAP.md"
if [[ "$MODE" == "--hardening" || "$MODE" == "--audit" ]]; then
  [[ ! -f AUDIT_BACKLOG.md && ! -f templates/AUDIT_BACKLOG.md ]] && echo "- AUDIT_BACKLOG.md"
  [[ ! -f SECURITY_OPERATIONS_BASELINE.md && ! -f templates/SECURITY_OPERATIONS_BASELINE.md ]] && echo "- SECURITY_OPERATIONS_BASELINE.md"
  [[ ! -f THIRD_PARTY_REGISTRY.md && ! -f templates/THIRD_PARTY_REGISTRY.md ]] && echo "- THIRD_PARTY_REGISTRY.md"
fi

if (( FAIL > 0 )); then
  exit 1
fi

exit 0
