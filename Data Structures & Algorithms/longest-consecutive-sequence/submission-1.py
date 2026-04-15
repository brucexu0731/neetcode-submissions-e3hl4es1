class UnionFind:
    def __init__(self, nums):
        self.root = {}
        self.length = {}
        for n in nums:
            self.root[n] = n
            self.length[n] = 1
    
    def find(self, n):
        if self.root[n] != n:
            self.root[n] = self.find(self.root[n])
        return self.root[n]
    
    def union(self, n1, n2):
        if n1 not in self.root or n2 not in self.root:
            return False 
        r1, r2 = self.find(n1), self.find(n2)
        if r1 == r2:
            return False 
        
        if n1 < n2:
            self.root[r2] = r1
            self.length[r1] += self.length[r2]
        else:
            self.root[r1] = r2
            self.length[r2] += self.length[r1]
        return True 
        


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        uf = UnionFind(nums)
        for n in nums:
            uf.union(n - 1, n)
            uf.union(n, n + 1)

        res = max(uf.length.values())
        return res
        