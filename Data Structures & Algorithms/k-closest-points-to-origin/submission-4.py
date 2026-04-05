class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [[((points[i][0]) ** 2 + (points[i][1]) ** 2), i] for i in range(len(points))]
        heapq.heapify(dist)
        res = []
        for i in range(k):
            point = heapq.heappop(dist)
            res.append(points[point[1]])
        return res