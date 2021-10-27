#!/usr/bin/env python3
"""a type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(x):
        return x * multiplier
    return multiply
