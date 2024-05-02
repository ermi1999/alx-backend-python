#!/usr/bin/env python3
"""
a module to add a list of integer and floats.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
