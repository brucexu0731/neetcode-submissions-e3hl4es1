class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)
        
        L = 0
        max_len = 1
        prev = ''

        for R in range(1, len(arr)):
            if arr[R - 1] > arr[R]:
                curr = '>'
            elif arr[R - 1] < arr[R]:
                curr = '<'
            else:
                curr = '='

            if curr == '=':
                L = R 
                prev = ''
            elif curr == prev:
                L = R - 1
                prev = curr
            else:
                max_len = max(max_len, R - L + 1)
                prev = curr
            
            print(R, L)
        
        return max_len

            