#!/usr/bin/env python3
"""Provide a helper function for pagination."""


def index_range(page: int, page_size: int) -> tuple:
    """Calculate the start and end indexes for a page."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
