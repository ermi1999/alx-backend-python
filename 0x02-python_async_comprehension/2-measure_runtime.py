#!/usr/bin/env python3
"""
module for measuring parallel comprehensions.
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    this function measures paralallel comprehensions.
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(), async_comprehension())
    total = time.perf_counter() - start
    return total
