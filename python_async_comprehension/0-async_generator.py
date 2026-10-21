#!/usr/bin/env python3
"""Asynchronous generator that yields random numbers."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield ten random numbers, waiting one second before each."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
