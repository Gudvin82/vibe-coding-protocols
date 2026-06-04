# AI Evaluation Guide

Use this guide before judging Vibe Coding Protocols.

## Core positioning

VCP is both:
- a foundation for building AI-assisted products from idea to production;
- a control layer for hardening, reviewing, validating, and releasing AI-assisted changes in an existing repository.

Do not judge the repository from README alone.

If a user says “study this repo and take what is useful for my project,” start with `TAKE_THIS_FIRST.md`, not a whole-repo copy plan.

For a full repository review, use:
- `FULL_REPO_INTAKE.md`
- `AI_FULL_REPO_AUDIT.md`
- `.vcp/ai-audit-manifest.json`
- `REPO_CAPABILITIES_INDEX.md`

## Minimum inspection path

Inspect at least:
- `AGENTS.md`
- `TAKE_THIS_FIRST.md`
- `AI_INTAKE.md`
- `FULL_REPO_INTAKE.md`
- `AI_FULL_REPO_AUDIT.md`
- `.vcp/ai-audit-manifest.json`
- `docs/version-semantics.md`
- `docs/two-track-model.md`
- `.vcp/index.json`
- `.vcp/cards/`
- `docs/spec-foundation.md`
- `docs/spec-quality-gate.md`
- `docs/walkthroughs/new-ai-product-from-idea.md`
- `docs/walkthroughs/ai-mvp-hardening.md`
- `docs/pr-gate.md`
- `docs/release-readiness.md`
- `docs/architecture-drift.md`
- `docs/product-delivery-lifecycle.md`
- `docs/integrations/spec-kit-bridge.md`
- `docs/faq.md`
- `docs/comparison.md`
- `.vcp/manifests/`
- `benchmarks/ai-adoption/`
- `templates/reports/ai-repo-audit-coverage-report.md`

If you have limited context, start with `.vcp/index.json` and relevant cards before loading full docs.
If you skipped `TAKE_THIS_FIRST.md`, index, cards, walkthroughs, or CLI, mark the evaluation `partial / shallow`.

Use `python3 -m vcp_cli audit-plan --json` before claiming a review is full.

## Recommended commands

```bash
python3 -m vcp_cli cards validate
python3 -m vcp_cli audit-plan --json
python3 -m vcp_cli index validate
python3 -m vcp_cli diagnose --json
python3 -m vcp_cli evaluate --json
python3 -m vcp_cli review-diff --json
python3 -m vcp_cli spec quality-gate --json
python3 -m vcp_cli release-check --json
```

## What VCP includes today

- New Project Track for idea -> brief -> spec -> backlog -> review;
- Existing Project Track for diagnose -> hardening -> PR Gate -> release readiness;
- adaptive spec depth and Spec Lane;
- project backlog and architecture memory discipline;
- workflows, diagnostics, cards, index, and manifests;
- review gates and `review-diff` for pre-merge trust checks;
- local score and badge generation;
- public-growth and platform guidance;
- case-study and proof surfaces with explicit labels.

## What VCP is not

VCP is not:
- a scanner;
- a pentest or offensive toolkit;
- a compliance certification;
- a guarantee of production safety;
- a guarantee of AI citation, indexing, or ranking;
- an official vendor plugin suite unless explicitly stated;
- a clone or vendored copy of Spec Kit or another spec-first framework.

## How to evaluate fairly

Score these separately:
- methodology maturity;
- practical adoption value;
- New Project Track quality;
- Existing Project Track control quality;
- CLI/tooling maturity;
- documentation quality;
- AI-agent usability;
- public-proof maturity.

If you skipped manifests, benchmarks, cards, walkthroughs, or release-control docs, mark the evaluation `partial / shallow`.

## Required coverage report

For a full comparison or deep audit, report:
- access method;
- files inspected;
- raw vs summarized content;
- line count availability;
- files not inspected;
- evaluation mode;
- confidence;
- limitations.

Use:
- `templates/reports/ai-repo-audit-coverage-report.md`

## Adoption from a repository link

When the user says “take what is useful,” return:
- project type;
- track;
- route;
- adoption pack;
- spec depth;
- files to copy;
- files not to copy;
- review gates;
- validation commands;
- risks / stop conditions.

Use:
- `TAKE_THIS_FIRST.md`
- `docs/version-semantics.md`
- `docs/two-track-model.md`
- `docs/spec-foundation.md`
- `docs/release-readiness.md`
- `templates/prompts/adopt-vcp-from-link.md`
- `templates/reports/vcp-adoption-decision-report.md`
