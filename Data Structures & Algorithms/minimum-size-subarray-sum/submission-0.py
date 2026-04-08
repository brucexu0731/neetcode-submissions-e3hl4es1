class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, window_sum = 0, 0
        min_length = float('inf')

        for R in range(len(nums)):
            window_sum += nums[R]
            
            while window_sum >= target:
                length = R - L + 1
                min_length = min(length, min_length)
                window_sum -= nums[L]
                L += 1
        
        return min_length if min_length < float('inf') else 0