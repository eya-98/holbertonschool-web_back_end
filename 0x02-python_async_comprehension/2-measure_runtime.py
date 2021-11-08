#!/usr/bin/env python3
""" write a measure_runtime coroutine"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    t = time.time()
    await asyncio.gather(
        *[async_comprehension() for i in range(4)]
    )
    return time.time() - t
