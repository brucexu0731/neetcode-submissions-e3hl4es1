# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return []
        
        def ms(arr):
            if len(arr) == 1:
                return arr
            
            m = len(arr) // 2
            return self.merge(ms(arr[:m]), ms(arr[m:]))
        
        return ms(pairs)

    def merge(self, a1, a2):
        i = 0
        j = 0
        arr = []
        print(a1)
        print(a2)
        while i < len(a1) and j < len(a2):
            if a1[i].key <= a2[j].key:
                arr.append(a1[i])
                i += 1
            else:
                arr.append(a2[j])
                j += 1
        if i < len(a1):
            arr += (a1[i:])
        else: 
            arr += (a2[j:])
        return arr


