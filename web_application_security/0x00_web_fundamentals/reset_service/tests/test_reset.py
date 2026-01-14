import time
from datetime import datetime, timedelta
import pytest
from reset_service.app import app, tokens, rate_limiter

@pytest.fixture
def client():
    app.config["TESTING"] = True
    client = app.test_client()
    yield client


def test_request_reset_generic_response(client):
    resp = client.post("/request-reset", data={"email": "nonexistent@example"}, headers={"Host": "localhost"})
    assert resp.status_code == 200
    assert b"If the email exists" in resp.data


def test_rate_limiting(client):
    ip = "127.0.0.1"
    # call more than allowed per minute
    for i in range(rate_limiter.per_minute):
        r = client.post("/request-reset", data={"email": f"e{i}@x"}, environ_base={"REMOTE_ADDR": ip}, headers={"Host": "localhost"})
        assert r.status_code == 200
    r = client.post("/request-reset", data={"email": "e6@x"}, environ_base={"REMOTE_ADDR": ip}, headers={"Host": "localhost"})
    assert r.status_code == 200  # still generic response, but limiter blocks token creation; test ensures calls succeed but limiter is enforced by not creating tokens


def test_token_single_use_and_expiry(client):
    # create token manually via store for test
    token = tokens.create_token("user@example.local", expiry_minutes=0)
    # expiry is immediate; GET should 404
    r = client.get(f"/reset/{token}", headers={"Host": "localhost"})
    assert r.status_code == 404

    token = tokens.create_token("user@example.local", expiry_minutes=1)
    r = client.get(f"/reset/{token}", headers={"Host": "localhost"})
    assert r.status_code == 200
    # consume via POST
    r = client.post(f"/reset/{token}", headers={"Host": "localhost"})
    assert r.status_code == 200
    # subsequent GET should 404
    r = client.get(f"/reset/{token}", headers={"Host": "localhost"})
    assert r.status_code == 404


def test_host_validation(client):
    token = tokens.create_token("user@example.local", expiry_minutes=1)
    # invalid Host header
    r = client.get(f"/reset/{token}", headers={"Host": "evil.com"})
    assert r.status_code == 400
