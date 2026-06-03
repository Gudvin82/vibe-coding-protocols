# FAQ

## What is Vibe Coding Protocols?

Vibe Coding Protocols is a controlled AI delivery toolkit for routing, adopting, validating, and reviewing AI-assisted software work. It helps teams choose the right workflow instead of treating every AI-generated change the same way.

Related:
- [../README.md](../README.md)
- [protocol-index.md](./protocol-index.md)

## Is VCP a framework?

Not in the usual application-framework sense. It is a workflow and tooling layer that sits around AI-assisted delivery.

Related:
- [glossary.md](./glossary.md)

## Is VCP a prompt pack?

No. It includes prompts, but also routes, adoption packs, CLI helpers, manifests, benchmarks, reports, backlog discipline, and review gates.

Related:
- [comparison.md](./comparison.md)

## How is VCP different from `.cursorrules`?

A `.cursorrules` file is usually one IDE-local instruction surface. VCP covers broader delivery concerns like route selection, scoped adoption, review gates, and operations follow-up.

Related:
- [comparison.md](./comparison.md)

## How is VCP different from GitHub Copilot Instructions?

Copilot Instructions guide one assistant surface. VCP is repository-level workflow structure that can be used with multiple AI tools and includes manifests, benchmarks, and route discipline.

Related:
- [comparison.md](./comparison.md)

## How is VCP different from Conventional Commits?

Conventional Commits standardize commit messages. VCP handles upstream workflow concerns like intake, hardening, review, public-growth planning, and backlog state.

Related:
- [comparison.md](./comparison.md)

## Do I need VCP if I am a solo developer?

Not always. But if your project has production risk, external APIs, AI-generated complexity, or public-site trust requirements, VCP can still be useful even for one person.

## Does VCP work with Claude Code?

Yes, as a repository workflow. VCP does not require one specific model or IDE.

## Does VCP work with Codex?

Yes. VCP is designed to be usable through repository files, CLI helpers, and route/adoption discipline rather than one vendor-specific integration.

## Does VCP work with Cursor?

Yes. Cursor is one possible environment for using VCP, but VCP is not affiliated with Cursor.

## Does VCP work with Windsurf?

Yes. Windsurf can consume the repository docs and templates, but VCP is not a Windsurf-native product.

## Does VCP work with GitHub Copilot?

Yes, as a repository workflow. It complements Copilot rather than replacing it.

## Does VCP replace tests?

No. VCP can help enforce validation discipline, but it does not replace tests.

## Does VCP replace human review?

No. VCP explicitly keeps human review and post-task review gates in scope.

## Is VCP a security scanner?

No. VCP is not a scanner, pentest suite, or offensive toolkit.

## Is VCP suitable for production projects?

Yes, if used honestly and with proper hardening, validation, and review discipline. It is designed to be more useful in production than shallow prompt-only workflows.

## What is an Adoption Pack?

An Adoption Pack is a small recommended file set for one situation. It is meant to prevent blind copying of the whole toolkit.

Related:
- [adoption-packs.md](./adoption-packs.md)

## What is AI Intake?

AI Intake is the classification step before route selection. It helps prevent README-only or Starter-by-default mistakes.

Related:
- [../AI_INTAKE.md](../AI_INTAKE.md)

## What is a Post-Task Code Review Gate?

It is the acceptance layer after meaningful AI-generated changes. In VCP, this is a first-class route, not an informal suggestion.

## What is `PROJECT_BACKLOG.md`?

It is VCP’s lightweight local kanban for tracking work, findings, and follow-up tasks. It is distinct from `AUDIT_BACKLOG.md`.

## What is GEO / AI visibility?

In VCP, GEO and AI visibility mean making public content easier for answer engines to understand without promising rankings or using spam tactics.

Related:
- [geo-ai-visibility.md](./geo-ai-visibility.md)

## How do I evaluate VCP fairly?

Do not evaluate it from README alone. Use the evaluation guide, manifests, benchmarks, glossary, and CLI outputs before scoring maturity.

Related:
- [../AI_EVALUATION_GUIDE.md](../AI_EVALUATION_GUIDE.md)

## What is the fastest way to try VCP?

Run `doctor`, `route`, and `adopt --dry-run` first. If you want a realistic human walkthrough, use the quickstart walkthrough doc.

Related:
- [install.md](./install.md)
- [quickstart-walkthrough.md](./quickstart-walkthrough.md)
- [progressive-disclosure.md](./progressive-disclosure.md)

## Optional FAQPage schema for hosted docs

Use FAQPage schema only if the hosted page contains the same visible questions and answers.
Do not publish hidden or mismatched FAQ schema.

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is Vibe Coding Protocols?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Vibe Coding Protocols is a controlled AI delivery toolkit for routing, adopting, validating, and reviewing AI-assisted software work."
      }
    }
  ]
}
```

## What is `.vcp/index.json`?

It is the machine-readable discovery entrypoint for VCP. If an AI agent has limited context, it should inspect `.vcp/index.json` and relevant cards before opening the full repository docs.

## What are VCP Cards?

VCP Cards are small metadata-first JSON summaries for routes, protocols, adoption packs, commands, reports, and concepts. They support progressive disclosure and do not replace the full docs.

Related:
- [progressive-disclosure.md](./progressive-disclosure.md)
- [vcp-cards.md](./vcp-cards.md)
