#!/usr/bin/env python3
"""This module calculates the start and the end indexes for the given page."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the start index and the end index in a page.

    Args:
        page (int): The number of the page.
        page_size (int): The size of each page.

    Returns:
        A tuple of size two with start_index as the first element and the
        end_index as the second element."""

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
