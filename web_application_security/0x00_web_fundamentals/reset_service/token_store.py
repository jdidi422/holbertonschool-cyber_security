"""Simple in-memory token store for tests and reference implementation."""
from datetime import datetime, timedelta
import secrets

class TokenStore:
    def __init__(self):
        # token -> {email, expires_at, used}
        self._store = {}

    def create_token(self, email, expiry_minutes=15):
        token = secrets.token_urlsafe(32)
        self._store[token] = {
            "email": email,
            "expires_at": datetime.utcnow() + timedelta(minutes=expiry_minutes),
            "used": False,
        }
        return token

    def get_token(self, token):
        return self._store.get(token)

    def consume_token(self, token):
        if token in self._store:
            self._store[token]["used"] = True

    def cleanup_expired(self):
        now = datetime.utcnow()
        for k in list(self._store.keys()):
            if self._store[k]["expires_at"] < now:
                del self._store[k]
