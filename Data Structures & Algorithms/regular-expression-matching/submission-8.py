class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        memo = {}

        def dfs(i, j):
            if i >= len(s) and j >= len(p):
                return True
            
            elif j >= len(p):
                return False 
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            #i can still be out of bounds, but it could still work
            # as j might be ending in star
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            #check for star
            if j + 1 < len(p) and p[j + 1] == "*":
                #skip the star entirely
                skip = dfs(i, j + 2)

                if not match:
                    pick = False 
                else:
                    pick = dfs(i + 1, j)
                memo[(i, j)] = pick or skip
                return pick or skip
            
            #check for match
            if match:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            
            memo[(i, j)] = False
            return False
        
        return dfs(0, 0)