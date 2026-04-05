# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        currB = headB
        la = 0
        lb = 0
        while currA:
            currA = currA.next
            la += 1
        
        while currB:
            currB = currB.next
            lb += 1
        
        if la > lb:
            while la > lb:
                headA = headA.next
                la -= 1
        
        if la < lb:
            while la < lb:
                headB = headB.next
                lb -= 1
        
        while headA and headB:
            if headA == headB:
                return headA
            else: 
                headA = headA.next
                headB = headB.next
        
        return None 