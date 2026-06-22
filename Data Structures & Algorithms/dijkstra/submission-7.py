from collections import defaultdict
import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        #build adjacency list
        adj = defaultdict(list)
        for source, dest, weight in edges:
            adj[source].append((weight, dest))
        
        shortest = {}
        for i in range(n):
            shortest[i] = -1
        heap = [(0, src)]

        while heap:
            dist, node = heapq.heappop(heap)
            if shortest[node] != -1:
                continue
            
            shortest[node] = dist

            for dn, nxt in adj[node]:
                heapq.heappush(heap, (dn + dist, nxt))
        
        return shortest

