#!/usr/bin/env python3
"""
module for implementing asynchronous coroutine.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    this function executes multiple coroutines at the same time with async
    """
    tasks = []
    delays = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed(tasks):
        delays.append(await task)

    return delays
