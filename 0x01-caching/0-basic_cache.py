#!/usr/bin/env python3
""" This module covers a basic caching.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A basic cache class that inherits from BaseCaching.
    """
    def put(self, key, item):
        """Adds new item to dictionary (cache data).

        Args:
            key (str): The key of the value to add to the cache.
            item (any): The value that to add to the cache.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the cache by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The cached item or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
