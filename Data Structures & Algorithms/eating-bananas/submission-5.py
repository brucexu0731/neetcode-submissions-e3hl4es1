class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)

        while l <= r:
            m = (l + r) // 2
            if self.eat(piles, h, m) > 0:
                r = m - 1
            else:
                l = m + 1
        return l

    def eat(self, piles, h, n) -> int:
        arr = piles[:]
        count = 0
        for num in arr:
            count += (num // n if num % n == 0 else num // n + 1)
        print("count", count)
        if count <= h:
            return 1
        else: 
            return -1 