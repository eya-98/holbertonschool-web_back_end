#!/usr/bin/env python3
"""Create a class LRUCache that inherits from BaseCaching"""
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRU class inherit from BaseCaching"""

    def __init__(self):
        """init function"""
        super().__init__()
        self.cache_data = OrderedDict()

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]

    def put(self, key, item):
        """put method"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                print('DISCARD:', end='')
                print(list(self.cache_data.keys())[0])
                self.cache_data.popitem(last=False)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
