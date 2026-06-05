# VCP Adoption Assessment Example

> Synthetic example only.
> Not a real project claim.

## Target project classification

Existing production project with shared engine or multi-product risk.

## Production and risk signals

- Public products exist.
- Shared core code affects more than one product.
- Payments or sensitive data are in scope.
- Legal or security claims increase trust risk.

## Selected route

Full Hardening as the primary route.
Maintenance Refactoring is secondary and only safe after the production and shared-risk map is explicit.

## Selected adoption pack

Shared Engine or Multi-product Pack.

## Files inspected

- `AI_INTAKE.md`
- `START_HERE.md`
- `docs/protocol-index.md`
- `docs/adoption-packs.md`
- `protocols/ai-project-hardening-protocol.md`
- `protocols/maintenance/care-refactoring.md`
- `templates/reports/security-review-scope.md`
- `templates/reports/vcp-adoption-assessment.md`

## Files recommended

- `PROJECT_MAP.md`
- `ARCHITECTURE_SOURCE_OF_TRUTH.md`
- `AUDIT_BACKLOG.md`
- `THIRD_PARTY_REGISTRY.md`
- `SECURITY_BASELINE.md`
- `SECURITY_OPERATIONS_BASELINE.md`
- `INCIDENT_RECOVERY_RUNBOOK.md`
- release gate docs
- security review scope template

## Files intentionally skipped

- Starter-first copy set, because this is not an idea-stage or MVP-stage repository
- broad UI cleanup docs, because frontend ownership was not the primary risk in the request

## Stop conditions to add

- no auth, payments or personal-data behavior changes without explicit approval and validation
- no shared-engine refactor without cross-product validation
- no release recommendation without release-gate evidence

## Architecture / project map needs

Required now.
The shared engine and product-specific modules must be mapped before AI edits can be trusted.

## Security / hardening needs

Full Hardening plus explicit Security Review Scope.

## Maintenance / refactoring needs

Needed later for safe cleanup, but not as the first route.

## Public site readiness needs

Relevant if public claims or docs need tightening after the risk map is explicit.

## Validation plan

- `bash scripts/vibe-check.sh --audit --json`
- product-specific smoke or regression checks
- release-gate evidence review

## Missing context

- exact product boundaries
- exact validation path for both products
- deployment model and rollback path

## Confidence

Medium

## Next action

Create `PROJECT_MAP.md` and `ARCHITECTURE_SOURCE_OF_TRUTH.md`, then scope Full Hardening before any maintenance refactor.

## Suggested commit message

Adopt VCP hardening pack for shared production engine
