class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head 

        self.cache = {}
        self.capacity = capacity 
    
    def remove(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next 
    
    def insert_head(self, node):
        self.head.next.prev = node
        node.next = self.head.next 
        self.head.next = node 
        node.prev = self.head 

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else: 
            node = self.cache[key]
            self.remove(node)
            self.insert_head(node)
            return node.val 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value 
            self.get(key)
            return
        
        if len(self.cache) < self.capacity:
            node = Node(key, value)
            self.cache[key] = node
            self.insert_head(node)
        else:
            node = Node(key, value)

            last = self.tail.prev 
            self.cache.pop(last.key)
            self.remove(last)

            self.cache[key] = node
            self.insert_head(node)
    
        
