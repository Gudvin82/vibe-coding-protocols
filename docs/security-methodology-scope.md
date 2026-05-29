# Security Methodology Scope

Use this page to separate repository policy from project security work.

## Four different layers

### Repository security policy

This covers the public `vibe-coding-protocols` repository itself:
- public markdown guidance;
- scripts shipped in the repository;
- public examples;
- issue,
  PR
  and disclosure hygiene.

See [../SECURITY.md](../SECURITY.md).

### Methodology security guidance

This covers what VCP encourages teams to document and review:
- readiness signals;
- project memory files;
- security baselines;
- incident recovery preparation;
- third-party intake discipline;
- hardening routes;
- release gates.

### Project-specific security baseline

This is where a real project defines its own security expectations.
Use:
- [../templates/SECURITY_BASELINE.md](../templates/SECURITY_BASELINE.md)
- [../templates/SECURITY_OPERATIONS_BASELINE.md](../templates/SECURITY_OPERATIONS_BASELINE.md)
- [../templates/THIRD_PARTY_REGISTRY.md](../templates/THIRD_PARTY_REGISTRY.md)
- [../templates/INCIDENT_RECOVERY_RUNBOOK.md](../templates/INCIDENT_RECOVERY_RUNBOOK.md)
- [../templates/reports/security-review-scope.md](../templates/reports/security-review-scope.md)

### Production security audit

This is a project-specific assessment of a real deployment.
It may require:
- manual review;
- scanner evidence;
- penetration testing;
- legal review;
- architecture review;
- production rollback and incident readiness.

VCP does not replace that work.

## What VCP can help with

VCP can help teams:
- make security-relevant decisions more explicit;
- avoid unsafe AI-generated shortcuts;
- track third-party integrations and update discipline;
- route projects toward Hardening or Extended review;
- preserve a written audit trail of risks and accepted constraints.

## What VCP cannot guarantee

VCP cannot guarantee:
- production safety;
- absence of vulnerabilities;
- legal compliance;
- dependency or supply-chain safety;
- correct cloud or infrastructure configuration;
- that AI-generated code is safe without review;
- real-world runtime security.

See also [security-tooling-landscape.md](./security-tooling-landscape.md).

## When to use each artifact

Use `SECURITY_BASELINE.md` when a project needs an explicit security posture
for the current stage.

Use `SECURITY_OPERATIONS_BASELINE.md` when the project has recurring checks,
owners,
cadence
and operational evidence.

Use `THIRD_PARTY_REGISTRY.md` when the project depends on external packages,
services,
APIs,
repositories
or hosted platforms.

Use `INCIDENT_RECOVERY_RUNBOOK.md` when the project needs clear rollback,
triage,
owner
and communication guidance.

Use `security-review-scope.md` before any defensive security review that needs explicit authorization and stop conditions.

## When to escalate routes

Escalate to Hardening when:
- the project already exists;
- AI-generated code is accumulating;
- secrets,
auth
or deploy risk are unclear;
- you need a structured readiness review.

Escalate to Extended when:
- the project is public;
- it is client-facing or production-bound;
- it handles auth,
payments
or personal data;
- incident readiness or operational accountability matter;
- a normal maintenance pass is no longer enough.
