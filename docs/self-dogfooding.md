# Self-Dogfooding

This repository should pass its own checks.

## Required local checks

- `bash scripts/check-toolkit.sh`
- `bash scripts/check-version-consistency.sh`
- `bash scripts/check-ide-rules-consistency.sh`
- `python3 scripts/check-newlines.py`
- `bash scripts/scan-placeholders.sh`
- `python3 scripts/validate-links.sh`
- `bash scripts/vibe-check.sh --audit --json`
- `bash scripts/tests/test-vibe-check-basic.sh`
- `npm test --prefix examples/todo-app-starter`

## What PASS means

PASS means repository hygiene is acceptable.

It does not mean:
- guaranteed security;
- production certification;
- no bugs;
- no legal or compliance risk.

## Expected warnings

These warnings are expected in this public repository unless the underlying state changes:
- `API_KEY` marker in git history;
- `SECRET` marker in git history;
- public root `AGENTS.md`;
- optional scanners not installed locally.

## Release gate

Before every release:
1. Run all checks.
2. Confirm `VERSION` consistency.
3. Run the newline checker.
4. Run script tests.
5. Confirm no fake metrics, fake case study or guaranteed security claims.
6. Confirm release notes exist.
7. Confirm the tag points to the final commit.
8. Inspect `git remote -v` and confirm you are releasing from the toolkit repository intentionally.
