# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visit = set()
        curr = head
        while curr:
            visit.add(curr)
            if curr.next in visit:
                return True
            curr = curr.next
        
        return False
        