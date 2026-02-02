from collections.abc import Set
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import time
from backend.cache.lru_cache import LRUCache
from backend.utils.logger import log_request
import json
app=FastAPI()
cache=LRUCache(capacity=5)
class RequestModel(BaseModel):
    url:Set[str]
from backend.utils.logger import log_request
import json
@app.post("/request")
def handle_request(request: RequestModel):
    start_time = time.time()

    url = list(request.url)[0]   # extract from set

    cached_response = cache.get(url)
    if cached_response:
        response_time = int((time.time() - start_time) * 1000)
        data_size = len(json.dumps(cached_response))

        log_request(
            url=url,
            cache_status="HIT",
            response_time_ms=response_time,
            data_size=data_size
        )

        return {
            "data": cached_response,
            "cache_status": "HIT",
            "response_time_ms": response_time
        }

    try:
        api_response = requests.get(url)
        api_response.raise_for_status()
        data = api_response.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    cache.put(url, data)

    response_time = int((time.time() - start_time) * 1000)
    data_size = len(json.dumps(data))

    log_request(
        url=url,
        cache_status="MISS",
        response_time_ms=response_time,
        data_size=data_size
    )

    return {
        "data": data,
        "cache_status": "MISS",
        "response_time_ms": response_time
    }
