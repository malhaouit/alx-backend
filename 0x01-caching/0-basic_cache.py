#!/usr/bin/env python3
""" This module covers a basic caching.
"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Implements some caching basics.
    """
    def put(self, key, item):
        """Adds new item to dictionary (cache data).

        Args:
            key: The key of the value that will be stored to the dictionary.
            item: The value value that will be stored to the dictionary.

        Returns:
            None.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the dictionary based on the key.

        Args:
            key: The key of the value to be searched.

        Returns:
            The value to be searched.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
