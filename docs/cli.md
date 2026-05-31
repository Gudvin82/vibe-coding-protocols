# CLI

VCP is now script-first plus a real local CLI surface.
Existing scripts remain canonical and supported.
The local `vcp_cli` product layer wraps and organizes those workflows without requiring network or external AI APIs.

## Stable local entrypoint

```bash
python3 -m vcp_cli --help
python3 -m vcp_cli version
python3 -m vcp_cli doctor
python3 -m vcp_cli check --fast
python3 -m vcp_cli route --profile production --json
python3 -m vcp_cli adopt --pack shared-engine --dry-run
python3 -m vcp_cli review plan
python3 -m vcp_cli manifest validate
python3 -m vcp_cli benchmark run
python3 -m vcp_cli score --json
python3 -m vcp_cli demo shared-engine
```

Optional convenience wrapper:

```bash
bin/vcp --help
```

## Commands

- `version` — print package, methodology, manifest schema and git info
- `doctor` — local repository health and discoverability checks
- `check` — safe wrapper around existing validation scripts
- `route` — route selector for target profiles
- `adopt` — adoption dry-run planner
- `score` — heuristic readiness summary
- `manifest` — show and validate machine-readable manifests
- `benchmark` — validate local benchmark scenarios
- `review` — helper for the Post-Task Code Review Gate
- `demo` — print route/adoption demo journeys

## Backward compatibility

Legacy wrapper aliases still delegate to `scripts/vibe-check.sh`:
- `python3 -m vcp_cli audit`
- `python3 -m vcp_cli starter`
- `python3 -m vcp_cli hardening`
- `python3 -m vcp_cli init-report`
- `python3 -m vcp_cli update-advice`

## Safety boundaries

The CLI:
- does not require network;
- does not require GitHub auth;
- does not call external AI APIs;
- does not run offensive tools;
- does not scan third-party targets;
- does not overwrite project files by default.

`adopt` is dry-run by default.
No destructive apply mode is enabled in `v0.5.0`.

## Related docs

- [route-map.md](./route-map.md)
- [protocol-index.md](./protocol-index.md)
- [adoption-packs.md](./adoption-packs.md)
- [demo.md](./demo.md)
- [tooling-roadmap.md](./tooling-roadmap.md)
- [known-limitations.md](./known-limitations.md)
