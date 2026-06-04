# CLI

VCP has practical local entrypaths:
- the Python CLI;
- the installed `vcp` console command after local package install;
- a thin local npm wrapper for Node-first usage.

It does not claim public PyPI or public npm publication unless those packages are actually released.

## Install and run

Recommended local path:

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install .
vcp doctor
```

No-install fallback from a clone:

```bash
python3 -m vcp_cli doctor
```

## Productized starting commands

```bash
vcp onboard --json
vcp classify --json
vcp adopt plan --json
vcp adopt apply --pack brownfield-rescue --target ./target-project --dry-run --json
vcp release-check --json
vcp public-growth check --json
```

## New local-first scaffold commands in `v0.8.2`

```bash
python3 -m vcp_cli dashboard build --output ./vcp-dashboard --json
python3 -m vcp_cli metrics board --json
python3 -m vcp_cli plugins list --json
python3 -m vcp_cli plugins validate examples/plugins/example-readiness-check.plugin.json --json
```

## Safety boundaries

The CLI:
- does not call external AI APIs;
- does not auto-apply adoption packs silently;
- does not overwrite existing files by default in `adopt apply`;
- does not run plugins;
- does not expose a hosted dashboard or hidden execution engine.
