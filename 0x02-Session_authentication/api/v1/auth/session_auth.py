#!/usr/bin/env python3
"""
This module defines the SessionAuth class, which inherits from the Auth class.
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """class i dont know yet"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """create session by id"""
        if user_id is None or type(user_id) != str:
            return None
        sessionID = str(uuid4())
        self.user_id_by_session_id[sessionID] = user_id
        return sessionID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        if session_id is None or type(session_id) != str:
            return None
        return self.user_id_by_session_id.get(session_id)
