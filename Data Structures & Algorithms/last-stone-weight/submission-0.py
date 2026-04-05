class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            diff = first - second
            if diff == 0:
                continue
            else:
                heapq.heappush(stones, diff)
        return stones[0] * -1 if stones else 0
        