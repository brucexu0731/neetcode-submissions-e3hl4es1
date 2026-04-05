from collections import deque
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.curr = self.q1

    def push(self, x: int) -> None:
        if len(self.q1) == 0:
            self.q1.append(x)
            while self.q2:
                self.q1.append(self.q2.popleft())
            self.curr = self.q1
        else:
            self.q2.append(x)
            while self.q1:
                self.q2.append(self.q1.popleft())
            self.curr = self.q2
        

    def pop(self) -> int:
        return self.curr.popleft()
        

    def top(self) -> int:
        return self.curr[0]
        

    def empty(self) -> bool:
        return len(self.curr) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()