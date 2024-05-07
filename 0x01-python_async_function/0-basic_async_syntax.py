#!/usr/bin/env python3
"""
module for implementing asynchronous coroutine.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    this function implements an asynchronous coroutine.
    """
    _delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(_delay)
    return _delay