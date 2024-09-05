#!/usr/bin/env python3
"""
This module defines the BasicAuth class, which inherits from the Auth class.
"""
from base64 import decode, encode
import re
from auth import Auth


class BasicAuth(Auth):
    """
    Basic authentication class that inherits from Auth.

    Args:
        Auth (class): The parent class for all authentication methods.
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """return  header"""
        if authorization_header is None or type(authorization_header) != str:
            return None
        match = re.search("^Basic ", authorization_header)
        if match is None:
            return None
        value = authorization_header.split(" ")[1]
        return value
