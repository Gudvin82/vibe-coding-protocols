# Recommended Pack

> Synthetic example only.
> Not a real project claim.

## Bad shallow recommendation

- Copy `AGENTS.md`
- Copy `AUDIT_BACKLOG.md`
- Maybe use Starter templates

Why this is wrong:

- it ignores production risk;
- it ignores shared-engine blast radius;
- it underrates payments, sensitive data and public claims;
- it skips route classification.

## Corrected recommendation

Classification:

- existing production project;
- shared engine or multi-product;
- security-sensitive.

Recommended route and pack:

- Full Hardening
- Shared Engine or Multi-product Pack
- Security Review Scope
- Architecture Source of Truth
- Project Map
- Audit Backlog
- Third Party Registry
- Release Gate
- Maintenance Refactoring only after mapping and stop conditions are explicit

## Files intentionally skipped

- Starter-only copy set, because the project already has production risk
- UI Ownership pack as the primary route, unless frontend ownership drift is the main active problem
