# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # fast and slow pointer
        # first pointer goes to k, reverse every node in-between, then both points move 
        # k nodes to reverse the next section
        if not head:
            return None
        dummy = ListNode(-1, head)
        slow = dummy 
        fast = head
        steps = 0

        i = 0
        arr = []
        while fast and i < k:
            arr.append(fast)
            fast = fast.next
            i += 1
            if i == k:
                #print([node.val for node in arr])
                while arr:
                    slow.next = arr.pop()
                    slow = slow.next
                slow.next = None
                arr = []

        while fast:
            arr.append(fast)
            fast = fast.next
            i += 1
            if i % k == 0:
                while arr:
                    slow.next = arr.pop()
                    slow = slow.next
                slow.next = None
                arr = []
        if arr:
            slow.next = arr[0]
        
        return dummy.next