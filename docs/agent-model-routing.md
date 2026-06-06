# Agent Model Routing

Repository package: `v0.8.8`

Use this guide when you adopt VCP inside your own repository and want to spend AI tokens deliberately.

This is a user-facing routing policy.
It is not a review policy for external evaluators.
It is also not an automatic model router.

## Why VCP cares about model routing

VCP helps teams avoid burning expensive reasoning models on simple repository discovery.

The basic rule is simple:
- use a fast/cheap tier for search, reading, and low-risk discovery;
- use a strong/reasoning tier for mutation, architecture, debugging, and release changes.

Examples may include Haiku or Sonnet, but the policy is provider-neutral.

## Routing table

| Task | Recommended tier | Why |
|---|---|---|
| grep/search files | fast/cheap | deterministic discovery |
| read README/docs | fast/cheap | low-risk context gathering |
| summarize logs/reports | fast/cheap | no mutation |
| locate command/test | fast/cheap | simple lookup |
| write code patch | strong/reasoning | mutation risk |
| change architecture | strong/reasoning | high reasoning load |
| debug complex failure | strong/reasoning | multi-step reasoning |
| update schemas/manifests/tests | strong/reasoning | consistency risk |
| release prep | strong/reasoning | public surface risk |
| security/safety decision | strong/reasoning | high consequence |

## Practical policy

### Fast/cheap tier

Use a fast/cheap model tier for:
- grep/search;
- reading files;
- locating commands;
- summarizing logs;
- checking whether something exists;
- extracting exact file references.

Typical examples:
- Haiku-like models;
- mini/small models;
- cheaper read-oriented subagents.

### Strong/reasoning tier

Use a strong/reasoning model tier for:
- writing patches;
- architecture changes;
- release prep;
- schema/manifest/test updates;
- debugging complex failures;
- safety-sensitive decisions.

Typical examples:
- Sonnet-like models;
- reasoning/pro models;
- main implementation-capable agents.

## Warnings

- Do not use a cheap model to make unreviewed code edits.
- Do not use an expensive model for blind file discovery.
- Search/read first, edit second.
- Always report whether tests were actually run.
- If the current model is too weak for the next step, stop and switch before editing.

## What this does not claim

This guide does not claim:
- automatic model switching inside Claude/Codex/Cursor;
- provider-specific hidden configuration;
- model API automation;
- guaranteed cost savings.

It is a manual operating policy for choosing the right model tier at the right time.
