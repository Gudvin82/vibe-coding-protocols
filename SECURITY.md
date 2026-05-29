# Security Policy

## Scope

This repository is a public methodology and toolkit repository.
It contains markdown templates,
scripts,
examples
and workflow guidance.

It is not a production security certification for projects using the methodology.
Using Vibe Coding Protocols can improve delivery and security discipline,
but it does not replace security engineering,
developer review,
security testing,
threat modeling,
legal review
or professional audit.

For scope boundaries between repository policy,
methodology guidance,
project-specific baseline work
and production review,
see [docs/security-methodology-scope.md](./docs/security-methodology-scope.md).

## Supported versions

The current repository package version is supported.
Older docs may remain for history,
but may not receive active corrections.

## What to report privately

Report privately if you find:
- dangerous guidance that could cause secret leakage;
- unsafe installation instructions;
- command examples that could delete data or expose credentials;
- a vulnerability in scripts shipped by this repository;
- an incorrect security checklist item that could create real risk;
- an accidental real secret,
  private endpoint,
  customer data
  or internal architecture detail in the public repository.

## What may be reported publicly

Safe wording issues,
typo-level fixes
and non-sensitive documentation improvements may be reported publicly.

Do not include real secrets,
tokens,
customer data,
exploit-ready details
or private architecture in public issues.

## What not to report as a vulnerability

The following are not vulnerabilities by themselves:
- "VCP does not guarantee production security";
- lack of full CLI automation;
- lack of deep unit test coverage;
- synthetic examples not being production-ready;
- methodology limitations already documented as limitations.

## Severity examples

High severity examples:
- a real secret committed to the repository;
- an unsafe command example that may expose credentials;
- dangerous security guidance likely to cause real harm.

Medium severity examples:
- a misleading checklist item that may weaken production posture;
- an unsafe recommendation for secret storage,
  deploy approval
  or rollback handling.

Low severity examples:
- wording ambiguity;
- non-sensitive docs issue;
- missing clarification that does not create immediate exploitable risk.

## Responsible disclosure process

- Do not open public issues with real secrets,
  tokens,
  customer data,
  private project details
  or exploit steps that could increase harm.
- Contact the maintainer privately first.
- Use the website or contact channel already referenced by this repository,
  or GitHub private vulnerability reporting if it is enabled later.
- Include minimal sanitized reproduction steps.
- Include affected file,
  path
  and repository version when possible.
- Include impact and safer wording if applicable.
- The maintainer will review and respond when possible,
  and may ask for sanitized clarification.

## Secrets policy

Never submit real secrets in issues,
pull requests,
discussions,
examples
or tests.

If a real secret is accidentally exposed,
rotate it immediately outside this repository.
Removing it from GitHub is not enough.

## Methodology usage disclaimer

VCP is a readiness and workflow signal,
not a security scanner
and not a certification.

VCP cannot guarantee:
- production security;
- legal compliance;
- dependency or supply-chain safety;
- that AI-generated code is safe without review.

For public,
client-facing
or production systems,
use the Hardening or Extended routes and independent review.

## Related artifacts and routes

Use these when the project itself needs security discipline:
- [templates/SECURITY_BASELINE.md](./templates/SECURITY_BASELINE.md)
- [templates/SECURITY_OPERATIONS_BASELINE.md](./templates/SECURITY_OPERATIONS_BASELINE.md)
- [templates/THIRD_PARTY_REGISTRY.md](./templates/THIRD_PARTY_REGISTRY.md)
- [templates/INCIDENT_RECOVERY_RUNBOOK.md](./templates/INCIDENT_RECOVERY_RUNBOOK.md)
- [templates/reports/security-review-scope.md](./templates/reports/security-review-scope.md)
- [docs/security-tooling-landscape.md](./docs/security-tooling-landscape.md)
- [protocols/ai-project-hardening-protocol.md](./protocols/ai-project-hardening-protocol.md)
- [protocols/ai-project-extended-protocol.md](./protocols/ai-project-extended-protocol.md)
