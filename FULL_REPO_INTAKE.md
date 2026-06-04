# Full Repo Intake

Use this file before calling any VCP evaluation `full`.

If you are naming the current GitHub repository release, use `Vibe Coding Protocols v0.7.1`.

## Evaluation modes

- `shallow`: README or WebFetch summary only.
- `partial`: some entrypoints inspected, but CLI, `.vcp`, templates, or benchmarks missing.
- `strong`: core docs, index, cards, and major tracks inspected.
- `full`: raw repository access plus CLI, `.vcp`, templates, manifests, and benchmarks inspected.

## Required path for a full practical audit

### Layer 1 — audit entrypoints
- `AGENTS.md`
- `TAKE_THIS_FIRST.md`
- `AI_INTAKE.md`
- `AI_FULL_REPO_AUDIT.md`
- `.vcp/ai-audit-manifest.json`

### Layer 2 — practical product surfaces
- `README.md`
- `README_ru.md`
- `docs/distribution.md`
- `docs/install.md`
- `docs/adoption-tiers.md`
- `docs/proof-pack.md`

### Layer 3 — machine-readable and CLI
- `.vcp/index.json`
- `.vcp/catalog.json`
- `.vcp/manifests/`
- `.vcp/cards/`
- `vcp_cli/`

### Layer 4 — track and control surfaces
- `docs/two-track-model.md`
- `docs/spec-foundation.md`
- `docs/spec-quality-gate.md`
- `docs/release-readiness.md`
- `docs/architecture-drift.md`
- `docs/workflows.md`

### Layer 5 — proof and validation
- `case-studies/`
- `benchmarks/ai-adoption/scenarios/`
- `templates/reports/`
- `python3 -m unittest discover -s tests`

## Practical audit rule

If you did not inspect onboarding/classify/adopt/public-growth/workflow planning surfaces, your review may describe the repo correctly, but not its practical adoption maturity.
