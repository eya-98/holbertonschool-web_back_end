#!/usr/bin/env python3
"""Create a class LFUCache that inherits from BaseCaching"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """LFU class inherit from BaseCaching"""
    Frequency = {}

    def __init__(self):
        """init function"""
        super().__init__()

    def get(self, key):
        """get method"""
        if key is None or key not in self.cache_data.keys():
            return None
        else:
            self.Frequency[key] += 1
            return self.cache_data[key]

    def put(self, key, item):
        """put method"""
        if key is not None and item is not None:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.Frequency[key] += 1
            else:
                length = len(self.cache_data.keys())
                self.Frequency[key] = 0
                if length < BaseCaching.MAX_ITEMS:
                    self.cache_data[key] = item
                else:
                    counter = 0
                    list_keys = []
                    for key_item, value in self.Frequency.items():
                        if value == sorted(self.Frequency.values())[0]:
                            counter += 1
                            list_keys.append(key_item)
                    if counter == 1:
                        print('DISCARD: ', end='')
                        The_key = sorted(self.Frequency)[0]
                        print(The_key)
                        self.cache_data.pop(The_key)
                        self.Frequency.pop(The_key)
                        self.cache_data[key] = item
                    else:
                        print('DISCARD: ', end='')
                        print(list_keys[0])
                        The_key = list_keys[0]
                        self.cache_data.pop(The_key)
                        self.Frequency.pop(The_key)
                        self.cache_data[key] = item
