class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def dfs(i, acc):
            if i == len(nums):
                if acc == target:
                    memo[(i, acc)] = 1
                    return 1
                else:
                    memo[(i, acc)] = 0
                    return 0
            if (i, acc) in memo:
                return memo[(i, acc)]
            
            sum_plus = dfs(i + 1, acc + nums[i])
            sum_minus = dfs(i + 1, acc - nums[i])

            memo[(i, acc)] = sum_plus + sum_minus 

            return sum_plus + sum_minus 
        
        return dfs(0, 0)