class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visit = set()
        queue = deque()
        visit.add((0,0))
        queue.append((0,0))

        length = 0

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROW - 1 and c == COL - 1:
                    return length 
                
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    ur, uc = r + dr, c + dc
                    if min(ur, uc) < 0 or ur == ROW or uc == COL or (ur, uc) in visit or grid[ur][uc] == 1:
                        continue
                    else:
                        visit.add((ur, uc))
                        queue.append((ur, uc))
            length += 1
        
        return -1 
        