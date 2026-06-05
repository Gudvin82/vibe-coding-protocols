# Third-party API Intake Protocol

Purpose:
When an AI agent proposes adding any external API, SDK, webhook, SaaS integration, data provider or public API, it must not immediately write integration code. It must first run API intake.

Core rule:
No external API dependency goes into production code without classification, registry entry, data and risk review, fallback plan and validation.

## Applies to

- public APIs;
- SaaS APIs;
- payment APIs;
- map, weather, crypto, translation and media APIs;
- AI and LLM APIs;
- analytics and marketing APIs;
- webhook providers;
- scraping and data APIs;
- SDK-backed integrations;
- any dependency that sends data to or receives data from a third-party system.

## Non-goals

- not a public API directory;
- not a recommendation list;
- not a guarantee that an API is safe;
- not legal review by itself;
- not vendor due diligence by itself;
- not automatic production approval.

## Operating rules

- Do not add secrets to code, prompts, examples or screenshots.
- Do not assume public or free means production-safe.
- Do not assume terms, quotas, caching rights or attribution are compatible until reviewed.
- Prefer one concrete integration decision over browsing a wide catalog.
- If the provider would handle personal, sensitive or customer data, escalate to hardening or regulated review as needed.
- If there is no fallback or graceful degradation path, record that risk before implementation.

## Checklist

### Classification

Record:
- API name;
- provider;
- category;
- purpose;
- product feature depending on it;
- owner;
- environment: prototype, staging or production;
- criticality: optional, important or critical.

### Auth and secrets

Record:
- auth type: none, API key, OAuth, JWT, basic auth, signed requests or other;
- secret storage location;
- rotation path;
- least privilege scope;
- token exposure risk;
- whether client-side use is safe.

### Data handling

Record:
- data sent;
- data received;
- personal data involved;
- sensitive data involved;
- customer data involved;
- logs and telemetry;
- retention assumptions;
- cross-border transfer concerns;
- whether data can be minimized.

### Terms and compliance

Record:
- terms of service link;
- acceptable use restrictions;
- commercial use allowed;
- attribution required;
- rate limits;
- caching rules;
- data reuse restrictions;
- privacy policy;
- whether a DPA is needed for personal data;
- license if relevant.

### Reliability

Record:
- rate limits and quota;
- SLA or status page;
- outage behavior;
- timeout and retry policy;
- fallback;
- graceful degradation;
- monitoring;
- alerting;
- owner for incident response.

### Security

Record:
- HTTPS required;
- certificate validation;
- webhook signing if applicable;
- input validation;
- response validation;
- SSRF risks;
- supply-chain risk;
- SDK dependency risk;
- abuse and rate-limit risk.

## Production gate

Before production use:
- update `THIRD_PARTY_REGISTRY`;
- add tests or mocks where proportional;
- add timeout, retry and fallback behavior;
- verify secrets handling;
- verify data minimization;
- run Post-Task Code Review;
- record accepted risk if unresolved.

## Stop conditions

Stop and escalate when:
- the API would require committing a key or token;
- terms, quotas or data handling are still unknown;
- personal, sensitive or customer data would be sent without explicit review;
- there is no fallback or outage behavior plan;
- the provider would become a hidden critical dependency;
- the agent cannot explain how to validate the integration safely.

## Valid outcomes

- No integration needed.
- Prototype-only integration with explicit limits.
- Approved narrow implementation scope.
- Hardening or regulated escalation before implementation.

## Final report

Use [../../templates/reports/third-party-api-intake-report.md](../../templates/reports/third-party-api-intake-report.md) and include:
- classification summary;
- auth and data risk summary;
- terms and quota review;
- fallback and reliability plan;
- registry update status;
- implementation decision;
- review gate requirement.
