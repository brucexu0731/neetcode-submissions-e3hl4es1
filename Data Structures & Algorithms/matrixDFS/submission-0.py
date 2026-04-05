class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        return self.dfs(grid, 0, 0, visit)


    def dfs(self, grid, r, c, visit):
        ROWS = len(grid)
        COLS = len(grid[0])

        #Base case 
        if min(r, c) < 0 or r == ROWS or c == COLS or (r, c) in visit or\
        grid[r][c] == 1:
            return 0
        elif r == ROWS - 1 and c == COLS - 1:
            return 1
        
        # recursive case 
        visit.add((r, c))

        count = 0 
        count += self.dfs(grid, r + 1, c, visit)
        count += self.dfs(grid, r - 1, c, visit)
        count += self.dfs(grid, r, c + 1 , visit)
        count += self.dfs(grid, r, c - 1, visit)

        #Backtracking
        visit.remove((r, c))

        return count

