class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None
class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.cache={}
        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    def _add_node(self,node):
        node.prev=self.head
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
    def _remove_node(self,node):
        prev=node.prev
        nxt=node.next
        prev.next=nxt
        nxt.prev=prev
    def _move_to_front(self,node):
        self._remove_node(node)
        self._add_node(node)
    def _pop_tail(self):
        lru=self.tail.prev
        self._remove_node(lru)
        return lru
    def get(self,key):
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self._move_to_front(node)
        return node.value
    def put(self,key,value):
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self._move_to_front(node)
        else:
            new_node=Node(key,value)
            self.cache[key]=new_node
            self._add_node(new_node)
            if len(self.cache)>self.capacity:
                lru=self._pop_tail()
                del self.cache[lru.key]
cache=LRUCache(2)
cache.put(1,"A")
cache.put(2,"B")
print(cache.get(1))
cache.put(3,"C")
print(cache.get(2))
print(cache.get(3))