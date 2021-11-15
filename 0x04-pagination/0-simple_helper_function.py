#!/usr/bin/env python3
"""Write a function named index_range"""


def index_range(page: int, page_size: int):
    """index range"""
    a = (page - 1) * page_size
    b = page * page_size
    return (a, b)
