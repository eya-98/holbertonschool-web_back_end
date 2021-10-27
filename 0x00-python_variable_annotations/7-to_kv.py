#!/usr/bin/env python3
"""returns a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of an str and sqr of a float or int"""
    return (k, v ** 2)
