class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val 
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #map key to nodes

        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head 
        
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            if node == self.head.next:
                return node.val
            else:
                self.remove(node)
                self.insert_head(self.cache[key])
                return node.val

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev 

    def insert_head(self, node):
        node.prev = self.head
        self.head.next.prev = node
        node.next = self.head.next
        self.head.next = node
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
                self.cache[key].val = value
                self.get(key)
                return

        if len(self.cache) < self.capacity:
            node = Node(key, value)
            self.cache[key] = node
            self.insert_head(node)

        else:
            node = self.tail.prev
            self.cache.pop(node.key, None)
            self.remove(self.tail.prev)
            node = Node(key, value)
            self.cache[key] = node
            self.insert_head(node)
        
