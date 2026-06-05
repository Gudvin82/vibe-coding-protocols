# Vibe Coding Protocols v0.5.8 — Protocol Cards, Index, and Progressive Disclosure

`v0.5.8` adds a progressive-disclosure discovery layer for VCP. It introduces VCP Cards for routes, protocols, adoption packs, commands and reports, a machine-readable `.vcp/index.json`, CLI index/card commands, and platform compatibility docs so AI agents can understand the repository without reading every file.

## Added in `v0.5.8`

- `.vcp/index.json` as one machine-readable AI-native repository entrypoint
- `.vcp/cards/` with route, protocol, adoption-pack, command, report, and concept cards
- `docs/progressive-disclosure.md`
- `docs/vcp-cards.md`
- `docs/vcp-mappings.md`
- `docs/platforms/` compatibility docs
- `schemas/vcp-card.schema.json`
- `vcp index` and `vcp cards` CLI surfaces

## Important boundaries

`v0.5.8` does **not** claim:

- agentskills.io compatibility
- Anthropic affiliation or endorsement
- official vendor plugins where only docs/prompts exist
- copied cybersecurity skill content
- guaranteed AI citation, indexing, ranking, or AI Overview placement

## Repository impact

This release improves:

- AI-native repository discovery
- progressive disclosure for large-context agents
- platform compatibility documentation
- card-based route inspection before full-doc loading
- index/card validation in CLI, manifests, and benchmark flows
