"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visit = {}    
        queue1 = deque()
        queue1.append(node)

        head = Node(node.val, [])
        visit[head.val] = head

        queue2 = deque()
        queue2.append(head)

        while queue1:
            for i in range(len(queue1)):
                n = queue1.popleft()
                c = queue2.popleft()

                for adj in n.neighbors:
                    adj_c = Node(adj.val,[])
                    if adj_c.val in visit:
                        c.neighbors.append(visit[adj_c.val])         
                    else:
                        queue1.append(adj)
                        queue2.append(adj_c)
                        visit[adj_c.val] = adj_c
                        c.neighbors.append(adj_c)
        
        return head 




        