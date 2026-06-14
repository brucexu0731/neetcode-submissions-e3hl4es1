from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                xi, yi = points[i]
                xj, yj = points[j]
                e = abs(xi - xj) + abs(yi - yj)
                adj[i].append([e, j])
                adj[j].append([e, i])
        res = 0
        arr = [[0, 0]]
        visit = set()

        while len(visit) < len(points):
            e, curr = heapq.heappop(arr)
            if curr in visit:
                continue

            visit.add(curr)
            res += e
            for dist, neighbor in adj[curr]:
                heapq.heappush(arr, [dist, neighbor])
        
        return res

                
