# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        print(length)
        
        curr = head
        prev = None
        nxt = None
        for i in range(length // 2):
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt 
        print(curr.val)
        print(nxt.val)
        if not length % 2:
            curr = prev 
        else: 
            curr = prev
            nxt = nxt.next
    
        
        for i in range(length // 2):
            if curr.val != nxt.val:
                return False
            curr = curr.next
            nxt = nxt.next
        
        return True