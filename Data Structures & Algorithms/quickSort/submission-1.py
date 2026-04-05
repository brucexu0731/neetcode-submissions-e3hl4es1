# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.qs(pairs, 0, len(pairs) - 1)
        
    def qs(self, pairs: List[Pair], s, e) -> List[Pair]: 
        if not pairs:
            return []
        if (e - s) <= 0:
            return pairs 

        #Swapping values smaller than pivot to the front 
        l = s
        for i in range(s, e):
            if pairs[i].key < pairs[e].key:
                temp = pairs[l]
                pairs[l] = pairs[i]
                pairs[i] = temp
                l += 1
        
        temp = pairs[l]
        pairs[l] = pairs[e]
        pairs[e] = temp

        self.qs(pairs, s, l - 1)
        self.qs(pairs, l + 1, e)

        return pairs


        