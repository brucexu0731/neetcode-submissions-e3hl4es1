import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
    
        row, col = len(grid), len(grid[0])
        # (h, r, c)
        arr = [(0, 0, 0)]
        visit = {(0, 0): grid[0][0]}
        heap = set()
        heapq.heapify(arr)

        while arr:
            h, r, c = heapq.heappop(arr)

            for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if nr == row - 1 and nc == col - 1:
                    return max(visit[(r, c)], grid[nr][nc])
                if min(nr, nc) < 0 or nr == row or nc == col or (nr, nc) in heap:
                    continue
                visit[(nr, nc)] = max(visit[(r, c)], grid[nr][nc])
                heapq.heappush(arr, (grid[nr][nc], nr, nc))
                heap.add((r, c))
        
                

