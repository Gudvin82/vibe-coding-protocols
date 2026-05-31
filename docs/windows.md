# Windows

VCP is now Python-CLI-first for the core workflow on Windows.
Bash is still supported for legacy parity, but it is no longer required for the main fast path.

## Support matrix

| Path | Status | Notes |
|---|---|---|
| PowerShell + Python CLI | Recommended | Core route, check, adopt, score, manifest and benchmark flow |
| Git Bash | Supported | Full legacy script compatibility |
| WSL | Supported | Linux-like environment |
| Native installed `vcp` package | Future | Not published yet |

## Recommended Windows path

```powershell
py -m vcp_cli doctor
py -m vcp_cli check --fast
py -m vcp_cli route --profile production
py -m vcp_cli adopt --pack production --dry-run
py -m vcp_cli score
```

Optional local launchers:

```powershell
bin\vcp.cmd doctor
pwsh -File .\bin\vcp.ps1 check --fast
```

## Optional full Bash compatibility

If you want full legacy script parity:
- Git Bash;
- WSL;
- MSYS2.

Bash is optional for core CLI usage, but it may still be needed for full legacy script parity.

## What works without Bash

The Python CLI fast path is intended to work without Bash for:
- `doctor`;
- `check --fast`;
- `route`;
- `adopt --dry-run`;
- `manifest validate`;
- `benchmark run`;
- `score`.

## Known limitations

- full legacy Bash parity is not complete on native Windows;
- authenticated GitHub release publishing is still external to the CLI;
- PowerShell launchers are local wrappers, not a published installer;
- Windows CI covers Python CLI parity, not every Bash legacy script.
