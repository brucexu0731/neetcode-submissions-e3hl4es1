from collections import defaultdict 
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_map = defaultdict(list)
        for edge in edges:
            adj_map[edge[0]].append(edge[1])
            adj_map[edge[1]].append(edge[0])
        
        visit = set()
        path = []
        def dfs(n, prev):
            nonlocal path
            if n in visit:
                for i in range(len(path)):
                    if path[i] == n:
                        path = path[i:]
                        path.append(n)
                        break
                return True


            visit.add(n)
            path.append(n)
            for v in adj_map[n]:
                if v == prev:
                    continue 
                if dfs(v, n):
                    return True 
            visit.remove(n)
            path.pop()
            return False 

        cycle = dfs(edges[0][0], None)
        cycle_edges = set()
        for i in range(1, len(path)):
            cycle_edges.add((path[i - 1], path[i]))
            cycle_edges.add((path[i], path[i - 1]))
        
        for i in range(len(edges) - 1, -1, -1):
            edge = edges[i]
            if (edge[0], edge[1]) in cycle_edges:
                return edge 

