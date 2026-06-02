# CLI

VCP now has two honest local entrypaths:
- the Python CLI, which remains the primary implementation;
- a thin local npm wrapper for Node-first users.

The repo is not claiming published npm, PyPI, Homebrew, or native installer distribution in `v0.5.2`.

## Start here

Linux and macOS:

```bash
python3 -m vcp_cli doctor
python3 -m vcp_cli route --profile production
python3 -m vcp_cli adopt --pack production --dry-run
```

Local npm wrapper:

```bash
npm run vcp -- doctor
npm run vcp -- route --profile production
npm run vcp -- manifest validate
```

Windows PowerShell:

```powershell
py -m vcp_cli doctor
py -m vcp_cli init --print-prompt
npm run vcp -- doctor
```

## Current commands

- `version` — repository package, methodology, git info
- `doctor` — environment, repo, manifest, and wrapper status
- `check` — Python-native fast checks and optional Bash-backed full checks
- `init` — guidance-only onboarding and copy-paste prompt output
- `route` — choose the route for a target profile
- `adopt` — dry-run an Adoption Pack
- `score` — readiness heuristic summary
- `manifest` — show and validate machine-readable metadata
- `benchmark` — validate route and adoption scenarios
- `review` — helper for the Post-Task Code Review Gate
- `demo` — print small route/adoption demos

## npm wrapper status

Local options that work inside this repository:

```bash
npm install
npm run vcp -- doctor
npm run vcp -- route --profile production
npm run vcp -- manifest validate
```

Optional local linking:

```bash
npm link
vcp doctor
vcp init --print-prompt
```

The wrapper is thin on purpose:
- it does not duplicate CLI logic;
- it detects `python3`, `python`, or `py` depending on platform;
- it fails clearly if Python is unavailable;
- it does not require network;
- it does not publish anything for you.

## Fast vs full

- `check --fast` is Python-native and is the preferred cross-platform path.
- `check --full` may call legacy Bash scripts when Bash is available.
- If Bash is missing, full legacy checks are skipped clearly instead of crashing.

## Init behavior

`vcp init` is guidance-only in `v0.5.2`.
It does not modify files by default.
Use it to:
- print the short onboarding flow;
- print a target-specific prompt with `--print-prompt`;
- steer an AI agent toward `AI_INTAKE.md`, `route`, and `adopt --dry-run`.

## Manifest location

Machine-readable metadata now lives in:
- `.vcp/manifests/`

The CLI prefers `.vcp/manifests/` and can still read legacy root manifests as a fallback if a repository has not been migrated yet.

## Safety boundaries

The CLI:
- does not require network;
- does not call external AI APIs;
- does not connect third-party APIs automatically;
- does not auto-apply Adoption Packs;
- does not run offensive tooling;
- does not replace human review.

## Related docs

- [npm.md](./npm.md)
- [windows.md](./windows.md)
- [init.md](./init.md)
- [adoption-packs.md](./adoption-packs.md)
- [adoption-packs.quickstart.md](./adoption-packs.quickstart.md)
- [tooling-roadmap.md](./tooling-roadmap.md)
- [release-v0.5.2.md](./release-v0.5.2.md)
