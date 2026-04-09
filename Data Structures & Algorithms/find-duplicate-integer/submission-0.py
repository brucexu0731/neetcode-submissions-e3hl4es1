class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # [1,2,3,2,4]
        # S -> 1, 2, 3, 2, 4
        # F -> 1, 3, 4, 2, 2
        # [1, 2, 3, 4, ..., n]
        arr = [0] * len(nums)
        for n in nums:
            if arr[n] == 1:
                return n
            else: 
                arr[n] = 1

