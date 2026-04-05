class MinHeap:
    
    def __init__(self):
        self.heap = [0]
        

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1
        while self.heap[i] < self.heap[i // 2] and i > 1:
            curr = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = curr
            i = i // 2

    def percolate_down(self, i):
        while i * 2 < len(self.heap):
            if (i * 2 + 1) < len(self.heap) and self.heap[(i * 2 + 1)] < self.heap[(i * 2)] and\
            self.heap[i] > self.heap[i * 2 + 1]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2 + 1]
                self.heap[i * 2 + 1] = tmp
                i = i * 2 + 1
            elif self.heap[i] > self.heap[i * 2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2]
                self.heap[i * 2] = tmp
                i = i * 2
            else:
                break
    
    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop() 
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop() 
        
        self.percolate_down(1)

        return res 
        

    def top(self) -> int:
        if len(self.heap) <= 1:
            return -1
        else:
            return self.heap[1]
        

    def heapify(self, nums: List[int]) -> None:
        if nums == []:
            return
        nums.append(nums[0])
        nums[0] = 0
        self.heap = nums

        index = (len(self.heap) - 1) // 2

        while index > 0: 
            self.percolate_down(index)
            index -= 1
        
            
        
        