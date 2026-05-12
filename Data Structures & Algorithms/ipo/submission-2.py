from collections import defaultdict
import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        #k picks, start with w capital
        # each pick we need to pick the highest profit given our available capital
        # afterwards our profit is added to our capital 

        # can i not just do a prefix sums
        # hashmap of heaps that maps each capital value to a max heap
        # doesn't work because 2 -> [8, 7, 6] 3-> [3, 2, 1]
        # How can we use 2 heaps?
        # need nlogn solution
        costs = defaultdict(list)
        #O(n) time
        for i in range(len(profits)):
            p = profits[i]
            c = capital[i]
            costs[c].append(p)
        
        profs = []
        res = w
        for i in range(w + 1):
            for p in costs[i]:
                heapq.heappush(profs, -p)
        
        # print(costs)
        # print(profs)
        while k > 0 and profs:
            curr = heapq.heappop(profs)
            res -= curr
            k -= 1
            w_new = w - curr
            for i in range(w + 1, w_new + 1):
                if i in costs:
                    for p in costs[i]:
                        heapq.heappush(profs, -p)
            w = w_new
        
        return res

        


        