# /third-party-api-intake

Use when an AI agent wants to add an external API, SDK, webhook, SaaS integration or public API.

## Required inputs

- feature depending on the integration;
- candidate provider or API name;
- environment and criticality;
- expected data flow;
- validation path.

## Agent behavior

1. Do not write integration code first.
2. Classify the API and owner.
3. Review auth, secrets, data handling, terms, rate limits and fallback.
4. Update `THIRD_PARTY_REGISTRY` or plan the required entry.
5. Decide whether the integration is safe to prototype, safe to implement narrowly or needs escalation.
6. Require post-task code review before production integration merge.

## Output

Produce [../templates/reports/third-party-api-intake-report.md](../templates/reports/third-party-api-intake-report.md).
