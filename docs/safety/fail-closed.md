# Fail-closed Safety Boundary

All write-capable, execute-capable, integration-capable, and privileged actions should fail closed unless explicitly requested, confirmed, and scoped.

## Action classes

- read-only;
- report-only;
- local-write;
- project-write;
- execute;
- network;
- credentialed;
- destructive.

## Default policy

- read-only and report-only are allowed;
- local-write requires an explicit output path;
- project-write requires human confirmation;
- execute requires an explicit command or interactive gate;
- network is disabled unless a command clearly documents it;
- credentialed actions are unsupported by default;
- destructive actions are disabled by default.

## Boundaries

- no hidden background actions;
- no autonomous notifications;
- no personal memory;
- no credential vault.
