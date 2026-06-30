class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        res = "" if x > 0 else "-"
        x = abs(x)
        while x:
            curr = x % 10
            res += str(curr)
            x //= 10

        
        if -2 ** 31 <= int(res) <= 2 ** 31 - 1:
            return int(res)
        else:
            return 0
        