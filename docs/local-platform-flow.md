# Local Platform Flow

VCP in `v0.8.5` should feel like a coherent local control platform without claiming hosted-platform behavior.

## Flow

```text
intake -> classify -> plan -> memory/backlog -> PR gate -> dashboard -> launch decision
```

## Recommended command path

```bash
vcp doctor --json
vcp onboard --json
vcp classify --json
vcp workflow plan --id mvp-to-launch --json
vcp adopt plan --pack brownfield-rescue --copy-list
vcp pr-gate explain --json
vcp metrics board --json
vcp dashboard build --output ./vcp-dashboard --json
```

Optional workspace flow:

```bash
vcp batch evaluate --targets targets.txt --json
```

## What this means

- local-first;
- no deployment engine;
- no hosted control plane;
- no certification claim;
- reviewable artifacts instead of hidden automation.

## Main artifacts

- `vcp-dashboard/index.html`
- `vcp-dashboard/dashboard.md`
- `vcp-dashboard/project-map.json`
- `vcp-dashboard/run-history.json`
- `vcp-dashboard/integration-status.json`
- `vcp-dashboard/launch-readiness.json`

## Related docs

- [dashboard](./dashboard.md)
- [project map](./project-map.md)
- [run state](./run-state.md)
- [integration packs](./integration-packs.md)
- [launch decision checklist](./launch-decision-checklist.md)
