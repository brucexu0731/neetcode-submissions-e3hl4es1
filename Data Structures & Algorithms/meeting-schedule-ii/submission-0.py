"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda x: x.start)
        groups = []
        group_count = 0
        for i in intervals:
            if not groups or i.start < groups[0]:
                heapq.heappush(groups, i.end)
                group_count += 1
            else:
                heapq.heappop(groups)
                heapq.heappush(groups, i.end)
        
        return group_count

             