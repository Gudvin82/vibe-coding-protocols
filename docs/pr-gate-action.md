# PR Gate Workflow Template

`v0.8.0` makes PR Gate easier to adopt through a workflow template first.

This release does not claim a GitHub Marketplace Action and does not require a composite action.

## Recommended template

Use:

- `ci-examples/github-actions/vcp-pr-gate.yml`

## What it does

The workflow template:
- checks out the caller repository;
- installs VCP from a pinned Git tag;
- runs `vcp review-diff --json`;
- optionally runs `vcp classify --json`;
- leaves fail-on behavior explicit.

## Why template first

For `v0.8.0`, a workflow template is safer than a composite action because it avoids checkout ambiguity between:
- the caller repository;
- the VCP source used for installation.

## Stability guidance

- use a tag such as `@v0.8.0` for stable adoption;
- use `main` only for experiments;
- treat the workflow as decision support, not certification.
