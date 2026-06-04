<!-- vcp-version: v0.6.7 -->

<!-- vcp-artifact: THIRD_PARTY_API_INTAKE_REPORT -->
<!-- vcp-version: v0.6.6 -->
<!-- methodology-version: v1.4 -->

# Third-party API Intake Report

## Overall result

State one of: no integration needed, prototype-only, narrow implementation approved, or escalate before implementation.

## Classification

Record API name, provider, category, purpose, owner, environment and criticality.

## Auth and secrets

Record auth type, secret storage plan, rotation path, least privilege and whether client-side use is safe.

## Data handling

Record data sent, data received, personal or sensitive data concerns, retention assumptions and minimization plan.

## Terms and compliance

Record terms link, acceptable use, commercial use, attribution, rate limits, caching and reuse restrictions, privacy policy and whether DPA review is needed.

## Reliability and fallback

Record quota, timeout and retry policy, outage behavior, fallback, graceful degradation, monitoring and incident owner.

## Security review

Record HTTPS expectations, webhook signing, input and response validation, SSRF or SDK risk, and abuse or rate-limit risk.

## Registry update

Record whether `THIRD_PARTY_REGISTRY` was updated, deferred or blocked, and why.

## Implementation decision

State the narrowest safe next step, what is still blocked, and whether post-task code review is required before production merge.
