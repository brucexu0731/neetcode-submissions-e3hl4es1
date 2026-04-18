from collections import defaultdict
import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for n1, n2, w in edges:
            adj[n1].append((n2, w))
        
        arr = [(0, src)]
        heapq.heapify(arr)

        res = {}

        while arr:
            dist, node = heapq.heappop(arr)
            if node in res:
                continue
            
            res[node] = dist

            for neighbor, w in adj[node]:
                heapq.heappush(arr, (dist + w, neighbor))
        
        for i in range(n):
            if i not in res:
                res[i] = -1 
                
        return res
