param(
  [switch]$Help,
  [string]$Mode = "audit",
  [switch]$Json,
  [switch]$Scanners,
  [switch]$Strict
)

if ($Help) {
  Write-Host "This is a lightweight PowerShell wrapper around scripts/vibe-check.sh."
  Write-Host "Recommended environments: Git Bash or WSL."
  Write-Host "Example: pwsh -File scripts/vibe-check.ps1 -Mode starter"
  exit 0
}

$bash = Get-Command bash -ErrorAction SilentlyContinue
if (-not $bash) {
  Write-Host "bash was not found. Install Git Bash or use WSL, then run scripts/vibe-check.sh."
  exit 1
}

$argsList = @("scripts/vibe-check.sh", "--$Mode")
if ($Json) { $argsList += "--json" }
if ($Scanners) { $argsList += "--scanners" }
if ($Strict) { $argsList += "--strict" }

& bash @argsList
exit $LASTEXITCODE
