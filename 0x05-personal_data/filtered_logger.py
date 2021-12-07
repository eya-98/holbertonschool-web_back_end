#!/usr/bin/env python
"""a function called filter_datum"""
import re


def filter_datum(fields, radaction, message, separator):
    """returns the log message obfuscated"""
    for i in range(len(fields)):
        pattern = re.search(
            '{}=[^{}]*'.format(fields[i], separator), message).group()
        replace = re.sub(
            '=[^{}]*'.format(separator),
            '={}'.format(radaction),
            pattern)
        message = re.sub(pattern, replace, message)
    return (message)
