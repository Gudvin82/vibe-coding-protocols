# Changelog

## v0.5.2

- Moved machine-readable manifests from the repository root into `.vcp/manifests/` and updated the CLI, tests, CI and validation scripts to use the cleaner layout
- Simplified the README and README_ru first screen so new users can find the route chooser, AI intake flow, Adoption Packs and current CLI options faster
- Added a local npm wrapper with `npm run vcp -- ...`, `bin/vcp-node.js`, and optional `npm link` support without claiming public npm package publication
- Added `vcp init` as a guidance-first onboarding command with target-specific prompt output
- Added Adoption Pack quickstart, measured-impact guidance, case-study template polish, and phase-based roadmap updates for `v0.6.0` through `v1.0`
- Preserved Python CLI, Bash legacy scripts, Windows-friendly launchers, manifest validation and benchmark validation across the `v0.5.x` feature set

## v0.5.1

- Added Windows-first Python CLI parity for the core fast path, including `doctor`, `check --fast`, `route`, `adopt`, `manifest`, `benchmark` and `score`
- Added PowerShell-friendly launchers in `bin/vcp.cmd` and `bin/vcp.ps1`
- Added Windows CI coverage for Python CLI parity without requiring Bash
- Added Third-party API Intake as a first-class protocol, command, report template, adoption pack and benchmark scenario
- Improved `THIRD_PARTY_REGISTRY` with compact and extended intake fields for safer external dependency review
- Added synthetic integration examples and contribution discipline for catalog-style integration entries

## v0.5.0

- Added a product-grade local `vcp_cli` surface with route, adopt, check, doctor, manifest, benchmark, review and demo commands
- Added machine-readable manifests for routes, packs, commands, reports and benchmarks
- Added AI adoption benchmark scenarios and local benchmark validation
- Added demo docs, route map and sanitized case-study structure
- Added hosted docs readiness docs and community contribution templates
- Preserved script-first workflows and wrapped them safely with `vcp check`

## v0.4.4

- Added a first-class Post-Task Code Review protocol family and `/loop-code-review`
- Added independent-review prompt and code-review report templates
- Added synthetic review examples for acceptance, no-actionable-findings and rejected-finding cases
- Integrated post-task review into AI intake, adoption packs, protocol indexes and route guidance
- Added lightweight `vcp_cli` route, adopt, score and manifest review-gate surfaces
