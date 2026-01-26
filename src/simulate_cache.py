from lru_cache import LRUCache
def process_requests_from_file(filename,cache):
    with open(filename,"r") as file:
        for line in file:
            parts=line.strip().split()
            if not parts:
                continue
            if parts[0]=="PUT":
                _, key,value=parts
                cache.put(int(key),value)
            elif parts[0]=="GET":
                _, key=parts
                cache.get(int(key))
            cache.display()
            print("-"*30)
if __name__=="__main__":
    lru=LRUCache(capacity=3)
    process_requests_from_file("requests.txt", lru)
