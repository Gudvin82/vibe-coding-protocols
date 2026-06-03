# Glossary

Short terms used across VCP.

## Adoption Pack

A scoped recommended file set for one situation.
It is not a command to copy the whole repository.

## AI Intake

The classification step before choosing a route.
It helps prevent shallow README-only recommendations.

## AI visibility

Whether an AI answer engine can discover and summarize a page.
VCP treats this as a documentation and trust-readiness problem, not a guaranteed ranking outcome.

## Card

A small metadata-first JSON description of a route, protocol, adoption pack, command, report, benchmark, template, or concept.
Cards support progressive disclosure.

## Controlled AI delivery

A workflow where AI-generated work is routed, scoped, validated, and reviewed instead of merged on trust alone.

## GEO

Generative Engine Optimization.
In VCP it means making public content easier for answer engines to understand without using spam, hidden content, or fake proof.

## Index

In VCP, `.vcp/index.json` is the machine-readable repository entrypoint for AI discovery.
It points to entrypoints, cards, manifests, docs, and safety boundaries.

## Manifest

Machine-readable metadata under `.vcp/manifests/`.
The CLI uses manifests for routes, packs, reports, commands, and benchmark validation.

## Page brief

A planning artifact for one page.
It captures audience, intent, proof, internal links, schema, and boundaries before writing.

## Post-task review gate

A required acceptance step after meaningful AI-generated changes.
The gate is represented by the Post-Task Code Review route.

## Progressive disclosure

An inspection pattern where AI first reads small metadata/index files, then relevant cards, then only the full docs needed for the task.

## Public growth

The VCP route for public-facing growth surfaces.
It combines SEO basics, GEO awareness, page-structure discipline, schema honesty, and trust-safe content boundaries.

## Public site readiness

The route for publishing docs, trust pages, and site metadata safely.
It focuses on visibility prerequisites like readable content, trust links, schema alignment, `robots.txt`, and `llms.txt`.

## Review gate

A validation and acceptance checkpoint before merge, release, or deployment.
Not every route uses the same depth, but meaningful work should not bypass it.

## Route

The main workflow path for a target situation, such as production hardening, public growth, maintenance, or operations.

## Thin wrapper

A CLI or integration surface that forwards to a deeper implementation.
In VCP, the local npm entrypoint is a thin wrapper around the Python CLI.
