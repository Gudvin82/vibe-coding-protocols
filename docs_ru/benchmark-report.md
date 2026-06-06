# Benchmark Report

Release: `v0.8.9`
Methodology: `v1.4`

## Summary

- source command: `python3 -m vcp_cli benchmark run --json`
- release context: `v0.8.9`
- release focus: license clarity, evaluator path enforcement, public proof, and adoption evidence
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

Эти benchmarks — локальные repository checks.
Они не сертифицируют production safety, launch success или hosted-platform readiness.

## Reproduce

```bash
python3 -m vcp_cli benchmark run --json
```
