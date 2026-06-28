class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]
            
            one = dfs(i + 1)
            two = dfs(i + 2)
            curr_cost = 0 if i < 0 else cost[i]
            memo[i] = curr_cost + min(one, two)

            return curr_cost + min(one, two)
        
        return dfs(-1)