class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        # instead of manually checking the hashmap for all the counts
        # we can just store the last occurence of that element
        last = {}

        for i in range(len(s)):
            last[s[i]] = i
        
        res = [-1]

        window = {}
        window[s[0]] = 0
        for i in range(len(s)):
            c = s[i]
            window[c] = i
            if window[c] == last[c]:
                window.pop(c)
            if not window:
                res.append(i)
        
        return [res[i] - res[i - 1] for i in range(1, len(res))]