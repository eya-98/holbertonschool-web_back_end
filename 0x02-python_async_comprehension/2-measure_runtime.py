#!/usr/bin/env python3
""" write a measure_runtime coroutine"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """async comprehension"""
    t = time.time()
    coroutine = [async_comprehension() for i in range(4)]
    await asyncio.gather(*coroutine)
    return time.time() - t
