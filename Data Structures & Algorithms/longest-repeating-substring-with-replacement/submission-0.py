class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        L = 0
        max_len = 0

        for R in range(len(s)):
            if s[R] not in freq:
                freq[s[R]] = 1
            else:
                freq[s[R]] += 1

            length = R - L + 1
            while length - k > self.getMajority(freq):
                print(freq[s[L]])
                freq[s[L]] -= 1
                L += 1
                length -= 1
            max_len = max(max_len, length)

        return max_len

    def getMajority (self, freq: dict) -> int:
        max_val = 0
        for value in freq.values():
            if value > max_val:
                max_val = value
        return max_val
