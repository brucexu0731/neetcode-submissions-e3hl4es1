from collections import defaultdict
class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.x_limit = 0
        self.y_limit = 0

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[(x, y)] += 1
        self.x_limit = max(self.x_limit, x)
        self.y_limit = max(self.y_limit, y)
        

    def count(self, point: List[int]) -> int:
        x, y = point 
        res = 0
        #left
        for i in range(0, x):
            l = x - i
            #top-left
            if self.points[(x, y + l)] > 0 and self.points[(i, y + l)] > 0 and self.points[(i, y)] > 0:
                res += self.points[(x, y + l)] * self.points[(i, y + l)] * self.points[(i, y)] * max(1, self.points[(x, y)])
            #bottom-left
            if self.points[(x, y - l)] > 0 and self.points[(i, y - l)] > 0 and self.points[(i, y)] > 0:
                res += self.points[(x, y - l)] * self.points[(i, y - l)] * self.points[(i, y)] * max(1, self.points[(x, y)])
        
        #right
        for i in range(x + 1, self.x_limit + 1):
            l = i - x
            #top-left
            if self.points[(x, y + l)] > 0 and self.points[(i, y + l)] > 0 and self.points[(i, y)] > 0:
                res += self.points[(x, y + l)] * self.points[(i, y + l)] * self.points[(i, y)] * max(1, self.points[(x, y)])
            #bottom-left
            if self.points[(x, y - l)] > 0 and self.points[(i, y - l)] > 0 and self.points[(i, y)] > 0:
                res += self.points[(x, y - l)] * self.points[(i, y - l)] * self.points[(i, y)] * max(1, self.points[(x, y)])
        
        return res

