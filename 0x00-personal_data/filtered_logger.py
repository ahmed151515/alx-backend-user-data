#!/usr/bin/env python3
"""solve task 
    """

from typing import List

import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """_summary_

    Returns:
        str: _description_
    """
    for feild in fields:
        message = re.sub(f"{feild}=[^{separator}]+",
                         f"{feild}={redaction}", message)
    return message
