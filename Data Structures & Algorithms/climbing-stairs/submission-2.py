class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 0:
        #     return 1 
        # elif n < 0:
        #     return 0
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        #Top Down DP:
        # cache = {}

        # def memoization(n):
        #     if n == 0:
        #         return 1
        #     elif n in cache:
        #         return cache[n]
        #     elif n < 0:
        #         return 0
        #     else: 
        #         cache[n] = memoization(n - 1) + memoization(n - 2)
        #         return cache[n]
        
        # return memoization(n)

        #Bottom Up DP:
        if n <= 2:
            return n
        
        dp = [1, 2]
        i = n - 3
        while i >= 0:
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
            i -= 1
        
        return dp[1]
