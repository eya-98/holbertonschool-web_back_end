#!/usr/bin/env python
"""a function called filter_datum"""
import re


def filter_datum(fields, radaction, message, separator):
    dic = {}
    field = [re.search('.*?=', message).group()]
    field += re.findall('{}.*?='.format(separator), message)
    value = re.findall('=.*?{}'.format(separator), message)
    for i in range(len(field)):
        field[i] = field[i][:-1]
        if i != 0:
            field[i] = field[i][1:]
        value[i] = value[i][1:]
        value[i] = value[i][:-1]
        dic[field[i]] = value[i]
    for i in fields:
        dic[i] = radaction
    new_string = ''
    for key in dic.keys():
        new_string += '{}'.format(key) + '=' + '{}'.format(dic[key]) + ';'
    return new_string
