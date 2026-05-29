# Windows

VCP is bash-first.

## Support matrix

| Path | Status | Recommended for |
|---|---|---|
| WSL | Recommended | Full script compatibility |
| Git Bash | Supported for most workflows | Users who want Bash scripts on Windows |
| PowerShell wrappers | Beta / limited | Smoke checks and basic validation |
| Native Windows CLI | Not mature yet | Future work |

## Recommended paths

### WSL

Best option if you want the closest behavior to Linux/macOS docs.
Use the same Bash commands shown in README and docs.

### Git Bash

Good option if you want to stay on Windows but still run Bash-first scripts.
Typical commands:

```bash
bash scripts/vibe-check.sh --doctor
python3 scripts/check-newlines.py
python3 scripts/validate-links.sh
```

### PowerShell wrapper

If `scripts/vibe-check.ps1` is present,
you can use it for basic forwarding:

```powershell
pwsh -File scripts/vibe-check.ps1 -Help
pwsh -File scripts/vibe-check.ps1 -Mode doctor
pwsh -File scripts/vibe-check.ps1 -Mode init-report
```

The wrapper does not reimplement the full toolkit.
It forwards to Bash-capable execution paths.

## Running Python checks on Windows

If Python is installed and available as `python` instead of `python3`,
use:

```powershell
python scripts/check-newlines.py
python scripts/validate-links.sh
```

If `python3` is available,
you may use the same commands as the README.

## What to do when shell scripts fail

Try this order:
1. switch to WSL;
2. use Git Bash;
3. use the PowerShell wrapper if the task is limited to basic vibe-check flows;
4. run Python-based checks directly where possible.

## Known limitations

- path handling differences;
- executable bit differences;
- Bash-specific assumptions in several scripts;
- the PowerShell wrapper may not cover all checks;
- CI remains Bash-first today.
