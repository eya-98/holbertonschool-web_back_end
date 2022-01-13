#!/usr/bin/env python3
"""class BasicAuth that inherits"""
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """class BasicAuth that inherits"""

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """returns the Base64 part of the Authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        string = ""
        i = 0
        while(i < len(authorization_header)):
            if i < 6:
                for j in "Basic ":
                    if j != authorization_header[i]:
                        return None
                    else:
                        i += 1
            else:
                string += authorization_header[i]
                i += 1
        return string
