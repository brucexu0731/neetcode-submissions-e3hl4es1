class Solution:
    def numDistinct(self, s: str, t: str) -> int:
    #     c a c a t
    # c   1 1 2 2 2
    # a   0 1 1 3 3
    # t   0 0 0 0 3

    #     x x y x y
    # x   1 2 2 3 3
    # y   0 0 2 2 5

    #     b a a a t
    # a   0 1 2 3 3
    # t   0 0 0 0 3
        rows = len(t)
        cols = len(s)

        dp = [[0] * cols for i in range(rows)]

        dp[0][0] = 1 if s[0] == t[0] else 0

        for i in range(1, cols):
            if s[i] == t[0]:
                dp[0][i] = 1 + dp[0][i - 1]
            else:
                dp[0][i] = dp[0][i - 1]
        
        for i in range(1, rows):
            for j in range(cols):
                if i > j:
                    continue
                if s[j] == t[i]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        
        print(dp)
        return dp[rows - 1][cols - 1]

