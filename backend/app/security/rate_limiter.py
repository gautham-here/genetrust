import time
from collections import defaultdict
from fastapi import Request, HTTPException
from typing import Dict, Tuple

_request_counts: Dict[str, Tuple[int, float]] = defaultdict(lambda: (0, time.time()))
RATE_LIMIT = 100
WINDOW_SECONDS = 60


def check_rate_limit(request: Request):
    client_ip = request.client.host if request.client else "unknown"
    count, window_start = _request_counts[client_ip]
    now = time.time()
    if now - window_start > WINDOW_SECONDS:
        _request_counts[client_ip] = (1, now)
    else:
        if count >= RATE_LIMIT:
            raise HTTPException(status_code=429, detail="Rate limit exceeded.")
        _request_counts[client_ip] = (count + 1, window_start)