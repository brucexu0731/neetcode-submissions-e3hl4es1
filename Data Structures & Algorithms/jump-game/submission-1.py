class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # go from back to front, last index is true, then going backwards
        # if the next spot has enough jumps to each any True indeces, that 
        # index will be true and we proceed

        # or do loop-recursion

        nums[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            tf = False 
            for j in range(1, nums[i] + 1):
                if i + j == len(nums):
                    break
                if nums[i + j]:
                    tf = True
                    break
            nums[i] = tf
        return nums[0]
            