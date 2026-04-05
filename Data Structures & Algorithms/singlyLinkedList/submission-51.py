class ListNode:
    def __init__(self, val = -1, nxt = None):
        self.val = val
        self.next = nxt

class LinkedList:
    
    def __init__(self): 
        self.head = ListNode()
        self.tail = ListNode()
    
    def get(self, index: int) -> int:
        print("get")
        curr = self.head.next
        i = 0
        while curr:
            print(curr.val)
            if index == i:
                return curr.val
            i += 1 
            curr = curr.next        
        return -1 
        

    def insertHead(self, val: int) -> None:
        print("insert head:", val)
        node = ListNode(val)
        node.next = self.head.next
        self.head.next = node
        if node.next == None:
            self.tail = node
        print("Tail:", self.tail.val)
        

    def insertTail(self, val: int) -> None:
        print("insert tail:", val)
        node = ListNode(val)
        if self.head.next == None:
            self.head.next = node 
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        print("Tail:", self.tail.val)

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while curr and i < index:
            #Move curr to node before target node
            i += 1
            curr = curr.next

        # if self.head.next == self.tail and index == 0:
        #     self.head.next = None
        #     self.tail = self.head
        #     return True 
        # elif self.head.next == self.tail and index > 0:
        #     return False

        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True 
        return False 

        # if self.head.val == -1:
        #     return False
        # elif self.head == self.tail and index == 0:
        #     self.head = ListNode()
        #     self.tail = ListNode()
        #     return True 
        # elif self.head == self.tail and index > 0:
        #     return False
        # elif index == 0:
        #     self.head = self.head.next
        #     return True
        
        # for i in range(index - 1):
        #     if curr.next == None:
        #         return False
        #     else:
        #         curr = curr.next 
        # if curr.next == self.tail:
        #     curr.next = None
        #     self.tail = curr
        # else:
        #     curr.next = curr.next.next        
        # return True 
        

    def getValues(self) -> List[int]:
        curr = self.head.next
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next 
        return arr
        
