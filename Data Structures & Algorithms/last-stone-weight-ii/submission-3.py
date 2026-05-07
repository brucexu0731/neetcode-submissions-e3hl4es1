class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) // 2

        memo = {}

        def dfs(i, curr):
            if i == len(stones):
                return curr - target
            if curr >= target:
                return curr - target
            if (i, curr) in memo:
                return memo[(i, curr)]
            
            without = dfs(i + 1, curr)
            add = dfs(i + 1, curr + stones[i])

            if abs(without) == abs(add):
                res = without if without >= 0 else add
                memo[(i, curr)] = res
                return res
            elif abs(without) < abs(add):
                memo[(i, curr)] = without
                return without
            else:
                memo[(i, curr)] = add
                return add 
        
        partition1 = target + dfs(0, 0)
        partition2 = sum(stones) - partition1

        return abs(partition1 - partition2)
                


