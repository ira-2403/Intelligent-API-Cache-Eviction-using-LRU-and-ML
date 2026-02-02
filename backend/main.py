from collections.abc import Set
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import time
from backend.cache.lru_cache import LRUCache
app=FastAPI()
cache=LRUCache(capacity=5)
class RequestModel(BaseModel):
    url:Set[str]
@app.post("/request")
def handle_request(request:RequestModel):
    start_time=time.time()
    urls=list(request.url)
    url=urls[0]
    cached_response=cache.get(url)
    if cached_response:
        response_time=int((time.time()-start_time)*1000)
        return {
            "data":cached_response,
            "cache_status":"HIT",
            "response_time_ms":response_time
        }
    try:
        api_response=requests.get(url)
        api_response.raise_for_status()
        data=api_response.json()
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
    cache.put(url,data)
    response_time=int((time.time()-start_time)*1000)
    return {
        "data":data,
        "cache_status":"MISS",
        "response_time_ms":response_time
    }
