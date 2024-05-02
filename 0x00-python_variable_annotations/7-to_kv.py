#!/usr/bin/env python3
"""
module for creating a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    this function takes key and value and
    creates a tuple with those values
    """
    return (k, v ** 2)
