class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        res = set()
        n = len(nums)
        freq = defaultdict(int)

        for i in range(n):
            freq[nums[i]] += 1
            if freq[nums[i]] > n / 3:
                res.add(nums[i])
        
        return list(res)
                