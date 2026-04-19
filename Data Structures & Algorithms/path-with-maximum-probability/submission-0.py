from collections import defaultdict
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = defaultdict(list)
        for i in range(len(edges)):
            n1, n2 = edges[i]
            p = succProb[i]
            adj[n1].append((p, n2))
            adj[n2].append((p, n1))
        
        arr = [[-1, start_node]]
        heapq.heapify(arr)
        visit = {}

        while arr:
            p, curr = heapq.heappop(arr)
            if curr in visit:
                continue
            visit[curr] = p

            for p_nxt, nxt in adj[curr]:
                if nxt in visit:
                    continue 
                heapq.heappush(arr, [p * p_nxt, nxt])
        
        return 0 if end_node not in visit else -visit[end_node]