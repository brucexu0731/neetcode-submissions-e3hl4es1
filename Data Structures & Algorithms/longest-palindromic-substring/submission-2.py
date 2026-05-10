class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = {}
        def dfs(i, j):
            if i == j:
                return [True, 1, s[i]]
            if i > j:
                return [True, 0, '']
            if (i, j) in memo:
                return memo[(i, j)]

            
            if s[i] == s[j]:
                valid, length, sub = dfs(i + 1, j - 1)
                if valid:
                    memo[(i, j)] = [True, 2 + length, s[i] + sub + s[j]] 
                    return memo[(i, j)]

            v1, l1, s1 = dfs(i + 1, j)
            v2, l2, s2 = dfs(i, j - 1)
            if l1 >= l2:
                memo[(i, j)] = [False, l1, s1]
                return [False, l1, s1]
            else:
                memo[(i, j)] = [False, l2, s2]
                return [False, l2, s2]

        return dfs(0, len(s) - 1)[2]

