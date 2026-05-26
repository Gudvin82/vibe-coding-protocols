# Safe Update Workflow

## Why `pull latest && deploy` is unsafe

Blind updates hide change scope, provenance, install hooks, breaking changes and rollback risk.

## Safe update process

1. Check upstream source and maintainer.
2. Review changelog, release notes and known issues.
3. Pin version, tag or commit.
4. Verify checksum or signature if available.
5. Run scanners and dependency review.
6. Run tests.
7. Deploy to staging.
8. Use canary or limited rollout where applicable.
9. Keep rollback plan ready.
10. Update `THIRD_PARTY_REGISTRY.md`.

## Emergency patch path

When a critical issue must be patched quickly:
- record why it is urgent;
- document source and version;
- reduce scope to the minimal safe patch;
- keep rollback owner and rollback point explicit;
- add a follow-up review if a full check was skipped.

## What to log in `AUDIT_BACKLOG.md`

- what changed;
- why it changed;
- what checks were run;
- what checks were skipped;
- risks accepted;
- rollback owner;
- next review date.

Related docs:
- [scanner-integration.md](./scanner-integration.md)
- [hardening-thresholds.md](./hardening-thresholds.md)
