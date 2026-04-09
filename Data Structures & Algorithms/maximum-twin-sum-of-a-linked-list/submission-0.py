# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
    # Store each node in an array 
    # [ 1, 2, 3, 4, 5, 6]
    # L -> 1 
    # R -> 6 
    # 7, 7, 7 -> compare and find maximum 
    # Return maximum twin sum 
    # Edge cases: 1. no odd number lists -> every index should have a twin
    # 2. [] --> return 0 
    # 3. 2 elements -> return the sum 

    # More space efficient method would be:
    # --> reverse the second half of the linked list, then we can traverse simultaneously 
    # from the ends to middle and compute sums O(n) time, O(1) space 

        if not head:
            return 0
        
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None

        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt 
        
        curr = prev 
        front = head

        max_sum = 0
        while front and curr:
            max_sum = max(max_sum, front.val + curr.val)
            front = front.next 
            curr = curr.next 
        
        return max_sum

        







