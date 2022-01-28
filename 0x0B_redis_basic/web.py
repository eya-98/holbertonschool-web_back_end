#!/usr/bin/env python3
"""implementation of a get_page function"""
import requests
import redis
from typing import Callable
from functools import wraps
Redis = redis.Redis()


def page_caching(method: Callable) -> Callable:
    """ Cache page requests
    """
    @wraps(method)
    def cacher(url: str):
        """ Cache page requests for 10sand count access"""
        Redis.incr(f'count:{url}')
        if Redis.exists(f'cache:{url}'):
            return Redis.get(f'cache:{url}')
        page = method(url)
        Redis.set(f'cache:{url}', page)
        Redis.expire(f'cache:{url}', 10)
        return page
    return cacher


@page_caching
def get_page(url: str) -> str:
    """ Request url and return html result """
    return requests.get(url).text
