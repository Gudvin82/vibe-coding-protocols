# Tooling Roadmap

## Available in v0.5.6

- local Python CLI
- local npm wrapper that forwards to the Python CLI
- Windows-first PowerShell path for the fast CLI workflow
- Bash-compatible legacy scripts
- machine-readable manifests under `.vcp/manifests/`
- benchmark scenarios
- repository evaluation helper via `vcp evaluate`
- post-task review helper
- third-party API intake protocol and registry discipline
- backlog validation, listing, add/move/done/archive/report output
- operations route docs and report templates for read-only production capture
- runtime backups for backlog writes

## What the tooling can catch today

- missing required structure
- broken local markdown links
- version drift
- manifest consistency
- benchmark scenario consistency
- basic CLI and wrapper smoke
- markdown readability warnings
- missing backlog sections and malformed project backlog headers

## What still requires human review

- architecture quality
- whether a refactor is worth doing
- business logic correctness
- legal or compliance judgment
- whether an external API is acceptable for the target product
- whether a captured production symptom is ready for implementation work
- final release or deployment approval
- public-standard maturity claims

## Still future

- published npm package
- PyPI or pipx packaging
- mature native Windows installer
- deep AST boundary linter
- automatic legal or terms review
- vendor risk automation
- live API monitoring integration
- authenticated GitHub Release publishing from the CLI

See also [public-proof-roadmap.md](./public-proof-roadmap.md), [roadmap.md](./roadmap.md), and [../ROADMAP.md](../ROADMAP.md).
