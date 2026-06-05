# Security Tooling Landscape

VCP is a defensive readiness framework.
It is not a scanner, exploit suite, pentest automation bundle or public API recommendation engine.

## VCP does

- enforce review discipline before risky changes;
- provide hardening and review routes;
- provide third-party dependency and API intake discipline;
- require registry, fallback and data review before production API use.

## VCP does not

- auto-connect external APIs;
- endorse public or free APIs as production-safe;
- replace legal, security or vendor review;
- provide offensive tooling.

## External API rule

If an AI agent wants to add an external API, SDK or webhook provider,
run Third-party API Intake before implementation.
