#!/usr/bin/env python3
"""Write a type-annotated function sum_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum of mixed list items"""
    sum: float = 0
    for i in mxd_lst:
        if i is int:
            i = float(i)
        sum += i
    return sum