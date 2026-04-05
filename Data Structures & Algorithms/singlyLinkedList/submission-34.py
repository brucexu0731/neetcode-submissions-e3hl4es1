class ListNode:
    def __init__(self, val = -1, nxt = None):
        self.val = val
        self.next = nxt

class LinkedList:
    
    def __init__(self): 
        self.head = ListNode()
        self.tail = ListNode()
    
    def get(self, index: int) -> int:
        curr = self.head 
        print("Head:", self.head.val)
        for i in range(index):
            print(curr.val)
            curr = curr.next 
            if curr == None:
                return -1
                        
        return curr.val 
        

    def insertHead(self, val: int) -> None:
        node = ListNode(val)
        if self.head.val == -1:
            self.head = node 
            self.tail = node
        else:
            node.next = self.head 
            self.head = node 
        print("head:", self.head.val)
        print("tail:", self.tail.val)
        

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        if self.tail.val == -1:
            self.head = node 
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        print("head:", self.head.val)    
        print("tail:", self.tail.val)
        

    def remove(self, index: int) -> bool:
        print("index:", index)
        curr = self.head 
        if self.head.val == -1:
            return False
        elif self.head == self.tail and index == 0:
            self.head = ListNode()
            self.tail = ListNode()
            return True 
        elif self.head == self.tail and index > 0:
            return False
        elif index == 0:
            self.head = self.head.next
            return True
        
        for i in range(index - 1):
            if curr.next == None:
                return False
            else:
                curr = curr.next 
        if curr.next == self.tail:
            curr.next = None
            self.tail = curr
        else:
            curr.next = curr.next.next        
        return True 
        

    def getValues(self) -> List[int]:
        if self.head.val == -1:
            return []
        curr = self.head 
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next 
        return arr
        
