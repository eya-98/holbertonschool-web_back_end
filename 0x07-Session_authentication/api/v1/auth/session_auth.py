#!/usr/bin/env python3
"""class BasicAuth that inherits"""
from flask import request
from typing import List, TypeVar, Tuple
from api.v1.auth.auth import Auth
from models.user import User
import base64


class SessionAuth(Auth):
    """Authentication mechanism"""