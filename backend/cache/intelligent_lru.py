from backend.cache.lru_cache import LRUCache
from backend.ml.predictor import CacheReusePredictor
class IntelligentLRUCache(LRUCache):
    def __init__(self,capacity:int):
        super().__init__(capacity)
        self.predictor=CacheReusePredictor()
        self.metadata_store={}
    def calculate_score(self,metadata):
        score=(
            metadata.get("url_freq",0)*2+
            metadata.get("cache_hit",0)*5+
            metadata.get("response_time_ms",0)/100-
            metadata.get("time_diff",0)/50-
            metadata.get("data_size",0)/1000)
        return score
    def get_lowest_score_key(self):
        lowest_key=None
        lowest_score=float("inf")
        for key in self.cache.keys():
            metadata=self.metadata_store.get(key,{})
            score=self.calculate_score(metadata)
            if score< lowest_score:
                lowest_score=score
                lowest_key=key
        print(lowest_key,lowest_score)
        return lowest_key
    def put(self,key,value,metadata:None):
        if metadata is None:
            metadata={
                "url_freq":1,
                "cache_hit":0,
                "response_time_ms":100,
                "time_diff":1,
                "data_size":500
            }
        self.metadata_store[key]=metadata
        if self.size<self.capacity:
            super().put(key,value)
            return
        evict_key=None
        try:
            prediction=self.predictor.predict(metadata)
        except Exception:
            prediction=0
        evict_key=self.get_lowest_score_key()
        if evict_key:
            node=self.cache.get(evict_key)
            if node:
                self._remove_node(node)
                del self.cache[evict_key]
                self.metadata_store.pop(evict_key,None)
                self.size-=1
        super().put(key,value)
    def get(self,key):
        value=super().get(key)
        if value is not None:
            metadata=self.metadata_store.get(key,{})
            metadata["cache_hit"]=metadata.get("cache_hit",0)+1
            metadata["url_freq"]=metadata.get("url_freq",0)+1
            self.metadata_store[key]=metadata
        return value    