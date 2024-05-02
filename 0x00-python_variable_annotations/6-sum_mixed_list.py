#!/usr/bin/env python3
"""
a module to add a list of integer and floats.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    this function returns the sum of the
    elements in the list that is passed as an argument
    """
    return sum(mxd_lst)
