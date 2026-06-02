# .vcp

This directory holds VCP machine-readable metadata.

## What is here

- `.vcp/manifests/` contains route, pack, command, report, benchmark, and package metadata.
- The CLI uses these files for `manifest`, `route`, `adopt`, `benchmark`, and `score`.

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
