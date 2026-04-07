class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot = sum(nums)
        left_sum = 0
        right_sum = tot 

        for i in range(len(nums)):
            left_sum += nums[i - 1] if i > 0 else 0
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
        
        return -1