class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        visit = set()
        shape = set()
        count = 0

        def dfs(r, c):
            nonlocal path 
            if r == row or c == col or min(r, c) < 0 or (r, c) in visit or grid[r][c] == 0: 
                path += 'O'
                return
            
            visit.add((r, c))
            path += 'R'
            dfs(r + 1, c)
            path += 'L'
            dfs(r - 1, c)
            path += 'D'
            dfs(r, c + 1)
            path += 'U'
            dfs(r, c - 1)
        
        for i in range(row):
            for j in range(col):
                if (i, j) not in visit and grid[i][j] == 1:
                    path = ''
                    dfs(i, j)
                    #print(path)
                    if path not in shape:
                        count += 1
                        shape.add(path)
        
        return count