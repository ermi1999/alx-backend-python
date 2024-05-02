#!/usr/bin/env python3
"""
module for creating a function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    this function accepts a float and returns
    a mulitiplier function that multiplies the
    argument with the multiplier. 
    """
    def fun(num: float) -> float:
        return multiplier * num
    
    return fun
