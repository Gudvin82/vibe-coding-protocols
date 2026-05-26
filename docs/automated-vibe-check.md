# Automated Vibe Check

`vibe-check` is a lightweight repository check with layered signals.

It does not replace the Hardening Protocol, human review, scanners or
security work.

![Automated Vibe Check example output](../assets/vibe-check-output.png)

This image is a demo-style terminal mockup that shows the kind of
signal the check produces. It is not presented as a real project scan
or a security verdict.

## What it checks

- baseline project structure;
- mode-specific starter / hardening / audit files;
- `.gitignore` presence and a few high-value ignore patterns;
- `.env` / `.env.*` files in the repository;
- whether `.env.example` or a documented baseline exists when env-like references appear;
- suspicious secret-like assignments in a quick grep-style pass;
- secret-like prefixes such as `sk-`, `ghp_`, `github_pat_`, `AKIA`, JWT-like tokens and password-bearing connection strings;
- soft lockfile checks for JavaScript and Python dependency manifests;
- public-safety warnings for root docs in webroot-style contexts;
- optional scanners if `--scanners` is requested and tools are already installed.

## What it does not check

- application correctness;
- test quality;
- dependency vulnerability status;
- security scanner findings;
- real production readiness;
- legal, privacy or payment compliance;
- real open ports, WAF, DDoS controls or infrastructure state.
- it does not convert scanner output into a security certification.

## Modes

```bash
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
bash scripts/vibe-check.sh --audit --strict
bash scripts/vibe-check.sh --audit --json
bash scripts/vibe-check.sh --audit --scanners || true
bash scripts/vibe-check.sh --scanners
bash scripts/vibe-check.sh --help
```

If `--scanners` is passed without a mode, audit mode is assumed.

## Example output

```text
$ bash scripts/vibe-check.sh --hardening
PASS: README.md present
PASS: .gitignore present
PASS: AI instructions file present
PASS: SECURITY_OPERATIONS_BASELINE reference present
WARN: Suspicious secret-like assignment detected; review and remove or mask it
WARN: Gitleaks not found; see docs/scanner-integration.md

SUMMARY: 4 pass, 2 warn, 0 fail
VIBE CHECK SCORE: 82/100
Breakdown:
- Structure: 25/25
- Safety files: 20/25
- Secrets hygiene: 20/25
- Optional scanners: 17/25
This is a readiness signal, not a security certification.
```

## How to use locally before AI-generated changes

1. Copy `scripts/vibe-check.sh` into your repository.
2. Run `--starter` before the first AI-generated vertical slice.
3. Run `--hardening` before merge or pre-deploy review on existing code.
4. Use the warnings to fill in missing project memory and audit files before the next AI iteration.
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

The GitHub workflow in this repository checks the toolkit itself, not
arbitrary target applications.

## How to interpret PASS / WARN / FAIL

- `PASS`: the basic file and workflow expectations are present.
- `WARN`: the repository is usable, but there are missing artifacts or public-safety concerns to review. In CI, warnings should stay visible but not fail the workflow on their own.
- `FAIL`: a baseline structural condition is missing, for example no `README.md`, no `.gitignore` or a real `.env` file is present. Fails should return a non-zero exit code.

## Exit codes

- default mode:
  - `FAIL` -> exit `1`
  - `WARN` -> exit `0`
- strict mode:
  - `WARN` -> exit `1`
  - `FAIL` -> exit `2`

## Optional scanner integration

If external tools are already installed, `--scanners` can call them and fold the result into the score.

See:
- [scanner-integration.md](./scanner-integration.md)

## Where to start

- New project: run `bash scripts/vibe-check.sh --starter`
  after adding `README.md`, `AGENTS.md` or `CLAUDE.md`, and `PROJECT_MAP.md`.
- Existing AI-generated code: run `bash scripts/vibe-check.sh --hardening`
  before a wider audit or pre-merge review.
- Audit-focused pass: run `bash scripts/vibe-check.sh --audit`
  when you mainly want to confirm audit structure and missing baseline docs.
