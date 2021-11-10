#!/usr/bin/env python3
"""FIFOCache that inherits from BaseCaching and is a caching system:"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """a class FIFOCache"""
    def __init__(self):
        """init function"""
        super().__init__()

    def put(self, key, item):
        """add item or update it"""
        if key is not None and item is not None:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                print('DISCARD:', end='')
                print(list(self.cache_data)[0])
                self.cache_data.pop(list(self.cache_data)[0])
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """"get item from the cache dict"""
        if key is None:
            pass
        elif key not in self.cache_data.keys():
            pass
        elif key in self.cache_data:
            return self.cache_data[key]
