# PR Gate

Before merge, run VCP Check.

VCP PR Gate is one of the main adoption paths for teams that already have a repository and want trust signals before merge.

It is a decision surface, not a security certification.
It is also not a GitHub Marketplace Action unless that is explicitly published.

Treat it as a pre-merge visibility layer: route, risk, validation, score, and release-control signals become explicit before a human decides whether to merge.

## PR Gate outcomes

- `pass`: checks are green, risk is understood, and no unresolved control gap blocks merge.
- `warn`: merge might still be allowed, but the repository owes follow-up work, accepted risk, or tighter validation evidence.
- `block`: merge should stop until the control gap is fixed.

## Typical block conditions

- `review-diff` shows high-risk or governed work without matching validation.
- architecture drift is visible but project memory and backlog were not updated.
- release-critical change has no PR Gate note, no rollback note, or no release-readiness evidence.
- version, cards, index, manifests, or benchmark validation are red.

## Minimal PR Gate

```yaml
name: VCP Check

on:
  pull_request:
  push:
    branches: [main]

jobs:
  vcp:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v6
        with:
          python-version: "3.x"
      - uses: actions/setup-node@v6
        with:
          node-version: "20"
      - run: bash scripts/check-version-consistency.sh
      - run: python3 scripts/check-public-version-surfaces.py
      - run: python3 scripts/check-readme-parity.py
      - run: python3 -m vcp_cli manifest validate
      - run: python3 -m vcp_cli cards validate
      - run: python3 -m vcp_cli index validate
      - run: python3 -m vcp_cli benchmark run
      - run: python3 -m vcp_cli review-diff --json
      - run: python3 -m vcp_cli release-check --json
      - run: python3 -m vcp_cli score --json
```

## Decision model

Use PR Gate to answer three questions before merge:

1. Did we understand the risk of the active diff?
2. Did we run the right validation for that risk?
3. Did we leave the repository more controlled, not less controlled?

If the answer to any of these is no, PR Gate should at least warn and often block.

## Related files

- `docs/github-action.md`
- `docs/release-readiness.md`
- `docs/architecture-drift.md`
- `docs/protocol-pack-security.md`
- `ci-examples/github-actions/vcp-check.yml`
- `.github/workflows/vibe-check.yml`
- `templates/reports/pr-gate-report.md`
