# Secret Rotation and Storage

## Where secrets should live

- Use a dedicated secret manager, platform environment store or encrypted private ops storage.
- Keep production, staging and test secrets separated.
- Do not store real secrets in public repositories.

## What not to do

- Do not paste secrets into AI prompts.
- Do not leave secrets in screenshots, logs, issue comments or PR descriptions.
- Do not keep live tokens in `.env.example`.
- Do not share production secrets with third-party templates, packages or public demos.

## Rotation triggers

Rotate or revoke secrets when:
- a leak is suspected;
- a token was pasted into the wrong place;
- a contributor or contractor loses access;
- a third-party integration changes scope;
- an incident requires containment;
- scheduled rotation cadence is reached.

## Revocation after leak

1. Disable or revoke the leaked secret.
2. Replace it with a new scoped secret.
3. Review logs and blast radius.
4. Update the security backlog.
5. Document what happened and what evidence exists.

## Scope and least privilege

- Use the smallest possible scope for each token.
- Separate read-only, write and admin credentials.
- Do not reuse the same token across environments.
- Restrict worker and agent tokens to only the APIs they need.

## Audit trail

Track:
- who owns the secret;
- where it is stored;
- what systems use it;
- when it was last rotated;
- what rollback or emergency replacement path exists.
