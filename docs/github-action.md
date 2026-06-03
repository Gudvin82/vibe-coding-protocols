# GitHub Action and PR Gate

VCP already ships a real repository workflow in `.github/workflows/vibe-check.yml`.

This repository also includes a reusable CI example at `ci-examples/github-actions/vcp-check.yml`.
It is a GitHub Actions workflow example, not a GitHub Marketplace Action.

## PR Gate positioning

Use VCP Check before merge to surface route, risk, validation, and score signals.
This is a decision surface, not a security certification.

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

## Recommended command set

```bash
python3 scripts/validate-links.sh
bash scripts/check-version-consistency.sh
python3 scripts/check-public-version-surfaces.py
python3 -m vcp_cli manifest validate
python3 -m vcp_cli cards validate
python3 -m vcp_cli index validate
python3 -m vcp_cli workflow validate
python3 -m vcp_cli benchmark run
python3 -m vcp_cli diagnose --json
python3 -m vcp_cli score --json
python3 -m vcp_cli review-diff --json
```

## Why this matters

VCP is more trustworthy when the same repo-level checks run in CI before merge, not only in chat or local development.

## Related docs

- `docs/pr-gate.md`
- `ci-examples/github-actions/vcp-check.yml`
- `.github/workflows/vibe-check.yml`
