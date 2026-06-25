# Evaluator Architecture Map

Repository package: `v0.9.4`

Use this map when you need a quick structural reading of VCP.

## Flow Map

```text
Raw AI MVP / Existing Project
        |
        v
onboard -> classify -> workflow plan
        |
        v
adopt plan -> PR Gate -> metrics board
        |
        v
dashboard -> launch decision -> trust-check
        |
        v
proof / benchmark / external evaluation
```

## Layered Map

```text
Core:
  CLI, version surfaces, trust-check, benchmark, manifests, tests

Guided Paths:
  10-minute path, MVP-to-Launch, spec-driven adoption, SaaS hardening

Optional Layers:
  dashboard, project memory, audit backlog, run history, integration packs, agent templates

Roadmap-only:
  hosted dashboard, VS Code extension, marketplace, PyPI/npm publication if not actually done
```

## Read Next

- `EVALUATE_THIS_REPO.md`
- `docs/product-model.md`
- `docs/killer-workflow.md`
- `docs/proof-snapshot.md`

## Visual layer

- [Control-layer diagram](../assets/diagrams/vcp-control-layer-map.svg)
- [Evaluator token budget](./evaluator-token-budget.md)
