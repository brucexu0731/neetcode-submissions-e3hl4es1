class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()

        while n not in visited:
            visited.add(n)
            res = 0
            while n:
                res += (n % 10) ** 2
                n //= 10
            n = res
            if n == 1:
                return True
        
        return False 
