# Progressive Disclosure

## What progressive disclosure means

In VCP, progressive disclosure means an AI agent should start with small metadata or index surfaces, then inspect only the route, protocol, adoption-pack, or concept cards that match the current task, and only after that open the full documents needed for real work.

The goal is not to hide repository detail. The goal is to avoid wasting context on unrelated docs and templates.

## Why VCP needs it

VCP has grown into a large delivery toolkit with many docs, templates, reports, manifests, and benchmark scenarios.

That means:
- README-only evaluation is shallow;
- reading the whole repository burns context;
- large AI agents may still miss important layers if discovery is unstructured;
- cards and indexes make discovery narrower and more repeatable.

## Recommended AI inspection order

1. `AGENTS.md`
2. `AI_EVALUATION_GUIDE.md`
3. `llms.txt`
4. `llms-full.txt` when deeper context is needed
5. `.vcp/index.json`
6. `.vcp/cards/`
7. `.vcp/manifests/`
8. selected docs, protocols, templates, and reports only

## What this is not

This is:
- not an agentskills.io compatibility claim;
- not a security skills catalog;
- not a replacement for full docs;
- not a hidden prompt injection layer.

## How to use it

Implemented CLI examples:

```bash
python3 -m vcp_cli index show
python3 -m vcp_cli index validate
python3 -m vcp_cli index search production
python3 -m vcp_cli cards list
python3 -m vcp_cli cards list --type route
python3 -m vcp_cli cards show production-hardening
python3 -m vcp_cli cards validate
```

Related:
- [vcp-cards.md](./vcp-cards.md)
- [vcp-mappings.md](./vcp-mappings.md)
- [../.vcp/cards/README.md](../.vcp/cards/README.md)
