#!/usr/bin/env python3
"""handel auth whis class
    """

from typing import List, TypeVar
from flask import request


class Auth:
    """template for all authentication system"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """check if path in excluded_paths"""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        if path[-1] != '/':
            path += '/'
        for exPath in excluded_paths:
            if path == exPath:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """i dont know what is yet"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """i dont know what is yet"""
        return None
