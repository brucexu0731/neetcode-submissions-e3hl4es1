class Solution:
    def isPalindrome(self, s: str) -> bool:
        dic_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        valid = set(dic_string)
        ns = ""
        for i in range(len(s)):
            if s[i] in valid:
                ns += s[i]
        
        i = 0
        j = len(ns) - 1
        while i < j:
            if ns[i].lower() != ns[j].lower():
                return False
            i += 1
            j -= 1
        return True