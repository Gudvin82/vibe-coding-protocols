# Starter Template Intake

Use this when adopting any full-stack starter template.

Do not trust “works out of the box” blindly.

Before using a starter template, ask:

1. What stack does it enforce?
2. Which surfaces are active by default?
3. Which surfaces can be deferred?
4. What cloud assumptions does it make?
5. Does it require credentials?
6. Does it have deployment docs?
7. Does it have rollback docs?
8. Does it have auth, session and security defaults?
9. Does it include tests?
10. What should be removed for this project?

## VCP wrapper

Before coding:
- create Product Brief;
- create Architecture Map;
- copy `templates/AGENTS.md`;
- define active, deferred and not-in-scope surfaces;
- run `vibe-check`;
- document third-party dependencies.
