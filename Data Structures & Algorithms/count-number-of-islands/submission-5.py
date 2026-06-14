from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        row, col = len(grid), len(grid[0])
        visit = set()
        count = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            

            while queue:
                for i in range(len(queue)):
                    nr, nc = queue.popleft()

                    for x, y in [[nr + 1, nc], [nr - 1, nc], [nr, nc + 1], [nr, nc - 1]]:
                        if (x < row) and (y < col) and (min(x, y) >= 0) and ((x, y) not in visit) and (grid[x][y] == '1'):
                            queue.append((x, y))
                            visit.add((x, y))
        
        for i in range(row):
            for j in range(col):
                if (i, j) not in visit and grid[i][j] == '1':
                    count += 1
                    visit.add((i, j))
                    bfs(i, j)
        
        return count
