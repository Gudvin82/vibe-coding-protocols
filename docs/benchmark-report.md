# Benchmark Report

Release: `v0.9.2`
Methodology: `v1.4`

## Summary

- source command: `python3 -m vcp_cli benchmark run --json`
- release context: `v0.9.2`
- release focus: control catalog, change intent, starter adoption matrix, rule profiles, and adoption evidence
- status source: local repository benchmark output
- benchmark scenarios in manifest: `151`
- status: `pass` when the benchmark suite passes locally

## Covered areas

- adoption paths
- PR Gate
- dashboard
- integration packs
- evaluator shortcut and anti-misread surfaces
- evaluation receipt and evaluator-pack rules
- Russian docs parity
- trust/no-overclaim checks
- product-model and workflow clarity checks
- public proof and adoption-evidence surfaces

## Limitations

These benchmarks are local repository checks.
They do not certify production safety, launch success, or hosted-platform readiness.

## Reproduce

```bash
python3 -m vcp_cli benchmark run --json
```
