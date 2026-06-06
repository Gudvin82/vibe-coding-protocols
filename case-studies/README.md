# Case Studies

Repository package: `v0.9.0`

This directory holds adoption evidence and before/after project stories.

Rules:
- mark synthetic examples clearly as synthetic;
- do not imply real customer adoption unless the case is real and reviewable;
- include commands run, produced artifacts, prevented risks, and limitations.

Start with:
- `TEMPLATE.md`
- `synthetic-vcp-public-proof.md`


## How to reproduce the demo

- run `python3 -m vcp_cli trust-check --json`
- run `python3 -m vcp_cli benchmark run --json`
- run `python3 -m vcp_cli evaluator receipt --json`
- inspect `examples/public-proof/`

This demo is synthetic where explicitly labeled and is not a fake real-world adoption claim.
