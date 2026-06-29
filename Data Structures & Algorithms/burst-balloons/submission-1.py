class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        #brute force way would be to do a dfs and burst every balloon
        # that would be every permutation of the array 
        # greedy? pop the smallest ballon first 
        nums = [1] + nums + [1]

        memo = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            
            max_val = 0
            for i in range(l, r + 1):
                pick_i = nums[i] * nums[l - 1] * nums[r + 1]
                pick_i += dfs(l, i - 1) + dfs(i + 1, r)
                max_val = max(pick_i, max_val)
            
            memo[(l, r)] = max_val
            return max_val
        
        return dfs(1, len(nums) - 2)
