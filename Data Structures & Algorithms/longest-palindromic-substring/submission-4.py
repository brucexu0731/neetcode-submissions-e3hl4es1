class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_index = (0,0)
        max_len = 0

        #check odd
        for i in range(len(s)):
            l = i - 1
            r = i + 1
            curr = 1
            curr_str = (i, i)
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    curr += 2
                    curr_str = (l, r)
                    l -= 1
                    r += 1
                else:
                    break
            if curr > max_len:
                max_len = curr
                max_index = curr_str
        #check even 
        for i in range(len(s) - 1):
            l = i
            r = i + 1
            curr = 0
            curr_str = (i, i)
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    curr += 2
                    curr_str = (l, r)
                    l -= 1
                    r += 1
                else:
                    break
            if curr > max_len:
                max_len = curr
                max_index = curr_str

        l, r = max_index
        return s[l:r + 1]
