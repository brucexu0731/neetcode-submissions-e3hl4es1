class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1) 
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        node = ListNode(value)
        if self.isEmpty():
            self.head.next = node
            self.tail.prev = node 
            node.prev = self.head
            node.next = self.tail
        else:
            node.prev = self.tail.prev 
            self.tail.prev.next = node
            self.tail.prev = node
            node.next = self.tail
            print("head:", self.head.next.val)
            print("tail:", self.tail.prev.val)
            

    def appendleft(self, value: int) -> None:
        node = ListNode(value)
        if self.isEmpty():
            self.head.next = node
            self.tail.prev = node 
            node.prev = self.head
            node.next = self.tail
        else:
            node.next = self.head.next 
            node.next.prev = node
            self.head.next = node
            node.prev = self.head

        

    def pop(self) -> int:
        if self.head.next == self.tail:
            return -1
        else:
            result = self.tail.prev.val 
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail 
            return result 
        

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1
        else:
            result = self.head.next.val 
            self.head.next = self.head.next.next
            self.head.next.prev = self.head 
            return result 
        
