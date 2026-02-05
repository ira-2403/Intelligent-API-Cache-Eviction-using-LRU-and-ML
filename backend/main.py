from functools import cache
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests,time,json
from backend.cache.lru_cache import LRUCache
from backend.cache.intelligent_lru import IntelligentLRUCache
from backend.utils.logger import log_request
app=FastAPI()
normal_cache=LRUCache(capacity=5)
intelligent_cache=IntelligentLRUCache(capacity=5)
url_frequency={}
last_request_time={}
class RequestModel(BaseModel):
    url:str
@app.post("/request")
def handle_request(request:RequestModel):
    start_time=time.time()
    url=request.url
    url_frequency[url]=url_frequency.get(url,0)+1
    normal_cached=normal_cache.get(url)
    intelligent_cached=intelligent_cache.get(url)
    current_time=time.time()
    time_diff=0
    if url in last_request_time:
        time_diff=current_time-last_request_time[url]
    last_request_time[url]=current_time
    if intelligent_cached:
        response_time=int((time.time()-start_time)*1000)
        data_size=len(json.dumps(intelligent_cached))
        log_request(url,"HIT",response_time,data_size)
        return {
            "data":intelligent_cached,
            "cache_status":"HIT",
            "response_time_ms":response_time,
            "data_size":data_size
            }
    try:
        api_response=requests.get(url)
        api_response.raise_for_status()
        data=api_response.json()
    except Exception as e:
        raise HTTPException(status_code=400,detail=str(e))
    response_time=int((time.time()-start_time)*1000)
    metadata={
        "url_freq":url_frequency[url],
        "cache_hit":0,
        "response_time_ms":response_time,
        "time_diff":time_diff,
        "data_size":len(str(data))
        }
    normal_cache.put(url,data)
    intelligent_cache.put(url,data,metadata)
    data_size=len(json.dumps(data))
    log_request(url,"MISS",response_time,data_size)
    return {
        "data":data,
        "cache_status":"MISS",
        "response_time_ms":response_time,
        "data_size":data_size
    }
@app.get("/stats")
def get_stats():
    i_stats=intelligent_cache.stats()
    i_total=i_stats["hits"]+i_stats["misses"]
    i_hit_rate=i_stats["hits"]/i_total if i_total>0 else 0
    n_stats=normal_cache.stats()
    n_total=n_stats["hits"]+n_stats["misses"]
    n_hit_rate=n_stats["hits"]/n_total if n_total>0 else 0
    return{
        "intelligent_cache":{
            "hits":i_stats["hits"],
            "misses":i_stats["misses"],
            "hit_rate":i_hit_rate,
            "current_size":i_stats["current_size"]
        },
        "normal_cache":{
            "hits":n_stats["hits"],
            "misses":n_stats["misses"],
            "hit_rate":n_hit_rate,
            "current_size":n_stats["current_size"]
        }
    }
@app.get("/comparision")
def comparison():
    normal_stats=normal_cache.stats()
    intelligent_stats=intelligent_cache.stats()
    return{
        "normal_lru":normal_stats,
        "intelligent_lru":intelligent_stats
    }
