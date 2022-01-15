#!/usr/bin/env python3
"""class SessionAuth that inherits"""
from flask import request
from typing import List, TypeVar, Tuple
from api.v1.auth.auth import Auth
from models.user import User
import uuid
import base64


class SessionAuth(Auth):
    """Authentication mechanism"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None:
            return None
        if type(user_id) is not str:
            return None
        session = str(uuid.uuid4())
        self.user_id_by_session_id[session] = user_id
        return session

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on a Session ID"""
        if session_id is None:
            return None
        if type(session_id) is not str:
            return None
        id = self.user_id_by_session_id.get(session_id)
        if id is not None:
            return id