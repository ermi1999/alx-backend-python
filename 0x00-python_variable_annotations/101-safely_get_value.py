#!/usr/bin/env python3
"""
module for safly getting a value from an iterable.
"""
from typing import TypeVar, Union, Any, Mapping
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    this function safly gets a value from a mappable
    """
    if key in dct:
        return dct[key]
    else:
        return default
