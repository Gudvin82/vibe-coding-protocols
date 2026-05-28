# Windows

VCP is bash-first.

## Recommended Windows options

Use one of these:
- Git Bash;
- WSL;
- PowerShell with the wrapper in `scripts/vibe-check.ps1`.

## What the PowerShell wrapper does

The wrapper does not reimplement `vibe-check`.
It checks for Bash, Git Bash or WSL and then calls the main shell script.

## Current limits

- native Windows CLI is not available yet;
- some scripts still assume a Bash-style environment;
- optional PowerShell smoke testing depends on `pwsh` being installed.

## Suggested commands

```powershell
pwsh -File scripts/vibe-check.ps1 -Help
pwsh -File scripts/vibe-check.ps1 -Mode doctor
pwsh -File scripts/vibe-check.ps1 -Mode init-report
```
