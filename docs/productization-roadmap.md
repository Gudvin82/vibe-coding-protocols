# Productization Roadmap

`v0.8.1` moves VCP from clone-only usage toward an installable CLI without pretending that every distribution channel is already live.

## What is practical now

- local Python CLI;
- local `python3 -m pip install .`;
- `vcp` console command after local install;
- safe onboarding and classify surfaces;
- non-destructive adoption plans plus explicit safe apply;
- PR Gate workflow template;
- public-growth check/report surfaces;
- repository-backed proof and case-study surfaces.

## What is still planned

- public PyPI publication;
- public npm publication;
- signed package provenance where possible;
- a VS Code extension;
- richer interactive workflow assistance beyond safe preview mode.

## Guardrails

- do not publish registry instructions until packages really exist;
- do not enable destructive apply modes by default;
- do not treat workflow JSON as an execution engine;
- do not list a VS Code Marketplace extension until it is actually shipped.
