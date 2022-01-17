#!/usr/bin/env python3
"""class SessionDBAuth that inherits from SessionExpAuth"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta
from os import getenv


class SessionDBAuth(SessionExpAuth):
    """an authentication class"""

    def create_session(self, user_id=None):
        """create session"""
        sessionID = super().create_session(user_id)
        if sessionID is None:
            return None
        else:
            session = {"user_id": user_id, "session_id": sessionID}
            UserSessions = UserSession(**session)
            UserSessions.save()
            return sessionID

    def user_id_for_session_id(self, session_id=None):
        """returns the User ID """
        if session_id is None:
            return None
        UserSession.load_from_file()
        session = UserSession.search({"session_id": session_id})
        if session is None or len(session) == 0:
            return None
        date = (timedelta(seconds=self.session_duration) +
                session[0].created_at)
        if date < datetime.now():
            return None
        return session[0].user_id

    def destroy_session(self, request=None):
        """destroys the UserSession"""
        if request is None:
            return False
        sessionID = self.session_cookie(request)
        if sessionID is None:
            return False
        user = UserSession.search({"session_id": sessionID})
        del self.user_id_by_session_id[sessionID]
        if user is not None and len(user) > 0:
            user[0].remove()
            return True
