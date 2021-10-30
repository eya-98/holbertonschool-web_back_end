#!/usr/bin/env python3
"""typing"""
from typing import Union, Mapping, Any, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """TypeVar"""
    if key in dct:
        return dct[key]
    else:
        return default
