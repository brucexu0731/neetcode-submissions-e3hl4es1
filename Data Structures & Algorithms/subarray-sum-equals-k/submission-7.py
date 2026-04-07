class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0 
        prefix = {}
        prefix[0] = 1

        for n in nums:
            curSum += n
            if curSum - k in prefix:
                res += prefix[curSum - k]

            if curSum not in prefix:
                prefix[curSum] = 1
            else:
                prefix[curSum] += 1

            

        
        return res