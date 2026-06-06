# Benchmark Report

Release: v0.8.7
Methodology: v1.4

## Summary

- source command: `python3 -m vcp_cli benchmark run --json`
- release context: `v0.8.7`
- status source: local repository benchmark output
- scenarios: 140
- status: pass

## Covered areas

- adoption paths
- PR Gate
- dashboard
- integration packs
- Russian docs parity
- trust/no-overclaim checks
- agent behavior checks
- product-model и workflow clarity checks

## Limitations

Эти benchmarks — локальные repository checks.
Они не сертифицируют production safety, launch success или hosted-platform readiness.

## Reproduce

```bash
python3 -m vcp_cli benchmark run --json
```
