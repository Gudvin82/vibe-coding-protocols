# PR Gate

Before merge, run VCP Check.

VCP PR Gate is one of the main adoption paths for teams that already have a repository and want trust signals before merge.

It is a decision surface, not a security certification.
It is also not a GitHub Marketplace Action unless that is explicitly published.

Treat it as a pre-merge visibility layer: route, risk, validation, and score become explicit before a human decides whether to merge.

## What PR Gate does

- checks current version and public source-of-truth surfaces;
- validates links, cards, index, manifests, and benchmarks;
- runs `review-diff` as a pre-merge trust helper;
- produces score and readiness signals;
- makes route, risk, and validation visible before merge.

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
      - uses: actions/setup-python@v5
        with:
          python-version: "3.x"
      - run: bash scripts/check-version-consistency.sh
      - run: python3 scripts/validate-links.sh
      - run: python3 -m vcp_cli manifest validate
      - run: python3 -m vcp_cli cards validate
      - run: python3 -m vcp_cli index validate
      - run: python3 -m vcp_cli benchmark run
      - run: python3 -m vcp_cli review-diff --json
      - run: python3 -m vcp_cli score --json
```

## What teams can tune

- strictness of failure conditions;
- when to block merge vs warn;
- which routes or packs are required;
- whether score badge output is published in README or PR summaries.

## Related files

- `docs/github-action.md`
- `ci-examples/github-actions/vcp-check.yml`
- `.github/workflows/vibe-check.yml`
- `templates/reports/pr-gate-report.md`
