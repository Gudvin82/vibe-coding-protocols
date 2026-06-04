# GitHub Action and PR Gate

VCP ships:
- a real repository workflow in `.github/workflows/vibe-check.yml`;
- a reusable workflow example in `ci-examples/github-actions/vcp-pr-gate.yml`;
- a PyPI publishing scaffold in `.github/workflows/publish-pypi.yml`.

These are workflow files, not a GitHub Marketplace Action claim.

## Recommended PR Gate workflow template

Use `ci-examples/github-actions/vcp-pr-gate.yml` for external repositories.

The template:
- checks out the caller repository;
- installs VCP from a pinned Git tag;
- runs `vcp review-diff --json`;
- optionally runs `vcp classify --json`;
- keeps failure behavior explicit.

## Safe default for other repositories

For a repository that has not fully adopted VCP assets yet, keep PR Gate narrow:

```bash
vcp review-diff --json
vcp classify --json
```

Add stronger commands only after the repository has adopted matching VCP surfaces.

## Why this matters

VCP is more trustworthy when the same diff-risk and release-control checks run in CI before merge, not only in chat or local development.

## Related docs

- `docs/pr-gate.md`
- `docs/pr-gate-action.md`
- `ci-examples/github-actions/vcp-pr-gate.yml`
- `.github/workflows/vibe-check.yml`
