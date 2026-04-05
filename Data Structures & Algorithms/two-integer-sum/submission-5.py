class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = [1, i]
            else:
                hashmap[nums[i]][0] += 1
                hashmap[nums[i]].append(i)
        for num in nums:
            if target - num == num and hashmap[num][0] > 1:
                return [hashmap[num][1], hashmap[num][2]]
            elif target - num in hashmap and target - num != num:
                return [hashmap[num][1], hashmap[target - num][1]]
            