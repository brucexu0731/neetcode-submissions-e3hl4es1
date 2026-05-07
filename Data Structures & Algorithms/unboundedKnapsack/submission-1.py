class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:

        col = capacity + 1
        row = len(profit)
        dp = [[0] * col for i in range(row)]

        for i in range(row):
            for w in range(col):
                curr_weight = weight[i]
                skip = 0
                if i > 0:
                    skip = dp[i - 1][w]
                add = 0
                if w - curr_weight >= 0:
                    add = profit[i] + dp[i][w - curr_weight]
                dp[i][w] = max(add, skip)
        
        return dp[row - 1][col - 1]