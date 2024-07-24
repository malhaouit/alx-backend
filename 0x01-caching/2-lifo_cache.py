#!/usr/bin/env python3
"""This module covers LIFO cache replacement policies."""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Implements LIFO cache."""
    def __init__(self):
        """Overloads the __init__ method of the BaseCaching class."""
        super().__init__()
        self.last_key = None

    def put(self, key, item):
        """Adds new item to the cache. If the number of items in the cache is
        higher than MAX_ITEMS, the last added element to the cache will be
        removed first and then the new item will be added.

        Args:
            key (str): The key of the value to add to the cache.
            item (any): The value to add to the cache.
       """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                if self.last_key:
                    print("DISCARD: {}".format(self.last_key))
                    del self.cache_data[self.last_key]

        self.cache_data[key] = item
        self.last_key = key

    def get(self, key):
        """Gets an item from the cache by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The cached item or None if the key is not found.
        """
        return self.cache_data.get(key, None)
