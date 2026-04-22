from collections import defaultdict
import heapq
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        def bfs(n, edges, fixed_edge):
            adj = defaultdict(list)

            for n1, n2, w in edges:
                adj[n1].append((w, n2))
                adj[n2].append((w, n1))
            
            arr = [fixed_edge]
            w, prev, curr = fixed_edge
            heapq.heapify(arr)
            visit = set()
            visit.add(prev)
            visit.add(curr)
            res = fixed_edge[0]
            for w, neighbor in adj[prev]:
                if neighbor not in visit:
                    heapq.heappush(arr, (w, prev, neighbor))
            for w, neighbor in adj[curr]:
                if neighbor not in visit:
                    heapq.heappush(arr, (w, curr, neighbor))
            

            while arr:
                w, prev, curr = heapq.heappop(arr)
                if curr in visit:
                    continue
                visit.add(curr)
                res += w

                for w, neighbor in adj[curr]:
                    if neighbor not in visit:
                        heapq.heappush(arr, (w, curr, neighbor))

            if len(visit) == n:
                return res 
            else:
                return -1
    
        mst = bfs(n, edges, (0, 0, 0))
        res = [[], []]
        for i in range(len(edges)):
            edges_copy = edges[:]
            edges_copy.pop(i)
            mst_copy = bfs(n, edges_copy, (0, 0, 0))
            if mst_copy == -1 or mst_copy > mst:
                res[0].append(i)
            else:
                res[1].append(i)
        
        pseudo = []
        for i in res[1]:
            n1, n2, w = edges[i]
            mst_copy = bfs(n, edges, (w, n1, n2))
            print(i)
            print(mst, mst_copy)
            if mst_copy == mst:
                pseudo.append(i)
        res[1] = pseudo

        return res 





        
        
