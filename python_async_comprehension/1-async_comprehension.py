#!/usr/bin/env python3
"""Collect random numbers using an asynchronous comprehension."""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect ten random numbers from async_generator."""
    return [number async for number in async_generator()]
