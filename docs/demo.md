# Demo Journeys

Use these local commands to show the product layer.

## Shared engine

```bash
python3 -m vcp_cli route --profile shared-engine
python3 -m vcp_cli adopt --pack shared-engine --dry-run
python3 -m vcp_cli review plan
python3 -m vcp_cli score
python3 -m vcp_cli benchmark run
```

## Third-party API intake

```bash
python3 -m vcp_cli route --profile third-party-api
python3 -m vcp_cli adopt --pack third-party-api --dry-run
python3 -m vcp_cli check --fast --json
python3 -m vcp_cli benchmark run --scenario third-party-api-intake
```

See also [demo-output.md](./demo-output.md).
