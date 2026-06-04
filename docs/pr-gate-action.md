# PR Gate Workflow Template

`v0.8.2` keeps PR Gate as a workflow template path, not a marketplace action claim.

## Recommended template

Use:
- `ci-examples/github-actions/vcp-pr-gate.yml`

## Copy-paste path

1. copy the workflow into `.github/workflows/` in the target repository;
2. pin a stable tag such as `@v0.8.2`;
3. start with `vcp review-diff --json`;
4. add `vcp classify --json` only if the repository benefits from route output too;
5. choose whether `warn` should fail the workflow or only annotate review.

## Expected outputs

- JSON diff-risk output from `review-diff`;
- optional route and tier context from `classify`;
- a workflow artifact if the target repository enables artifact upload.

## Local dry-run equivalent

```bash
python3 -m vcp_cli review-diff --json
python3 -m vcp_cli classify --json
```

## Limitations

- not a GitHub Marketplace Action;
- not an enterprise policy engine;
- not a security certification;
- does not auto-block merges unless the caller workflow is configured to do that.

## Optional artifact upload

If the caller repository already uploads CI artifacts, attach the JSON outputs from `review-diff` or `classify` there.
`v0.8.2` does not add a special artifact service of its own.
