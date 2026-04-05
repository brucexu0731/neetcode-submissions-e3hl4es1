class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = [0, 0, 0]

        for i in nums:
            n[i] += 1
        
        k = 0
        for i in range(len(n)):
            for j in range(n[i]):
                nums[k] = i
                k += 1
            

        