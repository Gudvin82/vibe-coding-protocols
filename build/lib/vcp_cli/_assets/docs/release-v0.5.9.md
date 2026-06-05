# Vibe Coding Protocols v0.5.9 — Spec Lane, Workflows, Diagnostics, Catalog UX, and Event Schema

`v0.5.9` adds five VCP-native layers: a Spec Lane for turning ideas into PRD, feature specs, acceptance criteria and tasks; workflow definitions for repeatable AI-assisted delivery flows; layer-by-layer diagnostics; catalog filters and maturity labels over VCP Cards; and a normalized event schema for review findings, production errors, backlog changes and release gates.

## Added in `v0.5.9`

- Spec-first route and adoption pack.
- `protocols/spec-driven/` for PRD/spec/task flow and change control.
- `templates/specs/` for PRD, feature spec, acceptance criteria, tasks, review, and changelog artifacts.
- `vcp spec` CLI helpers for template output, validation, review, and summary.
- `.vcp/workflows/` plus `vcp workflow` for local workflow discovery and validation.
- `.vcp/diagnostics/` plus `vcp diagnose` for project/process readiness checks by layer.
- `.vcp/catalog.json`, card maturity labels, recommended markers, platform badges, and filter-aware `vcp cards list`.
- `schemas/vcp-event.schema.json` and event-entry template for normalized finding records.
- Benchmark scenarios for spec-first routing, workflow selection, diagnostics, catalog filters, and event-schema review findings.

## What `v0.5.9` does not claim

`v0.5.9` does **not** claim:

- external spec-tool compatibility;
- workflow automation platform behavior;
- production mutation from workflow commands;
- network diagnostics or censorship tooling;
- SIEM / IDS / IPS compatibility;
- copied external catalogs, brands, or claims.

## Suggested validation

```bash
python3 -m vcp_cli spec validate --json
python3 -m vcp_cli workflow validate --json
python3 -m vcp_cli diagnose --profile production --json
python3 -m vcp_cli cards list --recommended --json
python3 -m vcp_cli benchmark run
```
