class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo={}
        
        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True
            elif (i == len(s) and j + 1 < len(p) and p[j + 1] != "*") or (i == len(s) and j + 1 == len(p)) or j == len(p):
                return False
            if (i, j) in memo:
                return memo[(i, j)]

            if p[j] == ".":
                if j + 1 < len(p) and p[j + 1] == "*":
                    i_copy = i - 1
                    while i_copy < len(s):
                        if dfs(i_copy + 1, j + 2):
                            memo[(i, j)] = True
                            return True
                        i_copy += 1
                    memo[(i, j)] = False
                    return False
                else:
                    memo[(i, j)] = dfs(i + 1, j + 1)
                    return memo[(i, j)]
            
            if j + 1 < len(p) and p[j + 1] == "*":
                wild_char = p[j]
                if dfs(i, j + 2):
                    memo[(i, j)] = True
                    return True
                i_copy = i
                while i_copy < len(s) and s[i_copy] == wild_char:
                    if dfs(i_copy + 1, j + 2):
                        memo[(i, j)] = True
                        return True
                    i_copy += 1
                memo[(i, j)] = False
                return False
            elif s[i] != p[j]:
                return False
            else:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
        
        return dfs(0, 0)
