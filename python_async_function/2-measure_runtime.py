#!/usr/bin/env python3
"""Measure the average runtime of wait_n."""

import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure wait_n runtime and return elapsed time divided by n."""
    start_time = time.time()
    import asyncio
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time / n
