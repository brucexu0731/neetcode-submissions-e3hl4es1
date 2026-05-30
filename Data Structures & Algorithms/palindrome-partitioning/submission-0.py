class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def dfs(i):

            if i == len(s):
                res.append(path[:])
            
            for j in range(i, len(s)):
                curr = s[i : j + 1]
                if self.isPalindrome(curr):
                    path.append(curr)
                    dfs(j + 1)
                    path.pop()
        
        dfs(0)
        return res


    
    def isPalindrome(self, s):
        l, r = 0, len(s) - 1

        while l <= r:
            if s[l] != s[r]:
                return False 
            l += 1
            r -= 1
        
        return True 