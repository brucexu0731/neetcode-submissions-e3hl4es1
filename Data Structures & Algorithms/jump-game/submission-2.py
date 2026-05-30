class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # go from back to front, last index is true, then going backwards
        # if the next spot has enough jumps to each any True indeces, that 
        # index will be true and we proceed

        # or do loop-recursion

        nums[-1] = True
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                nums[i] = True
                goal = i
            else:
                nums[i] = False

        return nums[0]
            