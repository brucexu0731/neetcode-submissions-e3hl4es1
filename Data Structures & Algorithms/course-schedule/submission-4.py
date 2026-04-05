
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = [] 
        self.next = [] 
    
    def search_prev(self, node):

        q = deque()
        visit = set()
        q.append(self)
        
        while q:
            for i in range(len(q)):
                course = q.popleft()
                if course == node:
                    return True
                 
                for c in course.prev:
                    if c in visit:
                        continue 
                    q.append(c)
                    visit.add(c)
        return False


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}

        for a, b in prerequisites:
            if a == b:
                return False
            if a in adj and b in adj:
                A = adj[a]
                B = adj[b]
                if B.search_prev(A):
                    return False
            if a not in adj:
                adj[a] = Node(a)
            if b not in adj:
                adj[b] = Node(b)
            adj[a].prev.append(adj[b])
            adj[b].next.append(adj[a])
        
        return True

