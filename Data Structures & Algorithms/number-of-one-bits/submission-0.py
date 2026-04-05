class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            l = n % 2
            if l^0:
                count += 1
            n = n >> 1 
        return count
        