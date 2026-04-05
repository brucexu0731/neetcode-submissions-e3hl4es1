class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for a in range(len(nums) - 2):
            if a and nums[a - 1] == nums[a]:
                continue
            valid = []
            b = a + 1
            c = len(nums) - 1
            val = 0 - nums[a]
            while b < c:
                if nums[b - 1] == nums[b] and b > a + 1:
                    b += 1
                    continue

                if nums[b] + nums[c] == val:
                    valid = [nums[a], nums[b], nums[c]]
                    b += 1
                    c -= 1
                    res.append(valid[:])
                elif nums[b] + nums[c] < val:
                    b += 1
                elif nums[b] + nums[c] > val:
                    c -= 1
            
        return res