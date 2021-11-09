#!/usr/bin/env python3
"""class that inherits from BaseCaching and is a caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """that inherits from BaseCaching and is a caching system"""
    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key is None:
            pass
        elif key not in self.cache_data.keys():
            pass
        elif key in self.cache_data:
            return self.cache_data[key]
