#!/usr/bin/env python3
"""Create a Cache Module"""
import uuid
import redis
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """increments the count for a key every time the method is called"""
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrapp a function """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    """Create a Cache class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key to the stored data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """convert the data back to the desired format"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Automatically parametrize Cache.get to str"""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Automatically parametrize Cache.get to int"""
        data = self._redis.get(key)
        try:
            data = int(data.decode("utf-8"))
            return data
        except Exception:
            return 0
