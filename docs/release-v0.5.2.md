# Vibe Coding Protocols v0.5.2 — Repository UX, npm Entrypoint, and Manifest Cleanup

v0.5.2 improves the first-time developer experience:

- repository root is easier to scan;
- machine-readable manifests move into `.vcp/manifests/`;
- a local npm wrapper exists for Node-first usage;
- `vcp init` gives a short guidance-first onboarding step;
- roadmap and measured-impact docs are clearer and more honest.

## Highlights

- Added `bin/vcp-node.js` and documented the local npm wrapper.
- Added `vcp init` in the Python CLI.
- Moved root manifest files into `.vcp/manifests/`.
- Added measured-impact guidance without inventing real-world metrics.
- Simplified README and improved progressive disclosure across docs.

## Boundaries

This release does not claim:

- a published npm package;
- a public `npx` install story;
- a production-grade native Windows installer;
- fake case-study metrics;
- guaranteed AI indexing or ranking.
