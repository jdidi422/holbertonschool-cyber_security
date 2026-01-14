"""Minimal secure reference implementation for password reset flow.

Features:
- tokens are random, single-use, and expire
- generic response to reset requests (no account enumeration)
- host header validation against allowed hosts
- per-IP and per-email rate limiting (simple in-memory)
- logging (no secrets logged)
"""
from datetime import datetime, timedelta
import logging
import secrets
from flask import Flask, request, jsonify, abort
from .token_store import TokenStore
from .rate_limiter import RateLimiter

app = Flask(__name__)
app.config.update(
    ALLOWED_HOSTS={"localhost", "127.0.0.1", "web0x00.hbtn"},
    TOKEN_EXPIRY_MINUTES=15,
)

# Minimal in-memory user "database" (no real emails)
USERS = {"user@example.local": {"id": 1}}

# components
tokens = TokenStore()
rate_limiter = RateLimiter(per_minute=5)

# logging
logger = logging.getLogger("reset_service")
handler = logging.FileHandler("reset_service/reset.log")
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def _validate_host():
    host = request.headers.get("Host", "")
    if ":" in host:
        host = host.split(":")[0]
    if host not in app.config["ALLOWED_HOSTS"]:
        abort(400, description="Invalid Host header")


@app.route("/request-reset", methods=["POST"])
def request_reset():
    _validate_host()
    ip = request.remote_addr or "-"
    email = request.form.get("email", "").strip()

    # rate limit checks
    if not rate_limiter.allow(ip=ip, key=email):
        return jsonify({"status": "ok", "message": "If the email exists, you will receive reset instructions."}), 200

    # If the email exists, create a token; otherwise still return generic response
    if email in USERS:
        token = tokens.create_token(email, expiry_minutes=app.config["TOKEN_EXPIRY_MINUTES"])
        # log event without storing token itself
        logger.info("Password reset requested for existing account: %s", email)
        # NOTE: in a real app, send email containing reset link using configured base URL
    else:
        # log generic event but do not reveal whether email exists
        logger.info("Password reset requested for unknown account or enumeration attempt: %s", email)

    return jsonify({"status": "ok", "message": "If the email exists, you will receive reset instructions."}), 200


@app.route("/reset/<token>", methods=["GET", "POST"])
def reset_token(token):
    _validate_host()
    if request.method == "GET":
        t = tokens.get_token(token)
        if not t or t["used"] or t["expires_at"] < datetime.utcnow():
            abort(404)
        # In a real app render a reset form; here we just indicate valid token
        return jsonify({"status": "ok", "message": "Token valid"}), 200

    # POST -> consume token and set new password (simulated)
    t = tokens.get_token(token)
    if not t or t["used"] or t["expires_at"] < datetime.utcnow():
        abort(404)
    # Consume token
    tokens.consume_token(token)
    # perform password change (omitted) and log event without secrets
    logger.info("Password reset completed for account id=%s", t["email"])
    return jsonify({"status": "ok", "message": "Password has been reset."}), 200


if __name__ == "__main__":
    app.run(port=5001)
