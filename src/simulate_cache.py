from lru_cache import LRUCache
def simulate_requests():
    cache=LRUCache(3)
    requests=[
        (1,"Page_A"),
        (2,"Page_B"),
        (3,"Page_C"),
        (1,None),
        (4,"Page_D"),
        (2,None)
    ]
    for req in requests:
        key,value=req
        if value:
            print(f"PUT {key} -> {value}")
            cache.put(key,value)
        else:
            print(f"GET {key} -> ",cache.get(key))
if __name__=="__main__":
    simulate_requests()