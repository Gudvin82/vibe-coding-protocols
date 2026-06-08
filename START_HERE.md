
# Start Here

Use this file to choose the correct VCP path before copying artifacts or
writing code.

## VCP in 60 seconds

VCP is a local-first control layer for AI-built and AI-assisted projects.

It helps teams:
- choose the right route before AI edits expand;
- define intent and control boundaries;
- add PR Gate, proof, trust-check, and release evidence;
- avoid pretending a local toolkit is a hosted platform.

## Choose your adoption mode

- 5 minutes
- 30 minutes
- half day
- full audit

See [docs/guided-adoption-modes.md](./docs/guided-adoption-modes.md).

## Fast path

```bash
python3 -m vcp_cli doctor --json
python3 -m vcp_cli route list --json
python3 -m vcp_cli route recommend --scenario raw-ai-mvp --json
python3 -m vcp_cli trust-check --json
```

## Route selector

- I am brand new to VCP:
  [docs/first-time-adoption.md](./docs/first-time-adoption.md)
- I do not know which VCP path to choose:
  [docs/route-recommender.md](./docs/route-recommender.md)
- I need the product spine first:
  [docs/product-spine.md](./docs/product-spine.md)
- I already have an AI-built MVP and need control before release:
  [docs/mvp-to-launch-path.md](./docs/mvp-to-launch-path.md)
- I want the fastest end-to-end walkthrough:
  [docs/flagship-demo.md](./docs/flagship-demo.md)
- I need a copy-ready local governance starter:
  [docs/portable-control-pack.md](./docs/portable-control-pack.md)
- I need copy-ready AI tool setup kits:
  [docs/integrations/agent-kits.md](./docs/integrations/agent-kits.md)
- I want to evaluate an AI tool/model/stack before adopting it:
  [docs/ai-ecosystem-watchlist.md](./docs/ai-ecosystem-watchlist.md)
- I want to train my team for safer AI coding:
  [docs/secure-agent-training-pack.md](./docs/secure-agent-training-pack.md)
- I want to roll out VCP with a team/client:
  [docs/client-adoption-playbook.md](./docs/client-adoption-playbook.md)
- I need to prepare a PR:
  [docs/pr-readiness.md](./docs/pr-readiness.md)
- AI already created chaos in my repo:
  [docs/anti-chaos-recovery-kit.md](./docs/anti-chaos-recovery-kit.md)
- I am evaluating VCP itself:
  [PUBLIC_EVALUATION_KIT.md](./PUBLIC_EVALUATION_KIT.md)

## Required / recommended / optional

Required first:
- `README.md`
- `docs/first-time-adoption.md`
- `docs/control-spine.md`
- `docs/scope-boundary.md`
- `docs/current-limitations.md`
- `python3 -m vcp_cli trust-check --json`

Recommended next:
- `docs/ai-ecosystem-watchlist.md`
- `docs/model-tool-governance.md`
- `docs/ai-stack-adoption-checklist.md`
- `docs/github-native-control-checklist.md`
- `docs/team-enablement-pack.md`
- `docs/ecosystem-scouting-workflow.md`
- `docs/flagship-demo.md`
- `docs/control-catalog.md`
- `docs/route-recommender.md`
- `docs/guided-adoption-modes.md`
- `docs/evidence-bundle.md`
- `docs/integrations/proof-matrix.md`
- `PUBLIC_EVALUATION_KIT.md`

If you are rolling VCP out with a team or client, start with these three files:
- `START_HERE.md`
- `docs/client-adoption-playbook.md`
- `docs/integrations/agent-kits.md`

When you adopt VCP into another repo, do not copy root `AGENTS.md` blindly.
Prefer `templates/AGENTS.md` or the more specific agent templates first.

Optional layers:
- dashboard artifact
- docs-site scaffold
- presentations destination
- visual proof diagrams

Roadmap-only, not shipped:
- hosted dashboard
- marketplace
- cloud sync
- autonomous orchestration
