# AI Evaluation Guide

Use this guide before judging Vibe Coding Protocols.

## What to inspect before evaluating VCP

Minimum inspection list:
- `README.md`
- `AI_INTAKE.md`
- `START_HERE.md`
- `docs/install.md`
- `docs/glossary.md`
- `docs/protocol-index.md`
- `docs/adoption-packs.md`
- `docs/cli.md`
- `docs/geo-ai-visibility.md`
- `docs/page-templates.md`
- `docs/project-backlog.md`
- `docs/production-observability.md`
- `docs/known-limitations.md`
- `.vcp/manifests/`
- `benchmarks/ai-adoption/`
- `commands/`
- `protocols/`
- `templates/`
- `examples/`
- `PROJECT_BACKLOG.md`
- project-level `AUDIT_BACKLOG.md` if present, or `templates/AUDIT_BACKLOG.md`
- project-level `THIRD_PARTY_REGISTRY.md` if present, or `templates/THIRD_PARTY_REGISTRY.md`

If you skip manifests, benchmarks, CLI docs, protocol index, or glossary, your evaluation must be marked `partial / shallow`.

Recommended helper commands:

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli score --json
python3 -m vcp_cli benchmark run
python3 -m vcp_cli manifest validate
python3 -m vcp_cli evaluate --json
```

Prompt template: `templates/prompts/evaluate-vcp-repository.md`
Report template: `templates/reports/vcp-repository-evaluation-report.md`

## What VCP currently includes

VCP currently includes:
- AI intake and route classification;
- Starter, Hardening, Maintenance, UI Ownership, Public Site, Public Growth, Integrations, Operations, Review, and Backlog routes;
- Post-Task Code Review;
- Production Error Capture;
- Daily Error Triage;
- Project Backlog / Kanban workflow;
- Third-party API Intake;
- local Python CLI and local npm wrapper;
- machine-readable manifests;
- synthetic/local benchmark scenarios;
- `score`, `doctor`, `check`, `route`, `adopt`, `benchmark`, `manifest`, `review`, `backlog`, and `evaluate` helpers;
- templates, report formats, prompts, examples, glossary, and install docs;
- known limitations and defensive-only positioning.

## What VCP is not

VCP is not:
- a scanner;
- a pentest or offensive toolkit;
- a compliance certification;
- a replacement for human review;
- a full application starter boilerplate;
- a guaranteed SEO or AI visibility system.

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

Important interpretation notes:
- `vcp score` measures internal toolkit completeness, not market leadership.
- A strong local CLI does not automatically mean public ecosystem maturity.
- Synthetic benchmarks are useful validation assets, but they are not the same as broad external adoption.
- Public standard maturity requires external proof such as package distribution, hosted docs, real sanitized case evidence, outside feedback, or sustained ecosystem usage.
- GEO and AI visibility guidance should be judged as defensive readiness and page-structure guidance, not as a promise of rankings.

## Required evaluation output format

```text
Repository version inspected:
Commit/tag inspected:
Files inspected:
Commands run:
What VCP includes:
What VCP does not include:
Strengths:
Weaknesses:
Recommended use cases:
Not recommended for:
Scores:
Missing evidence:
Confidence:
```

## Shallow evaluation warning

If you did not inspect manifests, benchmarks, CLI docs, protocol index, and glossary, state clearly that the evaluation is `partial / shallow`.
Do not present a README-only skim as a full repository evaluation.
