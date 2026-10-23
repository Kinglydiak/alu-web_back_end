#!/usr/bin/env python3
"""Filter and obfuscate sensitive information in log messages."""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscate the values of specified fields in a log message."""
    pattern = r'(^|{0})({1})=.*?(?={0}|$)'.format(re.escape(separator), '|'.join(map(re.escape, fields)))
    return re.sub(pattern, lambda match: match.group(1) + match.group(2) + '=' + redaction, message)


if __name__ == "__main__":
    fields = ["password", "date_of_birth"]
    message = "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;"
    print(filter_datum(fields, "xxx", message, ";"))
