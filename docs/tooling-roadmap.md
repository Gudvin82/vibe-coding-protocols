# Tooling Roadmap

VCP is intentionally markdown-first,
with lightweight validation and workflow tooling around it.

## Current tooling

Current repository tooling includes:
- `scripts/vibe-check.sh`;
- `scripts/check-newlines.py`;
- `scripts/validate-links.sh`;
- `scripts/check-version-consistency.sh`;
- `scripts/check-toolkit.sh`;
- `scripts/install-hooks.sh`;
- experimental wrappers and skeletons for npm,
  Python
  and VS Code.

## What tooling can catch today

Current scripts can catch or highlight:
- missing structure;
- version drift;
- broken local markdown links;
- newline-poor or collapsed docs;
- basic toolkit consistency;
- missing AI intake and adoption scaffolding.

## What still requires human review

Human review is still required for:
- architecture quality;
- security posture;
- business logic correctness;
- legal or compliance needs;
- UI design quality;
- whether a refactor is worth doing.

## Not yet available

VCP does not currently provide:
- a deep AST boundary linter;
- a full CLI product;
- a mature IDE extension product;
- a real security scanner;
- domain-specific rule packs.

## Possible future tooling

Potential future tooling may include:
- artifact validator;
- route completeness checker;
- adoption-pack selector;
- adoption assessment validator;
- maintenance report validator;
- AI boundary linting;
- design-system ownership checker;
- migration assistant;
- a unified `vcp` command surface.

## Related docs

- [cli.md](./cli.md)
- [target-project-classifier.md](./target-project-classifier.md)
- [adoption-packs.md](./adoption-packs.md)
- [ide-plugins.md](./ide-plugins.md)
- [boundary-linting.md](./boundary-linting.md)
- [integrations/README.md](./integrations/README.md)
- [public-site-readiness.md](./public-site-readiness.md)
- [security-tooling-landscape.md](./security-tooling-landscape.md)

## Why markdown-first is intentional

Markdown protocols are intentional.
They keep decisions visible,
reviewable
and adaptable across tools.

Automation will be added only where it improves safety
without hiding judgment.
Do not treat current wrappers or skeletons as a mature CLI product.
