#!/usr/bin/env python3
"""This module splits the dataset into manageable pages."""
import csv
import math
from typing import List, Dict, Union, Optional

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of lists representing the data on the
            requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_index, end_index = index_range(page, page_size)
        data_set = self.dataset()

        if start_index >= len(data_set):
            return []

        return data_set[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[
            str, Union[int, List[List], Optional[int]]]:
        """Provides hypermedia pagination.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            Dict[str, Union[int, List[List], Optional[int]]]: A dictionary
            containing pagination details.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.floor((total_items + page_size - 1) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
