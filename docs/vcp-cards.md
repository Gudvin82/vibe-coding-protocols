# VCP Cards

VCP Cards are metadata-first summaries of the most important repository surfaces.

They are designed so AI agents can scan a small JSON object before loading the full route, protocol, or template documentation.

## Card types

Allowed card types:
- `route`
- `protocol`
- `adoption_pack`
- `command`
- `report`
- `template`
- `benchmark`
- `concept`

## Required fields

Each card uses this minimal structure:

```json
{
  "id": "production-hardening",
  "type": "route",
  "name": "Production Hardening",
  "summary": "Use when an existing AI-generated project needs production readiness.",
  "use_when": [],
  "do_not_use_when": [],
  "risk_level": "high",
  "domains": [],
  "maps_to": {
    "sdlc_phase": [],
    "ai_failure_modes": [],
    "project_state": [],
    "risk_categories": []
  },
  "entry_files": [],
  "related_files": [],
  "cli": [],
  "outputs": [],
  "stop_conditions": [],
  "validation": [],
  "version": "v0.5.8"
}
```

## Why cards exist

Cards do not replace full docs.
They reduce context waste and help route discovery stay narrow.

## Validation

- `python3 -m vcp_cli cards validate` validates card fields and linked paths.
- `python3 -m vcp_cli index validate` validates the global index and directory references.

## Related

- [progressive-disclosure.md](./progressive-disclosure.md)
- [vcp-mappings.md](./vcp-mappings.md)
- [../.vcp/cards/README.md](../.vcp/cards/README.md)
