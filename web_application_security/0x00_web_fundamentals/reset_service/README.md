Reference secure password-reset implementation (for guidance and tests).

How to run tests:

- Create a virtualenv and install deps:
  python -m venv .venv && . .venv/bin/activate
  pip install -r reset_service/requirements.txt

- Run tests from repository root:
  pytest reset_service/tests -q

Notes:
- This is a *reference* example to demonstrate secure reset behavior and test coverage.
- It is intentionally minimal and uses in-memory stores for testing; adapt for production (persistent store, email delivery, background jobs).
