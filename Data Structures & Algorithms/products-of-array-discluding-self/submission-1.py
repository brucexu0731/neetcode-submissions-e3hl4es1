class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        post = 1
        for i in range(len(nums)):
            res[i] = res[i - 1] * nums[i - 1] if i - 1 >= 0 else 1
        
        for i in range(len(nums) - 2, -1, -1):
            post *= nums[i + 1]
            res[i] *= post

        return res
        