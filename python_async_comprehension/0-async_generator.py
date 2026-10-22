#!/usr/bin/env python3
"""Asynchronous generator that yields random numbers."""

import asyncio
import random


async def async_generator():
    """Yield ten random numbers between 0 and 10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
