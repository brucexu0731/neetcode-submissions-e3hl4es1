class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = [x for x in range(1, n + 1)]
        def dfs(path, arr, length):
            if length == k:
                res.append(path)
            if not arr:
                return 
            
            for i in range(len(arr)):
                path.append(arr[i])
                arr_copy = arr[i + 1:] if i < len(arr) - 1 else []
                dfs(path[:], arr_copy, length + 1)
                path.pop()
        
        dfs([], nums, 0)
        return res
