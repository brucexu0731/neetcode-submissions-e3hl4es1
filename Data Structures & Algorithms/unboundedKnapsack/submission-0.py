class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        memo = {}

        def dfs(i, curr_weight):
            if curr_weight == capacity or i == len(profit):
                return 0 
            if (i, curr_weight) in memo:
                return memo[(i, curr_weight)]
            
            #pick same
            add_same = 0
            if curr_weight + weight[i] <= capacity:
                add_same = profit[i] + dfs(i, curr_weight + weight[i])
            
            #pick 
            add_curr = 0
            if curr_weight + weight[i] <= capacity:
                add_curr = profit[i] + dfs(i + 1, curr_weight + weight[i])
            
            without_curr = dfs(i + 1, curr_weight)

            res = max(add_same, add_curr, without_curr)
            memo[(i, curr_weight)] = res
            return res
        
        return dfs(0, 0)