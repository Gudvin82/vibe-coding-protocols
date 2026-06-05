# Public vs Private Documentation

Use this guide to decide what can live in a public repository and what should stay private, sanitized or access-controlled.

## Safe to publish

- public markdown templates;
- reusable checklists;
- vendor-neutral prompts;
- sanitized examples;
- high-level architecture patterns without sensitive operational details;
- release notes and public onboarding docs;
- checksum manifests for public helper scripts.

## Keep private

Do not publish in an open repository:
- secrets;
- internal endpoints;
- internal IP ranges;
- real tokens or credentials;
- admin routes;
- private APIs;
- incident details with operational specifics;
- production configs;
- customer data;
- real on-call or escalation paths;
- detailed architecture diagrams that reveal sensitive operations.

## Sanitize before sharing with AI

Before pasting internal docs into an AI tool:
- remove secrets and tokens;
- replace real customer names and identifiers;
- remove internal hostnames and IPs;
- mask production-only routes and credentials;
- keep only the minimum architecture detail needed for the task.

## Encrypt or restrict access

Real project `AGENTS.md`, `PROJECT_MAP.md`, `ARCHITECTURE_SOURCE_OF_TRUTH.md`, incident runbooks, deployment notes and security docs often contain sensitive details.

Store them in a private repository, encrypted storage or another access-restricted system when they contain operational specifics.

## Architecture Source of Truth policy

The public template in this repository is safe to copy and adapt.

Your real project version may need:
- private deployment paths;
- internal integration notes;
- secret-handling details;
- rollback contacts;
- incident recovery procedures;
- accepted risk ownership.

That real version should usually stay private or be carefully sanitized.

## Review-first public script policy

If you copy a helper script from a public repository:
- download the script first;
- verify the checksum when available;
- review the file locally;
- do not normalize pipe-to-bash for production projects.

## Examples

The examples in this repository are synthetic or sanitized learning material.

They are not claimed as real production projects.
They should not be used as proof that a public project is safe to expose in the same way.
