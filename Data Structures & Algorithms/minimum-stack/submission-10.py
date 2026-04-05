class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float('inf')
        self.curr_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_val = min(val,self.min_val)
        self.curr_min.append(self.min_val)


    def pop(self) -> None:
        if not self.stack:
            return
        self.stack.pop()
        self.curr_min.pop()
        self.min_val = self.curr_min[-1] if self.curr_min else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.curr_min[-1]

