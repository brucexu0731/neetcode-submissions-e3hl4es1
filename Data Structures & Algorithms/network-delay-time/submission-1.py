from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #adjacency list, node 1 ... n -> [[distance, target],...]
        adj = defaultdict(list)
        edge_length = defaultdict(int)
        edge_length[(k, k)] = 0
        for edge in times:
            source = edge[0]
            target = edge[1]
            distance = edge[2]
            adj[source]. append([distance, target])
            edge_length[(source, target)] = distance 
        
        #Shortest distance from k to 1 ... n for each 1 ... n 
        shortest = defaultdict(int)

        #min-heap of [weight, current node, previous edge]
        arr = [[0, k, k]]
        heapq.heapify(arr)

        #counter for how many nodes processed 
        nodes = 0
        dist = 0

        #visit counter for level traversal 
        visit = set()

        while arr:
            curr = heapq.heappop(arr)
            prev = curr[2]
            node = curr[1]
            weight = curr[0]
            if node in shortest:
                continue
            
            shortest[node] = weight
            visit.add(node)
            nodes += 1
            dist += edge_length[(prev, node)]

            for t in adj[node]:
                if t[1] in visit:
                    continue
                heapq.heappush(arr, [weight + t[0], t[1], node])
        
        if nodes < n:
            return -1
        else:
            return max(shortest.values())

