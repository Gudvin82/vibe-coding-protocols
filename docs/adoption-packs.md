# Adoption Packs

Adoption packs help humans and AI agents choose the right VCP file set for a target repository.

## New Project Pack

Use when:

- the project is starting from idea;
- little or no code exists.

Do not use when:

- the repository already has production users or sensitive workflows.

Recommended files:

- `START_HERE.md`
- Starter Protocol
- `AGENTS.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE_MAP.md`
- relevant templates

Optional files:

- Lite Adoption Path
- Product Brief prompts

Validation:

- `bash scripts/vibe-check.sh --starter`

Final report expectation:

- route selected;
- files copied;
- minimum validation path.

## Existing MVP Pack

Use when:

- the project works;
- it is not public production yet.

Do not use when:

- users, payments, production environments or compliance risk already exist.

Recommended files:

- Hardening Light or Standard
- `AUDIT_BACKLOG.md`
- `THIRD_PARTY_REGISTRY.md`
- `SECURITY_BASELINE.md`
- `PROJECT_MAP.md`
- `AGENTS.md`

Optional files:

- `ARCHITECTURE_MAP.md`
- Maintenance Refactoring if the code is already hard to change

Validation:

- `bash scripts/vibe-check.sh --hardening`

Final report expectation:

- audit backlog;
- third-party inventory;
- route confirmation.

## Existing Production Pack

Use when:

- real users exist;
- the product is public;
- staging or production environments exist.

Do not use when:

- there is no running product yet.

Recommended files:

- Hardening Full
- `SECURITY_BASELINE.md`
- `SECURITY_OPERATIONS_BASELINE.md`
- `INCIDENT_RECOVERY_RUNBOOK.md`
- `THIRD_PARTY_REGISTRY.md`
- `AUDIT_BACKLOG.md`
- `PROJECT_MAP.md`
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`
- release gate docs
- security review scope template

Optional files:

- Maintenance Refactoring after the risk map is explicit

Validation:

- `bash scripts/vibe-check.sh --audit --json`
- targeted tests and release gate evidence

Final report expectation:

- production risk signals;
- selected scope;
- blockers and stop conditions.

## Regulated, Payments or Personal Data Pack

Use when:

- payments exist;
- personal data is processed;
- legal or compliance claims matter;
- sensitive user data is involved.

Do not use when:

- the project is only a toy or local demo with no sensitive exposure.

Recommended files:

- everything in Existing Production Pack
- Security Review Scope
- accepted risk tracking
- incident recovery
- third-party registry
- stronger stop conditions

Warnings:

- do not change auth, payment or personal-data behavior without explicit scope and validation.

Validation:

- hardening checks plus explicit human review

Final report expectation:

- scope boundaries;
- sensitive flows;
- escalation path.

## Shared Engine or Multi-product Pack

Use when:

- one codebase or engine powers multiple products;
- product-specific modules share core infrastructure.

Do not use when:

- the repository is isolated to one disposable product.

Recommended files:

- `PROJECT_MAP.md`
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`
- `AUDIT_BACKLOG.md`
- release gate docs
- `THIRD_PARTY_REGISTRY.md`
- Hardening Full
- Maintenance Refactoring
- security review scope

Special requirements:

- identify the common engine;
- identify product-specific modules;
- identify shared data model;
- identify cross-product regression risks;
- require validation for both products before release.

Validation:

- release gates plus product-specific regression checks

Final report expectation:

- engine map;
- shared-risk map;
- staged adoption plan.

## Maintenance Pack

Use when:

- code works but is hard to change;
- AI-generated code has accumulated complexity;
- duplicate logic or unclear ownership exists.

Do not use when:

- behavior, public contracts, auth or billing flows need intentional change.

Recommended files:

- Maintenance Refactoring Protocol
- `/care-refactoring`
- refactoring report template
- risk classification guidance
- characterization test guidance

Optional files:

- `PROJECT_MAP.md`
- `ARCHITECTURE_SOURCE_OF_TRUTH.md` if ownership is unclear

Validation:

- focused tests;
- build, lint or route-specific checks

Final report expectation:

- scope;
- risk level;
- preserved contracts;
- next safe step.

## UI Ownership Pack

Use when:

- pages or routes own visual styling;
- component APIs are inconsistent;
- hardcoded UI styling is spreading.

Do not use when:

- you are redesigning the entire product visually.

Recommended files:

- UI Component Ownership Protocol
- `/ui-refactoring`
- UI refactoring report template

Optional files:

- design-system docs;
- public-site readiness if landing/docs trust pages are involved

Validation:

- typecheck;
- lint;
- component or browser checks as appropriate

Final report expectation:

- ownership problems found;
- styling moved into components;
- exceptions retained and why.

## Public Site Pack

Use when:

- public site, docs or landing need readiness for search, AI crawlers and trust.

Do not use when:

- there is no public site or docs surface yet.

Recommended files:

- public site readiness doc
- SEO and AI crawler readiness doc
- `llms.txt` template
- `robots.txt` template
- schema.org templates
- OpenGraph, canonical and trust checklist docs

Optional files:

- release notes;
- SECURITY and community feedback docs

Validation:

- docs review;
- structured-data validation;
- link and readability checks

Final report expectation:

- public trust gaps;
- checklist status;
- next publish-safe step.

## Companion files

- [AI_INTAKE.md](../AI_INTAKE.md)
- [target-project-classifier.md](./target-project-classifier.md)
- [../templates/prompts/evaluate-vcp-for-my-repo.md](../templates/prompts/evaluate-vcp-for-my-repo.md)
- [../templates/reports/vcp-adoption-assessment.md](../templates/reports/vcp-adoption-assessment.md)
- [../examples/adoption/dual-production-engine/README.md](../examples/adoption/dual-production-engine/README.md)
