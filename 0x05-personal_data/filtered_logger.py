#!/usr/bin/env python3
"""a function called filter_datum"""
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """returns the log message obfuscated"""
    for i in range(len(fields)):
        pattern = re.search(
            '{}=[^{}]*'.format(fields[i], separator), message).group()
        replace = re.sub(
            '=[^{}]*'.format(separator),
            '={}'.format(redaction),
            pattern)
        message = re.sub(pattern, replace, message)
    return (message)
