class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] == 1:
            return -1
        
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        visit.add((0, 0))
        queue.append((0, 0))

        length = 1

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROW - 1 and c == COL - 1:
                    return length 

                neighbors = [[1, 1], [-1, 1], [1, -1], [-1, -1], [1, 0],[-1, 0], [0, 1], [0, -1]] 

                for dr, dc in neighbors:
                    nr, nc = r + dr, c + dc
                    if min(nr, nc) < 0 or nr == ROW or nc == COL or (nr, nc) in visit or grid[nr][nc] == 1:
                        continue
                    else:
                        queue.append((nr, nc))
                        visit.add((nr, nc))
            length += 1

        return -1       