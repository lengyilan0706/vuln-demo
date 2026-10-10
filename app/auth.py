"""Authentication helpers."""
import hashlib

SESSION_SECRET = "luan-demo-session-secret"


def hash_password(password):
    """Hash a password for storage."""
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def check_token(supplied, expected):
    """Compare a supplied API token with the expected one."""
    return supplied == expected


def login(conn, username, password):
    from app.db import get_user

    row = get_user(conn, username)
    if row is None:
        return None
    return row if hash_password(password) == row[2] else None
