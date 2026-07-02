import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort the interval and queries
        # starting from the smallest interval and smallest query
        # we push the (length, end) of each interval into the heap that
        # starts before the current query, then we pop the heap until we get
        # the interval with the smallest length that ends after our current query
        # So each interval gets inserted once and only gets popped when it's out of range,
        # and it will be a candidate as long as it's in the heap

        intervals.sort()
        value_to_value = {}
        for i in range(len(queries)):
            value_to_value[queries[i]] = float('inf')
        
        queries_copy = queries[:]
        queries.sort()
        heap = []

        i = 0
        j = 0
        print(queries)
        while j < len(queries):
            s, e = (float('inf'), float('inf')) if i >= len(intervals) else intervals[i]
            #current interval length
            l = e - s + 1
            #current query number
            curr = queries[j]
            # print(s, e)
            # print(curr)
            #if current interval starts before current query, push into heap
            if s <= curr:
                heapq.heappush(heap, (l, e))
                i += 1
            #otherwise means we searched all intervals, go to next qeury value 
            else:
                j += 1
            
            #each iteration we need to pop out all the ranges that are invalid
            while heap and heap[0][1] < curr:
                heapq.heappop(heap)

            value_to_value[curr] = min(value_to_value[curr], float('inf') if not heap else heap[0][0])
            #print(heap)
        
        for i in range(len(queries_copy)):
            q = queries_copy[i]
            queries_copy[i] = -1 if value_to_value[q] == float('inf') else value_to_value[q]
        
        return queries_copy





