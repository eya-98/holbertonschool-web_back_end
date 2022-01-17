#!/usr/bin/env python3
"""class SessionAuth that inherits"""
from flask import request
from typing import List, TypeVar, Tuple
from api.v1.auth.session_auth import SessionAuth
from models.user import User
import uuid
import base64
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """ an expiration date to a Session ID"""

    def __init__(self):
        """init method"""
        self.session_duration = getenv("SESSION_DURATION")
        if self.session_duration is None:
            self.session_duration = 0
        if self.session_duration.isdigit():
            self.session_duration = int(self.session_duration)
        else:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """Create a Session ID """
        id = super().create_session(user_id)
        if id is None:
            return None
        self.user_id_by_session_id[id] = {
            "user_id": user_id, "created_at": datetime.now()}
        return id

    def user_id_for_session_id(self, session_id=None):
        """user_id_for_session_id"""
        if session_id is None:
            return None
        if session_id not in self.user_id_by_session_id.keys():
            return None
        if self.session_duration <= 0:
            return self.user_id_by_session_id[session_id].get('user_id')
        if "created_at" not in self.user_id_by_session_id[session_id]:
            return None
        timeCreation = self.user_id_by_session_id[session_id]["created_at"]
        TotalTime = timeCreation + timedelta(seconds=self.session_duration)
        if TotalTime < datetime.now():
            return None
        return self.user_id_by_session_id[session_id]['user_id']
