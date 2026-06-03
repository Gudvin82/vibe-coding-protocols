# Windows

VCP keeps the Python CLI as the source of truth and adds a simpler local npm wrapper for Node-first users.
Native Windows packaging is still not a mature product in `v0.5.8`.

## Support matrix

| Path | Status | Recommended for |
|---|---|---|
| PowerShell + `py -m vcp_cli` | Recommended | Core cross-platform CLI flow |
| `npm run vcp -- ...` | Recommended | Node-first local repo usage |
| `npm link` + `vcp ...` | Supported locally | Frequent local use after linking |
| Git Bash | Supported | Legacy Bash parity |
| WSL | Supported | Linux-like workflow on Windows |
| Native published Windows installer | Not available yet | Future work |

## Recommended commands

```powershell
py -m vcp_cli doctor
py -m vcp_cli init --print-prompt
py -m vcp_cli route --profile production
npm run vcp -- doctor
npm run vcp -- manifest validate
```

If you linked the package locally:

```powershell
vcp doctor
vcp init --print-prompt
```

## When shell scripts fail

If a Bash-backed script fails on native Windows:
- prefer `py -m vcp_cli check --fast` first;
- use `npm run vcp -- check --fast` if you prefer Node-first invocation;
- switch to Git Bash or WSL for legacy Bash parity.

## Current limitations

- path handling can still differ between PowerShell and Bash-heavy examples;
- executable bits matter less on Windows, so prefer `py -m ...` or `npm run vcp -- ...`;
- PowerShell wrappers are local launchers, not a published installer;
- CI covers the Python fast path and local npm wrapper, not every Bash legacy path;
- global npm registry install is not claimed because no published npm package exists yet.

## Related docs

- [cli.md](./cli.md)
- [npm.md](./npm.md)
- [tooling-roadmap.md](./tooling-roadmap.md)
