#!/usr/bin/env python3
"""solve task
    """

from typing import List

import re
import logging


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """_summary_

        Args:
            fields (List[str]): _description_
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """_summary_

        Args:
            record (logging.LogRecord): _description_

        Returns:
            str: _description_
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


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
