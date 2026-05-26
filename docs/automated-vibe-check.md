# Automated Vibe Check

`vibe-check` is a lightweight repository check.

It does not replace the Hardening Protocol, human review, scanners or
security work.

![Automated Vibe Check example output](../assets/vibe-check-output.png)

This image is a demo-style terminal mockup that shows the kind of
signal the check produces. It is not presented as a real project scan
or a security verdict.

## What it checks

- presence of baseline project files;
- missing `README.md`, `AGENTS.md`, `PROJECT_MAP.md` or
  `AUDIT_BACKLOG.md` depending on mode;
- whether `.env.example` is expected;
- whether `.env` appears in the repository;
- whether `.gitignore` exists;
- whether architecture or project-map docs may need review in a public
  webroot context;
- whether `SECURITY_OPERATIONS_BASELINE.md` is referenced for hardening/audit work;
- whether `THIRD_PARTY_REGISTRY.md` is referenced for hardening/audit work;
- whether obvious backup, dump or log artifacts exist near the repository root.

## What it does not check

- application correctness;
- test quality;
- dependency vulnerability status;
- security scanner findings;
- real production readiness;
- legal, privacy or payment compliance;
- real open ports, WAF, DDoS controls or infrastructure state.

## Modes

```bash
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
```

## Example output

```text
$ bash scripts/vibe-check.sh --hardening
PASS: README.md present
PASS: .gitignore present
PASS: AI instructions file present
PASS: SECURITY_OPERATIONS_BASELINE reference present
WARN: AUDIT_BACKLOG.md is missing for hardening mode
WARN: public root AGENTS.md exists; make sure public docs are sanitized

Result: WARN
Summary: PASS=4 WARN=2 FAIL=0
Next recommended files to add or review:
- AUDIT_BACKLOG.md
```

## How to use locally before AI-generated changes

1. Copy `scripts/vibe-check.sh` into your repository.
2. Run `--starter` before the first AI-generated vertical slice.
3. Run `--hardening` before merge or pre-deploy review on existing code.
4. Use the warnings to fill in missing project memory and audit files before the next AI iteration.

## How to use in CI

Add it as a lightweight workflow gate for structure and obvious workflow gaps:

```bash
bash scripts/vibe-check.sh --starter
bash scripts/vibe-check.sh --hardening
bash scripts/vibe-check.sh --audit
```

The GitHub workflow in this repository checks the toolkit itself, not
arbitrary target applications.

## How to interpret PASS / WARN / FAIL

- `PASS`: the basic file and workflow expectations are present.
- `WARN`: the repository is usable, but there are missing artifacts or public-safety concerns to review. In CI, warnings should stay visible but not fail the workflow on their own.
- `FAIL`: a baseline structural condition is missing, for example no `README.md`, no `.gitignore` or a real `.env` file is present. Fails should return a non-zero exit code.

## Where to start

- New project: run `bash scripts/vibe-check.sh --starter`
  after adding `README.md`, `AGENTS.md` or `CLAUDE.md`, and `PROJECT_MAP.md`.
- Existing AI-generated code: run `bash scripts/vibe-check.sh --hardening`
  before a wider audit or pre-merge review.
- Audit-focused pass: run `bash scripts/vibe-check.sh --audit`
  when you mainly want to confirm audit structure and missing baseline docs.
