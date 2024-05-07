#!/usr/bin/env python3
"""module for creating asyncorous tasks"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random



def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    function for creating asyncorous task.
    """
    return asyncio.create_task(wait_random(max_delay))