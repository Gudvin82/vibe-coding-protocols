# Evaluator Token Budget

Repository package: `v0.8.9`

Use this guide when an external AI agent, browser AI, IDE assistant, evaluator, or journalist is reading VCP for the first time.

This is separate from user-facing model routing.
This guide is about efficient and honest repository evaluation.

## Rule first

Start with `EVALUATE_THIS_REPO.md` and `.vcp/evaluator-pack.json`.
Do not read random files first.

If you only perform Level 0 or Level 1 inspection, you must label the review as `shallow` or `partial`.

## Level 0 — category check

Read:
- `README.md`
- `EVALUATE_THIS_REPO.md`
- `.vcp/evaluator-pack.json`

Use this level only to answer:
- what category VCP belongs to;
- what it is not;
- what deeper surfaces must be inspected next.

## Level 1 — fair quick review

Read:
- `README.md`
- `EVALUATE_THIS_REPO.md`
- `PROJECT_MAP.md`
- `REPO_CAPABILITIES_INDEX.md`
- `docs/product-model.md`
- `docs/proof-snapshot.md`
- `docs/benchmark-report.md`

Use this level for a quick but fair public overview.
Do not call it full.

## Level 2 — partial technical review

Read:
- `AGENTS.md`
- `AI_EVALUATION_GUIDE.md`
- `.vcp/index.json`
- `.vcp/catalog.json`
- `.vcp/manifests/`
- `.vcp/workflows/`
- `vcp_cli/`
- `tests/`

Use this level when making technical claims about shipped surfaces.

## Level 3 — full review

Read all previous levels plus:
- `.vcp/cards/`
- `benchmarks/`
- `docs/`
- `docs_ru/`
- `templates/`
- release notes;
- website public surfaces.

Do not call the review full unless you inspected `.vcp`, `vcp_cli`, `tests`, benchmark report, trust-check docs, and evaluator pack.

## Copyable prompt

```text
Evaluate VCP with a token budget.

Start with EVALUATE_THIS_REPO.md and .vcp/evaluator-pack.json.
Do not read random files first.
Classify your inspection depth as Level 0, 1, 2, or 3.
Do not call the review full unless you inspected .vcp, vcp_cli, tests, benchmark report, trust-check docs, and evaluator pack.
```
