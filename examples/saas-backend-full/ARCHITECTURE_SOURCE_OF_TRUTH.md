# ARCHITECTURE_SOURCE_OF_TRUTH

## Components

- API service
- PostgreSQL database
- worker queue
- object storage

## Public vs private docs note

This file is synthetic. Real architecture docs may need to stay private / sanitized / encrypted.

## Critical flows

- signup
- billing webhook intake
- async job processing
- audit logging
