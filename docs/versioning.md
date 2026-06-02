# Versioning

This project uses two version lines:

- Repository package `v0.5.2` — GitHub toolkit packaging, CLI, npm wrapper, manifests, benchmarks, examples, CI and docs.
- Web methodology `v1.4` — public methodology pages on `anmalishev.ru`.

Repository package versions track the GitHub-distributed framework.
Methodology version tracks the public web methodology.

Current repository package: `v0.5.2`.
Current web methodology: `v1.4`.

`v0.5.2` is a packaging and repository UX release.
It keeps the existing Python CLI and Bash scripts, moves machine-readable manifests into `.vcp/manifests/`,
adds a local npm wrapper, adds `vcp init`, and makes first-time onboarding lighter without claiming
published npm, PyPI, Homebrew, or native installer distribution.
