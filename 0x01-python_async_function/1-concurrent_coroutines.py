#!/usr/bin/env python3
"""
module for implementing asynchronous coroutine.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    this function executes multiple coroutines at the same time with async
    """
    delays = []

    for _ in range(n):
        delays.append(asyncio.run(wait_random(max_delay)))

    return delays
