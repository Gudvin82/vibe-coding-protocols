# PROJECT_MAP

## Core files

- `bot.py`
- `webhook_handler.py`
- `redis_store.py`
- `message_pipeline.py`

## Critical flows

- Telegram webhook intake
- command parsing
- response generation
- Redis-backed temporary state

## External dependencies

- Telegram Bot API
- Redis
- optional AI provider
