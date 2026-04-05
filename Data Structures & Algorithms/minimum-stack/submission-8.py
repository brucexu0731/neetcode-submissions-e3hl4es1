class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = 2**32

    def push(self, val: int) -> None:
        (self.stack).append(val)
        if val < self.smallest:
            self.smallest = val
        

    def pop(self) -> None:
        num = (self.stack).pop()
        if self.stack == []:
            self.smallest = 2**32 
        elif num == self.smallest:
            self.smallest = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest
