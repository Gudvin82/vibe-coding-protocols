<!-- vcp-version: v0.8.0 -->

<!-- vcp-artifact: THIRD_PARTY_REGISTRY_FILLED_EXAMPLE -->
<!-- vcp-version: v0.8.0 -->
<!-- methodology-version: v1.4 -->

# Filled Third-Party Registry Example

> Synthetic filled example — not a real case study.

## Compact example

| Name | Provider | Category | Purpose | Owner | Environment | Criticality | Auth type | Secret location | Data sent | Data received | Personal or sensitive data | Terms reviewed | Commercial use allowed | Rate limits | SLA or status page | Fallback behavior | Monitoring | Review status | Last reviewed | Next review date | Removal plan | Linked finding or accepted risk | Validation notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Example Weather Service | Example Provider | public data API | show weather hint in prototype dashboard | product | staging | optional | API key | secret manager | coarse city name | weather summary | none planned | yes | unknown | free-tier documented | status page reviewed | cached placeholder and hide widget | app logs | prototype-only | 2026-05-31 | 2026-06-30 | remove if feature is dropped | none | mocked in tests |
| Example Mapping SDK | Example Provider | client SDK | render optional static map | frontend | prototype | optional | none in client | no secret in browser | coarse coordinates | tiles and map image | none planned | yes | yes with attribution | documented | no SLA | show text fallback if SDK fails | browser console plus app logs | prototype-only | 2026-05-31 | 2026-06-30 | remove if map value is low | accepted prototype risk | visual smoke plus mocked config |

## Extended note

The weather-style API remains blocked for production until timeout handling, graceful degradation, documented review owner and commercial-use confirmation are complete.
