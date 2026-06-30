from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        queue = deque()

        queue.append(0)

        depth = 1
        prev = 0
        while queue:
            furthest = prev
            for i in range(len(queue)):
                curr = queue.popleft()
                furthest = max(furthest, curr + nums[curr])
                if furthest >= len(nums) - 1:
                    return depth 
            for i in range(prev + 1, furthest + 1):
                queue.append(i)
            prev = furthest 
            depth += 1
        
        return -1