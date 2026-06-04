# Integration Status Model

VCP uses a conservative status model so integrations can be described without overclaiming hosted services, marketplace listings, or official vendor relationships.

## Statuses

### `shipped`

Use `shipped` only when the surface is implemented in this repository, covered by validation or tests, and documented as usable.

### `local-template`

Use `local-template` when examples, templates, or workflow scaffolds exist, but the user still needs to copy, pin, configure, or review them locally.
It is not a hosted integration and not a marketplace listing.

### `experimental`

Use `experimental` when a scaffold or draft implementation exists, but stability and compatibility are still intentionally limited.
No compatibility guarantee is implied.

### `roadmap`

Use `roadmap` when the repository describes a future direction only.
There is no implementation claim yet.

### `not-shipped`

Use `not-shipped` when the repository explicitly does not provide the surface today.
This is useful when users might otherwise assume it exists.

## Current integration matrix summary

The machine-readable source of truth lives in `.vcp/integrations.json`.

Key examples:
- Python CLI: `shipped`
- installed `vcp` console command after local install: `shipped`
- npm wrapper: `shipped`
- GitHub Actions PR Gate workflow example: `local-template`
- local dashboard artifact: `shipped`
- plugin CLI and contract draft: `experimental`
- PyPI publication: `roadmap`
- npm publication: `roadmap`
- VS Code extension: `roadmap`
- hosted dashboard: `not-shipped`
- plugin marketplace: `not-shipped`
- Go CLI rewrite: `not-shipped`
- web control plane: `not-shipped`
- metrics board: `shipped`
- audit backlog visualization: `shipped`

## How to describe VCP safely

Say:
- local CLI;
- local template;
- experimental plugin scaffold;
- roadmap-only extension concept;
- local dashboard artifact.

Do not say:
- official integration unless one exists;
- hosted dashboard unless one is implemented;
- plugin marketplace;
- public package publication unless it actually happened.
