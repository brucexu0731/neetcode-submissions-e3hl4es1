class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def dfs(i, j):
            if i == len(s) and j == len(p):
                return True
            elif (i == len(s) and j + 1 < len(p) and p[j + 1] != "*") or (i == len(s) and j + 1 == len(p)) or j == len(p):
                return False

            if p[j] == ".":
                if j + 1 < len(p) and p[j + 1] == "*":
                    i -= 1
                    while i < len(s):
                        if dfs(i + 1, j + 2):
                            return True
                        i += 1
                    return False
                else:
                    return dfs(i + 1, j + 1)
            
            if j + 1 < len(p) and p[j + 1] == "*":
                wild_char = p[j]
                if dfs(i, j + 2):
                    return True
                while i < len(s) and s[i] == wild_char:
                    if dfs(i + 1, j + 2):
                        return True
                    i += 1
                return False
            elif s[i] != p[j]:
                return False
            else:
                return dfs(i + 1, j + 1)
        
        return dfs(0, 0)
