from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # find the treasure chest, do BFS on the treasure chest

        queue = deque()
        visit = set()
        row, col = len(grid), len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visit.add((i, j))
                    break
        depth = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = depth
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if nr < row and nc < col and min(nr, nc) >= 0 and (nr, nc) not in visit and grid[nr][nc] != -1:
                        visit.add((nr, nc))
                        queue.append((nr, nc))
            depth += 1
        