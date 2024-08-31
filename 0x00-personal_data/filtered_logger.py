#!/usr/bin/env python3
"""solve task
    """

from typing import List
import re
import logging
from mysql import connector
import os


def get_db() -> connector.connection.MySQLConnection:
    """_summary_

    Returns:
        connector.connection.MySQLConnection: _description_
    """
    db = connector.connect(host=os.getenv(
        "PERSONAL_DATA_DB_HOST", "localhost"),
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        database=os.getenv("PERSONAL_DATA_DB_NAME"))
    return db


PII_FIELDS = ("name", "email", "password", "ssn", "phone")


def get_logger() -> logging.Logger:
    logger = logging.Logger("user_data", logging.INFO)
    logger.propagate = False
    target_handler = logging.StreamHandler()
    target_handler.setLevel(logging.INFO)

    formatter = RedactingFormatter(list(PII_FIELDS))
    target_handler.setFormatter(formatter)

    logger.addHandler(target_handler)
    return logger


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


def main() -> None:
    """_summary_
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    headers = [field[0] for field in cursor.description]
    logger = get_logger()

    for row in cursor:
        info_answer = ''
        for f, p in zip(row, headers):
            info_answer += f'{p}={(f)}; '
        logger.info(info_answer)

    cursor.close()
    db.close()


if __name__ == "__main__":

    main()
