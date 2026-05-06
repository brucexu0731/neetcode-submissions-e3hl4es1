class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False 
        target = total // 2

        sums = set()
        sums.add(0)
        sums.add(nums[0])

        for i in range(1, len(nums)):
            new_sums = set()
            for n in sums:
                new_sum = nums[i] + n
                new_sums.add(new_sum)
            sums = sums.union(new_sums)
            if target in sums:
                return True
        
        return False
        

            