#!/usr/bin/env python3
"""class BasicAuth that inherits"""
from flask import request
from typing import List, TypeVar, Tuple
from api.v1.auth.auth import Auth
from models.user import User
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ returns the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            b64 = base64_authorization_header.encode('utf-8')
            str_bytes = base64.b64decode(b64)
            return str_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """ returns the user email and password"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        toCheck = False
        for i in decoded_base64_authorization_header:
            if i == ":":
                toCheck = True
        if not toCheck:
            return (None, None)
        return(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password."""
        if user_email is None or not str:
            return None
        if user_pwd is None or not str:
            return None
        user = User()
        user_searched = user.search({"email": user_email, })
        if not user_searched:
            return None
        user = user_searched[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance"""
        request = self.authorization_header(request)
        header = self.extract_base64_authorization_header(request)
        decodedHeader = self.decode_base64_authorization_header(header)
        user, pwd = self.extract_user_credentials(decodedHeader)
        return self.user_object_from_credentials(user, pwd)
