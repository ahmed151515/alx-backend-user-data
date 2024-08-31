#!/usr/bin/env python3
"""solve task 
    """

from typing import List

import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        log = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: "
        msg = filter_datum(self.fields, self.REDACTION,
                           record.getMessage(), self.SEPARATOR)
        log += msg


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """_summary_
    Returns:
        str: _description_
    """
    for feild in fields:
        message = re.sub(f"{feild}=[^{separator}]+",
                         f"{feild}={redaction}", message)
    return message
