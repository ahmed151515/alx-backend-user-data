#!/usr/bin/env python3
"""solve task
    """

import bcrypt


def hash_password(password: str) -> bytes:
    """_summary_

    Args:
        password (str): _description_

    Returns:
        str: _description_
    """

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """_summary_

    Args:
        hashed_password (bytes): _description_
        password (str): _description_

    Returns:
        bool: _description_
    """
    return bcrypt.checkpw(hashed_password, password.encode('utf-8'))
