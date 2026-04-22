from collections import defaultdict
import heapq
class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for e1, e2, w in edges:
            adj[e1].append((e2, w))
            adj[e2].append((e1, w))
        
        arr = [(0, 0)]
        heapq.heapify(arr)
        visit = set()
        res = 0
        count = 0

        while arr:
            w, curr = heapq.heappop(arr)
            if curr in visit:
                continue 
            visit.add(curr)
            res += w
            count += 1

            for nxt, w in adj[curr]:
                heapq.heappush(arr, (w, nxt))
        print(count)

        return res if count == n else -1

