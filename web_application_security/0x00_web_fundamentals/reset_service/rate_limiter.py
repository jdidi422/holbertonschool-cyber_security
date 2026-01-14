"""Very small rate limiter for tests: allows N requests per minute per (ip,key) pair."""
from collections import deque
from datetime import datetime, timedelta

class RateLimiter:
    def __init__(self, per_minute=5):
        self.per_minute = per_minute
        # (ip,key) -> deque[timestamps]
        self._store = {}

    def allow(self, ip, key):
        k = (ip, key)
        now = datetime.utcnow()
        window_start = now - timedelta(minutes=1)
        q = self._store.setdefault(k, deque())
        # remove old
        while q and q[0] < window_start:
            q.popleft()
        if len(q) >= self.per_minute:
            return False
        q.append(now)
        return True
