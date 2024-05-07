#!/usr/bin/env python3
"""
a module for creating a generator.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> [float, None, None]:
    """
    function for creating a generator.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
