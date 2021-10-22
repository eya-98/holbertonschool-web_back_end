#!/usr/bin/env python3
"""Write a type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Write a type-annotated function sum_list"""
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
