# Target Project Classifier

Use this matrix before choosing a VCP route or CLI profile.

## Route matrix

| CLI profile | Target signal | Route |
|---|---|---|
| `new-project` | no code yet or idea stage | Starter Protocol |
| `existing-mvp` | working MVP before production | Hardening Light or Standard |
| `production` | existing production project | Full Hardening |
| `regulated` | payments, personal data or compliance | Full Hardening + Security Review Scope |
| `shared-engine` | one engine powers multiple products | Shared Engine / Multi-product Pack + Full Hardening |
| `maintenance` | working code is risky to extend | Maintenance Refactoring |
| `ui-ownership` | page-level visual ownership drift | UI Component Ownership |
| `third-party-api` | an external API, SDK or webhook is being proposed | Third-party API Intake |
| `operations` | production errors or log evidence must be observed without mutation | Operations Feedback Loop |
| `backlog` | tasks, follow-up work, and implementation state need one shared kanban | Project Backlog Workflow |
| `public-site` | public docs, trust or crawler readiness | Public Site Readiness |
| `public-growth` | service pages, public content, GEO, schema, or AI visibility need structured work | Public Growth Playbook |
| `post-task-review` | meaningful diff needs acceptance | Post-Task Code Review |

## Defaults

- Production plus user data defaults to Full Hardening.
- Payments or personal data default to Full Hardening.
- Shared engine work should include `PROJECT_MAP.md`, `templates/ARCHITECTURE_SOURCE_OF_TRUTH.md` and release gates.
- Security-sensitive change belongs in Hardening or Extended, not routine maintenance.
- External API requests should go through Third-party API Intake before implementation.
- Production observation work should stay read-only until triage and backlog state are written down.
- Backlog state should be updated before implementation starts, not after code is already merged.
- Public growth work should start from one audience intent, one page goal, and one proof boundary, not from keyword stuffing.
- Production, shared-engine and regulated work should assume a post-task review gate before merge or release.
- If no validation path exists, stop or narrow scope.

## CLI examples

```bash
python3 -m vcp_cli route --profile production --json
python3 -m vcp_cli route --profile shared-engine --json
python3 -m vcp_cli route --profile public-growth --json
python3 -m vcp_cli route --profile operations --json
python3 -m vcp_cli route --profile backlog --json
python3 -m vcp_cli route --profile third-party-api --json
python3 -m vcp_cli route --profile post-task-review --json
```

## Synthetic examples

- New SaaS MVP with no production users -> `new-project`
- Existing marketing website -> `public-site`
- Existing service site that needs stronger commercial/service pages -> `public-growth`
- Existing production app with payments -> `regulated`
- Two products on one shared engine -> `shared-engine`
- Working app with messy code -> `maintenance`
- Frontend pages with hardcoded styling -> `ui-ownership`
- Feature request that depends on a public API -> `third-party-api`
- Live webhook 500s need evidence capture and triage only -> `operations`
- Team needs one visible queue for ideas, bugs, docs, and follow-up work -> `backlog`
