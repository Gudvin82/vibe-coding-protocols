# Model / Tool Governance

Repository package: `v0.9.5`

AI models, datasets, agent tools, inference endpoints, UI tools, and evaluation
components behave like project dependencies.
They need review, ownership, and documented boundaries.

## Why this exists

Software teams already review package dependencies.
AI-assisted teams must also review:
- which model or tool is used;
- where data goes;
- which licenses or terms apply;
- what the tool is allowed to do;
- what fallback exists if it fails or becomes unavailable.

## Dependency fields

Each reviewed dependency should document:
- name;
- type;
- source/provider;
- local/cloud/hybrid;
- license;
- terms/usage notes;
- data sensitivity;
- approved usage;
- prohibited usage;
- review owner;
- risk level;
- fallback option;
- last reviewed;
- evidence links.

## Dependency types

- model
- dataset
- agent tool
- inference endpoint
- UI tool
- evaluation tool
- vector store
- automation tool

## Recommended review path

Use this together with:
- [AI Ecosystem Watchlist](./ai-ecosystem-watchlist.md)
- [AI Stack Adoption Checklist](./ai-stack-adoption-checklist.md)
- [Evidence Bundle](./evidence-bundle.md)
- [GitHub-native Control Checklist](./github-native-control-checklist.md)

## Governance questions

1. What data leaves the project boundary?
2. What code or content can the dependency generate or modify?
3. What license or terms matter for client/demo/prod use?
4. Who owns the review and re-review?
5. What is the fallback if the dependency is blocked or disappears?

## Boundaries

- VCP does not provide legal advice.
- VCP does not certify license compliance.
- VCP does not certify vendor security or production readiness.
- VCP helps teams document and review AI dependencies consistently.
