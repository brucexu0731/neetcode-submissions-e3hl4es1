class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, target, subset):
            if target == 0:
                res.append(subset[:])
                return
            if target < 0 or i >= len(nums):
                return
            
            subset.append(nums[i])
            dfs(i, target - nums[i], subset)
            subset.pop()
            dfs(i + 1, target, subset)

        dfs(0, target, [])
        return res
            