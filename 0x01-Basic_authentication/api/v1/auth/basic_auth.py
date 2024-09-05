#!/usr/bin/env python3
"""
This module defines the BasicAuth class, which inherits from the Auth class.
"""
from base64 import b64decode, b64encode
import re
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """
    Basic authentication class that inherits from Auth.

    Args:
        Auth (class): The parent class for all authentication methods.
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """return  header"""
        if authorization_header is None or type(authorization_header) != str:
            return None
        match = re.search("^Basic ", authorization_header)
        if match is None:
            return None
        value = authorization_header.split(" ")[1]
        return value

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """decode from base64"""
        if base64_authorization_header is None or type(
                base64_authorization_header) != str:
            return None
        try:
            value = b64decode(base64_authorization_header)
            return value.decode("utf-8")
        except Exception as e:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """return email and password as tuple"""
        if decoded_base64_authorization_header is None or type(
                decoded_base64_authorization_header) != str:
            return (None, None)
        match = re.search(":", decoded_base64_authorization_header)
        if match:
            data = decoded_base64_authorization_header.split(":")
            return (data[0], data[1])
        else:
            return (None, None)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """create obj of user"""
        if user_pwd is None or type(user_pwd) != str:
            return None
        if user_email is None or type(user_email) != str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        if len(users) <= 0:
            return None
        if users[0].is_valid_password(user_pwd):
            return users[0]

    def current_user(self, request=None) -> TypeVar('User'):
        """make basic auth finaly"""
        header = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(header)
        decode = self.decode_base64_authorization_header(b64)
        email, password = self.extract_user_credentials(decode)
        return self.user_object_from_credentials(email, password)
