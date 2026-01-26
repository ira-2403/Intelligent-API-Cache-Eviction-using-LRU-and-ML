from collections import OrderedDict
class LRUCache:
    def __init__(self,capacity):
        self.cache=OrderedDict()
        self.capacity=capacity
    def get(self,key):
        if key not in self.cache:
            print(f"GET{key}→MISS")
            return -1
        self.cache.move_to_end(key)
        print(f"GET{key}→HIT({self.cache[key]})")
        return self.cache[key]
    def put(self,key,value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key]=value
        if len(self.cache)>self.capacity:
            evicted=self.cache.popitem(last=False)
            print(f"EVICT{evicted}")
        print(f"PUT{key}→{value}")
    def display(self):
        print("CACHE STATE:",list(self.cache.items()))
