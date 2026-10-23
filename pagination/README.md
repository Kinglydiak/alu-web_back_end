# Pagination

This directory contains helper functions and implementations for pagination.

## 0. Simple helper function

The `index_range` function accepts a 1-indexed page number and a page size.
It returns a tuple containing the start index and end index for the requested
page. The start index is inclusive, and the end index is exclusive.
