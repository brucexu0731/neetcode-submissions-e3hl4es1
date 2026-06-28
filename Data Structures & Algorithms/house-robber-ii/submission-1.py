class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def dfs(i, robbed_first):
            if i >= len(nums):
                return 0
            if i == len(nums) - 1 and robbed_first:
                return 0
            if (i, robbed_first) in memo:
                return memo[(i, robbed_first)]
            
            if i == 0:
                rob = nums[i] + dfs(i + 2, True)
                skip = dfs(i + 1, False)
                return max(rob, skip)
            else:
                rob = nums[i] + dfs(i + 2, robbed_first)
                skip = dfs(i + 1, robbed_first)
                memo[(i, robbed_first)] = max(rob, skip)
                return max(rob, skip)
        
        return dfs(0, False)

