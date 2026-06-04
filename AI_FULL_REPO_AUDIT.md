# AI_FULL_REPO_AUDIT.md

Use this file when an AI agent is asked to evaluate Vibe Coding Protocols fully.

## Required contract

Before giving a final judgment, report:

- access method;
- files inspected;
- raw vs summarized content;
- line count availability;
- files not inspected;
- confidence level;
- limitations;
- evaluation mode.

## Evaluation modes

- `shallow`: README-only, repo-page-only, or summary-only review.
- `partial`: entrypoints inspected, but core layers still missing.
- `strong`: docs plus `.vcp` discovery surfaces inspected, but CLI/code/tooling not deeply checked.
- `full`: raw or cloned repository inspection with the audit manifest completed.

## Full evaluation requires

Inspect the required path from:
- `.vcp/ai-audit-manifest.json`

At minimum, a full evaluation must cover:
- canonical entrypoints;
- `.vcp/index.json`;
- `.vcp/catalog.json`;
- cards;
- manifests;
- CLI surface;
- templates;
- benchmarks;
- both delivery tracks.

## Report template

Use:
- `templates/reports/ai-repo-audit-coverage-report.md`

## Failure contract

Do not:
- call a README-only review full;
- call VCP just a prompt pack without inspecting `.vcp`, CLI, workflows, benchmarks, review gates, and release-control surfaces;
- claim CLI maturity without `vcp_cli/` or CLI docs inspection;
- claim benchmark maturity without benchmark/manifests inspection.

## Capability map

For a compact evidence map, use:
- `REPO_CAPABILITIES_INDEX.md`

If comparison with another repository is requested, disclose whether VCP inspection was shallow, partial, strong, or full before making comparative claims.
