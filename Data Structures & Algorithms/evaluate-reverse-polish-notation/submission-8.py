class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        ops = {'+', '-', '*', '/'}

        for c in tokens:
            if c not in ops:
                stack.append(int(c))
            else:
                num2 = stack.pop()
                num1 = stack.pop()

                if c == '+':
                    res = num1 + num2
                if c == '-':
                    res = num1 - num2
                if c == '*':
                    res = num1 * num2
                if c == '/':
                    res = num1 / num2
                    if res > 0:
                        res = math.floor(res)
                    else:
                        res = math.ceil(res)
                stack.append(res)
        
        return stack[0]

