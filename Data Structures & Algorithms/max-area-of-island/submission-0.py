class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit = set()
        largest = 0 

        def dfs(grid, r, c):
            ROW, COL = len(grid), len(grid[0])

            if min(r,c) < 0 or r == ROW or c == COL or grid[r][c] == 0 or\
            (r, c) in visit:
                return 0 
            
            count = 1
            visit.add((r, c))

            count += dfs(grid, r + 1, c)
            count += dfs(grid, r - 1, c)
            count += dfs(grid, r, c + 1)
            count += dfs(grid, r, c - 1)

            return count 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visit:
                    area = dfs(grid, i, j)
                    largest = max(largest, area)

        return largest



