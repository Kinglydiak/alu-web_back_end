#!/usr/bin/env python3
"""Filter and format log messages containing sensitive information."""

import logging
import re
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscate the values of specified fields in a log message."""
    pattern = r'(^|{0})({1})=.*?(?={0}|$)'.format(re.escape(separator), '|'.join(map(re.escape, fields)))
    return re.sub(pattern, lambda match: match.group(1) + match.group(2) + '=' + redaction, message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class."""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR)
        record.args = ()
        return super().format(record)


def get_logger() -> logging.Logger:
    """Create a logger that redacts personally identifiable information."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
        logger.addHandler(handler)
    return logger


def get_db():
    """Connect to the holberton database using environment credentials."""
    import os
    import mysql.connector

    return mysql.connector.connect(
        user=os.getenv("PERSONAL_DATA_DB_USERNAME", "root"),
        password=os.getenv("PERSONAL_DATA_DB_PASSWORD", ""),
        host=os.getenv("PERSONAL_DATA_DB_HOST", "localhost"),
        database=os.getenv("PERSONAL_DATA_DB_NAME"),
    )
