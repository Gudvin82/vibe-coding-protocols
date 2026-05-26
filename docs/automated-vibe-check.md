# Automated Vibe Check

`vibe-check` is a lightweight repository check with layered readiness signals.

It does not replace the Hardening Protocol, human review, real scanners or
security work.

![Automated Vibe Check example output](../assets/vibe-check-output.png)

This image is a demo-style terminal mockup. It is not a real project scan
and not a security verdict.

## What it checks

- baseline project structure;
- starter, hardening and audit route coverage;
- `.gitignore` presence and high-value ignore patterns;
- `.env` or `.env.*` files in the repository;
- whether `.env.example` or a documented baseline exists when env-like references appear;
- suspicious secret-like assignments in a quick grep-style pass;
- secret-like prefixes such as `sk-`, `ghp_`, `github_pat_`, `AKIA`, JWT-like tokens and password-bearing connection strings;
- soft git-history warnings for `.env`, `API_KEY` and `SECRET` markers when the repository is a git repo;
- soft lockfile checks for JavaScript and Python dependency manifests;
- optional scanners if `--scanners` is requested and tools are already installed.

## What it does not check

- application correctness;
- test quality;
- real production readiness;
- pentest depth;
- legal, privacy or payment compliance;
- infrastructure state;
- full dependency vulnerability status unless external tools are installed.

## Modes

```bash
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
bash scripts/vibe-check.sh --audit --strict
bash scripts/vibe-check.sh --audit --json
bash scripts/vibe-check.sh --audit --scanners || true
bash scripts/vibe-check.sh --help
```

If `--scanners` is passed without a mode, audit mode is assumed.

## Scoring model

`vibe-check` now separates core readiness from optional scanners.

- Core score: readiness checks for structure, safety files and secrets hygiene.
- Scanner bonus: optional extra signal when tools such as `gitleaks`, `trufflehog`, `trivy` or `semgrep` are already installed.

Missing scanners:
- produce warnings;
- do not fail default mode;
- do not remove a large part of the core score.

Example output:

```text
SUMMARY: 12 pass, 3 warn, 0 fail
VIBE CHECK CORE SCORE: 92/100
OPTIONAL SCANNERS: not fully available
SCANNER BONUS: 0/10
Breakdown:
- Structure: 25/25
- Safety files: 25/25
- Secrets hygiene: 20/25
This is a readiness signal, not a security certification.
```

Example JSON:

```json
{
  "score": 92,
  "core_score": 92,
  "scanner_bonus": 0,
  "scanner_status": "not_fully_available",
  "status": "warn",
  "pass": 12,
  "warn": 3,
  "fail": 0,
  "mode": "audit",
  "strict": false
}
```

## How to use locally

1. Copy `scripts/vibe-check.sh` into your repository.
2. Run `--starter` before the first AI-generated vertical slice.
3. Run `--hardening` before merge or pre-deploy review on existing code.
4. Use warnings to fill in missing project memory and audit files.
5. Use `--strict` when you want warnings to block a local or CI pass.
6. Use `--json` when another tool needs a machine-readable summary.

## How to use in CI

Add it as a lightweight workflow gate for structure and obvious workflow gaps:

```bash
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
bash scripts/vibe-check.sh --audit --scanners || true
```

The GitHub workflow in this repository checks the toolkit itself, not an
arbitrary target application.

## PASS / WARN / FAIL

- `PASS`: the basic file and workflow expectations are present.
- `WARN`: the repository is usable, but there are missing artifacts or public-safety concerns to review.
- `FAIL`: a baseline structural condition is missing or a real `.env`-like file exists in the repository.

## Exit codes

- default mode:
  - `PASS` or `WARN` -> exit `0`
  - `FAIL` -> exit `1`
- strict mode:
  - `WARN` -> exit `1`
  - `FAIL` -> exit `1`
- script or runtime error:
  - usage or runtime issue -> exit `2`

## Optional scanner integration

If external tools are already installed, `--scanners` can call them and report
an extra bonus signal.

See:
- [scanner-integration.md](./scanner-integration.md)

History checks are guidance signals, not proof of compromise by themselves.
If a real secret ever appeared in git history, rotate and revoke it rather than
only deleting the file.
