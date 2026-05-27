# Vibe-Check Scoring

`vibe-check` separates core readiness from optional scanner signal.

The score is a readiness signal, not a security certification.

| Category | Points | What it means |
|---|---:|---|
| Structure | 25 | Required project files and route selection basics are present |
| Memory / docs | 20 | `AGENTS`, `PROJECT_MAP`, architecture docs and related project memory exist where needed |
| Safety files | 25 | `.gitignore`, env policy and audit-oriented baseline files exist |
| Secret hygiene | 20 | obvious leak prevention and quick secret-pattern checks |
| Validation | 10 | tests, checks or runbook-style validation evidence is present |
| Optional scanners | bonus | scanner signal, not part of the core readiness score |

## How to read the score

- `core_score` is the main readiness signal.
- `scanner_bonus` is optional extra signal.
- `placeholder_excluded` shows how many lines were filtered because they looked
  like obvious placeholders such as `example`, `changeme` or `[FILL IN]`.
- `WARN` means attention is required, but the default mode does not fail.
- `FAIL` means a baseline condition must be fixed before merge or deploy.
- `--strict` changes warning behavior and can turn warnings into a blocking exit.

## What the score does not mean

The score does not mean:
- the project is secure;
- the project is production-ready;
- the project passed a pentest;
- all secrets and dependency issues are covered.

Use the score to spot missing structure, memory, env hygiene and validation
signals early.

Use hardening docs, review and scanners for deeper work.
