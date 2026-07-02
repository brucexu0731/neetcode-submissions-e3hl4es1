class Solution:
    def checkValidString(self, s: str) -> bool:
        # can do dfs with backtracking, track the path with a stack
        # if encountering a *, then split into 3 branches 
        # 3^n 
        flex = []
        open_paren = []

        for i in range(len(s)):
            if s[i] == ")":
                if not open_paren and not flex:
                    return False
                elif not open_paren:
                    flex.pop()
                else:
                    open_paren.pop()
            
            if s[i] == "(":
                open_paren.append(i)
            
            if s[i] == "*":
                flex.append(i)
        
        if len(open_paren) > len(flex):
            return False

        while open_paren:
            if open_paren[-1] > flex[-1]:
                return False
            open_paren.pop()
            flex.pop()
        
        return True
