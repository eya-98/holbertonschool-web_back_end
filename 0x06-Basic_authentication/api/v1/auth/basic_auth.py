#!/usr/bin/env python3
"""class BasicAuth that inherits"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class BasicAuth that inherits"""
