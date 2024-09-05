#!/usr/bin/env python3
"""handel auth whis class
    """

from typing import List, TypeVar
from flask import request


class Auth:
    """template for all authentication system"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """i dont know what is yet"""
        return False

    def authorization_header(self, request=None) -> str:
        """i dont know what is yet"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """i dont know what is yet"""
        return None
