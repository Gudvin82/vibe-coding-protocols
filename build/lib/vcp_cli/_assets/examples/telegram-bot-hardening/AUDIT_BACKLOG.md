# AUDIT_BACKLOG

| ID | Severity | Finding | Status | Follow-up |
| --- | --- | --- | --- | --- |
| BOT-001 | high | Bot token was referenced in a deployment note and must stay outside repo. | Open | Move to secret manager and scrub docs. |
| BOT-002 | medium | Webhook requests need signature or secret-path validation. | Open | Add verification and document retry behavior. |
| BOT-003 | medium | AI reply flow lacks prompt injection abuse notes. | Open | Add abuse cases and manual override path. |
