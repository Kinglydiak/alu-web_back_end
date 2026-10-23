#!/usr/bin/env python3
"""Hash passwords securely using bcrypt."""

import bcrypt


def hash_password(password: str) -> bytes:
    """Return a salted bcrypt hash of the given password."""
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt)
