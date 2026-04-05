

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            #if we hit a leaf node on the decision tree, append that subset
            if i >= len(nums):
                res.append(subset[:])
                return
            
            #decision to include nums[i] --> one alternate universe
            subset.append(nums[i])
            dfs(i + 1)

            #decision to not include nums[i] --> another alternate universe
            subset.pop()
            dfs(i + 1)
        
        dfs(0)

        return res
                