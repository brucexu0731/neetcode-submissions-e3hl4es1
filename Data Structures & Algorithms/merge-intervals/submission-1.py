class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        l = intervals[0][0]
        r = intervals[0][1]
        i = 0
        while i < len(intervals):
            if intervals[i][0] <= r:
                r = max(r, intervals[i][1])
            else:
                res.append([l, r])
                l = intervals[i][0]
                r = intervals[i][1]
            i += 1
        res.append([l, r])
        
        return res
