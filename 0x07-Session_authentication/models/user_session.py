#!/usr/bin/env python3
""" Usersession module
"""
from datetime import datetime
from typing import TypeVar, List, Iterable
from models import Base
from os import path
import json
import uuid


class UserSession(Base):
    """Session ID stored in database"""
    def __init__(self, *args: list, **kwargs: dict):
        """init method"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
        