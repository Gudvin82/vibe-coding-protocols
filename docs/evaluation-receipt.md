# Evaluation Receipt

Repository package: `v0.9.0`

An evaluation receipt makes it explicit what an AI or human reviewer actually inspected before making claims about VCP.

## Required fields

- evaluator name or tool;
- evaluation date;
- repository version;
- inspection depth: Level 0, Level 1, Level 2, or Level 3;
- files inspected;
- commands run;
- files not inspected;
- whether `.vcp/evaluator-pack.json` was read;
- whether `EVALUATE_THIS_REPO.md` was read;
- whether `vcp_cli/` was inspected;
- whether `tests/` were inspected;
- whether trust-check was run;
- whether benchmark was run;
- confidence level;
- claim status: `shallow overview`, `partial evaluation`, or `full evaluation`;
- score;
- limitations.

## Full-evaluation rule

If the evaluator did not inspect all of the following, they must not call the review full:
- `EVALUATE_THIS_REPO.md`
- `.vcp/evaluator-pack.json`
- `vcp_cli/`
- `tests/`
- `docs/benchmark-report.md`
- `docs/trust-check.md`

## Why this matters

Some browser and IDE AIs still over-weight stars, under-weight proof/CLI surfaces, and stop at README or repo summaries. The receipt makes skipped layers visible instead of hidden.

## Use

- template: `templates/reports/evaluation-receipt.md`
- schema: `schemas/evaluation-receipt.schema.json`
- example: `.vcp/evaluation-receipt.example.json`
- CLI: `python3 -m vcp_cli evaluator receipt --json`
