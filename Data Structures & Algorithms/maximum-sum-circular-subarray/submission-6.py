class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        min_sum = nums[0]
        max_sum = nums[0]
        curr_sum_min = 0
        curr_sum_max = 0
        tot = sum(nums)

        for n in nums:
            curr_sum_min += n 
            min_sum = min(min_sum, curr_sum_min)
            if curr_sum_min > 0:
                curr_sum_min = 0
            
            curr_sum_max += n
            max_sum = max(max_sum, curr_sum_max)
            if curr_sum_max < 0:
                curr_sum_max = 0
        
        return max_sum if min_sum == tot else max(max_sum, tot - min_sum)
