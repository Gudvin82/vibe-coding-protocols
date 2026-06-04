# Distribution

VCP `v0.8.2` keeps distribution claims honest.
It supports local installation and local wrappers now.
It does not claim public publication until publication actually happens.

## Current honest distribution status

| Path | Status | Command | Notes |
|---|---|---|---|
| Clone + Python module | Shipped | `python3 -m vcp_cli doctor` | No install required |
| Local package install in venv | Shipped | `python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install --upgrade pip setuptools wheel && python3 -m pip install . && vcp doctor` | Primary installable CLI path |
| Local no-build-isolation fallback | Shipped with environment caveat | `python3 -m venv --system-site-packages .venv && . .venv/bin/activate && python3 -m pip install . --no-build-isolation && vcp doctor` | Use only when local build deps are already available |
| `pipx` local path | Supported if available and validation passes | `pipx install . && vcp doctor` | Local path only, not PyPI |
| Node local wrapper | Shipped | `npm run vcp -- doctor` | Local repo path |
| Public PyPI | Roadmap unless published | `pip install vcp-cli` | Do not claim available until actually published |
| Public npm / `npx` | Roadmap unless published | `npx vcp` | Do not claim available today |

## What `v0.8.2` actually adds

- local install reliability guidance;
- conservative packaging metadata;
- local dashboard and plugin scaffold docs that do not depend on publication;
- machine-readable integration status so users can see what is shipped, local-template, experimental, roadmap, or not-shipped.

## Not claimed

`v0.8.2` does not claim:
- public PyPI publication;
- public npm publication;
- a hosted dashboard;
- a plugin marketplace;
- official vendor integrations.
