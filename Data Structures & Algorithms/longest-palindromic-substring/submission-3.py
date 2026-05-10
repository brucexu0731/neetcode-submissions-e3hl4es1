class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = ''
        max_len = 0

        #check odd
        for i in range(len(s)):
            l = i - 1
            r = i + 1
            curr = 1
            curr_str = s[i]
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    curr += 2
                    curr_str = s[l] + curr_str + s[r]
                    l -= 1
                    r += 1
                else:
                    break
            if curr > max_len:
                max_len = curr
                max_str = curr_str
        #check even 
        for i in range(len(s) - 1):
            l = i
            r = i + 1
            curr = 0
            curr_str = ''
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    curr += 2
                    curr_str = s[l] + curr_str + s[r]
                    l -= 1
                    r += 1
                else:
                    break
            if curr > max_len:
                max_len = curr
                max_str = curr_str

        return max_str
