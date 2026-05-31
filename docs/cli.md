# CLI

VCP is script-first plus a real local CLI surface.
The Python CLI is now the preferred cross-platform path for the core workflow, especially on Windows.

## Recommended entrypoints

Linux and macOS:

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli check --fast
python3 -m vcp_cli route --profile production --json
python3 -m vcp_cli adopt --pack production --dry-run --json
python3 -m vcp_cli manifest validate
python3 -m vcp_cli benchmark run
python3 -m vcp_cli score --json
```

Windows PowerShell:

```powershell
py -m vcp_cli doctor
py -m vcp_cli check --fast
py -m vcp_cli route --profile production --json
py -m vcp_cli adopt --pack production --dry-run --json
py -m vcp_cli manifest validate
py -m vcp_cli benchmark run
py -m vcp_cli score --json
```

Optional local wrappers:

```text
bin/vcp
bin/vcp.cmd
bin/vcp.ps1
```

## Commands

- `version` — package, methodology and git info
- `doctor` — repo health, OS and shell capability report
- `check` — Python-native fast checks and optional Bash-backed full checks
- `route` — route selector for target profiles including `third-party-api`
- `adopt` — dry-run pack planner including `third-party-api`
- `score` — heuristic readiness summary
- `manifest` — show and validate manifests
- `benchmark` — validate benchmark scenarios
- `review` — helper for the Post-Task Code Review Gate
- `demo` — print route and adoption demo journeys

## Fast vs full

- `check --fast` is Python-native and intended to work without Bash.
- `check --full` may call legacy Bash scripts when Bash is available.
- If Bash is missing, full legacy checks are reported clearly instead of crashing.

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
- does not auto-connect third-party APIs;
- does not run offensive tools;
- does not overwrite project files by default.

`adopt` is dry-run by default.
Integration ideas should go through Third-party API Intake before implementation code is written.

## Related docs

- [windows.md](./windows.md)
- [protocol-index.md](./protocol-index.md)
- [adoption-packs.md](./adoption-packs.md)
- [tooling-roadmap.md](./tooling-roadmap.md)
- [known-limitations.md](./known-limitations.md)
- [release-v0.5.1.md](./release-v0.5.1.md)
