
# Current Limitations

VCP intentionally stays local-first.

It is not SaaS, not a hosted dashboard, not a marketplace, and not an
official IDE extension.

VCP does not create PRs automatically, does not auto-merge, and is not a
full end-to-end security scanner.

VCP gives teams local artifacts, CLI checks, agent kits, PR Gate, proof
surfaces, evidence bundle, and rollout playbooks inside the repository.

## Current boundaries

- no hosted platform;
- no public PyPI/npm publication yet;
- no official VS Code extension;
- no automatic PR creation;
- no auto-merge;
- no compliance certification;
- no launch guarantee;
- no production safety guarantee;
- no telemetry or cloud sync;
- no named company case studies unless explicitly published.

## What is canonical

- `.vcp/` is the canonical machine-readable folder.
- `python3 -m vcp_cli` is the primary source CLI.
- locally installed `vcp` is supported when packaging is installed.
- code/CLI are MIT.
- docs/methodology are CC BY 4.0.
