class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        rows = len(word1) + 1
        cols = len(word2) + 1
        dp = [[0] * cols for i in range(rows)]

        for i in range(cols):
            dp[-1][i] = cols - 1 - i
        for j in range(rows):
            dp[j][-1] = rows - 1 - j
        
        for i in range(rows - 2, -1, -1):
            for j in range(cols - 2, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = min(
                        1 + dp[i + 1][j + 1],
                        1 + dp[i][j + 1],
                        1 + dp[i + 1][j]
                    )
        return dp[0][0]
