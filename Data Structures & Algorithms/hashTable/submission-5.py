class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val 

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity 
    

    def insert(self, key: int, value: int) -> None:

        i = key % self.capacity 
        while self.table[i]:
            if self.table[i].key == key:
                self.table[i] = Pair(key, value)
                return
            i += 1
        self.table[i] = Pair(key, value)
        self.size += 1

        if self.size * 2 >= self.capacity:
            self.resize()



    def get(self, key: int) -> int:
        i = key % self.capacity 
        while self.table[i]:
            if self.table[i].key == key:
                return self.table[i].val
            i += 1
        return -1


    def remove(self, key: int) -> bool:
        i = key % self.capacity 
        print(i)
        print(self.table)
        while self.table[i]:
            if self.table[i].key == key:
                self.table[i] = None 
                self.size -= 1
                return True 
            i += 1
        return False 

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity 


    def resize(self) -> None:
        self.capacity *= 2 
        arr = [None] * self.capacity 
        for pair in self.table:
            if pair:
                i = pair.key % self.capacity 
                while arr[i]:
                    i += 1
                arr[i] = pair
        self.table = arr 
        

