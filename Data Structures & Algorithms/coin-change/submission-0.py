class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def dfs(i, val):
            if val > amount:
                return float('inf')
            if val == amount:
                return 0
            if i == len(coins):
                return float('inf')
            if (i, val) in memo:
                return memo[(i, val)]
            
            add_curr = 1 + dfs(i, val + coins[i])
            skip_curr = dfs(i + 1, val)

            memo[(i, val)] = min(add_curr, skip_curr)
            return memo[(i, val)]
        
        res = dfs(0, 0)
        return -1 if res == float('inf') else res

