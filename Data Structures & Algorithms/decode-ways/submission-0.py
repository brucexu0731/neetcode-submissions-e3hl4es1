class Solution:
    def numDecodings(self, s: str) -> int:

        memo = {}
        def dfs(i):
            if i == len(s):
                return 1
            if i > len(s):
                return 0
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
            
            jump_one = dfs(i + 1)
            if int(s[i: i + 2]) > 26:
                jump_two = 0
            else:
                jump_two = dfs(i + 2)
            
            memo[i] = jump_one + jump_two
            return jump_one + jump_two
        
        return dfs(0)
            
            
