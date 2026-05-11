
class MyCalendar:
    
    def __init__(self):
        self.arr = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        print(self.arr)
        if not self.arr:
            self.arr.append((startTime, endTime))
            return True
        
        l, r = 0, len(self.arr) - 1

        while l <= r:
            m = (l + r) // 2
            s, e = self.arr[m]
            
            if endTime <= s:
                r = m - 1
            elif startTime >= e:
                l = m + 1
            else:
                return False
        
        self.arr.insert(l, (startTime, endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)