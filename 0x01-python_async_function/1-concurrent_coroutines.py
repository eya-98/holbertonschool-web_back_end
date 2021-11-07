#!/usr/bin/env python3
"""multiple coroutines"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    list_w = []
    for i in range(n):
        item = await wait_random(max_delay)
        list_w.append(item)
    return(list_w)