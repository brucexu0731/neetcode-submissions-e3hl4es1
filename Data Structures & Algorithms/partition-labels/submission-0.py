from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        freq = defaultdict(int)

        for c in s:
            freq[c] += 1
        
        res = [-1]

        window = {}
        for i in range(len(s)):
            c = s[i]
            if c not in window:
                window[c] = 1
            else:
                window[c] += 1
            split = True
            for c, val in window.items():
                if val != freq[c]:
                    split = False
                    break 
            if split:
                res.append(i)
                window = {}
        
        return [res[i] - res[i - 1] for i in range(1, len(res))]