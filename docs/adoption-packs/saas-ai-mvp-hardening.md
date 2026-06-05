# SaaS AI-MVP Hardening Pack

Use this pack when an AI-generated SaaS MVP needs visible control surfaces before wider rollout.

## Checklist focus

- product intent;
- user journey;
- auth boundary;
- workspace and account model;
- billing or credits boundary;
- API contracts;
- environment variables;
- data model;
- observability and logging;
- rate limits;
- abuse prevention;
- support or admin path;
- release readiness;
- PR Gate.

## Discovery

```bash
python3 -m vcp_cli adopt plan --pack saas-ai-mvp-hardening --json
```
