# GitHub Action and PR Gate

VCP ships workflow files and workflow templates.
It does not claim a GitHub Marketplace Action.

## Current surfaces

- repository workflow: `.github/workflows/vibe-check.yml`
- PyPI publish scaffold: `.github/workflows/publish-pypi.yml`
- reusable adoption template: `ci-examples/github-actions/vcp-pr-gate.yml`

## Recommended PR Gate template

Use `ci-examples/github-actions/vcp-pr-gate.yml` for external repositories.

Expected outputs:
- `review-diff` JSON;
- optional `classify` JSON;
- explicit pass/warn/block interpretation managed by the caller repository.

## Warn vs fail guidance

- `pass`: proceed normally;
- `warn`: repository can merge if maintainers choose, but follow-up is owed;
- `block`: stop until the control gap is fixed.

## Local equivalent

```bash
python3 -m vcp_cli review-diff --json
python3 -m vcp_cli classify --json
```

## What is not claimed

- marketplace action;
- automatic merge blocking everywhere;
- certification or security guarantee.
