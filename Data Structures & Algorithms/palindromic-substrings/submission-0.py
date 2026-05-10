class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0

        #check odd:
        for i in range(len(s)):
            l, r = i, i
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            res += count 
        
        #check even:
        for i in range(len(s)):
            l, r = i, i + 1
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            res += count 
        
        return res
        

