class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # at each position you can pick either ( or ) if there are less ) than (

        res = []
        def dfs(o, c, i, s):
            if i == n * 2:
                res.append(s)
                return 
            
            if o == n:
                return dfs(o, c + 1, i + 1, s + ')')
            
            if o == c:
                dfs(o + 1, c, i + 1, s + '(')
            else:
                # o > c, o can never be less than c in this implementation
                dfs(o + 1, c, i + 1, s + '(')
                dfs(o, c + 1, i + 1, s + ')')
        
        dfs(0, 0, 0, '')

        return res