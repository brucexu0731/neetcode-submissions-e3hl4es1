class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # there are at most 500 intervals -> find the start, then merge all
        # the intervals before the end

        res = []
        s, e = newInterval
        
        i = 0
        while i < len(intervals) and s > intervals[i][1]:
            res.append(intervals[i])
            i += 1

        if i == len(intervals):
            res.append(newInterval)
            return res
        
        # we found the location to insert the interval 
        curr = intervals[i]
        merged_interval = [0, 0]
        merged_interval[0] = min(s, curr[0])

        while i < len(intervals) and e > intervals[i][1]:
            i += 1
        
        if i == len(intervals):
            merged_interval[1] = e
            res.append(merged_interval)
            return res
        
        curr = intervals[i]
        if e >= curr[0]:
            merged_interval[1] = max(e, curr[1])
            res.append(merged_interval)
            res.extend(intervals[i + 1 : ])
        else:
            merged_interval[1] = e
            res.append(merged_interval)
            res.extend(intervals[i : ])

        return res



