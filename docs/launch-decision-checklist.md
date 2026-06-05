# Launch Decision Checklist

Use this checklist when a project is close to launch but still needs visible review and control.

Status labels:
- `go`
- `go-with-warnings`
- `warn`
- `block`
- `no-go`
- `needs-human-review`
- `not-applicable`

## Minimum path

- `vcp doctor --json`
- `vcp classify --json`
- `vcp pr-gate explain --json`
- `vcp dashboard build --output ./vcp-dashboard --json`

## Checkpoints

- current route is understood;
- known blockers are visible;
- PR Gate outcome is explicit;
- dashboard/project map reflects the current state;
- run history source is clear;
- proof layer is honest;
- integration status does not overclaim;
- human launch decision is still explicit.

## Non-goals

This checklist does not certify production safety, launch success, or security compliance.
