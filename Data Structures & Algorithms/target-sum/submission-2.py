class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        sums = {}
        sums[0] = 0

        for i in range(len(nums)):
            new_sums = {}
            for n in sums:
                sum1 = n + nums[i]
                sum2 = n - nums[i]
                if sum1 not in new_sums:
                    new_sums[sum1] = max(1, sums[n])
                else:
                    new_sums[sum1] += max(1, sums[n])
                if sum2 not in new_sums:
                    new_sums[sum2] = max(1, sums[n])
                else:
                    new_sums[sum2] += max(1, sums[n])
            sums = new_sums 

        return new_sums[target] if target in new_sums else 0