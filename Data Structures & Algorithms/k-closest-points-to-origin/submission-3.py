class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [[((points[i][0]) ** 2 + (points[i][1]) ** 2) ** 0.5, i] for i in range(len(points))]
        dist.sort(key=lambda x: x[0])
        print(dist)
        dist = dist[:k]
        res = []
        for i in dist:
            res.append(points[i[1]])
        return res