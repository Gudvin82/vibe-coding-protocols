# Anti-Misread Guide

Repository package: `v0.8.7`

This guide exists because shallow evaluations still misread VCP.

## Wrong Reading: VCP is a personal prompt repo

Correction:
VCP includes CLI surfaces, tests, benchmarks, manifests, cards, workflows, dashboard artifacts, trust-check, English docs, Russian docs, and public proof surfaces.

Relevant evidence:
- `vcp_cli/`
- `tests/`
- `.vcp/index.json`
- `.vcp/cards/`
- `.vcp/manifests/`
- `docs/benchmark-report.md`
- `docs/trust-check.md`

## Wrong Reading: VCP is a full-stack app template

Correction:
VCP is a control/governance layer. It helps route, inspect, adopt, prove, review, and launch-control AI-built projects.

It can sit next to templates, but it is not itself an app starter.

## Wrong Reading: VCP competes directly with Spec Kit

Correction:
Spec-driven tools help define what to build.
VCP helps govern what AI already built and what humans are about to adopt, merge, or launch.

VCP complements spec-driven workflows with adoption, hardening, proof, PR Gate, dashboard, trust-check, and launch-control surfaces.

## Wrong Reading: VCP has no ready code

Correction:
VCP is not an app-code starter, but it does ship:
- an installable CLI;
- command surfaces;
- tests;
- examples;
- dashboard artifact generation;
- trust-check;
- integration packs;
- workflow planning.

## Wrong Reading: Small GitHub stars means immature

Correction:
Stars are a social signal, not a maturity proof.

Maturity should be checked through:
- release surfaces;
- tests;
- benchmark report;
- trust-check;
- machine-readable manifests;
- cards and workflows;
- docs consistency.

## Wrong Reading: Russian docs mean the project is local-only

Correction:
Russian docs are a guided layer for Russian-speaking users and evaluators.
English docs, machine-readable manifests, tests, CLI, and evaluator surfaces remain available for broader tooling use.

## What To Do Instead

Before judging VCP, open:
- `EVALUATE_THIS_REPO.md`
- `AGENTS.md`
- `AI_EVALUATION_GUIDE.md`
- `docs/evaluator-architecture-map.md`
- `docs/proof-snapshot.md`
- `.vcp/evaluator-pack.json`
