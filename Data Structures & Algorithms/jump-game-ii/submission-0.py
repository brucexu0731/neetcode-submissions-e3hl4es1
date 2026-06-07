class Solution:
    def jump(self, nums: List[int]) -> int:
        # DP with memoization 
        # loop - recursion 

        memo = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]

            n = nums[i]
            min_hops = float('inf')
            for j in range(i + 1, i + n + 1):
                min_hops = min(min_hops, dfs(j))
            memo[i] = 1 + min_hops
            
            return 1 + min_hops
        
        return dfs(0)