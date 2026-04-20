from collections import defaultdict 
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, course in prerequisites:
            adj[course].append(pre)
        
        prereqs = {}
        
        def dfs(course):
            if course in prereqs:
                return prereqs[course]
            
            pre = set()
            
            for prereq in adj[course]:
                pre.add(prereq)
                p = dfs(prereq)
                pre = pre.union(p)
            
            prereqs[course] = pre
            
            return pre
        
        for i in range(numCourses):
            prereqs[i] = dfs(i)

        res = []
        for p, c in queries:
            res.append(p in prereqs[c])
        
        return res
