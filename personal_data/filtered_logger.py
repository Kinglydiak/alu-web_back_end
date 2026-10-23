#!/usr/bin/env python3
"""Filter and obfuscate sensitive fields in log messages."""

import re
from typing import List


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    """Obfuscate the values of specified fields in a log message."""
    pattern = r'(?<=' + re.escape(separator) + r'|^)(?:' + '|'.join(map(re.escape, fields)) + r')=[^' + re.escape(separator) + r']*'
    return re.sub(pattern, lambda match: match.group().split('=', 1)[0] + '=' + redaction, message)
