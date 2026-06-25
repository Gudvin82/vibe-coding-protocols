# Vibe Coding Protocols v0.9.5 — AI Review-Engine Positioning and Evaluator Clarity

## Release theme

Sharper category clarity, stronger evaluator guardrails, and more honest
positioning next to dedicated AI review engines.

## What shipped

- a dedicated AI review-engine comparison surface;
- stronger README / evaluator framing around review engines vs governance
  layers;
- clearer “complement, not replacement” guidance for VCP alongside dedicated
  diff/file review tools;
- stronger current-limitations wording around no built-in line-level review
  engine;
- synced current-version markers across evaluator/adopter/public surfaces.

## What did not ship

- a new built-in CLI review engine;
- autonomous line-level PR review comments;
- guaranteed NPE/XSS/SQLi/thread-safety detection;
- official plugin suite;
- IDE extension;
- marketplace install;
- hosted dashboard or SaaS.

## Why this patch exists

VCP was already strong as a governance and rollout layer, but external readers
could still misclassify it as either:
- only documentation;
- only an AI review bot;
- or a replacement for dedicated review-engine products.

`v0.9.5` hardens that public story without pretending a new product capability
already exists.

## Validation status

Use repository checks, trust-check, cards/index validation, and unit tests.

## No-overclaim boundary

VCP complements dedicated AI review engines.
It does not claim to replace them.
