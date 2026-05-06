class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        
        memo = {}

        def dfs(i, mm, nn):
            if i == len(strs):
                memo[(i, mm, nn)] = 0
                return 0
            if (i, mm, nn) in memo:
                return memo[(i, mm, nn)]
            
            s = strs[i]
            count0 = 0
            count1 = 0
            for c in s:
                if c == '0':
                    count0 += 1
                if c == '1':
                    count1 += 1
            
            with_str = 0
            if mm + count0 <= m and nn + count1 <= n:
                with_str = 1 + dfs(i + 1, mm + count0, nn + count1)
            without_str = dfs(i + 1, mm, nn)

            memo[(i, mm, nn)] = max(with_str, without_str)

            return max(with_str, without_str)
        
        return dfs(0, 0, 0)


        