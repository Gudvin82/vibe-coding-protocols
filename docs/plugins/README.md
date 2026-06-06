# Plugins

`v0.9.0` introduces plugin architecture preparation, not a plugin marketplace.

Today VCP includes:
- a draft local plugin metadata contract;
- plugin safety guidance;
- a local metadata validation skeleton;
- example plugin metadata under `examples/plugins/`.

It does not include:
- a remote registry;
- an install command;
- auto-execution;
- a marketplace;
- official vendor plugins.

## Local CLI surfaces

```bash
python3 -m vcp_cli plugins list --json
python3 -m vcp_cli plugins validate examples/plugins/example-readiness-check.plugin.json --json
```

These commands inspect metadata only.
They do not execute plugins.

See also:
- `docs/plugins/plugin-contract-draft.md`
- `docs/plugins/plugin-safety.md`
