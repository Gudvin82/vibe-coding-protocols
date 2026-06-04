<!-- vcp-version: v0.8.2 -->

<!-- vcp-artifact: THIRD_PARTY_REGISTRY -->
<!-- vcp-version: v0.8.2 -->
<!-- methodology-version: v1.4 -->

# THIRD_PARTY_REGISTRY.md

Use current official docs before adding or upgrading third-party dependencies.
If live-docs tools are available in your AI IDE, use them for package-specific details.

Small projects may use the compact section only.
Production or regulated projects should fill the extended review notes as well.

## Compact registry

| Name | Provider | Category | Purpose | Owner | Environment | Criticality | Auth type | Secret location | Data sent | Data received | Personal or sensitive data | Terms reviewed | Commercial use allowed | Rate limits | SLA or status page | Fallback behavior | Monitoring | Review status | Last reviewed | Next review date | Removal plan | Linked finding or accepted risk | Validation notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Example integration | Example provider | public API | Example feature support | engineering | staging | optional | API key | secret manager | coarse city name | weather summary | none | yes | unknown | documented | status page reviewed | cached placeholder | app logs | prototype-only | 2026-05-31 | 2026-06-30 | remove if feature is dropped | none | mocked in tests |

## Extended review notes

For each production or regulated integration, add a short section with:
- purpose and owner;
- auth model and rotation path;
- data sent and data received;
- personal, sensitive or customer data concerns;
- terms, caching, attribution and acceptable-use notes;
- fallback, graceful degradation and incident owner;
- review status and next review date.
