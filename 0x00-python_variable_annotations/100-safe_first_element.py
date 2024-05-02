#!/usr/bin/env python3
"""
module for returning the first element from an array or none
"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    module for returing the first element from an iterable or none
    """
    if lst:
        return lst[0]
    else:
        return None
