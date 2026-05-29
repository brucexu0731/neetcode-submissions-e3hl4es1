# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # iterate through each node, add them 
        # if one runs out, the remainder of the other gets appended 
        # if the sum exceeds 10, we carry 1 digit ahead 
        # if both lists run out and we still have a carry, create a new node 
        # at the end

        head = ListNode(None)
        carry = 0
        curr = head 

        while l1 and l2:
            curr_sum = l1.val + l2.val + carry
            if curr_sum >= 10:
                curr_val = curr_sum % 10
                carry = 1 
            else:
                curr_val = curr_sum
                carry = 0
            curr.next = ListNode(curr_val)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        #if l1 is longer
        while l1:
            curr_sum = l1.val + carry
            if curr_sum >= 10:
                curr_val = curr_sum % 10
                carry = 1 
            else:
                curr_val = curr_sum
                carry = 0
            curr.next = ListNode(curr_val)
            curr = curr.next
            l1 = l1.next
        
        #if l2 is longer
        while l2:
            curr_sum = l2.val + carry
            if curr_sum >= 10:
                curr_val = curr_sum % 10
                carry = 1 
            else:
                curr_val = curr_sum
                carry = 0
            curr.next = ListNode(curr_val)
            curr = curr.next
            l2 = l2.next
        
        #if there's a carry left
        if carry:
            curr.next = ListNode(1)

        return head.next

        



