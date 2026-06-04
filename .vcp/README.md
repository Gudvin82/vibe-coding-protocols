# .vcp

This directory holds VCP machine-readable metadata.

## What is here

- `.vcp/index.json` is the machine-readable repository entrypoint for progressive disclosure.
- `.vcp/ai-audit-manifest.json` defines the required inspection path for AI agents that claim a full VCP evaluation.
- `.vcp/cards/` contains metadata-first cards for routes, protocols, packs, commands, reports, and concepts.
- `.vcp/manifests/` contains route, pack, command, report, benchmark, and package metadata.
- The CLI uses these files for `manifest`, `route`, `adopt`, `benchmark`, `score`, and backlog-aware validation.

## Do most users need to edit this?

No.
Most users should work with:
- `README.md`
- `START_HERE.md`
- `AI_INTAKE.md`
- `docs/`
- `protocols/`
- `templates/`

Edit `.vcp/` only if you are maintaining machine-readable metadata for the toolkit itself.
