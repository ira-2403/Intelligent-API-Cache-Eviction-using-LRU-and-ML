from fastapi import FastAPI
from lru_cache import LRUCache
from logger import log_request

app = FastAPI()
cache = LRUCache(capacity=3)

@app.get("/")
def home():
    return {"message": "LRU Cache with Real Requests"}

@app.get("/data/{key}")
def get_data(key: str):
    value = cache.get(key)

    if value == -1:
        # cache miss
        value = f"Generated value for {key}"
        cache.put(key, value)
        log_request(key, hit=False)
        return {"key": key, "value": value, "cache": "MISS"}

    # cache hit
    log_request(key, hit=True)
    return {"key": key, "value": value, "cache": "HIT"}
