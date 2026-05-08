class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}

        def dfs(i, curr):
            if curr == amount:
                return 1
            if i == len(coins) or curr > amount:
                return 0
            if (i, curr) in memo:
                return memo[(i, curr)]
            
            add_coin = dfs(i, curr + coins[i])

            skip_coin = dfs(i + 1, curr)

            memo[(i, curr)] = add_coin + skip_coin
            return add_coin + skip_coin

        return dfs(0, 0)