#!/usr/bin/env python3
"""
module for creating a list from an iterable
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    this function returns the value with their
    length for each element in the list.
    """
    return [(i, len(i)) for i in lst]
