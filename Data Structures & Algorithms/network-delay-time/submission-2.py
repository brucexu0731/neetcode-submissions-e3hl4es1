from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for source, target, lag in times:
            adj[source].append((lag, target))
        
        dist = {}
        for i in range(1, n + 1):
            dist[i] = -1 
        heap = [(0, k)]

        while heap:
            d, curr = heapq.heappop(heap)
            if dist[curr] != -1:
                continue
            
            dist[curr] = d

            for d_next, neighbor in adj[curr]:
                heapq.heappush(heap, (d + d_next, neighbor))
        if min(dist.values()) == -1:
            return -1 
        else:
            return max(dist.values())
