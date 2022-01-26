#!/usr/bin/env python3
"""Create a Cache Module"""
import uuid
import redis
from typing import Union, Callable, Optional, Any


class Cache:
    """Create a Cache class"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key to the stored data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
