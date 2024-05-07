#!/usr/bin/env python3
"""
module for creating async comprehension.
"""
async_generator = __import__('0-async_generator').async_generator
import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    """
    this function returns a list of random floats.
    """
    return [i async for i in async_generator()]
