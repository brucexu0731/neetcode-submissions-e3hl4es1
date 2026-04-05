class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        rot = set()
        fresh = set()
        queue = deque()
        minute = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    rot.add((i, j))
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh.add((i, j))
        
        while queue and fresh:
            for i in range(len(queue)):
                print(fresh)
                print(minute)
                r, c = queue.popleft()

                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr == ROW or nc == COL or (nr, nc) in rot or grid[nr][nc] == 0:
                        continue
                    else:
                        rot.add((nr, nc))
                        queue.append((nr, nc))
                        fresh.remove((nr, nc))
            minute += 1

        if not fresh:
            return minute
        else:
            return -1
                    
                
                