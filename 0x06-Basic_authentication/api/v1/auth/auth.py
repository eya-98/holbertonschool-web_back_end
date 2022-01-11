#!/usr/bin/env python3
"""Manage the API authentication."""
from flask import request
from typing import List, TypeVar


class Auth:
    """a class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """public method that returns False"""
        if path is not None and excluded_paths is not None:
            for excludedPath in excluded_paths:
                if excludedPath.endswith('/'):
                    excludedPath = excludedPath[:-1]
                if excludedPath in path:
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        """public method that returns None"""
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """public method that returns None"""
        return None
