# Benchmark Report

Release: v0.8.8
Methodology: v1.4

## Summary

- source command: `python3 -m vcp_cli benchmark run --json`
- release context: `v0.8.8`
- routing/docs additions in this release: cost-aware model routing, evaluator token budget, visual proof layer
- status source: local repository benchmark output
- scenarios: 140
- status: pass

## Covered areas

- adoption paths
- PR Gate
- dashboard
- integration packs
- evaluator shortcut and anti-misread surfaces
- Russian docs parity
- trust/no-overclaim checks
- agent behavior checks
- product-model and workflow clarity checks

## Limitations

These benchmarks are local repository checks.
They do not certify production safety, launch success, or hosted-platform readiness.

## Reproduce

```bash
python3 -m vcp_cli benchmark run --json
```
