class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        can_pacific = {}
        can_atlantic = {}
        row, col = len(heights), len(heights[0])
        
        def flowPacific(r, c, prev):
            if r == row or c == col:
                return False 
            if (r == 0 or c == 0) and heights[r][c] <= prev:
                can_pacific[(r, c)] = True
                return True 
            if heights[r][c] > prev:
                return False 
            if (r, c) in can_pacific:
                return can_pacific[(r, c)]
            if (r, c) in visit:
                return False
            visit.add((r, c))

            if not (flowPacific(r + 1, c, heights[r][c]) or flowPacific(r - 1, c, heights[r][c]) or flowPacific(r, c + 1, heights[r][c]) or flowPacific(r, c - 1, heights[r][c])):
                can_pacific[(r, c)] = False
                return False 
            else: 
                can_pacific[(r, c)] = True
                return True 
        
        for r in range(row):
            for c in range(col):
                visit = set()
                if (r, c) not in can_pacific:
                    flowPacific(r, c, float('inf'))

        def flowAtlantic(r, c, prev):
            if (r == row - 1 or c == col - 1) and heights[r][c] <= prev:
                can_atlantic[(r, c)] = True
                return True 
            if r == -1 or c == -1:
                return False 
            if heights[r][c] > prev:
                return False 
            if (r, c) in can_atlantic:
                return can_atlantic[(r, c)]
            
            if (r, c) in visit:
                return False
            visit.add((r, c))
            
            if not (flowAtlantic(r + 1, c, heights[r][c]) or flowAtlantic(r - 1, c, heights[r][c]) or flowAtlantic(r, c + 1, heights[r][c]) or flowAtlantic(r, c - 1, heights[r][c])):
                can_atlantic[(r, c)] = False
                return False 
            else: 
                can_atlantic[(r, c)] = True
                return True 
        
        for r in range(row):
            for c in range(col):
                visit = set()
                if (r, c) not in can_atlantic:
                    flowAtlantic(r, c, float('inf'))
        
        res = []
        for r in range(row):
            for c in range(col):
                if can_pacific[(r, c)] and can_atlantic[(r, c)]:
                    res.append([r, c])
        
        return res