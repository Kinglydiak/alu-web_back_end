#!/usr/bin/env python3
"""Create a tuple from a string and a number."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return k and the square of v as a tuple."""
    return (k, float(v ** 2))
