#!/usr/bin/env python3
"""a function called filter_datum"""
import re
from typing import List
import logging
import os
import mysql.connector


PII_FIELDS = ("name", "email", "phone", "password", "ssn")


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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database"""
    database = mysql.connector.connection.MySQLConnection(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME')
    )
    return database


def main():
    """
    Connects to the database `my_db` using `get_db` function, retrieves all
    rows in the `users` table and display each row under a filtered format.
    Filtered PII fields: name, email, phone, ssn, and password.
    Format example:
        [HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***;
        email=***; phone=***; ssn=***; password=***;
        ip=e848:e856:4e0b:a056:54ad:1e98:8110:ce1b;
        last_login=2019-11-14T06:16:24; user_agent=Mozilla/5.0
        (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN);
    """
    database = get_db()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM users;")
    records = []
    for row in cursor:
        message = f"name={row[0]}; email={row[1]}; phone={row[2]}; " \
            f"ssn={row[3]}; password={row[4]}; ip={row[5]}; " \
            f"last_login={row[6]}; user_agent={row[7]};"
        records.append(message)

    logger = get_logger()
    for record in records:
        logger.info(record)
    cursor.close()
    database.close()
