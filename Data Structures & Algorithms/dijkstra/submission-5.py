from collections import defaultdict 
import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for s, d, w in edges:
            adj[s].append((w, d))
        
        heap = [(0, src)]
        res = {}
        for i in range(n):
            res[i] = -1
        
        while heap:
            w, d = heapq.heappop(heap)
            if res[d] != -1:
                continue
            
            res[d] = w

            for dist, neigh in adj[d]:
                heapq.heappush(heap, (dist + w, neigh))
        
        return res



