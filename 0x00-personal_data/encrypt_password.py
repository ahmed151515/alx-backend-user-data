#!/usr/bin/env python3
"""solve task
    """

import bcrypt


def hash_password(password: str):
    """_summary_

    Args:
        password (str): _description_

    Returns:
        str: _description_
    """

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
