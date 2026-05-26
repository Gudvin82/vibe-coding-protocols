# AGENTS

## Role

Make atomic, safe changes for the first vertical slice only.

## Stop Conditions

| Condition | Threshold | Required action |
|---|---:|---|
| Changed files | > 10 | Stop, list files, ask approval |
| New dependency | any | Explain package, version, source and risk |
| DB migration | any | Show schema diff and rollback plan |
| External HTTP call | any | Add it to the backlog and explain why |

## Reporting

Always report changed files, validation steps and what remains for Hardening.
