#!/usr/bin/env bash
set -euo pipefail

MODE=""

usage() {
  cat <<'USAGE'
Usage:
  bash scripts/extract-prompt.sh --mode starter
  bash scripts/extract-prompt.sh --mode hardening
  bash scripts/extract-prompt.sh --mode security
  bash scripts/extract-prompt.sh --mode token-aware-discovery
  bash scripts/extract-prompt.sh --mode independent-review
  bash scripts/extract-prompt.sh --mode testing
  bash scripts/extract-prompt.sh --help
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode)
      MODE="${2:-}"
      shift 2
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
  usage
  exit 2
fi

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
ROOT=$(cd "$SCRIPT_DIR/.." && pwd)
TARGET="$ROOT/prompts/modules/$MODE.md"

if [[ ! -f "$TARGET" ]]; then
  echo "Unknown prompt module: $MODE" >&2
  usage >&2
  exit 2
fi

cat "$TARGET"
