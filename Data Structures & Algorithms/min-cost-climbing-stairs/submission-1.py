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
            memo[i] = cost[i] + min(one, two)

            return cost[i] + min(one, two)
        
        return min(dfs(0), dfs(1))