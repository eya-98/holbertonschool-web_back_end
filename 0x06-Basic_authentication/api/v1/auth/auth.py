#!/usr/bin/env python3
"""Manage the API authentication."""
from flask import request
from typing import List, TypeVar


class Auth:
    """a class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method that returns False"""
        return False

    def authorization_header(self, request=None) -> str:
        """public method that returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """public method that returns None"""
        return None
