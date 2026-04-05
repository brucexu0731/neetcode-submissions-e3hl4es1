class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        m = max(nums)
        tot = m
        for i in range(m):
            tot += i
            tot -= nums[i]
        if tot in nums:
            tot = m + 1
        return tot 
        