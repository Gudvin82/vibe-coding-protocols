# Case Studies

Repository package: `v0.9.4`

VCP не заявляет broad public adoption без видимых доказательств. Case studies нужны, чтобы показать структуру evidence без выдумывания adopters.

## Текущие типы evidence

- synthetic examples;
- sanitized case packets;
- maintainer-known usage notes;
- template-only submission formats.

## С чего начать

- `case-studies/README.md`
- `case-studies/TEMPLATE.md`
- `case-studies/synthetic-vcp-public-proof.md`

## Правило

Synthetic examples должны оставаться явно synthetic.


## How to reproduce the demo

- run `python3 -m vcp_cli trust-check --json`
- run `python3 -m vcp_cli benchmark run --json`
- run `python3 -m vcp_cli evaluator receipt --json`
- inspect `examples/public-proof/`

This demo is synthetic where explicitly labeled and is not a fake real-world adoption claim.
