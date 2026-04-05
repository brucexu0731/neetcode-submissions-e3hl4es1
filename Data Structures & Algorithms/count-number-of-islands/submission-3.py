class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        visit = set()
    
        def fill(grid, r, c, visit):
            ROW, COL = len(grid), len(grid[0])
            if min(r,c) < 0 or r == ROW or c == COL or (r, c) in visit or grid[r][c] == "0":
                return 

            visit.add((r, c))

            fill(grid, r + 1, c, visit)
            fill(grid, r - 1, c, visit)
            fill(grid, r, c + 1, visit)
            fill(grid, r, c - 1, visit)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visit or grid[i][j] == "0":
                    continue 
                else: 
                    fill(grid, i, j, visit)
                    count += 1
        
        return count
               