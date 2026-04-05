class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = []
        for i in range(n + 1):
            count = 0
            b = i
            while b:
                if (b % 2) == 1:
                    count += 1
                b = b >> 1
            arr.append(count)
        
        return arr