# Protocol Index

This is a compact route catalog for VCP.

| Protocol / command | Route | Use when | Do not use when | Required inputs | Validation signals | Report template | Risk level |
|---|---|---|---|---|---|---|---|
| Starter Protocol | Starter | Starting a new project | Existing code already needs readiness audit | product brief, scope, stack intent | `vibe-check --starter`, build/test if present | project docs and plan artifacts | low to medium |
| Hardening Protocol | Hardening | Existing AI-generated project needs production or security readiness | You only need a tiny maintainability cleanup | repo, architecture, security and deploy evidence | `vibe-check --audit`, scanners, targeted checks | `AUDIT_BACKLOG.md`, scanner reports | medium to high |
| `/care-refactoring` | Maintenance | Working project is hard to change safely | Behavior or public contract must change | target scope, preserved behavior, validation path | focused tests, lint/build, route-specific checks | `templates/reports/refactoring-report.md` | low to high |
| `/ui-refactoring` | UI Ownership | UI styling ownership is drifting | You are redesigning the whole system | target slice, current UI behavior, validation path | typecheck, lint, component/build/manual checks | `templates/reports/ui-refactoring-report.md` | low to high |
| AI Intake | Intake and adoption | An AI agent must classify a target repo before judging or applying VCP | You only need a direct link to one known route | target repo stage, risk signals, missing context | route selection quality, adoption assessment | `templates/reports/vcp-adoption-assessment.md` | medium |
| Security Baseline | Security Baseline | Public or production-bound project needs baseline expectations | You want an exploit workflow | threat surface, auth/data/integration info | review plus route checks | `templates/SECURITY_BASELINE.md` | medium |
| Third-party intake | Supply chain | New dependency or service is being considered | No third-party change is involved | package/service details, docs, constraints | registry review, scanners, docs check | `templates/THIRD_PARTY_REGISTRY.md` | medium |
| Incident Recovery | Incident Recovery | Rollback, outage or recovery path must be documented | There is no incident/recovery concern yet | owner, rollback path, evidence | manual verification and runbook review | `templates/INCIDENT_RECOVERY_RUNBOOK.md` | high |
| Release readiness | Release Discipline | Need deploy decision and blockers | You are still shaping MVP scope | release state, blockers, evidence | `vibe-check`, tests, release gates | release docs and backlog | medium to high |
| Integrations docs | Integrations | Need IDE-specific onboarding guidance | You expect a mature plugin | selected IDE, route, files to copy | route checks and local validation | route report | low |
| Public-site readiness | Public site readiness | Publishing docs or AI-assisted product marketing pages | You need ranking guarantees | URLs, sitemap, robots, schema plan | local docs review, structured-data validation | site readiness checklist | medium |

## Intake-first docs

- [../AI_INTAKE.md](../AI_INTAKE.md)
- [target-project-classifier.md](./target-project-classifier.md)
- [adoption-packs.md](./adoption-packs.md)
- [../templates/prompts/evaluate-vcp-for-my-repo.md](../templates/prompts/evaluate-vcp-for-my-repo.md)
- [../templates/reports/vcp-adoption-assessment.md](../templates/reports/vcp-adoption-assessment.md)
