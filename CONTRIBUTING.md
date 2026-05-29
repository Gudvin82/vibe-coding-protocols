# Contributing

Improvements are welcome.

## Principles

- do not add real secrets;
- do not add private project data;
- anonymize or sanitize examples;
- avoid tool-specific lock-in without a clear reason;
- keep the methodology vendor-neutral where practical;
- add attribution when external ideas or discussions are meaningfully referenced;
- do not copy third-party copyrighted prompts,
  skills
  or frameworks verbatim without permission.

## Preferred contribution types

- clearer wording;
- better checklists;
- safer default templates;
- repository structure improvements;
- typo or link fixes;
- new synthetic or sanitized examples;
- better AI IDE guidance;
- lightweight automation improvements for the toolkit itself.

## Feedback channels

See:
- [docs/community-feedback.md](./docs/community-feedback.md)
- [docs/community.md](./docs/community.md)

Use Issues for reproducible bugs,
broken links,
script failures,
unsafe docs
and version drift.

Use Discussions,
if enabled,
for adoption questions,
integration feedback,
ideas,
show-and-tell
and protocol feedback.

## Contributing examples

When proposing examples:
- keep them synthetic or fully sanitized;
- remove client names and project identifiers;
- avoid real tokens,
domains
and customer data;
- explain what is intentionally deferred;
- do not present examples as proof of real production usage.

## Contributing protocol changes

When changing protocols or core routes:
- explain the route impact clearly;
- avoid turning artifacts into routes;
- update related README/docs links if the route changed;
- keep Lite,
  Starter,
  Hardening,
  Maintenance,
  UI Ownership
  and Extended terminology consistent.

## Contributing docs

When changing docs:
- preserve readable markdown formatting;
- avoid flattened sections or broken code fences;
- prefer navigation improvements over mass file moves;
- keep README concise and push depth into docs where possible;
- keep AI-readable raw formatting in mind.

## Before opening a PR

Check that:
- there are no local paths or machine-specific references;
- there are no customer names or internal IPs;
- there are no secret-looking placeholders that resemble real credentials;
- the text does not recommend risky or destructive actions without approval;
- examples stay synthetic or sanitized;
- local scripts and checks still pass.

## Attribution and sources

If your change is inspired by a third-party article,
talk,
thread
or tool:
- cite the source when useful;
- preserve the vendor-neutral spirit of the toolkit;
- avoid copy-pasting copyrighted text;
- explain the adaptation in plain language.
