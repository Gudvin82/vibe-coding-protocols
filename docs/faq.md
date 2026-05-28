# FAQ

## Is VCP a framework?

No. It is a configuration and workflow layer around AI-assisted delivery.

## Is this a security scanner?

No. `vibe-check` is a lightweight readiness signal, not a security scanner.

## Do I need all templates?

No. Start with the smallest route that fits your project.

## What is the difference between Lite, Starter, Hardening, Maintenance Refactoring and Extended?

- Lite: smallest safe onboarding path for solo or MVP work
- Starter: new project with explicit setup
- Hardening: existing AI-generated code needs readiness and security review
- Maintenance Refactoring: existing working project needs scoped behavior-preserving cleanup
- UI Component Ownership: existing frontend needs styling and component ownership cleanup
- Extended: public, client-facing or production-bound path

## What should I copy first?

Usually `templates/AGENTS.md`, `templates/PROJECT_MAP.md`, `templates/AUDIT_BACKLOG.md` and a Product Brief prompt.

## What is `AGENTS.md` vs `templates/AGENTS.md`?

Root `AGENTS.md` configures this repository.
`templates/AGENTS.md` is the generic copy-ready template for your project.

## Can I use this with Cursor, Windsurf or Copilot?

Yes. The toolkit is vendor-neutral and includes IDE-specific guidance where useful.

## Is this production-ready?

The toolkit can support production-bound work, but it does not make a project safe by default.

## How do I update copied templates?

Compare your local artifact with the current template, copy only useful changes and keep project-specific rules intact.

## Why are there two versions: repo `v0.2.x` and methodology `v1.4`?

The repository package version tracks GitHub toolkit packaging.
The methodology version tracks the public web methodology.
