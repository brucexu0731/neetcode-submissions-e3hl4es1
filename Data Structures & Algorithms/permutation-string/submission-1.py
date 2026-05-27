class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        freq = [0] * 26
        for c in s1:
            freq[ord(c) - ord('a')] += 1
        freq = tuple(freq)
        print(freq)

        
        i = 0
        while i < len(s2):
            if freq[ord(s2[i]) - ord('a')] == 0:
                i += 1
                continue
            j = i
            freq_sub = [0] * 26
            while j < i + len(s1) and i + len(s1) <= len(s2):
                c = s2[j]
                freq_sub[ord(c) - ord('a')] += 1
                j += 1
            if tuple(freq_sub) == freq:
                return True
            else:
                i += 1
        
        return False
                

        
        
        
