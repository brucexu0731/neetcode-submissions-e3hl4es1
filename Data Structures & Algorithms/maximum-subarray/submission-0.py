class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sliding_sum = 0

        for n in nums:
            sliding_sum += n
            max_sum = max(max_sum, sliding_sum)
            if sliding_sum < 0:
                sliding_sum = 0 
        
        return max_sum
            
            