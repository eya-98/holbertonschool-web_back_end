#!/usr/bin/env python3
"""a function called filter_datum"""
import re
from typing import List
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init function"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format function"""
        message = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(
            self.fields,
            self.REDACTION,
            message,
            self.SEPARATOR)


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
