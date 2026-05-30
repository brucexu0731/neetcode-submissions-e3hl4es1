import heapq
from collections import defaultdict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        max_heap = []
        window_map = defaultdict(int)
        res = []

        i, j = 0, k - 1
        for n in range(j + 1):
            heapq.heappush(max_heap, -nums[n])
            window_map[nums[n]] += 1
        

        while j < len(nums):
            #cleanup heap
            while window_map[-max_heap[0]] == 0:
                heapq.heappop(max_heap)
            
            #print(max_heap)
            
            curr_max = max_heap[0]
            res.append(-curr_max)

            window_map[nums[i]] -= 1
            i += 1
            j += 1
            if j == len(nums):
                break
            window_map[nums[j]] += 1
            heapq.heappush(max_heap, -nums[j])

        return res