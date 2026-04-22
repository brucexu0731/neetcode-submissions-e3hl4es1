from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        for i in range(n - 1):
            xi, yi = points[i]
            for j in range(i + 1, n ):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        arr = [(0, 0)]
        heapq.heapify(arr)
        visit = set()
        cost = 0

        while arr:
            w, curr = heapq.heappop(arr)
            if curr in visit:
                continue
            
            visit.add(curr)
            cost += w

            for d, nxt in adj[curr]:
                if nxt not in visit:
                    heapq.heappush(arr, (d, nxt))
        
        return cost

                
