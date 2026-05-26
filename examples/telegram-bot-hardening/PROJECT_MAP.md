# PROJECT_MAP

## Main components

- `bot.py`
- `webhook_handler.py`
- `jobs.py`
- `redis_store.py`

## External dependencies

- Telegram Bot API
- Redis
- optional LLM provider

## Critical flows

- incoming webhook
- command parsing
- outgoing reply
- retry queue for failed sends

## Risks

- duplicate webhook delivery
- token leakage
- abuse through user-generated prompt input
