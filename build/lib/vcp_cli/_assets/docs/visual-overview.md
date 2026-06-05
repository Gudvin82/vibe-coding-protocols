# Visual Overview

Visual overview: `docs/visual-overview.md`

This page gives a fast visual orientation for humans and AI agents without replacing the deeper docs.

## Product delivery lifecycle

```mermaid
flowchart LR
    idea["Idea"] --> intake["AI Intake"]
    intake --> route["Route"]
    route --> spec["Spec Depth"]
    spec --> backlog["Backlog"]
    backlog --> memory["Architecture Memory"]
    memory --> implementation["Implementation"]
    implementation --> review["Review Diff"]
    review --> diagnostics["Diagnostics"]
    diagnostics --> release["Release Gate"]
    release --> followup["Operations / Public Growth"]
```

## AI agent inspection path

```mermaid
flowchart LR
    readme["README"] --> agents["AGENTS.md"]
    agents --> take["TAKE_THIS_FIRST.md"]
    take --> intake["AI_INTAKE.md"]
    intake --> index[".vcp/index.json"]
    index --> cards[".vcp/cards"]
    cards --> docs["Relevant docs"]
```

## Adoption decision flow

```mermaid
flowchart TD
    start["Target project"] --> new["New product"]
    start --> existing["Existing MVP"]
    start --> production["Production project"]
    start --> publicsite["Public site"]
    start --> tiny["Tiny change"]
    new --> starter["Spec-first / Starter"]
    existing --> hardening["Hardening"]
    production --> gates["Diagnostics / Review gates"]
    publicsite --> growth["Public Growth"]
    tiny --> nospec["No-spec + validation"]
```

## Trust gates flow

```mermaid
flowchart LR
    change["AI change"] --> review["review-diff"]
    review --> spec["spec depth check"]
    spec --> backlog["backlog sync"]
    backlog --> architecture["architecture impact"]
    architecture --> validation["validation"]
    validation --> score["score"]
    score --> decision["merge / release decision"]
```

## How to use this page

- Human first impression: read this page, then `docs/demo.md`.
- AI first inspection: use `AGENTS.md`, `TAKE_THIS_FIRST.md`, then this page if lifecycle context is needed.
- Adoption from link: use the decision flow before copying files.
