# Control Catalog

Repository package: `v0.9.4`

VCP is a local-first AI control platform for AI-built and AI-assisted projects.

The Control Catalog is the fastest way for a human or AI agent to see what VCP actually ships, when to use it, and what is still roadmap-only.

## Categories

1. Core commands
2. Guided paths
3. Adoption packs
4. Report templates
5. Agent rule profiles
6. Evaluator surfaces
7. Proof and evidence surfaces
8. Diagrams and presentations
9. Integration packs
10. Roadmap-only surfaces

## Status model

- `shipped`: available now
- `optional`: shipped but not always required
- `experimental`: shipped with bounded expectations
- `roadmap-only`: described but not implemented
- `not-shipped`: intentionally absent

## Use it

- read `.vcp/control-catalog.json` for machine-readable discovery
- run `python3 -m vcp_cli catalog list --json` for a stable list
- run `python3 -m vcp_cli catalog explain --id mvp-to-launch --json` for a single entry

## Boundaries

The control catalog is local, read-only, and documentation-first. It does not turn VCP into a hosted marketplace or remote registry.
