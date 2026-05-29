class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search 
        # Boundary Conditions
        # [3, 4, 5, 6, 1, 2]
        # if m is greater than nums[0], it's in the left sorted portion, 
        # that means elements to its left are strictly smaller, but elements
        # to its right could be larger or smaller -> what to do then? 
        # -> check nums[-1], if m is smaller than nums[-1] we need to go right, 
        # otherwise go left 

        # if m is less than nums[0], it's in the right sorted portion, that 
        # means elements to its right are strictly larger 
        # -> if value is smaller than m, we go left
        # -> if value is larger, we check nums[-1], if it's smaller we go right,
        # otherwise we go left 

        # now check with [1,2,3,4,5,6] -> 5

        l, r = 0, len(nums) - 1

        if nums[0] <= nums[-1]:
            return nums[0]

        while l < r:
            m = (l + r) // 2
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                if nums[m] > nums[m -1]:
                    r = m - 1
                else:
                    return nums[m]
        
        return nums[l]



