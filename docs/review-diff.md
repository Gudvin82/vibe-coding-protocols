# Review Diff

`vcp review-diff` is a local pre-merge helper for AI-assisted changes.

It looks at the current git diff, classifies impacted areas, estimates risk, suggests the likely spec depth, and points to repo artifacts that may need an update before merge or release.

It does not:

- edit files;
- approve a merge;
- replace human review;
- make network calls.

## Commands

```bash
python3 -m vcp_cli review-diff
python3 -m vcp_cli review-diff --base main --head HEAD
python3 -m vcp_cli review-diff --json
```

## What it checks

- changed files;
- impacted areas:
  - docs
  - CLI
  - templates
  - protocols
  - manifests
  - workflows
  - cards
  - tests
  - public growth
- basic path and keyword risk signals;
- whether related repo artifacts may need follow-up.

## Typical follow-up artifacts

- `PROJECT_BACKLOG.md`
- `PROJECT_MAP.md`
- `templates/ARCHITECTURE_SOURCE_OF_TRUTH.md`
- `AUDIT_BACKLOG.md`
- `templates/THIRD_PARTY_REGISTRY.md`
- release notes
- manifests / cards / index

## Why this exists

VCP is more useful when it can help before merge, not only at intake time. `review-diff` gives a small local trust gate that helps decide whether a change can stay on the no-spec path or needs more discipline before release.
