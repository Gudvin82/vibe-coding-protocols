# Security Policy

## Scope

This repository is a public methodology and toolkit repository.
It contains markdown templates, scripts, examples and workflow guidance.

It is not a production security certification for projects using the methodology.
Using Vibe Coding Protocols can improve security discipline,
but it does not replace developer review, security testing,
threat modeling, legal review or professional audit.

For scope boundaries between repository policy,
methodology guidance and project-specific review,
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
- an accidental real secret, private endpoint, customer data
  or internal architecture detail in the public repository.

## What not to report as a vulnerability

The following are not vulnerabilities by themselves:
- "VCP does not guarantee production security";
- lack of full CLI automation;
- lack of deep unit test coverage;
- synthetic examples not being production-ready;
- methodology limitations already documented as limitations.

## Responsible disclosure process

- Do not open public issues with real secrets, tokens, customer data,
  private project details or exploit steps that could increase harm.
- Contact the maintainer privately first.
- Use the website or contact channel already referenced by this repository,
  or GitHub private vulnerability reporting if it is enabled later.
- Include minimal sanitized reproduction steps.
- Include affected file, path and repository version when possible.
- Include impact and suggested safer wording if applicable.
- The maintainer will acknowledge when possible and may ask
  for sanitized clarification.

## Public reporting process

Safe wording issues, typo-level fixes and non-sensitive documentation
improvements may be reported publicly.

## Secrets policy

Never submit real secrets in issues, pull requests, discussions,
examples or tests.

If a real secret is accidentally exposed,
rotate it immediately outside this repository.
Removing it from GitHub is not enough.

## Methodology usage disclaimer

VCP is a readiness and workflow signal,
not a security scanner and not a certification.

For public, client-facing or production systems,
use the Hardening or Extended routes and independent review.
