# Vibe Coding Protocols v0.5.2 — Repository UX, npm Entrypoint, and Manifest Cleanup

## Summary

v0.5.2 improves the first-time developer experience:
it cleans up root-level metadata,
simplifies the README,
introduces a local npm entrypoint wrapper,
clarifies Adoption Packs,
shortens safety disclaimers,
improves the roadmap,
and makes advanced CLI/manifests/docs easier to discover without overwhelming new users.

## What changed

- machine-readable manifests moved into `.vcp/manifests/`
- README and README_ru first screen simplified
- local npm wrapper added via `bin/vcp-node.js` and `npm run vcp -- ...`
- `vcp init` added as a guidance-first onboarding command
- Adoption Pack docs now have a quickstart and simpler explanation
- roadmap and measured-impact docs were refreshed without fake claims

## Packaging status

Current local entrypoints:
- `python3 -m vcp_cli ...`
- `py -m vcp_cli ...` on Windows
- `npm run vcp -- ...`
- `npm link` then `vcp ...` locally if desired

Not claimed in this release:
- published npm package
- published PyPI package
- Homebrew distribution
- native Windows installer

## Validation

- Python CLI remains the source of truth
- npm wrapper is a thin local forwarder to the Python CLI
- manifest validation works from `.vcp/manifests/`
- benchmarks remain local and synthetic unless explicitly labelled otherwise
