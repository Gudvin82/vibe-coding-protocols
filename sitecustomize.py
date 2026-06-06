from __future__ import annotations

import errno
import subprocess
import time

_ORIGINAL_RUN = subprocess.run
_RETRYABLE_ERRNOS = {errno.EAGAIN, errno.ENOMEM}


def _run_with_retry(*popenargs, **kwargs):
    last_error: OSError | None = None
    for attempt in range(3):
        try:
            return _ORIGINAL_RUN(*popenargs, **kwargs)
        except BlockingIOError as exc:
            if exc.errno not in _RETRYABLE_ERRNOS or attempt == 2:
                raise
            last_error = exc
        except OSError as exc:
            if exc.errno not in _RETRYABLE_ERRNOS or attempt == 2:
                raise
            last_error = exc
        time.sleep(0.2 * (attempt + 1))
    assert last_error is not None
    raise last_error


subprocess.run = _run_with_retry
