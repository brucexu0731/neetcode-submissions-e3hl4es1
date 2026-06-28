from collections import defaultdict, deque
import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #dijkstra's 
        adj = defaultdict(list)

        for s, d, p in flights:
            adj[s].append((p, d))
        
        queue = deque()
        queue.append((0, src))
        visited = {}
        visited[src] = 0
        depth = 0

        while queue and depth <= k:
            for i in range(len(queue)):
                price, curr = queue.popleft()
                for p, nxt in adj[curr]:
                    nxt_price = p + price
                    if (nxt in visited and nxt_price < visited[nxt]) or nxt not in visited:
                        queue.append((nxt_price, nxt))
                        visited[nxt] = nxt_price
            depth += 1
        
        return visited[dst] if dst in visited else -1


