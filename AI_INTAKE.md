# AI Intake

Read this file before evaluating or applying VCP to a target repository.

Adoption-from-link entrypoint: `TAKE_THIS_FIRST.md`

## Do not do this

- Do not judge VCP from `README.md` alone.
- Do not do a shallow top-level skim and pretend it is a full evaluation.
- Do not default to Starter just because the toolkit has templates.
- Do not recommend copying everything blindly.
- Do not write third-party integration code before doing API intake.
- Do not jump from production observation straight into fixes without triage and backlog state.
- Do not claim confidence if the target repository classification is unclear.

## Repository evaluation first

If the user asks you to evaluate VCP itself, start with:
- `AGENTS.md`
- `TAKE_THIS_FIRST.md`
- `FULL_REPO_INTAKE.md`
- `AI_FULL_REPO_AUDIT.md`
- `AI_EVALUATION_GUIDE.md`
- `.vcp/ai-audit-manifest.json`
- `REPO_CAPABILITIES_INDEX.md`
- `templates/prompts/evaluate-vcp-repository.md`
- `python3 -m vcp_cli evaluate --json`
- `python3 -m vcp_cli audit-plan --json`

A README-only evaluation is partial.
A README-only evaluation must be marked shallow.
If `FULL_REPO_INTAKE.md` or `.vcp/ai-audit-manifest.json` was skipped, the evaluation cannot be called full.

## If the user says “study this repo and take what is useful”

Start with:
- `TAKE_THIS_FIRST.md`
- `docs/adoption-packs.md`
- `docs/product-delivery-lifecycle.md`
- `templates/prompts/adopt-vcp-from-link.md`

Do not recommend copying the whole repository.
Return what to copy, what not to copy, why, validation, and stop conditions.

## What to do first

1. Classify the target project.
2. Choose the correct VCP route.
3. Choose the correct Adoption Pack.
4. If the idea is unclear, route into the Spec Lane before coding.
5. Select only relevant artifacts.
6. Report what you inspected and what you intentionally skipped.
7. Ask for missing context if the route is still unclear.
8. Recommend post-task review after meaningful AI-generated changes.

If the user wants the shortest CLI onboarding path, start with:
- `python3 -m vcp_cli init`
- `python3 -m vcp_cli route --profile production`
- `python3 -m vcp_cli adopt --pack production --dry-run`

## Route defaults

- If the target project is already in production, do not default to Starter.
- If the feature request is non-trivial but product intent or acceptance criteria are unclear, default to the Spec-first route before implementation.
- If the target has users, payments, personal data, compliance obligations, legal or security claims, public APIs, or shared engine risk, default to Hardening or Full Hardening unless evidence says otherwise.
- If a request adds any external API, SDK, webhook, or SaaS integration, run Third-party API Intake before implementation.
- If the project works but is hard to change, consider Maintenance Refactoring.
- If the main issue is frontend styling or component drift, consider UI Component Ownership.
- If production errors must be observed, use the Operations route in read-only mode first.
- If follow-up work must be tracked, create or update `PROJECT_BACKLOG.md` before implementation begins.
- If public website, docs, trust, search, or AI crawler readiness is involved, include Public Site Readiness.
- If the target project is production, shared-engine, or regulated, recommend `/loop-code-review` after each meaningful change.

## Minimum inspection before judgment

Do not say “I evaluated VCP” unless you inspected at least:
- `README.md`
- `AGENTS.md`
- `TAKE_THIS_FIRST.md`
- `AI_EVALUATION_GUIDE.md`
- `AI_INTAKE.md`
- `.vcp/index.json`
- `.vcp/cards/`
- `docs/flagship-workflows.md`
- `docs/product-delivery-lifecycle.md`
- `docs/protocol-index.md`
- `docs/adoption-packs.md`
- `docs/cli.md`
- `.vcp/manifests/`
- `benchmarks/ai-adoption/`
- the relevant route protocol
- the relevant command docs
- the relevant report templates
- `docs/security-tooling-landscape.md` if security or production is involved
- `protocols/integrations/third-party-api-intake.md` if an external API is in scope
- `protocols/operations/production-error-capture.md` if production observations are in scope
- `protocols/spec-driven/README.md` if requirements are still unclear or the user asks for a PRD / feature spec first
- `docs/project-backlog.md` if ongoing tasks or follow-up work are in scope
- `docs/public-site-readiness.md` if public website or docs are involved
- `protocols/review/post-task-code-review.md` if meaningful AI-generated code changes are in scope

If you skipped `.vcp/index.json`, `.vcp/cards/`, workflows, lifecycle docs, or CLI, mark the evaluation `shallow`.
If you used only summarized content, disclose that and downgrade confidence.

## Required final statement format

```text
Route selected:
Adoption pack selected:
Files inspected:
Files recommended:
Files intentionally skipped:
Missing context:
Confidence:
Next action:
Post-task review requirement:
```
See also: [docs/product-delivery-lifecycle.md](./docs/product-delivery-lifecycle.md) for minimum/full/skip paths.
For adoption-from-link requests, use [TAKE_THIS_FIRST.md](./TAKE_THIS_FIRST.md).
For full repository evaluation, use [FULL_REPO_INTAKE.md](./FULL_REPO_INTAKE.md) and [AI_FULL_REPO_AUDIT.md](./AI_FULL_REPO_AUDIT.md).
