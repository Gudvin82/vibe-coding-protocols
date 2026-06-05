# Release Readiness

Release Readiness is the top-level check before calling a repository slice ready for release.

It is not a production safety guarantee.

## Output

- `pass`
- `warn`
- `block`

## Checks

- version surfaces are consistent;
- README and README_ru parity passes;
- public source-of-truth checker passes;
- review-diff has been reviewed;
- diagnostics are clear or accepted;
- cards, index, and manifests validate;
- benchmarks pass;
- architecture memory is updated;
- backlog is updated;
- third-party changes were reviewed;
- score was generated;
- PR Gate passed or accepted risk is recorded;
- release notes exist;
- manual GitHub Release checklist exists.

## When to block

- version surfaces disagree;
- release notes are missing;
- production-critical changes have no PR Gate or rollback note;
- architecture memory is stale and ignored;
- validation evidence is missing for risky changes.

## Related files

- `templates/reports/release-readiness-report.md`
- `docs/pr-gate.md`
- `docs/architecture-drift.md`
- `docs/public-source-of-truth-audit.md`
- `python3 -m vcp_cli release-check --json`
