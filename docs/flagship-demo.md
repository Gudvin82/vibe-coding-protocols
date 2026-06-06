# Flagship Demo

<!-- vcp-version: v0.9.1 -->
<!-- methodology-version: v1.4 -->

The flagship demo is the canonical 10-minute story for VCP:

`raw AI MVP -> classify -> change intent -> adoption plan -> PR Gate -> trust-check -> dashboard -> launch decision`

This demo is synthetic but realistic. It does not contain secrets, real customers, or production claims.

## Files
- `examples/flagship-demo/00-raw-ai-mvp.md`
- `examples/flagship-demo/02-classification.json`
- `examples/flagship-demo/03-change-intent.json`
- `examples/flagship-demo/04-control-charter.md`
- `examples/flagship-demo/05-adoption-plan.json`
- `examples/flagship-demo/06-work-package.json`
- `examples/flagship-demo/07-pr-gate.json`
- `examples/flagship-demo/08-trust-check.json`
- `examples/flagship-demo/09-dashboard-summary.md`
- `examples/flagship-demo/10-launch-decision.md`
- `examples/flagship-demo/11-evaluation-receipt.json`

## Command sequence

```bash
python3 -m vcp_cli trust-check --json
python3 -m vcp_cli catalog explain --id mvp-to-launch --json
python3 -m vcp_cli change intent validate examples/flagship-demo/03-change-intent.json --json
python3 -m vcp_cli charter validate .vcp/project-control-charter.example.json --json
python3 -m vcp_cli evaluator receipt validate examples/flagship-demo/11-evaluation-receipt.json --json
python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json
```
