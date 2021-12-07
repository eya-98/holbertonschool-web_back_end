#!/usr/bin/env python3
"""a function called filter_datum"""
import re
from typing import Str, List


def filter_datum(fields: List, radaction: Str, message: Str, separator: Str):
    """returns the log message obfuscated"""
    for i in range(len(fields)):
        pattern = re.search('{}=[^{}]*'.format(fields[i], separator), message).group()
        replace = re.sub('=[^{}]*'.format(separator), '={}'.format(radaction), pattern)
        message = re.sub(pattern, replace, message)
    return (message)
