class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        items = len(profit)
        dp = [[0] * (capacity + 1) for _ in range(items)] 

        for i in range(items):
            for c in range(capacity + 1):
                skip = dp[i-1][c]
                include = 0
                if c - weight[i] >= 0:
                    include = profit[i] + dp[i-1][c - weight[i]]
                dp[i][c] = max(include, skip)

        return dp[items - 1][capacity]