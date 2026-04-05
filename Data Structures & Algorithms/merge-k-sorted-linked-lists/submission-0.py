# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #temp_min = lists[0]
        head = ListNode(-1)
        curr = head 
        while lists:
        #for i in range(4):
            temp_min = lists[0]
            while None in lists:
                lists.remove(None)
            for node in lists:
                print(node.val)
                if temp_min == None:
                    temp_min = node
                elif node.val < temp_min.val :
                    temp_min = node
                print("min:", temp_min.val)
            for i in range(len(lists)):
                print("2nd iteration:", lists[i].val)
                if lists[i].val == temp_min.val:
                    lists[i] = lists[i].next
                    break  
            curr.next = temp_min
            curr = curr.next 
        return head.next 

                
