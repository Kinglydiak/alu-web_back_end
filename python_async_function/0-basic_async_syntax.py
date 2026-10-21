#!/usr/bin/env python3
"""Basic asynchronous syntax."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between zero and max_delay seconds."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
