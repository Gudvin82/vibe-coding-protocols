# Public Proof Demo

Repository package: `v0.9.4`

Это 2-минутный public proof artifact для evaluators, которым нужно быстро увидеть практическую ценность.

## Сценарий

Есть raw AI-generated MVP. VCP превращает его в:
- route;
- risk backlog;
- adoption plan;
- PR Gate recommendation;
- metrics board;
- launch decision;
- trust-check result.

## Артефакты

- `examples/public-proof/before-raw-ai-mvp.md`
- `examples/public-proof/after-vcp-launch-control-package.md`
- `examples/public-proof/route-example.json`
- `examples/public-proof/risk-backlog-example.json`
- `examples/public-proof/pr-gate-example.json`
- `examples/public-proof/metrics-board-example.json`
- `examples/public-proof/launch-decision-example.md`
- `examples/public-proof/trust-check-example.json`

## Важная пометка

Этот demo synthetic, если какой-то файл явно не говорит иное.


## How to reproduce the demo

- run `python3 -m vcp_cli trust-check --json`
- run `python3 -m vcp_cli benchmark run --json`
- run `python3 -m vcp_cli evaluator receipt --json`
- inspect `examples/public-proof/`

This demo is synthetic where explicitly labeled and is not a fake real-world adoption claim.
