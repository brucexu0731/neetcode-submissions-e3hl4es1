from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj = defaultdict(list)
        for source, dest in tickets:
            adj[source].append(dest)
        
        res = []
        def dfs(curr):
            if len(res) == len(tickets):
                res.append(curr)
                return True

            adj_copy = adj[curr][:]
            res.append(curr)
            for i, nxt in enumerate(adj_copy):
                adj[curr].pop(i)
                if dfs(nxt):
                    return True 
                adj[curr].insert(i, nxt)
            res.pop()
            return False
        
        dfs("JFK")
        return res
                


        

