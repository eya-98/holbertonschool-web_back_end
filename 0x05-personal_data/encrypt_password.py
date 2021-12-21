#!/usr/bin/env python3
"""encrypt password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """return a hashed password"""
    password = password.encode()
    encryptedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
    return (encryptedPassword)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """returns valid or not valid password"""
    return bcrypt.checkpw(password.encode(), hashed_password)
