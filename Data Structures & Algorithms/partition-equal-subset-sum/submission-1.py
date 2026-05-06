class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # we want the sum to be total / 2 -> if total is odd then false, if even we proceed
        total = sum(nums)
        if total % 2:
            return False 
        target = total // 2

        memo = {}
        
        def dfs(i, acc):
            if acc == target:
                memo[(i, acc)] = True 
                return True 
            if acc > target:
                memo[(i, acc)] = False
                return False 
            if i == len(nums):
                memo[(i, acc)] = False 
                return False 
            if (i, acc) in memo:
                return memo[(i, acc)]
            
            
            without_curr = dfs(i + 1, acc)
            with_curr = dfs(i + 1, acc + nums[i])
            res = without_curr or with_curr
            memo[(i, acc)] = res
            return res
         
        
        return dfs(0, 0)