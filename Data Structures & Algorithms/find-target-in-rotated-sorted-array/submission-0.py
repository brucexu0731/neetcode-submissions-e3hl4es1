class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Case 1 if the array is not-rotated:
        # normal Binary Search 

        # Rotated:
        # m > nums[0]
        # in the left sorted portion, if target > m, we go to right
        # but if target < m, it could be in either left or right, we need 
        # to check it against nums[0] 
        # if target >= nums[0] it's in the left portion, if target < nums[0]
        # it's in the right portion --> this works for unrotated as well 

        # m < nums[0]
        # in the right sorted portion:
        # if target < m, we go left
        # if target > m, if target <= nums[-1], we go right -> won't apply to unrotated 

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            print(nums[m])
            if nums[m] == target:
                return m

            if nums[m] >= nums[0]:
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    if target >= nums[0]:
                        r = m - 1
                    else:
                        l = m + 1
            
            if nums[m] < nums[0]:
                if target < nums[m]:
                    r = m - 1
                elif target > nums[m]:
                    if target <= nums[-1]:
                        l = m + 1
                    else:
                        r = m - 1
        
        return -1


