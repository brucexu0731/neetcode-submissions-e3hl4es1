class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        path = []

        def dfs(i, curr):
            if curr == target:
                res.append(path[:])
                return
            if i == len(candidates) or curr > target:
                return 

            level = set()
            for j in range(i, len(candidates)):
                val = candidates[j]
                if val not in level:
                    level.add(val)
                    path.append(val)
                    dfs(j + 1, curr + val)
                    path.pop()


        
        dfs(0, 0)
        return res