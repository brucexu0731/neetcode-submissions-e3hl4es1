import heapq
class MedianFinder:

    def __init__(self):
        self.large, self.small = [], []
        self.size_l = 0
        self.size_s = 0

    def addNum(self, num: int) -> None:
        if not self.large:
            heapq.heappush(self.large, num)
            self.size_l += 1
            return
        elif not self.small:
            if num <= self.large[0]:
                heapq.heappush(self.small, -num)
                self.size_s += 1
                return
            else:
                tmp = heapq.heappop(self.large)
                heapq.heappush(self.small, -tmp)
                self.size_s += 1
                heapq.heappush(self.large, num)
                return
        
        t1 = -self.small[0]
        t2 = self.large[0]

        if self.size_l == self.size_s:
            if num <= t1:
                heapq.heappush(self.small, -num)
                self.size_s += 1
            else:
                heapq.heappush(self.large, num)
                self.size_l += 1
        elif self.size_l > self.size_s:
            if num <= t2:
                heapq.heappush(self.small, -num)
                self.size_s += 1
            else:
                tmp = heapq.heappop(self.large)
                heapq.heappush(self.small, -tmp)
                self.size_s += 1
                heapq.heappush(self.large, num)
        else:
            if num >= t1:
                heapq.heappush(self.large, num)
                self.size_l += 1
            else:
                tmp = heapq.heappop(self.small)
                heapq.heappush(self.large, -tmp)
                self.size_l += 1
                heapq.heappush(self.small, -num)
        
        print(self.large, self.small)
        
        

    def findMedian(self) -> float:
        if self.size_l == self.size_s:
            return (self.large[0] - self.small[0]) / 2
        elif self.size_l > self.size_s:
            return self.large[0]
        else:
            return -self.small[0]
        
        