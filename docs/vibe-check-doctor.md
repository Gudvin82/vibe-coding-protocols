# Vibe-Check Doctor

Use `--doctor` when you want a quick toolkit and environment diagnosis.

```bash
bash scripts/vibe-check.sh --doctor
bash scripts/vibe-check.sh --doctor --json
```

## What it reports

- toolkit version and methodology version;
- whether this is a git repository;
- remote origin for safety review;
- whether `SHA256SUMS` exists;
- whether key onboarding files exist;
- whether `bash`, `git`, `python3`, `node` and `npm` are available;
- whether optional scanners are available;
- a recommended route based on the current files.

## Remote safety note

If `remote origin` still points to the source toolkit or template repository,
confirm that you are not editing the wrong repository before setup, push, PR or deploy.

## What it does not do

- it does not change files;
- it does not run optional scanners;
- it does not certify security or production readiness.
