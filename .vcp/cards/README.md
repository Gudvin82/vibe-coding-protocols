# VCP Cards

VCP Cards are small machine-readable descriptions of routes, protocols, adoption packs, commands, reports, benchmarks, templates, concepts, platforms, presets, workflows, and diagnostics.

They exist to support progressive disclosure for AI agents and humans.

Read order:
1. `.vcp/index.json`
2. one or more relevant cards
3. full docs only for the selected area

Card directories:
- `routes/`
- `protocols/`
- `adoption-packs/`
- `commands/`
- `reports/`
- `concepts/`
- `platforms/`
- `presets/`
- `workflows/`
- `diagnostics/`

Validation:
- `python3 -m vcp_cli cards validate`
- `python3 -m vcp_cli index validate`
