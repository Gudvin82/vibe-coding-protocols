# CLI roadmap

Possible future helper:
- `vibe-init --starter`
- `vibe-init --hardening`
- `vibe-init --audit`

## What exists right now

- [scripts/init-minimal.sh](../scripts/init-minimal.sh) — minimal bootstrap helper
- it is intentionally not a full CLI;
- it is safe-by-default and review-first;
- it does not auto-commit, auto-push or install dependencies.

## Safety rules

- dry-run first;
- never overwrite without confirmation;
- no secrets;
- no auto-commit;
- no network scans;
- no production config changes.

## Possible implementation later

- Node.js package
- Python script
- current shell helper remains intentionally small for now
