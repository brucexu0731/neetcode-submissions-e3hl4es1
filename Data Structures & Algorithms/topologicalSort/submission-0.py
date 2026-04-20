from collections import defaultdict
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        
        visit = set()
        res = []

        def dfs(node, path):
            if node in path:
                return False 
            if node in visit:
                return True

            visit.add(node)
            path.add(node)
            is_valid = True
            for i in adj[node]:
                is_valid &= dfs(i, path)
            res.append(node)
            path.remove(node)
            return is_valid
        
        for i in range(n):
            if i in visit:
                continue
            if not dfs(i, set()):
                return []
        
        return res[::-1]

            

