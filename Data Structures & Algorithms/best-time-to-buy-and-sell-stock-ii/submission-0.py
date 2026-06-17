class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(curr):
            if curr >= len(prices):
                return 0
            if curr in memo:
                return memo[curr]
            max_prof = 0
            curr_price = prices[curr]
            for i in range(curr + 1, len(prices)):
                buy_curr = prices[i] - curr_price + dfs(i)
                #print('curr: ', curr, buy_curr)
                skip_curr = dfs(i)
                #print('curr: ', curr, skip_curr)
                max_prof = max(max_prof, buy_curr, skip_curr)
            memo[curr] = max_prof
            return max_prof
        dfs(0)
        #print(memo)
        return max(memo.values())