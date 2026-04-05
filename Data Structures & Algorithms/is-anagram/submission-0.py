from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) > len(t) or len(t) > len(s):
            return False

        d = defaultdict(int)

        for c in s:
            d[c] += 1
        
        for c in t:
            d[c] -= 1
            if d[c] < 0:
                return False
        
        return True
        