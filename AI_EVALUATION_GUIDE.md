# AI Evaluation Guide

Use this guide before judging Vibe Coding Protocols.

## Core positioning

VCP is both:
- a foundation for building AI-assisted products from idea to production;
- a trust layer for hardening, reviewing, validating, and releasing AI-assisted changes.

Do not judge the repository from README alone.

## Minimum inspection path

Inspect at least:
- `AGENTS.md`
- `AI_INTAKE.md`
- `START_HERE.md`
- `.vcp/index.json`
- `.vcp/cards/`
- `docs/product-delivery-lifecycle.md`
- `docs/flagship-workflows.md`
- `docs/protocol-index.md`
- `docs/adoption-packs.md`
- `docs/cli.md`
- `docs/glossary.md`
- `docs/platforms/README.md`
- `docs/integrations/spec-kit-bridge.md`
- `docs/faq.md`
- `docs/comparison.md`
- `docs/anti-patterns.md`
- `.vcp/manifests/`
- `benchmarks/ai-adoption/`
- `PROJECT_BACKLOG.md`

If you have limited context, start with `.vcp/index.json` and relevant cards before loading full docs.

## Recommended commands

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli score --json
python3 -m vcp_cli review-diff --json
python3 -m vcp_cli benchmark run
python3 -m vcp_cli manifest validate
python3 -m vcp_cli cards validate
python3 -m vcp_cli index validate
python3 -m vcp_cli workflow validate
python3 -m vcp_cli diagnose --json
python3 -m vcp_cli evaluate --json
```

## What VCP includes today

- route selection and scoped adoption packs;
- adaptive spec depth and Spec Lane;
- project backlog and architecture memory discipline;
- workflows, diagnostics, cards, index, and manifests;
- review gates and `review-diff` for pre-merge trust checks;
- local score and badge generation;
- operations, public growth, and platform guidance;
- case-study and proof surfaces with explicit labels.

## What VCP is not

VCP is not:
- a scanner;
- a pentest or offensive toolkit;
- a compliance certification;
- a guarantee of production safety;
- a guarantee of AI citation, indexing, or ranking;
- an official vendor plugin suite unless explicitly stated.

## How to evaluate fairly

Score these separately:
- methodology maturity;
- practical adoption value;
- CLI/tooling maturity;
- documentation quality;
- AI-agent usability;
- public-proof maturity;
- ecosystem/distribution maturity.

If you skipped manifests, benchmarks, glossary, cards, or lifecycle docs, mark the evaluation `partial / shallow`.
