#!/usr/bin/env python3
"""solve task 
    """

from typing import List


def filter_datum(fields: list[str], redaction: str, message: str, separator: str) -> str:
    """_summary_

    Returns:
        str: _description_
    """
    log = message.split(separator)
    for feild in fields:
        for i in range(len(log)):
            if feild in log[i]:
                new = f'{feild}={redaction}'
                log[i] = new
    return f"{separator}".join(log)
