#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
from typing import Dict, List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the dataset caches."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Return the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE, encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Return the dataset indexed by its original position."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(
        self, index: int = None, page_size: int = 10
    ) -> Dict:
        """Return a page while remaining resilient to deleted rows."""
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        assert index < len(self.dataset())

        data = []
        current_index = index

        while len(data) < page_size and current_index < len(self.dataset()):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        next_index = current_index

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data,
        }
