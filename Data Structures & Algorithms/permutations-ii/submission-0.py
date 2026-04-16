class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        path = []

        def dfs(nums):
            if not nums:
                res.add(tuple(path))
            
            for i in range(len(nums)):
                path.append(nums[i])
                nums_copy = nums[:]
                nums_copy.pop(i)
                dfs(nums_copy)
                path.pop()
        
        dfs(nums)
        return [list(x) for x in list(res)]