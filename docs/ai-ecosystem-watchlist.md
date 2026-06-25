# AI Ecosystem Watchlist

Repository package: `v0.9.5`

VCP uses this watchlist as a governance surface for reviewing external AI tools,
models, developer tooling, training resources, and ecosystem references.

VCP does not ship these external tools.
It does not claim official integration, endorsement, maintenance, or bundled
support.

## Why this exists

Teams evaluating AI tools often jump from a trending repo directly into a pilot.
The watchlist creates a slower, safer path:

1. classify the tool;
2. note why it matters;
3. capture license and reuse notes;
4. record maturity and risk;
5. map it to a VCP review path;
6. decide `watch`, `candidate`, `approved-for-demo`,
   `approved-for-client-review`, `blocked`, or `roadmap-only`.

## What already existed

Before `v0.9.5`, VCP already had:
- [Ecosystem Map](./ecosystem-map.md) for positioning VCP inside the broader AI tooling landscape;
- [AI Tooling](./ai-tooling.md) for practical coexistence with AI coding tools;
- [Integration Proof Matrix](./integrations/proof-matrix.md) for shipped copy-ready kit evidence;
- [Current Limitations](./current-limitations.md) and [Scope Boundary](./scope-boundary.md) for no-overclaim boundaries.

This watchlist extends those surfaces.
It does not replace them.

## Review statuses

- `watch`: relevant enough to keep observing.
- `candidate`: worth a scoped review or internal note.
- `approved-for-demo`: acceptable for sandbox/demo evaluation.
- `approved-for-client-review`: acceptable to discuss or prototype with a client.
- `blocked`: not acceptable without deeper changes or evidence.
- `roadmap-only`: acknowledged, but not currently adopted.

## Categories

- agent tooling
- RAG
- vector DB
- inference/deployment
- UI/demo
- evaluation
- security
- MLOps
- local models
- documentation
- developer training

## Recommended VCP review path

Use this watchlist together with:
- [Model / Tool Governance](./model-tool-governance.md)
- [AI Stack Adoption Checklist](./ai-stack-adoption-checklist.md)
- [Ecosystem Scouting Workflow](./ecosystem-scouting-workflow.md)
- [Evidence Bundle](./evidence-bundle.md)
- [Current Limitations](./current-limitations.md)

## Suggested workflow

```text
discover
→ classify
→ license/risk review
→ demo suitability
→ VCP route mapping
→ approved / watch / blocked / roadmap-only
```

## Reference types used in this release

Typical references for watchlist entries include:
- curated open-source AI catalogs;
- Hugging Face ecosystem references;
- GitHub Secure Code Game style training references;
- GitHub-native security/control references;
- local AI stack discussions;
- ecosystem scouting feeds;
- developer education resources.

## Important boundary

The watchlist is not:
- a giant AI catalog;
- a model registry;
- a hosted scouting service;
- a GitHub trending clone;
- a Hugging Face clone.

It is a governance review surface for teams adopting external AI components.
