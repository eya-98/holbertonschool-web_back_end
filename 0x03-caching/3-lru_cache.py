#!/usr/bin/env python3
"""Create a class LRUCache that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    keysList = []

    def __init__(self):
        """init function"""
        super().__init__()

    def put(self, key, item):
        """put method"""
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.keysList.pop(self.keysList.index(key))
            if len(
                    self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data.keys():
                print('DISCARD:', end='')
                print(self.keysList[0])
                self.cache_data.pop(
                    list(
                        self.cache_data)[
                        list(
                            self.cache_data).index(
                            '{}'.format(
                                self.keysList[0]))])
                self.keysList.pop(0)
            self.cache_data[key] = item
            self.keysList.append(key)

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            self.keysList.pop(self.keysList.index(key))
            self.keysList.append(key)
            return self.cache_data[key]
