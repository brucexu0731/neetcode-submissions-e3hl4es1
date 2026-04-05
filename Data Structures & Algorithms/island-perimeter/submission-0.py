class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set() 
        perim = 1
        ROW = len(grid)
        COL = len(grid[0])

        def dfs(r, c):
            print((r, c))
            nonlocal perim
            print(perim)
            if min(r, c) < 0 or r == ROW or c == COL or grid[r][c] == 0:
                return 
            if (r, c) in visit: 
                perim -= 1
                return
            
            perim += 3

            visit.add((r, c))

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
            
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return perim