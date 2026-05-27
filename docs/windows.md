# Windows

Windows support in this repository is lightweight.

## Recommended paths

Use one of these:
- Git Bash;
- WSL;
- PowerShell with the wrapper in `scripts/vibe-check.ps1`.

## What the PowerShell wrapper does

The wrapper does not reimplement `vibe-check`.
It checks for Bash, Git Bash or WSL and then calls the main shell script.

## If Bash is missing

Install Git for Windows or use WSL.
The wrapper will print a friendly message instead of silently failing.

## Notes

- some shell-focused scripts are still Bash-first;
- Windows support here is pragmatic, not a separate product surface.
