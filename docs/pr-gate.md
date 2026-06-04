# PR Gate

Before merge, run VCP PR Gate.

VCP PR Gate is one of the main adoption paths for teams that already have a repository and want trust signals before merge.

It is a decision surface, not a security certification.
It is also not a GitHub Marketplace Action unless that is explicitly published.

## Easiest adoption path

Use the workflow template in `ci-examples/github-actions/vcp-pr-gate.yml`.

The safe default for general repositories is:
- install VCP from a pinned Git tag;
- run `vcp review-diff --json`;
- optionally run `vcp classify --json`;
- add stricter VCP commands only after the repository has adopted matching VCP surfaces.

## PR Gate outcomes

- `pass`: diff risk is visible and no unresolved control gap blocks merge.
- `warn`: merge may still be allowed, but the repository owes follow-up work or stronger validation evidence.
- `block`: merge should stop until the control gap is fixed.

## Typical block conditions

- `review-diff` shows high-risk or governed work without matching validation.
- architecture drift is visible but project memory and backlog were not updated.
- release-critical change has no PR Gate note, no rollback note, or no release-readiness evidence.
- VCP-managed repo surfaces are red after VCP has been adopted into that repository.

## Pin stable versions

For adoption in another repository, prefer a pinned tag such as `@v0.8.1`.
Use `main` only for experiments.

## Fail-on behavior

The workflow template documents simple modes:
- fail on `block`;
- fail on `warn`;
- never fail, report only.

Choose the strictness that matches your repository maturity.

## Related files

- `docs/github-action.md`
- `docs/pr-gate-action.md`
- `docs/release-readiness.md`
- `docs/architecture-drift.md`
- `ci-examples/github-actions/vcp-pr-gate.yml`
- `.github/workflows/vibe-check.yml`
- `templates/reports/pr-gate-report.md`
