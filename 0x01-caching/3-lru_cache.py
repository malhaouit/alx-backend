#!/usr/bin/env python3
"""This module covers LRU cache replacement policies."""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """Implements LRU cache."""
    def __init__(self):
        """Overloads the __init__ method of the BaseCaching class."""
        super().__init__()
        self.order = []  # List to keep track of the order of keys

    def put(self, key, item):
        """Adds new item to the cache. If the number of items in the cache is
        higher than MAX_ITEMS, the least recently used element in the cache
        will be removed first and then the new item will be added.

        Args:
            key (str): The key of the value to add to the cache.
            item (any): The value to add to the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Gets an item from the cache by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The cached item or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None

        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
