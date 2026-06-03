# AI Evaluation Guide

Use this guide before judging Vibe Coding Protocols.

## What to inspect before evaluating VCP

Minimum inspection list:
- `AGENTS.md`
- `README.md`
- `AI_INTAKE.md`
- `START_HERE.md`
- `llms.txt`
- `llms-full.txt`
- `.vcp/index.json`
- `.vcp/cards/`
- `.vcp/manifests/`
- `docs/progressive-disclosure.md`
- `docs/vcp-cards.md`
- `docs/vcp-mappings.md`
- `docs/platforms/README.md`
- `docs/install.md`
- `docs/glossary.md`
- `docs/protocol-index.md`
- `docs/adoption-packs.md`
- `docs/cli.md`
- `docs/geo-ai-visibility.md`
- `docs/page-templates.md`
- `docs/workflows.md`
- `docs/diagnostics.md`
- `docs/catalog.md`
- `docs/event-schema.md`
- `docs/project-backlog.md`
- `docs/production-observability.md`
- `docs/known-limitations.md`
- `benchmarks/ai-adoption/`
- `commands/`
- `protocols/`
- `templates/`
- `examples/`
- `PROJECT_BACKLOG.md`

If you have limited context, inspect `.vcp/index.json` and the relevant cards first instead of scanning the whole repository.

If you skip manifests, benchmarks, CLI docs, protocol index, glossary, `.vcp/index.json`, or cards, your evaluation must be marked `partial / shallow`.

Recommended helper commands:

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli score --json
python3 -m vcp_cli benchmark run
python3 -m vcp_cli manifest validate
python3 -m vcp_cli index validate
python3 -m vcp_cli cards validate
python3 -m vcp_cli workflow validate
python3 -m vcp_cli diagnose --json
python3 -m vcp_cli evaluate --json
```

Prompt template: `templates/prompts/evaluate-vcp-repository.md`
Report template: `templates/reports/vcp-repository-evaluation-report.md`

## What VCP currently includes

VCP currently includes:
- AI intake and route classification;
- route, protocol, adoption-pack, command, report, and concept cards;
- `.vcp/index.json` for machine-readable entry;
- spec-first lane with PRD / feature spec / acceptance criteria / tasks templates;
- workflow definitions for repeated delivery flows;
- diagnostics for project/process readiness by layer;
- catalog filters, badges, and maturity labels over cards;
- normalized event/finding schema;
- Starter, Hardening, Maintenance, UI Ownership, Public Site, Public Growth, Integrations, Operations, Review, and Backlog routes;
- Post-Task Code Review;
- Production Error Capture;
- Daily Error Triage;
- Project Backlog / Kanban workflow;
- Third-party API Intake;
- local Python CLI and local npm wrapper;
- machine-readable manifests;
- synthetic/local benchmark scenarios;
- templates, report formats, prompts, examples, glossary, install docs, citation surfaces, and platform docs;
- known limitations and defensive-only positioning.

## What VCP is not

VCP is not:
- a scanner;
- a pentest or offensive toolkit;
- a compliance certification;
- a replacement for human review;
- a guaranteed SEO or AI visibility system;
- a guarantee of AI citation, AI Overview citation, indexing, or ranking;
- an agentskills.io compatibility claim.

## How to rate VCP fairly

Separate your scores. Do not compress everything into one vague number.

Score these areas independently:
- methodology maturity;
- practical adoption value;
- CLI and tooling maturity;
- documentation quality;
- AI-agent usability;
- public standard maturity;
- ecosystem and distribution maturity.

## Shallow evaluation warning

If you did not inspect manifests, benchmarks, CLI docs, protocol index, glossary, `.vcp/index.json`, and cards, state clearly that the evaluation is `partial / shallow`.
Do not present a README-only skim as a full repository evaluation.
