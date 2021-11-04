#!/usr/bin/env python3
"""asynchronous"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Write an asynchronous coroutine """
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
