# Public Proof Demo

Repository package: `v0.9.5`

This is the 2-minute public proof artifact for evaluators who need to see practical value quickly.

## Scenario

A raw AI-generated MVP exists. VCP turns it into:
- route;
- risk backlog;
- adoption plan;
- PR Gate recommendation;
- metrics board;
- launch decision;
- trust-check result.

## Artifacts

- `examples/public-proof/before-raw-ai-mvp.md`
- `examples/public-proof/after-vcp-launch-control-package.md`
- `examples/public-proof/route-example.json`
- `examples/public-proof/risk-backlog-example.json`
- `examples/public-proof/pr-gate-example.json`
- `examples/public-proof/metrics-board-example.json`
- `examples/public-proof/launch-decision-example.md`
- `examples/public-proof/trust-check-example.json`

## Important label

This demo is synthetic unless a file explicitly says otherwise.


## How to reproduce the demo

- run `python3 -m vcp_cli trust-check --json`
- run `python3 -m vcp_cli benchmark run --json`
- run `python3 -m vcp_cli evaluator receipt --json`
- inspect `examples/public-proof/`

This demo is synthetic where explicitly labeled and is not a fake real-world adoption claim.
