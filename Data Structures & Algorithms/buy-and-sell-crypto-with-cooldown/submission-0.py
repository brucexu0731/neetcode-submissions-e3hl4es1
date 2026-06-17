class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def dfs(curr):
            if curr >= len(prices):
                return 0
            if curr in memo:
                return memo[curr]
            
            max_profit = 0
            for i in range(curr + 1, len(prices)):
                buy_curr = prices[i] - prices[curr] + dfs(i + 2)
                skip_curr = dfs(i)
                max_profit = max(max_profit, buy_curr, skip_curr)
            memo[curr] = max_profit
            return max_profit

        dfs(0)
        return max(memo.values())