<!-- vcp-version: v0.9.3 -->
<!-- methodology-version: v1.4 -->
<!-- vcp-version: v0.8.4 -->

<!-- vcp-version: v0.8.2 -->

<!-- vcp-artifact: SECURITY_REVIEW_SCOPE -->
<!-- vcp-version: v0.8.2 -->

# Security Review Scope

> Do not run security testing against systems you do not own
> or do not have explicit permission to test.

## Review owner

State who requested and owns the review.

## Authorized systems

List only systems that are explicitly in scope.

## Excluded targets

List systems,
environments
or dependencies that must not be touched.

## Allowed tools

List approved defensive tools,
commands
or scanners.

## Disallowed tools/actions

List prohibited actions such as destructive tests,
credential spraying,
unauthorized scanning
or third-party infrastructure probing.

## Data handling rules

State what evidence may be stored,
shared
or redacted.

## Secrets handling

Explain how secrets are avoided,
masked
and rotated if exposure occurs.

## Production safety constraints

State limits for production interaction,
rate,
risk
and rollback expectations.

## Evidence storage

State where notes,
reports
and sanitized evidence will live.

## Disclosure path

Reference the responsible disclosure path and escalation owner.

## Stop conditions

List conditions that require the review to pause or escalate.

## Approval status

Record whether the review is approved,
by whom,
and for which version or target.
