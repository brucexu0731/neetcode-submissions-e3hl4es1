class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {} # key is (index, buying or selling) -> max profit if 
        # bought curr / sold at curr
        max_prof = 0
        def dfs(i, buying):
            nonlocal max_prof
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
        
            if buying:
                buy = -prices[i] + dfs(i + 1, False)
                skip = dfs(i + 1, buying)
                res = max(buy, skip)
                memo[(i, True)] = res
                max_prof = max(max_prof, res)
                return res
            else:
                sell = prices[i] + dfs(i + 2, True)
                skip = dfs(i + 1, buying)
                res = max(sell, skip)
                memo[(i, False)] = res
                return res
        
        dfs(0, True)
        print(memo)
        return max_prof
