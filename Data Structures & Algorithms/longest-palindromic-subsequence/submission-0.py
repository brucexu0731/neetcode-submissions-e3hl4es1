class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        ss = ''
        for char in s:
            ss = char + ss
        
        rows = cols = len(s) + 1
        dp = [[0] * cols for i in range(rows)]

        for i in range(1, rows):
            for j in range(1, cols):
                if s[j - 1] == ss[i - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[rows - 1][cols - 1]
            
            
    
