#!/usr/bin/env python3
"""a function called filter_datum"""
import re
from typing import List
import logging
PII_FIELDS = ("Name", "Address", "Email", "password", "ssn")

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


def get_logger() -> logging.Logger:
    """return logging logger object"""
    logger = logging.getLogger('user_data')
    logger.propagate = False
    logger.setLevel(logging.INFO)
    loggers = logging.StreamHandler()
    loggers.setLevel(logging.INFO)
    formatter = RedactingFormatter(list(PII_FIELDS))
    loggers.setFormatter(formatter)
    logger.addHandler(loggers)
    return logger