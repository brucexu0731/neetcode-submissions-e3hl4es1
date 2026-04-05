class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        arr = [-1] * (len(nums) + 1)

        for n in nums:
            arr[n] = n
        
        for i in range(len(arr)):
            if arr[i] == -1:
                return i