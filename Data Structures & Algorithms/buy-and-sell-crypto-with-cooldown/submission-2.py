class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} # key is (index, buying or selling) -> max profit if 
        # bought curr / sold at curr
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
        
            if buying:
                buy = -prices[i] + dfs(i + 1, False)
                skip = dfs(i + 1, buying)
                res = max(buy, skip)
                memo[(i, True)] = res
                return res
            else:
                sell = prices[i] + dfs(i + 2, True)
                skip = dfs(i + 1, buying)
                res = max(sell, skip)
                memo[(i, False)] = res
                return res
        
        print(memo)
        return dfs(0, True)
