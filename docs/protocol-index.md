# Protocol Index

Compact VCP route catalog.

| Protocol / command | Route | Use when | Do not use when | Required inputs | Validation signals | Report template | Risk level |
|---|---|---|---|---|---|---|---|
| Starter Protocol | starter | starting a new project | production code already exists | product brief, scope | `vibe-check --starter` | project docs | low to medium |
| Hardening Protocol | hardening | existing AI-generated project needs readiness audit | you only need one tiny cleanup | repo, architecture, risk signals | `vibe-check --audit --json` | `AUDIT_BACKLOG.md` | medium to high |
| `/care-refactoring` | maintenance | working code is hard to change | behavior change is required | preserved behavior, validation path | focused tests, review gate | `templates/reports/refactoring-report.md` | low to high |
| `/ui-refactoring` | ui-ownership | UI ownership is drifting | whole-system redesign | target slice, current UI behavior | typecheck, lint, review gate | `templates/reports/ui-refactoring-report.md` | low to high |
| `/third-party-api-intake` | integrations | an external API, SDK or webhook is being proposed | no third-party system is involved | provider, purpose, data flow, validation path | `vcp check --fast --json`, review gate | `templates/reports/third-party-api-intake-report.md` | medium to high |
| Public Growth Playbook | public-growth | service pages, articles, cases, trust pages, or AI visibility need structured improvement | the plan depends on hidden content, fake proof, or guaranteed ranking claims | audience intent, proof boundary, page brief | links, readability, review gate | `templates/reports/public-growth-audit-report.md` | medium |
| `/prod-log-monitor` | operations | production errors need read-only observation | the task expects fixes, deploys, or mutation | authorized log path, time window, privacy boundaries | `vcp doctor`, capture report | `templates/reports/production-error-capture-report.md` | medium |
| `/daily-error-triage` | operations | captured evidence must be grouped into follow-up work | root-cause or implementation work must start immediately | inbox entries, recent incidents, backlog path | `vcp backlog validate`, triage report | `templates/reports/daily-error-triage-report.md` | medium |
| `/backlog-update` | backlog | tasks need one visible kanban before implementation starts | hardening findings should live in `AUDIT_BACKLOG.md` instead | current work item, owner, status, validation path | `vcp backlog validate` | `templates/reports/backlog-update-report.md` | low to medium |
| `/loop-code-review` | review | meaningful AI-generated changes need acceptance | full security audit is still unresolved | active diff, validation output, reviewer path | review plus validation green | `templates/reports/code-review-report.md` | medium to high |
| AI Intake | intake | an AI agent must classify a target repo first | route is already known | repo stage, risk signals | adoption assessment quality | `templates/reports/vcp-adoption-assessment.md` | medium |
| Public Site Readiness | public-site | publishing public docs or product site | no public site exists | trust links, publish checklist | links, readability, site checks | adoption assessment or local notes | medium |
