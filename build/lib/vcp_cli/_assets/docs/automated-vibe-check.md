# Automated Vibe Check

`vibe-check` is a lightweight readiness check for repository structure, project memory,
env hygiene and obvious workflow gaps.

It is not a security certification.

## Modes

```bash
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
bash scripts/vibe-check.sh --audit --strict
bash scripts/vibe-check.sh --audit --json
bash scripts/vibe-check.sh --audit --scanners
bash scripts/vibe-check.sh --doctor
bash scripts/vibe-check.sh --doctor --json
bash scripts/vibe-check.sh --init-report
bash scripts/vibe-check.sh --init-report --json
bash scripts/vibe-check.sh --help
```

## What it checks

- route-specific structure files;
- AI instruction files and Memory Bank references;
- `.gitignore` and env baseline;
- obvious secret-like patterns;
- optional scanner availability;
- checksum manifest coverage for public helper scripts when `SHA256SUMS` exists;
- artifact version marker visibility for copy-ready templates;
- content quality warnings for key files that exist but still look empty.

## Doctor mode

Use `--doctor` when you want a quick toolkit and environment diagnosis.
It reports versions, key files, tool availability, optional scanner availability and a suggested route.

## Init report mode

Use `--init-report` when you want a route suggestion without changing files.
It reports detected files, stack hints, copy-first suggestions and the first command to run.

## Example audit JSON

```json
{
  "score": 86,
  "core_score": 86,
  "scanner_bonus": 0,
  "placeholder_excluded": 12,
  "artifact_version_warnings": 2,
  "content_quality_warnings": 3,
  "scanner_status": "not_fully_available",
  "status": "warn",
  "pass": 12,
  "warn": 3,
  "fail": 0,
  "mode": "audit",
  "strict": false
}
```

## How to read it

- `core_score` is the readiness signal;
- `scanner_bonus` is optional and separate;
- `placeholder_excluded` helps you notice when the placeholder filter may be hiding noise;
- `artifact_version_warnings` shows where copied artifacts may need review;
- `content_quality_warnings` shows where files exist but still need meaningful content;
- `WARN` means attention is needed but does not fail by default;
- `FAIL` means the project should be fixed before merge or deploy;
- `--strict` turns warnings into a failing exit code.

## Review-first install note

If you use public helper scripts from this repository:
- download them first;
- verify `SHA256SUMS` when available;
- review the file before running it.

Keep pipe-to-bash only for empty or test repositories.

## Self-dogfooding CI

The canonical self-dogfooding workflow in this repository is:
- `.github/workflows/vibe-check.yml`

It runs toolkit checks, version consistency, newline validation,
script tests and the runnable `todo-app-starter` test.

## Changed files guardrail

Default threshold: 15 files.

For large planned PRs, set repository variable:

`MAX_CHANGED_FILES=30`

Docs-only PRs warn instead of failing.
