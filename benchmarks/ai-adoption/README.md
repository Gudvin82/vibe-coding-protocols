# AI Adoption Benchmarks

Synthetic benchmark scenarios for local VCP route and adoption validation.

These scenarios do not call external AI models.
They validate that local routing, pack metadata and expected review-gate logic stay internally consistent.

Use:

```bash
python3 -m vcp_cli benchmark list
python3 -m vcp_cli benchmark run
python3 -m vcp_cli benchmark run --scenario shared-engine-production
python3 -m vcp_cli benchmark run --scenario third-party-api-intake
python3 -m vcp_cli benchmark run --scenario production-error-capture
python3 -m vcp_cli benchmark run --scenario project-backlog-update
python3 -m vcp_cli benchmark run --scenario repository-evaluation-full
python3 -m vcp_cli benchmark run --scenario repository-evaluation-shallow
```
