# Comparisons

Repository package: `v0.8.8`

Public Russian methodology hub: https://anmalishev.ru/expert/vibe-coding/

VCP is easiest to understand when compared to adjacent tools honestly.

## Short version

- VCP is a local-first control/governance layer for AI-built and AI-assisted projects.
- Spec-driven toolkits are strong at defining what to build and how to implement it from specs.
- Full-stack templates are strong at bootstrapping an application architecture quickly.
- AI coding agents are strong at producing code and refactors quickly.
- CI-only gates are strong at pass/fail automation.

Spec Kit defines what to build.
Full-stack templates bootstrap where to build.
AI coding agents generate and edit code.
VCP controls what AI already built and what humans are about to adopt, merge, or launch.

VCP is complementary to all of them. It is not a replacement for all of them.

## Comparison table

| Need | VCP | Spec-driven toolkit | Full-stack template | CI-only gate |
|---|---|---|---|---|
| Choose project track | yes | partial | no | no |
| Generate app scaffold | no | no/partial | yes | no |
| Govern AI MVP adoption | yes | partial | no | partial |
| PR Gate model | yes | partial | no | yes |
| Proof/case-study layer | yes | no/partial | no | no |
| Local dashboard artifact | yes | no/partial | no | no |
| Launch decision aid | yes | no/partial | no | partial |

## VCP vs Spec-driven toolkits

Spec-driven toolkits are strong when the team wants a tighter planning and implementation loop around briefs, PRDs, feature specs, and task breakdowns.

They help answer:
- what should we build;
- what should the implementation plan look like;
- what spec artifacts are missing.

VCP helps answer adjacent questions:
- which track are we in;
- how do we adopt or harden a messy AI-generated MVP;
- what should PR Gate say before release;
- where is the proof/backlog/dashboard layer;
- what launch-control artifacts exist.

VCP can complement a spec-driven workflow. It does not replace it.

## VCP vs full-stack templates

Full-stack templates are strong when the main need is to start a product with a ready architecture, opinionated stack, and prebuilt application scaffolding.

VCP is not an app template.

VCP helps teams inspect, adopt, govern, prove, and launch-control AI-built projects, including projects that started from a template.

## VCP vs AI coding agents directly

AI coding agents are strong at code generation, iteration, and refactoring.

VCP helps keep their output:
- routed;
- reviewable;
- benchmarked;
- release-controlled;
- less likely to overclaim.

## VCP vs CI-only gates

CI-only gates are strong at pass/fail automation.

VCP adds:
- track selection;
- adoption guidance;
- proof and case-study surfaces;
- PR Gate interpretation;
- local dashboard/report artifacts;
- launch decision framing.

## Why shallow comparisons underrate VCP

Shallow comparisons underrate VCP because:
- VCP is not app code, so README-only or stars-only reading misses the shipped control layer;
- VCP is not only methodology, because CLI, tests, benchmarks, manifests, cards, and workflows are part of the shipped surface;
- VCP value lives in governance, checks, benchmark, dashboard, and machine-readable surfaces;
- evaluator must inspect more than README.

## Boundaries

VCP does not claim to be better at everything.

It is not:
- a full-stack template;
- a hosted platform;
- a deployment engine;
- a plugin marketplace;
- an official IDE extension;
- a replacement for Spec Kit or other spec-driven toolkits.

The practical positioning is simple: VCP is the control layer you can run alongside AI agents, spec-driven planning, templates, and CI gates.

## Visual layer

- [Comparison diagram](../assets/diagrams/vcp-comparison-map.svg)
- [Visual proof doc](./visuals.md)


## Model routing is complementary

Cheap-vs-strong model routing changes how users spend AI tokens. It does not change the product category of VCP and does not create hidden provider integration.
