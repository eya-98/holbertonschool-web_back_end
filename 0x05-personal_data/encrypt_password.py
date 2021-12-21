#!/usr/bin/env python3
"""encrypt password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """return a hashed password"""
    password = password.encode()
    encryptedPassword = bcrypt.hashpw(p, bcrypt.gensalt())
    return (cryptedPassword)
