
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

        reqs = {i : [] for i in range(numCourses)}

        for a, b in prerequisites:
            reqs[a].append(b)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return False
            if reqs[node] == []:
                return True 
            
            visit.add(node)
            for pre in reqs[node]:
                if not dfs(pre):
                    return False 
            visit.remove(node)
            reqs[node] = []
            return True 
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        # for a, b in prerequisites:
        #     if a == b:
        #         return False
        #     if a in adj and b in adj:
        #         A = adj[a]
        #         B = adj[b]
        #         if B.search_prev(A):
        #             return False
        #     if a not in adj:
        #         adj[a] = Node(a)
        #     if b not in adj:
        #         adj[b] = Node(b)
        #     adj[a].prev.append(adj[b])
        #     adj[b].next.append(adj[a])
        
        # return True

