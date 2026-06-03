# GitHub Action and PR Gate

VCP already ships a real repository workflow in `.github/workflows/vibe-check.yml`.

This repository also includes a reusable CI example at `ci-examples/github-actions/vcp-check.yml`.
It is an example, not a GitHub Marketplace Action.

## What the gate should run

- version consistency;
- link validation;
- toolkit check;
- manifest validate;
- benchmark run;
- cards validate;
- index validate;
- workflow validate;
- diagnose;
- score;
- review-diff when a diff exists.

## Example command set

```bash
python3 scripts/validate-links.sh
bash scripts/check-version-consistency.sh
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
