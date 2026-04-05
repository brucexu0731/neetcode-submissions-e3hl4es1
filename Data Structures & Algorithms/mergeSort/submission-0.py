# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.ms(pairs, 0, len(pairs) - 1)
    
    def ms(self, arr, s, e):
        if (e - s) <= 0:
            return arr 
        
        m = (s + e) // 2 

        self.ms(arr, s, m)
        self.ms(arr, m + 1, e)

        self.merge(arr, s, m, e)

        return arr
    
    def merge(self, arr, s, m, e):
        L1 = arr[s : m + 1]
        L2 = arr[m + 1 : e + 1]
        k = s
        i = 0
        j = 0

        while i < len(L1) and j < len(L2) and k < e:
            if L1[i].key <= L2[j].key:
                arr[k] = L1[i]
                i += 1
            else:
                arr[k] = L2[j]
                j += 1
            k += 1
        
        while i < len(L1):
            arr[k] = L1[i]
            i += 1
            k += 1
        
        while j < len(L2):
            arr[k] = L2[j]
            j += 1
            k += 1


