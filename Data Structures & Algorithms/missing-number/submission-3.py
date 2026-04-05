class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        m = len(nums)
        tot = m
        for i in range(m):
            tot += i
            tot -= nums[i]

        return tot 
        