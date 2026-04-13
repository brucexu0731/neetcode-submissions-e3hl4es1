class UnionFind:
    def __init__(self, n):
        self.root = {}
        self.rank = {}
        for i in range(1, n + 1):
            self.root[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        if self.root[n] != n:
            self.root[n] = self.find(self.root[n])
        return self.root[n]
    
    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)
        if r1 == r2:
            return False
        if self.rank[r1] > self.rank[r2]:
            self.root[r2] = r1
        elif self.rank[r1] < self.rank[r2]:
            self.root[r1] = r2
        else:
            self.root[r2] = r1
            self.rank[r1] += 1
        return True 

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        union = UnionFind(n)

        for edge in edges:
            if not union.union(edge[0], edge[1]):
                return edge 
        
        return []

