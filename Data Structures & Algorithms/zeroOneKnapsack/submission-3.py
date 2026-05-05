class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        memo = {}

        def dfsHelper(profit, weight, curr_weight, i):
            if curr_weight == capacity or i == len(weight):
                memo[(i, curr_weight)] = 0
                return 0
            if (i, curr_weight) in memo:
                return memo[(i, curr_weight)]
                
            w, p = weight[i], profit[i]
            profit_with, profit_without = 0, 0
            if curr_weight + w <= capacity:
                    profit_with = p + dfsHelper(profit, weight, curr_weight + w, i + 1)
            
            profit_without = dfsHelper(profit, weight, curr_weight, i + 1)
            
            res = max(profit_with, profit_without)
            memo[(i, curr_weight)] = res
            return res
        
        return dfsHelper(profit, weight, 0, 0)