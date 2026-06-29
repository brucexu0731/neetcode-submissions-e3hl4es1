class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # we can do loop-recursion dfs where we explore the longest
        # increasing path rooted at every index, and we compare the 
        # values returned for each dfs rooted at a value larger than 
        # the current index 

        # so we would do something like
        # dfs(i, j)
        # for every number after i, j (including i, j), pick that number
        # do dfs of every number after it (second loop), check each of the dfs results 
        # of indeces with values larger than curr against the current max 
        res = 1
        row, col = len(matrix), len(matrix[0])
        memo = {}
        def dfs(i, j, prev):
            if i == row or j == col or min(i, j) < 0 or matrix[i][j] <= prev:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            longest = 1
            # check remaining row
            up = dfs(i - 1, j, matrix[i][j])
            down = dfs(i + 1, j, matrix[i][j])
            left = dfs(i, j - 1, matrix[i][j])
            right = dfs(i, j + 1, matrix[i][j])

            longest += max(up, down, left, right)
            memo[(i, j)] = longest
            return longest
        
        for r in range(row):
            for c in range(col):
                res = max(res, dfs(r, c, -1))
        print(memo)
        return res
        # {(0, 0): 1, (0, 1): 1, (1, 2): 1, (0, 2): 2, (2, 0): 1, (1, 1): 2, (1, 0): 3, (2, 1): 3}

            


                    

