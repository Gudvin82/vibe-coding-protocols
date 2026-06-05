# SECURITY_NOTES

## Placeholder policy

- `TELEGRAM_BOT_TOKEN=[example-placeholder]`
- `WEBHOOK_SECRET=[example-placeholder]`

## Risks to harden

- secret path or signature validation for webhook
- abuse rate limits
- prompt injection if AI is present
- logging of message content and user identifiers
- TTL and retention for Redis keys
