class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {"[": "]", "(": ")", "{": "}"}
        for char in s:
            if char == "[" or char == "(" or char == "{":
                stack.append(char)
            else:
                if not stack:
                    return False
                c = stack.pop()
                if my_dict[c] != char:
                    return False 
        
        if stack:
            return False
        else: 
            return True