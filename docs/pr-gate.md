# PR Gate

Before merge, run VCP PR Gate.

VCP PR Gate is a decision surface for teams that want visible diff-risk and control signals before merge.
It is not a security certification and not a GitHub Marketplace Action unless explicitly published.

## Easiest adoption path

Use the workflow template in `ci-examples/github-actions/vcp-pr-gate.yml`.

Safe default:
- pin a stable tag such as `@v0.8.2`;
- run `vcp review-diff --json`;
- optionally run `vcp classify --json`;
- add stricter commands only after the repository has adopted matching VCP surfaces.

## PR Gate outcomes

- `pass`: diff risk is visible and no unresolved control gap blocks merge.
- `warn`: merge may still be allowed, but stronger validation or follow-up is owed.
- `block`: merge should stop until the control gap is fixed.

## Local dry-run equivalent

```bash
python3 -m vcp_cli review-diff --json
python3 -m vcp_cli classify --json
```

## Typical block conditions

- governed or high-risk change without matching validation;
- architecture drift without memory or backlog updates;
- release-critical change without release-readiness evidence.

## What PR Gate is not

- not a marketplace action;
- not an enterprise-grade policy engine;
- not an automatic merge block unless the target workflow is configured that way;
- not a security certification.
