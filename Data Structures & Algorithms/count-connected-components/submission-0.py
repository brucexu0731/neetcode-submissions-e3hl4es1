from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        print(adj)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for children in adj[node]:
                dfs(children)
        
        res = 0
        for i in range(n):
            if i in visit:
                print(i)
                continue
            res += 1
            dfs(i)

        return res