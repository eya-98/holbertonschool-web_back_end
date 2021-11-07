#!/usr/bin/env python3
"""multiple coroutines"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """return list of delays in sorting order"""
    list_w = []
    for i in range(n):
        list_w.append(wait_random(max_delay))
    items = []
    for item in asyncio.as_completed(list_w):
        item = await item
        items.append(item)
    return items
