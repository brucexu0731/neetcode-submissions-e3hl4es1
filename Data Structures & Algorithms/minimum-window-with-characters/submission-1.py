from collections import defaultdict 
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # two pointers, sliding window 
        freq_t = defaultdict(int)
        for c in t:
            freq_t[c] += 1
        
        window = defaultdict(int)

        min_len = float('inf')
        res = (-1, -1)
        have = 0
        chars = len(freq_t)

        l, r = 0, 0

        while l < len(s) and r < len(s):
            c = s[r]
            if c in freq_t:
                window[c] += 1   
                if window[c] == freq_t[c]:
                    have += 1
            print(l, r)
            while have == chars:
                length = r - l + 1
                if length < min_len:
                    min_len = length 
                    res = (l, r)

                char = s[l]
                if char in window:
                    window[char] -= 1
                    if window[char] < freq_t[char]:
                        have -= 1

                l += 1
            
            r += 1
        print(res)
        l, r = res
        return "" if min_len == float('inf') else s[l : r + 1]





            

            