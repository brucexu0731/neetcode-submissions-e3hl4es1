class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        memo = {}

        def dfs(i, j, k, n, m, prev):
            if abs(n - m) > 1:
                memo[(i, j)] = False
                return False
            if i == len(s1) and j == len(s2):
                if k == len(s3):
                    return True
                else:
                    return False
            if k == len(s3):
                return False 
            if (i, j) in memo:
                return memo[(i, j)]
            
            addi = False
            if i < len(s1) and s1[i] == s3[k]:
                if prev == 'i':
                    addi = dfs(i + 1, j, k + 1, n, m, 'i')
                else:
                    addi = dfs(i + 1, j, k + 1, n + 1, m, 'i')

            addj = False
            if j < len(s2) and s2[j] == s3[k]:
                if prev == 'j':
                    addj = dfs(i, j + 1, k + 1, n, m, 'j')
                else:
                    addj = dfs(i, j + 1, k + 1, n, m + 1, 'j')
            memo[(i, j)] = addi or addj
            return addi or addj
        
        return dfs(0, 0, 0, 0, 0, '')
