#!/usr/bin/env python3
"""Provide utility functions for nested mappings."""

from typing import Any, Mapping, Sequence


def access_nested_map(
    nested_map: Mapping,
    path: Sequence
) -> Any:
    """Retrieve a value from a nested mapping using a sequence of keys."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map
