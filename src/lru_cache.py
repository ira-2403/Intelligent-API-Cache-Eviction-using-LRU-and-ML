# src/lru_cache.py
from collections import OrderedDict
from logger import log_access

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            log_access(key, False)
            return -1

        self.cache.move_to_end(key)
        log_access(key, True)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
